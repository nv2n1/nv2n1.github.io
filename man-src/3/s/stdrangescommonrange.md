---
title: "stdrangescommonrange(3)"
name: "stdrangescommonrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangescommonrange/"
---

std::ranges::CommonRange - std::ranges::CommonRange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template&lt;class T&gt;

concept CommonRange = Range&lt;T&gt; &amp;&amp; Same&lt;iterator_t&lt;T&gt;, sentinel_t&lt;T&gt;&gt;;</code></pre> 
The CommonRange concept is a refinement of Range for which ranges::begin and ranges::end return the same type (e.g. all standard library containers). 
