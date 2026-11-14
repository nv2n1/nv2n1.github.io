---
title: "quantlib_mceuropeangjrgarchengine(3)"
name: "quantlib_mceuropeangjrgarchengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mceuropeangjrgarchengine/"
description: "QuantLib::MCEuropeanGJRGARCHEngine – Monte Carlo GJR-GARCH-model engine for European options."
---

<p>QuantLib::MCEuropeanGJRGARCHEngine &#8211; Monte Carlo GJR-GARCH-model engine for European options. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/mceuropeangjrgarchengine.hpp&gt; </p>
<p> Inherits <code>MCVanillaEngine&lt; MultiVariate, RNG, S &gt;</code>. </p>
<h3>Public Types</h3>
<p>typedef <code>MCVanillaEngine</code>&lt; <code>MultiVariate</code>, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>MCEuropeanGJRGARCHEngine</code> (const boost::shared_ptr&lt; <code>GJRGARCHProcess</code> &gt; &amp;, Size timeSteps, Size timeStepsPerYear, bool antitheticVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed) </p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; path_pricer_type &gt; <code>pathPricer</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCEuropeanGJRGARCHEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo GJR-GARCH-model engine for European options. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
