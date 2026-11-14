---
title: "stdnearbyintstdnearbyintfstdnearbyintl(3)"
name: "stdnearbyintstdnearbyintfstdnearbyintl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnearbyintstdnearbyintfstdnearbyintl/"
description: "std::nearbyint,std::nearbyintf,std::nearbyintl – std::nearbyint,std::nearbyintf,std::nearbyintl"
---

<p>std::nearbyint,std::nearbyintf,std::nearbyintl &#8211; std::nearbyint,std::nearbyintf,std::nearbyintl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float nearbyint ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float nearbyintf( float arg );<br />
double nearbyint ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double nearbyint ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double nearbyintl( long double arg );<br />
double nearbyint ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Rounds the floating-point argument arg to an integer value in floating-point format, using the current_rounding_mode.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>The nearest integer value to arg, according to the current_rounding_mode, is returned. </p>
<h2>Error handling</h2>
<p>This function is not subject to any of the errors specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* FE_INEXACT is never raised<br />
* If arg is ±∞, it is returned, unmodified<br />
* If arg is ±0, it is returned, unmodified<br />
* If arg is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>The only difference between std::nearbyint and std::rint is that std::nearbyint never raises FE_INEXACT.<br />
The largest representable floating-point values are exact integers in all standard floating-point formats, so std::nearbyint never overflows on its own; however the result may overflow any integer type (including std::intmax_t), when stored in an integer variable.<br />
If the current rounding mode is FE_TONEAREST, this function rounds to even in halfway cases (like rint, but unlike round). </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfenv&gt;
int main()

{

#pragma STDC FENV_ACCESS ON
    std::fesetround(FE_TONEAREST);
    std::cout &lt;&lt; &quot;rounding to nearest: 
&quot;
              &lt;&lt; &quot;nearbyint(+2.3) = &quot; &lt;&lt; std::nearbyint(2.3)
              &lt;&lt; &quot;  nearbyint(+2.5) = &quot; &lt;&lt; std::nearbyint(2.5)
              &lt;&lt; &quot;  nearbyint(+3.5) = &quot; &lt;&lt; std::nearbyint(3.5) &lt;&lt; '
'
              &lt;&lt; &quot;nearbyint(-2.3) = &quot; &lt;&lt; std::nearbyint(-2.3)
              &lt;&lt; &quot;  nearbyint(-2.5) = &quot; &lt;&lt; std::nearbyint(-2.5)
              &lt;&lt; &quot;  nearbyint(-3.5) = &quot; &lt;&lt; std::nearbyint(-3.5) &lt;&lt; '
';
    std::fesetround(FE_DOWNWARD);
    std::cout &lt;&lt; &quot;rounding down:
&quot;
              &lt;&lt; &quot;nearbyint(+2.3) = &quot; &lt;&lt; std::nearbyint(2.3)
              &lt;&lt; &quot;  nearbyint(+2.5) = &quot; &lt;&lt; std::nearbyint(2.5)
              &lt;&lt; &quot;  nearbyint(+3.5) = &quot; &lt;&lt; std::nearbyint(3.5) &lt;&lt; '
'
              &lt;&lt; &quot;nearbyint(-2.3) = &quot; &lt;&lt; std::nearbyint(-2.3)
              &lt;&lt; &quot;  nearbyint(-2.5) = &quot; &lt;&lt; std::nearbyint(-2.5)
              &lt;&lt; &quot;  nearbyint(-3.5) = &quot; &lt;&lt; std::nearbyint(-3.5) &lt;&lt; '
';
    std::cout &lt;&lt; &quot;nearbyint(-0.0) = &quot; &lt;&lt; std::nearbyint(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;nearbyint(-Inf) = &quot; &lt;&lt; std::nearbyint(-INFINITY) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;rounding to nearest:<br />
&nbsp;<wbr>&nbsp;nearbyint(+2.3) = 2 nearbyint(+2.5) = 2 nearbyint(+3.5) = 4<br />
&nbsp;<wbr>&nbsp;nearbyint(-2.3) = -2 nearbyint(-2.5) = -2 nearbyint(-3.5) = -4<br />
&nbsp;<wbr>&nbsp;rounding down:<br />
&nbsp;<wbr>&nbsp;nearbyint(+2.3) = 2 nearbyint(+2.5) = 2 nearbyint(+3.5) = 3<br />
&nbsp;<wbr>&nbsp;nearbyint(-2.3) = -3 nearbyint(-2.5) = -3 nearbyint(-3.5) = -4<br />
&nbsp;<wbr>&nbsp;nearbyint(-0.0) = -0<br />
&nbsp;<wbr>&nbsp;nearbyint(-Inf) = -inf</p>
<h2>See also</h2>
<p>rint<br />
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
fegetround<br />
fesetround gets or sets rounding direction<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
