---
title: "stdnumeric_limitsis_signed(3)"
name: "stdnumeric_limitsis_signed"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsis_signed/"
description: "std::numeric_limits<T>::is_signed – std::numeric_limits<T>::is_signed"
---

<p>std::numeric_limits&lt;T&gt;::is_signed &#8211; std::numeric_limits&lt;T&gt;::is_signed</p>
<h2>Synopsis</h2>
<pre><code>static const bool is_signed;
(until C++ 11)

    static constexpr bool is_signed;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::is_signed is true for all signed arithmetic types T and false for the unsigned types. This constant is meaningful for all specializations. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::is_signed<br />
/* non-specialized */ false<br />
bool false<br />
char implementation-defined<br />
signed char true<br />
unsigned char false<br />
wchar_t implementation-defined<br />
char8_t false<br />
char16_t false<br />
char32_t false<br />
short true<br />
unsigned short false<br />
int true<br />
unsigned int false<br />
long true<br />
unsigned long false<br />
long long true<br />
unsigned long long false<br />
float true<br />
double true<br />
long double true</p>
<h2>See also</h2>
<p>is_signed checks if a type is a signed arithmetic type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_integer identifies integer types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_exact identifies exact types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_bounded identifies types that represent a finite set of values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
