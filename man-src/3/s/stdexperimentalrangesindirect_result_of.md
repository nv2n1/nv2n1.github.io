---
title: "stdexperimentalrangesindirect_result_of(3)"
name: "stdexperimentalrangesindirect_result_of"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesindirect_result_of/"
---

std::experimental::ranges::indirect_result_of - std::experimental::ranges::indirect_result_of

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;class&gt;
    struct indirect_result_of {
};
template &lt;class F, class... Is&gt;
(ranges TS)

    requires Invocable&lt;F, ranges::reference_t&lt;Is&gt;...&gt;

struct indirect_result_of&lt;F(Is...)&gt;

    : std::result_of&lt;F(ranges::reference_t&lt;Is&gt; &amp;&amp;...)&gt; {
};
</code></pre>
