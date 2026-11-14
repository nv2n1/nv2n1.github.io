---
title: "useconvergenceestimate_(3)"
name: "useconvergenceestimate_"
section: "3"
letter: "u"
url: "/docs/linux/man/3-useconvergenceestimate_/"
description: "QuantLib::GaussLobattoIntegral – Integral of a one-dimensional function."
---

<p>QuantLib::GaussLobattoIntegral &#8211; Integral of a one-dimensional function. </p>
<h2>Synopsis</h2>
<pre><code>static const Real alpha_



static const Real beta_



static const Real x1_



static const Real x2_



static const Real x3_</code></pre>
<p> Inherits QuantLib::Integrator.</p>
<h3>Public Member Functions</h3>
<p>static const Real alpha_</p>
<p>static const Real beta_</p>
<p>static const Real x1_</p>
<p>static const Real x2_</p>
<p>static const Real x3_<br />
 Real <code>integrate</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b) const </p>
<p> Real <code>adaptivGaussLobattoStep</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b, Real fa, Real fb, Real is) const </p>
<p> Real <code>calculateAbsTolerance</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b) const</p>
<h3>Protected Attributes</h3>
<p>Real <code>relAccuracy_</code> </p>
<p> const bool <code>useConvergenceEstimate_</code></p>
<h3>Static Protected Attributes</h3>
<pre><code>static const Real alpha_



static const Real beta_



static const Real x1_



static const Real x2_



static const Real x3_</code></pre>
<h2>Detailed Description</h2>
<p>Integral of a one-dimensional function. </p>
<p> Given a target accuracy $ \psilon $, the integral of a function $ f $ between $ a $ and $ b $ is calculated by means of the Gauss-Lobatto formula </p>
<p> References: This algorithm is a C++ implementation of the algorithm outlined in </p>
<p> W. Gander and W. Gautschi, Adaptive Quadrature &#8211; Revisited. BIT, <a href="/docs/linux/man/1-40/">40</a>(1):84-101, March 2000. CS technical report: <a href="ftp://ftp.inf.ethz.ch">ftp.inf.ethz.ch</a>/pub/publications/tech-reports/3xx/306.ps.gz </p>
<p> The original MATLAB version can be downloaded here <a rel="nofollow" href="http://www.inf.ethz.ch/personal/gander/adaptlob.m">http://www.inf.ethz.ch/personal/gander/adaptlob.m</a></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
