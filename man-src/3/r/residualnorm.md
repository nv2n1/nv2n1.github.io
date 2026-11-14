---
title: "residualnorm(3)"
name: "residualnorm"
section: "3"
letter: "r"
url: "/docs/linux/man/3-residualnorm/"
---

QuantLib::NonLinearLeastSquare - Non-linear least-square method. 

<h2>Synopsis</h2>

<pre><code>NonLinearLeastSquare (Constraint &amp;c, Real accuracy=1e-4, Size maxiter=100)


Default constructor.


NonLinearLeastSquare (Constraint &amp;c, Real accuracy, Size maxiter, boost::shared_ptr&lt; OptimizationMethod &gt; om)


Default constructor.


~NonLinearLeastSquare ()


Destructor.


Array &amp; perform (LeastSquareProblem &amp;lsProblem)


Solve least square problem using numerix solver.


void setInitialValue (const Array &amp;initialValue)



Array &amp; results ()


return the results


Real residualNorm ()


return the least square residual norm


Real lastValue ()


return last function value


Integer exitFlag ()


return exit flag


Integer iterationsNumber ()


return the performed number of iterations</code></pre>

<h3>Public Member Functions</h3>

<pre><code>NonLinearLeastSquare (Constraint &amp;c, Real accuracy=1e-4, Size maxiter=100)


Default constructor.


NonLinearLeastSquare (Constraint &amp;c, Real accuracy, Size maxiter, boost::shared_ptr&lt; OptimizationMethod &gt; om)


Default constructor.


~NonLinearLeastSquare ()


Destructor.


Array &amp; perform (LeastSquareProblem &amp;lsProblem)


Solve least square problem using numerix solver.


void setInitialValue (const Array &amp;initialValue)



Array &amp; results ()


return the results


Real residualNorm ()


return the least square residual norm


Real lastValue ()


return last function value


Integer exitFlag ()


return exit flag


Integer iterationsNumber ()


return the performed number of iterations</code></pre>

<h2>Detailed Description</h2>

Non-linear least-square method. 

 Using a given optimization algorithm (default is conjugate gradient), 

 [ min r(x) : x in R^n ].PP where $ r(x) = |f(x)|^2 $ is the Euclidean norm of $ f(x) $ for some vector-valued function $ f $ from $ R^n $ to $ R^m $, [ f = (f_1, ..., f_m) ] with $ f_i(x) = b_i - 
 hi(x,t_i) $ where $ b $ is the vector of target data and $ phi $ is a scalar function. 

 Assuming the differentiability of $ f $, the gradient of $ r $ is defined by [ grad r(x) = f'(x)^t.f(x) ]

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
