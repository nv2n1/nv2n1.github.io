---
title: "stdexperimentalrangesrelation(3)"
name: "stdexperimentalrangesrelation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesrelation/"
---

std::experimental::ranges::Relation - std::experimental::ranges::Relation

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / concepts&gt;

    template &lt;class R, class T, class U&gt;

    concept bool Relation =

        Predicate&lt;R, T, T&gt; &amp;&amp;

        Predicate&lt;R, U, U&gt; &amp;&amp;

        CommonReference&lt;

            const std::remove_reference_t&lt;T&gt; &amp;,

            const std::remove_reference_t&lt;U&gt; &amp;&gt; &amp;&amp;

        Predicate&lt;R, (1)(ranges TS)

                         ranges::common_reference_t&lt;

                             const std::remove_reference_t&lt;T&gt; &amp;,

                             const std::remove_reference_t&lt;U&gt; &amp;&gt;,

                  ranges::common_reference_t&lt;

                      const std::remove_reference_t&lt;T&gt; &amp;,

                      const std::remove_reference_t&lt;U&gt; &amp;&gt;&gt; &amp;&amp;

        Predicate&lt;R, T, U&gt; &amp;&amp;

        Predicate&lt;R, U, T&gt;;</code></pre> 
The concept Relation&lt;R, T, U&gt; specifies that R defines a binary relation over the set of expressions whose type and value category are those encoded by either T or U. 
Given 
* r, an expression such that decltype((r)) is R, 
* t, an expression such that decltype((t)) is T, 
* u, an expression such that decltype((u)) is U, 
and let C be ranges::common_reference_t&lt;const std::remove_reference_t&lt;T&gt;&amp;, const std::remove_reference_t&lt;U&gt;&amp;&gt;, 
then Relation&lt;R, T, U&gt; is satisfied only if 
* bool(r(t, u)) == bool(r(C(t), C(u))) and 
* bool(r(u, t)) == bool(r(C(u), C(t))). 
