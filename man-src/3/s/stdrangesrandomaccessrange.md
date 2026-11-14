---
title: "stdrangesrandomaccessrange(3)"
name: "stdrangesrandomaccessrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesrandomaccessrange/"
---

std::ranges::RandomAccessRange - std::ranges::RandomAccessRange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template&lt;class T&gt;

concept RandomAccessRange =

BidirectionalRange&lt;T&gt; &amp;&amp; RandomAccessIterator&lt;iterator_t&lt;T&gt;&gt;;</code></pre> 
The RandomAccessRange concept is a refinement of Range for which ranges::begin returns a model of RandomAccessIterator. 
