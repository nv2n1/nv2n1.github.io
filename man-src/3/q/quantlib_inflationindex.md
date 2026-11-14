---
title: "quantlib_inflationindex(3)"
name: "quantlib_inflationindex"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_inflationindex/"
description: "QuantLib::InflationIndex – Base class for inflation-rate indexes,."
---

<p>QuantLib::InflationIndex &#8211; Base class for inflation-rate indexes,. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/inflationindex.hpp&gt; </p>
<p> Inherits <code>QuantLib::Index</code>, and <code>QuantLib::Observer</code>. </p>
<p> Inherited by <code>YoYInflationIndex</code>, and <code>ZeroInflationIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>InflationIndex</code> (const std::string &amp;familyName, const <code>Region</code> &amp;region, bool revised, bool interpolated, <code>Frequency</code> frequency, const <code>Period</code> &amp;availabilitiyLag, const <code>Currency</code> &amp;currency) </p>
<p> <code>Index interface</code> </p>
<p> std::string <code>name</code> () const<br />
 <i>Returns the name of the index. </i><br />
 <code>Calendar</code> <code>fixingCalendar</code> () const </p>
<p> bool <code>isValidFixingDate</code> (const <code>Date</code> &amp;fixingDate) const<br />
 <i>returns TRUE if the fixing date is a valid one </i><br />
 virtual Rate <code>fixing</code> (const <code>Date</code> &amp;fixingDate, bool forecastTodaysFixing=false) const =0 </p>
<p> void <code>addFixing</code> (const <code>Date</code> &amp;fixingDate, Rate fixing, bool forceOverwrite=false) </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<p> <code>Inspectors</code> </p>
<p> std::string <code>familyName</code> () const </p>
<p> <code>Region</code> <code>region</code> () const </p>
<p> bool <code>revised</code> () const </p>
<p> bool <code>interpolated</code> () const </p>
<p> <code>Frequency</code> <code>frequency</code> () const </p>
<p> <code>Period</code> <code>availabilityLag</code> () const </p>
<p> <code>Currency</code> <code>currency</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>Date</code> <code>referenceDate_</code> </p>
<p> std::string <code>familyName_</code> </p>
<p> <code>Region</code> <code>region_</code> </p>
<p> bool <code>revised_</code> </p>
<p> bool <code>interpolated_</code> </p>
<p> <code>Frequency</code> <code>frequency_</code> </p>
<p> <code>Period</code> <code>availabilityLag_</code> </p>
<p> <code>Currency</code> <code>currency_</code> </p>
<h2>Detailed Description</h2>
<p>Base class for inflation-rate indexes,.</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p>Returns the name of the index. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between indexes. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implements <code>Index</code>.</p>
<h3><code>Calendar</code> fixingCalendar () const [virtual]</h3>
<p>Inflation indices do not have fixing calendars. An inflation index value is valid for every day (including weekends) of a calendar period. I.e. it uses the <code>NullCalendar</code> as its fixing calendar. </p>
<p> Implements <code>Index</code>.</p>
<h3>virtual Rate fixing (const <code>Date</code> &amp; fixingDate, bool forecastTodaysFixing = false) const [pure virtual]</h3>
<p>Forecasting index values requires an inflation term structure. The inflation term structure (ITS) defines the usual lag (not the index). I.e. an ITS is always relatve to a base date that is earlier than its asof date. This must be so because indices are available only with a lag. However, the index availability lag only sets a minimum lag for the ITS. An ITS may be relative to an earlier date, e.g. an index may have a 2-month delay in publication but the inflation swaps may take as their base the index 3 months before. </p>
<p> Implements <code>Index</code>. </p>
<p> Implemented in <code>ZeroInflationIndex</code>, and <code>YoYInflationIndex</code>.</p>
<h3>void addFixing (const <code>Date</code> &amp; fixingDate, Rate fixing, bool forceOverwrite = false)</h3>
<p>this method creates all the &#8216;fixings&#8217; for the relevant period of the index. E.g. for monthly indices it will put the same value in every calendar day in the month.</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>.</p>
<h3>bool interpolated () const</h3>
<p>Forecasting index values using an inflation term structure uses the interpolation of the inflation term structure unless interpolation is set to false. In this case the extrapolated values are constant within each period taking the mid-period extrapolated value.</p>
<h3><code>Period</code> availabilityLag () const</h3>
<p>The availability lag describes when the index is <i>available</i>, not how it is used. Specifically the fixing for, say, January, may only be available in April but the index will always return the index value applicable for January as its January fixing (independent of the lag in availability). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
