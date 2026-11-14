---
title: "stdnumeric_limitsmin_exponent10(3)"
name: "stdnumeric_limitsmin_exponent10"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsmin_exponent10/"
description: "std::numeric_limits<T>::min_exponent10 – std::numeric_limits<T>::min_exponent10"
---

<p>std::numeric_limits&lt;T&gt;::min_exponent10 &#8211; std::numeric_limits&lt;T&gt;::min_exponent10</p>
<h2>Synopsis</h2>
<pre><code>static const int min_exponent10;
(until C++ 11)

    static constexpr int min_exponent10;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::min_exponent10 is the lowest negative number n such that 10n<br />
is a valid normalized value of the floating-point type T. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::min_exponent10<br />
/* non-specialized */ 0<br />
bool 0<br />
char 0<br />
signed char 0<br />
unsigned char 0<br />
wchar_t 0<br />
char8_t 0<br />
char16_t 0<br />
char32_t 0<br />
short 0<br />
unsigned short 0<br />
int 0<br />
unsigned int 0<br />
long 0<br />
unsigned long 0<br />
long long 0<br />
unsigned long long 0<br />
float FLT_MIN_10_EXP<br />
double DBL_MIN_10_EXP<br />
long double LDBL_MIN_10_EXP</p>
<h2>Example</h2>
<p>Demonstrates the relationships of min_exponent, min_exponent10, min, and radix for the type float:<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

int main()

{
    std::cout &lt;&lt; &quot;min() = &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::min() &lt;&lt; '
'
              &lt;&lt; &quot;min_exponent10 = &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::min_exponent10 &lt;&lt; '
'
              &lt;&lt; std::hexfloat
              &lt;&lt; &quot;min() = &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::min() &lt;&lt; '
'
              &lt;&lt; &quot;min_exponent = &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::min_exponent &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;min() = 1.17549e-38<br />
&nbsp;<wbr>&nbsp;min_exponent10 = -37<br />
&nbsp;<wbr>&nbsp;min() = 0x1p-126<br />
&nbsp;<wbr>&nbsp;min_exponent = -125</p>
<h2>See also</h2>
<p>min_exponent one more than the smallest negative power of the radix that is a valid normalized floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
max_exponent one more than the largest integer power of the radix that is a valid finite floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
max_exponent10 the largest integer power of 10 that is a valid finite floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
