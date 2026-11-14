---
title: "quantlib_multiproductcomposite(3)"
name: "quantlib_multiproductcomposite"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_multiproductcomposite/"
description: "QuantLib::MultiProductComposite – Composition of one or more market-model products."
---

<p>QuantLib::MultiProductComposite &#8211; Composition of one or more market-model products. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/products/multiproductcomposite.hpp&gt; </p>
<p> Inherits <code>QuantLib::MarketModelComposite</code>. </p>
<h3>Public Member Functions</h3>
<p><code>MarketModelMultiProduct interface</code> </p>
<p> Size <code>numberOfProducts</code> () const </p>
<p> Size <code>maxNumberOfCashFlowsPerProductPerStep</code> () const </p>
<p> bool <code>nextTimeStep</code> (const <code>CurveState</code> &amp;currentState, std::vector&lt; Size &gt; &amp;numberCashFlowsThisStep, std::vector&lt; std::vector&lt; CashFlow &gt; &gt; &amp;cashFlowsGenerated)<br />
 <i>return value indicates whether path is finished, TRUE means done </i><br />
 std::auto_ptr&lt; <code>MarketModelMultiProduct</code> &gt; <code>clone</code> () const<br />
 <i>returns a newly-allocated copy of itself </i></p>
<h2>Detailed Description</h2>
<p>Composition of one or more market-model products. </p>
<p> Instances of this class build a multiple market-model product by composing two or more subproducts. </p>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>All subproducts must have the same rate times.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
