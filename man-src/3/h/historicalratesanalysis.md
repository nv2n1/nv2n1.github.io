---
title: "historicalratesanalysis(3)"
name: "historicalratesanalysis"
section: "3"
letter: "h"
url: "/docs/linux/man/3-historicalratesanalysis/"
description: "ql/models/marketmodels/historicalratesanalysis.hpp – Statistical analysis of historical rates."
---

<h2 class="name">NAME</h2>
<p> ql/models/marketmodels/historicalratesanalysis.hpp &#8211; Statistical analysis of historical rates. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/statistics/sequencestatistics.hpp&gt;<br />
 #include &lt;ql/time/date.hpp&gt; </p>
<h3>Classes</h3>
<p> class <code>HistoricalRatesAnalysis</code><br />
 <i>Historical rate analysis class </i></p>
<h3>Functions</h3>
<p> void <code>historicalRatesAnalysis</code> (SequenceStatistics &amp;statistics, std::vector&lt; Date &gt; &amp;skippedDates, std::vector&lt; std::string &gt; &amp;skippedDatesErrorMessage, const Date &amp;startDate, const Date &amp;endDate, const Period &amp;step, const std::vector&lt; boost::shared_ptr&lt; InterestRateIndex &gt; &gt; &amp;indexes) </p>
<h2>Detailed Description</h2>
<p> Statistical analysis of historical rates. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
