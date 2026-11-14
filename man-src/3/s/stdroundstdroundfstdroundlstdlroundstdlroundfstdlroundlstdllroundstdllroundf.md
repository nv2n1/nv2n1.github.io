---
title: "stdroundstdroundfstdroundlstdlroundstdlroundfstdlroundlstdllroundstdllroundf(3)"
name: "stdroundstdroundfstdroundlstdlroundstdlroundfstdlroundlstdllroundstdllroundf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdroundstdroundfstdroundlstdlroundstdlroundfstdlroundlstdllroundstdllroundf/"
description: "std::round,std::roundf,std::roundl,std::lround,std::lroundf,std::lroundl,std::llround,std::llroundf – std::round,std::roundf,std::roundl,std::lround,std::lroundf,std::lroundl,std::llround,std::llro..."
---

<p>std::round,std::roundf,std::roundl,std::lround,std::lroundf,std::lroundl,std::llround,std::llroundf &#8211; std::round,std::roundf,std::roundl,std::lround,std::lroundf,std::lroundl,std::llround,std::llroundf</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float round ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float roundf( float arg );<br />
double round ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double round ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double roundl( long double arg );<br />
double round ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
long lround ( float arg ); <code>(5)</code> <i>(since C++11)</i><br />
long lroundf( float arg );<br />
long lround ( double arg ); <code>(6)</code> <i>(since C++11)</i><br />
long lround ( long double arg ); <code>(7)</code> <i>(since C++11)</i><br />
long lroundl( long double arg );<br />
long lround ( IntegralType arg ); <code>(8)</code> <i>(since C++11)</i><br />
long long llround ( float arg ); <code>(9)</code> <i>(since C++11)</i><br />
long long llroundf( float arg );<br />
long long llround ( double arg ); <code>(10)</code> <i>(since C++11)</i><br />
long long llround ( long double arg ); <code>(11)</code> <i>(since C++11)</i><br />
long long llroundl( long double arg );<br />
long long llround ( IntegralType arg ); <code>(12)</code> <i>(since C++11)</i><br />
1-3) Computes the nearest integer value to arg (in floating-point format), rounding halfway cases away from zero, regardless of the current rounding mode.<br />
5-7, 9-11) Computes the nearest integer value to arg (in integer format), rounding halfway cases away from zero, regardless of the current rounding mode.<br />
4,8,12) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2), 6), or 10), respectively (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>If no errors occur, the nearest integer value to arg, rounding halfway cases away from zero, is returned.</p>
<h2>Return value</h2>
<p>&nbsp;math-round away zero.svg<br />
Argument<br />
If a domain error occurs, an implementation-defined value is returned </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the result of std::lround or std::llround is outside the range representable by the return type, a domain error or a range error may occur.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;For the std::round function: </p>
<p>* The current rounding_mode has no effect.<br />
* If arg is ±∞, it is returned, unmodified<br />
* If arg is ±0, it is returned, unmodified<br />
* If arg is NaN, NaN is returned </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;For std::lround and std::llround functions: </p>
<p>* FE_INEXACT is never raised<br />
* The current rounding_mode has no effect.<br />
* If arg is ±∞, FE_INVALID is raised and an implementation-defined value is returned<br />
* If the result of the rounding is outside the range of the return type, FE_INVALID is raised and an implementation-defined value is returned<br />
* If arg is NaN, FE_INVALID is raised and an implementation-defined value is returned</p>
<h2>Notes</h2>
<p>FE_INEXACT may be (but isn&#8217;t required to be) raised by std::round when rounding a non-integer finite value.<br />
The largest representable floating-point values are exact integers in all standard floating-point formats, so std::round never overflows on its own; however the result may overflow any integer type (including std::intmax_t), when stored in an integer variable.<br />
POSIX_specifies that all cases where std::lround or std::llround raise FE_INEXACT are domain errors.<br />
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
&nbsp;<wbr>&nbsp;#pragma STDC FENV_ACCESS ON </p>
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
<p>&nbsp;<wbr>&nbsp;round(+2.3) = 2 round(+2.5) = 3 round(+2.7) = 3<br />
&nbsp;<wbr>&nbsp;round(-2.3) = -2 round(-2.5) = -3 round(-2.7) = -3<br />
&nbsp;<wbr>&nbsp;round(-0.0) = -0<br />
&nbsp;<wbr>&nbsp;round(-Inf) = -inf<br />
&nbsp;<wbr>&nbsp;lround(+2.3) = 2 lround(+2.5) = 3 lround(+2.7) = 3<br />
&nbsp;<wbr>&nbsp;lround(-2.3) = -2 lround(-2.5) = -3 lround(-2.7) = -3<br />
&nbsp;<wbr>&nbsp;lround(-0.0) = 0<br />
&nbsp;<wbr>&nbsp;lround(-Inf) = -9223372036854775808<br />
&nbsp;<wbr>&nbsp;std::lround(LONG_MAX+1.5) = -9223372036854775808<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID was raised</p>
<h2>See also</h2>
<p>floor<br />
floorf<br />
floorl nearest integer not greater than the given value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
ceil<br />
ceilf<br />
ceill nearest integer not less than the given value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
trunc<br />
truncf<br />
truncl nearest integer not greater in magnitude than the given value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
