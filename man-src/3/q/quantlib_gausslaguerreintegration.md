---
title: "quantlib_gausslaguerreintegration(3)"
name: "quantlib_gausslaguerreintegration"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_gausslaguerreintegration/"
description: "QuantLib::GaussLaguerreIntegration – generalized Gauss-Laguerre integration"
---

<p>QuantLib::GaussLaguerreIntegration &#8211; generalized Gauss-Laguerre integration </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/integrals/gaussianquadratures.hpp&gt; </p>
<p> Inherits <code>QuantLib::GaussianQuadrature</code>. </p>
<h3>Public Member Functions</h3>
<p><code>GaussLaguerreIntegration</code> (Size n, <code>Real</code> s=0.0) </p>
<h2>Detailed Description</h2>
<p>generalized Gauss-Laguerre integration </p>
<p> This class performs a 1-dimensional Gauss-Laguerre integration. [ int_{0}^{inf} f(x) mathrm{d}x ] The weighting function is [ w(x;s)=x^s 
