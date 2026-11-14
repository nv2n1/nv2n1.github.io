---
title: "stdrangescontiguousrange(3)"
name: "stdrangescontiguousrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangescontiguousrange/"
---

std::ranges::ContiguousRange - std::ranges::ContiguousRange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template&lt;class T&gt;

concept ContiguousRange =

RandomAccessRange&lt;T&gt; &amp;&amp; ContiguousIterator&lt;iterator_t&lt;T&gt;&gt; &amp;&amp;

requires(T&amp; t) {

    { ranges::data(t) } -&gt; Same&lt;std::add_pointer_t&lt;iter_reference_t&lt;iterator_t&lt;T&gt;&gt;&gt;&gt;;

};</code></pre> 
The ContiguousRange concept is a refinement of Range for which ranges::begin returns a model of ContiguousIterator and the customization point ranges::data is usable. 
