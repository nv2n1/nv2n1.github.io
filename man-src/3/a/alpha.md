---
title: "alpha(3)"
name: "alpha"
section: "3"
letter: "a"
url: "/docs/linux/man/3-alpha/"
description: "QuantLib::GaussianOrthogonalPolynomial – orthogonal polynomial for Gaussian quadratures"
---

<h2 class="name">NAME</h2>
<p> QuantLib::GaussianOrthogonalPolynomial &#8211; orthogonal polynomial for Gaussian quadratures </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/integrals/gaussianorthogonalpolynomial.hpp&gt; </p>
<p> Inherited by <code>GaussHermitePolynomial</code>, <code>GaussHyperbolicPolynomial</code>, <code>GaussJacobiPolynomial</code>, and <code>GaussLaguerrePolynomial</code>. </p>
<h3>Public Member Functions</h3>
<p> virtual Real <code>mu_0</code> () const =0 </p>
<p> virtual Real <code>alpha</code> (Size i) const =0 </p>
<p> virtual Real <code>beta</code> (Size i) const =0 </p>
<p> virtual Real <code>w</code> (Real x) const =0 </p>
<p> Real <code>value</code> (Size i, Real x) const </p>
<p> Real <code>weightedValue</code> (Size i, Real x) const </p>
<h2>Detailed Description</h2>
<p> orthogonal polynomial for Gaussian quadratures </p>
<p> References: Gauss quadratures and orthogonal polynomials </p>
<p> G.H. Gloub and J.H. Welsch: Calculation of Gauss quadrature rule. Math. Comput. 23 (1986), 221-230 </p>
<p> The polynomials are defined by the three-term recurrence relation [ P_{k+1}(x)=(x-lpha_k) P_k(x) &#8211; nerated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
