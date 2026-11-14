---
title: "stdrangesbidirectionalrange(3)"
name: "stdrangesbidirectionalrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesbidirectionalrange/"
---

std::ranges::BidirectionalRange - std::ranges::BidirectionalRange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template&lt;class T&gt;

concept BidirectionalRange =

ForwardRange&lt;T&gt; &amp;&amp; BidirectionalIterator&lt;iterator_t&lt;T&gt;&gt;;</code></pre> 
The BidirectionalRange concept is a refinement of Range for which ranges::begin returns a model of BidirectionalIterator. 
