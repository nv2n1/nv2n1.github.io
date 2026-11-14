---
title: "cdor(3)"
name: "cdor"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdor/"
description: "QuantLib::Cdor – CDOR rate"
---

<p>QuantLib::Cdor &#8211; CDOR rate </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/cdor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Cdor</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>CDOR rate </p>
<p> Canadian Dollar Offered Rate fixed by IDA. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is the rate fixed in <code>Canada</code> by IDA. Use <code>CADLibor</code> if you&#8217;re interested in the London fixing by BBA.</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>check settlement days, end-of-month adjustment, and day-count convention.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
