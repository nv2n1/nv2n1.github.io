---
title: "stdscalbnstdscalbnfstdscalbnlstdscalblnstdscalblnfstdscalblnl(3)"
name: "stdscalbnstdscalbnfstdscalbnlstdscalblnstdscalblnfstdscalblnl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdscalbnstdscalbnfstdscalbnlstdscalblnstdscalblnfstdscalblnl/"
description: "std::scalbn,std::scalbnf,std::scalbnl,std::scalbln,std::scalblnf,std::scalblnl – std::scalbn,std::scalbnf,std::scalbnl,std::scalbln,std::scalblnf,std::scalblnl"
---

<p>std::scalbn,std::scalbnf,std::scalbnl,std::scalbln,std::scalblnf,std::scalblnl &#8211; std::scalbn,std::scalbnf,std::scalbnl,std::scalbln,std::scalblnf,std::scalblnl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float scalbn ( float x, int exp ); <code>(1)</code> <i>(since C++11)</i><br />
float scalbnf( float x, int exp );<br />
double scalbn ( double x, int exp ); <code>(2)</code> <i>(since C++11)</i><br />
long double scalbn ( long double x, int exp ); <code>(3)</code> <i>(since C++11)</i><br />
long double scalbnl( long double x, int exp );<br />
double scalbn ( IntegralType x, int exp ); <code>(4)</code> <i>(since C++11)</i><br />
float scalbln ( float x, long exp ); <code>(5)</code> <i>(since C++11)</i><br />
float scalblnf( float x, long exp );<br />
double scalbln ( double x, long exp ); <code>(6)</code> <i>(since C++11)</i><br />
long double scalbln ( long double x, long exp ); <code>(7)</code> <i>(since C++11)</i><br />
long double scalblnl( long double x, long exp );<br />
double scalbln ( IntegralType x, long exp ); <code>(8)</code> <i>(since C++11)</i><br />
1-3,5-7) Multiplies a floating point value x by FLT_RADIX raised to power exp.<br />
4,8) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(2)</code> or <code>(6)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>x &#8211; floating point value<br />
exp &#8211; integer value</p>
<h2>Return value</h2>
<p>If no errors occur, x multiplied by FLT_RADIX to the power of arg (x×FLT_RADIXexp<br />
) is returned.<br />
If a range error due to overflow occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned.<br />
If a range error due to underflow occurs, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* Unless a range error occurs, FE_INEXACT is never raised (the result is exact)<br />
* Unless a range error occurs, the_current_rounding_mode is ignored<br />
* If x is ±0, it is returned, unmodified<br />
* If x is ±∞, it is returned, unmodified<br />
* If exp is 0, then x is returned, unmodified<br />
* If x is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>On binary systems (where FLT_RADIX is 2), std::scalbn is equivalent to std::ldexp.<br />
Although std::scalbn and std::scalbln are specified to perform the operation efficiently, on many implementations they are less efficient than multiplication or division by a power of two using arithmetic operators.<br />
The function name stands for &quot;new scalb&quot;, where scalb was an older non-standard function whose second argument had floating-point type.<br />
The scalbln function is provided because the factor required to scale from the smallest positive floating-point value to the largest finite one may be greater than 32767, the standard-guaranteed INT_MAX. In particular, for the 80-bit long double, the factor is 32828.<br />
The GNU implementation does not set errno regardless of math_errhandling </p>
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
    std::cout &lt;&lt; &quot;scalbn(7, -4) = &quot; &lt;&lt; std::scalbn(7, -4) &lt;&lt; '
'
              &lt;&lt; &quot;scalbn(1, -1074) = &quot; &lt;&lt; std::scalbn(1, -1074)
              &lt;&lt; &quot; (minimum positive subnormal double)
&quot;
              &lt;&lt; &quot;scalbn(nextafter(1,0), 1024) = &quot;
              &lt;&lt; std::scalbn(std::nextafter(1, 0), 1024)
              &lt;&lt; &quot; (largest finite double)
&quot;;
    // special values
    std::cout &lt;&lt; &quot;scalbn(-0, 10) = &quot; &lt;&lt; std::scalbn(-0.0, 10) &lt;&lt; '
'
              &lt;&lt; &quot;scalbn(-Inf, -1) = &quot; &lt;&lt; std::scalbn(-INFINITY, -1) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;scalbn(1, 1024) = &quot; &lt;&lt; std::scalbn(1, 1024) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno == ERANGE: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout &lt;&lt; &quot;    FE_OVERFLOW raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;scalbn(7, -4) = 0.4375<br />
&nbsp;<wbr>&nbsp;scalbn(1, -1074) = 4.94066e-324 (minimum positive subnormal double)<br />
&nbsp;<wbr>&nbsp;scalbn(nextafter(1,0), 1024) = 1.79769e+308 (largest finite double)<br />
&nbsp;<wbr>&nbsp;scalbn(-0, 10) = -0<br />
&nbsp;<wbr>&nbsp;scalbn(-Inf, -1) = -inf<br />
&nbsp;<wbr>&nbsp;scalbn(1, 1024) = inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_OVERFLOW raised</p>
<h2>See also</h2>
<p>frexp<br />
frexpf<br />
frexpl decomposes a number into significand and a power of 2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
ldexp<br />
ldexpf<br />
ldexpl multiplies a number by 2 raised to a power<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
