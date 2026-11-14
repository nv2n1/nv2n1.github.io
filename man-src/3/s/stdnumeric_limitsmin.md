---
title: "stdnumeric_limitsmin(3)"
name: "stdnumeric_limitsmin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsmin/"
description: "std::numeric_limits<T>::min – std::numeric_limits<T>::min"
---

<p>std::numeric_limits&lt;T&gt;::min &#8211; std::numeric_limits&lt;T&gt;::min</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;limits&gt;<br />
static T min() throw(); <i>(until C++11)</i><br />
static constexpr T min() noexcept; <i>(since C++11)</i><br />
Returns the minimum finite value representable by the numeric type T.<br />
For floating-point types with denormalization, min returns the minimum positive normalized value. Note that this behavior may be unexpected, especially when compared to the behavior of min for integral types. To find the value that has no values less than it, use numeric_limits::lowest.<br />
min is only meaningful for bounded types and for unbounded unsigned types, that is, types that represent an infinite set of negative values have no meaningful minimum. </p>
<h2>Return value</h2>
<p>T std::numeric_limits&lt;T&gt;::min()<br />
/* non-specialized */ T()<br />
bool false<br />
char CHAR_MIN<br />
signed char SCHAR_MIN<br />
unsigned char 0<br />
wchar_t WCHAR_MIN<br />
char8_t 0<br />
char16_t 0<br />
char32_t 0<br />
short SHRT_MIN<br />
unsigned short 0<br />
int INT_MIN<br />
unsigned int 0<br />
long LONG_MIN<br />
unsigned long 0<br />
long long LLONG_MIN<br />
unsigned long long 0<br />
float FLT_MIN<br />
double DBL_MIN<br />
long double LDBL_MIN </p>
<h2>Example</h2>
<p>Demonstrates the use with typedef types, and the difference in the sign of the result between integer and floating-point types<br />
 // Run this code </p>
<pre><code>#include &lt;limits&gt;

#include &lt;cstddef&gt;

#include &lt;iostream&gt;
int main()

{
    std::cout
        &lt;&lt; &quot;short: &quot; &lt;&lt; std::dec &lt;&lt; std::numeric_limits&lt;short&gt;::min()
        &lt;&lt; &quot; or &quot; &lt;&lt; std::hex &lt;&lt; std::showbase
        &lt;&lt; std::numeric_limits&lt;short&gt;::min() &lt;&lt; '
'
        &lt;&lt; &quot;int: &quot; &lt;&lt; std::dec &lt;&lt; std::numeric_limits&lt;int&gt;::min() &lt;&lt; std::showbase
        &lt;&lt; &quot; or &quot; &lt;&lt; std::hex &lt;&lt; std::numeric_limits&lt;int&gt;::min() &lt;&lt; '
'
        &lt;&lt; std::dec
        &lt;&lt; &quot;ptrdiff_t: &quot; &lt;&lt; std::numeric_limits&lt;std::ptrdiff_t&gt;::min() &lt;&lt; std::showbase
        &lt;&lt; &quot; or &quot; &lt;&lt; std::hex &lt;&lt; std::numeric_limits&lt;std::ptrdiff_t&gt;::min() &lt;&lt; '
'
        &lt;&lt; &quot;float: &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::min()
        &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;float&gt;::min() &lt;&lt; '
'
        &lt;&lt; &quot;double: &quot; &lt;&lt; std::defaultfloat &lt;&lt; std::numeric_limits&lt;double&gt;::min()
        &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;double&gt;::min() &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;short: -32768 or 0x8000<br />
&nbsp;<wbr>&nbsp;int: -2147483648 or 0x80000000<br />
&nbsp;<wbr>&nbsp;ptrdiff_t: -9223372036854775808 or 0x8000000000000000<br />
&nbsp;<wbr>&nbsp;float: 1.17549e-38 or 0x1p-126<br />
&nbsp;<wbr>&nbsp;double: 2.22507e-308 or 0x1p-1022</p>
<h2>See also</h2>
<p>lowest returns the lowest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> <i>(C++11)</i><br />
denorm_min returns the smallest positive subnormal value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
max returns the largest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
