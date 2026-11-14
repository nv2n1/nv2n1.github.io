---
title: "calculateabstolerance(3)"
name: "calculateabstolerance"
section: "3"
letter: "c"
url: "/docs/linux/man/3-calculateabstolerance/"
description: "QuantLib::GaussLobattoIntegral – Integral of a one-dimensional function."
---

<p>QuantLib::GaussLobattoIntegral &#8211; Integral of a one-dimensional function. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/integrals/gausslobattointegral.hpp&gt; </p>
<p> Inherits QuantLib::Integrator. </p>
<h3>Public Member Functions</h3>
<p><code>GaussLobattoIntegral</code> (Size maxIterations, Real absAccuracy, Real relAccuracy=<code>Null</code>&lt; Real &gt;(), bool useConvergenceEstimate=true) </p>
<h3>Protected Member Functions</h3>
<p>Real <code>integrate</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b) const </p>
<p> Real <code>adaptivGaussLobattoStep</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b, Real fa, Real fb, Real is) const </p>
<p> Real <code>calculateAbsTolerance</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b) const </p>
<h3>Protected Attributes</h3>
<p>Real <code>relAccuracy_</code> </p>
<p> const bool <code>useConvergenceEstimate_</code> </p>
<h3>Static Protected Attributes</h3>
<p>static const Real <code>alpha_</code> </p>
<p> static const Real <code>beta_</code> </p>
<p> static const Real <code>x1_</code> </p>
<p> static const Real <code>x2_</code> </p>
<p> static const Real <code>x3_</code> </p>
<h2>Detailed Description</h2>
<p>Integral of a one-dimensional function. </p>
<p> Given a target accuracy $ \psilon $, the integral of a function $ f $ between $ a $ and $ b $ is calculated by means of the Gauss-Lobatto formula </p>
<p> References: This algorithm is a C++ implementation of the algorithm outlined in </p>
<p> W. Gander and W. Gautschi, Adaptive Quadrature &#8211; Revisited. BIT, <a href="/docs/linux/man/1-40/">40</a>(1):84-101, March 2000. CS technical report: <a href="ftp://ftp.inf.ethz.ch">ftp.inf.ethz.ch</a>/pub/publications/tech-reports/3xx/306.ps.gz </p>
<p> The original MATLAB version can be downloaded here <a rel="nofollow" href="http://www.inf.ethz.ch/personal/gander/adaptlob.m">http://www.inf.ethz.ch/personal/gander/adaptlob.m</a> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
