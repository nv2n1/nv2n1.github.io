---
title: "stdnumeric_limitsis_modulo(3)"
name: "stdnumeric_limitsis_modulo"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsis_modulo/"
description: "std::numeric_limits<T>::is_modulo – std::numeric_limits<T>::is_modulo"
---

<p>std::numeric_limits&lt;T&gt;::is_modulo &#8211; std::numeric_limits&lt;T&gt;::is_modulo</p>
<h2>Synopsis</h2>
<pre><code>static const bool is_modulo;
(until C++ 11)

    static constexpr bool is_modulo;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::is_modulo is true for all arithmetic types T that<br />
are possible to<br />
<i>(until C++11)</i>handle overflows with modulo arithmetic, that is, if the result of addition, subtraction, multiplication, or division of this type would fall outside the range [min(), max()], the value returned by such operation differs from the expected value by a multiple of max()-min()+1.<br />
is_modulo is false for signed integer types, unless the implementation defines signed integer overflow to wrap. <i>(since C++11)</i> </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::is_modulo<br />
/* non-specialized */ false<br />
bool false<br />
char implementation-defined<br />
signed char implementation-defined<br />
unsigned char true<br />
wchar_t implementation-defined<br />
char8_t true<br />
char16_t true<br />
char32_t true<br />
short implementation-defined<br />
unsigned short true<br />
int implementation-defined<br />
unsigned int true<br />
long implementation-defined<br />
unsigned long true<br />
long long implementation-defined<br />
unsigned long long true<br />
float false<br />
double false<br />
long double false</p>
<h2>Notes</h2>
<p>Although the C++11 standard still says &quot;On most machines, this is true for signed integers.&quot;, it is a defect and has been corrected. The exact wording changed from C++03 to C++11 in such a way that the true value is no longer compatible with undefined_behavior_on_signed_integer_overflow. Because of that, the implementations that rely on signed overflow being undefined (for optimization opportunities) now set is_modulo to false for signed integers. See for example GCC_PR_22200. </p>
<h2>Example</h2>
<p>Demonstrates the behavior of modulo types<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;

#include &lt;limits&gt;
template &lt;class T&gt;

typename std::enable_if&lt;std::numeric_limits&lt;T&gt;::is_modulo&gt;::type
check_overflow()

{
    std::cout &lt;&lt; &quot;
max value is &quot; &lt;&lt; std::numeric_limits&lt;T&gt;::max() &lt;&lt; '
'
              &lt;&lt; &quot;min value is &quot; &lt;&lt; std::numeric_limits&lt;T&gt;::min() &lt;&lt; '
'
              &lt;&lt; &quot;max value + 1 is &quot; &lt;&lt; std::numeric_limits&lt;T&gt;::max() + 1 &lt;&lt; '
';
}
int main()

{
    check_overflow&lt;int&gt;();
    check_overflow&lt;unsigned long&gt;();
    // check_overflow&lt;float&gt;(); // compile-time error, not a modulo type
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;max value is 2147483647<br />
&nbsp;<wbr>&nbsp;min value is -2147483648<br />
&nbsp;<wbr>&nbsp;max value + 1 is -2147483648 </p>
<p>&nbsp;<wbr>&nbsp;max value is 18446744073709551615<br />
&nbsp;<wbr>&nbsp;min value is 0<br />
&nbsp;<wbr>&nbsp;max value + 1 is 0 </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
LWG_2422 C++11 is_modulo was required to true required to be false for signed integer types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for signed integer types on most machines unless signed integer overflow is defined to wrap</p>
<h2>See also</h2>
<p>is_integer identifies integer types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_iec559 identifies the IEC 559/IEEE 754 floating-point types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
is_exact identifies exact types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
