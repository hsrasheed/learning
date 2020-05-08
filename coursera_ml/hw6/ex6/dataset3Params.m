function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

C_list = [0.01, 0.03, 0.1, 0.3, 1];
s_list = [0.01, 0.03, 0.1, 0.];

% create a blank results matrix
results = zeros(length(C_list) * length(s_list), 3)   

row = 1;
%fprintf('size(X) is %s\n', mat2str(size(X)))
%fprintf('size(y) is %s\n', size(y))
for C_val = C_list
    for sigma_val = s_list
      fprintf('C is %f\n', C_val)
      fprintf('sigma is %f\n', sigma_val)
        % your code goes here to train using C_val and sigma_val
        %    and compute the validation set errors 'err_val'
        
        size_x = size(X);
        model= svmTrain(X, y, C_val, @(x1, x2) gaussianKernel(x1, x2, sigma_val)); 
        %model = svmTrain([ones(size_x,1) X], y, C_val, gaussianKernel([ones(size_x,1) X],y,sigma_val));
        predictions = svmPredict(model, Xval);
        
        %err_val = yval-predictions;
        err_val = mean(double(predictions ~= yval));
        fprintf('Error was %f\n', err_val)
        % save the results in the matrix
        results(row,:) = [C_val sigma_val err_val];
        row = row + 1;
    endfor
endfor

% use the min() function on the results matrix to find 
%   the C and sigma values that give the lowest validation error

[lowest_error, lowest_error_row] = min(results(:,3))

C = results(lowest_error_row,1)
sigma = results(lowest_error_row,2)


% =========================================================================

end
