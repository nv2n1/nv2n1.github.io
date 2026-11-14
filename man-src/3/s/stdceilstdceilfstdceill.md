---
title: "stdceilstdceilfstdceill(3)"
name: "stdceilstdceilfstdceill"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdceilstdceilfstdceill/"
description: "std::ceil,std::ceilf,std::ceill – std::ceil,std::ceilf,std::ceill"
---

<p>std::ceil,std::ceilf,std::ceill &#8211; std::ceil,std::ceilf,std::ceill</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float ceil ( float arg );<br />
float ceilf( float arg ); <i>(since C++11)</i><br />
double ceil ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double ceil ( long double arg );<br />
long double ceill( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double ceil ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the smallest integer value not less than arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>If no errors occur, the smallest integer value not less than arg, that is ⌈arg⌉, is returned.</p>
<h2>Return value</h2>
<p>&nbsp;math-ceil.svg<br />
Argument </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* The current rounding_mode has no effect.<br />
* If arg is ±∞, it is returned unmodified<br />
* If arg is ±0, it is returned, unmodified<br />
* If arg is NaN, NaN is returned</p>
<h2>Notes</h2>
<pre><code>FE_INEXACT may be (but isn't required to be) raised when rounding a non-integer finite value.

The largest representable floating-point values are exact integers in all standard floating-point formats, so this function never overflows on its own; however the result may overflow any integer type (including std::intmax_t), when stored in an integer variable.

This function (for double argument) behaves as if (except for the freedom to not raise FE_INEXACT) implemented by the following code:
#include &lt;cmath&gt;

#include &lt;cfenv&gt;

#pragma STDC FENV_ACCESS ON

  double ceil(double x)

  {
    double result;
    int save_round = std::fegetround();
    std::fesetround(FE_UPWARD);
    result = std::rint(x); // or std::nearbyint
    std::fesetround(save_round);
    return result;

  }
</code></pre>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

int main()

{
    std::cout &lt;&lt; std::fixed
              &lt;&lt; &quot;ceil(+2.4) = &quot; &lt;&lt; std::ceil(+2.4) &lt;&lt; '
'
              &lt;&lt; &quot;ceil(-2.4) = &quot; &lt;&lt; std::ceil(-2.4) &lt;&lt; '
'
              &lt;&lt; &quot;ceil(-0.0) = &quot; &lt;&lt; std::ceil(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;ceil(-Inf) = &quot; &lt;&lt; std::ceil(-INFINITY) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;ceil(+2.4) = 3.000000<br />
&nbsp;<wbr>&nbsp;ceil(-2.4) = -2.000000<br />
&nbsp;<wbr>&nbsp;ceil(-0.0) = -0.000000<br />
&nbsp;<wbr>&nbsp;ceil(-Inf) = -INF</p>
<h2>See also</h2>
<p>floor<br />
floorf<br />
floorl nearest integer not greater than the given value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
trunc<br />
truncf<br />
truncl nearest integer not greater in magnitude than the given value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
round<br />
roundf<br />
roundl<br />
lround<br />
lroundf<br />
lroundl<br />
llround<br />
llroundf<br />
llroundl nearest integer, rounding away from zero in halfway cases<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
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
rint<br />
rintf<br />
rintl<br />
lrint<br />
lrintf<br />
lrintl<br />
llrint<br />
llrintf nearest integer using current rounding mode with<br />
llrintl exception if the result differs<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
