---
title: "gaussianquadrature(3)"
name: "gaussianquadrature"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gaussianquadrature/"
description: "QuantLib::GaussianQuadrature – Integral of a 1-dimensional function using the Gauss quadratures method."
---

<p>QuantLib::GaussianQuadrature &#8211; Integral of a 1-dimensional function using the Gauss quadratures method. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/integrals/gaussianquadratures.hpp&gt; </p>
<p> Inherited by <code>GaussChebyshev2thIntegration</code>, <code>GaussChebyshevIntegration</code>, <code>GaussGegenbauerIntegration</code>, <code>GaussHermiteIntegration</code>, <code>GaussHyperbolicIntegration</code>, <code>GaussJacobiIntegration</code>, <code>GaussLaguerreIntegration</code>, and <code>GaussLegendreIntegration</code>. </p>
<h3>Public Member Functions</h3>
<p><code>GaussianQuadrature</code> (Size n, const <code>GaussianOrthogonalPolynomial</code> &amp;p) </p>
<p> template&lt;class F &gt; <code>Real</code> <code>operator()</code> (const F &amp;f) const </p>
<p> Size <code>order</code> () const </p>
<h2>Detailed Description</h2>
<p>Integral of a 1-dimensional function using the Gauss quadratures method. </p>
<p> References: Gauss quadratures and orthogonal polynomials </p>
<p> G.H. Gloub and J.H. Welsch: Calculation of Gauss quadrature rule. Math. Comput. 23 (1986), 221-230 </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the result is tested by checking it against known good values.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
