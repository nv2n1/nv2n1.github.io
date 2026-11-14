---
title: "quantity_(3)"
name: "quantity_"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantity_/"
description: "QuantLib::EnergyFuture – Energy future."
---

<p>QuantLib::EnergyFuture &#8211; Energy future. </p>
<h2>Synopsis</h2>
<pre><code>void performCalculations () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::EnergyCommodity</code>.</p>
<h3>Public Member Functions</h3>
<p><code>EnergyFuture</code> (<code>Integer</code> buySell, const <code>Quantity</code> &amp;quantity, const CommodityUnitCost &amp;tradePrice, const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; &amp;index, const <code>CommodityType</code> &amp;commodityType, const boost::shared_ptr&lt; SecondaryCosts &gt; &amp;secondaryCosts) </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 <code>Quantity</code> <code>quantity</code> () const </p>
<p> const CommodityUnitCost &amp; <code>tradePrice</code> () const </p>
<p> const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; <code>index</code> () const</p>
<h3>Protected Member Functions</h3>
<pre><code>void performCalculations () const



Protected Attributes</code></pre>
<p> <code>Integer</code> <code>buySell_</code> </p>
<p> <code>Quantity</code> <code>quantity_</code> </p>
<p> CommodityUnitCost <code>tradePrice_</code> </p>
<p> boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; <code>index_</code></p>
<h2>Detailed Description</h2>
<p>Energy future.</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
