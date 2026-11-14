---
title: "stdexperimentalanytype(3)"
name: "stdexperimentalanytype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalanytype/"
---

std::experimental::any::type - std::experimental::any::type

<h2>Synopsis</h2>

<pre><code>const type_info &amp;type() const noexcept;
(library fundamentals TS)</code></pre> 
Queries the contained type. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The typeid of the contained value if instance is non-empty, otherwise typeid(void). 
