---
title: "stdanytype(3)"
name: "stdanytype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdanytype/"
---

std::any::type - std::any::type

<h2>Synopsis</h2>

<pre><code>const std::type_info &amp;type() const noexcept;
(since C++ 17)</code></pre> 
Queries the contained type. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The typeid of the contained value if instance is non-empty, otherwise typeid(void). 
