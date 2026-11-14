---
title: "stdsub_matchlength(3)"
name: "stdsub_matchlength"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsub_matchlength/"
---

std::sub_match&lt;BidirIt&gt;::length - std::sub_match&lt;BidirIt&gt;::length

<h2>Synopsis</h2>

<pre><code>difference_type length() const;
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Returns the number of characters in the match, i.e. std::distance(first, second) if the match is valid, 0 otherwise. 

<h2>Complexity</h2>

Constant
