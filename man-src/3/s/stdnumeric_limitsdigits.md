---
title: "stdnumeric_limitsdigits(3)"
name: "stdnumeric_limitsdigits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsdigits/"
description: "std::numeric_limits<T>::digits – std::numeric_limits<T>::digits"
---

<p>std::numeric_limits&lt;T&gt;::digits &#8211; std::numeric_limits&lt;T&gt;::digits</p>
<h2>Synopsis</h2>
<pre><code>static const int digits;
(until C++ 11)

    static constexpr int digits;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::digits is the number of digits in base-radix that can be represented by the type T without change. For integer types, this is the number of bits not counting the sign bit and the padding bits (if any). For floating-point types, this is the number of digits in the mantissa. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::digits (assuming no padding bits)<br />
/* non-specialized */ 0<br />
bool 1<br />
char CHAR_BIT &#8211; std::numeric_limits&lt;char&gt;::is_signed<br />
signed char CHAR_BIT &#8211; 1<br />
unsigned char CHAR_BIT<br />
wchar_t CHAR_BIT*sizeof(wchar_t) &#8211; std::numeric_limits&lt;wchar_t&gt;::is_signed<br />
char8_t CHAR_BIT<br />
char16_t CHAR_BIT*sizeof(char16_t)<br />
char32_t CHAR_BIT*sizeof(char32_t)<br />
short CHAR_BIT*sizeof(short)-1<br />
unsigned short CHAR_BIT*sizeof(short)<br />
int CHAR_BIT*sizeof(int)-1<br />
unsigned int CHAR_BIT*sizeof(int)<br />
long CHAR_BIT*sizeof(long)-1<br />
unsigned long CHAR_BIT*sizeof(long)<br />
long long CHAR_BIT*sizeof(long long)-1<br />
unsigned long long CHAR_BIT*sizeof(long long)<br />
float FLT_MANT_DIG<br />
double DBL_MANT_DIG<br />
long double LDBL_MANT_DIG</p>
<h2>See also</h2>
<p>radix the radix or integer base used by the representation of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
min_exponent one more than the smallest negative power of the radix that is a valid normalized floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
max_exponent one more than the largest integer power of the radix that is a valid finite floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
