---
title: "stdpowstdpowfstdpowl(3)"
name: "stdpowstdpowfstdpowl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpowstdpowfstdpowl/"
description: "std::pow,std::powf,std::powl – std::pow,std::powf,std::powl"
---

<p>std::pow,std::powf,std::powl &#8211; std::pow,std::powf,std::powl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float pow ( float base, float exp );<br />
float powf( float base, float exp ); <i>(since C++11)</i><br />
double pow ( double base, double exp ); <code>(2)</code><br />
long double pow ( long double base, long double exp );<br />
long double powl( long double base, long double exp ); <code>(1)</code> <i>(since C++11)</i><br />
float pow ( float base, int iexp ); <code>(3)</code> <code>(4)</code> <i>(until C++11)</i><br />
double pow ( double base, int iexp ); <code>(5)</code> <i>(until C++11)</i><br />
long double pow ( long double base, int iexp ); <code>(6)</code> <i>(until C++11)</i><br />
Promoted pow ( Arithmetic1 base, Arithmetic2 exp ); <code>(7)</code> <i>(since C++11)</i><br />
1-6) Computes the value of base raised to the power exp or iexp.<br />
7) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by 1-3). If any argument has integral_type, it is cast to double. If any argument is long double, then the return type Promoted is also long double, otherwise the return type is always double. </p>
<h2>Parameters</h2>
<p>base &#8211; base as a value of floating-point or integral_type<br />
exp &#8211; exponent as a value of floating-point or integral_type<br />
iexp &#8211; exponent as integer value</p>
<h2>Return value</h2>
<p>If no errors occur, base raised to the power of exp (or iexp) (baseexp<br />
), is returned.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a pole error or a range error due to overflow occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If base is finite and negative and exp is finite and non-integer, a domain error occurs and a range error may occur.<br />
If base is zero and exp is zero, a domain error may occur.<br />
If base is zero and exp is negative, a domain error or a pole error may occur.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* pow(+0, exp), where exp is a negative odd integer, returns +∞ and raises FE_DIVBYZERO<br />
* pow(-0, exp), where exp is a negative odd integer, returns -∞ and raises FE_DIVBYZERO<br />
* pow(±0, exp), where exp is negative, finite, and is an even integer or a non-integer, returns +∞ and raises FE_DIVBYZERO<br />
* pow(±0, -∞) returns +∞ and may raise FE_DIVBYZERO<br />
* pow(+0, exp), where exp is a positive odd integer, returns +0<br />
* pow(-0, exp), where exp is a positive odd integer, returns -0<br />
* pow(±0, exp), where exp is positive non-integer or a positive even integer, returns +0<br />
* pow(-1, ±∞) returns 1<br />
* pow(+1, exp) returns 1 for any exp, even when exp is NaN<br />
* pow(base, ±0) returns 1 for any base, even when base is NaN<br />
* pow(base, exp) returns NaN and raises FE_INVALID if base is finite and negative and exp is finite and non-integer.<br />
* pow(base, -∞) returns +∞ for any |base|&lt;1<br />
* pow(base, -∞) returns +0 for any |base|&gt;1<br />
* pow(base, +∞) returns +0 for any |base|&lt;1<br />
* pow(base, +∞) returns +∞ for any |base|&gt;1<br />
* pow(-∞, exp) returns -0 if exp is a negative odd integer<br />
* pow(-∞, exp) returns +0 if exp is a negative non-integer or even integer<br />
* pow(-∞, exp) returns -∞ if exp is a positive odd integer<br />
* pow(-∞, exp) returns +∞ if exp is a positive non-integer or even integer<br />
* pow(+∞, exp) returns +0 for any negative exp<br />
* pow(+∞, exp) returns +∞ for any positive exp<br />
* except where specified above, if any argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>pow(float, int) returns float until C++11 (per overload 4) but returns double since C++11 (per overload 7)<br />
Although std::pow cannot be used to obtain a root of a negative number, std::cbrt is provided for the common case where exp is 1/3 </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cfenv&gt;

#include &lt;cstring&gt;
#pragma STDC FENV_ACCESS ON

int main()

{
    // typical usage
    std::cout &lt;&lt; &quot;pow(2, 10) = &quot; &lt;&lt; std::pow(2, 10) &lt;&lt; '
'
              &lt;&lt; &quot;pow(2, 0.5) = &quot; &lt;&lt; std::pow(2, 0.5) &lt;&lt; '
'
              &lt;&lt; &quot;pow(-2, -3) = &quot; &lt;&lt; std::pow(-2, -3) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;pow(-1, NAN) = &quot; &lt;&lt; std::pow(-1, NAN) &lt;&lt; '
'
              &lt;&lt; &quot;pow(+1, NAN) = &quot; &lt;&lt; std::pow(+1, NAN) &lt;&lt; '
'
              &lt;&lt; &quot;pow(INFINITY, 2) = &quot; &lt;&lt; std::pow(INFINITY, 2) &lt;&lt; '
'
              &lt;&lt; &quot;pow(INFINITY, -1) = &quot; &lt;&lt; std::pow(INFINITY, -1) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;pow(-1, 1/3) = &quot; &lt;&lt; std::pow(-1, 1.0 / 3) &lt;&lt; '
';
    if (errno == EDOM)
        std::cout &lt;&lt; &quot;    errno == EDOM &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;pow(-0, -3) = &quot; &lt;&lt; std::pow(-0.0, -3) &lt;&lt; '
';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout &lt;&lt; &quot;    FE_DIVBYZERO raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;pow(2, 10) = 1024<br />
&nbsp;<wbr>&nbsp;pow(2, 0.5) = 1.41421<br />
&nbsp;<wbr>&nbsp;pow(-2, -3) = -0.125<br />
&nbsp;<wbr>&nbsp;pow(-1, NAN) = nan<br />
&nbsp;<wbr>&nbsp;pow(+1, NAN) = 1<br />
&nbsp;<wbr>&nbsp;pow(INFINITY, 2) = inf<br />
&nbsp;<wbr>&nbsp;pow(INFINITY, -1) = 0<br />
&nbsp;<wbr>&nbsp;pow(-1, 1/3) = -nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == EDOM Numerical argument out of domain<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised<br />
&nbsp;<wbr>&nbsp;pow(-0, -3) = -inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_DIVBYZERO raised</p>
<h2>See also</h2>
<p>sqrt<br />
sqrtf computes square root (<br />
sqrtl √<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
cbrt computes cubic root (<br />
cbrtf 3<br />
cbrtl √<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x)<br />
<i>(C++11)</i> <i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
hypot computes square root of the sum of the squares of two given numbers (<br />
hypotf √<br />
hypotl x2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+y2<br />
<i>(C++11)</i> )<br />
<i>(C++11)</i> <i>(function)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex power, one or both arguments may be a complex number<br />
pow(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::pow to two valarrays or a valarray and a value<br />
pow(std::valarray) <i>(function template)</i> </p>
