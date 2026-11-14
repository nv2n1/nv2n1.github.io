---
title: "stdnumeric_limitsmax(3)"
name: "stdnumeric_limitsmax"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsmax/"
description: "std::numeric_limits<T>::max – std::numeric_limits<T>::max"
---

<p>std::numeric_limits&lt;T&gt;::max &#8211; std::numeric_limits&lt;T&gt;::max</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;limits&gt;<br />
static T max() throw(); <i>(until C++11)</i><br />
static constexpr T max() noexcept; <i>(since C++11)</i><br />
Returns the maximum finite value representable by the numeric type T. Meaningful for all bounded types. </p>
<h2>Return value</h2>
<p>T std::numeric_limits&lt;T&gt;::max()<br />
/* non-specialized */ T()<br />
bool true<br />
char CHAR_MAX<br />
signed char SCHAR_MAX<br />
unsigned char UCHAR_MAX<br />
wchar_t WCHAR_MAX<br />
char8_t UCHAR_MAX<br />
char16_t UINT_LEAST16_MAX<br />
char32_t UINT_LEAST32_MAX<br />
short SHRT_MAX<br />
unsigned short USHRT_MAX<br />
int INT_MAX<br />
unsigned int UINT_MAX<br />
long LONG_MAX<br />
unsigned long ULONG_MAX<br />
long long LLONG_MAX<br />
unsigned long long ULLONG_MAX<br />
float FLT_MAX<br />
double DBL_MAX<br />
long double LDBL_MAX </p>
<h2>Example</h2>
<p>Demonstrates the use of max() with some fundamental types and some standard library typedefs (the output is system-specific)<br />
 // Run this code </p>
<pre><code>#include &lt;limits&gt;

#include &lt;cstddef&gt;

#include &lt;iostream&gt;

int main()

{
    std::cout &lt;&lt; &quot;short: &quot; &lt;&lt; std::dec &lt;&lt; std::numeric_limits&lt;short&gt;::max()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; std::numeric_limits&lt;short&gt;::max() &lt;&lt; '
'
              &lt;&lt; &quot;int: &quot; &lt;&lt; std::dec &lt;&lt; std::numeric_limits&lt;int&gt;::max()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hex &lt;&lt; std::numeric_limits&lt;int&gt;::max() &lt;&lt; '
'
              &lt;&lt; std::dec
              &lt;&lt; &quot;streamsize: &quot; &lt;&lt; std::dec &lt;&lt; std::numeric_limits&lt;std::streamsize&gt;::max()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hex &lt;&lt; std::numeric_limits&lt;std::streamsize&gt;::max() &lt;&lt; '
'
              &lt;&lt; &quot;size_t: &quot; &lt;&lt; std::dec &lt;&lt; std::numeric_limits&lt;std::size_t&gt;::max()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hex &lt;&lt; std::numeric_limits&lt;std::size_t&gt;::max() &lt;&lt; '
'
              &lt;&lt; &quot;float: &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::max()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;float&gt;::max() &lt;&lt; '
'
              &lt;&lt; &quot;double: &quot; &lt;&lt; std::defaultfloat &lt;&lt; std::numeric_limits&lt;double&gt;::max()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;double&gt;::max() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;short: 32767 or 0x7fff<br />
&nbsp;<wbr>&nbsp;int: 2147483647 or 0x7fffffff<br />
&nbsp;<wbr>&nbsp;size_t: 18446744073709551615 or 0xffffffffffffffff<br />
&nbsp;<wbr>&nbsp;streamsize: 9223372036854775807 or 0x7fffffffffffffff<br />
&nbsp;<wbr>&nbsp;float: 3.40282e+38 or 0x1.fffffep+127<br />
&nbsp;<wbr>&nbsp;double: 1.79769e+308 or 0x1.fffffffffffffp+1023</p>
<h2>See also</h2>
<p>lowest returns the lowest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> <i>(C++11)</i><br />
min returns the smallest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
