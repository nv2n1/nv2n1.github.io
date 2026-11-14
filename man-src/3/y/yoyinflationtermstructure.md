---
title: "yoyinflationtermstructure(3)"
name: "yoyinflationtermstructure"
section: "3"
letter: "y"
url: "/docs/linux/man/3-yoyinflationtermstructure/"
description: "QuantLib::YoYInflationIndex – Base class for year-on-year inflation indices."
---

<p>QuantLib::YoYInflationIndex &#8211; Base class for year-on-year inflation indices. </p>
<h2>Synopsis</h2>
<pre><code>YoYInflationIndex (const std::string &amp;familyName, const Region &amp;region, bool revised, bool interpolated, bool ratio, Frequency frequency, const Period &amp;availabilityLag, const Currency &amp;currency, const Handle&lt; YoYInflationTermStructure &gt; &amp;ts=Handle&lt; YoYInflationTermStructure &gt;())



Rate fixing (const Date &amp;fixingDate, bool forecastTodaysFixing=false) const



bool ratio () const



Handle&lt; YoYInflationTermStructure &gt; yoyInflationTermStructure () const</code></pre>
<p> Inherits <code>QuantLib::InflationIndex</code>. Inherited by <code>YYEUHICP</code>, <code>YYEUHICPr</code>, <code>YYUKRPI</code>, and <code>YYUKRPIr</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>YoYInflationIndex (const std::string &amp;familyName, const Region &amp;region, bool revised, bool interpolated, bool ratio, Frequency frequency, const Period &amp;availabilityLag, const Currency &amp;currency, const Handle&lt; YoYInflationTermStructure &gt; &amp;ts=Handle&lt; YoYInflationTermStructure &gt;())



Rate fixing (const Date &amp;fixingDate, bool forecastTodaysFixing=false) const



bool ratio () const



Handle&lt; YoYInflationTermStructure &gt; yoyInflationTermStructure () const</code></pre>
<h2>Detailed Description</h2>
<p>Base class for year-on-year inflation indices. </p>
<p> These may be genuine indices published on, say, Bloomberg, or &#8216;fake&#8217; indices that are defined as the ratio of an index at different time points.</p>
<h2>Member Function Documentation</h2>
<h3><code>Rate</code> fixing (const <code>Date</code> &amp; fixingDate, bool forecastTodaysFixing = false) const [virtual]</h3>
<p>Forecasting index values requires an inflation term structure. The inflation term structure (ITS) defines the usual lag (not the index). I.e. an ITS is always relatve to a base date that is earlier than its asof date. This must be so because indices are available only with a lag. However, the index availability lag only sets a minimum lag for the ITS. An ITS may be relative to an earlier date, e.g. an index may have a 2-month delay in publication but the inflation swaps may take as their base the index 3 months before. </p>
<p> Implements <code>InflationIndex</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
