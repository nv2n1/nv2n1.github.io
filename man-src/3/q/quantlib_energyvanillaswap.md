---
title: "quantlib_energyvanillaswap(3)"
name: "quantlib_energyvanillaswap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_energyvanillaswap/"
description: "QuantLib::EnergyVanillaSwap – Vanilla energy swap."
---

<p>QuantLib::EnergyVanillaSwap &#8211; Vanilla energy swap. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/energyvanillaswap.hpp&gt; </p>
<p> Inherits QuantLib::EnergySwap. </p>
<h3>Public Member Functions</h3>
<p><code>EnergyVanillaSwap</code> (bool payer, const <code>Calendar</code> &amp;calendar, const <code>Money</code> &amp;fixedPrice, const <code>UnitOfMeasure</code> &amp;fixedPriceUnitOfMeasure, const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; &amp;index, const <code>Currency</code> &amp;payCurrency, const <code>Currency</code> &amp;receiveCurrency, const PricingPeriods &amp;pricingPeriods, const <code>CommodityType</code> &amp;commodityType, const boost::shared_ptr&lt; SecondaryCosts &gt; &amp;secondaryCosts, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;payLegTermStructure, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;receiveLegTermStructure, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountTermStructure) </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 <code>Integer</code> <code>payReceive</code> () const </p>
<p> const <code>Money</code> &amp; <code>fixedPrice</code> () const </p>
<p> const <code>UnitOfMeasure</code> &amp; <code>fixedPriceUnitOfMeasure</code> () const </p>
<p> const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; &amp; <code>index</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>performCalculations</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>Integer</code> <code>payReceive_</code> </p>
<p> <code>Money</code> <code>fixedPrice_</code> </p>
<p> <code>UnitOfMeasure</code> <code>fixedPriceUnitOfMeasure_</code> </p>
<p> boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; <code>index_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>payLegTermStructure_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>receiveLegTermStructure_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>discountTermStructure_</code> </p>
<h2>Detailed Description</h2>
<p>Vanilla energy swap.</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
