
check = 0;
ntrial = 80;
winpos = zeros(1,ntrial/2);
losspos = zeros(1,ntrial/2);
side = round(rand(1,ntrial));
while sum(side)~=ntrial/2
    side = round(rand(1,ntrial));
end
%order = zeros(1,ntrial);
%order(1:40) = 1;

triger = 0;
while triger==0
    RAndom = round(1*randn(1,8)+5);
    if sum(RAndom(1:8))==ntrial/2 && ~any(RAndom<=2)
        triger = 1;
    end
end

pro = 0.85;
%pro = 0.15;
while check==0
    idxpos = 0;
for idxpro = 1:length(RAndom)
    pro = 1-pro;
    for k = 1:RAndom(idxpro)
        idxpos = idxpos+1;
        winpos(idxpos) = (rand<=pro);  
        %losspos(idxpos) = (rand<=pro);
    end
end
disp(sum(winpos));
%disp(sum(losspos));
if sum(winpos)==ntrial/4 %sum(losspos)==ntrial/4
    check=1;
end
end


