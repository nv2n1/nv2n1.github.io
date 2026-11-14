---
title: "stdnumeric_limitsdigits10(3)"
name: "stdnumeric_limitsdigits10"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsdigits10/"
description: "std::numeric_limits<T>::digits10 – std::numeric_limits<T>::digits10"
---

<p>std::numeric_limits&lt;T&gt;::digits10 &#8211; std::numeric_limits&lt;T&gt;::digits10</p>
<h2>Synopsis</h2>
<pre><code>static const int digits10;
(until C++ 11)

    static constexpr int digits10(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::digits10 is the number of base-10 digits that can be represented by the type T without change, that is, any number with this many significant decimal digits can be converted to a value of type T and back to decimal form, without change due to rounding or overflow. For base-radix types, it is the value of digits (digits-1 for floating-point types) multiplied by log<br />
10(radix) and rounded down. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::digits10<br />
/* non-specialized */ 0<br />
bool 0<br />
char std::numeric_limits&lt;char&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
signed char std::numeric_limits&lt;signed char&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
unsigned char std::numeric_limits&lt;unsigned char&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
wchar_t std::numeric_limits&lt;wchar_t&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
char8_t std::numeric_limits&lt;char8_t&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
char16_t std::numeric_limits&lt;char16_t&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
char32_t std::numeric_limits&lt;char32_t&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
short std::numeric_limits&lt;short&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
unsigned short std::numeric_limits&lt;unsigned short&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
int std::numeric_limits&lt;int&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
unsigned int std::numeric_limits&lt;unsigned int&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
long std::numeric_limits&lt;long&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
unsigned long std::numeric_limits&lt;unsigned long&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
long long std::numeric_limits&lt;long long&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
unsigned long long std::numeric_limits&lt;unsigned long long&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code><br />
float FLT_DIG /* 6 for IEEE float */<br />
double DBL_DIG /* 15 for IEEE double */<br />
long double LDBL_DIG /* 18 for 80-bit Intel long double */</p>
<h2>Example</h2>
<p>An 8-bit binary type can represent any two-digit decimal number exactly, but 3-digit decimal numbers 256..999 cannot be represented. The value of digits10 for an 8-bit type is 2 (8 * <a href="/docs/linux/man/2-std--log10/">std::log10</a>(2) is 2.41)<br />
The standard 32-bit IEEE 754 floating-point type has a 24 bit fractional part (23 bits written, one implied), which may suggest that it can represent 7 digit decimals (24 * <a href="/docs/linux/man/2-std--log10/">std::log10</a>(2) is 7.22), but relative rounding errors are non-uniform and some floating-point values with 7 decimal digits do not survive conversion to 32-bit float and back: the smallest positive example is 8.589973e9, which becomes 8.589974e9 after the roundtrip. These rounding errors cannot exceed one bit in the representation, and digits10 is calculated as (24-1)*<a href="/docs/linux/man/2-std--log10/">std::log10</a>(2), which is 6.92. Rounding down results in the value 6.<br />
Likewise, the 16-digit string 9007199254740993 does not survive text-&gt;double-&gt;text roundtrip, becoming 9007199254740992: the 64-bit IEEE 754 type double guarantees this roundtrip only for 15 decimal digits. </p>
<h2>See also</h2>
<p>radix the radix or integer base used by the representation of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
digits number of radix digits that can be represented without change<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
min_exponent one more than the smallest negative power of the radix that is a valid normalized floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
max_exponent one more than the largest integer power of the radix that is a valid finite floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
