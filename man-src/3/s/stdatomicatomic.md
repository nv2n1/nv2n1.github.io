---
title: "stdatomicatomic(3)"
name: "stdatomicatomic"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicatomic/"
---

std::atomic&lt;T&gt;::atomic - std::atomic&lt;T&gt;::atomic

<h2>Synopsis</h2>

<pre><code>atomic() noexcept = default;
(1)(since C++ 11)

    constexpr atomic(T desired) noexcept;
(2)(since C++ 11)

    atomic(const atomic &amp;) = delete;
(3)(since C++ 11)</code></pre> 
Constructs new atomic variable. 
1) The default constructor is trivial: no initialization takes place other than zero_initialization of static and thread-local objects. std::atomic_init may be used to complete initialization. 
2) Initializes the underlying value with desired. The initialization is not atomic. 
3) Atomic variables are not CopyConstructible. 

<h2>Parameters</h2>

desired - value to initialize with

<h2>Notes</h2>

The default-initialized std::atomic&lt;T&gt; does not contain a T object, and its only valid uses are destruction and initialization by std::atomic_init, see LWG_2334 
