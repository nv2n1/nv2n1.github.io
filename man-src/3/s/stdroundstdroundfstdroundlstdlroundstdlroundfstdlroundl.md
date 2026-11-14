---
title: "stdroundstdroundfstdroundlstdlroundstdlroundfstdlroundl(3)"
name: "stdroundstdroundfstdroundlstdlroundstdlroundfstdlroundl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdroundstdroundfstdroundlstdlroundstdlroundfstdlroundl/"
description: "std::round,std::roundf,std::roundl,std::lround,std::lroundf,std::lroundl, – std::round,std::roundf,std::roundl,std::lround,std::lroundf,std::lroundl,"
---

<p>std::round,std::roundf,std::roundl,std::lround,std::lroundf,std::lroundl, &#8211; std::round,std::roundf,std::roundl,std::lround,std::lroundf,std::lroundl,</p>
<h2>Synopsis</h2>
<p>Defined in header&nbsp;<wbr>&lt;cmath&gt;<br />
float round&nbsp;<wbr>(&nbsp;<wbr>float arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(1)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
float roundf(&nbsp;<wbr>float arg&nbsp;<wbr>);<br />
double round&nbsp;<wbr>(&nbsp;<wbr>double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long double round&nbsp;<wbr>(&nbsp;<wbr>long double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr><code>(3)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long double roundl(&nbsp;<wbr>long double arg&nbsp;<wbr>);<br />
double round&nbsp;<wbr>(&nbsp;<wbr>IntegralType arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(4)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long lround&nbsp;<wbr>(&nbsp;<wbr>float arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(5)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long lroundf(&nbsp;<wbr>float arg&nbsp;<wbr>);<br />
long lround&nbsp;<wbr>(&nbsp;<wbr>double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(6)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long lround&nbsp;<wbr>(&nbsp;<wbr>long double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(7)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long lroundl(&nbsp;<wbr>long double arg&nbsp;<wbr>);<br />
long lround&nbsp;<wbr>(&nbsp;<wbr>IntegralType arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(8)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long long llround&nbsp;<wbr>(&nbsp;<wbr>float arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(9)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long long llroundf(&nbsp;<wbr>float arg&nbsp;<wbr>);<br />
long long llround&nbsp;<wbr>(&nbsp;<wbr>double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(10)</code>&nbsp;<wbr><i>(since C++11)</i><br />
long long llround&nbsp;<wbr>(&nbsp;<wbr>long double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr><code>(11)</code>&nbsp;<wbr><i>(since C++11)</i><br />
long long llroundl(&nbsp;<wbr>long double arg&nbsp;<wbr>);<br />
long long llround&nbsp;<wbr>(&nbsp;<wbr>IntegralType arg&nbsp;<wbr>);&nbsp;<wbr><code>(12)</code>&nbsp;<wbr><i>(since C++11)</i><br />
1-3)&nbsp;<wbr>Computes the nearest integer value to arg&nbsp;<wbr>(in floating-point format), rounding<br />
halfway cases away from zero, regardless of the current rounding mode.<br />
5-7, 9-11)&nbsp;<wbr>Computes the nearest integer value to arg&nbsp;<wbr>(in integer format), rounding<br />
halfway cases away from zero, regardless of the current rounding mode.<br />
4,8,12)&nbsp;<wbr>A set of overloads or a function template accepting an argument of any<br />
integral type. Equivalent to 2), 6), or 10), respectively&nbsp;<wbr>(the argument is cast to<br />
double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>If no errors occur, the nearest integer value to arg, rounding halfway cases away<br />
from zero, is returned. </p>
<h2>Return value</h2>
<p>math-round away zero.svg<br />
Argument<br />
If a domain error occurs, an implementation-defined value is returned </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling. </p>
<p>If the result of std::lround or std::llround is outside the range representable by<br />
the return type, a domain error or a range error may occur. </p>
<p>If the implementation supports IEEE floating-point arithmetic&nbsp;<wbr>(IEC 60559), </p>
<p>For the std::round function: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>The current rounding mode has no effect.<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is&nbsp;<wbr>±∞, it is returned, unmodified<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is&nbsp;<wbr>±0, it is returned, unmodified<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is NaN, NaN is returned </p>
<p>For std::lround and std::llround functions: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>FE_INEXACT is never raised<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>The current rounding mode has no effect.<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is&nbsp;<wbr>±∞, FE_INVALID is raised and an implementation-defined value is<br />
&nbsp;<wbr>returned<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If the result of the rounding is outside the range of the return type,<br />
&nbsp;<wbr>FE_INVALID is raised and an implementation-defined value is returned<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is NaN, FE_INVALID is raised and an implementation-defined value is<br />
&nbsp;<wbr>returned</p>
<h2>Notes</h2>
<p>FE_INEXACT may be&nbsp;<wbr>(but isn&#8217;t required to be)&nbsp;<wbr>raised by std::round when rounding a<br />
non-integer finite value.<br />
The largest representable floating-point values are exact integers in all standard<br />
floating-point formats, so std::round never overflows on its own;&nbsp;<wbr>however the result<br />
may overflow any integer type&nbsp;<wbr>(including std::intmax_t), when stored in an integer<br />
variable.<br />
POSIX specifies that all cases where std::lround or std::llround raise FE_INEXACT<br />
are domain errors.<br />
The double version of std::round behaves as if implemented as follows: </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;cfenv&gt;

#pragma STDC FENV_ACCESS ON

double round(double x)

{
    std::fenv_t save_env;
    std::feholdexcept(&amp;save_env);
    double result = std::rint(x);
    if (std::fetestexcept(FE_INEXACT)) {

        auto const save_round = std::fegetround();

        std::fesetround(FE_TOWARDZERO);

        result = std::rint(std::copysign(0.5 + std::fabs(x), x));

        std::fesetround(save_round);
    }
    std::feupdateenv(&amp;save_env);
    return result;
}
</code></pre>
<h2>Example</h2>
<p>// Run this code #include &lt;iostream&gt;</p>
<p>#include &lt;cmath&gt;</p>
<p>#include &lt;cfenv&gt;</p>
<p>#include &lt;climits&gt;<br />
&nbsp;<wbr>#pragma STDC FENV_ACCESS ON </p>
<pre><code>int main()

{
    // round
    std::cout &lt;&lt; &quot;round(+2.3) = &quot; &lt;&lt; std::round(2.3)
              &lt;&lt; &quot;  round(+2.5) = &quot; &lt;&lt; std::round(2.5)
              &lt;&lt; &quot;  round(+2.7) = &quot; &lt;&lt; std::round(2.7) &lt;&lt; '
'
              &lt;&lt; &quot;round(-2.3) = &quot; &lt;&lt; std::round(-2.3)
              &lt;&lt; &quot;  round(-2.5) = &quot; &lt;&lt; std::round(-2.5)
              &lt;&lt; &quot;  round(-2.7) = &quot; &lt;&lt; std::round(-2.7) &lt;&lt; '
';
    std::cout &lt;&lt; &quot;round(-0.0) = &quot; &lt;&lt; std::round(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;round(-Inf) = &quot; &lt;&lt; std::round(-INFINITY) &lt;&lt; '
';
    // lround
    std::cout &lt;&lt; &quot;lround(+2.3) = &quot; &lt;&lt; std::lround(2.3)
              &lt;&lt; &quot;  lround(+2.5) = &quot; &lt;&lt; std::lround(2.5)
              &lt;&lt; &quot;  lround(+2.7) = &quot; &lt;&lt; std::lround(2.7) &lt;&lt; '
'
              &lt;&lt; &quot;lround(-2.3) = &quot; &lt;&lt; std::lround(-2.3)
              &lt;&lt; &quot;  lround(-2.5) = &quot; &lt;&lt; std::lround(-2.5)
              &lt;&lt; &quot;  lround(-2.7) = &quot; &lt;&lt; std::lround(-2.7) &lt;&lt; '
';
    std::cout &lt;&lt; &quot;lround(-0.0) = &quot; &lt;&lt; std::lround(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;lround(-Inf) = &quot; &lt;&lt; std::lround(-INFINITY) &lt;&lt; '
';
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;std::lround(LONG_MAX+1.5) = &quot;
              &lt;&lt; std::lround(LONG_MAX + 1.5) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID was raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>round(+2.3)&nbsp;<wbr>=&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>round(+2.5)&nbsp;<wbr>=&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>round(+2.7)&nbsp;<wbr>=&nbsp;<wbr>3<br />
&nbsp;<wbr>round(-2.3)&nbsp;<wbr>=&nbsp;<wbr>-2&nbsp;<wbr>&nbsp;<wbr>round(-2.5)&nbsp;<wbr>=&nbsp;<wbr>-3&nbsp;<wbr>&nbsp;<wbr>round(-2.7)&nbsp;<wbr>=&nbsp;<wbr>-3<br />
&nbsp;<wbr>round(-0.0)&nbsp;<wbr>=&nbsp;<wbr>-0<br />
&nbsp;<wbr>round(-Inf)&nbsp;<wbr>=&nbsp;<wbr>-inf<br />
&nbsp;<wbr>lround(+2.3)&nbsp;<wbr>=&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>lround(+2.5)&nbsp;<wbr>=&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>lround(+2.7)&nbsp;<wbr>=&nbsp;<wbr>3<br />
&nbsp;<wbr>lround(-2.3)&nbsp;<wbr>=&nbsp;<wbr>-2&nbsp;<wbr>&nbsp;<wbr>lround(-2.5)&nbsp;<wbr>=&nbsp;<wbr>-3&nbsp;<wbr>&nbsp;<wbr>lround(-2.7)&nbsp;<wbr>=&nbsp;<wbr>-3<br />
&nbsp;<wbr>lround(-0.0)&nbsp;<wbr>=&nbsp;<wbr>0<br />
&nbsp;<wbr>lround(-Inf)&nbsp;<wbr>=&nbsp;<wbr>-9223372036854775808<br />
&nbsp;<wbr>std::lround(LONG_MAX+1.5)&nbsp;<wbr>=&nbsp;<wbr>-9223372036854775808<br />
&nbsp;<wbr>&nbsp;<wbr>FE_INVALID was raised</p>
<h2>See also</h2>
<p>floor<br />
floorf&nbsp;<wbr>&nbsp;<wbr>nearest integer not greater than the given value<br />
floorl&nbsp;<wbr>&nbsp;<wbr><i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
ceil<br />
ceilf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nearest integer not less than the given value<br />
ceill&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
trunc<br />
truncf<br />
truncl&nbsp;<wbr>&nbsp;<wbr>nearest integer not greater in magnitude than the given value<br />
<i>(C++11)</i>&nbsp;<wbr><i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
