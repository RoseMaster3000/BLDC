function [tsunami] = UI_3DPlot_MATLAB(coordvars,ExcelFileName)
    tsunami = readtable(ExcelFileName);
    %coordvars = {'R_MagnetOutR_m','R_MagnetRadialLength_m','MagBackIronInR_m'};
    
    for i = 1:height(tsunami)
        % This matrix holds the data that you want to display on the datatip
        UserData(i,:) = [tsunami.(coordvars{1})(i),tsunami.(coordvars{2})(i),tsunami.(coordvars{3})(i)];
    end
    
    fig = figure;
    h = scatter3(tsunami.(coordvars{1}),tsunami.(coordvars{2}),tsunami.(coordvars{3}),'filled');
    xlabel((coordvars{1}), 'Interpreter', 'none');
    ylabel((coordvars{2}), 'Interpreter', 'none');
    zlabel((coordvars{3}), 'Interpreter', 'none');
    set(h,'UserData',UserData);                 % Upload the datatip data to the plot
    dcm_obj = datacursormode(fig);  
    set(dcm_obj,'UpdateFcn',@Func, 'Interpreter', 'none');% Point the data cursor to the custom datatip function
    datacursormode on     


function txt = Func(empt,event_obj)
    % Find the index of the actuator selected on the plot
    pos = get(event_obj,'Position')
    data = get(event_obj,'Target')
    xdata = get(data,'XData')
    ydata = get(data,'YData')
    index = find(xdata==pos(1) & ydata==pos(2))
    
    % Retrieve the user data created for this plot
    userdata = get(data,'UserData');
    idx1 = userdata(index,1);
    idx2 = userdata(index,2);
    idx3 = userdata(index,3);

    % Format the datatip text
    txt = {['Motor ',num2str(index)], ...
           [coordvars{1} ': ',num2str(idx1),''], ...
           [coordvars{2} ': ',num2str(idx2),''], ...
           [coordvars{3} ': ',num2str(idx3),'']};
end
end
