---
title: "currentvalue_(3)"
name: "currentvalue_"
section: "3"
letter: "c"
url: "/docs/linux/man/3-currentvalue_/"
description: "QuantLib::Problem – Constrained optimization problem."
---

<p>QuantLib::Problem &#8211; Constrained optimization problem. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/problem.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Problem</code> (<code>CostFunction</code> &amp;costFunction, <code>Constraint</code> &amp;constraint, const <code>Array</code> &amp;initialValue=<code>Array</code>())<br />
 <i>default constructor </i><br />
 void <code>reset</code> () </p>
<p> <code>Real</code> <code>value</code> (const <code>Array</code> &amp;x)<br />
 <i>call cost function computation and increment evaluation counter </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>values</code> (const <code>Array</code> &amp;x)<br />
 <i>call cost values computation and increment evaluation counter </i><br />
 void <code>gradient</code> (<code>Array</code> &amp;grad_f, const <code>Array</code> &amp;x)<br />
 <i>call cost function gradient computation and increment </i><br />
 <code>Real</code> <code>valueAndGradient</code> (<code>Array</code> &amp;grad_f, const <code>Array</code> &amp;x)<br />
 <i>call cost function computation and it gradient </i><br />
 <code>Constraint</code> &amp; <code>constraint</code> () const<br />
 <i></i><code>Constraint</code>.<br />
 <code>CostFunction</code> &amp; <code>costFunction</code> () const<br />
 <i>Cost function. </i><br />
 void <code>setCurrentValue</code> (const <code>Array</code> &amp;currentValue) </p>
<p> const <code>Array</code> &amp; <code>currentValue</code> () const<br />
 <i>current value of the local minimum </i><br />
 void <code>setFunctionValue</code> (<code>Real</code> functionValue) </p>
<p> <code>Real</code> <code>functionValue</code> () const<br />
 <i>value of cost function </i><br />
 void <code>setGradientNormValue</code> (<code>Real</code> squaredNorm) </p>
<p> <code>Real</code> <code>gradientNormValue</code> () const<br />
 <i>value of cost function gradient norm </i><br />
 <code>Integer</code> <code>functionEvaluation</code> () const<br />
 <i>number of evaluation of cost function </i><br />
 <code>Integer</code> <code>gradientEvaluation</code> () const<br />
 <i>number of evaluation of cost function gradient </i></p>
<h3>Protected Attributes</h3>
<p><code>CostFunction</code> &amp; <code>costFunction_</code><br />
 <i>Unconstrained cost function. </i><br />
 <code>Constraint</code> &amp; <code>constraint_</code><br />
 <i></i><code>Constraint</code>.<br />
 <code>Array</code> <code>currentValue_</code><br />
 <i>current value of the local minimum </i><br />
 <code>Real</code> <code>functionValue_</code><br />
 <i>function and gradient norm values at the curentValue_ (i.e. the last step) </i><br />
 <code>Real</code> <code>squaredNorm_</code> </p>
<p> <code>Integer</code> <code>functionEvaluation_</code><br />
 <i>number of evaluation of cost function and its gradient </i><br />
 <code>Integer</code> <code>gradientEvaluation_</code> </p>
<h2>Detailed Description</h2>
<p>Constrained optimization problem.</p>
<h2>Member Function Documentation</h2>
<h3>void reset ()</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>it does not reset the current minumum to any initial value</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
