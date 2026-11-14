---
title: "quantlib_conjugategradient(3)"
name: "quantlib_conjugategradient"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_conjugategradient/"
description: "QuantLib::ConjugateGradient – Multi-dimensional Conjugate Gradient class."
---

<p>QuantLib::ConjugateGradient &#8211; Multi-dimensional Conjugate Gradient class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/conjugategradient.hpp&gt; </p>
<p> Inherits QuantLib::LineSearchBasedMethod. </p>
<h3>Public Member Functions</h3>
<p><code>ConjugateGradient</code> (const boost::shared_ptr&lt; <code>LineSearch</code> &gt; &amp;lineSearch=boost::shared_ptr&lt; <code>LineSearch</code> &gt;()) </p>
<p> virtual EndCriteria::Type <code>minimize</code> (<code>Problem</code> &amp;P, const <code>EndCriteria</code> &amp;endCriteria)<br />
 <i>solve the optimization problem P </i></p>
<h2>Detailed Description</h2>
<p>Multi-dimensional Conjugate Gradient class. </p>
<p> Fletcher-Reeves-Polak-Ribiere algorithm adapted from Numerical Recipes in C, 2nd edition. </p>
<p> User has to provide line-search method and optimization end criteria. Search direction $ d_i = &#8211; f'(x_i) + c_i*d_{i-1} $ where $ c_i = ||f'(x_i)||^2/||f'(x_{i-1})||^2 $ and $ d_1 = &#8211; f'(x_1) $ </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
