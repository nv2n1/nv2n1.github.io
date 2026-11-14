---
title: "setvalue(3)"
name: "setvalue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setvalue/"
description: "QuantLib::IntervalPrice – interval price"
---

<p>QuantLib::IntervalPrice &#8211; interval price </p>
<h2>Synopsis</h2>
<pre><code>static TimeSeries&lt; IntervalPrice &gt; makeSeries (const std::vector&lt; Date &gt; &amp;d, const std::vector&lt; Real &gt; &amp;open, const std::vector&lt; Real &gt; &amp;close, const std::vector&lt; Real &gt; &amp;high, const std::vector&lt; Real &gt; &amp;low)



static std::vector&lt; Real &gt; extractValues (const TimeSeries&lt; IntervalPrice &gt; &amp;, IntervalPrice::Type)



static TimeSeries&lt; Real &gt; extractComponent (const TimeSeries&lt; IntervalPrice &gt; &amp;, enum IntervalPrice::Type)</code></pre>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Open</code>, <code>Close</code>, <code>High</code>, <code>Low</code> }</p>
<h3>Public Member Functions</h3>
<p><code>IntervalPrice</code> (<code>Real</code> open, <code>Real</code> close, <code>Real</code> high, <code>Real</code> low)<br />
 <code>Inspectors</code> </p>
<p> <code>Real</code> <code>open</code> () const </p>
<p> <code>Real</code> <code>close</code> () const </p>
<p> <code>Real</code> <code>high</code> () const </p>
<p> <code>Real</code> <code>low</code> () const </p>
<p> <code>Real</code> <code>value</code> (IntervalPrice::Type) const<br />
 <code>Modifiers</code><br />
 static TimeSeries&lt; IntervalPrice &gt; makeSeries (const std::vector&lt; Date &gt; &amp;d, const std::vector&lt; Real &gt; &amp;open, const std::vector&lt; Real &gt; &amp;close, const std::vector&lt; Real &gt; &amp;high, const std::vector&lt; Real &gt; &amp;low)</p>
<p>static std::vector&lt; Real &gt; extractValues (const TimeSeries&lt; IntervalPrice &gt; &amp;, IntervalPrice::Type)</p>
<p>static TimeSeries&lt; Real &gt; extractComponent (const TimeSeries&lt; IntervalPrice &gt; &amp;, enum IntervalPrice::Type) <code>Helper functions</code> </p>
<pre><code>static TimeSeries&lt; IntervalPrice &gt; makeSeries (const std::vector&lt; Date &gt; &amp;d, const std::vector&lt; Real &gt; &amp;open, const std::vector&lt; Real &gt; &amp;close, const std::vector&lt; Real &gt; &amp;high, const std::vector&lt; Real &gt; &amp;low)



static std::vector&lt; Real &gt; extractValues (const TimeSeries&lt; IntervalPrice &gt; &amp;, IntervalPrice::Type)



static TimeSeries&lt; Real &gt; extractComponent (const TimeSeries&lt; IntervalPrice &gt; &amp;, enum IntervalPrice::Type)</code></pre>
<h2>Detailed Description</h2>
<p>interval price</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
