---
title: "create(3)"
name: "create"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create/"
description: "QuantLib::MarketModelFactory – base class for market-model factories"
---

<h2 class="name">NAME</h2>
<p> QuantLib::MarketModelFactory &#8211; base class for market-model factories </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/models/marketmodels/marketmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>. </p>
<p> Inherited by CotSwapToFwdAdapterFactory, FlatVolFactory, and FwdToCotSwapAdapterFactory. </p>
<h3>Public Member Functions</h3>
<p> virtual boost::shared_ptr&lt; <code>MarketModel</code> &gt; <code>create</code> (const <code>EvolutionDescription</code> &amp;, Size numberOfFactors) const =0 </p>
<h2>Detailed Description</h2>
<p> base class for market-model factories </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
