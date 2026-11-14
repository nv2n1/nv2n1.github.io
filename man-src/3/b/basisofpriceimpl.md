---
title: "basisofpriceimpl(3)"
name: "basisofpriceimpl"
section: "3"
letter: "b"
url: "/docs/linux/man/3-basisofpriceimpl/"
description: "QuantLib::CommodityCurve – Commodity term structure."
---

<p>QuantLib::CommodityCurve &#8211; <code>Commodity</code> term structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/commoditycurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::TermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CommodityCurve</code> (const std::string &amp;name, const <code>CommodityType</code> &amp;commodityType, const <code>Currency</code> &amp;currency, const <code>UnitOfMeasure</code> &amp;unitOfMeasure, const <code>Calendar</code> &amp;calendar, const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; <code>Real</code> &gt; &amp;prices, const <code>DayCounter</code> &amp;dayCounter=<code>Actual365Fixed</code>()) </p>
<p> <code>CommodityCurve</code> (const std::string &amp;name, const <code>CommodityType</code> &amp;commodityType, const <code>Currency</code> &amp;currency, const <code>UnitOfMeasure</code> &amp;unitOfMeasure, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter=<code>Actual365Fixed</code>()) </p>
<h3>Friends</h3>
<p>class <code>CommodityIndex</code> </p>
<h3>Inspectors</h3>
<p>std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;out, const <code>CommodityCurve</code> &amp;curve) </p>
<p> std::string <code>name_</code> </p>
<p> <code>CommodityType</code> <code>commodityType_</code> </p>
<p> <code>UnitOfMeasure</code> <code>unitOfMeasure_</code> </p>
<p> <code>Currency</code> <code>currency_</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>dates_</code> </p>
<p> std::vector&lt; Time &gt; <code>times_</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>data_</code> </p>
<p> <code>Interpolation</code> <code>interpolation_</code> </p>
<p> <code>ForwardFlat</code> <code>interpolator_</code> </p>
<p> boost::shared_ptr&lt; <code>CommodityCurve</code> &gt; <code>basisOfCurve_</code> </p>
<p> <code>Real</code> <code>basisOfCurveUomConversionFactor_</code> </p>
<p> const std::string &amp; <code>name</code> () const </p>
<p> const <code>CommodityType</code> &amp; <code>commodityType</code> () const </p>
<p> const <code>UnitOfMeasure</code> &amp; <code>unitOfMeasure</code> () const </p>
<p> const <code>Currency</code> &amp; <code>currency</code> () const </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i><br />
 const std::vector&lt; Time &gt; &amp; <code>times</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>prices</code> () const </p>
<p> std::vector&lt; std::pair&lt; <code>Date</code>, <code>Real</code> &gt; &gt; <code>nodes</code> () const </p>
<p> bool <code>empty</code> () const </p>
<p> void <code>setPrices</code> (std::map&lt; <code>Date</code>, <code>Real</code> &gt; &amp;prices) </p>
<p> void <code>setBasisOfCurve</code> (const boost::shared_ptr&lt; <code>CommodityCurve</code> &gt; &amp;basisOfCurve) </p>
<p> <code>Real</code> <code>price</code> (const <code>Date</code> &amp;d, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, Integer nearbyOffset) const </p>
<p> <code>Real</code> <code>basisOfPrice</code> (const <code>Date</code> &amp;d) const </p>
<p> <code>Date</code> <code>underlyingPriceDate</code> (const <code>Date</code> &amp;date, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, Integer nearbyOffset) const </p>
<p> const boost::shared_ptr&lt; <code>CommodityCurve</code> &gt; &amp; <code>basisOfCurve</code> () const </p>
<p> <code>Real</code> <code>basisOfPriceImpl</code> (Time t) const </p>
<p> <code>Real</code> <code>priceImpl</code> (Time t) const </p>
<h2>Detailed Description</h2>
<p><code>Commodity</code> term structure. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
