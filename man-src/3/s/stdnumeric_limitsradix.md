---
title: "stdnumeric_limitsradix(3)"
name: "stdnumeric_limitsradix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsradix/"
description: "std::numeric_limits<T>::radix – std::numeric_limits<T>::radix"
---

<p>std::numeric_limits&lt;T&gt;::radix &#8211; std::numeric_limits&lt;T&gt;::radix</p>
<h2>Synopsis</h2>
<pre><code>static const int radix;
(until C++ 11)

    static constexpr int radix;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::radix is the base of the number system used in the representation of the type. It is 2 for all binary numeric types, but it may be, for example, 10 for IEEE 754 decimal_floating-point_types or for third-party binary-coded_decimal integers. This constant is meaningful for all specializations. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::radix<br />
/* non-specialized */ 0<br />
bool 2<br />
char 2<br />
signed char 2<br />
unsigned char 2<br />
wchar_t 2<br />
char8_t 2<br />
char16_t 2<br />
char32_t 2<br />
short 2<br />
unsigned short 2<br />
int 2<br />
unsigned int 2<br />
long 2<br />
unsigned long 2<br />
long long 2<br />
unsigned long long 2<br />
float FLT_RADIX<br />
double FLT_RADIX<br />
long double FLT_RADIX</p>
<h2>See also</h2>
<p>digits number of radix digits that can be represented without change<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
min_exponent one more than the smallest negative power of the radix that is a valid normalized floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
max_exponent one more than the largest integer power of the radix that is a valid finite floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
