---
title: "stdexperimentalrangesmergeable(3)"
name: "stdexperimentalrangesmergeable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesmergeable/"
---

std::experimental::ranges::Mergeable - std::experimental::ranges::Mergeable

<h2>Synopsis</h2>

<pre><code>template &lt; class I1, class I2, class Out, class R = ranges::less&lt;&gt;,

class P1 = ranges::identity, class P2 = ranges::identity &gt;

concept bool Mergeable =

InputIterator&lt;I1&gt; &amp;&amp;

InputIterator&lt;I2&gt; &amp;&amp;                                                               (ranges TS)

WeaklyIncrementable&lt;Out&gt; &amp;&amp;

IndirectlyCopyable&lt;I1, Out&gt; &amp;&amp;

IndirectlyCopyable&lt;I2, Out&gt; &amp;&amp;

IndirectStrictWeakOrder&lt;R, ranges::projected&lt;I1, P1&gt;, ranges::projected&lt;I2, P2&gt;&gt;;</code></pre> 
The Mergeable concept specifies the common requirements of algorithms that merge sorted sequences into an output sequence by copying the elements (for example, ranges::merge). 
