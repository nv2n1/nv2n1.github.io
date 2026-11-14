---
title: "stdatomic_refatomic_ref(3)"
name: "stdatomic_refatomic_ref"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refatomic_ref/"
description: "std::atomic_ref<T>::atomic_ref – std::atomic_ref<T>::atomic_ref"
---

<p>std::atomic_ref&lt;T&gt;::atomic_ref &#8211; std::atomic_ref&lt;T&gt;::atomic_ref</p>
<h2>Synopsis</h2>
<p>explicit atomic_ref( T&amp; obj ); <code>(1)</code> <i>(since C++20)</i><br />
atomic_ref( const atomic_ref&amp; ref ) noexcept; <code>(2)</code> <i>(since C++11)</i><br />
Constructs a new atomic_ref object.<br />
1) Constructs an atomic_ref object referencing the object obj. The behavior is undefined if obj is not aligned to required_alignment.<br />
2) Constructs an atomic_ref object referencing the object referenced by ref. </p>
<h2>Parameters</h2>
<p>obj &#8211; object to reference<br />
ref &#8211; another atomic_ref object to copy from</p>
