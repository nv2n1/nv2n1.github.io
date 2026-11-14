---
title: "nu(3)"
name: "nu"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nu/"
description: "QuantLib::SABRInterpolation – SABR smile interpolation between discrete volatility points."
---

<p>QuantLib::SABRInterpolation &#8211; SABR smile interpolation between discrete volatility points. </p>
<h2>Synopsis</h2>
<pre><code>template&lt;class I1 , class I2 &gt; SABRInterpolation (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin, Time t, const Real &amp;forward, Real alpha, Real beta, Real nu, Real rho, bool alphaIsFixed, bool betaIsFixed, bool nuIsFixed, bool rhoIsFixed, bool vegaWeighted=false, const boost::shared_ptr&lt; EndCriteria &gt; &amp;endCriteria=boost::shared_ptr&lt; EndCriteria &gt;(), const boost::shared_ptr&lt; OptimizationMethod &gt; &amp;optMethod=boost::shared_ptr&lt; OptimizationMethod &gt;())



Real expiry () const



Real forward () const



Real alpha () const



Real beta () const



Real nu () const



Real rho () const



Real rmsError () const



Real maxError () const



const std::vector&lt; Real &gt; &amp; interpolationWeights () const



EndCriteria::Type endCriteria ()</code></pre>
<p> Inherits <code>QuantLib::Interpolation</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>template&lt;class I1 , class I2 &gt; SABRInterpolation (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin, Time t, const Real &amp;forward, Real alpha, Real beta, Real nu, Real rho, bool alphaIsFixed, bool betaIsFixed, bool nuIsFixed, bool rhoIsFixed, bool vegaWeighted=false, const boost::shared_ptr&lt; EndCriteria &gt; &amp;endCriteria=boost::shared_ptr&lt; EndCriteria &gt;(), const boost::shared_ptr&lt; OptimizationMethod &gt; &amp;optMethod=boost::shared_ptr&lt; OptimizationMethod &gt;())



Real expiry () const



Real forward () const



Real alpha () const



Real beta () const



Real nu () const



Real rho () const



Real rmsError () const



Real maxError () const



const std::vector&lt; Real &gt; &amp; interpolationWeights () const



EndCriteria::Type endCriteria ()</code></pre>
<h2>Detailed Description</h2>
<p>SABR smile interpolation between discrete volatility points.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
