---
title: "stdexperimentalatomic_weak_ptratomic_weak_ptr(3)"
name: "stdexperimentalatomic_weak_ptratomic_weak_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalatomic_weak_ptratomic_weak_ptr/"
---

std::experimental::atomic_weak_ptr&lt;T&gt;::atomic_weak_ptr - std::experimental::atomic_weak_ptr&lt;T&gt;::atomic_weak_ptr

<h2>Synopsis</h2>

<pre><code>constexpr atomic_weak_ptr() noexcept;
(1)

    constexpr atomic_weak_ptr(weak_ptr&lt;T&gt; desired) noexcept;
(2)

    atomic_weak_ptr(const atomic_weak_ptr &amp;) = delete;
(3)</code></pre> 
Constructs a new atomic_weak_ptr object. 
1) The default constructor initializes the object to an empty state. 
2) Initializes the underlying weak_ptr&lt;T&gt; with desired. The initialization is not atomic. 
3) Atomic variables are not CopyConstructible. 

<h2>Parameters</h2>

desired - value to initialize with
