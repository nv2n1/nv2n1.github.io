---
title: "stdnumeric_limitsquiet_nan(3)"
name: "stdnumeric_limitsquiet_nan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsquiet_nan/"
description: "std::numeric_limits<T>::quiet_NaN – std::numeric_limits<T>::quiet_NaN"
---

<p>std::numeric_limits&lt;T&gt;::quiet_NaN &#8211; std::numeric_limits&lt;T&gt;::quiet_NaN</p>
<h2>Synopsis</h2>
<pre><code>static T quiet_NaN() throw();             (until C++11)

static constexpr T quiet_NaN() noexcept;  (since C++11)</code></pre>
<p>Returns the special value &quot;quiet not-a-number&quot;, as represented by the floating-point type T. Only meaningful if std::numeric_limits&lt;T&gt;::has_quiet_NaN == true. In IEEE 754, the most common binary representation of floating-point numbers, any value with all bits of the exponent set and at least one bit of the fraction set represents a NaN. It is implementation-defined which values of the fraction represent quiet or signaling NaNs, and whether the sign bit is meaningful. </p>
<h2>Return value</h2>
<p>T std::numeric_limits&lt;T&gt;::quiet_NaN()<br />
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
float NAN or another implementation-defined NaN<br />
double implementation-defined<br />
long double implementation-defined </p>
<h2>Notes</h2>
<p>A NaN never compares equal to itself. Copying a NaN may not preserve its bit representation. </p>
<h2>Example</h2>
<p>Several ways to generate a NaN (the output string is compiler-specific)<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;limits&gt;

#include &lt;cmath&gt;
int main()

{
    std::cout &lt;&lt; std::numeric_limits&lt;double&gt;::quiet_NaN() &lt;&lt; ' '
              &lt;&lt; std::numeric_limits&lt;double&gt;::signaling_NaN() &lt;&lt; ' '
              &lt;&lt; std::acos(2) &lt;&lt; ' '
              &lt;&lt; std::tgamma(-1) &lt;&lt; ' '
              &lt;&lt; std::log(-1) &lt;&lt; ' '
              &lt;&lt; std::sqrt(-1) &lt;&lt; ' '
              &lt;&lt; 0 / 0.0 &lt;&lt; '
';
    std::cout &lt;&lt; &quot;NaN == NaN? &quot; &lt;&lt; std::boolalpha
              &lt;&lt; (std::numeric_limits&lt;double&gt;::quiet_NaN() == std::numeric_limits&lt;double&gt;::quiet_NaN()) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;nan nan nan nan nan -nan -nan<br />
&nbsp;<wbr>&nbsp;NaN == NaN? false</p>
<h2>See also</h2>
<p>has_quiet_NaN identifies floating-point types that can represent the special value &quot;quiet not-a-number&quot; (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
signaling_NaN returns a signaling NaN value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
nan<br />
nanf<br />
nanl not-a-number (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
isnan checks if the given number is NaN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
