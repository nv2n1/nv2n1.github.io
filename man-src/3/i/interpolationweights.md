---
title: "interpolationweights(3)"
name: "interpolationweights"
section: "3"
letter: "i"
url: "/docs/linux/man/3-interpolationweights/"
description: "QuantLib::SABRInterpolation – SABR smile interpolation between discrete volatility points."
---

<p>QuantLib::SABRInterpolation &#8211; SABR smile interpolation between discrete volatility points. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/sabrinterpolation.hpp&gt; </p>
<p> Inherits <code>QuantLib::Interpolation</code>. </p>
<h3>Public Member Functions</h3>
<p>template&lt;class I1 , class I2 &gt; <code>SABRInterpolation</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin, <code>Time</code> t, const <code>Real</code> &amp;forward, <code>Real</code> alpha, <code>Real</code> beta, <code>Real</code> nu, <code>Real</code> rho, bool alphaIsFixed, bool betaIsFixed, bool nuIsFixed, bool rhoIsFixed, bool vegaWeighted=false, const boost::shared_ptr&lt; <code>EndCriteria</code> &gt; &amp;endCriteria=boost::shared_ptr&lt; <code>EndCriteria</code> &gt;(), const boost::shared_ptr&lt; <code>OptimizationMethod</code> &gt; &amp;optMethod=boost::shared_ptr&lt; <code>OptimizationMethod</code> &gt;()) </p>
<p> <code>Real</code> <code>expiry</code> () const </p>
<p> <code>Real</code> <code>forward</code> () const </p>
<p> <code>Real</code> <code>alpha</code> () const </p>
<p> <code>Real</code> <code>beta</code> () const </p>
<p> <code>Real</code> <code>nu</code> () const </p>
<p> <code>Real</code> <code>rho</code> () const </p>
<p> <code>Real</code> <code>rmsError</code> () const </p>
<p> <code>Real</code> <code>maxError</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>interpolationWeights</code> () const </p>
<p> EndCriteria::Type <code>endCriteria</code> () </p>
<h2>Detailed Description</h2>
<p>SABR smile interpolation between discrete volatility points. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
