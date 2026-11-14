---
title: "quantlib_simpledaycounter(3)"
name: "quantlib_simpledaycounter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_simpledaycounter/"
description: "QuantLib::SimpleDayCounter – Simple day counter for reproducing theoretical calculations."
---

<p>QuantLib::SimpleDayCounter &#8211; Simple day counter for reproducing theoretical calculations. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/daycounters/simpledaycounter.hpp&gt; </p>
<p> Inherits <code>QuantLib::DayCounter</code>. </p>
<h2>Detailed Description</h2>
<p>Simple day counter for reproducing theoretical calculations. </p>
<p> This day counter tries to ensure that whole-month distances are returned as a simple fraction, i.e., 1 year = 1.0, 6 months = 0.5, 3 months = 0.25 and so forth. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>this day counter should be used together with <code>NullCalendar</code>, which ensures that dates at whole-month distances share the same day of month. It is <code>not</code> guaranteed to work with any other calendar.</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the results is checked against known good values.</dl>
<p> <code>Examples: </code> </p>
<p> <code>FittedBondCurve.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
