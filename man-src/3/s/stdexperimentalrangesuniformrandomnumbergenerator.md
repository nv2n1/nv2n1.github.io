---
title: "stdexperimentalrangesuniformrandomnumbergenerator(3)"
name: "stdexperimentalrangesuniformrandomnumbergenerator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesuniformrandomnumbergenerator/"
---

std::experimental::ranges::UniformRandomNumberGenerator - std::experimental::ranges::UniformRandomNumberGenerator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/random&gt;

template &lt;class G&gt;

concept bool UniformRandomNumberGenerator =

Invocable&lt;G&amp;&gt; &amp;&amp;

UnsignedIntegral&lt;std::result_of_t&lt;G&amp;()&gt;&gt; &amp;&amp;      (ranges TS)

requires {

    { G::min() } -&gt; Same&lt;std::result_of_t&lt;G&amp;()&gt;&gt;&amp;&amp;;

    { G::max() } -&gt; Same&lt;std::result_of_t&lt;G&amp;()&gt;&gt;&amp;&amp;;

};</code></pre> 
The concept UniformRandomNumberGenerator&lt;G&gt; specifies that G is the type of a uniform random number generator, that is, objects of type G is a function object returning unsigned integer values such that each value in the range of possible results has (ideally) equal probability of being returned. 
UniformRandomNumberGenerator&lt;G&gt; is satisfied only if, given any object g of type G: 
* G::min() and G::max() are prvalue constant expressions; 
* G::min() &lt; G::max() 
* g() is in the range [G::min(), G::max()] 
* g() has amortized constant complexity. 
