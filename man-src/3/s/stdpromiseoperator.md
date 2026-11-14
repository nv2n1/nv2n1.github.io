---
title: "stdpromiseoperator(3)"
name: "stdpromiseoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpromiseoperator/"
---

std::promise&lt;R&gt;::operator= - std::promise&lt;R&gt;::operator=

<h2>Synopsis</h2>

<pre><code>promise &amp;operator=(promise &amp;&amp;other) noexcept;
(1)(since C++ 11)

    promise &amp;
    operator=(const promise &amp;rhs) = delete;
(2)(since C++ 11)</code></pre> 
Assigns the contents. 
1) Move assignment operator. First, abandons the shared state (as in ~promise()), then assigns the shared state of other as if by executing std::promise(std::move(other)).swap(*this). 
2) promise is not copy-assignable. 

<h2>Parameters</h2>

other - another promise to acquire the state from

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>


