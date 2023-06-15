
check = 0;
ntrial = 120;
winpos = zeros(1,ntrial/2);
losspos = zeros(1,ntrial/2);
side = round(rand(1,ntrial));
while sum(side)~=ntrial/2
    side = round(rand(1,ntrial));
end

triger = 0;
while triger==0
    RAndom = round(1*randn(1,10)+6);
    if sum(RAndom(1:10))==ntrial/2 && ~any(RAndom<=3)
        triger = 1;
    end
end

pro = 0.85;
%pro = 0.15;
check = 0;
while check==0
    idxpos = 0;
for idxpro = 1:length(RAndom)
    pro = 1-pro;
    milestone = idxpos;
    repeat=0;
    while repeat==0
        idxpos = milestone;
    for k = 1:RAndom(idxpro)
        idxpos = idxpos+1;
        winpos(idxpos) = (rand<=pro);
        if k==1 && idxpos~=1 && winpos(idxpos)==winpos(idxpos-1)
            winpos(idxpos) = 1-winpos(idxpos);
        end
        %losspos(idxpos) = (rand<=pro);
    end
    if winpos(idxpos)==winpos(idxpos-1) && abs(winpos(idxpos)-pro)<0.5 
        repeat = 1;
    end
    end
end
disp(sum(winpos));
%disp(sum(losspos));
if sum(winpos)==ntrial/4 %sum(losspos)==ntrial/4
    check=1;
end
end

%%


