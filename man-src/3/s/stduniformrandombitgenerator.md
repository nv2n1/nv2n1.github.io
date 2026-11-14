---
title: "stduniformrandombitgenerator(3)"
name: "stduniformrandombitgenerator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduniformrandombitgenerator/"
---

std::UniformRandomBitGenerator - std::UniformRandomBitGenerator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;random&gt;

template &lt;class G&gt;

concept UniformRandomBitGenerator =

std::Invocable&lt;G&amp;&gt; &amp;&amp;

std::UnsignedIntegral&lt;std::invoke_result_t&lt;G&amp;&gt;&gt; &amp;&amp;                           (since C++20)

requires {

    G::min(); requires std::Same&lt;decltype(G::min()), std::invoke_result_t&lt;G&amp;&gt;&gt;;

    G::max(); requires std::Same&lt;decltype(G::max()), std::invoke_result_t&lt;G&amp;&gt;&gt;;

};</code></pre> 
The concept UniformRandomBitGenerator &lt;G&gt; specifies that G is the type of a uniform random bit generator, that is, objects of type G is a function object returning unsigned integer values such that each value in the range of possible results has (ideally) equal probability of being returned. 
UniformRandomBitGenerator&lt;G&gt; is satisfied only if, given any object g of type G: 
* G::min() and G::max() are constant expressions; 
* G::min() &lt; G::max() 
* g() is in the range [G::min(), G::max()] 
* g() has amortized constant complexity. 
