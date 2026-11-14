---
title: "quantlib_tibor(3)"
name: "quantlib_tibor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_tibor/"
description: "QuantLib::Tibor – JPY TIBOR index"
---

<p>QuantLib::Tibor &#8211; JPY TIBOR index </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/tibor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Tibor</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>JPY TIBOR index </p>
<p> Tokyo Interbank Offered Rate. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is the rate fixed in Tokio by JBA. Use <code>JPYLibor</code> if you&#8217;re interested in the London fixing by BBA.</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>check settlement days and end-of-month adjustment.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
