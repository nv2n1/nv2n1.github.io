---
title: "stdbyte(3)"
name: "stdbyte"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbyte/"
description: "std::byte – std::byte"
---

<p>std::byte &#8211; std::byte</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cstddef&gt;<br />
enum class byte : unsigned char {} ; <i>(since C++17)</i><br />
std::byte is a distinct type that implements the concept of byte as specified in the C++ language definition.<br />
Like char and unsigned char, it can be used to access raw memory occupied by other objects (object_representation), but unlike those types, it is not a character type and is not an arithmetic type. A byte is only a collection of bits, and the only operators defined for it are the bitwise ones. </p>
<h2>Non-member functions</h2>
<p>&nbsp;std::to_integer </p>
<p>template &lt;class IntegerType&gt; <i>(since C++17)</i><br />
constexpr IntegerType to_integer(std::byte b) noexcept; </p>
<p>Equivalent to: return IntegerType(b); This overload only participates in overload resolution if std::is_integral_v&lt;IntegerType&gt; is true. </p>
<p>&nbsp;std::operator&lt;&lt;=,operator&gt;&gt;= </p>
<p>template &lt;class IntegerType&gt; <code>(1)</code> <i>(since C++17)</i><br />
constexpr std::byte&amp; operator&lt;&lt;=(std::byte&amp; b, IntegerType shift) noexcept;<br />
template &lt;class IntegerType&gt; <code>(2)</code> <i>(since C++17)</i><br />
constexpr std::byte&amp; operator&gt;&gt;=(std::byte&amp; b, IntegerType shift) noexcept; </p>
<p>1) Equivalent to: return b = b &lt;&lt; shift; This overload only participates in overload resolution if std::is_integral_v&lt;IntegerType&gt; is true.<br />
2) Equivalent to: return b = b &gt;&gt; shift;<br />
This overload only participates in overload resolution if std::is_integral_v&lt;IntegerType&gt; is true. </p>
<p>&nbsp;std::operator&lt;&lt;,operator&gt;&gt; </p>
<p>template &lt;class IntegerType&gt; <code>(1)</code> <i>(since C++17)</i><br />
constexpr std::byte operator &lt;&lt;(std::byte b, IntegerType shift) noexcept;<br />
template &lt;class IntegerType&gt; <code>(2)</code> <i>(since C++17)</i><br />
constexpr std::byte operator &gt;&gt;(std::byte b, IntegerType shift) noexcept; </p>
<p>1) Equivalent to: return std::byte(static_cast&lt;unsigned int&gt;(b) &lt;&lt; shift); This overload only participates in overload resolution if std::is_integral_v&lt;IntegerType&gt; is true.<br />
2) Equivalent to: return std::byte(static_cast&lt;unsigned int&gt;(b) &gt;&gt; shift);<br />
This overload only participates in overload resolution if std::is_integral_v&lt;IntegerType&gt; is true. </p>
<p>&nbsp;std::operator|=,operator&amp;=,operator^= </p>
<p>constexpr std::byte&amp; operator|=(std::byte&amp; l, std::byte r) noexcept; <code>(1)</code> <i>(since C++17)</i><br />
constexpr std::byte&amp; operator&amp;=(std::byte&amp; l, std::byte r) noexcept; <code>(2)</code> <i>(since C++17)</i><br />
constexpr std::byte&amp; operator^=(std::byte&amp; l, std::byte r) noexcept; <code>(3)</code> <i>(since C++17)</i> </p>
<p>1) Equivalent to: return l = l | r;.<br />
2) Equivalent to: return l = l &amp; r;.<br />
3) Equivalent to: return l = l ^ r;. </p>
<p>&nbsp;std::operator|,operator&amp;,operator^,operator~ </p>
<p>constexpr std::byte operator|(std::byte l, std::byte r) noexcept; <code>(1)</code> <i>(since C++17)</i><br />
constexpr std::byte operator&amp;(std::byte l, std::byte r) noexcept; <code>(2)</code> <i>(since C++17)</i><br />
constexpr std::byte operator^(std::byte l, std::byte r) noexcept; <code>(3)</code> <i>(since C++17)</i><br />
constexpr std::byte operator~(std::byte b) noexcept; <code>(4)</code> <i>(since C++17)</i> </p>
<p>1) Equivalent to: return std::byte(static_cast&lt;unsigned int&gt;(l) | static_cast&lt;unsigned int&gt;(r));.<br />
2) Equivalent to: return std::byte(static_cast&lt;unsigned int&gt;(l) &amp; static_cast&lt;unsigned int&gt;(r));.<br />
3) Equivalent to: return std::byte(static_cast&lt;unsigned int&gt;(l) ^ static_cast&lt;unsigned int&gt;(r));.<br />
4) Equivalent to: return std::byte(~static_cast&lt;unsigned int&gt;(b));</p>
<h2>Notes</h2>
<p>A numeric value n can be converted to a byte value using std::byte{n}, due to C++17 relaxed enum class initialization rules.<br />
A byte can be converted to a numeric value (such as to produce an integer hash of an object) using std::to_integer. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
