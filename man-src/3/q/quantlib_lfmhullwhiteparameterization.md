---
title: "quantlib_lfmhullwhiteparameterization(3)"
name: "quantlib_lfmhullwhiteparameterization"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lfmhullwhiteparameterization/"
description: "QuantLib::LfmHullWhiteParameterization – Libor market model parameterization based on Hull White paper"
---

<p>QuantLib::LfmHullWhiteParameterization &#8211; Libor market model parameterization based on Hull White paper </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lfmhullwhiteparam.hpp&gt; </p>
<p> Inherits <code>QuantLib::LfmCovarianceParameterization</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LfmHullWhiteParameterization</code> (const boost::shared_ptr&lt; <code>LiborForwardModelProcess</code> &gt; &amp;process, const boost::shared_ptr&lt; <code>OptionletVolatilityStructure</code> &gt; &amp;capletVol, const <code>Matrix</code> &amp;correlation=<code>Matrix</code>(), Size factors=1) </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>integratedCovariance</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<h3>Protected Member Functions</h3>
<p>Size <code>nextIndexReset</code> (Time t) const </p>
<h3>Protected Attributes</h3>
<p><code>Matrix</code> <code>diffusion_</code> </p>
<p> <code>Matrix</code> <code>covariance_</code> </p>
<p> std::vector&lt; Time &gt; <code>fixingTimes_</code> </p>
<h2>Detailed Description</h2>
<p>Libor market model parameterization based on Hull White paper </p>
<p> Hull, John, White, Alan, 1999, <code>Forward</code> Rate Volatilities, <code>Swap</code> Rate Volatilities and the Implementation of the <code>Libor</code> Market Model (&lt;<a rel="nofollow" href="http://www.rotman.utoronto.ca/~amackay/fin/libormktmodel2.pdf">http://www.rotman.utoronto.ca/~amackay/fin/libormktmodel2.pdf</a>&gt;) </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness is tested by Monte-Carlo reproduction of caplet &amp; ratchet npvs and comparison with Black pricing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
