% Before running the code please type clear all and clc in command window.
% Sometimes eigenvalue might be negative because the determinent of adj is
% 0 as it is a sparse matrix .Please run code until the values of eigenvector
%are not poisitive. Sorry for inconvenience . Thank you
clear all;
clc;

load adj;
adj = adj';
[V,D] = eigs(adj);

[eig_max, ind] = max(diag(D));

eig_vect = V(:,ind);

[eig_vect_sorted, ind_sorted] = sort(eig_vect);

disp(eig_vect_sorted(191771));
disp(ind_sorted(191771));
disp(eig_vect_sorted(191770));
disp(ind_sorted(191770));
disp(eig_vect_sorted(191769));
disp(ind_sorted(191769));