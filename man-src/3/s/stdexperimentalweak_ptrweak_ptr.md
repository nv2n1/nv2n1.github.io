---
title: "stdexperimentalweak_ptrweak_ptr(3)"
name: "stdexperimentalweak_ptrweak_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalweak_ptrweak_ptr/"
---

std::experimental::weak_ptr&lt;T&gt;::weak_ptr - std::experimental::weak_ptr&lt;T&gt;::weak_ptr

<h2>Synopsis</h2>

<pre><code>constexpr weak_ptr() noexcept;
(1)(library fundamentals TS)

    weak_ptr(const weak_ptr &amp;r) noexcept;
(2)(library fundamentals TS)

    template &lt;class Y&gt;
    (2)(library fundamentals TS)

        weak_ptr(const weak_ptr&lt;Y&gt; &amp;r) noexcept;

template &lt;class Y&gt;
(2)(library fundamentals TS)

    weak_ptr(const std::experimental::shared_ptr&lt;Y&gt; &amp;r) noexcept;

weak_ptr(weak_ptr &amp;&amp;r) noexcept;
(3)(library fundamentals TS)

    template &lt;class Y&gt;
    (3)(library fundamentals TS)

        weak_ptr(weak_ptr&lt;Y&gt; &amp;&amp;r) noexcept;</code></pre> 
Constructs a new weak_ptr that potentially shares an object with r. 
1) Default constructor. Constructs empty weak_ptr. 
2) Constructs new weak_ptr which shares an object managed by r. If r manages no object, *this manages no object too. The templated overloads don't participate in overload resolution unless either Y* is implicitly convertible to T*, or Y is the type &quot;array of N U&quot; for some type U and some number N, and T is the type &quot;array of unknown bound of (possibly cv-qualified) U&quot;. 
3) Move constructors. Moves a weak_ptr instance from r into *this. After this, r is empty and r.use_count()==0. The templated overload doesn't participate in overload resolution unless either Y* is implicitly convertible to T*, or Y is the type &quot;array of N U&quot; for some type U and some number N, and T is the type &quot;array of unknown bound of (possibly cv-qualified) U&quot;. 

<h2>Parameters</h2>

r - a std::experimental::shared_ptr or std::experimental::weak_ptr that will be viewed by this std::experimental::weak_ptr

<h2>Exceptions</h2>

noexcept specification: 
noexcept

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>creates a new weak_ptr

constructor   (public member function of std::weak_ptr&lt;T&gt;)
assigns the weak_ptr

operator=     (public member function of std::weak_ptr&lt;T&gt;)




</code></pre>
