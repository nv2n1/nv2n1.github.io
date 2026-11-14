---
title: "stdstrong_equality(3)"
name: "stdstrong_equality"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrong_equality/"
description: "std::strong_equality – std::strong_equality"
---

<p>std::strong_equality &#8211; std::strong_equality</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;compare&gt;<br />
class strong_equality; <i>(since C++20)</i><br />
The class type std::strong_equality is the result type of a three-way_comparison that<br />
* admits only equality and inequality comparisons (no less-than/greater-than)<br />
* implies substitutability: if a is equivalent to b, f(a) is also equivalent to f(b), where f denotes a function that reads only comparison-salient state that is accessible via the argument&#8217;s public const members. In other words, equivalent values are indistinguishable. </p>
<h2>Constants</h2>
<p>The type std::strong_equality has four valid values, implemented as const static data members of its type: </p>
<p>Member constant Definition </p>
<p>equivalent(inline constexpr) a valid value of the type std::strong_equality indicating equality<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>equal(inline constexpr) a valid value of the type std::strong_equality indicating equality<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>nonequivalent(inline constexpr) a valid value of the type std::strong_equality indicating non-equality<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>nonequal(inline constexpr) a valid value of the type std::strong_equality indicating non-equality<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Conversions</h2>
<p>std::strong_equality is implicitly-convertible to std::weak_equality, and std::strong_ordering is implicitly-convertible to strong_equality. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implicit conversion to std::weak_equality<br />
operator weak_equality <i>(public member function)</i> </p>
<p>&nbsp;std::strong_equality::operator weak_equality </p>
<p>constexpr operator weak_equality() const noexcept;</p>
<h2>Return value</h2>
<p>std::weak_equality::equivalent if v is equivalent or equal, std::weak_equality::nonequivalent if v is nonequivalent or nonequal. </p>
<h2>Comparisons</h2>
<p>Comparison operators are defined between values of this type and literal 0. This supports the expressions a &lt;=&gt; b == 0 and a &lt;=&gt; b != 0 used to convert the result of a three-way comparison operator to a boolean relationship; see std::is_eq and std::is_neq.<br />
The behavior of a program that attempts to compare a strong_equality with anything other than the integer literal 0 is undefined. </p>
<p>operator== compares with zero<br />
operator!= <i>(function)</i><br />
operator&lt;=&gt; </p>
<p>&nbsp;operator== </p>
<p>friend constexpr bool operator==(strong_equality v, /*unspecified*/ u) noexcept;<br />
friend constexpr bool operator==(/*unspecified*/ u, strong_equality v) noexcept;</p>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_equality value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>true if v is equivalent or equal, false if v is nonequivalent or nonequal<br />
&nbsp;operator!= </p>
<pre><code>friend constexpr bool operator!=(strong_equality v, /*unspecified*/ u) noexcept;

friend constexpr bool operator!=(/*unspecified*/ u, strong_equality v) noexcept;

</code></pre>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_equality value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>false if v is equivalent or equal, and true if v is nonequivalent or nonequal<br />
&nbsp;operator&lt;=&gt; </p>
<pre><code>friend constexpr strong_equality operator&lt;=&gt;(strong_equality v, /*unspecified*/ u) noexcept;

friend constexpr strong_equality operator&lt;=&gt;(/*unspecified*/ u, strong_equality v) noexcept;

</code></pre>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_equality value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>v </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>strong_ordering the result type of 3-way comparison that supports all 6 operators and is substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
weak_ordering the result type of 3-way comparison that supports all 6 operators and is not substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
partial_ordering the result type of 3-way comparison that supports all 6 operators, is not substitutable, and allows incomparable values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
weak_equality the result type of 3-way comparison that supports only equality/inequality and is not substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20) </p>
