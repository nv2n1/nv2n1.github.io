---
title: "discounttermstructure_(3)"
name: "discounttermstructure_"
section: "3"
letter: "d"
url: "/docs/linux/man/3-discounttermstructure_/"
description: "QuantLib::EnergyBasisSwap – Energy basis swap."
---

<p>QuantLib::EnergyBasisSwap &#8211; Energy basis swap. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/energybasisswap.hpp&gt; </p>
<p> Inherits QuantLib::EnergySwap. </p>
<h3>Public Member Functions</h3>
<p><code>EnergyBasisSwap</code> (const <code>Calendar</code> &amp;calendar, const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; &amp;spreadIndex, const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; &amp;payIndex, const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; &amp;receiveIndex, bool spreadToPayLeg, const <code>Currency</code> &amp;payCurrency, const <code>Currency</code> &amp;receiveCurrency, const PricingPeriods &amp;pricingPeriods, const CommodityUnitCost &amp;basis, const <code>CommodityType</code> &amp;commodityType, const boost::shared_ptr&lt; SecondaryCosts &gt; &amp;secondaryCosts, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;payLegTermStructure, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;receiveLegTermStructure, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountTermStructure) </p>
<p> const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; &amp; <code>payIndex</code> () const </p>
<p> const boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; &amp; <code>receiveIndex</code> () const </p>
<p> const CommodityUnitCost &amp; <code>basis</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>performCalculations</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; <code>spreadIndex_</code> </p>
<p> boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; <code>payIndex_</code> </p>
<p> boost::shared_ptr&lt; <code>CommodityIndex</code> &gt; <code>receiveIndex_</code> </p>
<p> bool <code>spreadToPayLeg_</code> </p>
<p> CommodityUnitCost <code>basis_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>payLegTermStructure_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>receiveLegTermStructure_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>discountTermStructure_</code> </p>
<h2>Detailed Description</h2>
<p>Energy basis swap.</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
