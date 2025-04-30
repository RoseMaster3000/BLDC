function [Outputs] = UI_MotorCalcs_MATLAB_Vectorized(vars_name, vars_value, consts_name, consts_value, MinTor, MagnetBr, MaxBMagnetIron, PresentBLaminationBackIron, SpeedReq, PostProcess,NumObj_)
% This function calculate the motor performance for a given set of
% parameters. This function is called by an optimizer. 
%
% Inputs: 
% vars_name: Names of the variable parameters. These parameters are purturebed by
% the optimizer
% vars_value: Values of the variable parameters
% consts_name:  Names of the constant parameters. 
% consts_value: Values of the constant parameters. 
%
% Outputs:
% Outputs: The objective paraemters to be minimized. 
%
  

for ii = 1:length(vars_value) 
    eval([vars_name{ii} '= cell2mat(vars_value(ii));']);
    
end
for ii = 1:length(consts_value) 
    eval([consts_name{ii} '= cell2mat(consts_value(ii));']);
end
I_SFLAG_ = 0; % If 1 Reduced Slot, if 0 Regular Number of Slots
Motor.Params.VacMagneticPerm_H_m = R_VacMagneticPerm;                   % Magnetic perm of a vacuum (H/m)
Motor.Params.SCL = 0.0254;                       % Scale Factor, inches to meter
Motor.Params.MagneticLossCoef1 = R_MagneticLossCoef1;                   % Magnetic loss coeff, a1
Motor.Params.MagneticLossCoef2 = R_MagneticLossCoef2;                    % Magnetic loss coeff, a2
Motor.Params.MagneticLossCoef3 = R_MagneticLossCoef3;                    % Magnetic loss coeff, a3
Motor.Params.FLDGAP = R_AirgapRadialLength;               % Fluid gap, (m)
Motor.Params.KINVSC = R_FluidKinVisc;                        % Fluid Kinematic Viscosity (cSt)
Motor.Params.SPGRAV = R_FluidSpecificGrav;                      % Fluid Specific gravity (-)
Motor.Params.FDENSTY = Motor.Params.SPGRAV * 998;             % Fluid density (kg/m^3)
Motor.Params.ASFLAG = I_SFLAG_;
Motor.Params.GearRatio = R_GearRatio;                      % Gear Ratio (-)

% Input parameters
Motor.Params.R_MtrLength_m = R_MtrLength;           % Motor length (m)
Motor.Params.R_LaminatR_m = R_LaminatR;       % Lamination radius (m)
Motor.Params.R_LaminatToothWedgeThickness_m = R_LaminatToothWedgeThickness;       % Lamination tooth tip and wedge thickness (m)
Motor.Params.R_MagnetOutR_m = R_MagnetOutR;       % Magnet outer radius (m)
Motor.Params.AirgapRadialLength_m = R_AirgapRadialLength;         % Radial length of airgap (m)
Motor.Params.R_MagnetRadialLength_m = R_MagnetRadialLength;         % Radial length of magnet (m)
Motor.Params.MagnetBackIronInnerR_m = R_MagnetBackIronInnerR;       % Magnet assembly backiron inner radius (m)
Motor.Params.MagnetBr_T = MagnetBr;               % Magnet Br (T)
Motor.Params.PresentBLaminationBackIron_T = PresentBLaminationBackIron;             % Present B in lamination back iron (T)
Motor.Params.PresentBLaminationToothIron_T = PresentBLaminationBackIron;             % Present B in lamination tooth iron (T)
Motor.Params.MaxBMagnetIron_T = MaxBMagnetIron;       % Maximum B in magnet assembly iron (T)
Motor.Params.WIRER = R_WireCopperR;      %  wire copper radius (m)
% Motor.Params.INS = char(Insulation);             % Single or Heavy insulation ('S','H')
% Motor.Params.INS =       'H'   ;      % Single or Heavy insulation ('S','H')
Motor.Params.InsulThick_m = R_InsulThick;
Motor.Params.FillFactor_ = R_FillFactor;               % Fill factor (-)
Motor.Params.LamSlotLinerThick_m = R_LamSlotLinerThick;       % Lamination slot liner thickness (m)
Motor.Params.RatedCurrent6Step_A = R_PhaseCurrentAmp*sqrt(3)/2;               % Rated current, 6-step (A)
Motor.Params.NP = double(I_PolePair)*2;               % # of magnet assembly poles (-)
% Motor.Params.NumLamTeeth_ = double(I_NumLaminatTeeth_3)*3;               % # of lamination teeth (-)
Motor.Params.NumLamTeeth_ = double(I_PolePair*2*3);               % # of lamination teeth (-)
Motor.Params.NumElecPhase_ = double(I_NumElecPhase);               % # of electrical phases (-)
Motor.Params.LoadInertia_ozin_s2 = 1385.43*R_LoadInertia;             % Load inertia reflected to motor (oz-in/sec^2)


% Power points for motor loss calcs
%MatMinTor_Nm = cell2mat(MinTor);
 MatMinTor_Nm = (MinTor);

CurrentMultiple = MatMinTor_Nm/max(MatMinTor_Nm);
Motor.Params.OperCurrent_A =     Motor.Params.RatedCurrent6Step_A*CurrentMultiple;      % Current points    [1,2,3] (A)
Motor.Params.MtrSpeed_rpm =     Motor.Params.GearRatio*(SpeedReq);      % Speed points      [1,2,3] (rpm)
Motor.Params.DUTCY =     100*ones(1,length(MinTor));       % Duty cycle points [1,2,3] (%)

% Design config flags
Motor.Params.FLAGIT =    false ;       % Integer number of turns, flag (bool)
Motor.Params.CON =       false ;       % Convert to US units where applicable (bool)

% Run motor design function
Motor = Func_DesignMotor(Motor);



if PostProcess == false
    if isfield(Motor,'Results')
        EffMin_ = min(Motor.Results.EffMtr_);
        EffMax_ = max(Motor.Results.EffMtr_);
        VDC = max(Motor.Results.VMag_VPhPkN)*sqrt(3);
        %Outputs = [double(-1*Motor.Results.TauShaft_Nm(1)*Motor.Params.GearRatio), double(-1*Motor.Results.TauShaft_Nm(2)*Motor.Params.GearRatio), double(-1*Motor.Results.TauShaft_Nm(3)*Motor.Params.GearRatio), double(Motor.Results.Weight_kg), double(-1*EffMax_), double(VMax_VPhPkN), double(Motor.Results.NumTurn), double(Motor.Results.MagVol_m3), double(-1*Motor.Results.TauShaft_Nm(4)*Motor.Params.GearRatio), double(-1*EffMin_)]; 


    Outputs = [double(-1*Motor.Results.TauShaft_Nm*Motor.Params.GearRatio), double(-1*Motor.Results.EffMtr_), double(Motor.Results.Weight_kg), double(Motor.Results.MagVol_m3), double(VDC), double(Motor.Results.NumTurn), double(Motor.Params.R_MtrLength_m), double(Motor.Params.R_LaminatR_m)]; 
    else
        %Motor.Params = rmfield(Motor.Params, {'OperCurrent_A','ASFLAG','NumElecPhase_'})
        %Motor.Params = rmfield(Motor.Params, 'MtrSpeed_rpm')
        %Motor.Params = rmfield(Motor.Params, 'DUTCY')
        %Motor.Params = rmfield(Motor.Params, 'INS')
        %Motor.Params = rmfield(Motor.Params, 'FLAGIT')
        %Motor.Params = rmfield(Motor.Params, 'CON')

        Outputs = [double(1e6+0.5)*ones(1,2*length(MatMinTor_Nm)+6)];
        % Outputs = double(Motor.Params.ErrorMessage);
    end    
else
    Motor.Results.VDC = max(Motor.Results.VMag_VPhPkN)*sqrt(3);
    Motor.Params = rmfield(Motor.Params,'MagnetBackIronInnerR_m'); % it is stored in the Motor.Results
    Motor.Results.MeanEffMtr_Percent = 100*mean(Motor.Results.EffMtr_);
    Motor.Results.MinEffMtr_Percent = 100*min(Motor.Results.EffMtr_);
    TrqMargin = 100*(Motor.Results.TauShaft_Nm*Motor.Params.GearRatio - MatMinTor_Nm)./MatMinTor_Nm;
    Motor.Results.MeanTrqMargin_Percent = mean(TrqMargin);
    Motor.Results.MinTrqMargin_Percent = min(TrqMargin);
    Outputs = Motor;
end
end


function [Motor] = Func_DesignMotor(Motor)

Motor.Params.ErrorMessage = 0;
% This routine controls the looping of the design process


%% Constants
VacMagneticPerm_H_m = Motor.Params.VacMagneticPerm_H_m;                   % Magnetic perm of a vacuum (H/m)
SCL = Motor.Params.SCL;                       % Scale Factor, inches to meter
MagneticLossCoef1 = Motor.Params.MagneticLossCoef1;                   % Magnetic loss coeff, a1
MagneticLossCoef2 = Motor.Params.MagneticLossCoef2;                    % Magnetic loss coeff, a2
MagneticLossCoef3 = Motor.Params.MagneticLossCoef3;                    % Magnetic loss coeff, a3
FLDGAP = Motor.Params.FLDGAP;               % Fluid gap, (m)
KINVSC = Motor.Params.KINVSC;                        % Fluid Kinematic Viscosity (cSt)
%SPGRAV = Motor.Params.SPGRAV;                      % Fluid Specific gravity (-)
FDENSTY = Motor.Params.FDENSTY;             % Fluid density (kg/m^3)
ASFLAG = Motor.Params.ASFLAG;
%InsulThick_m = 0.0035*SCL;                  % Wire insulation thickness (m)

%% Inputs
% Convert to SI units for all calcs

R_MtrLength_m = Motor.Params.R_MtrLength_m;           % Motor length (m)
R_LaminatR_m = Motor.Params.R_LaminatR_m;       % Lamination radius (m)
R_LaminatToothWedgeThickness_m = Motor.Params.R_LaminatToothWedgeThickness_m;       % Lamination tooth tip and wedge thickness (m)
R_MagnetOutR_m = Motor.Params.R_MagnetOutR_m;       % Magnet outer radius (m)
AirgapRadialLength_m = Motor.Params.AirgapRadialLength_m;         % Radial length of airgap (m)
R_MagnetRadialLength_m = Motor.Params.R_MagnetRadialLength_m;         % Radial length of magnet (m)
MagnetBackIronInnerR_m = Motor.Params.MagnetBackIronInnerR_m;       % Magnet assembly backiron inner radius (m)
MagnetBr_T = Motor.Params.MagnetBr_T;               % Magnet Br (T)
PresentBLaminationBackIron_T = Motor.Params.PresentBLaminationBackIron_T;             % Present B in lamination back iron (T)
PresentBLaminationToothIron_T = Motor.Params.PresentBLaminationToothIron_T;             % Present B in lamination tooth iron (T)
MaxBMagnetIron_T = Motor.Params.MaxBMagnetIron_T;       % Maximum B in magnet assembly iron (T)
WIRER = Motor.Params.WIRER;      % Present wire radius (m)
% INS = Motor.Params.INS;             % Single or Heavy insulation ('S','H')
InsulThick_m = Motor.Params.InsulThick_m;
FillFactor_ = Motor.Params.FillFactor_;               % Fill factor (-)
LamSlotLinerThick_m = Motor.Params.LamSlotLinerThick_m;       % Lamination slot liner thickness (m)
RatedCurrent6Step_A = Motor.Params.RatedCurrent6Step_A;               % Rated current, 6-step (A)
NP = Motor.Params.NP;               % # of magnet assembly poles (-)
NumLamTeeth_ = Motor.Params.NumLamTeeth_;               % # of lamination teeth (-)
NumElecPhase_ = Motor.Params.NumElecPhase_;               % # of electrical phases (-)
LoadInertia_ozin_s2 = Motor.Params.LoadInertia_ozin_s2;             % Load inertia reflected to motor (oz-in/sec^2)

% Power points for motor loss calcs
OperCurrent_A = Motor.Params.OperCurrent_A;         % Current points    [1,2,3] (A)
MtrSpeed_rpm = Motor.Params.MtrSpeed_rpm;         % Speed points      [1,2,3] (rpm)
DUTCY = Motor.Params.DUTCY;         % Duty cycle points [1,2,3] (%)

% Design config flags
FLAGIT = Motor.Params.FLAGIT;       % Integer number of turns, flag (bool)
CON = Motor.Params.CON;             % Convert to US units where applicable (bool)


%% Calculated values
RL1 = R_MagnetOutR_m + AirgapRadialLength_m;                     % Lamination tooth tip diameter
RL2 = RL1 + R_LaminatToothWedgeThickness_m;                    % Lamination slot ID. Allow for tooth tip and winding wedge thickness
GR = R_MagnetRadialLength_m / AirgapRadialLength_m;                       % Gap ratio of (R_MagnetRadialLength_m/AirgapRadialLength_m)
RM2 = R_MagnetOutR_m - R_MagnetRadialLength_m;                     % Magnet inner radius
RM3 = RM2;                          % Magnet assembly backiron outer radius (equal to RM2 usually)
VOLUMN = R_MtrLength_m * pi * (R_LaminatR_m^2);          % Volume
MVOL = R_MtrLength_m * pi * (R_MagnetOutR_m^2 - RM2^2);    % Magnet volume


%% Limit checks

if R_LaminatR_m > (10*R_MtrLength_m) || R_LaminatR_m < (0.1*R_MtrLength_m)        % Lam OD 10 times to 1/10 stack length, (aspect ratio check)
    fprintf('Exiting - stator L/D aspect ratio <> 10!')
    return;
end

% if VOLUMN < VOLMN || VOLUMN > VOLMX     % Motor volume is out of range
%     disp('Exiting - volume out of range!')
%     return;
% end

if R_MagnetOutR_m > (20*R_MtrLength_m) || R_MagnetOutR_m < (0.05*R_MtrLength_m)        % Lam OD 10 times to 1/10 stack length, (aspect ratio check)
    Motor.Params.ErrorMessage = 1%('Exiting - rotor/stator aspect ratio <> 20!')
    return;
end

if R_MagnetOutR_m >= R_LaminatR_m                           % Rotor is bigger than the stator
    Motor.Params.ErrorMessage = 2%('Exiting - rotor larger than stator!')
    return;
end



%% ---- Calculate motor design ---- %%

% This routine goes through an iterative method that converges on a
%   viable "magnetic design" for conventional BLDC motors.
% The design is a balance of iron area, (tooth and backiron), and
%   coil area, ((slot-insulators)*fill factor).
% A viable design is one where a geometery is developed that has just
%   enough iron in it to carry the flux that is generated by the magnet
%   and coil.

% STEP 1: Calculate the magnet area and flux generated by the magnet. This assumes
%         all MMF drops are in the airgap and the magnet. There are no drops in the
%         iron and the magnet has a recoil permeability close to air.

AMAG = 2 * pi * R_MtrLength_m * (R_MagnetOutR_m - R_MagnetRadialLength_m / 2) / NP;    % Average magnet area
FLUXM = MagnetBr_T * AMAG * (GR / (1 + GR));        % Flux generated in the airgap

% STEP 2: At this time we do not know the coil area, # of turns or the flux it will
%         generate. Therefore, to start, assume the coil will generate some perecntage
%         of the flux generate by the magnet.
%         To start assume the coil flux is .5% of the magnet flux. This is so we don't
%         jump out with negative slot area on early guesses of the the coil flux

FLUXC = FLUXM * 0.005; % Start with 0.5% of magnet flux

% Iterative design process
I = 0;
while I < 10000

    % STEP 3: Calculate the net flux that will be in each tooth. Note it is assumed
    %         that there is 2 phase on of a 3 phase, WYE, 6 state drive.
    %         Maximum total flux per tooth
    FLUXMT = (FLUXM + (2 * FLUXC)) / (real(NumLamTeeth_) / real(NP));

    % Step 4: We can now calculate the tooth width needed to carry the total flux per tooth

    TW = FLUXMT / (R_MtrLength_m * PresentBLaminationToothIron_T); % Magnet flux based on average magnet radius

    % STEP 5: We can also calculate the backiron thickness needed to carry the flux. Note
    %         it is assumed the total flux from one pole goes up the teeth and splits. One
    %         half going clockwise and the other half going counter clockwise.

    BTL = (FLUXM + (2 * FLUXC)) / (2 * R_MtrLength_m * PresentBLaminationBackIron_T);        % Lamination backiron thickness
    BTM = (FLUXM + (2 * FLUXC)) / (2 * R_MtrLength_m * MaxBMagnetIron_T);     % Magnet assembly backiron thickness
    RL3 = R_LaminatR_m - BTL;                                    % ID of lamination backiron

    % Check for valid dimensions
    if RL3 <= RL2
        Motor.Params.ErrorMessage = 3%('Exiting - RL3 < RL2!');
        return;
    end

    % STEP 6: Calculate the slot area available for windings per magnetic pole per phase
    %         Make sure the area is positive and that the slot opening has not closed up
    %
    %       AS=((PI*(RL3^2-RL1^2))-(TW*(RL3-RL1)*NumLamTeeth_))/(NP*NumElecPhase_) % Does not include slot liners
    %
    %       Rl2 compensates for the wedge, and liner in the front of the slot

    ASL = ((pi * (RL3^2 - RL2^2)) - (TW * (RL3 - RL2) * NumLamTeeth_)) / (NP * NumElecPhase_);    % Lamination slot area
    AS = ASL - (2 * (RL3 - RL2) * LamSlotLinerThick_m) - (((2 * pi * RL3 / NumLamTeeth_) - TW) * LamSlotLinerThick_m); % Winding Slot area

    % Check for valid slot area
    if AS <= 0
        Motor.Params.ErrorMessage = 4%  ('Exiting - slot area negative!');
        return;
    end

    % Calculate the slot opening width
    CIRCUM = 2 * pi * RL1;                              % Arc length of lamination ID
    SPAN = CIRCUM / NumLamTeeth_;                                 % Arc length of one tooth pitch
    SW = SPAN - TW;                                     % Approx width of slot opening

    % Check for valid slot opening
    if SW <= 0
        Motor.Params.ErrorMessage = 5%('Exiting - slot opening negative!');
        return;
    end

    % STEP 7: We have a valid slot area and opening now calculate the # of turns that
    %         will fit in the area.
    %
    %        WIREA=PI*(((WIRED(WS,1)+WIRED(WS,2))/2.)^2)   % Wire area  (INCORRECT)

    WireWInsR = WIRER + InsulThick_m / 2;        % Wire radius, heavy insulation
    % if INS == 'S'
    %     WireWInsR = WIRER + InsulThick_m / 4;    % Wire radius, single insulation
    % end
    WIREA = pi * (WireWInsR^2);                             % Wire area

    N = AS * FillFactor_ / (WIREA * 2);                          % Turns in available area

    % STEP 8: Based on the assumed coil flux we have a coil geometery, now calculate
    %         the actual coil flux density and compare.
    %         Way we have done it for years but AMAG does not include air gap.

    ACTFC = N * RatedCurrent6Step_A * VacMagneticPerm_H_m * AMAG / (AirgapRadialLength_m + R_MagnetRadialLength_m);             % Actual coil flux

    % Correct way but do I want to change??
    % AGAPAM=2.*PI*R_MtrLength_m*((RL1+R_MagnetOutR_m)/2.)/NP                  % TJH Change to include airgap 12-Apr-07
    % ACTFC=N*RatedCurrent6Step_A*VacMagneticPerm_H_m*AGAPAM/(AirgapRadialLength_m+R_MagnetRadialLength_m)                      % Actual coil flux

    % STEP 9: This is the design convergance check. If the assumed coil flux is not within
    %         .1% of the coil flux just calculated, the design is not valid. Adjust the
    %         assumed coil flux and GOTO STEP #3 and recalculate the design. If it is
    %         within .1%, the design is valid and drop to STEP 10.

    res = abs((FLUXC - ACTFC) / FLUXC);
    if res < 0.025
        break;  % Converged
    else
        FLUXC = FLUXC + (ACTFC - FLUXC) / 2;            % Update coil flux
    end

    I = I + 1;  % Count the number of iterations
    if I >= 9999
        Motor.Params.ErrorMessage = 6%('Exiting - Stuck in convergence loop!');
        return;
    end
end

% STEP 10: The design process started with given magnet assembly dimensions. Up to this point there
%          have been no checks to verify if the magnet assembly backiron is at a specified flux
%          density, MaxBMagnetIron_T.
%          Note: If MagnetBackIronInnerR_m equal to zero, calculate MagnetBackIronInnerR_m so flux in backiron equals MaxBMagnetIron_T.
%          This is flaged by MagnetBackIronInnerR_m <= 0. If MagnetBackIronInnerR_m > 0 user input a MagnetBackIronInnerR_m value and
%          calculate the rotor backiron flux density. (This is a bit of a kludge.)

if MagnetBackIronInnerR_m <= 0
    ARB = MaxBMagnetIron_T;                                       % Set flux to max
    MagnetBackIronInnerR_m = RM3 - BTM;                                    % Calculate MagnetBackIronInnerR_m based on max flux density
    if MagnetBackIronInnerR_m < 0
        MagnetBackIronInnerR_m = 0;
        Motor.Params.ErrorMessage = 7%('Exiting - MagnetBackIronInnerR_m less than zero!');
        return;
    end
    %MagnetBackIronInnerR_m = -MagnetBackIronInnerR_m;                                         % Negate MagnetBackIronInnerR_m for further calculations (why? -DCM)
    ACTRM4 = 0;
else
    ACTRM4 = RM3 - MagnetBackIronInnerR_m;                                 % Actual backiron thickness
    ARB = (FLUXM + (2 * FLUXC)) / (2 * R_MtrLength_m * ACTRM4);     % Actual flux density
    if ARB > MaxBMagnetIron_T
        Motor.Params.ErrorMessage = 8%('Exiting - magnet backiron flux density too high!');
        return;
    end
end



%%  ---- Calculate the motor performance specifications ---- %%
% OPTSPC()

% Initialize other local variables
RES = 0;        % Phase resistance of conventional configuration
%RESRS = 0;      % Phase resistance of reduced slot configuration
RESPHS = 0;     % Phase resistance depending on configuration
RSTURNS = 0;    % Number of reduced slot turns
QTURN = 0;      % Flag for 1/4 turns
QTURNR = 0;     % Correction ratio for 6 pole 9 slot alternating windings


%  If the integer turns flag is set, check to see if the calculated number of turns, N,
%    (a floating point number), is within +/- 2.5% of the integer, IN, that N would round to.
%  Note: If reduced slot, allow 1/2 turns (whole turns in reduced slot)
%     If reduced slot, allow 1/4 turns (half turns is reduced slot)
%     wind N+.5, N-.5, N+.5, N-.5..... for 4, 8, 12, 16, 20, 24 etc poles
%     wind N+.5, N-.5, N-.5, N+.5, N-.5, N-.5..... for 6, 18, 30 etc poles
%     (really N.33 winding so adjust parameters accordingly - SEE COMMENTS BELOW)

if FLAGIT
    if N < 0.975                % Less than one turn
        Motor.Params.ErrorMessage = 9%('Exiting - Less than one turn!')
        return;
    end

    IN = floor(N);              % Truncate N to get integer part

    %   Original code - gives me a headache
    %
    %	  REM1=(N)/IN                              % Fraction amount in percent
    %	  REM2=(N)/(IN+.5)                         % Fraction amount in percent
    %	  REM3=(N)/(IN+1)                          % Fraction amount in percent
    %
    %	  IF((REM1 >= 1.00) && (REM1 <= 1.02))     % 0 to 2% greater
    %	    GO TO 987
    %	  ELSEIF((ASFLAG ~= 0) &&  ((REM2 >= 0.98) && (REM2 <= 1.02))) % Allow a half turn
    %	  	GO TO 987
    %	  ELSE IF((REM3 >= 0.98) && (REM3 <= 1.00)) % 0 to 2% less
    %	  	GO TO 987
    %	  ELSE
    %	    RETURN
    %	  ENDIF

    SkipToCalcs = false;

    % New Code: Check all motor (standard and reduced slot) for integer turns
    QTURN = 0;                  % Flag for 1/4 turns (alternating reduced slot winding)
    RSTURNS = 2 * N;            % Reduced slot turns
    IN = floor(N);              % Truncate N
    REM1 = N - IN;              % Remainder of integer # of turns
    if REM1 >= 0.5
        IN = IN + 1;            % Increment if 0.5 or greater
    end
    REM2 = N / IN;
    if (REM2 >= 0.975) && (REM2 <= 1.025)  % 97.5-102.5 integer turns
        SkipToCalcs = true;     % Go to the calculation section
    end

    if ~SkipToCalcs
        % Further checks for reduced slot turns
        if (NumElecPhase_ == 3) && (ASFLAG ~= 0)
            RSTURNS = 2 * N;    % Reduced slot turns
            IN = floor(2 * N);
            REM1 = 2 * N - IN;  % Remainder of integer # of turns
            if REM1 >= 0.5
                IN = IN + 1;    % Increment if 0.5 or greater
            end
            REM2 = N / (IN / 2);
            if (REM2 >= 0.975) && (REM2 <= 1.025)
                SkipToCalcs = true;     % Go to the calculation section
            end
        end
    end

    %    Check for 1/4 turns (oddball alternating turn reduced slot motors)
    %    This is 1/2 turns for reduced slot (3 phase motors)
    %    For 4 pole 6 tooth (and any integer multipuls)
    %       This gives the following winding pattern:
    %       N+.5, N-.5, N+.5, N-.5, N+.5, N-.5....
    %       Fill calculation works out ok
    %    For 6 pole 9 tooth (and any integer multipuls not already covered by 4 pole integer multipuls)
    %       This gives the following winding pattern:
    %       N+.5, N-.5, N-.5, N+.5, N-.5, N-.5, N+.5, N-.5, N-.5...
    %       Fill calculation actually works out to a N+.333 average turn count
    %    This N+.333 needs to be accounted for

    if ~SkipToCalcs
        if (NumElecPhase_ == 3) && (ASFLAG ~= 0)
            RSTURNS = 2 * N;    % Reduced slot turns
            QTURN = floor(N);   % Truncate N
            IN = floor(4 * N);  % Truncate to get integer part
            REM1 = 4 * N - IN;  % Remainder of integer # of turns
            if REM1 >= 0.5
                IN = IN + 1;    % Increment if 0.5 or greater
            end
            REM2 = N / (IN / 4);
            if (REM2 >= 0.975) && (REM2 <= 1.025)
                SkipToCalcs = true;     % Go to the calculation section
            end
        end
    end

    if ~SkipToCalcs
        Motor.Params.ErrorMessage = 10%('Exiting - Not an integer number of turns!');
        return;                 % Not integer so return
    end
end

%%  Perform calculations

% Check for quarter turns and set up QTURNRatio parameter multiplier ratio
if (QTURN ~= 0) && any(ismember(NP, [6, 18, 30, 42, 54, 66, 78, 90]))
    RSTURNS = 2 * QTURN + 0.333;                % Reduced slot turns
    QTURNR = (QTURN + (0.333 / 2)) / N;         % For 6 poles and multipuls not covered by 4 pole multipliers
else
    QTURNR = 1.0;
end

% Calculate the motor parameters
% Torque Total Machine
TOR = (MagnetBr_T * NP * R_MagnetRadialLength_m * (N * QTURNR) * RatedCurrent6Step_A * (R_MagnetOutR_m + RM2) * R_MtrLength_m) / (R_MagnetRadialLength_m + AirgapRadialLength_m); % Newton-Meters - baseline Tim's code
%TOR = 3/2*(MagnetBr_T * NP * R_MagnetRadialLength_m * (N * QTURNR) * RatedCurrent6Step_A * (R_MagnetOutR_m + RM2) * R_MtrLength_m) / (R_MagnetRadialLength_m + AirgapRadialLength_m); % Newton-Meters

KT = TOR / RatedCurrent6Step_A;                                  % Newton-meters/amp
KB = KT;                                        % In metric Kt=Kb - baseline Tim's code
%KB = 2/3*KT;                                        % In metric Kt=Kb

% Resistance per phase
RPM = 1.8e-8 / (pi * (WIRER)^2);     % Resistance per meter of current wire size
% RSAVE = (RL3 + RL2) / 2;                      % Average radius of the lamination coil area
% NOT quite correct because more turns at RL3 than RL2
RSAVE = (RL3 + RL3 + RL2) / 3;                  % Better??

% From here on all winding calculations assume an "average turn" that exists at RSAVE
%
% The following calculates endturn lengths at the OUTSIDE of the bundle at RSAVE, or
%  in other word the LAST/OUTERMOST turn at average radius RSAVE. Calculating this endturn
%  length will give a high resistance for machine wound (tight) bundles but will compensate
%  for the extra bundle length of hand inserted bundles.

NWP = NumLamTeeth_ / (3 * NP);            % Not 1 for multi-teared windings

if NP == 2                                      % Model the endturn as a half circle.
    DCORD = 2 * RSAVE;                          % Circle diameter (DCORD), equal to the slot span of 1 winding pole.
else
    DCORD = 2 * (RSAVE * sin((2 * pi) / NP / 2));
end

RESA = RPM * 2 * NP * N * R_MtrLength_m;                    % Resistance of axial length
RES = RPM * 2 * NP * N * (R_MtrLength_m + (pi * DCORD / 2)); % Conventional resistance

WireAxialOverhang = 1*SCL;              %  wire axial overhang over stator stack length typical 0.5 - 1 inch
LengthOneTurn = 2*NWP*NP*(R_MtrLength_m+WireAxialOverhang) + 2*RSAVE*(2*pi/NP)*NP*NWP; % equation VII-32
RES = RPM*N*LengthOneTurn; 


if ASFLAG == 0
    LASFLAG = NumLamTeeth_ / 2;                           % If conventional
else
    LASFLAG = ASFLAG;                           % Actual reduced slot value
end

% Compensate the resistance for reduced slot count stators
% Compensate the resistance, (endturn region), for the "reduced" slot count stators
%   (This compensates for winding around a single tooth only!)
% Again initially assume hand inserted
DCORDRS = 2 * (RSAVE * sin((2 * pi) / LASFLAG / 2)); % DCORD equal to slot span of one tooth with outermost turn length.

% DCORDRS=(DCORD+(TW*(NumLamTeeth_/ASFLAG)))/2. (check eqn)    % For machine wound, calculate actual endturn
%                                                    % average DCORD at RSAVE. (Innermost + Outermost turns)/2

RESRSH = RPM * 2 * NP * (N * QTURNR) * (R_MtrLength_m + (pi * DCORDRS / 2)); % Reduced slot resistance


% Calculate a length needed for the endturns. Doing this here because it uses
%  the same types of assumptions as the endturn resistance calculation uses.
% Regular # of slots
ETL = NP * N * (pi * DCORD / 2);                    % EndTurn wire length for a phase
ETL = ETL * NumElecPhase_;                                     % Wire length of endturns for all phases
VET = ETL * (pi * (WIRER + InsulThick_m / 2)^2); % Volume of all endturns at one end, 100% fill
VET = VET / 0.375;                                  % Endturn volume required at 37.5% fill
ETA = pi * (((R_LaminatR_m + RL3) / 2)^2 - RL2^2);           % Area available for endturns
ETD = VET / ETA;                                    % Height of endturn volume

% Reduced slot, endturns around one tooth
ETDRS = (DCORDRS - (TW * (NumLamTeeth_ / LASFLAG))) / 2;      % 1/2 average SLOT width for bundle over end of tooth
ETDRS = ETDRS * 1.2;                                % Increase endturn space 20%

ZETD = (R_MtrLength_m + (2 * ETD));                             % Total Length including endturns
ZETDRS=(R_MtrLength_m + (2 * ETDRS));                           % Total Length including endturns


% Calculate inductance per phase (old method)
INDO = NP * N * FLUXC / RatedCurrent6Step_A;
INDO = INDO * (QTURNR^2);

% Correct the old method based on FEA correlation
if (NP / 2) == 2
    INDC = INDO * 1.69;
elseif (NP / 2) == 3
    INDC = INDO * 2.65;
elseif (NP / 2) == 4
    INDC = INDO * 3.91;
else
    INDC = 0;
end
INDC = INDC * (QTURNR^2);

% Inductance per phase (SRP new method)
% --- IND_SRP()
% This calculates the inductance using SRP's leakage additions.

% Initialize turns array
TURNS = zeros(250, 1);          % Number of turns for each tooth
PHI_CS = zeros(50, 1);          % Flux through each cross slot leakage path

% Calculate the number of turns for each tooth

for J = 1:NWP
    for I = J:(NumLamTeeth_/NP - J + 1)
        TURNS(I) = TURNS(I) + N;
    end
end

% Calculate the reluctance of each tooth
LGE = AirgapRadialLength_m;                       % Length of airgap
PC = R_MagnetRadialLength_m / AirgapRadialLength_m;                   % Permeance coefficient
RMAVE = (R_MagnetOutR_m + RM2) / 2;        % Average magnet radius
Rtooth = (LGE + PC * LGE) * NumLamTeeth_ / (VacMagneticPerm_H_m * 2 * pi * RMAVE * R_MtrLength_m);

% Calculate the component of inductance due to flux across the intended airgap
Lgap = 0;
for I = 1:NumLamTeeth_/NP
    Lgap = Lgap + TURNS(I)^2 / Rtooth;
end

% Calculate the reluctance of end turns
Rend = pi / (2 * VacMagneticPerm_H_m * TW);

% Calculate the component of inductance due to flux at the ends of
%  the motor- remember there are two ends
Lend = 0;
for I = 1:NumLamTeeth_/NP
    Lend = Lend + 2 * TURNS(I)^2 / Rend;
end

% Calculate the cross slot leakage reluctance
arg1 = abs(RL3 - TW * NumLamTeeth_ / (2 * pi));
arg2 = abs(RL2 - TW * NumLamTeeth_ / (2 * pi));
Rcs = 2 * pi / (VacMagneticPerm_H_m * R_MtrLength_m * NumLamTeeth_ * (log(arg1) - log(arg2)));

% Calculate the flux for each cross slot leakage path
PHI_CS(1) = 2 * TURNS(1) * RatedCurrent6Step_A / Rcs;
for I = 2:NWP
    PHI_CS(I) = (TURNS(I) - TURNS(I - 1)) * RatedCurrent6Step_A / Rcs;
end

% Calculate the Inductance contribution for each cross slot leakage path
% There are also two contributions for each because of symmetry
Lcs = 2 * TURNS(NWP) * PHI_CS(NWP) / RatedCurrent6Step_A;
for I = 1:(NWP - 1)
    Lcs = Lcs + 2 * TURNS(I) * (PHI_CS(I) - PHI_CS(I + 1)) / RatedCurrent6Step_A;
end

% Calculate the total inductance
INDP = NP * (Lgap + Lend + Lcs);
Minduct = 0.33 * INDP;
ind_ln2ln = 2 * (INDP + Minduct);

% ---- IND_SRP() end

INDP = INDP * (QTURNR^2);

% Inertia
DEN = 7250;                             % Kilograms/meter^3
JR = 0.5 * DEN * pi * R_MtrLength_m * (R_MagnetOutR_m^4);      % Kg-m^2
JR = JR / 9.807;                        % Kg-m-sec^2

% VOLUMN = R_MtrLength_m * pi * (R_LaminatR_m^2);            % Volume (calculated above)
% MVOL = R_MtrLength_m * pi * (R_MagnetOutR_m^2 - RM2^2);      % Magnet volume (calculated above)

% Stator volume, weight and surface area
AREA1 = pi * (R_LaminatR_m^2 - RL3^2);           % Backiron area
VOL1 = AREA1 * R_MtrLength_m;                       % Backiron volume
AREA2 = NumLamTeeth_ * TW * (RL3 - RL1);          % Tooth area
VOL2 = AREA2 * R_MtrLength_m;                       % Tooth volume
FeVOL = VOL1 + VOL2;                    % Total Lamination iron volume

WHT1 = VOL1 * 7650;                     % Backiron weight
WHT2 = VOL2 * 7650;                     % Tooth weight
FeWHT = WHT1 + WHT2;                    % Lamination weight

STAREA = R_MtrLength_m * (2 * pi * R_LaminatR_m) + 2 * (pi * R_LaminatR_m^2); % Stator Surface Area

% Copper Weight
CuWHT = RES / RPM;                      % Length of wire for 1 phase
CuWHT = CuWHT * (pi * (WIRER)^2); % Volume of Cu for 1 phase
CuWHT = CuWHT * NumElecPhase_ * 8906;              % All the phases and Cu Density Kg/m^3

% Rotor Weight
RWHT = R_MtrLength_m * pi * (R_MagnetOutR_m^2) * 7250;         % Rotor weight

% Total Weight
WHT = FeWHT + CuWHT + RWHT;

% Calculate the losses at each of the speed/current points
for I = 1:length(Motor.Params.MtrSpeed_rpm)
    % I^2R Losses
    WATR(I) = 2 * (OperCurrent_A(I)^2) * RES;   % I^2R Losses

    % Fe Losses
    FREQ = MtrSpeed_rpm(I) / 60 * (NP / 2);    % Magnetic frequency in Hertz
    WATMB = (WHT1 * 2.2) * MagneticLossCoef1 * (PresentBLaminationBackIron_T^MagneticLossCoef2) * (FREQ^MagneticLossCoef3); % Backiron losses  NOTE ** US UNITS Watts/L
    WATMT = (WHT2 * 2.2) * MagneticLossCoef1 * (PresentBLaminationToothIron_T^MagneticLossCoef2) * (FREQ^MagneticLossCoef3); % Tooth losses
    WATM(I) = WATMB + WATMT;            % Backiron and tooth losses
    FreqElec_rad_s = FREQ*2*pi;

    % Fluid Losses
    FreqMech_rad_s = MtrSpeed_rpm(I) / 60 * 2 * pi;      % Shaft Speed radians/sec
    DYNVISC = 0.000001 * FDENSTY * KINVSC; % Dynamic Viscosity

    % BFDAMP=2.*PI*DYNVISC*((2.*R_MagnetOutR_m)**3)*R_MtrLength_m/(4*FldGap) % Damping Coeff (N-M/rad/sec)
    %                                                   % Includes 2x fudgfe factor
    % BFTORQ=BFDAMP*FREQ                              % Damping Torque (N-M)

    % GE Model
    % Damping Torque (N-M)
    if MtrSpeed_rpm(I) <= 0
        BFTORQ = 0;
    else
        BFTORQ = fluidDrag(MtrSpeed_rpm(I), FDENSTY, DYNVISC, R_MagnetOutR_m, R_MtrLength_m, FLDGAP); % Fluid drag function
    end

    WATF(I) = 0.000739 * (141.6 * BFTORQ) * MtrSpeed_rpm(I);   % Fluid damping power losses, Watts

    % Total Losses Calculation
    WATT(I) = WATR(I) + WATM(I) + WATF(I); % Total losses (resistive, magnetic, fluid)

    TauEM_Nm(I) = KT*OperCurrent_A(I);  % EM Torque
    TauShaft_Nm(I) = TauEM_Nm(I) - (WATM(I) + WATF(I))/(FreqMech_rad_s+10*eps);
    PwrShaft_W(I) = TauShaft_Nm(I)*FreqMech_rad_s;

    % efficiency
    EffMtr_(I) =  PwrShaft_W(I)/(PwrShaft_W(I)+WATT(I)+10*eps); % Motor Efficiency

    % Voltage
    Iq_APkN(I) = OperCurrent_A(I)*2/sqrt(3);
    Id_APkN = 0;
    Vq_VPhPkN = Iq_APkN(I)*RES + FreqElec_rad_s*INDP*Id_APkN + FreqMech_rad_s*KB/sqrt(3);
    Vd_VPhPkN = Id_APkN*RES - FreqElec_rad_s*INDP*Iq_APkN(I);
    VMag_VPhPkN(I) = sqrt(Vq_VPhPkN^2 + Vd_VPhPkN^2);
    PwrElec_W(I) = (3/2*(Vq_VPhPkN*Iq_APkN(I)+Vd_VPhPkN*Id_APkN));
    Eff1_ = PwrShaft_W(I)/ PwrElec_W(I);

    % Voltage, different calcualtion
    Isixstep = OperCurrent_A(I);
    VsixstepL2LReal(I) = Isixstep*2*RES + FreqMech_rad_s*KB;
    VsixstepL2LImag(I) = ind_ln2ln*FreqElec_rad_s* Isixstep;
    VsixstepL2LMag(I) = sqrt(VsixstepL2LReal(I)^2+VsixstepL2LImag(I)^2);
    Eff2_ = PwrShaft_W(I)/(VsixstepL2LReal(I)*Isixstep+10*eps);

end

% Calculate totals
DCDOM = sum(DUTCY);         % Denominator of duty cycle ratio

%WATRT = sum(WATR.*DUTCY/DCDOM);  % Total resistive losses
WATRT = sum(WATR/4);  % Total resistive losses

%WATMT = sum(WATM.*DUTCY/DCDOM);    % Total magnetic losses
WATMT = sum(WATM/4);    % Total magnetic losses

%WATFT = sum(WATF.*DUTCY/DCDOM);        % Total fluid losses
WATFT = sum(WATF/4);        % Total fluid losses

%WATGT = sum(WATT.*DUTCY/DCDOM);    % Grand total losses
WATGT = sum(WATT/4);    % Grand total losses

WATFMT = WATFT + WATMT;                         % Fluid and magnetic losses

% FOM's (Figure of Merit)
ACCL = TOR / (JR + LoadInertia_ozin_s2);                        % Torque/inertia
TPSW = TOR / sqrt((RatedCurrent6Step_A^2) * RES);                % Torque/sqrt(watt)
CDEN = RatedCurrent6Step_A / (pi * ((WIRER)^2));      % Current density


% Output the results based on slot values
if ASFLAG == 0                                  % Regular number of slots
    RESPHS = RES;
    ZTOTAL = ZETD;
elseif ASFLAG ~= 0                              % Reduced slot, endturns around one tooth
    RESPHS = RESRSH;
    ZTOTAL = ZETDRS;
end

USZ = 0;
USRL4 = 0;
USRM1 = 0;   
% Convert to US units where applicable
if CON == true
    RL1 = RL1 / SCL;            % Convert Lamination tooth tip radius
    RL2 = RL2 / SCL;            % Convert Lamination slot radius
    RM2 = RM2 / SCL;            % Convert Magnet inner radius
    RM3 = RM3 / SCL;            % Convert Magnet inner radius
    MagnetBackIronInnerR_m = MagnetBackIronInnerR_m / SCL;            % Magnet ass backiron inner radius
    ACTRM4 = ACTRM4 / SCL;      % Actual backiron thickness
    TW = TW / SCL;              % Convert Tooth width
    BTL = BTL / SCL;            % Backiron thickness, lamination
    BTM = BTM / SCL;            % Backiron thickness, magnet assembly
    RL3 = RL3 / SCL;            % Lamination slot outer
    ASL = ASL / (SCL^2);        % Lamination slot area
    AS = AS / (SCL^2);          % Winding Slot area
    CIRCUM = CIRCUM / SCL;      % Arc length of lamination ID
    SPAN = SPAN / SCL;          % Arc length of one tooth pitch
    SW = SW / SCL;              % Approx width of slot opening
    WireWInsR = WireWInsR / SCL;        % Wire radius
    WIREA = WIREA / (SCL^2);    % Wire area

    TOR = TOR * 141.6;          % Convert torque to oz-in
    KT = KT * 141.6;            % Convert Kt to oz-in/amp
    JR = JR * 1389;             % Convert inertia to oz-in-sec^2
    ACCL = ACCL * 141.6 / 1389; % Adjust torque/inertia
    TPSW = TPSW * 141.6;        % Convert torque/sqrt(watt)
    VOLUMN = VOLUMN / (SCL^3);  % Convert volume
    MVOL = MVOL / (SCL^3);      % Convert magnet volume
    ASL = ASL / (SCL^2);        % Convert lam slot area
    AS = AS / (SCL^2);          % Convert winding slot area
    STAREA = STAREA / (SCL^2);  % Convert stator surface area
    WHT = WHT * 2.2;            % Convert total weight
    FeWHT = FeWHT * 2.2;        % Convert Fe weight
    CuWHT = CuWHT * 2.2;        % Convert Cu weight
    RWHT = RWHT * 2.2;          % Convert rotor weight
    CDEN = CDEN * (SCL^2);      % Convert current density
    ZETD = ZETD / SCL;          % Convert total length including endturns
    ZTOTAL = ZTOTAL / SCL;      % Convert total length including endturns

    % Additional conversions for output
    USZ = R_MtrLength_m / SCL;              % Convert length
    USRL4 = R_LaminatR_m / SCL;          % Convert diameter
    USRM1 = R_MagnetOutR_m / SCL;          % Convert magnet diameter

end


%     % Call the winding scale function if needed
%     if strcmp(FLAGOP, 'Y')
%         Nscale = (ASFLAG == 0) * N + (ASFLAG ~= 0) * 2 * N; % Determine number of turns
%         Func_Wscale(WS, INS, FillFactor_, Nscale, (RESPHS * RatedCurrent6Step_A^2), KT, KB, RESPHS, INDP, INDO, INDC, NP);
%     end

%WS = WS * 8; % Restore the wire size index

%% Results from motor performance specifications

Motor.Results.LamTTipR_m = RL1;            % Lamination tooth tip radius (in)                (m)
Motor.Results.LamSlotR_m = RL2;            % Lamination slot radius    (in)                  (m)
Motor.Results.MagInR_m = RM2;            % Magnet inner radius       (in)                  (m)
Motor.Results.MagBackIranOutR_m = RM3;            % Magnet ass backiron outer radius (in)           (m)
Motor.Results.MagBackIronInR_m = MagnetBackIronInnerR_m;            % Magnet ass backiron inner radius (in)           (m)
Motor.Results.ActualBackIronThick_m = ACTRM4;      % Actual backiron thickness (in)                  (m)
Motor.Results.ToothWidth_m = TW;              % Tooth width               (in)                  (m)
Motor.Results.GapRatio = GR;              % Gap ratio of (R_MagnetRadialLength_m/AirgapRadialLength_m
Motor.Results.BackIronThickLam_m = BTL;            % Backiron thickness, lamination (in)             (m)
Motor.Results.BackIronThickMag_m = BTM;            % Backiron thickness, magnet assembly (in)        (m)
Motor.Results.LamSlotOutR_m = RL3;            % Lamination slot outer     (in)                  (m)
Motor.Results.LamSlotA_m2 = ASL;            % Lamination slot area      (in^2)                (m^2)
Motor.Results.WindSlotA_m2 = AS;              % Winding Slot area         (in^2)                (m^2)
Motor.Results.ArcLamID_m = CIRCUM;      % Arc length of lamination ID (in)                (m)
Motor.Results.ArcToothPitch_m = SPAN;          % Arc length of one tooth pitch (in)              (m)
Motor.Results.SlotOpenWidth_m = SW;              % Approx width of slot opening (in)               (m)
Motor.Results.WireWInsR_m = WireWInsR;        % Wire radius with insulation               (in)                  (m)
Motor.Results.WIREA_m2 = WIREA;        % Wire area                 (in^2)                (m^2)
Motor.Results.NumTurn = N;                % # of turns                (-)
Motor.Results.ActualFluxDens = ARB;            % Actual flux density
Motor.Results.ActualCoilFlux = ACTFC;        % Actual coil flux
Motor.Results.RateTrqPPhase_Nm = TOR;            % Rated Torque per phase    (oz-in)               (N-m)
Motor.Results.KT_Nm_A = KT;              % Kt                        (oz-in/amp)           (N-m/amp)
Motor.Results.KB_VLLPkNs_rad = KB;              % Kb                        (V/(rad/s))
Motor.Results.InducPh_H = INDP;          % inductance, phase         (H)
Motor.Results.ResisPh_ohm = RESPHS;      % resistance, phase         (Ohm)
Motor.Results.Inertia_Nms2 = JR;              % inertia                   (oz-in-sec^2)         (N-m-sec^2)
Motor.Results.TrqPerInertia_1_s2 = ACCL;          % torque/inertia            (oz-in)/(oz-in-sec^2) (N-m)/(N-m-sec^2)
Motor.Results.TPSW = TPSW;          % torque/sqrt(watt)
Motor.Results.Volume_m3 = VOLUMN;      % volume                    (in^3)                (m^3)
Motor.Results.MagVol_m3 = MVOL;          % magnet volume             (in^3)                (m^3)
Motor.Results.LamSlotA_m2 = ASL;            % lam slot area             (in^2)                (m^2)
Motor.Results.WindSlotA_m2 = AS;              % winding slot area         (in^2)                (m^2)
Motor.Results.StatorSurfA_m2 = STAREA;      % stator surface area       (in^2)                (m^2)
Motor.Results.Weight_kg = WHT;            % total weight              (lbm)                 (kg)
Motor.Results.FeWeight_kg = FeWHT;        % Fe weight                 (lbm)                 (kg)
Motor.Results.CuWeight_kg = CuWHT;        % Cu weight                 (lbm)                 (kg)
Motor.Results.RotWeight_kg = RWHT;          % rotor weight              (lbm)                 (kg)
Motor.Results.CurrDens_A_m2 = CDEN;          % current density           (A/in^2)              (A/m^2)
Motor.Results.ZETD = ZETD;          % total length including endturns (in)            (m)
Motor.Results.ZTOTAL = ZTOTAL;      % total length including endturns (in)            (m)
% Motor.Results.USZ = USZ;            % length                    (in)                  (m)
% Motor.Results.USRL4 = USRL4;        % diameter                  (in)                  (m)
% Motor.Results.USRM1 = USRM1;        % magnet diameter           (in)                  (m)
Motor.Results.ResLoss_W = WATR;        % Total resistive losses    (W)
Motor.Results.BackIronLoss_W = WATM;        % Total magnetic losses     (W)
Motor.Results.FluidLoss_W = WATF;        % Total fluid losses        (W)
Motor.Results.MeanResLoss_W = WATRT;        % Total resistive losses    (W)
Motor.Results.MeanBackIronLoss_W = WATMT;        % Total magnetic losses     (W)
Motor.Results.MeanFluidLoss_W = WATFT;        % Total fluid losses        (W)
Motor.Results.MeanWATFMT = WATFMT;      % Fluid and magnetic losses (W)
Motor.Results.MeanTotalLoss_W = WATGT;        % Grand total losses        (W)
Motor.Results.EffMtr_ = EffMtr_;
Motor.Results.PwrShaft_W = PwrShaft_W;
Motor.Results.TauShaft_Nm = TauShaft_Nm; 
Motor.Results.VMag_VPhPkN = VMag_VPhPkN;
Motor.Results.PwrElec_W = PwrElec_W;
Motor.Results.VsixstepL2LMag = VsixstepL2LMag;
Motor.Results.VsixstepL2LReal = VsixstepL2LReal;
Motor.Results.VsixstepL2LImag = VsixstepL2LImag;
Motor.Results.Iq_APkN = Iq_APkN;
Motor.Results.MaxTotalLoss_W = max(WATT);
end




function fluidDragTorque = fluidDrag(Speed, Density, DynVisc, Radius, Length, airgap)
% This function calculates the fluid drag torque in the air gap, units are N-m,
% based on the GE model.
% Input parameters:
% Speed    - Speed in rpm
% Density  - Density of fluid in Kg/m^3
% DynVisc  - Dynamic viscosity of fluid in Kg/(m-s)
% Radius   - Radius of rotor in meters
% Length   - Length of rotor in meters
% airgap   - Radial air gap of motor in meters

% Convert speed from rpm to radians per second
Spd = Speed / 60;  % Convert rpm to revolutions per second

% Convert inputs to local variables
Radiusm = Radius;
Lengthm = Length;
Airgapm = airgap;
Airgapratio = Airgapm / Radiusm;

% Calculate Taylor number components
TaylorA = Density * 2 * pi * Spd * Radiusm * Airgapm / DynVisc;
TaylorB = sqrt(Airgapm / Radiusm);
Taylor = TaylorA * TaylorB;

% Calculate TN1 and TN2
TN1 = (2 * (1 + Airgapratio)^2) / (TaylorA * (1 + 0.5 * Airgapratio));
TN2 = 0.11 * (Taylor^0.854) / TaylorA;
TN3 = 0.476 * sqrt(TaylorB) / sqrt(TaylorA);
TN4 = calcTurbFric(TN3, TaylorA, Airgapratio);  % Call to the auxiliary function

% Determine the value based on Taylor number
if Taylor < 41.3
    Value = TN1;
elseif Taylor < 63.0
    Value = TN2;
elseif TN3 > TN4
    Value = TN3;
else
    Value = TN4;
end

% Calculate fluid drag torque in N-m
fluidDragTorque = Value * pi * Lengthm * Density * ...
    (Radiusm^4) * (2 * pi * Spd)^2;
end

function fric = calcTurbFric(iVal, Tna, AgRatio)
% This function is used by FluidDrag to calculate the turbulence friction coefficient.
% iVal is the initial guess at the friction coefficient.
% Tna is the "a" part of the Taylor number calculation.
% AgRatio is the airgap over the rotor radius ratio.

% Initialize variables
iterateCount = 0;
inc = 0.001;
fric1 = iVal;
fric2 = iVal * (1 + inc);

while true
    % Calculate Taylor numbers
    CTF1 = exp(((1 + AgRatio) / (1.2 * sqrt(2 * fric1 * (1 + AgRatio / 2)))) - ...
        log(sqrt(fric1 / 2) / (2 * (1 + AgRatio))) - 8.58);
    CTF2 = exp(((1 + AgRatio) / (1.2 * sqrt(2 * fric2 * (1 + AgRatio / 2)))) - ...
        log(sqrt(fric2 / 2) / (2 * (1 + AgRatio))) - 8.58);

    error1 = (CTF1 - Tna);
    error2 = (CTF2 - Tna);

    % Check for convergence
    if abs(error1) < 0.00001
        break;  % Converged
    end

    if abs(error1) < abs(error2)
        % fric1 was a better guess
        ratio = -error1 / error2;
        fric1 = fric1 * (1 + (inc * ratio));
        fric2 = fric1 * (1 + inc);
    else
        % fric2 was a better guess
        ratio = -error1 / error2;
        fric1 = fric1 * (1 - (inc * ratio));
        fric2 = fric1 * (1 + inc);
    end

    iterateCount = iterateCount + 1;
    if iterateCount > 1000000
        fric1 = -1;  % Indicate failure to converge
        break;
    end
end

% Return the calculated friction coefficient
fric = fric1;
end
