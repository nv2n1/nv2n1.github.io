---
title: "quantlib_dailytenoreuribor365(3)"
name: "quantlib_dailytenoreuribor365"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dailytenoreuribor365/"
description: "QuantLib::DailyTenorEuribor365 – Daily tenor Actual/365 Euribor index."
---

<p>QuantLib::DailyTenorEuribor365 &#8211; Daily tenor Actual/365 Euribor index. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/euribor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DailyTenorEuribor365</code> (<code>Natural</code> settlementDays, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>Daily tenor Actual/365 Euribor index. </p>
<p> <code>Euribor</code> rate adjusted for the mismatch between the actual/360 convention used for <code>Euribor</code> and the actual/365 convention previously used by a few pre-EUR currencies. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
