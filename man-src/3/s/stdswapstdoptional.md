---
title: "stdswapstdoptional(3)"
name: "stdswapstdoptional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdoptional/"
---

std::swap(std::optional) - std::swap(std::optional)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;optional&gt;

    template &lt;class T&gt;
    (since C++ 17)

        void swap(optional&lt;T&gt; &amp;lhs, optional&lt;T&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Overloads the std::swap algorithm for std::optional. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 
This function template does not participate in overload resolution unless std::is_move_constructible_v&lt;T&gt; and std::is_swappable_v&lt;T&gt; are both true. 

<h2>Parameters</h2>

lhs, rhs - optional objects whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept(noexcept(lhs.swap(rhs)))

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exchanges the contents 
swap <i>(public member function)</i> 
