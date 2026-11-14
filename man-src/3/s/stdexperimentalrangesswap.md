---
title: "stdexperimentalrangesswap(3)"
name: "stdexperimentalrangesswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesswap/"
---

std::experimental::ranges::swap - std::experimental::ranges::swap

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / utility&gt;

    namespace
{
    (ranges TS)

        constexpr /* unspecified */ swap = /* unspecified */;
    (customization point object)
}

Call signature

    template &lt;class T, class U&gt;

requires /* see below */

    void
    swap(T &amp;&amp;t, U &amp;&amp;u) noexcept(/* see below */);</code></pre> 
Exchanges the values referenced by t and u. 
A call to ranges::swap is equivalent to: 
1) (void)swap(std::forward&lt;T&gt;(t), std::forward&lt;U&gt;(u)), if that expression is valid, where the overload_resolution is performed with the following candidates: <pre><code>*template &lt;class T&gt;
void swap(T &amp;, T &amp;) = delete;

*template &lt;class T, std::size_t N&gt;
void swap(T (&amp;)[N], T (&amp;)[N]) = delete;

*any declarations of swap found by argument - dependent_lookup.</code></pre> 
If the function selected by overload resolution does not exchange the values referenced by t and u, the program is ill-formed; no diagnostic required. 
2) Otherwise, (void)ranges::swap_ranges(t, u), if T and U are lvalue references to array types of equal extent (but possibly different element types) and ranges::swap(*t, *u) is a valid expression; 
3) Otherwise, if T and U are both V&amp; for some type V that meets the syntactic requirements of MoveConstructible&lt;V&gt; and Assignable&lt;V&amp;, V&gt;, exchanges the referenced values as if by V v{std::move(t)}; t = std::move(u); u = std::move(v);. If the semantic requirements of either concept are not satisfied, the program is ill-formed; no diagnostic required. 
4) In all other cases, a call to ranges::swap is ill-formed. 
ranges::swap can be used in a constant expression if every function it calls (as specified above) can be so used. 
Customization point objects 
The name ranges::swap denotes a customization point object, which is a function_object of a literal Semiregular class type (denoted, for exposition purposes, as SwapT). All instances of SwapT are equal. Thus, ranges::swap can be copied freely and its copies can be used interchangeably. 
Given a set of types Args..., if std::declval&lt;Args&gt;()... meet the requirements for arguments to ranges::swap above, SwapT will satisfy ranges::Invocable&lt;const SwapT, Args...&gt;. Otherwise, no function call operator of SwapT participates in overload resolution. 
In every translation unit in which ranges::swap is defined, it refers to the same instance of the customization point object. (This means that it can be used freely in things like inline functions and function templates without violating the one-definition_rule.) 

<h2>Exceptions</h2>

1) 
noexcept specification: 
noexcept(noexcept((void)swap(std::forward&lt;T&gt;(t), std::forward&lt;T&gt;(u)))) 
, where swap is found as described above. 
2) 
noexcept specification: 
noexcept(noexcept(ranges::swap(*t, *u))) 
3) 
noexcept specification: 
noexcept(std::is_nothrow_move_constructible&lt;V&gt;::value &amp;&amp; 
std::is_nothrow_move_assignable&lt;V&gt;::value)

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
