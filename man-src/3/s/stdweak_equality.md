---
title: "stdweak_equality(3)"
name: "stdweak_equality"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdweak_equality/"
description: "std::weak_equality – std::weak_equality"
---

<p>std::weak_equality &#8211; std::weak_equality</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;compare&gt;<br />
class weak_equality; <i>(since C++20)</i><br />
The class type std::weak_equality is the result type of a three-way_comparison that<br />
* admits only equality and inequality comparisons (no less-than/greater-than)<br />
* does not imply substitutability: if a is equivalent to b, f(a) may not be equivalent to f(b), where f denotes a function that reads only comparison-salient state that is accessible via the argument&#8217;s public const members. In other words, equivalent values may be distinguishable.<br />
std::weak_equality is the weakest comparison category type: it is not implicitly-convertible to any other comparison category, but the other four comparison categories (std::strong_equality, std::partial_ordering, std::weak_ordering, std::strong_ordering) are implicitly-convertible to std::weak_equality. </p>
<h2>Constants</h2>
<p>The type std::weak_equality has only two valid values, implemented as const static data members of its type: std::weak_equality::equivalent and std::weak_equality::nonequivalent: </p>
<p>Member constant Definition </p>
<p>equivalent(inline constexpr) a valid value of the type std::weak_equality indicating equivalence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>nonequivalent(inline constexpr) a valid value of the type std::weak_equality indicating non-equivalence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Comparisons</h2>
<p>Comparison operators are defined between values of this type and literal 0. This supports the expressions a &lt;=&gt; b == 0 and a &lt;=&gt; b != 0 used to convert the result of a three-way comparison operator to a boolean relationship; see std::is_eq and std::is_neq.<br />
The behavior of a program that attempts to compare a weak_equality with anything other than the integer literal 0 is undefined. </p>
<p>operator== compares with zero<br />
operator!= <i>(function)</i><br />
operator&lt;=&gt; </p>
<p>&nbsp;operator== </p>
<p>friend constexpr bool operator==(weak_equality v, /*unspecified*/ u) noexcept;<br />
friend constexpr bool operator==(/*unspecified*/ u, weak_equality v) noexcept;</p>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_equality value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>true if v is equivalent, false if v is nonequivalent<br />
&nbsp;operator!= </p>
<pre><code>friend constexpr bool operator!=(weak_equality v, /*unspecified*/ u) noexcept;

friend constexpr bool operator!=(/*unspecified*/ u, weak_equality v) noexcept;

</code></pre>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_equality value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>false if v is equivalent, and true if v is nonequivalent<br />
&nbsp;operator&lt;=&gt; </p>
<pre><code>friend constexpr weak_equality operator&lt;=&gt;(weak_equality v, /*unspecified*/ u) noexcept;

friend constexpr weak_equality operator&lt;=&gt;(/*unspecified*/ u, weak_equality v) noexcept;

</code></pre>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_equality value to check<br />
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
strong_equality the result type of 3-way comparison that supports only equality/inequality and is substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20) </p>
