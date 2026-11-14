---
title: "stdcbrtstdcbrtfstdcbrtl(3)"
name: "stdcbrtstdcbrtfstdcbrtl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcbrtstdcbrtfstdcbrtl/"
description: "std::cbrt,std::cbrtf,std::cbrtl – std::cbrt,std::cbrtf,std::cbrtl"
---

<p>std::cbrt,std::cbrtf,std::cbrtl &#8211; std::cbrt,std::cbrtf,std::cbrtl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float cbrt ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float cbrtf( float arg );<br />
double cbrt ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double cbrt ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double cbrtl( long double arg );<br />
double cbrt ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the cubic root of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the cubic root of arg (<br />
3<br />
√<br />
arg), is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if the argument is ±0 or ±∞, it is returned, unchanged<br />
* if the argument is NaN, NaN is returned.</p>
<h2>Notes</h2>
<p>std::cbrt(arg) is not equivalent to std::pow(arg, 1.0/3) because std::pow cannot raise a negative base to a fractional exponent. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;
int main()

{
    // normal use
    std::cout &lt;&lt; &quot;cbrt(729) = &quot; &lt;&lt; std::cbrt(729) &lt;&lt; '
'
              &lt;&lt; &quot;cbrt(-0.125) = &quot; &lt;&lt; std::cbrt(-0.125) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;cbrt(-0) = &quot; &lt;&lt; std::cbrt(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;cbrt(+inf) = &quot; &lt;&lt; std::cbrt(INFINITY) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;cbrt(729) = 9<br />
&nbsp;<wbr>&nbsp;cbrt(-0.125) = -0.5<br />
&nbsp;<wbr>&nbsp;cbrt(-0) = -0<br />
&nbsp;<wbr>&nbsp;cbrt(+inf) = inf</p>
<h2>See also</h2>
<p>pow<br />
powf<br />
powl raises a number to the given power (xy)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
sqrt<br />
sqrtf computes square root (<br />
sqrtl √<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
hypot computes square root of the sum of the squares of two given numbers (<br />
hypotf √<br />
hypotl x2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+y2<br />
<i>(C++11)</i> )<br />
<i>(C++11)</i> <i>(function)</i><br />
<i>(C++11)</i> </p>
