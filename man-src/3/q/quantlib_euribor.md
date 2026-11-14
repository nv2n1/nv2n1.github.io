---
title: "quantlib_euribor(3)"
name: "quantlib_euribor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_euribor/"
description: "QuantLib::Euribor – Euribor index"
---

<p>QuantLib::Euribor &#8211; Euribor index </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/euribor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<p> Inherited by <code>Euribor10M</code>, <code>Euribor11M</code>, <code>Euribor1M</code>, <code>Euribor1Y</code>, <code>Euribor2M</code>, <code>Euribor2W</code>, <code>Euribor3M</code>, <code>Euribor3W</code>, <code>Euribor4M</code>, <code>Euribor5M</code>, <code>Euribor6M</code>, <code>Euribor7M</code>, <code>Euribor8M</code>, <code>Euribor9M</code>, and <code>EuriborSW</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Euribor</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>Euribor index </p>
<p> <code>Euribor</code> rate fixed by the ECB. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is the rate fixed by the ECB. Use EurLibor if you&#8217;re interested in the London fixing by BBA.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
