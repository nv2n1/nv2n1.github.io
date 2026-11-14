---
title: "stdnumeric_limitssignaling_nan(3)"
name: "stdnumeric_limitssignaling_nan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitssignaling_nan/"
description: "std::numeric_limits<T>::signaling_NaN – std::numeric_limits<T>::signaling_NaN"
---

<p>std::numeric_limits&lt;T&gt;::signaling_NaN &#8211; std::numeric_limits&lt;T&gt;::signaling_NaN</p>
<h2>Synopsis</h2>
<pre><code>static T signaling_NaN() throw();             (until C++11)

static constexpr T signaling_NaN() noexcept;  (since C++11)</code></pre>
<p>Returns the special value &quot;signaling not-a-number&quot;, as represented by the floating-point type T. Only meaningful if std::numeric_limits&lt;T&gt;::has_signaling_NaN == true. In IEEE 754, the most common binary representation of floating-point numbers, any value with all bits of the exponent set and at least one bit of the fraction set represents a NaN. It is implementation-defined which values of the fraction represent quiet or signaling NaNs, and whether the sign bit is meaningful. </p>
<h2>Return value</h2>
<p>T std::numeric_limits&lt;T&gt;::signaling_NaN()<br />
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
float implementation-defined<br />
double implementation-defined<br />
long double implementation-defined </p>
<h2>Notes</h2>
<p>A NaN never compares equal to itself. Copying a NaN is not required, by IEEE-754, to preserve its bit representation (sign and payload), though most implementation do.<br />
When a signaling NaN is used as an argument to an arithmetic expression, the appropriate floating-point exception may be raised and the NaN is &quot;quieted&quot;, that is, the expression returns a quiet NaN. </p>
<h2>Example</h2>
<p>Demonstrates the use of a signaling NaN to raise a floating-point exception<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;limits&gt;

#include &lt;cfenv&gt;

#pragma STDC_FENV_ACCESS on

void show_fe_exceptions()

{
    int n = std::fetestexcept(FE_ALL_EXCEPT);
    if (n &amp; FE_INVALID)
        std::cout &lt;&lt; &quot;FE_INVALID is raised
&quot;;
    else if (n == 0)
        std::cout &lt;&lt; &quot;no exceptions are raised
&quot;;
    std::feclearexcept(FE_ALL_EXCEPT);
}

int main()

{
    double snan = std::numeric_limits&lt;double&gt;::signaling_NaN();
    std::cout &lt;&lt; &quot;After sNaN was obtained &quot;;
    show_fe_exceptions();
    double qnan = snan * 2.0;
    std::cout &lt;&lt; &quot;After sNaN was multiplied by 2 &quot;;
    show_fe_exceptions();
    double qnan2 = qnan * 2.0;
    std::cout &lt;&lt; &quot;After the quieted NaN was multiplied by 2 &quot;;
    show_fe_exceptions();
    std::cout &lt;&lt; &quot;The result is &quot; &lt;&lt; qnan2 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;After sNaN was obtained no exceptions are raised<br />
&nbsp;<wbr>&nbsp;After sNaN was multiplied by 2 FE_INVALID is raised<br />
&nbsp;<wbr>&nbsp;After the quieted NaN was multiplied by 2 no exceptions are raised<br />
&nbsp;<wbr>&nbsp;The result is nan</p>
<h2>See also</h2>
<p>has_signaling_NaN identifies floating-point types that can represent the special value &quot;signaling not-a-number&quot; (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
quiet_NaN returns a quiet NaN value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
isnan checks if the given number is NaN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
