function [mu sigma2] = estimateGaussian(X)
%ESTIMATEGAUSSIAN This function estimates the parameters of a 
%Gaussian distribution using the data in X
%   [mu sigma2] = estimateGaussian(X), 
%   The input X is the dataset with each n-dimensional data point in one row
%   The output is an n-dimensional vector mu, the mean of the data set
%   and the variances sigma^2, an n x 1 vector
% 

% Useful variables
[m, n] = size(X);
fprintf('size(X) is %s\n', mat2str(size(X)))
%fprintf('X is %s\n', mat2str(X))
% You should return these values correctly
mu = zeros(n, 1);
sigma2 = zeros(n, 1);
sigma = zeros(n, 1);
% ====================== YOUR CODE HERE ======================
% Instructions: Compute the mean of the data and the variances
%               In particular, mu(i) should contain the mean of
%               the data for the i-th feature and sigma2(i)
%               should contain variance of the i-th feature.
%

  mu = mean(X,1)'
  
%  for j=1:m
%    mu = mu + X(j,:)';
%  end
%  mu = mu/m
  
  for j=1:m
    fprintf('size(sigma) is %s\n', mat2str(size(sigma)))
    fprintf('size(X_j) is %s\n', mat2str(size(X(j,:)')))
    fprintf('size(mu) is %s\n', mat2str(size(mu)))
    sigma = sigma + (X(j,:)' - mu).^2
  end
  sigma2 = (sigma).*(1/m)
  






% =============================================================


end
