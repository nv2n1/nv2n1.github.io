---
title: "stdswapstdfunction(3)"
name: "stdswapstdfunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdfunction/"
---

std::swap(std::function) - std::swap(std::function)

<h2>Synopsis</h2>

<pre><code>template &lt;class R, class... Args&gt;
(since C++ 11)

    void swap(function&lt;R(Args...)&gt; &amp;lhs, function&lt;R(Args...)&gt; &amp;rhs);
(until C++ 17)

    template &lt;class R, class... Args&gt;
    (since C++ 17)

        void swap(function&lt;R(Args...)&gt; &amp;lhs, function&lt;R(Args...)&gt; &amp;rhs) noexcept;</code></pre> 
Overloads the std::swap algorithm for std::function. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - polymorphic function wrappers whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 
