---
title: "qt_(3)"
name: "qt_"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qt_/"
description: "QuantLib::LineSearch – Base class for line search."
---

<p>QuantLib::LineSearch &#8211; Base class for line search. </p>
<h2>Synopsis</h2>
<pre><code>LineSearch (Real=0.0)


Default constructor.


virtual ~LineSearch ()


Destructor.


const Array &amp; lastX ()


return last x value


Real lastFunctionValue ()


return last cost function value


const Array &amp; lastGradient ()


return last gradient


Real lastGradientNorm2 ()


return square norm of last gradient


bool succeed ()



virtual Real operator() (Problem &amp;P, EndCriteria::Type &amp;ecType, const EndCriteria &amp;, const Real t_ini)=0


Perform line search.


Real update (Array &amp;params, const Array &amp;direction, Real beta, const Constraint &amp;constraint)



const Array &amp; searchDirection () const


current value of the search direction


Array &amp; searchDirection ()



Protected Attributes</code></pre>
<p> Inherited by <code>ArmijoLineSearch</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LineSearch (Real=0.0)


Default constructor.


virtual ~LineSearch ()


Destructor.


const Array &amp; lastX ()


return last x value


Real lastFunctionValue ()


return last cost function value


const Array &amp; lastGradient ()


return last gradient


Real lastGradientNorm2 ()


return square norm of last gradient


bool succeed ()



virtual Real operator() (Problem &amp;P, EndCriteria::Type &amp;ecType, const EndCriteria &amp;, const Real t_ini)=0


Perform line search.


Real update (Array &amp;params, const Array &amp;direction, Real beta, const Constraint &amp;constraint)



const Array &amp; searchDirection () const


current value of the search direction


Array &amp; searchDirection ()



Protected Attributes</code></pre>
<p> <code>Array</code> <code>searchDirection_</code><br />
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
<p>Base class for line search.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
