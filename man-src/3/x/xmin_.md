---
title: "xmin_(3)"
name: "xmin_"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmin_/"
description: "QuantLib::Solver1D – Base class for 1-D solvers."
---

<p>QuantLib::Solver1D &#8211; Base class for 1-D solvers. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/math/solver1d.hpp&gt;</code></pre>
<p> Inherits <code>CuriouslyRecurringTemplate&lt; Impl &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Modifiers</code> </p>
<p> template&lt;class F &gt; Real <code>solve</code> (const F &amp;f, Real accuracy, Real guess, Real step) const </p>
<p> template&lt;class F &gt; Real <code>solve</code> (const F &amp;f, Real accuracy, Real guess, Real xMin, Real xMax) const </p>
<p> void <code>setMaxEvaluations</code> (Size evaluations) </p>
<p> void <code>setLowerBound</code> (Real lowerBound)<br />
 <i>sets the lower bound for the function domain </i><br />
 void <code>setUpperBound</code> (Real upperBound)<br />
 <i>sets the upper bound for the function domain </i></p>
<h3>Protected Attributes</h3>
<p>Real <code>root_</code> </p>
<p> Real <code>xMin_</code> </p>
<p> Real <code>xMax_</code> </p>
<p> Real <code>fxMin_</code> </p>
<p> Real <code>fxMax_</code> </p>
<p> Size <code>maxEvaluations_</code> </p>
<p> Size <code>evaluationNumber_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class Impl&gt; class QuantLib::Solver1D&lt; Impl &gt;</h3>
<p>Base class for 1-D solvers. </p>
<p> The implementation of this class uses the so-called &#8216;Barton-Nackman trick&#8217;, also known as &#8216;the curiously recurring template pattern&#8217;. Concrete solvers will be declared as: </p>
<pre> class Foo : public Solver1D&lt;Foo&gt; {
 public:
 ...
 template &lt;class F&gt;
 Real solveImpl(const F&amp; f, Real accuracy) const {
 ...
 }
 };</pre>
<p>&nbsp;<wbr>Before calling solveImpl, the base class will set its protected data members so that:</p>
<dl>
<dt>*</p>
<dd>xMin_ and xMax_ form a valid bracket;</p>
<dt>*</p>
<dd>fxMin_ and fxMax_ contain the values of the function in xMin_ and xMax_;</p>
<dt>*</p>
<dd>root_ is a valid initial guess. The implementation of solveImpl can safely assume all of the above.</dl>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>clean up the interface so that it is clear whether the accuracy is specified for $ x $ or $ f(x) $.</p>
<dt>*</p>
<dd>add target value (now the target value is 0.0)</dl>
</dl>
<h2>Member Function Documentation</h2>
<h3>Real solve (const F &amp; f, Real accuracy, Real guess, Real step) const</h3>
<p>This method returns the zero of the function $ f $, determined with the given accuracy $ \psilon $; depending on the particular solver, this might mean that the returned $ x $ is such that $ |f(x)| &lt; \psilon $, or that $ |x-lon $ where $ s the real zero. </p>
<p> This method contains a bracketing routine to which an initial guess must be supplied as well as a step used to scan the range of the possible bracketing values.</p>
<h3>Real solve (const F &amp; f, Real accuracy, Real guess, Real xMin, Real xMax) const</h3>
<p>This method returns the zero of the function $ f $, determined with the given accuracy $ \psilon $; depending on the particular solver, this might mean that the returned $ x $ is such that $ |f(x)| &lt; \psilon $, or that $ |x-lon $ where $ s the real zero. </p>
<p> An initial guess must be supplied, as well as two values $ x_mathrm{min} $ and $ x_mathrm{max} $ which must bracket the zero (i.e., either $ f(x_mathrm{min}) </p>
<hr>
<p> evaluations)&quot; </p>
<p> This method sets the maximum number of function evaluations for the bracketing routine. An error is thrown if a bracket is not found after this number of evaluations.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
