---
title: "lastfunctionvalue(3)"
name: "lastfunctionvalue"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lastfunctionvalue/"
description: "QuantLib::LineSearch – Base class for line search."
---

<p>QuantLib::LineSearch &#8211; Base class for line search. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/linesearch.hpp&gt; </p>
<p> Inherited by <code>ArmijoLineSearch</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LineSearch</code> (Real=0.0)<br />
 <i>Default constructor. </i><br />
 virtual <code>~LineSearch</code> ()<br />
 <i>Destructor. </i><br />
 const <code>Array</code> &amp; <code>lastX</code> ()<br />
 <i>return last x value </i><br />
 Real <code>lastFunctionValue</code> ()<br />
 <i>return last cost function value </i><br />
 const <code>Array</code> &amp; <code>lastGradient</code> ()<br />
 <i>return last gradient </i><br />
 Real <code>lastGradientNorm2</code> ()<br />
 <i>return square norm of last gradient </i><br />
 bool <code>succeed</code> () </p>
<p> virtual Real <code>operator()</code> (<code>Problem</code> &amp;P, EndCriteria::Type &amp;ecType, const <code>EndCriteria</code> &amp;, const Real t_ini)=0<br />
 <i>Perform line search. </i><br />
 Real <code>update</code> (<code>Array</code> &amp;params, const <code>Array</code> &amp;direction, Real beta, const <code>Constraint</code> &amp;constraint) </p>
<p> const <code>Array</code> &amp; <code>searchDirection</code> () const<br />
 <i>current value of the search direction </i><br />
 <code>Array</code> &amp; <code>searchDirection</code> () </p>
<h3>Protected Attributes</h3>
<p><code>Array</code> <code>searchDirection_</code><br />
 <i>current values of the search direction </i><br />
 <code>Array</code> <code>xtd_</code><br />
 <i>new x and its gradient </i><br />
 <code>Array</code> <code>gradient_</code> </p>
<p> Real <code>qt_</code><br />
 <i>cost function value and gradient norm corresponding to xtd_ </i><br />
 Real <code>qpt_</code> </p>
<p> bool <code>succeed_</code><br />
 <i>flag to know if linesearch succeed </i></p>
<h2>Detailed Description</h2>
<p>Base class for line search. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
