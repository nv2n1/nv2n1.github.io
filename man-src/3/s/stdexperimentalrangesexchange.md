---
title: "stdexperimentalrangesexchange(3)"
name: "stdexperimentalrangesexchange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesexchange/"
---

std::experimental::ranges::exchange - std::experimental::ranges::exchange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/utility&gt;

template&lt; MoveConstructible T, class U = T &gt;

requires Assignable&lt;T&amp;, U&gt;                                            (ranges TS)

constexpr T exchange(T&amp; obj, U&amp;&amp; new_val) noexcept(/* see below */);</code></pre> 
Replaces the value of obj with new_value and returns the old value of obj, as if by <pre><code>T old_value = std::move(obj);

obj = std::forward&lt;U&gt;(new_value);

return old_value;
</code></pre>

<h2>Parameters</h2>

obj - object whose value to replace 
new_value - the value to assign to obj

<h2>Return value</h2>

The old value of obj 

<h2>Exceptions</h2>

noexcept specification: 
noexcept(std::is_nothrow_move_constructible&lt;T&gt;::value &amp;&amp; 
std::is_nothrow_assignable&lt;T&amp;, U&gt;::value)

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

exchange replaces the argument with a new value and returns its previous value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++14)</i> 
