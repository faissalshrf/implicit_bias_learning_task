
check = 0;

while check==0
triger = 0;
ntrial = 60;
winpos = round(rand(1,ntrial));
losspos = round(rand(1,ntrial));
side = round(rand(1,ntrial));
order = zeros(1,ntrial);

while triger == 0
    random = randn(1,9);
    random = random+6.5;
    for k = 1:length(random)
        random(k) = round(random(k));
    end
    if sum(random) == ntrial && random(end)<6
        triger=1;
    end
    
end

idxorder = 0;
vorder = 0;
for idxran = 1:length(random)
    vorder = 1-vorder;
    for k = 1:random(idxran)
        idxorder = idxorder+1;
        order(idxorder)= vorder;
    end
end

flag = zeros(1,4); % wn, wl, ln, lw
idxdif = find(order(1:end-1)~=order(2:end));
for k = 1:length(idxdif)
    idx = idxdif(k);
    if order(idx)==1 % w
        if losspos(idx+1) == winpos(idx) % wl
            flag(2)=flag(2)+1;
        elseif losspos(idx+1) ~= winpos(idx) % wn
            flag(1)=flag(1)+1;
        end
    elseif order(idx)==0 % l 
        if winpos(idx+1)==losspos(idx) % lw
            flag(4)=flag(4)+1;
        elseif winpos(idx+1) ~= losspos(idx) % ln
            flag(3)=flag(3)+1;
        end
    end
end

if sum(winpos)==ntrial/2 && sum(losspos)==ntrial/2 && sum(side)==ntrial/2 && sum(order)==ntrial/2
    check = isequal(flag,[2,2,2,2]);
end
end
            


