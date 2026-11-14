---
title: "stdweak_ordering(3)"
name: "stdweak_ordering"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdweak_ordering/"
description: "std::weak_ordering – std::weak_ordering"
---

<p>std::weak_ordering &#8211; std::weak_ordering</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;compare&gt;<br />
class weak_ordering; <i>(since C++20)</i><br />
The class type std::weak_ordering is the result type of a three-way_comparison that<br />
* admits all six relational operators (==, !=, &lt;, &lt;=, &gt;, &gt;=)<br />
* does not imply substitutability: if a is equivalent to b, f(a) may not be equivalent to f(b), where f denotes a function that reads only comparison-salient state that is accessible via the argument&#8217;s public const members. In other words, equivalent values may be distinguishable.<br />
* does not allow incomparable values: at least one of a &lt; b, a == b, and a &gt; b must be true </p>
<h2>Constants</h2>
<p>The type std::weak_ordering has three valid values, implemented as const static data members of its type: </p>
<p>Member constant Definition </p>
<p>less(inline constexpr) a valid value of the type std::weak_ordering indicating less-than (ordered before) relationship<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>equivalent(inline constexpr) a valid value of the type std::weak_ordering indicating equivalence (neither ordered before nor ordered after)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>greater(inline constexpr) a valid value of the type std::weak_ordering indicating greater-than (ordered after) relationship<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Conversions</h2>
<p>std::weak_ordering is implicitly-convertible to std::weak_equality and std::partial_ordering, while std::strong_ordering is implicitly-convertible to weak_ordering. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implicit conversion to std::weak_equality<br />
operator weak_equality <i>(public member function)</i> </p>
<p>&nbsp;std::weak_ordering::operator weak_equality </p>
<p>constexpr operator weak_equality() const noexcept;</p>
<h2>Return value</h2>
<p>std::weak_equality::equivalent if v is equivalent, std::weak_equality::nonequivalent if v is less or greater.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implicit conversion to std::partial_ordering<br />
operator partial_ordering <i>(public member function)</i><br />
&nbsp;std::weak_ordering::operator partial_ordering </p>
<pre><code>constexpr operator partial_ordering() const noexcept;
</code></pre>
<h2>Return value</h2>
<p>std::partial_ordering::less if v is less, std::partial_ordering::greater if v is greater, std::partial_ordering::equivalent if v is equivalent. </p>
<h2>Comparisons</h2>
<p>Comparison operators are defined between values of this type and literal 0. This supports the expressions a &lt;=&gt; b == 0 or a &lt;=&gt; b &lt; 0 that can be used to convert the result of a three-way comparison operator to a boolean relationship; see std::is_eq, std::is_lt, etc.<br />
The behavior of a program that attempts to compare a weak_ordering with anything other than the integer literal 0 is undefined. </p>
<p>operator==<br />
operator!=<br />
operator&lt; compares with zero<br />
operator&gt; <i>(function)</i><br />
operator&lt;=<br />
operator&gt;=<br />
operator&lt;=&gt; </p>
<p>&nbsp;operator== </p>
<p>friend constexpr bool operator==(weak_ordering v, /*unspecified*/ u) noexcept;<br />
friend constexpr bool operator==(/*unspecified*/ u, weak_ordering v) noexcept;</p>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>true if v is equivalent, false if v is less or greater<br />
&nbsp;operator!= </p>
<pre><code>friend constexpr bool operator!=(weak_ordering v, /*unspecified*/ u) noexcept;

friend constexpr bool operator!=(/*unspecified*/ u, weak_ordering v) noexcept;

</code></pre>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>true if v is less or greater, and false if v is equivalent<br />
&nbsp;operator&lt;<br />
friend constexpr bool operator&lt;(weak_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&lt;(/*unspecified*/ u, weak_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is less, and false if v is greater or equivalent<br />
2) true if v is greater, and false if v is less or equivalent<br />
&nbsp;operator&lt;=<br />
friend constexpr bool operator&lt;=(weak_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&lt;=(/*unspecified*/ u, weak_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is less or equivalent, and false if v is greater<br />
2) true if v is greater or equivalent, and false if v is less<br />
&nbsp;operator&gt;<br />
friend constexpr bool operator&gt;(weak_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&gt;(/*unspecified*/ u, weak_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is greater, and false if v is less or equivalent<br />
2) true if v is less, and false if v is greater or equivalent<br />
&nbsp;operator&gt;=<br />
friend constexpr bool operator&gt;=(weak_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&gt;=(/*unspecified*/ u, weak_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is greater or equivalent, and false if v is less<br />
2) true if v is less or equivalent, and false if v is greater<br />
&nbsp;operator&lt;=&gt;<br />
friend constexpr weak_ordering operator&lt;=&gt;(weak_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr weak_ordering operator&lt;=&gt;(/*unspecified*/ u, weak_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::weak_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) v.<br />
2) greater if v is less, less if v is greater, otherwise v. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>strong_ordering the result type of 3-way comparison that supports all 6 operators and is substitutable<br />
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
