---
title: "stdnumeric_limitstinyness_before(3)"
name: "stdnumeric_limitstinyness_before"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitstinyness_before/"
description: "std::numeric_limits<T>::tinyness_before – std::numeric_limits<T>::tinyness_before"
---

<p>std::numeric_limits&lt;T&gt;::tinyness_before &#8211; std::numeric_limits&lt;T&gt;::tinyness_before</p>
<h2>Synopsis</h2>
<pre><code>static const bool tinyness_before;
(until C++ 11)

    static constexpr bool tinyness_before;
(since C++ 11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::tinyness_before is true for all floating-point types T that test results of floating-point expressions for underflow before rounding. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::tinyness_before<br />
/* non-specialized */ false<br />
bool false<br />
char false<br />
signed char false<br />
unsigned char false<br />
wchar_t false<br />
char8_t false<br />
char16_t false<br />
char32_t false<br />
short false<br />
unsigned short false<br />
int false<br />
unsigned int false<br />
long false<br />
unsigned long false<br />
long long false<br />
unsigned long long false<br />
float implementation-defined<br />
double implementation-defined<br />
long double implementation-defined</p>
<h2>Notes</h2>
<p>Standard-compliant IEEE 754 floating-point implementations are required to detect the floating-point underflow, and have two alternative situations where this can be done<br />
1) Underflow occurs (and FE_UNDERFLOW may be raised) if a computation produces a result whose absolute value, computed as though both the exponent range and the precision were unbounded, is smaller than std::numeric_limits&lt;T&gt;::min(). Such implementation detects tinyness before rounding (e.g. UltraSparc, POWER).<br />
2) Underflow occurs (and FE_UNDERFLOW may be raised) if after the rounding of the result to the target floating-point type (that is, rounding to std::numeric_limits&lt;T&gt;::digits bits), the result&#8217;s absolute value is smaller than std::numeric_limits&lt;T&gt;::min(). Formally, the absolute value of a nonzero result computed as though the exponent range were unbounded is smaller than std::numeric_limits&lt;T&gt;::min(). Such implementation detects tinyness after rounding (e.g. SuperSparc) </p>
<h2>Example</h2>
<p>Multiplication of the largest subnormal number by the number one machine epsilon greater than 1.0 gives the tiny value 0x0.fffffffffffff8p-1022 before rounding, but normal value 1p-1022 after rounding. The implementation used to execute this test (IBM Power7) detects tinyness before rounding.<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;limits&gt;

#include &lt;cmath&gt;

#include &lt;cfenv&gt;

int main()

{
    std::cout &lt;&lt; &quot;Tinyness before: &quot; &lt;&lt; std::boolalpha
              &lt;&lt; std::numeric_limits&lt;double&gt;::tinyness_before &lt;&lt; '
';
    double denorm_max = std::nextafter(std::numeric_limits&lt;double&gt;::min(), 0);
    double multiplier = 1 + std::numeric_limits&lt;double&gt;::epsilon();
    std::feclearexcept(FE_ALL_EXCEPT);
    double result = denorm_max * multiplier; // Underflow only if tinyness_before
    if (std::fetestexcept(FE_UNDERFLOW))
        std::cout &lt;&lt; &quot;Underflow detected
&quot;;
    std::cout &lt;&lt; std::hexfloat &lt;&lt; denorm_max &lt;&lt; &quot; x &quot; &lt;&lt; multiplier &lt;&lt; &quot; = &quot;
              &lt;&lt; result &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Tinyness before: true<br />
&nbsp;<wbr>&nbsp;Underflow detected<br />
&nbsp;<wbr>&nbsp;0xf.ffffffffffffp-1030 x 0x1.0000000000001p+0 = 0x1p-1022</p>
<h2>See also</h2>
<p>has_denorm_loss identifies the floating-point types that detect loss of precision as denormalization loss rather than inexact result<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
has_denorm identifies the denormalization style used by the floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
