---
title: "stdstrong_ordering(3)"
name: "stdstrong_ordering"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrong_ordering/"
description: "std::strong_ordering – std::strong_ordering"
---

<p>std::strong_ordering &#8211; std::strong_ordering</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;compare&gt;<br />
class strong_ordering; <i>(since C++20)</i><br />
The class type std::strong_ordering is the result type of a three-way_comparison that<br />
* admits all six relational operators (==, !=, &lt;, &lt;=, &gt;, &gt;=)<br />
* implies substitutability: if a is equivalent to b, f(a) is also equivalent to f(b), where f denotes a function that reads only comparison-salient state that is accessible via the argument&#8217;s public const members. In other words, equivalent values are indistinguishable.<br />
* does not allow incomparable values: at least one of a &lt; b, a == b, and a &gt; b must be true </p>
<h2>Constants</h2>
<p>The type std::strong_ordering has four valid values, implemented as const static data members of its type: </p>
<p>Member constant Definition </p>
<p>less(inline constexpr) a valid value of the type std::strong_ordering indicating less-than (ordered before) relationship<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>equivalent(inline constexpr) a valid value of the type std::strong_ordering indicating equivalence (neither ordered before nor ordered after)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>equal(inline constexpr) a valid value of the type std::strong_ordering indicating equivalence (neither ordered before nor ordered after)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>greater(inline constexpr) a valid value of the type std::strong_ordering indicating greater-than (ordered after) relationship<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Conversions</h2>
<p>std::strong_ordering is the strongest of the five comparison categories: it is not implicitly-convertible from any other category and is implicitly-convertible to the other four. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implicit conversion to std::strong_equality<br />
operator strong_equality <i>(public member function)</i> </p>
<p>&nbsp;std::strong_ordering::operator strong_equality </p>
<p>constexpr operator strong_equality() const noexcept;</p>
<h2>Return value</h2>
<p>std::strong_equality::equal if v is equivalent or equal, std::strong_equality::nonequal if v is less or greater.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implicit conversion to std::weak_equality<br />
operator weak_equality <i>(public member function)</i><br />
&nbsp;std::strong_ordering::operator weak_equality </p>
<pre><code>constexpr operator weak_equality() const noexcept;
</code></pre>
<h2>Return value</h2>
<p>std::weak_equality::equivalent if v is equal or equivalent, std::weak_equality::nonequivalent if v is less or greater.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implicit conversion to std::partial_ordering<br />
operator partial_ordering <i>(public member function)</i><br />
&nbsp;std::strong_ordering::operator partial_ordering constexpr operator partial_ordering() const noexcept;</p>
<h2>Return value</h2>
<p>std::partial_ordering::less if v is less, std::partial_ordering::greater if v is greater, std::partial_ordering::equivalent if v is equal or equivalent.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implicit conversion to std::weak_ordering<br />
operator weak_ordering <i>(public member function)</i><br />
&nbsp;std::strong_ordering::operator weak_ordering constexpr operator weak_ordering() const noexcept;</p>
<h2>Return value</h2>
<p>std::weak_ordering::less if v is less, std::weak_ordering::greater if v is greater, std::weak_ordering::equivalent if v is equal or equivalent. </p>
<h2>Comparisons</h2>
<p>Comparison operators are defined between values of this type and literal 0. This supports the expressions a &lt;=&gt; b == 0 or a &lt;=&gt; b &lt; 0 that can be used to convert the result of a three-way comparison operator to a boolean relationship; see std::is_eq, std::is_lt, etc.<br />
The behavior of a program that attempts to compare a strong_ordering with anything other than the integer literal 0 is undefined. </p>
<p>operator==<br />
operator!=<br />
operator&lt; compares with zero<br />
operator&gt; <i>(function)</i><br />
operator&lt;=<br />
operator&gt;=<br />
operator&lt;=&gt; </p>
<p>&nbsp;operator== </p>
<p>friend constexpr bool operator==(strong_ordering v, /*unspecified*/ u) noexcept;<br />
friend constexpr bool operator==(/*unspecified*/ u, strong_ordering v) noexcept;</p>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>true if v is equivalent or equal, false if v is less or greater<br />
&nbsp;operator!= </p>
<pre><code>friend constexpr bool operator!=(strong_ordering v, /*unspecified*/ u) noexcept;

friend constexpr bool operator!=(/*unspecified*/ u, strong_ordering v) noexcept;

</code></pre>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>true if v is less or greater, and false if v is equivalent or equal<br />
&nbsp;operator&lt;<br />
friend constexpr bool operator&lt;(strong_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&lt;(/*unspecified*/ u, strong_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is less, and false if v is greater, equivalent, or equal<br />
2) true if v is greater, and false if v is less, equivalent, or equal<br />
&nbsp;operator&lt;=<br />
friend constexpr bool operator&lt;=(strong_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&lt;=(/*unspecified*/ u, strong_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is less, equivalent, or equal, and false if v is greater<br />
2) true if v is greater, equivalent, or equal, and false if v is less<br />
&nbsp;operator&gt;<br />
friend constexpr bool operator&gt;(strong_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&gt;(/*unspecified*/ u, strong_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is greater, and false if v is less, equivalent, or equal<br />
2) true if v is less, and false if v is greater, equivalent, or equal<br />
&nbsp;operator&gt;=<br />
friend constexpr bool operator&gt;=(strong_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&gt;=(/*unspecified*/ u, strong_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is greater, equivalent, or equal, and false if v is less<br />
2) true if v is less, equivalent, or equal, and false if v is greater<br />
&nbsp;operator&lt;=&gt;<br />
friend constexpr strong_ordering operator&lt;=&gt;(strong_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr strong_ordering operator&lt;=&gt;(/*unspecified*/ u, strong_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::strong_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) v.<br />
2) greater if v is less, less if v is greater, otherwise v. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>weak_ordering the result type of 3-way comparison that supports all 6 operators and is not substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
partial_ordering the result type of 3-way comparison that supports all 6 operators, is not substitutable, and allows incomparable values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
strong_equality the result type of 3-way comparison that supports only equality/inequality and is substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
weak_equality the result type of 3-way comparison that supports only equality/inequality and is not substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20) </p>
