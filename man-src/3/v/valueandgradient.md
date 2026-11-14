---
title: "valueandgradient(3)"
name: "valueandgradient"
section: "3"
letter: "v"
url: "/docs/linux/man/3-valueandgradient/"
description: "QuantLib::CostFunction – Cost function abstract class for optimization problem."
---

<p>QuantLib::CostFunction &#8211; Cost function abstract class for optimization problem. </p>
<h2>Synopsis</h2>
<pre><code>virtual Real value (const Array &amp;x) const =0


method to overload to compute the cost function value in x


virtual Disposable&lt; Array &gt; values (const Array &amp;x) const =0


method to overload to compute the cost function values in x


virtual void gradient (Array &amp;grad, const Array &amp;x) const


method to overload to compute grad_f, the first derivative of


virtual Real valueAndGradient (Array &amp;grad, const Array &amp;x) const


method to overload to compute grad_f, the first derivative of


virtual Real finiteDifferenceEpsilon () const


Default epsilon for finite difference method :.</code></pre>
<p> Inherited by AbcdError, SABRError, FrobeniusCostFunction, <code>LeastSquareFunction</code>, PenaltyFunction&lt; Curve &gt;, and <code>ProjectedCostFunction</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual Real value (const Array &amp;x) const =0


method to overload to compute the cost function value in x


virtual Disposable&lt; Array &gt; values (const Array &amp;x) const =0


method to overload to compute the cost function values in x


virtual void gradient (Array &amp;grad, const Array &amp;x) const


method to overload to compute grad_f, the first derivative of


virtual Real valueAndGradient (Array &amp;grad, const Array &amp;x) const


method to overload to compute grad_f, the first derivative of


virtual Real finiteDifferenceEpsilon () const


Default epsilon for finite difference method :.</code></pre>
<h2>Detailed Description</h2>
<p>Cost function abstract class for optimization problem.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
