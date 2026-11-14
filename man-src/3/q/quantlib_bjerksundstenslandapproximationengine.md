---
title: "quantlib_bjerksundstenslandapproximationengine(3)"
name: "quantlib_bjerksundstenslandapproximationengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_bjerksundstenslandapproximationengine/"
description: "QuantLib::BjerksundStenslandApproximationEngine – Bjerksund and Stensland pricing engine for American options (1993)."
---

<p>QuantLib::BjerksundStenslandApproximationEngine &#8211; Bjerksund and Stensland pricing engine for American options (1993). </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/bjerksundstenslandengine.hpp&gt; </p>
<p> Inherits VanillaOption::engine. </p>
<h3>Public Member Functions</h3>
<p><code>BjerksundStenslandApproximationEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Bjerksund and Stensland pricing engine for American options (1993). </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dl>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
