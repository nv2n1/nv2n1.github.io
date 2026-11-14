---
title: "extractcomponent(3)"
name: "extractcomponent"
section: "3"
letter: "e"
url: "/docs/linux/man/3-extractcomponent/"
description: "QuantLib::IntervalPrice – interval price"
---

<p>QuantLib::IntervalPrice &#8211; interval price </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/prices.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Open</code>, <code>Close</code>, <code>High</code>, <code>Low</code> } </p>
<h3>Public Member Functions</h3>
<p><code>IntervalPrice</code> (<code>Real</code> open, <code>Real</code> close, <code>Real</code> high, <code>Real</code> low) </p>
<p> <code>Inspectors</code> </p>
<p> <code>Real</code> <code>open</code> () const </p>
<p> <code>Real</code> <code>close</code> () const </p>
<p> <code>Real</code> <code>high</code> () const </p>
<p> <code>Real</code> <code>low</code> () const </p>
<p> <code>Real</code> <code>value</code> (IntervalPrice::Type) const </p>
<p> <code>Modifiers</code> </p>
<p> void <code>setValue</code> (<code>Real</code> value, IntervalPrice::Type) </p>
<p> void <code>setValues</code> (<code>Real</code> open, <code>Real</code> close, <code>Real</code> high, <code>Real</code> low) </p>
<h3>Static Public Member Functions</h3>
<p><code>Helper functions</code> </p>
<p> static <code>TimeSeries</code>&lt; <code>IntervalPrice</code> &gt; <code>makeSeries</code> (const std::vector&lt; <code>Date</code> &gt; &amp;d, const std::vector&lt; <code>Real</code> &gt; &amp;open, const std::vector&lt; <code>Real</code> &gt; &amp;close, const std::vector&lt; <code>Real</code> &gt; &amp;high, const std::vector&lt; <code>Real</code> &gt; &amp;low) </p>
<p> static std::vector&lt; <code>Real</code> &gt; <code>extractValues</code> (const <code>TimeSeries</code>&lt; <code>IntervalPrice</code> &gt; &amp;, IntervalPrice::Type) </p>
<p> static <code>TimeSeries</code>&lt; <code>Real</code> &gt; <code>extractComponent</code> (const <code>TimeSeries</code>&lt; <code>IntervalPrice</code> &gt; &amp;, enum IntervalPrice::Type) </p>
<h2>Detailed Description</h2>
<p>interval price </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
