---
title: "quantlib_dailytenoreurlibor(3)"
name: "quantlib_dailytenoreurlibor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dailytenoreurlibor/"
description: "QuantLib::DailyTenorEURLibor – base class for the one day deposit BBA EUR LIBOR indexes"
---

<p>QuantLib::DailyTenorEURLibor &#8211; base class for the one day deposit BBA EUR LIBOR indexes </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/eurlibor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<p> Inherited by <code>EURLiborON</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DailyTenorEURLibor</code> (<code>Natural</code> settlementDays, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>base class for the one day deposit BBA EUR LIBOR indexes </p>
<p> Euro O/N LIBOR fixed by BBA. It can be also used for T/N and S/N indexes, even if such indexes do not have BBA fixing. </p>
<p> See &lt;<a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1414&gt;. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is the rate fixed in London by BBA. Use <code>Euribor</code> if you&#8217;re interested in the fixing by the ECB.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
