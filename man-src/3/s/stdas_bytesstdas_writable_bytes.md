---
title: "stdas_bytesstdas_writable_bytes(3)"
name: "stdas_bytesstdas_writable_bytes"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdas_bytesstdas_writable_bytes/"
---

std::as_bytes,std::as_writable_bytes - std::as_bytes,std::as_writable_bytes

<h2>Synopsis</h2>

<pre><code>template &lt;class T, std::size_t N&gt;
(1)

    std::span&lt;const std::byte, S /* see below */&gt; as_bytes(std::span&lt;T, N&gt; s) noexcept;

template &lt;class T, std::size_t N&gt;
(2)

    std::span&lt;std::byte, S /* see below */&gt; as_writable_bytes(std::span&lt;T, N&gt; s) noexcept;</code></pre> 
Obtains a view to the object representation of the elements of the span s. 
If N is std::dynamic_extent, the extent of the returned span S is also std::dynamic_extent; otherwise it is sizeof(T) * N. 
as_writable_bytes only participates in overload resolution if std::is_const_v&lt;T&gt; is false. 

<h2>Return value</h2>

1) A span constructed with {reinterpret_cast&lt;const std::byte*&gt;(s.data()), s.size_bytes()}. 
2) A span constructed with {reinterpret_cast&lt;std::byte*&gt;(s.data()), s.size_bytes()}. 
