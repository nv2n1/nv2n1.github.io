---
title: "quantlib_euribor365(3)"
name: "quantlib_euribor365"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_euribor365/"
description: "QuantLib::Euribor365 – Actual/365 Euribor index."
---

<p>QuantLib::Euribor365 &#8211; Actual/365 Euribor index. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/euribor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<p> Inherited by <code>Euribor365_10M</code>, <code>Euribor365_11M</code>, <code>Euribor365_1M</code>, <code>Euribor365_1Y</code>, <code>Euribor365_2M</code>, <code>Euribor365_2W</code>, <code>Euribor365_3M</code>, <code>Euribor365_3W</code>, <code>Euribor365_4M</code>, <code>Euribor365_5M</code>, <code>Euribor365_6M</code>, <code>Euribor365_7M</code>, <code>Euribor365_8M</code>, <code>Euribor365_9M</code>, and <code>Euribor365_SW</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Euribor365</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>Actual/365 Euribor index. </p>
<p> <code>Euribor</code> rate adjusted for the mismatch between the actual/360 convention used for <code>Euribor</code> and the actual/365 convention previously used by a few pre-EUR currencies. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
