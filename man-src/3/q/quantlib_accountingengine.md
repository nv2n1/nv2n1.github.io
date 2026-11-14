---
title: "quantlib_accountingengine(3)"
name: "quantlib_accountingengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_accountingengine/"
description: "QuantLib::AccountingEngine – Engine collecting cash flows along a market-model simulation."
---

<p>QuantLib::AccountingEngine &#8211; Engine collecting cash flows along a market-model simulation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/accountingengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>AccountingEngine</code> (const boost::shared_ptr&lt; <code>MarketModelEvolver</code> &gt; &amp;evolver, const <code>Clone</code>&lt; <code>MarketModelMultiProduct</code> &gt; &amp;product, <code>Real</code> initialNumeraireValue) </p>
<p> void <code>multiplePathValues</code> (<code>SequenceStatisticsInc</code> &amp;stats, Size numberOfPaths) </p>
<h2>Detailed Description</h2>
<p>Engine collecting cash flows along a market-model simulation. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
