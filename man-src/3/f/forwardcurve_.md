---
title: "forwardcurve_(3)"
name: "forwardcurve_"
section: "3"
letter: "f"
url: "/docs/linux/man/3-forwardcurve_/"
description: "QuantLib::CommodityIndex – base class for commodity indexes"
---

<p>QuantLib::CommodityIndex &#8211; base class for commodity indexes </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/commodityindex.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>, and <code>QuantLib::Observer</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CommodityIndex</code> (const std::string &amp;name, const <code>CommodityType</code> &amp;commodityType, const <code>Currency</code> &amp;currency, const <code>UnitOfMeasure</code> &amp;unitOfMeasure, const <code>Calendar</code> &amp;calendar, Real lotQuantity, const boost::shared_ptr&lt; <code>CommodityCurve</code> &gt; &amp;forwardCurve, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, int nearbyOffset) </p>
<p> void <code>addQuote</code> (const <code>Date</code> &amp;quoteDate, Real quote) </p>
<p> void <code>addQuotes</code> (const std::map&lt; <code>Date</code>, Real &gt; &amp;quotes) </p>
<p> void <code>clearQuotes</code> () </p>
<p> bool <code>isValidQuoteDate</code> (const <code>Date</code> &amp;quoteDate) const<br />
 <i>returns TRUE if the quote date is valid </i><br />
 bool <code>empty</code> () const </p>
<p> bool <code>forwardCurveEmpty</code> () const </p>
<p> const <code>TimeSeries</code>&lt; Real &gt; &amp; <code>quotes</code> () const </p>
<p> <code>Index interface</code> </p>
<p> std::string <code>name</code> () const </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<p> <code>Inspectors</code> </p>
<p> const <code>CommodityType</code> &amp; <code>commodityType</code> () const </p>
<p> const <code>Currency</code> &amp; <code>currency</code> () const </p>
<p> const <code>UnitOfMeasure</code> &amp; <code>unitOfMeasure</code> () const </p>
<p> const <code>Calendar</code> &amp; <code>calendar</code> () const </p>
<p> const boost::shared_ptr&lt; <code>CommodityCurve</code> &gt; &amp; <code>forwardCurve</code> () const </p>
<p> Real <code>lotQuantity</code> () const </p>
<p> Real <code>price</code> (const <code>Date</code> &amp;date) </p>
<p> Real <code>forwardPrice</code> (const <code>Date</code> &amp;date) const </p>
<p> <code>Date</code> <code>lastQuoteDate</code> () const </p>
<h3>Protected Attributes</h3>
<p>std::string <code>name_</code> </p>
<p> <code>CommodityType</code> <code>commodityType_</code> </p>
<p> <code>UnitOfMeasure</code> <code>unitOfMeasure_</code> </p>
<p> <code>Currency</code> <code>currency_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code> </p>
<p> Real <code>lotQuantity_</code> </p>
<p> <code>TimeSeries</code>&lt; Real &gt; <code>quotes_</code> </p>
<p> boost::shared_ptr&lt; <code>CommodityCurve</code> &gt; <code>forwardCurve_</code> </p>
<p> Real <code>forwardCurveUomConversionFactor_</code> </p>
<p> boost::shared_ptr&lt; ExchangeContracts &gt; <code>exchangeContracts_</code> </p>
<p> <code>Integer</code> <code>nearbyOffset_</code> </p>
<h3>Friends</h3>
<p>std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>CommodityIndex</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>base class for commodity indexes</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
