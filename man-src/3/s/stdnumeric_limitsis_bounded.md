---
title: "stdnumeric_limitsis_bounded(3)"
name: "stdnumeric_limitsis_bounded"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsis_bounded/"
description: "std::numeric_limits<T>::is_bounded – std::numeric_limits<T>::is_bounded"
---

<p>std::numeric_limits&lt;T&gt;::is_bounded &#8211; std::numeric_limits&lt;T&gt;::is_bounded</p>
<h2>Synopsis</h2>
<pre><code>static const bool is_bounded;
(until C++ 11)

    static constexpr bool is_bounded;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::is_bounded is true for all arithmetic types T that represent a finite set of values. While all fundamental types are bounded, this constant would be false in a specialization of std::numeric_limits for a library-provided arbitrary precision arithmetic type. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::is_bounded<br />
/* non-specialized */ false<br />
bool true<br />
char true<br />
signed char true<br />
unsigned char true<br />
wchar_t true<br />
char8_t true<br />
char16_t true<br />
char32_t true<br />
short true<br />
unsigned short true<br />
int true<br />
unsigned int true<br />
long true<br />
unsigned long true<br />
long long true<br />
unsigned long long true<br />
float true<br />
double true<br />
long double true</p>
<h2>See also</h2>
<p>is_integer identifies integer types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_signed identifies signed types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_exact identifies exact types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
