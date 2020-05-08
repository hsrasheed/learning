function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters
  %fprintf('Iteration:\n', iter);
    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
  num_parameters = length(theta);
  for j = 1:num_parameters
    cost_derivative = 0;
    for i=1:m, 
      x = X(i,:);
      cost_derivative = cost_derivative + (theta'*x' - y(i));
    end;

    cost_derivative = cost_derivative/m;
    theta(j) = theta(j) - alpha*cost_derivative*x(j);

    % ============================================================
  end
    % Save the cost J in every iteration
  current_cost = computeCost(X, y, theta);
  J_history(iter) = current_cost;
  fprintf('Iteration: %d - Cost computed = %f\n', iter, current_cost);
  %fprintf('Program paused. Press enter to continue.\n');
  %pause;
end
  
end
