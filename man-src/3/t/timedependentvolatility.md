---
title: "timedependentvolatility(3)"
name: "timedependentvolatility"
section: "3"
letter: "t"
url: "/docs/linux/man/3-timedependentvolatility/"
description: "QuantLib::MarketModel – base class for market models"
---

<p>QuantLib::MarketModel &#8211; base class for market models </p>
<h2>Synopsis</h2>
<pre><code>virtual const std::vector&lt; Rate &gt; &amp; initialRates () const =0



virtual const std::vector&lt; Spread &gt; &amp; displacements () const =0



virtual const EvolutionDescription &amp; evolution () const =0



virtual Size numberOfRates () const =0



virtual Size numberOfFactors () const =0



virtual Size numberOfSteps () const =0



virtual const Matrix &amp; pseudoRoot (Size i) const =0



virtual const Matrix &amp; covariance (Size i) const



virtual const Matrix &amp; totalCovariance (Size endIndex) const



std::vector&lt; Volatility &gt; timeDependentVolatility (Size i) const</code></pre>
<p> Inherited by <code>AbcdVol</code>, CotSwapToFwdAdapter, FlatVol, FwdPeriodAdapter, FwdToCotSwapAdapter, and PseudoRootFacade.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual const std::vector&lt; Rate &gt; &amp; initialRates () const =0



virtual const std::vector&lt; Spread &gt; &amp; displacements () const =0



virtual const EvolutionDescription &amp; evolution () const =0



virtual Size numberOfRates () const =0



virtual Size numberOfFactors () const =0



virtual Size numberOfSteps () const =0



virtual const Matrix &amp; pseudoRoot (Size i) const =0



virtual const Matrix &amp; covariance (Size i) const



virtual const Matrix &amp; totalCovariance (Size endIndex) const



std::vector&lt; Volatility &gt; timeDependentVolatility (Size i) const</code></pre>
<h2>Detailed Description</h2>
<p>base class for market models </p>
<p> For each time step, generates the pseudo-square root of the covariance matrix for that time step.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
