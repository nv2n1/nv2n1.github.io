---
title: "setcurrentvalue(3)"
name: "setcurrentvalue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setcurrentvalue/"
description: "QuantLib::Problem – Constrained optimization problem."
---

<p>QuantLib::Problem &#8211; Constrained optimization problem. </p>
<h2>Synopsis</h2>
<pre><code>Problem (CostFunction &amp;costFunction, Constraint &amp;constraint, const Array &amp;initialValue=Array())


default constructor


void reset ()



Real value (const Array &amp;x)


call cost function computation and increment evaluation counter


Disposable&lt; Array &gt; values (const Array &amp;x)


call cost values computation and increment evaluation counter


void gradient (Array &amp;grad_f, const Array &amp;x)


call cost function gradient computation and increment


Real valueAndGradient (Array &amp;grad_f, const Array &amp;x)


call cost function computation and it gradient


Constraint &amp; constraint () const


Constraint.


CostFunction &amp; costFunction () const


Cost function.


void setCurrentValue (const Array &amp;currentValue)



const Array &amp; currentValue () const


current value of the local minimum


void setFunctionValue (Real functionValue)



Real functionValue () const


value of cost function


void setGradientNormValue (Real squaredNorm)



Real gradientNormValue () const


value of cost function gradient norm


Integer functionEvaluation () const


number of evaluation of cost function


Integer gradientEvaluation () const


number of evaluation of cost function gradient



Protected Attributes</code></pre>
<h3>Public Member Functions</h3>
<pre><code>Problem (CostFunction &amp;costFunction, Constraint &amp;constraint, const Array &amp;initialValue=Array())


default constructor


void reset ()



Real value (const Array &amp;x)


call cost function computation and increment evaluation counter


Disposable&lt; Array &gt; values (const Array &amp;x)


call cost values computation and increment evaluation counter


void gradient (Array &amp;grad_f, const Array &amp;x)


call cost function gradient computation and increment


Real valueAndGradient (Array &amp;grad_f, const Array &amp;x)


call cost function computation and it gradient


Constraint &amp; constraint () const


Constraint.


CostFunction &amp; costFunction () const


Cost function.


void setCurrentValue (const Array &amp;currentValue)



const Array &amp; currentValue () const


current value of the local minimum


void setFunctionValue (Real functionValue)



Real functionValue () const


value of cost function


void setGradientNormValue (Real squaredNorm)



Real gradientNormValue () const


value of cost function gradient norm


Integer functionEvaluation () const


number of evaluation of cost function


Integer gradientEvaluation () const


number of evaluation of cost function gradient



Protected Attributes</code></pre>
<p> <code>CostFunction</code> &amp; <code>costFunction_</code><br />
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
 <code>Integer</code> <code>gradientEvaluation_</code></p>
<h2>Detailed Description</h2>
<p>Constrained optimization problem.</p>
<h2>Member Function Documentation</h2>
<h3>void reset ()</h3>
<p><code>Warning</code></p>
<dl>
<dd>it does not reset the current minumum to any initial value</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
