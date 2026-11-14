---
title: "rebin(3)"
name: "rebin"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rebin/"
description: "QuantLib::TimeBasket – Distribution over a number of dates."
---

<p>QuantLib::TimeBasket &#8211; Distribution over a number of dates. </p>
<h2>Synopsis</h2>
<pre><code>TimeBasket &amp; operator+= (const TimeBasket &amp;other)



TimeBasket &amp; operator-= (const TimeBasket &amp;other)</code></pre>
<p> Inherits std::map&lt;Date,Real&gt;.</p>
<h3>Public Member Functions</h3>
<p><code>TimeBasket</code> (const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; <code>Real</code> &gt; &amp;values)<br />
 <code>Algebra</code> </p>
<pre><code>TimeBasket &amp; operator+= (const TimeBasket &amp;other)



TimeBasket &amp; operator-= (const TimeBasket &amp;other)</code></pre>
<p> <code>Other methods</code> </p>
<p> <code>TimeBasket</code> <code>rebin</code> (const std::vector&lt; <code>Date</code> &gt; &amp;buckets) const<br />
 <i>redistribute the entries over the given dates </i></p>
<h3>Map interface</h3>
<p>typedef super::iterator <code>iterator</code> </p>
<p> typedef super::const_iterator <code>const_iterator</code> </p>
<p> typedef super::reverse_iterator <code>reverse_iterator</code> </p>
<p> typedef super::const_reverse_iterator <code>const_reverse_iterator</code> </p>
<p> bool <code>hasDate</code> (const <code>Date</code> &amp;) const<br />
 <i>membership </i></p>
<h2>Detailed Description</h2>
<p>Distribution over a number of dates.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
