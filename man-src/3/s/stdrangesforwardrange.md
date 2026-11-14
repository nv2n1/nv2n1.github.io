---
title: "stdrangesforwardrange(3)"
name: "stdrangesforwardrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesforwardrange/"
---

std::ranges::ForwardRange - std::ranges::ForwardRange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template&lt;class T&gt;

concept ForwardRange = InputRange&lt;T&gt; &amp;&amp; ForwardIterator&lt;iterator_t&lt;T&gt;&gt;;</code></pre> 
The ForwardRange concept is a refinement of Range for which ranges::begin returns a model of ForwardIterator. 
