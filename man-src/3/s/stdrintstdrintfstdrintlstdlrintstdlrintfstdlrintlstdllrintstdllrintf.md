---
title: "stdrintstdrintfstdrintlstdlrintstdlrintfstdlrintlstdllrintstdllrintf(3)"
name: "stdrintstdrintfstdrintlstdlrintstdlrintfstdlrintlstdllrintstdllrintf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrintstdrintfstdrintlstdlrintstdlrintfstdlrintlstdllrintstdllrintf/"
description: "std::rint,std::rintf,std::rintl,std::lrint,std::lrintf,std::lrintl,std::llrint,std::llrintf – std::rint,std::rintf,std::rintl,std::lrint,std::lrintf,std::lrintl,std::llrint,std::llrintf"
---

<p>std::rint,std::rintf,std::rintl,std::lrint,std::lrintf,std::lrintl,std::llrint,std::llrintf &#8211; std::rint,std::rintf,std::rintl,std::lrint,std::lrintf,std::lrintl,std::llrint,std::llrintf</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float rint ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float rintf( float arg );<br />
double rint ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double rint ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double rintl( long double arg );<br />
double rint ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
long lrint ( float arg ); <code>(5)</code> <i>(since C++11)</i><br />
long lrintf( float arg );<br />
long lrint ( double arg ); <code>(6)</code> <i>(since C++11)</i><br />
long lrint ( long double arg ); <code>(7)</code> <i>(since C++11)</i><br />
long lrintl( long double arg );<br />
long lrint ( IntegralType arg ); <code>(8)</code> <i>(since C++11)</i><br />
long long llrint ( float arg ); <code>(9)</code> <i>(since C++11)</i><br />
long long llrintf( float arg );<br />
long long llrint ( double arg ); <code>(10)</code> <i>(since C++11)</i><br />
long long llrint ( long double arg ); <code>(11)</code> <i>(since C++11)</i><br />
long long llrintl( long double arg );<br />
long long llrint ( IntegralType arg ); <code>(12)</code> <i>(since C++11)</i><br />
1-3) Rounds the floating-point argument arg to an integer value (in floating-point format), using the current_rounding_mode.<br />
5-7, 9-11) Rounds the floating-point argument arg to an integer value, using the current_rounding_mode.<br />
4,8,12) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to (2,6,10), respectively (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>If no errors occur, the nearest integer value to arg, according to the current_rounding_mode, is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the result of std::lrint or std::llrint is outside the range representable by the return type, a domain error or a range error may occur.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;For the std::rint function: </p>
<p>* If arg is ±∞, it is returned, unmodified<br />
* If arg is ±0, it is returned, unmodified<br />
* If arg is NaN, NaN is returned </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;For std::lrint and std::llrint functions: </p>
<p>* If arg is ±∞, FE_INVALID is raised and an implementation-defined value is returned<br />
* If the result of the rounding is outside the range of the return type, FE_INVALID is raised and an implementation-defined value is returned<br />
* If arg is NaN, FE_INVALID is raised and an implementation-defined value is returned</p>
<h2>Notes</h2>
<p>POSIX_specifies that all cases where std::lrint or std::llrint raise FE_INEXACT are domain errors.<br />
As specified in math_errhandling, FE_INEXACT may be (but isn&#8217;t required to be on non-IEEE floating-point platforms) raised by std::rint when rounding a non-integer finite value.<br />
The only difference between std::rint and std::nearbyint is that std::nearbyint never raises FE_INEXACT.<br />
The largest representable floating-point values are exact integers in all standard floating-point formats, so std::rint never overflows on its own; however the result may overflow any integer type (including std::intmax_t), when stored in an integer variable.<br />
If the current rounding mode is&#8230;<br />
* FE_DOWNWARD, then std::rint is equivalent to std::floor.<br />
* FE_UPWARD, then std::rint is equivalent to std::ceil.<br />
* FE_TOWARDZERO, then std::rint is equivalent to std::trunc<br />
* FE_TONEAREST, then std::rint differs from std::round in that halfway cases are rounded to even rather than away from zero. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfenv&gt;

#include &lt;climits&gt;
int main()

{

#pragma STDC FENV_ACCESS ON
    std::fesetround(FE_TONEAREST);
    std::cout &lt;&lt; &quot;rounding to nearest (halfway cases to even):
&quot;
              &lt;&lt; &quot;rint(+2.3) = &quot; &lt;&lt; std::rint(2.3)
              &lt;&lt; &quot;  rint(+2.5) = &quot; &lt;&lt; std::rint(2.5)
              &lt;&lt; &quot;  rint(+3.5) = &quot; &lt;&lt; std::rint(3.5) &lt;&lt; '
'
              &lt;&lt; &quot;rint(-2.3) = &quot; &lt;&lt; std::rint(-2.3)
              &lt;&lt; &quot;  rint(-2.5) = &quot; &lt;&lt; std::rint(-2.5)
              &lt;&lt; &quot;  rint(-3.5) = &quot; &lt;&lt; std::rint(-3.5) &lt;&lt; '
';
    std::fesetround(FE_DOWNWARD);
    std::cout &lt;&lt; &quot;rounding down:
&quot;
              &lt;&lt; &quot;rint(+2.3) = &quot; &lt;&lt; std::rint(2.3)
              &lt;&lt; &quot;  rint(+2.5) = &quot; &lt;&lt; std::rint(2.5)
              &lt;&lt; &quot;  rint(+3.5) = &quot; &lt;&lt; std::rint(3.5) &lt;&lt; '
'
              &lt;&lt; &quot;rint(-2.3) = &quot; &lt;&lt; std::rint(-2.3)
              &lt;&lt; &quot;  rint(-2.5) = &quot; &lt;&lt; std::rint(-2.5)
              &lt;&lt; &quot;  rint(-3.5) = &quot; &lt;&lt; std::rint(-3.5) &lt;&lt; '
'
              &lt;&lt; &quot;rounding down with lrint
&quot;
              &lt;&lt; &quot;lrint(+2.3) = &quot; &lt;&lt; std::lrint(2.3)
              &lt;&lt; &quot;  lrint(+2.5) = &quot; &lt;&lt; std::lrint(2.5)
              &lt;&lt; &quot;  lrint(+3.5) = &quot; &lt;&lt; std::lrint(3.5) &lt;&lt; '
'
              &lt;&lt; &quot;lrint(-2.3) = &quot; &lt;&lt; std::lrint(-2.3)
              &lt;&lt; &quot;  lrint(-2.5) = &quot; &lt;&lt; std::lrint(-2.5)
              &lt;&lt; &quot;  lrint(-3.5) = &quot; &lt;&lt; std::lrint(-3.5) &lt;&lt; '
';
    std::cout &lt;&lt; &quot;lrint(-0.0) = &quot; &lt;&lt; std::lrint(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;lrint(-Inf) = &quot; &lt;&lt; std::lrint(-INFINITY) &lt;&lt; '
';
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;std::rint(0.1) = &quot; &lt;&lt; std::rint(.1) &lt;&lt; '
';
    if (std::fetestexcept(FE_INEXACT))
        std::cout &lt;&lt; &quot;    FE_INEXACT was raised
&quot;;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;std::lrint(LONG_MIN-2048.0) = &quot;
              &lt;&lt; std::lrint(LONG_MIN - 2048.0) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID was raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;rounding to nearest (halfway cases to even):<br />
&nbsp;<wbr>&nbsp;rint(+2.3) = 2 rint(+2.5) = 2 rint(+3.5) = 4<br />
&nbsp;<wbr>&nbsp;rint(-2.3) = -2 rint(-2.5) = -2 rint(-3.5) = -4<br />
&nbsp;<wbr>&nbsp;rounding down:<br />
&nbsp;<wbr>&nbsp;rint(+2.3) = 2 rint(+2.5) = 2 rint(+3.5) = 3<br />
&nbsp;<wbr>&nbsp;rint(-2.3) = -3 rint(-2.5) = -3 rint(-3.5) = -4<br />
&nbsp;<wbr>&nbsp;rounding down with lrint<br />
&nbsp;<wbr>&nbsp;lrint(+2.3) = 2 lrint(+2.5) = 2 lrint(+3.5) = 3<br />
&nbsp;<wbr>&nbsp;lrint(-2.3) = -3 lrint(-2.5) = -3 lrint(-3.5) = -4<br />
&nbsp;<wbr>&nbsp;lrint(-0.0) = 0<br />
&nbsp;<wbr>&nbsp;lrint(-Inf) = -9223372036854775808<br />
&nbsp;<wbr>&nbsp;std::rint(0.1) = 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INEXACT was raised<br />
&nbsp;<wbr>&nbsp;std::lrint(LONG_MIN-2048.0) = -9223372036854775808<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID was raised</p>
<h2>See also</h2>
<p>trunc<br />
truncf<br />
truncl nearest integer not greater in magnitude than the given value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
nearbyint<br />
nearbyintf<br />
nearbyintl nearest integer using current rounding mode<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
fegetround<br />
fesetround gets or sets rounding direction<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
