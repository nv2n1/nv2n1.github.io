---
title: "stdexperimentalpropagate_constpropagate_const(3)"
name: "stdexperimentalpropagate_constpropagate_const"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpropagate_constpropagate_const/"
---

std::experimental::propagate_const&lt;T&gt;::propagate_const - std::experimental::propagate_const&lt;T&gt;::propagate_const

<h2>Synopsis</h2>

<pre><code>constexpr propagate_const() = default;
(1)(library fundamentals TS v2)

    constexpr propagate_const(propagate_const &amp;&amp;p) = default;
(2)(library fundamentals TS v2)

    template &lt;class U&gt;
    (3)(library fundamentals TS v2)

    /* see below */ constexpr propagate_const(propagate_const&lt;U&gt; &amp;&amp;pu);

template &lt;class U&gt;
(4)(library fundamentals TS v2)

    /* see below */ constexpr propagate_const(U &amp;&amp;u);

propagate_const(const propagate_const &amp;) = delete;
(5)(library fundamentals TS v2)</code></pre> 
Let t_ designate the private data member that is the wrapped pointer-like object. 
1) Constructs an propagate_const, default-initializing this-&gt;t_. 
2) Explicitly defaulted move constructor that move constructs this-&gt;t_ from p.t_. 
3) Initializes this-&gt;t_ as if by direct-non-list-initialization from the expression std::move(pu.t_) 
This constructor does not participate in overload resolution unless std::is_constructible&lt;T, U&amp;&amp;&gt;::value is true, and is explicit if and only if std::is_convertible&lt;U&amp;&amp;, T&gt;::value is false. 
4) Initializes this-&gt;t_ as if by direct-non-list-initialization with the expression std::forward&lt;U&gt;(u). 
This constructor does not participate in overload resolution unless std::is_constructible&lt;T, U&amp;&amp;&gt;::value is true and std::decay_t&lt;U&gt; is not a specialization of propagate_const. This constructor is explicit if and only if std::is_convertible&lt;U&amp;&amp;, T&gt;::value is false. 
5) Copy constructor is explicitly deleted. 

<h2>Parameters</h2>

p - another propagate_const object to move from 
pu - another propagate_const object of a different specialization to move from 
u - another object to initialize the contained pointer with
