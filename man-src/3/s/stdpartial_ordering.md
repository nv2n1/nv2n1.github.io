---
title: "stdpartial_ordering(3)"
name: "stdpartial_ordering"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpartial_ordering/"
description: "std::partial_ordering – std::partial_ordering"
---

<p>std::partial_ordering &#8211; std::partial_ordering</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;compare&gt;<br />
class partial_ordering; <i>(since C++20)</i><br />
The class type std::partial_ordering is the result type of a three-way_comparison that<br />
* admits all six relational operators (==, !=, &lt;, &lt;=, &gt;, &gt;=)<br />
* does not imply substitutability: if a is equivalent to b, f(a) may not be equivalent to f(b), where f denotes a function that reads only comparison-salient state that is accessible via the argument&#8217;s public const members. In other words, equivalent values may be distinguishable.<br />
* admits incomparable values: a &lt; b, a == b, and a &gt; b may all be false </p>
<h2>Constants</h2>
<p>The type std::partial_ordering has four valid values, implemented as const static data members of its type: </p>
<p>Member constant Definition </p>
<p>less(inline constexpr) a valid value of the type std::partial_ordering indicating less-than (ordered before) relationship<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>equivalent(inline constexpr) a valid value of the type std::partial_ordering indicating equivalence (neither ordered before nor ordered after)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>greater(inline constexpr) a valid value of the type std::partial_ordering indicating greater-than (ordered after) relationship<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>unordered(inline constexpr) a valid value of the type std::partial_ordering indicating relationship with an incomparable value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Conversions</h2>
<p>std::partial_ordering is implicitly-convertible to std::weak_equality, while both std::strong_ordering and std::weak_ordering are implicitly-convertible to partial_ordering. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implicit conversion to std::weak_equality<br />
operator weak_equality <i>(public member function)</i> </p>
<p>&nbsp;std::partial_ordering::operator weak_equality </p>
<p>constexpr operator weak_equality() const noexcept;</p>
<h2>Return value</h2>
<p>std::weak_equality::equivalent if v is equivalent, std::weak_equality::nonequivalent if v is less, greater, or unordered. </p>
<h2>Comparisons</h2>
<p>Comparison operators are defined between values of this type and literal 0. This supports the expressions a &lt;=&gt; b == 0 or a &lt;=&gt; b &lt; 0 that can be used to convert the result of a three-way comparison operator to a boolean relationship; see std::is_eq, std::is_lt, etc.<br />
The behavior of a program that attempts to compare a partial_ordering with anything other than the integer literal 0 is undefined. </p>
<p>operator==<br />
operator!=<br />
operator&lt; compares with zero<br />
operator&gt; <i>(function)</i><br />
operator&lt;=<br />
operator&gt;=<br />
operator&lt;=&gt; </p>
<p>&nbsp;operator== </p>
<p>friend constexpr bool operator==(partial_ordering v, /*unspecified*/ u) noexcept;<br />
friend constexpr bool operator==(/*unspecified*/ u, partial_ordering v) noexcept;</p>
<h2>Parameters</h2>
<p>v &#8211; a std::partial_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>true if v is equivalent, false if v is less, greater, or unordered<br />
&nbsp;operator!= </p>
<pre><code>friend constexpr bool operator!=(partial_ordering v, /*unspecified*/ u) noexcept;

friend constexpr bool operator!=(/*unspecified*/ u, partial_ordering v) noexcept;

</code></pre>
<h2>Parameters</h2>
<p>v &#8211; a std::partial_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>true if v is unordered, less, or greater, and false if v is equivalent<br />
&nbsp;operator&lt;<br />
friend constexpr bool operator&lt;(partial_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&lt;(/*unspecified*/ u, partial_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::partial_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is less, and false if v is greater, equivalent, or unordered<br />
2) true if v is greater, and false if v is less, equivalent, or unordered<br />
&nbsp;operator&lt;=<br />
friend constexpr bool operator&lt;=(partial_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&lt;=(/*unspecified*/ u, partial_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::partial_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is less or equivalent, and false if v is greater or unordered<br />
2) true if v is greater or equivalent, and false if v is less or unordered<br />
&nbsp;operator&gt;<br />
friend constexpr bool operator&gt;(partial_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&gt;(/*unspecified*/ u, partial_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::partial_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is greater, and false if v is less, equivalent, or unordered<br />
2) true if v is less, and false if v is greater, equivalent, or unordered<br />
&nbsp;operator&gt;=<br />
friend constexpr bool operator&gt;=(partial_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr bool operator&gt;=(/*unspecified*/ u, partial_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::partial_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) true if v is greater or equivalent, and false if v is less or unordered<br />
2) true if v is less or equivalent, and false if v is greater or unordered<br />
&nbsp;operator&lt;=&gt;<br />
friend constexpr partial_ordering operator&lt;=&gt;(partial_ordering v, /*unspecified*/ u) noexcept; <code>(1)</code><br />
friend constexpr partial_ordering operator&lt;=&gt;(/*unspecified*/ u, partial_ordering v) noexcept; <code>(2)</code> </p>
<h2>Parameters</h2>
<p>v &#8211; a std::partial_ordering value to check<br />
u &#8211; an unused parameter of any type that accepts literal zero argument</p>
<h2>Return value</h2>
<p>1) v.<br />
2) greater if v is less, less if v is greater, otherwise v. </p>
<h2>Notes</h2>
<p>The built-in_operator_&lt;=&gt; between floating-point values uses this ordering: the positive zero and the negative zero compare equivalent, but can be distinguished, and NaN values compare unordered with any other value. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>strong_ordering the result type of 3-way comparison that supports all 6 operators and is substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
weak_ordering the result type of 3-way comparison that supports all 6 operators and is not substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
strong_equality the result type of 3-way comparison that supports only equality/inequality and is substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20)<br />
weak_equality the result type of 3-way comparison that supports only equality/inequality and is not substitutable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
(C++20) </p>
