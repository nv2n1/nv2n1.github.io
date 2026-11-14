---
title: "armijolinesearch(3)"
name: "armijolinesearch"
section: "3"
letter: "a"
url: "/docs/linux/man/3-armijolinesearch/"
description: "QuantLib::ArmijoLineSearch – Armijo line search."
---

<p>QuantLib::ArmijoLineSearch &#8211; Armijo line search. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/armijo.hpp&gt; </p>
<p> Inherits <code>QuantLib::LineSearch</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ArmijoLineSearch</code> (Real eps=1e-8, Real alpha=0.05, Real beta=0.65)<br />
 <i>Default constructor. </i><br />
 Real <code>operator()</code> (<code>Problem</code> &amp;P, EndCriteria::Type &amp;ecType, const <code>EndCriteria</code> &amp;, const Real t_ini)<br />
 <i>Perform line search. </i></p>
<h2>Detailed Description</h2>
<p>Armijo line search. </p>
<p> Let $ lpha $ and $ 2 scalars in $ [0,1] $. Let $ x $ be the current value of the unknown, $ d $ the search direction and $ t $ the step. Let $ f $ be the function to minimize. The line search stops when $ t $ verifies [ f(x + t dot d) &#8211; f(x) </p>
<hr>
<p>nt approximations, Optimization, volume 124 of Applied Mathematical Sciences, Springer-Verlag, NY, 1997) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
