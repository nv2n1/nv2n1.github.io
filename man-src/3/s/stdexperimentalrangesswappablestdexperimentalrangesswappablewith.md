---
title: "stdexperimentalrangesswappablestdexperimentalrangesswappablewith(3)"
name: "stdexperimentalrangesswappablestdexperimentalrangesswappablewith"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesswappablestdexperimentalrangesswappablewith/"
---

std::experimental::ranges::Swappable,std::experimental::ranges::SwappableWith - std::experimental::ranges::Swappable,std::experimental::ranges::SwappableWith

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / concepts&gt;

    template &lt;class T&gt;

    concept bool Swappable =

        requires(T &amp; a, T &amp;b)
{
    (1)(ranges TS)

        ranges::swap(a, b);
};

template &lt;class T, class U&gt;

concept bool SwappableWith =

    CommonReference&lt;

        const std::remove_reference_t&lt;T&gt; &amp;,

        const std::remove_reference_t&lt;U&gt; &amp;&gt; &amp;&amp;

    requires(T &amp;&amp;t, U &amp;&amp;u)
{
    (2)(ranges TS)

        ranges::swap(std::forward&lt;T&gt;(t), std::forward&lt;T&gt;(t));

    ranges::swap(std::forward&lt;U&gt;(u), std::forward&lt;U&gt;(u));

    ranges::swap(std::forward&lt;T&gt;(t), std::forward&lt;U&gt;(u));

    ranges::swap(std::forward&lt;U&gt;(u), std::forward&lt;T&gt;(t));
};</code></pre> 
The concept Swappable&lt;T&gt; specifies that lvalues of type T are swappable. 
The concept SwappableWith&lt;T, U&gt; specifies that expressions of the type and value category encoded by T and U are swappable with each other. SwappableWith&lt;T, U&gt; is satisfied only if a call to ranges::swap(t, u) exchanges the value of t and u, that is, given distinct objects t2 equal to t and u2 equal to u, after evaluating either ranges::swap(t, u) or ranges::swap(u, t), t2 is equal to u and u2 is equal to t. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 
