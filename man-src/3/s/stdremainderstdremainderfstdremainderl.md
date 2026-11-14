---
title: "stdremainderstdremainderfstdremainderl(3)"
name: "stdremainderstdremainderfstdremainderl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremainderstdremainderfstdremainderl/"
description: "std::remainder,std::remainderf,std::remainderl – std::remainder,std::remainderf,std::remainderl"
---

<p>std::remainder,std::remainderf,std::remainderl &#8211; std::remainder,std::remainderf,std::remainderl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float remainder ( float x, float y ); <code>(1)</code> <i>(since C++11)</i><br />
float remainderf( float x, float y );<br />
double remainder ( double x, double y ); <code>(2)</code> <i>(since C++11)</i><br />
long double remainder ( long double x, long double y ); <code>(3)</code> <i>(since C++11)</i><br />
long double remainderl( long double x, long double y );<br />
Promoted remainder ( Arithmetic1 x, Arithmetic2 y ); <code>(4)</code> <i>(since C++11)</i> </p>
<pre><code>1-3) Computes the IEEE remainder of the floating point division operation x/y.

4) A set of overloads or a function template for all combinations of arguments of arithmetic_type not covered by (1-3). If any argument has integral_type, it is cast to double. If any other argument is long double, then the return type is long double, otherwise it is double.

The IEEE floating-point remainder of the division operation x/y calculated by this function is exactly the value x - n*y, where the value n is the integral value nearest the exact value x/y. When |n-x/y| = ½, the value n is chosen to be even.

In contrast to std::fmod(), the returned value is not guaranteed to have the same sign as x.

If the returned value is 0, it will have the same sign as x.
</code></pre>
<h2>Parameters</h2>
<p>x, y &#8211; values of floating-point or integral_types</p>
<h2>Return value</h2>
<p>If successful, returns the IEEE floating-point remainder of the division x/y as defined above.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a range error occurs due to underflow, the correct result is returned.<br />
If y is zero, but the domain error does not occur, zero is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
Domain error may occur if y is zero.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* The current rounding_mode has no effect.<br />
* FE_INEXACT is never raised, the result is always exact.<br />
* If x is ±∞ and y is not NaN, NaN is returned and FE_INVALID is raised<br />
* If y is ±0 and x is not NaN, NaN is returned and FE_INVALID is raised<br />
* If either argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>POSIX_requires that a domain error occurs if x is infinite or y is zero.<br />
std::fmod, but not std::remainder is useful for doing silent wrapping of floating-point types to unsigned integer types: (0.0 &lt;= (y = std::fmod( std::rint(x), 65536.0 )) ? y : 65536.0 + y) is in the range [-0.0 .. 65535.0], which corresponds to unsigned short, but std::remainder(std::rint(x), 65536.0) is in the range [-32767.0, +32768.0], which is outside of the range of signed short. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfenv&gt;
#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;remainder(+5.1, +3.0) = &quot; &lt;&lt; std::remainder(5.1, 3) &lt;&lt; '
'
              &lt;&lt; &quot;remainder(-5.1, +3.0) = &quot; &lt;&lt; std::remainder(-5.1, 3) &lt;&lt; '
'
              &lt;&lt; &quot;remainder(+5.1, -3.0) = &quot; &lt;&lt; std::remainder(5.1, -3) &lt;&lt; '
'
              &lt;&lt; &quot;remainder(-5.1, -3.0) = &quot; &lt;&lt; std::remainder(-5.1, -3) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;remainder(-0.0, 1.0) = &quot; &lt;&lt; std::remainder(-0.0, 1) &lt;&lt; '
'
              &lt;&lt; &quot;remainder(5.1, Inf) = &quot; &lt;&lt; std::remainder(5.1, INFINITY) &lt;&lt; '
';
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;remainder(+5.1, 0) = &quot; &lt;&lt; std::remainder(5.1, 0) &lt;&lt; '
';
    if (fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;remainder(+5.1, +3.0) = -0.9<br />
&nbsp;<wbr>&nbsp;remainder(-5.1, +3.0) = 0.9<br />
&nbsp;<wbr>&nbsp;remainder(+5.1, -3.0) = -0.9<br />
&nbsp;<wbr>&nbsp;remainder(-5.1, -3.0) = 0.9<br />
&nbsp;<wbr>&nbsp;remainder(-0.0, 1.0) = -0<br />
&nbsp;<wbr>&nbsp;remainder(5.1, Inf) = 5.1<br />
&nbsp;<wbr>&nbsp;remainder(+5.1, 0) = -nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>div(int)<br />
ldiv<br />
lldiv computes quotient and remainder of integer division<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
fmod<br />
fmodf<br />
fmodl remainder of the floating point division operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
remquo<br />
remquof<br />
remquol signed remainder as well as the three last bits of the division operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
