---
title: "exitflag(3)"
name: "exitflag"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exitflag/"
description: "QuantLib::NonLinearLeastSquare – Non-linear least-square method."
---

<p>QuantLib::NonLinearLeastSquare &#8211; Non-linear least-square method. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/leastsquare.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>NonLinearLeastSquare</code> (<code>Constraint</code> &amp;c, <code>Real</code> accuracy=1e-4, Size maxiter=100)<br />
 <i>Default constructor. </i><br />
 <code>NonLinearLeastSquare</code> (<code>Constraint</code> &amp;c, <code>Real</code> accuracy, Size maxiter, boost::shared_ptr&lt; <code>OptimizationMethod</code> &gt; om)<br />
 <i>Default constructor. </i><br />
 <code>~NonLinearLeastSquare</code> ()<br />
 <i>Destructor. </i><br />
 <code>Array</code> &amp; <code>perform</code> (<code>LeastSquareProblem</code> &amp;lsProblem)<br />
 <i>Solve least square problem using numerix solver. </i><br />
 void <code>setInitialValue</code> (const <code>Array</code> &amp;initialValue) </p>
<p> <code>Array</code> &amp; <code>results</code> ()<br />
 <i>return the results </i><br />
 <code>Real</code> <code>residualNorm</code> ()<br />
 <i>return the least square residual norm </i><br />
 <code>Real</code> <code>lastValue</code> ()<br />
 <i>return last function value </i><br />
 <code>Integer</code> <code>exitFlag</code> ()<br />
 <i>return exit flag </i><br />
 <code>Integer</code> <code>iterationsNumber</code> ()<br />
 <i>return the performed number of iterations </i></p>
<h2>Detailed Description</h2>
<p>Non-linear least-square method. </p>
<p> Using a given optimization algorithm (default is conjugate gradient), </p>
<p> [ min r(x) : x in R^n ].PP where $ r(x) = |f(x)|^2 $ is the Euclidean norm of $ f(x) $ for some vector-valued function $ f $ from $ R^n $ to $ R^m $, [ f = (f_1, &#8230;, f_m) ] with $ f_i(x) = b_i &#8211;<br />
 hi(x,t_i) $ where $ b $ is the vector of target data and $ phi $ is a scalar function. </p>
<p> Assuming the differentiability of $ f $, the gradient of $ r $ is defined by [ grad r(x) = f'(x)^t.f(x) ] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
