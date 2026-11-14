---
title: "stdrangesoutputrange(3)"
name: "stdrangesoutputrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesoutputrange/"
---

std::ranges::OutputRange - std::ranges::OutputRange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template&lt;class R, class T&gt;

concept OutputRange = Range&lt;R&gt; &amp;&amp; OutputIterator&lt;iterator_t&lt;R&gt;, T&gt;;</code></pre> 
The OutputRange concept is a refinement of Range for which ranges::begin returns a model of OutputIterator. 
