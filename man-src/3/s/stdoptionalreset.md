---
title: "stdoptionalreset(3)"
name: "stdoptionalreset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoptionalreset/"
---

std::optional&lt;T&gt;::reset - std::optional&lt;T&gt;::reset

<h2>Synopsis</h2>

<pre><code>void reset() noexcept;
(since C++ 17)</code></pre> 
If *this contains a value, destroy that value as if by value().T::~T(). Otherwise, there are no effects. 
*this does not contain a value after this call. 

<h2>See also</h2>

<pre><code>assigns contents

operator= (public member function)




</code></pre>
