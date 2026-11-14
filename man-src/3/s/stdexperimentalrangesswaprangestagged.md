---
title: "stdexperimentalrangesswaprangestagged(3)"
name: "stdexperimentalrangesswaprangestagged"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesswaprangestagged/"
---

std::experimental::ranges::swap(ranges::tagged) - std::experimental::ranges::swap(ranges::tagged)

<h2>Synopsis</h2>

<pre><code>friend constexpr void swap(tagged &amp;lhs, tagged &amp;rhs) noexcept(noexcept(lhs.swap(rhs)))

    requires Swappable&lt;Base&gt;;</code></pre> 
Swap the contents of *this and rhs, as if by lhs.swap(rhs);. 
This function is a hidden friend: it is not visible to ordinary unqualified or qualified_lookup, and can only be found by argument-dependent_lookup when tagged is an associated class of the arguments. 

<h2>Notes</h2>

Unlike most non-member swaps in the standard library, this swap is a hidden friend function declared in the body of tagged, not a function template. The tagged in the function declaration is the injected-class-name. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents of two tagged objects 
swap <i>(public member function)</i> 
