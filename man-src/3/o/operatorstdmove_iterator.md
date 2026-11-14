---
title: "operatorstdmove_iterator(3)"
name: "operatorstdmove_iterator"
section: "3"
letter: "o"
url: "/docs/linux/man/3-operatorstdmove_iterator/"
---

operator+(std::move_iterator) - operator+(std::move_iterator)

<h2>Synopsis</h2>

<pre><code>template &lt;class Iter&gt;

move_iterator&lt;Iter&gt;(until C++ 17)

operator+(typename move_iterator&lt;Iter&gt;::difference_type n,

          const move_iterator&lt;Iter&gt; &amp;it);

template &lt;class Iter&gt;

constexpr move_iterator&lt;Iter&gt;(since C++ 17)

operator+(typename move_iterator&lt;Iter&gt;::difference_type n,

          const move_iterator&lt;Iter&gt; &amp;it);</code></pre> 
Returns the iterator it incremented by n. 

<h2>Parameters</h2>

n - the number of positions to increment the iterator 
it - the iterator adaptor to increment

<h2>Return value</h2>

The incremented iterator, that is move_iterator&lt;Iter&gt;(it.base() + n) 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>operator++

operator++(int)

operator+=      advances or decrements the iterator

operator+       (public member function)

operator--

operator--(int)

operator-=

operator-




</code></pre>
