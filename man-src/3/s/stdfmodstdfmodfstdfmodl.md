---
title: "stdfmodstdfmodfstdfmodl(3)"
name: "stdfmodstdfmodfstdfmodl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfmodstdfmodfstdfmodl/"
description: "std::fmod,std::fmodf,std::fmodl – std::fmod,std::fmodf,std::fmodl"
---

<p>std::fmod,std::fmodf,std::fmodl &#8211; std::fmod,std::fmodf,std::fmodl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float fmod ( float x, float y );<br />
float fmodf( float x, float y ); <i>(since C++11)</i><br />
double fmod ( double x, double y ); <code>(1)</code> <code>(2)</code><br />
long double fmod ( long double x, long double y );<br />
long double fmodl( long double x, long double y ); <code>(3)</code> <i>(since C++11)</i><br />
Promoted fmod ( Arithmetic1 x, Arithmetic2 y ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the floating-point remainder of the division operation x/y.<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic_type not covered by (1-3). If any argument has integral_type, it is cast to double. If any other argument is long double, then the return type is long double, otherwise it is double.<br />
The floating-point remainder of the division operation x/y calculated by this function is exactly the value x &#8211; n*y, where n is x/y with its fractional part truncated.<br />
The returned value has the same sign as x and is less than y in magnitude. </p>
<h2>Parameters</h2>
<p>x, y &#8211; floating point values</p>
<h2>Return value</h2>
<p>If successful, returns the floating-point remainder of the division x/y as defined above.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
Domain error may occur if y is zero.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If x is ±0 and y is not zero, ±0 is returned<br />
* If x is ±∞ and y is not NaN, NaN is returned and FE_INVALID is raised<br />
* If y is ±0 and x is not NaN, NaN is returned and FE_INVALID is raised<br />
* If y is ±∞ and x is finite, x is returned.<br />
* If either argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<pre><code>POSIX_requires that a domain error occurs if x is infinite or y is zero.

std::fmod, but not std::remainder is useful for doing silent wrapping of floating-point types to unsigned integer types: (0.0 &lt;= (y = std::fmod( std::rint(x), 65536.0 )) ? y : 65536.0 + y) is in the range [-0.0 .. 65535.0], which corresponds to unsigned short, but std::remainder(std::rint(x), 65536.0 is in the range [-32767.0, +32768.0], which is outside of the range of signed short.

The double version of fmod behaves as if implemented as follows
double fmod(double x, double y)

  {

#pragma STDC FENV_ACCESS ON
    double result = std::remainder(std::fabs(x), (y = std::fabs(y)));
    if (std::signbit(result))
        result += y;
    return std::copysign(result, x);

  }</code></pre>
<p>The expression x &#8211; trunc(x/y)*y may not equal fmod(x,y) when the rounding of x/y to initialize the argument of trunc loses too much precision (example: x = 30.508474576271183309, y = 6.1016949152542370172) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfenv&gt;
#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;fmod(+5.1, +3.0) = &quot; &lt;&lt; std::fmod(5.1, 3) &lt;&lt; '
'
              &lt;&lt; &quot;fmod(-5.1, +3.0) = &quot; &lt;&lt; std::fmod(-5.1, 3) &lt;&lt; '
'
              &lt;&lt; &quot;fmod(+5.1, -3.0) = &quot; &lt;&lt; std::fmod(5.1, -3) &lt;&lt; '
'
              &lt;&lt; &quot;fmod(-5.1, -3.0) = &quot; &lt;&lt; std::fmod(-5.1, -3) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;fmod(+0.0, 1.0) = &quot; &lt;&lt; std::fmod(0, 1) &lt;&lt; '
'
              &lt;&lt; &quot;fmod(-0.0, 1.0) = &quot; &lt;&lt; std::fmod(-0.0, 1) &lt;&lt; '
'
              &lt;&lt; &quot;fmod(5.1, Inf) = &quot; &lt;&lt; std::fmod(5.1, INFINITY) &lt;&lt; '
';
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;fmod(+5.1, 0) = &quot; &lt;&lt; std::fmod(5.1, 0) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;fmod(+5.1, +3.0) = 2.1<br />
&nbsp;<wbr>&nbsp;fmod(-5.1, +3.0) = -2.1<br />
&nbsp;<wbr>&nbsp;fmod(+5.1, -3.0) = 2.1<br />
&nbsp;<wbr>&nbsp;fmod(-5.1, -3.0) = -2.1<br />
&nbsp;<wbr>&nbsp;fmod(+0.0, 1.0) = 0<br />
&nbsp;<wbr>&nbsp;fmod(-0.0, 1.0) = -0<br />
&nbsp;<wbr>&nbsp;fmod(5.1, Inf) = 5.1<br />
&nbsp;<wbr>&nbsp;fmod(+5.1, 0) = -nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>div(int)<br />
ldiv<br />
lldiv computes quotient and remainder of integer division<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
remainder<br />
remainderf<br />
remainderl signed remainder of the division operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
remquo<br />
remquof<br />
remquol signed remainder as well as the three last bits of the division operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
