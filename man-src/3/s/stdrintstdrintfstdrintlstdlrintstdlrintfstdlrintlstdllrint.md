---
title: "stdrintstdrintfstdrintlstdlrintstdlrintfstdlrintlstdllrint(3)"
name: "stdrintstdrintfstdrintlstdlrintstdlrintfstdlrintlstdllrint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrintstdrintfstdrintlstdlrintstdlrintfstdlrintlstdllrint/"
description: "std::rint,std::rintf,std::rintl,std::lrint,std::lrintf,std::lrintl,std::llrint, – std::rint,std::rintf,std::rintl,std::lrint,std::lrintf,std::lrintl,std::llrint,"
---

<p>std::rint,std::rintf,std::rintl,std::lrint,std::lrintf,std::lrintl,std::llrint, &#8211; std::rint,std::rintf,std::rintl,std::lrint,std::lrintf,std::lrintl,std::llrint,</p>
<h2>Synopsis</h2>
<p>Defined in header&nbsp;<wbr>&lt;cmath&gt;<br />
float rint&nbsp;<wbr>(&nbsp;<wbr>float arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(1)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
float rintf(&nbsp;<wbr>float arg&nbsp;<wbr>);<br />
double rint&nbsp;<wbr>(&nbsp;<wbr>double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long double rint&nbsp;<wbr>(&nbsp;<wbr>long double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr><code>(3)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long double rintl(&nbsp;<wbr>long double arg&nbsp;<wbr>);<br />
double rint&nbsp;<wbr>(&nbsp;<wbr>IntegralType arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(4)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long lrint&nbsp;<wbr>(&nbsp;<wbr>float arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(5)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long lrintf(&nbsp;<wbr>float arg&nbsp;<wbr>);<br />
long lrint&nbsp;<wbr>(&nbsp;<wbr>double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(6)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long lrint&nbsp;<wbr>(&nbsp;<wbr>long double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(7)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long lrintl(&nbsp;<wbr>long double arg&nbsp;<wbr>);<br />
long lrint&nbsp;<wbr>(&nbsp;<wbr>IntegralType arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(8)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long long llrint&nbsp;<wbr>(&nbsp;<wbr>float arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(9)</code>&nbsp;<wbr>&nbsp;<wbr><i>(since C++11)</i><br />
long long llrintf(&nbsp;<wbr>float arg&nbsp;<wbr>);<br />
long long llrint&nbsp;<wbr>(&nbsp;<wbr>double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(10)</code>&nbsp;<wbr><i>(since C++11)</i><br />
long long llrint&nbsp;<wbr>(&nbsp;<wbr>long double arg&nbsp;<wbr>);&nbsp;<wbr>&nbsp;<wbr><code>(11)</code>&nbsp;<wbr><i>(since C++11)</i><br />
long long llrintl(&nbsp;<wbr>long double arg&nbsp;<wbr>);<br />
long long llrint&nbsp;<wbr>(&nbsp;<wbr>IntegralType arg&nbsp;<wbr>);&nbsp;<wbr><code>(12)</code>&nbsp;<wbr><i>(since C++11)</i><br />
1-3)&nbsp;<wbr>Rounds the floating-point argument arg to an integer value&nbsp;<wbr>(in floating-point<br />
format), using the current rounding mode.<br />
5-7, 9-11)&nbsp;<wbr>Rounds the floating-point argument arg to an integer value, using the<br />
current rounding mode.<br />
4,8,12)&nbsp;<wbr>A set of overloads or a function template accepting an argument of any<br />
integral type. Equivalent to&nbsp;<wbr>(2,6,10), respectively&nbsp;<wbr>(the argument is cast to<br />
double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>If no errors occur, the nearest integer value to arg, according to the current<br />
rounding mode, is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling. </p>
<p>If the result of std::lrint or std::llrint is outside the range representable by the<br />
return type, a domain error or a range error may occur. </p>
<p>If the implementation supports IEEE floating-point arithmetic&nbsp;<wbr>(IEC 60559), </p>
<p>For the std::rint function: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is&nbsp;<wbr>±∞, it is returned, unmodified<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is&nbsp;<wbr>±0, it is returned, unmodified<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is NaN, NaN is returned </p>
<p>For std::lrint and std::llrint functions: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is&nbsp;<wbr>±∞, FE_INVALID is raised and an implementation-defined value is<br />
&nbsp;<wbr>returned<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If the result of the rounding is outside the range of the return type,<br />
&nbsp;<wbr>FE_INVALID is raised and an implementation-defined value is returned<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If arg is NaN, FE_INVALID is raised and an implementation-defined value is<br />
&nbsp;<wbr>returned</p>
<h2>Notes</h2>
<p>POSIX specifies that all cases where std::lrint or std::llrint raise FE_INEXACT are<br />
domain errors.<br />
As specified in math_errhandling, FE_INEXACT may be&nbsp;<wbr>(but isn&#8217;t required to be on<br />
non-IEEE floating-point platforms)&nbsp;<wbr>raised by std::rint when rounding a non-integer<br />
finite value.<br />
The only difference between std::rint and std::nearbyint is that std::nearbyint<br />
never raises FE_INEXACT.<br />
The largest representable floating-point values are exact integers in all standard<br />
floating-point formats, so std::rint never overflows on its own;&nbsp;<wbr>however the result<br />
may overflow any integer type&nbsp;<wbr>(including std::intmax_t), when stored in an integer<br />
variable.<br />
If the current rounding mode is&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>FE_DOWNWARD, then std::rint is equivalent to std::floor.<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>FE_UPWARD, then std::rint is equivalent to std::ceil.<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>FE_TOWARDZERO, then std::rint is equivalent to std::trunc<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>FE_TONEAREST, then std::rint differs from std::round in that halfway cases are<br />
&nbsp;<wbr>rounded to even rather than away from zero. </p>
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
<p>&nbsp;<wbr>rounding to nearest&nbsp;<wbr>(halfway cases to even):<br />
&nbsp;<wbr>rint(+2.3)&nbsp;<wbr>=&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>rint(+2.5)&nbsp;<wbr>=&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>rint(+3.5)&nbsp;<wbr>=&nbsp;<wbr>4<br />
&nbsp;<wbr>rint(-2.3)&nbsp;<wbr>=&nbsp;<wbr>-2&nbsp;<wbr>&nbsp;<wbr>rint(-2.5)&nbsp;<wbr>=&nbsp;<wbr>-2&nbsp;<wbr>&nbsp;<wbr>rint(-3.5)&nbsp;<wbr>=&nbsp;<wbr>-4<br />
&nbsp;<wbr>rounding down:<br />
&nbsp;<wbr>rint(+2.3)&nbsp;<wbr>=&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>rint(+2.5)&nbsp;<wbr>=&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>rint(+3.5)&nbsp;<wbr>=&nbsp;<wbr>3<br />
&nbsp;<wbr>rint(-2.3)&nbsp;<wbr>=&nbsp;<wbr>-3&nbsp;<wbr>&nbsp;<wbr>rint(-2.5)&nbsp;<wbr>=&nbsp;<wbr>-3&nbsp;<wbr>&nbsp;<wbr>rint(-3.5)&nbsp;<wbr>=&nbsp;<wbr>-4<br />
&nbsp;<wbr>rounding down with lrint<br />
&nbsp;<wbr>lrint(+2.3)&nbsp;<wbr>=&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>lrint(+2.5)&nbsp;<wbr>=&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>lrint(+3.5)&nbsp;<wbr>=&nbsp;<wbr>3<br />
&nbsp;<wbr>lrint(-2.3)&nbsp;<wbr>=&nbsp;<wbr>-3&nbsp;<wbr>&nbsp;<wbr>lrint(-2.5)&nbsp;<wbr>=&nbsp;<wbr>-3&nbsp;<wbr>&nbsp;<wbr>lrint(-3.5)&nbsp;<wbr>=&nbsp;<wbr>-4<br />
&nbsp;<wbr>lrint(-0.0)&nbsp;<wbr>=&nbsp;<wbr>0<br />
&nbsp;<wbr>lrint(-Inf)&nbsp;<wbr>=&nbsp;<wbr>-9223372036854775808<br />
&nbsp;<wbr>std::rint(0.1)&nbsp;<wbr>=&nbsp;<wbr>0<br />
&nbsp;<wbr>&nbsp;<wbr>FE_INEXACT was raised<br />
&nbsp;<wbr>std::lrint(LONG_MIN-2048.0)&nbsp;<wbr>=&nbsp;<wbr>-9223372036854775808<br />
&nbsp;<wbr>&nbsp;<wbr>FE_INVALID was raised</p>
<h2>See also</h2>
<p>trunc<br />
truncf<br />
truncl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nearest integer not greater in magnitude than the given value<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
nearbyint<br />
nearbyintf<br />
nearbyintl nearest integer using current rounding mode<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
fegetround<br />
fesetround gets or sets rounding direction<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function)</i><br />
<i>(C++11)</i> </p>
