g = 9.81;
m = 4.5;
l = 0.554;
b = 1.2; 

theta_0 = 20*(pi/180);
theta_dot_0 = 0 ;

omega_n = sqrt((4*m*l*g - (b^2)/(2*m*l)));
a_0 = -b/(m*l);
a_1 = theta_0;
a_2 = (theta_dot_0 + a_0*theta_0)/omega_n;

theta_t = @(t) exp(a_0 .* t) .* (a_1 .* cos(omega_n .* t) + a_2 .* sin(omega_n .* t));

% Plot the function over a range of time values
t_values = 0:0.01:10;  % Create a vector of time values
y_values = theta_t(t_values);  % Evaluate the function at each time value
plot(t_values, y_values);
xlabel('Time (t)');
ylabel('theta(t)');
title('Time-Dependent Function theta(t)');
grid on;

