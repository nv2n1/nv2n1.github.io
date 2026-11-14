---
title: "stdexperimentalrangesindirectstrictweakorder(3)"
name: "stdexperimentalrangesindirectstrictweakorder"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesindirectstrictweakorder/"
---

std::experimental::ranges::IndirectStrictWeakOrder - std::experimental::ranges::IndirectStrictWeakOrder

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt; class F, class I1, class I2 = I1 &gt;

concept bool IndirectStrictWeakOrder =

Readable&lt;I1&gt; &amp;&amp; Readable&lt;I2&gt; &amp;&amp;

CopyConstructible&lt;F&gt; &amp;&amp;

StrictWeakOrder&lt;F&amp;, ranges::value_type_t&lt;I1&gt;&amp;, ranges::value_type_t&lt;I2&gt;&amp;&gt; &amp;&amp;  (ranges TS)

StrictWeakOrder&lt;F&amp;, ranges::value_type_t&lt;I1&gt;&amp;, ranges::reference_t&lt;I2&gt;&gt; &amp;&amp;

StrictWeakOrder&lt;F&amp;, ranges::reference_t&lt;I1&gt;, ranges::value_type_t&lt;I2&gt;&amp;&gt; &amp;&amp;

StrictWeakOrder&lt;F&amp;, ranges::reference_t&lt;I1&gt;, ranges::reference_t&lt;I2&gt;&gt; &amp;&amp;

StrictWeakOrder&lt;F&amp;, ranges::iter_common_reference_t&lt;I1&gt;,

ranges::iter_common_reference_t&lt;I2&gt;&gt;;
</code></pre> 
&nbsp;This section is incomplete 
&nbsp;Reason: add description and extra caveats 
