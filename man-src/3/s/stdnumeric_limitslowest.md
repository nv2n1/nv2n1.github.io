---
title: "stdnumeric_limitslowest(3)"
name: "stdnumeric_limitslowest"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitslowest/"
description: "std::numeric_limits<T>::lowest – std::numeric_limits<T>::lowest"
---

<p>std::numeric_limits&lt;T&gt;::lowest &#8211; std::numeric_limits&lt;T&gt;::lowest</p>
<h2>Synopsis</h2>
<pre><code>static constexpr T lowest() noexcept;  (since C++11)</code></pre>
<p>Returns the lowest finite value representable by the numeric type T, that is, a finite value x such that there is no other finite value y where y &lt; x. This is different from std::numeric_limits&lt;T&gt;::min() for floating-point types. Only meaningful for bounded types. </p>
<h2>Return value</h2>
<p>T std::numeric_limits&lt;T&gt;::lowest()<br />
/* non-specialized */ T();<br />
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
float -FLT_MAX<br />
double -DBL_MAX<br />
long double -LDBL_MAX </p>
<h2>Notes</h2>
<p>While it&#8217;s not true for fundamental C++ floating-point types, a third-party floating-point type T may exist such that std::numeric_limits&lt;T&gt;::lowest() != -std::numeric_limits&lt;T&gt;::max(). </p>
<h2>Example</h2>
<p>Demonstrates min, max, and lowest for floating-point types<br />
 // Run this code </p>
<pre><code>#include &lt;limits&gt;

#include &lt;iostream&gt;

int main()

{
    std::cout &lt;&lt; &quot;std::numeric_limits&lt;T&gt;::min():
&quot;
              &lt;&lt; &quot;	float: &quot; &lt;&lt; std::numeric_limits&lt;float&gt;::min()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;float&gt;::min() &lt;&lt; '
'
              &lt;&lt; &quot;	double: &quot; &lt;&lt; std::defaultfloat &lt;&lt; std::numeric_limits&lt;double&gt;::min()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;double&gt;::min() &lt;&lt; '
';
    std::cout &lt;&lt; &quot;std::numeric_limits&lt;T&gt;::lowest():
&quot;
              &lt;&lt; &quot;	float: &quot; &lt;&lt; std::defaultfloat &lt;&lt; std::numeric_limits&lt;float&gt;::lowest()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;float&gt;::lowest() &lt;&lt; '
'
              &lt;&lt; &quot;	double: &quot; &lt;&lt; std::defaultfloat &lt;&lt; std::numeric_limits&lt;double&gt;::lowest()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;double&gt;::lowest() &lt;&lt; '
';
    std::cout &lt;&lt; &quot;std::numeric_limits&lt;T&gt;::max():
&quot;
              &lt;&lt; &quot;	float: &quot; &lt;&lt; std::defaultfloat &lt;&lt; std::numeric_limits&lt;float&gt;::max()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;float&gt;::max() &lt;&lt; '
'
              &lt;&lt; &quot;	double: &quot; &lt;&lt; std::defaultfloat &lt;&lt; std::numeric_limits&lt;double&gt;::max()
              &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat &lt;&lt; std::numeric_limits&lt;double&gt;::max() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;std::numeric_limits&lt;T&gt;::min():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;float: 1.17549e-38 or 0x1p-126<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double: 2.22507e-308 or 0x1p-1022<br />
&nbsp;<wbr>&nbsp;std::numeric_limits&lt;T&gt;::lowest():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;float: -3.40282e+38 or -0x1.fffffep+127<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double: -1.79769e+308 or -0x1.fffffffffffffp+1023<br />
&nbsp;<wbr>&nbsp;std::numeric_limits&lt;T&gt;::max():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;float: 3.40282e+38 or 0x1.fffffep+127<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double: 1.79769e+308 or 0x1.fffffffffffffp+1023</p>
<h2>See also</h2>
<p>min returns the smallest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
denorm_min returns the smallest positive subnormal value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
max returns the largest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
