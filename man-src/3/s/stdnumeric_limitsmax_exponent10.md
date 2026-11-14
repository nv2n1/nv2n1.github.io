---
title: "stdnumeric_limitsmax_exponent10(3)"
name: "stdnumeric_limitsmax_exponent10"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsmax_exponent10/"
description: "std::numeric_limits<T>::max_exponent10 – std::numeric_limits<T>::max_exponent10"
---

<p>std::numeric_limits&lt;T&gt;::max_exponent10 &#8211; std::numeric_limits&lt;T&gt;::max_exponent10</p>
<h2>Synopsis</h2>
<pre><code>static const int max_exponent10;
(until C++ 11)

    static constexpr int max_exponent10;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::max_exponent10 is the largest positive number n such that 10n<br />
is a representable finite value of the floating-point type T. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::max_exponent10<br />
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
float FLT_MAX_10_EXP<br />
double DBL_MAX_10_EXP<br />
long double LDBL_MAX_10_EXP</p>
<h2>Example</h2>
<p>Demonstrates the relationships of max_exponent, max_exponent10, and max() for the type float:<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

int main()

{
    std::cout &lt;&lt; &quot;max() = &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::max() &lt;&lt; '
'
              &lt;&lt; &quot;max_exponent10 = &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::max_exponent10 &lt;&lt; '
'
              &lt;&lt; std::hexfloat
              &lt;&lt; &quot;max() = &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::max() &lt;&lt; '
'
              &lt;&lt; &quot;max_exponent = &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::max_exponent &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;max() = 3.40282e+38<br />
&nbsp;<wbr>&nbsp;max_exponent10 = 38<br />
&nbsp;<wbr>&nbsp;max() = 0x1.fffffep+127<br />
&nbsp;<wbr>&nbsp;max_exponent = 128</p>
<h2>See also</h2>
<p>max_exponent one more than the largest integer power of the radix that is a valid finite floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
min_exponent one more than the smallest negative power of the radix that is a valid normalized floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
min_exponent10 the smallest negative power of ten that is a valid normalized floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
