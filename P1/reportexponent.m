A = csvread('AnonymizedEdgeList.csv');
dim = max(max(A));
[E_Size, junk] = size(A);
adj = sparse(A(:,1), A(:,2), ones(E_Size,1), dim, dim, E_Size);

indeg = sum(adj);
outdeg = sum(adj');


indeg_hist = hist(indeg,dim);

outdeg_hist =hist(outdeg,dim);

logx=log(indeg_hist);
logx(logx<0)=0;
logy=log(1:dim);
points_in_deg = polyfit (logx,logy,1);

logx=log(outdeg_hist);
logx(logx<0)=0;
logy=log(1:dim);
points_out_deg = polyfit (logx,logy,1);

fprintf('Indegrees Exponent is %g, Intercept is %g \n',log(points_in_deg(2)),(points_in_deg(1)));
fprintf('Outdegrees Exponent is %g, Intercept is %g \n',log(points_out_deg(2)),(points_out_deg(1)));
% logx=log(A(:,1));
% logy=log(A(:,2));
% p=polyfit(logx,logy,1);
% plot(logx,logy,'bo');
% axis equal square
% grid
% xlabel('log(x)');
% ylabel('log(y)');
% k=p(1);
% loga=p(2);
% a=exp(loga);
% hold on;
% plot(logx,k*logx+loga,'g');
% legend('Data',sprintf('y=%.3f{}log(x)+log(%.3f)',k,a));
% figure
% plot(x,y,'bo');
% xlabel('x');
% ylabel('y');
% axis equal square
% grid
% hold on; 
% plot(x,a*x.^k,'g')
% legend('Data',sprintf('y=%.3f{}x^{%.3f}',a,k));