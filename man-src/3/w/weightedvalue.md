---
title: "weightedvalue(3)"
name: "weightedvalue"
section: "3"
letter: "w"
url: "/docs/linux/man/3-weightedvalue/"
description: "QuantLib::GaussianOrthogonalPolynomial – orthogonal polynomial for Gaussian quadratures"
---

<p>QuantLib::GaussianOrthogonalPolynomial &#8211; orthogonal polynomial for Gaussian quadratures </p>
<h2>Synopsis</h2>
<pre><code>virtual Real mu_0 () const =0



virtual Real alpha (Size i) const =0



virtual Real beta (Size i) const =0



virtual Real w (Real x) const =0



Real value (Size i, Real x) const



Real weightedValue (Size i, Real x) const</code></pre>
<p> Inherited by <code>GaussHermitePolynomial</code>, <code>GaussHyperbolicPolynomial</code>, <code>GaussJacobiPolynomial</code>, and <code>GaussLaguerrePolynomial</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual Real mu_0 () const =0



virtual Real alpha (Size i) const =0



virtual Real beta (Size i) const =0



virtual Real w (Real x) const =0



Real value (Size i, Real x) const



Real weightedValue (Size i, Real x) const</code></pre>
<h2>Detailed Description</h2>
<p>orthogonal polynomial for Gaussian quadratures </p>
<p> References: Gauss quadratures and orthogonal polynomials </p>
<p> G.H. Gloub and J.H. Welsch: Calculation of Gauss quadrature rule. Math. Comput. 23 (1986), 221-230 </p>
<p> The polynomials are defined by the three-term recurrence relation [ P_{k+1}(x)=(x-lpha_k) P_k(x) &#8211; nerated automatically by Doxygen for QuantLib from the source code.</p>
