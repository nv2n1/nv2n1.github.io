---
title: "pathwisevegasaccountingengine(3)"
name: "pathwisevegasaccountingengine"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pathwisevegasaccountingengine/"
description: "QuantLib::PathwiseVegasAccountingEngine – Engine collecting cash flows along a market-model simulation for doing pathwise computation of Deltas and vegas."
---

<p>QuantLib::PathwiseVegasAccountingEngine &#8211; Engine collecting cash flows along a market-model simulation for doing pathwise computation of Deltas and vegas. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/pathwiseaccountingengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>PathwiseVegasAccountingEngine</code> (const boost::shared_ptr&lt; <code>LogNormalFwdRateEuler</code> &gt; &amp;evolver, const <code>Clone</code>&lt; <code>MarketModelPathwiseMultiProduct</code> &gt; &amp;product, const boost::shared_ptr&lt; <code>MarketModel</code> &gt; &amp;pseudoRootStructure, const std::vector&lt; std::vector&lt; <code>Matrix</code> &gt; &gt; &amp;VegaBumps, <code>Real</code> initialNumeraireValue) </p>
<p> void <code>multiplePathValues</code> (std::vector&lt; <code>Real</code> &gt; &amp;means, std::vector&lt; <code>Real</code> &gt; &amp;errors, Size numberOfPaths) </p>
<h2>Detailed Description</h2>
<p>Engine collecting cash flows along a market-model simulation for doing pathwise computation of Deltas and vegas. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
