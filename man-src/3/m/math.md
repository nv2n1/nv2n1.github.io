---
title: "math(3)"
name: "math"
section: "3"
letter: "m"
url: "/docs/linux/man/3-math/"
description: "Math tools – Math facilities of the library include:"
---

<h2 class="name">NAME</h2>
<p> Math tools &#8211; Math facilities of the library include: </p>
<h2>Pseudo-random number and low-discrepancy sequence generators</h2>
<p> Implementations of pseudo-random number and low-discrepancy sequence generators. They share the ql/RandomNumbers directory.</p>
<h2>One-dimensional solvers</h2>
<p> The abstract class <code>QuantLib::Solver1D</code> provides the interface for one-dimensional solvers which can find the zeroes of a given function. </p>
<p> A number of such solvers is contained in the ql/Solvers1D directory. </p>
<p> The implementation of the algorithms was inspired by &#8216;Numerical Recipes in C&#8217;, 2nd edition, Press, Teukolsky, Vetterling, Flannery &#8211; Chapter 9 </p>
<p> Some work is needed to resolve the ambiguity of the root finding accuracy defition: for some algorithms it is the x-accuracy, for others it is f(x)-accuracy.</p>
<h2>Optimizers</h2>
<p> The optimization framework (corresponding to the ql/Optimization directory) implements some multi-dimensional minimizing methods. The function to be minimized is to be derived from the <code>QuantLib::CostFunction</code> base class (if the gradient is not analytically implemented, it will be computed numerically). </p>
<p> <code>The simplex method</code>.RS 4 </p>
<p> This method, implemented in <code>QuantLib::Simplex</code>, is rather raw and requires quite a lot of computing resources, but it has the advantage that it does not need any evaluation of the cost function&#8217;s gradient, and that it is quite easily implemented. First, we must choose N+1 starting points, given here by a starting point $ mathbf{P}_{0} $ and N points such that [ mathbf{P}_{mathbf{i}}=mathbf{P}_{0}+</p>
<hr>
<p> mathbf{e}_{mathbf{i}}, ] where $ </p>
<hr>
<p> $ is the problem&#8217;s characteristic length scale). These points will form a geometrical form called simplex. The principle of the downhill simplex method is, at each iteration, to move the worst point (highest cost function value) through the opposite face to a better point. When the simplex seems to be constrained in a valley, it will be contracted downhill, keeping the best point unchanged. </p>
<p> <code>The conjugate gradient method</code>.RS 4 We&#8217;ll now continue with a bit more sophisticated method, implemented in <code>QuantLib::ConjugateGradient</code> . At each step, we minimize (using Armijo&#8217;s line search algorithm, implemented in <code>QuantLib::ArmijoLineSearch</code>) the function along a line defined by [ mathbf{d_i} = -bla f(mathbf{x_i})+ac{</p>
<hr>
<p>rt bla f(mathbf{x_i})ightVert ^{2}}{</p>
<hr>
<p>rt bla f(mathbf{x_{i-1}})ightVert ^{2}}mathbf{d_{i-1}}, ] [ mathbf{d}_{0} = -bla f(mathbf{x}_{0}). ] </p>
<p> As we can see, this optimization method requires the knowledge of the gradient of the cost function. See <code>QuantLib::ConjugateGradient</code> .</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
