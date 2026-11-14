---
title: "stdrangesviewablerange(3)"
name: "stdrangesviewablerange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesviewablerange/"
---

std::ranges::ViewableRange - std::ranges::ViewableRange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template&lt;class T&gt;

concept ViewableRange =

Range&lt;T&gt; &amp;&amp; (__ForwardingRange&lt;T&gt; || View&lt;std::decay_t&lt;T&gt;&gt;);</code></pre> 
The ViewableRange concept is a refinement of Range that describes a range that can be safely converted into a View. 
(note __ForwardingRange is the exposition-only concept defined in Range) 
