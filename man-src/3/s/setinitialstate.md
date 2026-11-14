---
title: "setinitialstate(3)"
name: "setinitialstate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setinitialstate/"
description: "QuantLib::MarketModelEvolver – Market-model evolver."
---

<p>QuantLib::MarketModelEvolver &#8211; Market-model evolver. </p>
<h2>Synopsis</h2>
<pre><code>virtual const std::vector&lt; Size &gt; &amp; numeraires () const =0



virtual Real startNewPath ()=0



virtual Real advanceStep ()=0



virtual Size currentStep () const =0



virtual const CurveState &amp; currentState () const =0



virtual void setInitialState (const CurveState &amp;)=0</code></pre>
<p> Inherited by <code>ConstrainedEvolver</code>, <code>LogNormalCmSwapRatePc</code>, <code>LogNormalCotSwapRatePc</code>, <code>LogNormalFwdRateEuler</code>, <code>LogNormalFwdRateIpc</code>, <code>LogNormalFwdRatePc</code>, <code>NormalFwdRatePc</code>, and <code>SVDDFwdRatePc</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual const std::vector&lt; Size &gt; &amp; numeraires () const =0



virtual Real startNewPath ()=0



virtual Real advanceStep ()=0



virtual Size currentStep () const =0



virtual const CurveState &amp; currentState () const =0



virtual void setInitialState (const CurveState &amp;)=0</code></pre>
<h2>Detailed Description</h2>
<p>Market-model evolver. </p>
<p> Abstract base class. The evolver does the actual gritty work of evolving the forward rates from one time to the next.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
