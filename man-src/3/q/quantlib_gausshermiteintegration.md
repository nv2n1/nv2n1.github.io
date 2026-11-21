---
title: "quantlib_gausshermiteintegration(3)"
name: "quantlib_gausshermiteintegration"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_gausshermiteintegration/"
description: "QuantLib::GaussHermiteIntegration – generalized Gauss-Hermite integration"
---
<p>QuantLib::GaussHermiteIntegration &#8211; generalized Gauss-Hermite integration </p>
<h2>SYNOPSIS</h2>
<p> <br />
 </p>
<p>#include &lt;ql/math/integrals/gaussianquadratures.hpp&gt; </p>
<p>Inherits <code>QuantLib::GaussianQuadrature</code>. </p>
<h3>Public Member Functions</h3>
<p> <br />
 <code>GaussHermiteIntegration</code> (Size n, <code>Real</code> mu=0.0) <br />
  </p>
<h2>Detailed Description</h2>
<p>generalized Gauss-Hermite integration </p>
<p>This class performs a 1-dimensional Gauss-Hermite integration. [ int_{-inf}^{inf} f(x) mathrm{d}x ] The weighting function is [ w(x;mu)=|x|^{2mu} \xp{-x*x} ] and [ mu &gt; -0.5 ] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAD">Public Member Functions</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAE">Detailed Description</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">Author</a></dt>
<dd>  </dd></dl>
