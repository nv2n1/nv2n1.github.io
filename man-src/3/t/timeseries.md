---
title: "timeseries(3)"
name: "timeseries"
section: "3"
letter: "t"
url: "/docs/linux/man/3-timeseries/"
description: "QuantLib::Index – purely virtual base class for indexes"
---

<p>QuantLib::Index &#8211; purely virtual base class for indexes </p>
<h2>Synopsis</h2>
<pre><code>virtual std::string name () const =0


Returns the name of the index.


virtual Calendar fixingCalendar () const =0


returns the calendar defining valid fixing dates


virtual bool isValidFixingDate (const Date &amp;fixingDate) const =0


returns TRUE if the fixing date is a valid one


virtual Real fixing (const Date &amp;fixingDate, bool forecastTodaysFixing=false) const =0


returns the fixing at the given date


const TimeSeries&lt; Real &gt; &amp; timeSeries () const


returns the fixing TimeSeries


virtual void addFixing (const Date &amp;fixingDate, Real fixing, bool forceOverwrite=false)


stores the historical fixing at the given date


void addFixings (const TimeSeries&lt; Real &gt; &amp;t, bool forceOverwrite=false)


stores historical fixings from a TimeSeries


template&lt;class DateIterator , class ValueIterator &gt; void addFixings (DateIterator dBegin, DateIterator dEnd, ValueIterator vBegin, bool forceOverwrite=false)


stores historical fixings at the given dates


void clearFixings ()


clears all stored historical fixings</code></pre>
<p> Inherits <code>QuantLib::Observable</code>. Inherited by <code>InflationIndex</code>, and <code>InterestRateIndex</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual std::string name () const =0


Returns the name of the index.


virtual Calendar fixingCalendar () const =0


returns the calendar defining valid fixing dates


virtual bool isValidFixingDate (const Date &amp;fixingDate) const =0


returns TRUE if the fixing date is a valid one


virtual Real fixing (const Date &amp;fixingDate, bool forecastTodaysFixing=false) const =0


returns the fixing at the given date


const TimeSeries&lt; Real &gt; &amp; timeSeries () const


returns the fixing TimeSeries


virtual void addFixing (const Date &amp;fixingDate, Real fixing, bool forceOverwrite=false)


stores the historical fixing at the given date


void addFixings (const TimeSeries&lt; Real &gt; &amp;t, bool forceOverwrite=false)


stores historical fixings from a TimeSeries


template&lt;class DateIterator , class ValueIterator &gt; void addFixings (DateIterator dBegin, DateIterator dEnd, ValueIterator vBegin, bool forceOverwrite=false)


stores historical fixings at the given dates


void clearFixings ()


clears all stored historical fixings</code></pre>
<h2>Detailed Description</h2>
<p>purely virtual base class for indexes </p>
<p> <code>Warning</code></p>
<dl>
<dd>this class performs no check that the provided/requested fixings are for dates in the past, i.e. for dates less than or equal to the evaluation date. It is up to the client code to take care of possible inconsistencies due to &#8216;seeing in the future&#8217;</dl>
<h2>Member Function Documentation</h2>
<h3>virtual std::string name () const [pure virtual]</h3>
<p>Returns the name of the index. </p>
<p> <code>Warning</code></p>
<dl>
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
<p> the dates passed as arguments must be the actual calendar dates of the fixings; no settlement days must be used.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
