---
title: "isvalidfixingdate(3)"
name: "isvalidfixingdate"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isvalidfixingdate/"
description: "QuantLib::Index – purely virtual base class for indexes"
---

<p>QuantLib::Index &#8211; purely virtual base class for indexes </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/index.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>InflationIndex</code>, and <code>InterestRateIndex</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual std::string <code>name</code> () const =0<br />
 <i>Returns the name of the index. </i><br />
 virtual <code>Calendar</code> <code>fixingCalendar</code> () const =0<br />
 <i>returns the calendar defining valid fixing dates </i><br />
 virtual bool <code>isValidFixingDate</code> (const <code>Date</code> &amp;fixingDate) const =0<br />
 <i>returns TRUE if the fixing date is a valid one </i><br />
 virtual Real <code>fixing</code> (const <code>Date</code> &amp;fixingDate, bool forecastTodaysFixing=false) const =0<br />
 <i>returns the fixing at the given date </i><br />
 const <code>TimeSeries</code>&lt; Real &gt; &amp; <code>timeSeries</code> () const<br />
 <i>returns the fixing </i><code>TimeSeries</code><br />
 virtual void <code>addFixing</code> (const <code>Date</code> &amp;fixingDate, Real fixing, bool forceOverwrite=false)<br />
 <i>stores the historical fixing at the given date </i><br />
 void <code>addFixings</code> (const <code>TimeSeries</code>&lt; Real &gt; &amp;t, bool forceOverwrite=false)<br />
 <i>stores historical fixings from a </i><code>TimeSeries</code><br />
 template&lt;class DateIterator , class ValueIterator &gt; void <code>addFixings</code> (DateIterator dBegin, DateIterator dEnd, ValueIterator vBegin, bool forceOverwrite=false)<br />
 <i>stores historical fixings at the given dates </i><br />
 void <code>clearFixings</code> ()<br />
 <i>clears all stored historical fixings </i></p>
<h2>Detailed Description</h2>
<p>purely virtual base class for indexes </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>this class performs no check that the provided/requested fixings are for dates in the past, i.e. for dates less than or equal to the evaluation date. It is up to the client code to take care of possible inconsistencies due to &#8216;seeing in the future&#8217;</dl>
<h2>Member Function Documentation</h2>
<h3>virtual std::string name () const [pure virtual]</h3>
<p>Returns the name of the index. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between indexes. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implemented in <code>BMAIndex</code>, <code>InflationIndex</code>, and <code>InterestRateIndex</code>.</p>
<h3>virtual Real fixing (const <code>Date</code> &amp; fixingDate, bool forecastTodaysFixing = false) const [pure virtual]</h3>
<p>returns the fixing at the given date </p>
<p> the date passed as arguments must be the actual calendar date of the fixing; no settlement days must be used. </p>
<p> Implemented in <code>InflationIndex</code>, <code>ZeroInflationIndex</code>, <code>YoYInflationIndex</code>, and <code>InterestRateIndex</code>.</p>
<h3>virtual void addFixing (const <code>Date</code> &amp; fixingDate, Real fixing, bool forceOverwrite = false) [virtual]</h3>
<p>stores the historical fixing at the given date </p>
<p> the date passed as arguments must be the actual calendar date of the fixing; no settlement days must be used.</p>
<h3>void addFixings (const <code>TimeSeries</code>&lt; Real &gt; &amp; t, bool forceOverwrite = false)</h3>
<p>stores historical fixings from a <code>TimeSeries</code> </p>
<p> the dates in the <code>TimeSeries</code> must be the actual calendar dates of the fixings; no settlement days must be used.</p>
<h3>void addFixings (DateIterator dBegin, DateIterator dEnd, ValueIterator vBegin, bool forceOverwrite = false)</h3>
<p>stores historical fixings at the given dates </p>
<p> the dates passed as arguments must be the actual calendar dates of the fixings; no settlement days must be used. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
