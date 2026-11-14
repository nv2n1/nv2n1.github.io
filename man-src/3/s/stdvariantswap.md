---
title: "stdvariantswap(3)"
name: "stdvariantswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvariantswap/"
---

std::variant&lt;Types...&gt;::swap - std::variant&lt;Types...&gt;::swap

<h2>Synopsis</h2>

<pre><code>void swap(variant &amp;rhs) noexcept(/* see below */);
(1)(since C++ 17)</code></pre> 
Swaps two variant objects. 
* if both *this and rhs are valueless by exception, does nothing 
* otherwise, if both *this and rhs hold the same alternative, calls swap(std::get&lt;i&gt;(*this), std:get&lt;i&gt;(rhs)) where i is index(). If an exception is thrown, the state of the values depends on the exception safety of the swap function called. 
* otherwise, exchanges values of rhs and *this. If an exception is thrown, the state of *this and rhs depends on exception safety of variant's move constructor. 
The behavior is undefined unless lvalues of type T_i are Swappable and std::is_move_constructible_v&lt;T_i&gt; is true for all T_i in Types.... 

<h2>Parameters</h2>

rhs - a variant object to swap with

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

If this-&gt;index() == rhs.index(), may throw any exception thrown by swap(std::get&lt;i&gt;(*this), std::get&lt;i&gt;(rhs)) with i being index(). 
Otherwise, may throw any exception thrown by the move constructors of the alternatives currently held by *this and rhs. 
noexcept specification: 
noexcept(((std::is_nothrow_move_constructible_v&lt;Types&gt; &amp;&amp; 
std::is_nothrow_swappable_v&lt;Types&gt;) &amp;&amp; ...))

<h2>Example</h2>

// Run this code <pre><code>#include &lt;variant&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;
int main()

{
    std::variant&lt;int, std::string&gt; v1{2}, v2{&quot;abc&quot;};
    std::visit([](auto &amp;&amp;x) { std::cout &lt;&lt; x &lt;&lt; ' '; }, v1);
    std::visit([](auto &amp;&amp;x) { std::cout &lt;&lt; x &lt;&lt; '\n'; }, v2);
    v1.swap(v2);
    std::visit([](auto &amp;&amp;x) { std::cout &lt;&lt; x &lt;&lt; ' '; }, v1);
    std::visit([](auto &amp;&amp;x) { std::cout &lt;&lt; x &lt;&lt; '\n'; }, v2);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;2 abc 
&nbsp;<wbr>&nbsp;abc 2
