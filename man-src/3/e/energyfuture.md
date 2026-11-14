---
title: "energyfuture(3)"
name: "energyfuture"
section: "3"
letter: "e"
url: "/docs/linux/man/3-energyfuture/"
description: "QuantLib::EnergyFuture – Energy future."
---

<p>QuantLib::EnergyFuture &#8211; Energy future. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/energyfuture.hpp&gt; </p>
<p> Inherits <code>QuantLib::EnergyCommodity</code>. </p>
<h3>Public Member Functions</h3>
<p><code>EnergyFuture</code> (<code>Integer</code> buySell, const <code>Quantity</code> &amp;quantity, const CommodityUnitCost &amp;tradePrice, const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; &amp;index, const <code>CommodityType</code> &amp;commodityType, const boost::shared_ptr&lt; SecondaryCosts &gt; &amp;secondaryCosts) </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 <code>Quantity</code> <code>quantity</code> () const </p>
<p> const CommodityUnitCost &amp; <code>tradePrice</code> () const </p>
<p> const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; <code>index</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>performCalculations</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>Integer</code> <code>buySell_</code> </p>
<p> <code>Quantity</code> <code>quantity_</code> </p>
<p> CommodityUnitCost <code>tradePrice_</code> </p>
<p> boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; <code>index_</code> </p>
<h2>Detailed Description</h2>
<p>Energy future. </p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
