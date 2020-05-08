function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %

    descent_param = 0;

    for i=1:m, 
        x = X(i,:);
        descent_param = descent_param + (theta'*x' - y(i));
    end;

    descent_param = descent_param/(m);

    theta(1) = theta(1) - alpha*descent_param*x(1)

    theta(2) = theta(2) - alpha*descent_param*x(2)

    % ============================================================
    current_cost = computeCost(X, y, theta);
    fprintf('Iteration: %d - Cost computed = %f\n', iter, current_cost);
    % Save the cost J in every iteration    
    J_history(iter) = current_cost;
    %fprintf('Program paused. Press enter to continue.\n');
    %pause;
end

end