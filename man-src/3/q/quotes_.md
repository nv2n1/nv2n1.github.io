---
title: "quotes_(3)"
name: "quotes_"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quotes_/"
description: "QuantLib::CommodityIndex – base class for commodity indexes"
---

<p>QuantLib::CommodityIndex &#8211; base class for commodity indexes </p>
<h2>Synopsis</h2>
<pre><code>const CommodityType &amp; commodityType () const



const Currency &amp; currency () const



const UnitOfMeasure &amp; unitOfMeasure () const



const Calendar &amp; calendar () const



const boost::shared_ptr&lt; CommodityCurve &gt; &amp; forwardCurve () const



Real lotQuantity () const



Real price (const Date &amp;date)



Real forwardPrice (const Date &amp;date) const



Date lastQuoteDate () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Observable</code>, and <code>QuantLib::Observer</code>.</p>
<h3>Public Member Functions</h3>
<p><code>CommodityIndex</code> (const std::string &amp;name, const <code>CommodityType</code> &amp;commodityType, const <code>Currency</code> &amp;currency, const <code>UnitOfMeasure</code> &amp;unitOfMeasure, const <code>Calendar</code> &amp;calendar, Real lotQuantity, const boost::shared_ptr&lt; <code>CommodityCurve</code> &gt; &amp;forwardCurve, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, int nearbyOffset) </p>
<p> void <code>addQuote</code> (const <code>Date</code> &amp;quoteDate, Real quote) </p>
<p> void <code>addQuotes</code> (const std::map&lt; <code>Date</code>, Real &gt; &amp;quotes) </p>
<p> void <code>clearQuotes</code> () </p>
<p> bool <code>isValidQuoteDate</code> (const <code>Date</code> &amp;quoteDate) const<br />
 <i>returns TRUE if the quote date is valid </i><br />
 bool <code>empty</code> () const </p>
<p> bool <code>forwardCurveEmpty</code> () const </p>
<p> const <code>TimeSeries</code>&lt; Real &gt; &amp; <code>quotes</code> () const<br />
 <code>Index interface</code> </p>
<p> std::string <code>name</code> () const<br />
 <code>Observer interface</code><br />
 const CommodityType &amp; commodityType () const</p>
<p>const Currency &amp; currency () const</p>
<p>const UnitOfMeasure &amp; unitOfMeasure () const</p>
<p>const Calendar &amp; calendar () const</p>
<p>const boost::shared_ptr&lt; CommodityCurve &gt; &amp; forwardCurve () const</p>
<p>Real lotQuantity () const</p>
<p>Real price (const Date &amp;date)</p>
<p>Real forwardPrice (const Date &amp;date) const</p>
<p>Date lastQuoteDate () const</p>
<p>Protected Attributes <code>Inspectors</code> </p>
<pre><code>const CommodityType &amp; commodityType () const



const Currency &amp; currency () const



const UnitOfMeasure &amp; unitOfMeasure () const



const Calendar &amp; calendar () const



const boost::shared_ptr&lt; CommodityCurve &gt; &amp; forwardCurve () const



Real lotQuantity () const



Real price (const Date &amp;date)



Real forwardPrice (const Date &amp;date) const



Date lastQuoteDate () const



Protected Attributes</code></pre>
<p> std::string <code>name_</code> </p>
<p> <code>CommodityType</code> <code>commodityType_</code> </p>
<p> <code>UnitOfMeasure</code> <code>unitOfMeasure_</code> </p>
<p> <code>Currency</code> <code>currency_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code> </p>
<p> Real <code>lotQuantity_</code> </p>
<p> <code>TimeSeries</code>&lt; Real &gt; <code>quotes_</code> </p>
<p> boost::shared_ptr&lt; <code>CommodityCurve</code> &gt; <code>forwardCurve_</code> </p>
<p> Real <code>forwardCurveUomConversionFactor_</code> </p>
<p> boost::shared_ptr&lt; ExchangeContracts &gt; <code>exchangeContracts_</code> </p>
<p> <code>Integer</code> <code>nearbyOffset_</code></p>
<h3>Friends</h3>
<p>std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>CommodityIndex</code> &amp;)</p>
<h2>Detailed Description</h2>
<p>base class for commodity indexes</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
