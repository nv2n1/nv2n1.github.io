---
title: "bspline(3)"
name: "bspline"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bspline/"
description: "QuantLib::BSpline – B-spline basis functions."
---

<p>QuantLib::BSpline &#8211; B-spline basis functions. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/bspline.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>BSpline</code> (<code>Natural</code> p, <code>Natural</code> n, const std::vector&lt; <code>Real</code> &gt; &amp;knots) </p>
<p> <code>Real</code> <code>operator()</code> (<code>Natural</code> i, <code>Real</code> x) const </p>
<h2>Detailed Description</h2>
<p>B-spline basis functions. </p>
<p> Follows treatment and notation from: </p>
<p> Weisstein, Eric W. &#8216;B-Spline.&#8217; From MathWorld&#8211;A Wolfram Web Resource. &lt;<a rel="nofollow" href="http://mathworld.wolfram.com/B-Spline.html">http://mathworld.wolfram.com/B-Spline.html</a>&gt; </p>
<p> $ (p+1) $-th order B-spline (or p degree polynomial) basis functions $ N_{i,p}(x), i = 0,1,2 </p>
<hr>
<p> knot vector of size $ p+n+2 $ defined at the increasingly sorted points $ (x_0, x_1 </p>
<hr>
<p>ratic B-spline has $ p=2 $, a cubic B-spline has $ p=3 $, etc. </p>
<p> The B-spline basis functions are defined recursively as follows: </p>
<p> [ xtrm{&nbsp;<wbr>if&nbsp;<wbr>} x_{i} </p>
<hr>
<p>xtrm{&nbsp;<wbr>otherwise} \ N_{i,p}(x) &amp;=&amp; N_{i,p-1}(x) ac{(x &#8211; x_{i})}{ (x_{i+p-1} &#8211; x_{i})} + N_{i+1,p-1}(x) ac{(x_{i+p} &#8211; x)}{(x_{i+p} &#8211; x_{i+1})} 
d{array} ] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
