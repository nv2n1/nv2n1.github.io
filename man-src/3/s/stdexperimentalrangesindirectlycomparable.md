---
title: "stdexperimentalrangesindirectlycomparable(3)"
name: "stdexperimentalrangesindirectlycomparable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesindirectlycomparable/"
---

std::experimental::ranges::IndirectlyComparable - std::experimental::ranges::IndirectlyComparable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt; class I1, class I2, class R = ranges::equal_to&lt;&gt;,

class P1 = ranges::identity, class P2 = ranges::identity &gt;                  (ranges TS)

concept bool IndirectlyComparable =

IndirectRelation&lt;R, ranges::projected&lt;I1, P1&gt;, ranges::projected&lt;I2, P2&gt;&gt;;
</code></pre> 
&nbsp;This section is incomplete 
&nbsp;Reason: add description and extra caveats 
