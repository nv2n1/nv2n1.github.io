---
title: "stdexperimentalget_underlying(3)"
name: "stdexperimentalget_underlying"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalget_underlying/"
---

std::experimental::get_underlying - std::experimental::get_underlying

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;
(library fundamentals TS v2)

    constexpr T &amp;get_underlying(propagate_const&lt;T&gt; &amp;pt) noexcept;

template &lt;class T&gt;
(library fundamentals TS v2)

    constexpr const T &amp;get_underlying(const propagate_const&lt;T&gt; &amp;pt) noexcept;</code></pre> 
Retrieves a reference to the pointer-like object stored in a propagate_const. 

<h2>Parameters</h2>

pt - a propagate_const object

<h2>Return value</h2>

A reference to the pointer-like object stored in pt. 
