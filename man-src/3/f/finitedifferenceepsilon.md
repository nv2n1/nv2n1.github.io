---
title: "finitedifferenceepsilon(3)"
name: "finitedifferenceepsilon"
section: "3"
letter: "f"
url: "/docs/linux/man/3-finitedifferenceepsilon/"
description: "QuantLib::CostFunction – Cost function abstract class for optimization problem."
---

<p>QuantLib::CostFunction &#8211; Cost function abstract class for optimization problem. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/costfunction.hpp&gt; </p>
<p> Inherited by AbcdError, SABRError, FrobeniusCostFunction, <code>LeastSquareFunction</code>, PenaltyFunction&lt; Curve &gt;, and <code>ProjectedCostFunction</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>Real</code> <code>value</code> (const <code>Array</code> &amp;x) const =0<br />
 <i>method to overload to compute the cost function value in x </i><br />
 virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>values</code> (const <code>Array</code> &amp;x) const =0<br />
 <i>method to overload to compute the cost function values in x </i><br />
 virtual void <code>gradient</code> (<code>Array</code> &amp;grad, const <code>Array</code> &amp;x) const<br />
 <i>method to overload to compute grad_f, the first derivative of </i><br />
 virtual <code>Real</code> <code>valueAndGradient</code> (<code>Array</code> &amp;grad, const <code>Array</code> &amp;x) const<br />
 <i>method to overload to compute grad_f, the first derivative of </i><br />
 virtual <code>Real</code> <code>finiteDifferenceEpsilon</code> () const<br />
 <i>Default epsilon for finite difference method :. </i></p>
<h2>Detailed Description</h2>
<p>Cost function abstract class for optimization problem. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
