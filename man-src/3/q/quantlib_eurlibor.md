---
title: "quantlib_eurlibor(3)"
name: "quantlib_eurlibor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_eurlibor/"
description: "QuantLib::EURLibor – base class for all BBA EUR LIBOR indexes but the O/N"
---

<p>QuantLib::EURLibor &#8211; base class for all BBA EUR LIBOR indexes but the O/N </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/eurlibor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<p> Inherited by <code>EURLibor10M</code>, <code>EURLibor11M</code>, <code>EURLibor1M</code>, <code>EURLibor1Y</code>, <code>EURLibor2M</code>, <code>EURLibor2W</code>, <code>EURLibor3M</code>, <code>EURLibor4M</code>, <code>EURLibor5M</code>, <code>EURLibor6M</code>, <code>EURLibor7M</code>, <code>EURLibor8M</code>, <code>EURLibor9M</code>, and <code>EURLiborSW</code>. </p>
<h3>Public Member Functions</h3>
<p><code>EURLibor</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> <code>Date calculations</code><br />
 see <a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1412 </p>
<p> <code>Date</code> <code>valueDate</code> (const <code>Date</code> &amp;fixingDate) const </p>
<p> <code>Date</code> <code>maturityDate</code> (const <code>Date</code> &amp;valueDate) const </p>
<h2>Detailed Description</h2>
<p>base class for all BBA EUR LIBOR indexes but the O/N </p>
<p> Euro LIBOR fixed by BBA. </p>
<p> See &lt;<a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1414&gt;. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is the rate fixed in London by BBA. Use <code>Euribor</code> if you&#8217;re interested in the fixing by the ECB.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
