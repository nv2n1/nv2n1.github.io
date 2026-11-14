---
title: "stdexperimentalrangesindirectlyswappable(3)"
name: "stdexperimentalrangesindirectlyswappable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesindirectlyswappable/"
---

std::experimental::ranges::IndirectlySwappable - std::experimental::ranges::IndirectlySwappable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt;class I1, class I2 = I1&gt;

concept bool IndirectlySwappable =

Readable&lt;I1&gt; &amp;&amp; Readable&lt;I2&gt; &amp;&amp;

requires(I1&amp;&amp; i1, I2&amp;&amp; i2) {

    ranges::iter_swap(std::forward&lt;I1&gt;(i1), std::forward&lt;I2&gt;(i2));  (ranges TS)

    ranges::iter_swap(std::forward&lt;I2&gt;(i2), std::forward&lt;I1&gt;(i1));

    ranges::iter_swap(std::forward&lt;I1&gt;(i1), std::forward&lt;I1&gt;(i1));

    ranges::iter_swap(std::forward&lt;I2&gt;(i2), std::forward&lt;I2&gt;(i2));

};
</code></pre> 
&nbsp;This section is incomplete 
&nbsp;Reason: add description and extra caveats 
