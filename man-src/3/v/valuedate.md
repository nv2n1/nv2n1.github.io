---
title: "valuedate(3)"
name: "valuedate"
section: "3"
letter: "v"
url: "/docs/linux/man/3-valuedate/"
description: "QuantLib::EURLibor – base class for all BBA EUR LIBOR indexes but the O/N"
---

<p>QuantLib::EURLibor &#8211; base class for all BBA EUR LIBOR indexes but the O/N </p>
<h2>Synopsis</h2>
<pre><code>EURLibor (const Period &amp;tenor, const Handle&lt; YieldTermStructure &gt; &amp;h=Handle&lt; YieldTermStructure &gt;())</code></pre>
<p> Inherits <code>QuantLib::IborIndex</code>. Inherited by <code>EURLibor10M</code>, <code>EURLibor11M</code>, <code>EURLibor1M</code>, <code>EURLibor1Y</code>, <code>EURLibor2M</code>, <code>EURLibor2W</code>, <code>EURLibor3M</code>, <code>EURLibor4M</code>, <code>EURLibor5M</code>, <code>EURLibor6M</code>, <code>EURLibor7M</code>, <code>EURLibor8M</code>, <code>EURLibor9M</code>, and <code>EURLiborSW</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>EURLibor (const Period &amp;tenor, const Handle&lt; YieldTermStructure &gt; &amp;h=Handle&lt; YieldTermStructure &gt;())</code></pre>
<p> <code>Date calculations</code><br />
 see <a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1412<br />
 <code>Date</code> <code>valueDate</code> (const <code>Date</code> &amp;fixingDate) const </p>
<p> <code>Date</code> <code>maturityDate</code> (const <code>Date</code> &amp;valueDate) const</p>
<h2>Detailed Description</h2>
<p>base class for all BBA EUR LIBOR indexes but the O/N </p>
<p> Euro LIBOR fixed by BBA. </p>
<p> See &lt;<a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1414&gt;. </p>
<p> <code>Warning</code></p>
<dl>
<dd>This is the rate fixed in London by BBA. Use <code>Euribor</code> if you&#8217;re interested in the fixing by the ECB.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
