---
title: "garch11(3)"
name: "garch11"
section: "3"
letter: "g"
url: "/docs/linux/man/3-garch11/"
description: "QuantLib::Garch11 – GARCH volatility model."
---

<p>QuantLib::Garch11 &#8211; GARCH volatility model. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/volatility/garch.hpp&gt; </p>
<p> Inherits QuantLib::VolatilityCompositor. </p>
<h3>Public Member Functions</h3>
<p><code>Garch11</code> (<code>Real</code> a, <code>Real</code> b, <code>Real</code> vl) </p>
<p> <code>Garch11</code> (const <code>TimeSeries</code>&lt; Volatility &gt; &amp;qs) </p>
<p> <code>TimeSeries</code>&lt; Volatility &gt; <code>calculate</code> (const <code>TimeSeries</code>&lt; Volatility &gt; &amp;quoteSeries) </p>
<p> <code>TimeSeries</code>&lt; Volatility &gt; <code>calculate</code> (const <code>TimeSeries</code>&lt; Volatility &gt; &amp;quoteSeries, <code>Real</code>, <code>Real</code>, <code>Real</code>) </p>
<p> void <code>calibrate</code> (const <code>TimeSeries</code>&lt; Volatility &gt; &amp;quoteSeries) </p>
<h2>Detailed Description</h2>
<p>GARCH volatility model. </p>
<p> Volatilities are assumed to be expressed on an annual basis. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
