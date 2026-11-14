---
title: "stdexperimentalrangessortable(3)"
name: "stdexperimentalrangessortable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangessortable/"
---

std::experimental::ranges::Sortable - std::experimental::ranges::Sortable

<h2>Synopsis</h2>

<pre><code>template &lt;class I, class R = ranges::less&lt;&gt;, class P = ranges::identity&gt;

concept bool Sortable =                                                   (ranges TS)

Permutable&lt;I&gt; &amp;&amp;

IndirectStrictWeakOrder&lt;R, ranges::projected&lt;I, P&gt;&gt;;</code></pre> 
The Sortable concept specifies the common requirements of algorithms that permute sequences into ordered sequences (for example, ranges::sort). 
