---
title: "stdexperimentalrangesreadable(3)"
name: "stdexperimentalrangesreadable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesreadable/"
---

std::experimental::ranges::Readable - std::experimental::ranges::Readable

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;class In&gt;

    concept bool Readable =

        requires
{

    typename ranges::value_type_t&lt;In&gt;;

    typename ranges::reference_t&lt;In&gt;;
    (ranges TS)

        typename ranges::rvalue_reference_t&lt;In&gt;;
}
&amp;&amp;

    CommonReference&lt;ranges::reference_t&lt;In&gt; &amp;&amp;, ranges::value_type_t&lt;In&gt; &amp;&gt; &amp;&amp;

        CommonReference&lt;ranges::reference_t&lt;In&gt; &amp;&amp;, ranges::rvalue_reference_t&lt;In&gt; &amp;&amp;&gt; &amp;&amp;

            CommonReference&lt;ranges::rvalue_reference_t&lt;In&gt; &amp;&amp;, const ranges::value_type_t&lt;In&gt; &amp;&gt;;</code></pre> 
The concept Readable is satisfied by types that are readable by applying operator*, such as pointers, smart pointers, and iterators. 
