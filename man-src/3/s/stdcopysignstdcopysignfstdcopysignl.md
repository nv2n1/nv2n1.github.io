---
title: "stdcopysignstdcopysignfstdcopysignl(3)"
name: "stdcopysignstdcopysignfstdcopysignl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcopysignstdcopysignfstdcopysignl/"
description: "std::copysign,std::copysignf,std::copysignl – std::copysign,std::copysignf,std::copysignl"
---

<p>std::copysign,std::copysignf,std::copysignl &#8211; std::copysign,std::copysignf,std::copysignl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float copysign ( float x, float y ); <code>(1)</code> <i>(since C++11)</i><br />
float copysignf( float x, float y );<br />
double copysign ( double x, double y ); <code>(2)</code> <i>(since C++11)</i><br />
long double copysign ( long double x, long double y ); <code>(3)</code> <i>(since C++11)</i><br />
long double copysignl( long double x, long double y );<br />
Promoted copysign ( Arithmetic1 x, Arithmetic2 y ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Composes a floating point value with the magnitude of x and the sign of y.<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by (1-3). If any argument has integral_type, it is cast to double. If any argument is long double, then the return type Promoted is also long double, otherwise the return type is always double. </p>
<h2>Parameters</h2>
<p>x, y &#8211; floating point values</p>
<h2>Return value</h2>
<p>If no errors occur, the floating point value with the magnitude of x and the sign of y is returned.<br />
If x is NaN, then NaN with the sign of y is returned.<br />
If y is -0, the result is only negative if the implementation supports the signed zero consistently in arithmetic operations. </p>
<h2>Error handling</h2>
<p>This function is not subject to any errors specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* The returned value is exact (FE_INEXACT is never raised) and independent of the current rounding_mode.</p>
<h2>Notes</h2>
<p>std::copysign is the only portable way to manipulate the sign of a NaN value (to examine the sign of a NaN, signbit may also be used) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;
int main(void)

{
    std::cout &lt;&lt; &quot;copysign(1.0,+2.0) = &quot; &lt;&lt; std::copysign(1.0, +2.0) &lt;&lt; '
'
              &lt;&lt; &quot;copysign(1.0,-2.0) = &quot; &lt;&lt; std::copysign(1.0, -2.0) &lt;&lt; '
'
              &lt;&lt; &quot;copysign(inf,-2.0) = &quot; &lt;&lt; std::copysign(INFINITY, -2.0) &lt;&lt; '
'
              &lt;&lt; &quot;copysign(NaN,-2.0) = &quot; &lt;&lt; std::copysign(NAN, -2.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;copysign(1.0,+2.0) = 1<br />
&nbsp;<wbr>&nbsp;copysign(1.0,-2.0) = -1<br />
&nbsp;<wbr>&nbsp;copysign(inf,-2.0) = -inf<br />
&nbsp;<wbr>&nbsp;copysign(NaN,-2.0) = -nan</p>
<h2>See also</h2>
<p>abs(float)<br />
fabs<br />
fabsf<br />
fabsl absolute value of a floating point value (|x|)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
signbit checks if the given number is negative<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
