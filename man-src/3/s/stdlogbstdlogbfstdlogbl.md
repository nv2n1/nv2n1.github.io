---
title: "stdlogbstdlogbfstdlogbl(3)"
name: "stdlogbstdlogbfstdlogbl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlogbstdlogbfstdlogbl/"
description: "std::logb,std::logbf,std::logbl – std::logb,std::logbf,std::logbl"
---

<p>std::logb,std::logbf,std::logbl &#8211; std::logb,std::logbf,std::logbl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float logb ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float logbf( float arg );<br />
double logb ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double logb ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double logbl( long double arg );<br />
double logb ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Extracts the value of the unbiased radix-independent exponent from the floating-point argument arg, and returns it as a floating-point value.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double).<br />
Formally, the unbiased exponent is the signed integral part of log<br />
r|arg| (returned by this function as a floating-point value), for non-zero arg, where r is std::numeric_limits&lt;T&gt;::radix and T is the floating-point type of arg. If arg is subnormal, it is treated as though it was normalized. </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>If no errors occur, the unbiased exponent of arg is returned as a signed floating-point value.<br />
If a domain error occurs, an implementation-defined value is returned<br />
If a pole error occurs, -HUGE_VAL, -HUGE_VALF, or -HUGE_VALL is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
Domain or range error may occur if arg is zero.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If arg is ±0, -∞ is returned and FE_DIVBYZERO is raised.<br />
* If arg is ±∞, +∞ is returned<br />
* If arg is NaN, NaN is returned.<br />
* In all other cases, the result is exact (FE_INEXACT is never raised) and the_current_rounding_mode is ignored</p>
<h2>Notes</h2>
<p>POSIX_requires that a pole error occurs if arg is ±0.<br />
The value of the exponent returned by std::logb is always 1 less than the exponent retuned by std::frexp because of the different normalization requirements: for the exponent e returned by std::logb, |arg*r-e<br />
| is between 1 and r (typically between 1 and 2), but for the exponent e returned by std::frexp, |arg*2-e<br />
| is between 0.5 and 1. </p>
<h2>Example</h2>
<p>Compares different floating-point decomposition functions<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;limits&gt;

#include &lt;cfenv&gt;

#pragma STDC FENV_ACCESS ON

int main()

{
    double f = 123.45;
    std::cout &lt;&lt; &quot;Given the number &quot; &lt;&lt; f &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat
              &lt;&lt; f &lt;&lt; std::defaultfloat &lt;&lt; &quot; in hex,
&quot;;
    double f3;
    double f2 = std::modf(f, &amp;f3);
    std::cout &lt;&lt; &quot;modf() makes &quot; &lt;&lt; f3 &lt;&lt; &quot; + &quot; &lt;&lt; f2 &lt;&lt; '
';
    int i;
    f2 = std::frexp(f, &amp;i);
    std::cout &lt;&lt; &quot;frexp() makes &quot; &lt;&lt; f2 &lt;&lt; &quot; * 2^&quot; &lt;&lt; i &lt;&lt; '
';
    i = std::ilogb(f);
    std::cout &lt;&lt; &quot;logb()/ilogb() make &quot; &lt;&lt; f / std::scalbn(1.0, i) &lt;&lt; &quot; * &quot;
              &lt;&lt; std::numeric_limits&lt;double&gt;::radix
              &lt;&lt; &quot;^&quot; &lt;&lt; std::ilogb(f) &lt;&lt; '
';
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;logb(0) = &quot; &lt;&lt; std::logb(0) &lt;&lt; '
';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout &lt;&lt; &quot;    FE_DIVBYZERO raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Given the number 123.45 or 0x1.edccccccccccdp+6 in hex,<br />
&nbsp;<wbr>&nbsp;modf() makes 123 + 0.45<br />
&nbsp;<wbr>&nbsp;frexp() makes 0.964453 * 2^7<br />
&nbsp;<wbr>&nbsp;logb()/ilogb() make 1.92891 * 2^6<br />
&nbsp;<wbr>&nbsp;logb<code>(0)</code> = -Inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_DIVBYZERO raised</p>
<h2>See also</h2>
<p>frexp<br />
frexpf<br />
frexpl decomposes a number into significand and a power of 2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
ilogb<br />
ilogbf<br />
ilogbl extracts exponent of the number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
scalbn<br />
scalbnf<br />
scalbnl<br />
scalbln<br />
scalblnf<br />
scalblnl multiplies a number by FLT_RADIX raised to a power<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
