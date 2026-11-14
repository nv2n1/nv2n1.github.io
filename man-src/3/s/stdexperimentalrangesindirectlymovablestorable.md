---
title: "stdexperimentalrangesindirectlymovablestorable(3)"
name: "stdexperimentalrangesindirectlymovablestorable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesindirectlymovablestorable/"
---

std::experimental::ranges::IndirectlyMovableStorable - std::experimental::ranges::IndirectlyMovableStorable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt; class In, class Out &gt;

concept bool IndirectlyMovableStorable =

IndirectlyMovable&lt;In, Out&gt; &amp;&amp;

Writable&lt;Out, ranges::value_type_t&lt;In&gt;&gt; &amp;&amp;                                  (ranges TS)

Movable&lt;ranges::value_type_t&lt;In&gt;&gt; &amp;&amp;

Constructible&lt;ranges::value_type_t&lt;In&gt;, ranges::rvalue_reference_t&lt;In&gt;&gt; &amp;&amp;

Assignable&lt;ranges::value_type_t&lt;In&gt;&amp;, ranges::rvalue_reference_t&lt;In&gt;&gt;;
</code></pre> 
&nbsp;This section is incomplete 
&nbsp;Reason: add description and extra caveats 
