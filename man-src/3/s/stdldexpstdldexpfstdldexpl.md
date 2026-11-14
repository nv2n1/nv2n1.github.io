---
title: "stdldexpstdldexpfstdldexpl(3)"
name: "stdldexpstdldexpfstdldexpl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdldexpstdldexpfstdldexpl/"
description: "std::ldexp,std::ldexpf,std::ldexpl – std::ldexp,std::ldexpf,std::ldexpl"
---

<p>std::ldexp,std::ldexpf,std::ldexpl &#8211; std::ldexp,std::ldexpf,std::ldexpl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float ldexp ( float x, int exp );<br />
float ldexpf( float x, int exp ); <i>(since C++11)</i><br />
double ldexp ( double x, int exp ); <code>(1)</code> <code>(2)</code><br />
long double ldexp ( long double x, int exp );<br />
long double ldexpl( long double x, int exp ); <code>(3)</code> <i>(since C++11)</i><br />
double ldexp ( IntegralType x, int exp ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Multiplies a floating point value x by the number 2 raised to the exp power.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>x &#8211; floating point value<br />
exp &#8211; integer value</p>
<h2>Return value</h2>
<p>If no errors occur, x multiplied by 2 to the power of exp (x×2exp<br />
) is returned.<br />
If a range error due to overflow occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned.<br />
If a range error due to underflow occurs, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* Unless a range error occurs, FE_INEXACT is never raised (the result is exact)<br />
* Unless a range error occurs, the_current_rounding_mode is ignored<br />
* If x is ±0, it is returned, unmodified<br />
* If x is ±∞, it is returned, unmodified<br />
* If exp is 0, then x is returned, unmodified<br />
* If x is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>On binary systems (where FLT_RADIX is 2), std::ldexp is equivalent to std::scalbn.<br />
The function std::ldexp (&quot;load exponent&quot;), together with its dual, std::frexp, can be used to manipulate the representation of a floating-point number without direct bit manipulations.<br />
On many implementations, std::ldexp is less efficient than multiplication or division by a power of two using arithmetic operators. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cstring&gt;

#include &lt;cfenv&gt;
#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;ldexp(7, -4) = &quot; &lt;&lt; std::ldexp(7, -4) &lt;&lt; '
'
              &lt;&lt; &quot;ldexp(1, -1074) = &quot; &lt;&lt; std::ldexp(1, -1074)
              &lt;&lt; &quot; (minimum positive subnormal double)
&quot;
              &lt;&lt; &quot;ldexp(nextafter(1,0), 1024) = &quot;
              &lt;&lt; std::ldexp(std::nextafter(1, 0), 1024)
              &lt;&lt; &quot; (largest finite double)
&quot;;
    // special values
    std::cout &lt;&lt; &quot;ldexp(-0, 10) = &quot; &lt;&lt; std::ldexp(-0.0, 10) &lt;&lt; '
'
              &lt;&lt; &quot;ldexp(-Inf, -1) = &quot; &lt;&lt; std::ldexp(-INFINITY, -1) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;ldexp(1, 1024) = &quot; &lt;&lt; std::ldexp(1, 1024) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno == ERANGE: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout &lt;&lt; &quot;    FE_OVERFLOW raised
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;ldexp(7, -4) = 0.4375<br />
&nbsp;<wbr>&nbsp;ldexp(1, -1074) = 4.94066e-324 (minimum positive subnormal double)<br />
&nbsp;<wbr>&nbsp;ldexp(nextafter(1,0), 1024) = 1.79769e+308 (largest finite double)<br />
&nbsp;<wbr>&nbsp;ldexp(-0, 10) = -0<br />
&nbsp;<wbr>&nbsp;ldexp(-Inf, -1) = -inf<br />
&nbsp;<wbr>&nbsp;ldexp(1, 1024) = inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_OVERFLOW raised</p>
<h2>See also</h2>
<p>frexp<br />
frexpf<br />
frexpl decomposes a number into significand and a power of 2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
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
