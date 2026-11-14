---
title: "calculatesecondarycostamounts(3)"
name: "calculatesecondarycostamounts"
section: "3"
letter: "c"
url: "/docs/linux/man/3-calculatesecondarycostamounts/"
description: "QuantLib::EnergyCommodity – Energy commodity class."
---

<p>QuantLib::EnergyCommodity &#8211; Energy commodity class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/energycommodity.hpp&gt; </p>
<p> Inherits <code>QuantLib::Commodity</code>. </p>
<p> Inherited by <code>EnergyFuture</code>, and EnergySwap. </p>
<h3>Public Types</h3>
<p>enum <code>DeliverySchedule</code> { <code>Constant</code>, <code>Window</code>, <code>Hourly</code>, <code>Daily</code>, <code>Weekly</code>, <code>Monthly</code>, <code>Quarterly</code>, <code>Yearly</code> } </p>
<p> enum <code>QuantityPeriodicity</code> { <code>Absolute</code>, <code>PerHour</code>, <code>PerDay</code>, <code>PerWeek</code>, <code>PerMonth</code>, <code>PerQuarter</code>, <code>PerYear</code> } </p>
<p> enum <code>PaymentSchedule</code> { <code>WindowSettlement</code>, <code>MonthlySettlement</code>, <code>QuarterlySettlement</code>, <code>YearlySettlement</code> } </p>
<h3>Public Member Functions</h3>
<p><code>EnergyCommodity</code> (const <code>CommodityType</code> &amp;commodityType, const boost::shared_ptr&lt; SecondaryCosts &gt; &amp;secondaryCosts) </p>
<p> virtual <code>Quantity</code> <code>quantity</code> () const =0 </p>
<p> const <code>CommodityType</code> &amp; <code>commodityType</code> () const </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<h3>Protected Member Functions</h3>
<p><code>Real</code> <code>calculateUnitCost</code> (const <code>CommodityType</code> &amp;commodityType, const CommodityUnitCost &amp;unitCost, const <code>Date</code> &amp;evaluationDate) const </p>
<p> void <code>calculateSecondaryCostAmounts</code> (const <code>CommodityType</code> &amp;commodityType, <code>Real</code> totalQuantityValue, const <code>Date</code> &amp;evaluationDate) const </p>
<h3>Static Protected Member Functions</h3>
<p>static <code>Real</code> <code>calculateFxConversionFactor</code> (const <code>Currency</code> &amp;fromCurrency, const <code>Currency</code> &amp;toCurrency, const <code>Date</code> &amp;evaluationDate) </p>
<p> static <code>Real</code> <code>calculateUomConversionFactor</code> (const <code>CommodityType</code> &amp;commodityType, const <code>UnitOfMeasure</code> &amp;fromUnitOfMeasure, const <code>UnitOfMeasure</code> &amp;toUnitOfMeasure) </p>
<h3>Protected Attributes</h3>
<p><code>CommodityType</code> <code>commodityType_</code> </p>
<h2>Detailed Description</h2>
<p>Energy commodity class. </p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
