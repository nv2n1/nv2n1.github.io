---
title: "stdexperimentalobserver_ptrobserver_ptr(3)"
name: "stdexperimentalobserver_ptrobserver_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalobserver_ptrobserver_ptr/"
---

std::experimental::observer_ptr&lt;W&gt;::observer_ptr - std::experimental::observer_ptr&lt;W&gt;::observer_ptr

<h2>Synopsis</h2>

<pre><code>constexpr observer_ptr() noexcept;
(1)(library fundamentals TS v2)

    constexpr observer_ptr(nullptr_t) noexcept;

explicit observer_ptr(element_type *p) noexcept;
(2)(library fundamentals TS v2)

    template &lt;class W2&gt;
    (3)(library fundamentals TS v2)

        observer_ptr(observer_ptr&lt;W2&gt; other) noexcept;

observer_ptr(const observer_ptr &amp;other) = default;
(4)(library fundamentals TS v2)(implicitly declared)

    observer_ptr(observer_ptr &amp;&amp;other) = default;
(5)(library fundamentals TS v2)(implicitly declared)</code></pre> 
1) Constructs an observer_ptr that has no corresponding watched object. 
2) Constructs an observer_ptr that watches p. 
3) Constructs an observer_ptr that watches other.get(). This constructor does not participate in overload resolution unless W2* is convertible to element_type*. 
4-5) Implicitly declared copy and move constructors. Constructs an observer_ptr that watches other.get(). 

<h2>Parameters</h2>

p - a pointer to an object to watch 
other - another observer_ptr to copy from
