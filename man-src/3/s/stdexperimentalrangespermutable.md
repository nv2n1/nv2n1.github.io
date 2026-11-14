---
title: "stdexperimentalrangespermutable(3)"
name: "stdexperimentalrangespermutable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangespermutable/"
---

std::experimental::ranges::Permutable - std::experimental::ranges::Permutable

<h2>Synopsis</h2>

<pre><code>template &lt;class I&gt;

concept bool Permutable =

ForwardIterator&lt;I&gt; &amp;&amp;               (ranges TS)

IndirectlyMovableStorable&lt;I, I&gt; &amp;&amp;

IndirectlySwappable&lt;I, I&gt;;</code></pre> 
The Permutable concept specifies the common requirements of algorithms that reorder elements in place by moving or swapping them (for example, ranges::rotate). 
