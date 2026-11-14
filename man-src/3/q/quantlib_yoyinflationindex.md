---
title: "quantlib_yoyinflationindex(3)"
name: "quantlib_yoyinflationindex"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_yoyinflationindex/"
description: "QuantLib::YoYInflationIndex – Base class for year-on-year inflation indices."
---

<p>QuantLib::YoYInflationIndex &#8211; Base class for year-on-year inflation indices. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/inflationindex.hpp&gt; </p>
<p> Inherits <code>QuantLib::InflationIndex</code>. </p>
<p> Inherited by <code>YYEUHICP</code>, <code>YYEUHICPr</code>, <code>YYUKRPI</code>, and <code>YYUKRPIr</code>. </p>
<h3>Public Member Functions</h3>
<p><code>YoYInflationIndex</code> (const std::string &amp;familyName, const <code>Region</code> &amp;region, bool revised, bool interpolated, bool ratio, <code>Frequency</code> frequency, const <code>Period</code> &amp;availabilityLag, const <code>Currency</code> &amp;currency, const <code>Handle</code>&lt; <code>YoYInflationTermStructure</code> &gt; &amp;ts=<code>Handle</code>&lt; <code>YoYInflationTermStructure</code> &gt;()) </p>
<p> <code>Rate</code> <code>fixing</code> (const <code>Date</code> &amp;fixingDate, bool forecastTodaysFixing=false) const </p>
<p> bool <code>ratio</code> () const </p>
<p> <code>Handle</code>&lt; <code>YoYInflationTermStructure</code> &gt; <code>yoyInflationTermStructure</code> () const </p>
<h2>Detailed Description</h2>
<p>Base class for year-on-year inflation indices. </p>
<p> These may be genuine indices published on, say, Bloomberg, or &#8216;fake&#8217; indices that are defined as the ratio of an index at different time points.</p>
<h2>Member Function Documentation</h2>
<h3><code>Rate</code> fixing (const <code>Date</code> &amp; fixingDate, bool forecastTodaysFixing = false) const [virtual]</h3>
<p>Forecasting index values requires an inflation term structure. The inflation term structure (ITS) defines the usual lag (not the index). I.e. an ITS is always relatve to a base date that is earlier than its asof date. This must be so because indices are available only with a lag. However, the index availability lag only sets a minimum lag for the ITS. An ITS may be relative to an earlier date, e.g. an index may have a 2-month delay in publication but the inflation swaps may take as their base the index 3 months before. </p>
<p> Implements <code>InflationIndex</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
