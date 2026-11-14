---
title: "stdrangesinputrange(3)"
name: "stdrangesinputrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesinputrange/"
---

std::ranges::InputRange - std::ranges::InputRange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template&lt;class T&gt;

concept InputRange = Range&lt;T&gt; &amp;&amp; InputIterator&lt;iterator_t&lt;T&gt;&gt;;</code></pre> 
The InputRange concept is a refinement of Range for which ranges::begin returns a model of InputIterator. 
