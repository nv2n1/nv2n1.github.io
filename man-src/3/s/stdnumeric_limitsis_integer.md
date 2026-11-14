---
title: "stdnumeric_limitsis_integer(3)"
name: "stdnumeric_limitsis_integer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsis_integer/"
description: "std::numeric_limits<T>::is_integer – std::numeric_limits<T>::is_integer"
---

<p>std::numeric_limits&lt;T&gt;::is_integer &#8211; std::numeric_limits&lt;T&gt;::is_integer</p>
<h2>Synopsis</h2>
<pre><code>static const bool is_integer;
(until C++ 11)

    static constexpr bool is_integer;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::is_integer is true for all integer arithmetic types T and false otherwise. This constant is meaningful for all specializations. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::is_integer<br />
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
float false<br />
double false<br />
long double false</p>
<h2>See also</h2>
<p>is_integral checks if a type is an integral type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_signed identifies signed types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_exact identifies exact types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_bounded identifies types that represent a finite set of values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
