---
title: "stdinitializer_listbegin(3)"
name: "stdinitializer_listbegin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinitializer_listbegin/"
---

std::initializer_list&lt;T&gt;::begin - std::initializer_list&lt;T&gt;::begin

<h2>Synopsis</h2>

<pre><code>const T *begin() const noexcept;
(since C++ 11)(until C++ 14)

    constexpr const T *begin() const noexcept;
(since C++ 14)</code></pre> 
Returns a pointer to the first element in the initializer list. 
If the initializer list is empty, the values of begin() and end() are unspecified, but will be identical. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

a pointer to the first element in the initializer list 

<h2>Complexity</h2>

Constant

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to one past the last element 
end <i>(public member function)</i> 
