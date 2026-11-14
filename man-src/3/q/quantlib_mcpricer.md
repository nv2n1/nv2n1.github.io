---
title: "quantlib_mcpricer(3)"
name: "quantlib_mcpricer"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mcpricer/"
description: "QuantLib::McPricer – base class for Monte Carlo pricers"
---

<p>QuantLib::McPricer &#8211; base class for Monte Carlo pricers </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/pricers/mcpricer.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p>Real <code>value</code> (Real tolerance, Size maxSamples=QL_MAX_INTEGER, Size minSamples=1023) const<br />
 <i>add samples until the required tolerance is reached </i><br />
 Real <code>valueWithSamples</code> (Size samples, Size minSamples=1023) const<br />
 <i>simulate a fixed number of samples </i><br />
 Real <code>errorEstimate</code> () const<br />
 <i>estimated error of the samples simulated so far </i><br />
 const S &amp; <code>sampleAccumulator</code> (void) const<br />
 <i>access to the sample accumulator for more statistics </i></p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>MonteCarloModel</code>&lt; MC, RNG, S &gt; &gt; <code>mcModel_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;template&lt; class &gt; class MC, class RNG, class S = Statistics&gt; class QuantLib::McPricer&lt; MC, RNG, S &gt;</h3>
<p>base class for Monte Carlo pricers </p>
<p> Eventually this class might be linked to the general tree of pricers, in order to have tools like impliedVolatility available. Also, it could, eventually, offer greeks methods. Deriving a class from <code>McPricer</code> gives an easy way to write a Monte Carlo Pricer. See McEuropean as example of one factor pricer, <code>Basket</code> as example of multi factor pricer. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
