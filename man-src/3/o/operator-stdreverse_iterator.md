---
title: "operator-stdreverse_iterator(3)"
name: "operator-stdreverse_iterator"
section: "3"
letter: "o"
url: "/docs/linux/man/3-operator-stdreverse_iterator/"
---

operator-(std::reverse_iterator) - operator-(std::reverse_iterator)

<h2>Synopsis</h2>

<pre><code>template &lt;class Iterator&gt;

typename reverse_iterator&lt;Iterator&gt;::difference_type(until C++ 11)

operator-(const reverse_iterator&lt;Iterator&gt; &amp;lhs,

          const reverse_iterator&lt;Iterator&gt; &amp;rhs);

template &lt;class Iterator1, class Iterator2&gt;

auto operator-(const reverse_iterator&lt;Iterator1&gt; &amp;lhs, (since C++ 11)

                                                           const reverse_iterator&lt;Iterator2&gt; &amp;rhs(until C++ 17)

                   ) -&gt; decltype(rhs.base() - lhs.base());

template &lt;class Iterator1, class Iterator2&gt;

constexpr auto operator-(const reverse_iterator&lt;Iterator1&gt; &amp;lhs, (since C++ 17)

                                                                     const reverse_iterator&lt;Iterator2&gt; &amp;rhs

                         ) -&gt; decltype(rhs.base() - lhs.base());</code></pre> 
Returns the distance between two iterator adaptors. 

<h2>Parameters</h2>

lhs, rhs - iterator adaptors to compute the difference of

<h2>Return value</h2>

rhs.base() - lhs.base() 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
