---
title: "stdnumeric_limitsis_specialized(3)"
name: "stdnumeric_limitsis_specialized"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsis_specialized/"
description: "std::numeric_limits<T>::is_specialized – std::numeric_limits<T>::is_specialized"
---

<p>std::numeric_limits&lt;T&gt;::is_specialized &#8211; std::numeric_limits&lt;T&gt;::is_specialized</p>
<h2>Synopsis</h2>
<pre><code>static const bool is_specialized;
(until C++ 11)

    static constexpr bool is_specialized;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::is_specialized is true for all T for which there exists a specialization of std::numeric_limits. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::is_specialized<br />
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
is_iec559 identifies the IEC 559/IEEE 754 floating-point types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_exact identifies exact types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_bounded identifies types that represent a finite set of values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
