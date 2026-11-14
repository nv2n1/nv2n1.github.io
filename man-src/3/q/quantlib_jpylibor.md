---
title: "quantlib_jpylibor(3)"
name: "quantlib_jpylibor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_jpylibor/"
description: "QuantLib::JPYLibor – JPY LIBOR rate"
---

<p>QuantLib::JPYLibor &#8211; JPY LIBOR rate </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/jpylibor.hpp&gt; </p>
<p> Inherits <code>QuantLib::Libor</code>. </p>
<h3>Public Member Functions</h3>
<p><code>JPYLibor</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>JPY LIBOR rate </p>
<p> Japanese Yen LIBOR fixed by BBA. </p>
<p> See &lt;<a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1414&gt;. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is the rate fixed in London by BBA. Use TIBOR if you&#8217;re interested in the Tokio fixing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
