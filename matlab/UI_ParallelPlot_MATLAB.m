function [tsunami] = UI_ParallelPlot_MATLAB(coordvars,ExcelFileName)
    tsunami = readtable(ExcelFileName);
   % coordvars = {'R_MagnetRadialLength_m','R_MagnetOutR_m'};
    figure
    parallelplot(tsunami,'CoordinateVariables',coordvars,'Jitter',0);