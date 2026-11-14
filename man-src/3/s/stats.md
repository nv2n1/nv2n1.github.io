---
title: "stats(3)"
name: "stats"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stats/"
description: "QuantLib::HistoricalRatesAnalysis – Historical rate analysis class"
---

<p>QuantLib::HistoricalRatesAnalysis &#8211; Historical rate analysis class </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/models/marketmodels/historicalratesanalysis.hpp&gt;</code></pre>
<h3>Public Member Functions</h3>
<p><code>HistoricalRatesAnalysis</code> (const boost::shared_ptr&lt; <code>SequenceStatistics</code> &gt; &amp;stats, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate, const <code>Period</code> &amp;step, const std::vector&lt; boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &gt; &amp;indexes) </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>skippedDates</code> () const </p>
<p> const std::vector&lt; std::string &gt; &amp; <code>skippedDatesErrorMessage</code> () const </p>
<p> const boost::shared_ptr&lt; <code>SequenceStatistics</code> &gt; &amp; <code>stats</code> () const</p>
<h2>Detailed Description</h2>
<p>Historical rate analysis class</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
