
ntrial = 120;
order = zeros(1,ntrial);
side = round(rand(1,ntrial));
while sum(side)~=ntrial/2
    side = round(rand(1,ntrial));
end

winpos = zeros(1,ntrial);
losspos = zeros(1,ntrial);


triger = 0;
while triger==0
    Random = round(1*randn(1,20)+6);
    if sum(Random)==ntrial && ~any(Random<=2)
        if ~any(Random(1:10)>7) && ~any(Random(11:19)<6)
            triger=1;
        end
    end
if triger==1
triger = 0;
idxorder = 0;
vorder = 0;
for idxran = 1:length(Random)
    vorder = 1-vorder;
    for k = 1:Random(idxran)
        idxorder = idxorder+1;
        order(idxorder)= vorder;
    end
end
disp(sum(order));
if sum(order)==ntrial/2
    triger=1;
end
end
end

tripro = 0;
while tripro==0
    proran = round(3*randn(1,10)+12);
    if sum(proran)==ntrial
        tripro=1;
    end
end


% proran = [13,12,17,17,14,10,10,14,13];
% Random = [7,8,8,9,18,20,19,23,8];
idxpos = 0;
pro = 0.15;
PRO = zeros(1,ntrial);

CHECK = 0;
while CHECK==0
for idxpro = 1:length(proran)
    pro = 1-pro;
    for k = 1:proran(idxpro)
        idxpos = idxpos+1;
        winpos(idxpos) = (rand<=pro);
        losspos(idxpos) = (rand<=pro);
        PRO(idxpos)=pro;
    end
end
disp(sum(winpos));
disp(sum(losspos));
idxpos = 0;
if sum(winpos)==ntrial/2 && sum(losspos)==ntrial/2
    CHECK=1;
end
end


idxdif = find(order(1:end-1)~=order(2:end));
plot(80+1:80+idxdif(1), PRO(1:idxdif(1)),'-g','linewidth',3);
for i = 1:length(idxdif)
    %xline(idxdif(i));
    hold on
    stpt = idxdif(i);
    if i==length(idxdif)
        edpt = length(PRO);
    else
        edpt = idxdif(i+1);
    end
    if mod(i,2)==1 
        plot(stpt+80:edpt+80, PRO(stpt:edpt),'--r','linewidth',3);
    else
        plot(stpt+80:edpt+80, PRO(stpt:edpt),'-g','linewidth',3);
    end 
end
hold on
ylim([0,1])



        
%%

idxpb = [201:440];
winPRO = zeros(1,length(idxpb));
winPRO([1:13,30:52,181:199,221:240]) = 0.15;
winPRO([14:29,53:80,161:180,200:220]) = 0.85;
winPRO([81:160]) = 0.5;
lossPRO = zeros(1,length(idxpb));
lossPRO([1:19,50:62,97:111,134:160]) = 0.85;
lossPRO([20:49,63:96,112:133]) = 0.15;
lossPRO([161:240]) = 0.5;
plot(idxpb,winPRO,'-g','linewidth',3);
hold on
plot(idxpb,lossPRO,'--r','linewidth',3);

hold on


idxpb = [1:40];
winPRO = zeros(1,length(idxpb));
winPRO([1:7,22:29]) = 0.15;
winPRO([8:21,30:40]) = 0.85;
plot(idxpb,winPRO,'-g','linewidth',3);
lossPRO = zeros(1,length(idxpb));
lossPRO([12:18,30:40]) = 0.15;
lossPRO([1:11,19:29]) = 0.85;
plot(idxpb+40,lossPRO,'--r','linewidth',3);

xline(40.5,'--k','linewidth',5);
xline(80.5,'--k','linewidth',5);
xline(120.5+80,'--k','linewidth',5);
xline(200.5+80,'--k','linewidth',5);
xline(280.5+80,'--k','linewidth',5);

xlim([0,440]);






