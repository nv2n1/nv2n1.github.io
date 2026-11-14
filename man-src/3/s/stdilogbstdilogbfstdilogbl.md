---
title: "stdilogbstdilogbfstdilogbl(3)"
name: "stdilogbstdilogbfstdilogbl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdilogbstdilogbfstdilogbl/"
description: "std::ilogb,std::ilogbf,std::ilogbl – std::ilogb,std::ilogbf,std::ilogbl"
---

<p>std::ilogb,std::ilogbf,std::ilogbl &#8211; std::ilogb,std::ilogbf,std::ilogbl</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cmath&gt;

    int ilogb(float arg);
(1)(since C++ 11)

    int ilogbf(float arg);

int ilogb(double arg);
(2)(since C++ 11)

    int ilogb(long double arg);
(3)(since C++ 11)

    int ilogbl(long double arg);

int ilogb(IntegralType arg);
(4)(since C++ 11)

#define FP_ILOGB0 /*implementation-defined*/ (5)(since C++ 11)

#define FP_ILOGBNAN /*implementation-defined*/ (6)(since C++ 11)</code></pre>
<p>1-3) Extracts the value of the unbiased exponent from the floating-point argument arg, and returns it as a signed integer value.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double).<br />
5) Expands to integer constant expression whose value is either INT_MIN or -INT_MAX.<br />
6) Expands to integer constant expression whose value is either INT_MIN or +INT_MAX.<br />
Formally, the unbiased exponent is the integral part of log<br />
r|arg| as a signed integral value, for non-zero arg, where r is std::numeric_limits&lt;T&gt;::radix and T is the floating-point type of arg. </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>If no errors occur, the unbiased exponent of arg is returned as a signed int value.<br />
If arg is zero, FP_ILOGB0 is returned.<br />
If arg is infinite, INT_MAX is returned.<br />
If arg is a NaN, FP_ILOGBNAN is returned.<br />
If the correct result is greater than INT_MAX or smaller than INT_MIN, the return value is unspecified. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
A domain error or range error may occur if arg is zero, infinite, or NaN.<br />
If the correct result is greater than INT_MAX or smaller than INT_MIN, a domain error or a range error may occur<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the correct result is greater than INT_MAX or smaller than INT_MIN, FE_INVALID is raised.<br />
* If arg is ±0, ±∞, or NaN, FE_INVALID is raised.<br />
* In all other cases, the result is exact (FE_INEXACT is never raised) and the_current_rounding_mode is ignored</p>
<h2>Notes</h2>
<p>If arg is not zero, infinite, or NaN, the value returned is exactly equivalent to static_cast&lt;int&gt;(std::logb(arg))<br />
POSIX_requires that a domain error occurs if arg is zero, infinite, NaN, or if the correct result is outside of the range of int.<br />
POSIX also requires that, on XSI-conformant systems, the value returned when the correct result is greater than INT_MAX is INT_MAX and the value returned when the correct result is less than INT_MIN is INT_MIN.<br />
The correct result can be represented as int on all known implementations. For overflow to occur, INT_MAX must be less than LDBL_MAX_EXP*log2(FLT_RADIX) or INT_MIN must be greater than LDBL_MIN_EXP-LDBL_MANT_DIG)*log2(FLT_RADIX).<br />
The value of the exponent returned by std::ilogb is always 1 less than the exponent retuned by std::frexp because of the different normalization requirements: for the exponent e returned by std::ilogb, |arg*r-e<br />
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
    std::cout &lt;&lt; &quot;ilogb(0) = &quot; &lt;&lt; std::ilogb(0) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Given the number 123.45 or 0x1.edccccccccccdp+6 in hex,<br />
&nbsp;<wbr>&nbsp;modf() makes 123 + 0.45<br />
&nbsp;<wbr>&nbsp;frexp() makes 0.964453 * 2^7<br />
&nbsp;<wbr>&nbsp;logb()/ilogb() make 1.92891 * 2^6<br />
&nbsp;<wbr>&nbsp;ilogb<code>(0)</code> = -2147483648<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>frexp<br />
frexpf<br />
frexpl decomposes a number into significand and a power of 2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
logb<br />
logbf<br />
logbl extracts exponent of the number<br />
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
