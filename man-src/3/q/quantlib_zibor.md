---
title: "quantlib_zibor(3)"
name: "quantlib_zibor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_zibor/"
description: "QuantLib::Zibor – CHF ZIBOR rate"
---

<p>QuantLib::Zibor &#8211; CHF ZIBOR rate </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/zibor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Zibor</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>CHF ZIBOR rate </p>
<p> Zurich Interbank Offered Rate. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is the rate fixed in Zurich by BBA. Use <code>CHFLibor</code> if you&#8217;re interested in the London fixing by BBA.</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>check settlement days, end-of-month adjustment, and day-count convention.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
