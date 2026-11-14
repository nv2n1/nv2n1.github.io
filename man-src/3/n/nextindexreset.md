---
title: "nextindexreset(3)"
name: "nextindexreset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nextindexreset/"
description: "QuantLib::LfmHullWhiteParameterization – Libor market model parameterization based on Hull White paper"
---

<p>QuantLib::LfmHullWhiteParameterization &#8211; Libor market model parameterization based on Hull White paper </p>
<h2>Synopsis</h2>
<pre><code>LfmHullWhiteParameterization (const boost::shared_ptr&lt; LiborForwardModelProcess &gt; &amp;process, const boost::shared_ptr&lt; OptionletVolatilityStructure &gt; &amp;capletVol, const Matrix &amp;correlation=Matrix(), Size factors=1)



Disposable&lt; Matrix &gt; diffusion (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Disposable&lt; Matrix &gt; covariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Disposable&lt; Matrix &gt; integratedCovariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Protected Member Functions</code></pre>
<p> Inherits <code>QuantLib::LfmCovarianceParameterization</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LfmHullWhiteParameterization (const boost::shared_ptr&lt; LiborForwardModelProcess &gt; &amp;process, const boost::shared_ptr&lt; OptionletVolatilityStructure &gt; &amp;capletVol, const Matrix &amp;correlation=Matrix(), Size factors=1)



Disposable&lt; Matrix &gt; diffusion (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Disposable&lt; Matrix &gt; covariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Disposable&lt; Matrix &gt; integratedCovariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Protected Member Functions</code></pre>
<p> Size <code>nextIndexReset</code> (Time t) const</p>
<h3>Protected Attributes</h3>
<p><code>Matrix</code> <code>diffusion_</code> </p>
<p> <code>Matrix</code> <code>covariance_</code> </p>
<p> std::vector&lt; Time &gt; <code>fixingTimes_</code></p>
<h2>Detailed Description</h2>
<p>Libor market model parameterization based on Hull White paper </p>
<p> Hull, John, White, Alan, 1999, <code>Forward</code> Rate Volatilities, <code>Swap</code> Rate Volatilities and the Implementation of the <code>Libor</code> Market Model (&lt;<a rel="nofollow" href="http://www.rotman.utoronto.ca/~amackay/fin/libormktmodel2.pdf">http://www.rotman.utoronto.ca/~amackay/fin/libormktmodel2.pdf</a>&gt;) </p>
<p> <code>Tests</code></p>
<dl>
<dd>the correctness is tested by Monte-Carlo reproduction of caplet &amp; ratchet npvs and comparison with Black pricing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
