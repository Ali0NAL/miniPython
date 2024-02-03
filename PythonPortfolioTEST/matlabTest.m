clear all
filename = 'De.xlsx';
data = xlsread(filename,1,'A:Y');
pn=20;
maxiter=20000; 
wmin=0; 
wmax=0.03;
yas=numel(data(1,:)); 
for i=1:pn
w(yas,1)=-1;
while w(yas,1)<0
for j=1:yas-1
w(j,1)=wmin+rand*(wmax-wmin);
end
w(yas,1)=1-(sum(w(1:(yas-1),1)));
end
ER=0;
for k=1:yas
ER=ER+w(k,1)*mean(data(:,k));
end
C=cov(data);
STD=zeros(yas,1);
for st1=1:yas
for st2=1:yas
if st1==st2
STD(st1,1)=STD(st1,1)+C(st1,st2)*w(st1,1)*w(st2,1);
else
STD(st1,1)=STD(st1,1)+2*C(st1,st2)*w(st1,1)*w(st2,1);
end
end
end
STSapma=(sum(STD(:,1)))^0.5;
fx=ER/STSapma;
OPT(i,1:yas)=w;
OPT(i,yas+1)=ER;
OPT(i,yas+2)=STSapma;
OPT(i,yas+3)=fx;
end
44
for iter=1:maxiter
[p,t]=max(OPT(:,yas+3));
[pe,te]=min(OPT(:,yas+3));
bestw=OPT(t,1:yas);
worstw=OPT(te,1:yas);
for i=1:pn
for j=1:yas-1
w(j,1) = OPT(i,j) + rand * (bestw(1,j) - OPT(i,j)) - rand * (worstw(1,j) - OPT(i,j));
if w(j,1)<0.001
w(j,1)=0;
end
end
w(yas,1)=1-(sum(w(1:(yas-1),1)));
ER=0;
for k=1:yas
ER=ER+w(k,1)*mean(data(:,k));
end
C=cov(data);
STD=zeros(yas,1);
for st1=1:yas
for st2=1:yas
if st1==st2
STD(st1,1)=STD(st1,1)+C(st1,st2)*w(st1,1)*w(st2,1);
else
STD(st1,1)=STD(st1,1)+2*C(st1,st2)*w(st1,1)*w(st2,1);
end
end
end
STSapma=(sum(STD(:,1)))^0.5;
fx=ER/STSapma;
for t=1:yas
if w(t,1)<0
fx=-1E-6;
end
end
OPT1(i,1:yas)=w;
OPT1(i,yas+1)=ER;
45
OPT1(i,yas+2)=STSapma;
OPT1(i,yas+3)=fx;
end
for i=1:pn
if OPT(i,yas+3)<OPT1(i,yas+3)
OPT(i,:)=OPT1(i,:);
end
end
end
