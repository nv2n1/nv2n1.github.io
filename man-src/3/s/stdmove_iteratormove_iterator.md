---
title: "stdmove_iteratormove_iterator(3)"
name: "stdmove_iteratormove_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmove_iteratormove_iterator/"
---

std::move_iterator&lt;Iter&gt;::move_iterator - std::move_iterator&lt;Iter&gt;::move_iterator

<h2>Synopsis</h2>

<pre><code>move_iterator();
(until C++ 17)

    constexpr move_iterator();
(since C++ 17)

    explicit move_iterator(iterator_type x);
(until C++ 17)

    constexpr explicit move_iterator(iterator_type x);
(1)(since C++ 17)

    template &lt;class U&gt;
    (2)(until C++ 17)

        move_iterator(const move_iterator&lt;U&gt; &amp;other);
(3)

    template &lt;class U&gt;
    (since C++ 17)

        constexpr move_iterator(const move_iterator&lt;U&gt; &amp;other);</code></pre> 
Constructs a new iterator adaptor. 
1) Default constructor. The underlying iterator is value-initialized. Operations on the resulting iterator have defined behavior if and only if the corresponding operations on a value-initialized Iterator also have defined behavior. 
2) The underlying iterator is initialized with x. 
3) The underlying iterator is initialized with that of other. 

<h2>Parameters</h2>

x - iterator to adapt 
other - iterator adaptor to copy

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>assigns another iterator

operator= (public member function)




</code></pre>
