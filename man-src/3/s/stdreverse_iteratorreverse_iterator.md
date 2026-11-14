---
title: "stdreverse_iteratorreverse_iterator(3)"
name: "stdreverse_iteratorreverse_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreverse_iteratorreverse_iterator/"
---

std::reverse_iterator&lt;Iter&gt;::reverse_iterator - std::reverse_iterator&lt;Iter&gt;::reverse_iterator

<h2>Synopsis</h2>

<pre><code>reverse_iterator();
(until C++ 17)

    constexpr reverse_iterator();
(since C++ 17)

    explicit reverse_iterator(iterator_type x);
(until C++ 17)

    constexpr explicit reverse_iterator(iterator_type x);
(1)(since C++ 17)

    template &lt;class U&gt;
    (2)(until C++ 17)

        reverse_iterator(const reverse_iterator&lt;U&gt; &amp;other);
(3)

    template &lt;class U&gt;
    (since C++ 17)

        constexpr reverse_iterator(const reverse_iterator&lt;U&gt; &amp;other);</code></pre> 
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
