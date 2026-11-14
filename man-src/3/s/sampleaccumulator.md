---
title: "sampleaccumulator(3)"
name: "sampleaccumulator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sampleaccumulator/"
description: "QuantLib::McPricer – base class for Monte Carlo pricers"
---

<p>QuantLib::McPricer &#8211; base class for Monte Carlo pricers </p>
<h2>Synopsis</h2>
<pre><code>Real value (Real tolerance, Size maxSamples=QL_MAX_INTEGER, Size minSamples=1023) const


add samples until the required tolerance is reached


Real valueWithSamples (Size samples, Size minSamples=1023) const


simulate a fixed number of samples


Real errorEstimate () const


estimated error of the samples simulated so far


const S &amp; sampleAccumulator (void) const


access to the sample accumulator for more statistics



Protected Attributes</code></pre>
<h3>Public Member Functions</h3>
<pre><code>Real value (Real tolerance, Size maxSamples=QL_MAX_INTEGER, Size minSamples=1023) const


add samples until the required tolerance is reached


Real valueWithSamples (Size samples, Size minSamples=1023) const


simulate a fixed number of samples


Real errorEstimate () const


estimated error of the samples simulated so far


const S &amp; sampleAccumulator (void) const


access to the sample accumulator for more statistics



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>MonteCarloModel</code>&lt; MC, RNG, S &gt; &gt; <code>mcModel_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;template&lt; class &gt; class MC, class RNG, class S = Statistics&gt; class QuantLib::McPricer&lt; MC, RNG, S &gt;</h3>
<p>base class for Monte Carlo pricers </p>
<p> Eventually this class might be linked to the general tree of pricers, in order to have tools like impliedVolatility available. Also, it could, eventually, offer greeks methods. Deriving a class from <code>McPricer</code> gives an easy way to write a Monte Carlo Pricer. See McEuropean as example of one factor pricer, <code>Basket</code> as example of multi factor pricer.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
