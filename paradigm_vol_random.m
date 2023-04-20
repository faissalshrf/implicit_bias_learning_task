
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
    Random = round(4*randn(1,9)+13.5);
    if sum(Random)==ntrial && ~any(Random<=2)
        if ~any(Random(1:4)>10) && ~any(Random(5:8)<18)
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
    proran = round(3*randn(1,9)+13.5);
    if sum(proran)==ntrial
        tripro=1;
    end
end

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
plot(1:idxdif(1), PRO(1:idxdif(1)),'-g','linewidth',3);
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
        plot(stpt:edpt, PRO(stpt:edpt),'--r','linewidth',3);
    else
        plot(stpt:edpt, PRO(stpt:edpt),'-g','linewidth',3);
    end 
end
ylim([0,1])

        












