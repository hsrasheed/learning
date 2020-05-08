function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));
fprintf('size(Theta1) is %s\n', mat2str(size(Theta1)));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));
fprintf('size(Theta2) is %s\n', mat2str(size(Theta2)));

% Setup some useful variables
m = size(X, 1);
fprintf('\nm: %d\n',m);

% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

y_matrix = eye(num_labels)(y,:);
fprintf('size(y_matrix) is %s\n', mat2str(size(y_matrix)))
a1 = [ones(m,1) X];
z2 = a1*Theta1';
sig_z2 = sigmoid(z2);
a2 = [ones(size(sig_z2),1) sig_z2];
fprintf('size(a2) is %s\n', mat2str(size(a2)))
z3 = a2*Theta2';
a3 = sigmoid(z3);

hypothesis = a3;
term1 = -y_matrix(:)'*log(hypothesis)(:);
term2 = (1-y_matrix)(:)'*log(1-hypothesis)(:);
%theta(1) = 0
term3 = ((Theta1(:,2:end)(:)'*Theta1(:,2:end)(:)) + (Theta2(:,2:end)(:)'*Theta2(:,2:end)(:)))*(lambda/(2*m));
J = (term1 - term2)./m + term3;
%J = (term1 - term2)./m

d3 = a3 - y_matrix;
fprintf('size(d3) is %s\n', mat2str(size(d3)))
z2_grad = sigmoidGradient(z2);
fprintf('size(z2) is %s\n', mat2str(size(z2)))
d2 = (d3 * Theta2(:,2:end)).* z2_grad;
fprintf('size(d2) is %s\n', mat2str(size(d2)))
%nonconformant arguments (op1 is 16x4, op2 is 16x3)
Delta1 = d2' * a1;
fprintf('size(Delta1) is %s\n', mat2str(size(Delta1)))
Delta2 = d3' * a2;
fprintf('size(Delta2) is %s\n', mat2str(size(Delta2)))
Theta1_grad = (Delta1)./m;
Theta2_grad = (Delta2)./m;

Theta1(:,1) = 0
Theta2(:,1) = 0
Theta1_scale = Theta1*(lambda/m)
Theta2_scale = Theta2*(lambda/m)

Theta1_grad = Theta1_grad + Theta1_scale
Theta2_grad = Theta2_grad + Theta2_scale









% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
