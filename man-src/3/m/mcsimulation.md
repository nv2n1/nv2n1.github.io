---
title: "mcsimulation(3)"
name: "mcsimulation"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mcsimulation/"
description: "QuantLib::McSimulation – base class for Monte Carlo engines"
---

<p>QuantLib::McSimulation &#8211; base class for Monte Carlo engines </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/mcsimulation.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>MonteCarloModel</code>&lt; MC, RNG, S &gt;::<code>path_generator_type</code> <code>path_generator_type</code> </p>
<p> typedef <code>MonteCarloModel</code>&lt; MC, RNG, S &gt;::<code>path_pricer_type</code> <code>path_pricer_type</code> </p>
<p> typedef <code>MonteCarloModel</code>&lt; MC, RNG, S &gt;::stats_type <code>stats_type</code> </p>
<p> typedef <code>MonteCarloModel</code>&lt; MC, RNG, S &gt;::result_type <code>result_type</code> </p>
<h3>Public Member Functions</h3>
<p>result_type <code>value</code> (Real tolerance, Size maxSamples=QL_MAX_INTEGER, Size minSamples=1023) const<br />
 <i>add samples until the required absolute tolerance is reached </i><br />
 result_type <code>valueWithSamples</code> (Size samples) const<br />
 <i>simulate a fixed number of samples </i><br />
 result_type <code>errorEstimate</code> () const<br />
 <i>error estimated using the samples simulated so far </i><br />
 const stats_type &amp; <code>sampleAccumulator</code> (void) const<br />
 <i>access to the sample accumulator for richer statistics </i><br />
 void <code>calculate</code> (Real requiredTolerance, Size requiredSamples, Size maxSamples) const<br />
 <i>basic calculate method provided to inherited pricing engines </i></p>
<h3>Protected Member Functions</h3>
<p><code>McSimulation</code> (bool antitheticVariate, bool controlVariate) </p>
<p> virtual boost::shared_ptr&lt; <code>path_pricer_type</code> &gt; <code>pathPricer</code> () const =0 </p>
<p> virtual boost::shared_ptr&lt; <code>path_generator_type</code> &gt; <code>pathGenerator</code> () const =0 </p>
<p> virtual <code>TimeGrid</code> <code>timeGrid</code> () const =0 </p>
<p> virtual boost::shared_ptr&lt; <code>path_pricer_type</code> &gt; <code>controlPathPricer</code> () const </p>
<p> virtual boost::shared_ptr&lt; <code>path_generator_type</code> &gt; <code>controlPathGenerator</code> () const </p>
<p> virtual boost::shared_ptr&lt; <code>PricingEngine</code> &gt; <code>controlPricingEngine</code> () const </p>
<p> virtual result_type <code>controlVariateValue</code> () const </p>
<h3>Static Protected Member Functions</h3>
<p>template&lt;class Sequence &gt; static Real <code>maxError</code> (const Sequence &amp;sequence) </p>
<p> static Real <code>maxError</code> (Real error) </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>MonteCarloModel</code>&lt; MC, RNG, S &gt; &gt; <code>mcModel_</code> </p>
<p> bool <code>antitheticVariate_</code> </p>
<p> bool <code>controlVariate_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;template&lt; class &gt; class MC, class RNG, class S = Statistics&gt; class QuantLib::McSimulation&lt; MC, RNG, S &gt;</h3>
<p>base class for Monte Carlo engines </p>
<p> Eventually this class might offer greeks methods. Deriving a class from <code>McSimulation</code> gives an easy way to write a Monte Carlo engine. </p>
<p> See McVanillaEngine as an example. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
