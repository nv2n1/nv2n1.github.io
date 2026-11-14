---
title: "quantlib_pathwiseaccountingengine(3)"
name: "quantlib_pathwiseaccountingengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_pathwiseaccountingengine/"
description: "QuantLib::PathwiseAccountingEngine – Engine collecting cash flows along a market-model simulation for doing pathwise computation of Deltas."
---

<p>QuantLib::PathwiseAccountingEngine &#8211; Engine collecting cash flows along a market-model simulation for doing pathwise computation of Deltas. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/pathwiseaccountingengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>PathwiseAccountingEngine</code> (const boost::shared_ptr&lt; <code>LogNormalFwdRateEuler</code> &gt; &amp;evolver, const <code>Clone</code>&lt; <code>MarketModelPathwiseMultiProduct</code> &gt; &amp;product, const boost::shared_ptr&lt; <code>MarketModel</code> &gt; &amp;pseudoRootStructure, <code>Real</code> initialNumeraireValue) </p>
<p> void <code>multiplePathValues</code> (<code>SequenceStatisticsInc</code> &amp;stats, Size numberOfPaths) </p>
<h2>Detailed Description</h2>
<p>Engine collecting cash flows along a market-model simulation for doing pathwise computation of Deltas. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
