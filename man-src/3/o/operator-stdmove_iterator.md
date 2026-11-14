---
title: "operator-stdmove_iterator(3)"
name: "operator-stdmove_iterator"
section: "3"
letter: "o"
url: "/docs/linux/man/3-operator-stdmove_iterator/"
---

operator-(std::move_iterator) - operator-(std::move_iterator)

<h2>Synopsis</h2>

<pre><code>template &lt;class Iterator1, class Iterator2&gt;

auto operator-(const move_iterator&lt;Iterator1&gt; &amp;lhs, (since C++ 11)

                                                        const move_iterator&lt;Iterator2&gt; &amp;rhs(until C++ 17)

                   ) -&gt; decltype(lhs.base() - rhs.base());

template &lt;class Iterator1, class Iterator2&gt;

constexpr auto operator-(const move_iterator&lt;Iterator1&gt; &amp;lhs, (since C++ 17)

                                                                  const move_iterator&lt;Iterator2&gt; &amp;rhs

                         ) -&gt; decltype(lhs.base() - rhs.base());</code></pre> 
Returns the distance between two iterator adaptors. 

<h2>Parameters</h2>

lhs, rhs - iterator adaptors to compute the difference of

<h2>Return value</h2>

lhs.base() - rhs.base() 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
