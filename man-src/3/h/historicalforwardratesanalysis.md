---
title: "historicalforwardratesanalysis(3)"
name: "historicalforwardratesanalysis"
section: "3"
letter: "h"
url: "/docs/linux/man/3-historicalforwardratesanalysis/"
description: "ql/models/marketmodels/historicalforwardratesanalysis.hpp – Statistical analysis of historical forward rates."
---

<h2 class="name">NAME</h2>
<p> ql/models/marketmodels/historicalforwardratesanalysis.hpp &#8211; Statistical analysis of historical forward rates. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/matrix.hpp&gt;<br />
 #include &lt;ql/time/calendar.hpp&gt;<br />
 #include &lt;ql/indexes/iborindex.hpp&gt;<br />
 #include &lt;ql/indexes/swapindex.hpp&gt;<br />
 #include &lt;ql/termstructures/yield/piecewiseyieldcurve.hpp&gt;<br />
 #include &lt;ql/termstructures/yield/ratehelpers.hpp&gt;<br />
 #include &lt;ql/quotes/simplequote.hpp&gt;<br />
 #include &lt;ql/math/statistics/sequencestatistics.hpp&gt;<br />
 #include &lt;ql/time/date.hpp&gt; </p>
<h3>Classes</h3>
<p> class <code>HistoricalForwardRatesAnalysisImpl&lt; Traits, Interpolator &gt;</code><br />
 <i>Historical correlation class </i></p>
<h3>Functions</h3>
<p> template&lt;class Traits , class Interpolator &gt; void <code>historicalForwardRatesAnalysis</code> (SequenceStatistics &amp;statistics, std::vector&lt; Date &gt; &amp;skippedDates, std::vector&lt; std::string &gt; &amp;skippedDatesErrorMessage, std::vector&lt; Date &gt; &amp;failedDates, std::vector&lt; std::string &gt; &amp;failedDatesErrorMessage, std::vector&lt; Period &gt; &amp;fixingPeriods, const Date &amp;startDate, const Date &amp;endDate, const Period &amp;step, const boost::shared_ptr&lt; InterestRateIndex &gt; &amp;fwdIndex, const Period &amp;initialGap, const Period &amp;horizon, const std::vector&lt; boost::shared_ptr&lt; IborIndex &gt; &gt; &amp;iborIndexes, const std::vector&lt; boost::shared_ptr&lt; SwapIndex &gt; &gt; &amp;swapIndexes, const DayCounter &amp;yieldCurveDayCounter, Real yieldCurveAccuracy=1.0e-12, const Interpolator &amp;i=Interpolator()) </p>
<h2>Detailed Description</h2>
<p> Statistical analysis of historical forward rates. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
