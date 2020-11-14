T = readtable('initial_dataset.csv');
A = table2array(T);
A(any(isnan(A),2),:) = [];
figure(1)
plot(A, 'x')