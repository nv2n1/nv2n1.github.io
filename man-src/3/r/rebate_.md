---
title: "rebate_(3)"
name: "rebate_"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rebate_/"
description: "QuantLib::BarrierOption – Barrier option on a single asset."
---

<p>QuantLib::BarrierOption &#8211; Barrier option on a single asset. </p>
<h2>Synopsis</h2>
<pre><code>BarrierOption (Barrier::Type barrierType, Real barrier, Real rebate, const boost::shared_ptr&lt; StrikedTypePayoff &gt; &amp;payoff, const boost::shared_ptr&lt; Exercise &gt; &amp;exercise)



void setupArguments (PricingEngine::arguments *) const



Volatility impliedVolatility (Real price, const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Real accuracy=1.0e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::OneAssetOption</code>. Inherited by <code>DividendBarrierOption</code>, and <code>QuantoBarrierOption</code>.</p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for barrier option calculation </i><br />
 class <code>engine</code><br />
 <i>Barrier-option engine base class </i></p>
<h3>Public Member Functions</h3>
<pre><code>BarrierOption (Barrier::Type barrierType, Real barrier, Real rebate, const boost::shared_ptr&lt; StrikedTypePayoff &gt; &amp;payoff, const boost::shared_ptr&lt; Exercise &gt; &amp;exercise)



void setupArguments (PricingEngine::arguments *) const



Volatility impliedVolatility (Real price, const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Real accuracy=1.0e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const



Protected Attributes</code></pre>
<p> Barrier::Type <code>barrierType_</code> </p>
<p> <code>Real</code> <code>barrier_</code> </p>
<p> <code>Real</code> <code>rebate_</code></p>
<h2>Detailed Description</h2>
<p>Barrier option on a single asset. </p>
<p> The analytic pricing <code>engine</code> will be used if none if passed. </p>
<p> <code>Examples: </code> </p>
<p> <code>Replication.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Option</code>. </p>
<p> Reimplemented in <code>DividendBarrierOption</code>.</p>
<h3><code>Volatility</code> impliedVolatility (<code>Real</code> price, const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp; process, <code>Real</code> accuracy = 1.0e-4, Size maxEvaluations = 100, <code>Volatility</code> minVol = 1.0e-7, <code>Volatility</code> maxVol = 4.0) const</h3>
<p><code>Warning</code></p>
<dl>
<dd>see <code>VanillaOption</code> for notes on implied-volatility calculation.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
