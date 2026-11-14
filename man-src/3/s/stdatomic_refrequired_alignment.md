---
title: "stdatomic_refrequired_alignment(3)"
name: "stdatomic_refrequired_alignment"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refrequired_alignment/"
---

std::atomic_ref&lt;T&gt;::required_alignment - std::atomic_ref&lt;T&gt;::required_alignment

<h2>Synopsis</h2>

<pre><code>static constexpr std::size_t required_alignment= /*implementation-defined*/;  (since C++20)</code></pre> 
The value of required_alignment is the required alignment for an object to be referenced by an atomic reference, which is at least alignof(T). 

<h2>Notes</h2>

Hardware could require that an object to be referenced by an atomic_ref&lt;T&gt; have stricter alignment than other T objects, and whether operations on an atomic_ref are lock-free can depend on the alignment of the referenced object. 
