---
title: "gausshermiteintegration(3)"
name: "gausshermiteintegration"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gausshermiteintegration/"
description: "QuantLib::GaussHermiteIntegration – generalized Gauss-Hermite integration"
---

<p>QuantLib::GaussHermiteIntegration &#8211; generalized Gauss-Hermite integration </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/integrals/gaussianquadratures.hpp&gt; </p>
<p> Inherits <code>QuantLib::GaussianQuadrature</code>. </p>
<h3>Public Member Functions</h3>
<p><code>GaussHermiteIntegration</code> (Size n, <code>Real</code> mu=0.0) </p>
<h2>Detailed Description</h2>
<p>generalized Gauss-Hermite integration </p>
<p> This class performs a 1-dimensional Gauss-Hermite integration. [ int_{-inf}^{inf} f(x) mathrm{d}x ] The weighting function is [ w(x;mu)=|x|^{2mu} 
