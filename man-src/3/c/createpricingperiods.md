---
title: "createpricingperiods(3)"
name: "createpricingperiods"
section: "3"
letter: "c"
url: "/docs/linux/man/3-createpricingperiods/"
description: "QuantLib::CommodityPricingHelper – commodity index helper"
---

<p>QuantLib::CommodityPricingHelper &#8211; commodity index helper </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/commoditypricinghelpers.hpp&gt; </p>
<h3>Static Public Member Functions</h3>
<p>static <code>Real</code> <code>calculateFxConversionFactor</code> (const <code>Currency</code> &amp;fromCurrency, const <code>Currency</code> &amp;toCurrency, const <code>Date</code> &amp;evaluationDate) </p>
<p> static <code>Real</code> <code>calculateUomConversionFactor</code> (const <code>CommodityType</code> &amp;commodityType, const <code>UnitOfMeasure</code> &amp;fromUnitOfMeasure, const <code>UnitOfMeasure</code> &amp;toUnitOfMeasure) </p>
<p> static <code>Real</code> <code>calculateUnitCost</code> (const <code>CommodityType</code> &amp;commodityType, const CommodityUnitCost &amp;unitCost, const <code>Currency</code> &amp;baseCurrency, const <code>UnitOfMeasure</code> &amp;baseUnitOfMeasure, const <code>Date</code> &amp;evaluationDate) </p>
<p> static void <code>createPricingPeriods</code> (<code>Date</code> startDate, <code>Date</code> endDate, const <code>Quantity</code> &amp;quantity, EnergyCommodity::DeliverySchedule deliverySchedule, EnergyCommodity::QuantityPeriodicity qtyPeriodicity, const PaymentTerm &amp;paymentTerm, PricingPeriods &amp;pricingPeriods) </p>
<h2>Detailed Description</h2>
<p>commodity index helper </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
