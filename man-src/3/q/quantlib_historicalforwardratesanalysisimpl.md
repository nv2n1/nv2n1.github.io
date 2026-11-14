---
title: "quantlib_historicalforwardratesanalysisimpl(3)"
name: "quantlib_historicalforwardratesanalysisimpl"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_historicalforwardratesanalysisimpl/"
description: "QuantLib::HistoricalForwardRatesAnalysisImpl – Historical correlation class"
---

<p>QuantLib::HistoricalForwardRatesAnalysisImpl &#8211; Historical correlation class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/historicalforwardratesanalysis.hpp&gt; </p>
<p> Inherits QuantLib::HistoricalForwardRatesAnalysis. </p>
<h3>Public Member Functions</h3>
<p><code>HistoricalForwardRatesAnalysisImpl</code> (const boost::shared_ptr&lt; <code>SequenceStatistics</code> &gt; &amp;stats, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate, const <code>Period</code> &amp;step, const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp;fwdIndex, const <code>Period</code> &amp;initialGap, const <code>Period</code> &amp;horizon, const std::vector&lt; boost::shared_ptr&lt; <code>IborIndex</code> &gt; &gt; &amp;iborIndexes, const std::vector&lt; boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &gt; &amp;swapIndexes, const <code>DayCounter</code> &amp;yieldCurveDayCounter, Real yieldCurveAccuracy) </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>skippedDates</code> () const </p>
<p> const std::vector&lt; std::string &gt; &amp; <code>skippedDatesErrorMessage</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>failedDates</code> () const </p>
<p> const std::vector&lt; std::string &gt; &amp; <code>failedDatesErrorMessage</code> () const </p>
<p> const std::vector&lt; <code>Period</code> &gt; &amp; <code>fixingPeriods</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Traits, class Interpolator&gt; class QuantLib::HistoricalForwardRatesAnalysisImpl&lt; Traits, Interpolator &gt;</h3>
<p>Historical correlation class </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
