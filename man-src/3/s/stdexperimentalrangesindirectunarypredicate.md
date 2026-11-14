---
title: "stdexperimentalrangesindirectunarypredicate(3)"
name: "stdexperimentalrangesindirectunarypredicate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesindirectunarypredicate/"
---

std::experimental::ranges::IndirectUnaryPredicate - std::experimental::ranges::IndirectUnaryPredicate

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt;class F, class I&gt;

concept bool IndirectUnaryPredicate =

Readable&lt;I&gt; &amp;&amp; CopyConstructible&lt;F&gt; &amp;&amp;              (ranges TS)

Predicate&lt;F&amp;, ranges::value_type_t&lt;I&gt;&amp;&gt; &amp;&amp;

Predicate&lt;F&amp;, ranges::reference_t&lt;I&gt;&gt; &amp;&amp;

Predicate&lt;F&amp;, ranges::iter_common_reference_t&lt;I&gt;&gt;;
</code></pre> 
&nbsp;This section is incomplete 
&nbsp;Reason: add description and extra caveats 
