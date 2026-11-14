---
title: "quantlib_chflibor(3)"
name: "quantlib_chflibor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_chflibor/"
description: "QuantLib::CHFLibor – CHF LIBOR rate"
---

<p>QuantLib::CHFLibor &#8211; CHF LIBOR rate </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/chflibor.hpp&gt; </p>
<p> Inherits <code>QuantLib::Libor</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CHFLibor</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>CHF LIBOR rate </p>
<p> Swiss Franc LIBOR fixed by BBA. </p>
<p> See &lt;<a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1414&gt;. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is the rate fixed in London by BBA. Use ZIBOR if you&#8217;re interested in the Zurich fixing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
