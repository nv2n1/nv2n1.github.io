---
title: "stdnumeric_limitsdenorm_min(3)"
name: "stdnumeric_limitsdenorm_min"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsdenorm_min/"
description: "std::numeric_limits<T>::denorm_min – std::numeric_limits<T>::denorm_min"
---

<p>std::numeric_limits&lt;T&gt;::denorm_min &#8211; std::numeric_limits&lt;T&gt;::denorm_min</p>
<h2>Synopsis</h2>
<pre><code>static T denorm_min() throw();             (until C++11)

static constexpr T denorm_min() noexcept;  (since C++11)</code></pre>
<p>Returns the minimum positive subnormal_value of the type T, if std::numeric_limits&lt;T&gt;::has_denorm != std::denorm_absent, otherwise returns std::numeric_limits&lt;T&gt;::min(). Only meaningful for floating-point types. </p>
<h2>Return value</h2>
<p>T std::numeric_limits&lt;T&gt;::denorm_min()<br />
/* non-specialized */ T()<br />
bool false<br />
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
float 2-149<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if std::numeric_limits&lt;float&gt;::is_iec559 == true<br />
double 2-1074<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if std::numeric_limits&lt;double&gt;::is_iec559 == true<br />
long double /* implementation-defined */ </p>
<h2>Example</h2>
<p>Demonstates the underlying bit structure of the denorm_min() and prints the values<br />
 // Run this code </p>
<pre><code>#include &lt;cassert&gt;

#include &lt;cstdint&gt;

#include &lt;cstring&gt;

#include &lt;iostream&gt;

#include &lt;limits&gt;
int main()

{
    // the smallest subnormal value has sign bit = 0, exponent = 0
    // and only the least significant bit of the fraction is 1
    std::uint32_t denorm_bits = 0x0001;
    float denorm_float;
    std::memcpy(&amp;denorm_float, &amp;denorm_bits, sizeof(float));
    assert(denorm_float == std::numeric_limits&lt;float&gt;::denorm_min());
    std::cout &lt;&lt; &quot;float	min()		denorm_min()
&quot;;
    std::cout &lt;&lt; &quot;	&quot; &lt;&lt; std::numeric_limits&lt;float&gt;::min() &lt;&lt; '	';
    std::cout &lt;&lt; std::numeric_limits&lt;float&gt;::denorm_min() &lt;&lt; '
';
    std::cout &lt;&lt; &quot;double	min()		denorm_min()
&quot;;
    std::cout &lt;&lt; &quot;	&quot; &lt;&lt; std::numeric_limits&lt;double&gt;::min() &lt;&lt; '	';
    std::cout &lt;&lt; std::numeric_limits&lt;double&gt;::denorm_min() &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;float<tt> </tt>min()<tt> </tt><tt> </tt>denorm_min()</p>
<p>&nbsp;<wbr>&nbsp;<tt> </tt>1.17549e-38<tt> </tt>1.4013e-45</p>
<p>&nbsp;<wbr>&nbsp;double<tt> </tt>min()<tt> </tt><tt> </tt>denorm_min()</p>
<p>&nbsp;<wbr>&nbsp;<tt> </tt>2.22507e-308<tt> </tt>4.94066e-324</p>
<h2>See also</h2>
<p>min returns the smallest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
has_denorm identifies the denormalization style used by the floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
lowest returns the lowest finite value of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> <i>(C++11)</i> </p>
