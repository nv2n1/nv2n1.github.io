---
title: "quantlib_optimizationmethod(3)"
name: "quantlib_optimizationmethod"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_optimizationmethod/"
description: "QuantLib::OptimizationMethod – Abstract class for constrained optimization method."
---

<p>QuantLib::OptimizationMethod &#8211; Abstract class for constrained optimization method. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/method.hpp&gt; </p>
<p> Inherited by <code>LevenbergMarquardt</code>, LineSearchBasedMethod, and <code>Simplex</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual EndCriteria::Type <code>minimize</code> (<code>Problem</code> &amp;P, const <code>EndCriteria</code> &amp;endCriteria)=0<br />
 <i>minimize the optimization problem P </i></p>
<h2>Detailed Description</h2>
<p>Abstract class for constrained optimization method. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
