---
title: "stdexperimentalpropagate_constoperator(3)"
name: "stdexperimentalpropagate_constoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpropagate_constoperator/"
---

std::experimental::propagate_const&lt;T&gt;::operator= - std::experimental::propagate_const&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>constexpr propagate_const &amp;operator=(propagate_const &amp;&amp;p) = default;
(1)(library fundamentals TS v2)

    template &lt;class U&gt;
    (2)(library fundamentals TS v2)

        constexpr propagate_const &amp;
        operator=(propagate_const&lt;U&gt; &amp;&amp;pu);

template &lt;class U&gt;
(3)(library fundamentals TS v2)

    constexpr propagate_const &amp;
    operator=(U &amp;&amp;u);

propagate_const &amp;operator=(const propagate_const &amp;) = delete;
(4)(library fundamentals TS v2)</code></pre> 
Let t_ designate the private data member that is the wrapped pointer-like object. 
1) Explicitly defaulted move assignment operator that move assigns this-&gt;t_ from p.t_. 
2) Assigns std::move(pu.t_) to this-&gt;t_. 
This function does not participate in overload resolution unless U is implicitly convertible to T. 
3) Assigns std::forward&lt;U&gt;(u) to this-&gt;t_. 
This function does not participate in overload resolution unless U is implicitly convertible to T and std::decay_t&lt;U&gt; is not a specialization of propagate_const 
4) Copy assignment operator is explicitly deleted. 

<h2>Parameters</h2>

p - another propagate_const object to move from 
pu - another propagate_const object of a different specialization to move from 
u - another object to assign to the contained pointer

<h2>Return value</h2>

*this. 
