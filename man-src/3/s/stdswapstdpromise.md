---
title: "stdswapstdpromise(3)"
name: "stdswapstdpromise"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdpromise/"
---

std::swap(std::promise) - std::swap(std::promise)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;future&gt;

    template &lt;class R&gt;
    (since C++ 11)

        void swap(promise&lt;R&gt; &amp;lhs, promise&lt;R&gt; &amp;rhs) noexcept;</code></pre> 
Specializes the std::swap algorithm for std::promise. Exchanges the shared state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - promises whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two promise objects 
swap <i>(public member function)</i> 
