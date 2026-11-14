---
title: "stdexperimentalatomic_shared_ptratomic_shared_ptr(3)"
name: "stdexperimentalatomic_shared_ptratomic_shared_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalatomic_shared_ptratomic_shared_ptr/"
---

std::experimental::atomic_shared_ptr&lt;T&gt;::atomic_shared_ptr - std::experimental::atomic_shared_ptr&lt;T&gt;::atomic_shared_ptr

<h2>Synopsis</h2>

<pre><code>constexpr atomic_shared_ptr() noexcept;
(1)

    constexpr atomic_shared_ptr(shared_ptr&lt;T&gt; desired) noexcept;
(2)

    atomic_shared_ptr(const atomic_shared_ptr &amp;) = delete;
(3)</code></pre> 
Constructs a new atomic_shared_ptr object. 
1) The default constructor initializes the object to an empty state. 
2) Initializes the underlying shared_ptr&lt;T&gt; with desired. The initialization is not atomic. 
3) Atomic variables are not CopyConstructible. 

<h2>Parameters</h2>

desired - value to initialize with

<h2>Exceptions</h2>


