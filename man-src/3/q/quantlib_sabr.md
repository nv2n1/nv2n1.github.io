---
title: "quantlib_sabr(3)"
name: "quantlib_sabr"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_sabr/"
description: "QuantLib::SABR – SABR interpolation factory and traits"
---

<p>QuantLib::SABR &#8211; SABR interpolation factory and traits </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/sabrinterpolation.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>SABR</code> (<code>Time</code> t, Real forward, Real alpha, Real beta, Real nu, Real rho, bool alphaIsFixed, bool betaIsFixed, bool nuIsFixed, bool rhoIsFixed, bool vegaWeighted=false, const boost::shared_ptr&lt; <code>EndCriteria</code> &gt; endCriteria=boost::shared_ptr&lt; <code>EndCriteria</code> &gt;(), const boost::shared_ptr&lt; <code>OptimizationMethod</code> &gt; optMethod=boost::shared_ptr&lt; <code>OptimizationMethod</code> &gt;()) </p>
<p> template&lt;class I1 , class I2 &gt; <code>Interpolation</code> <code>interpolate</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin) const </p>
<h3>Static Public Attributes</h3>
<p>static const bool <code>global</code> = true </p>
<h2>Detailed Description</h2>
<p>SABR interpolation factory and traits </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
