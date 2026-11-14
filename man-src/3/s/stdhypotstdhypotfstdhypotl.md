---
title: "stdhypotstdhypotfstdhypotl(3)"
name: "stdhypotstdhypotfstdhypotl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhypotstdhypotfstdhypotl/"
description: "std::hypot,std::hypotf,std::hypotl – std::hypot,std::hypotf,std::hypotl"
---

<p>std::hypot,std::hypotf,std::hypotl &#8211; std::hypot,std::hypotf,std::hypotl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float hypot ( float x, float y ); <code>(1)</code> <i>(since C++11)</i><br />
float hypotf( float x, float y );<br />
double hypot ( double x, double y ); <code>(2)</code> <i>(since C++11)</i><br />
long double hypot ( long double x, long double y ); <code>(3)</code> <i>(since C++11)</i><br />
long double hypotl( long double x, long double y );<br />
Promoted hypot ( Arithmetic1 x, Arithmetic2 y ); <code>(4)</code> <i>(since C++11)</i><br />
float hypot ( float x, float y, float z ); <code>(5)</code> <i>(since C++17)</i><br />
double hypot ( double x, double y, double z ); <code>(6)</code> <i>(since C++17)</i><br />
long double hypot ( long double x, long double y, long double z ); <code>(7)</code> <i>(since C++17)</i><br />
Promoted hypot ( Arithmetic1 x, Arithmetic2 y, Arithmetic3 z ); <code>(8)</code> <i>(since C++17)</i> </p>
<pre><code>1-3) Computes the square root of the sum of the squares of x and y, without undue overflow or underflow at intermediate stages of the computation.

4) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by (1-3). If any argument has integral_type, it is cast to double. If any other argument is long double, then the return type is long double, otherwise it is double.

5-7) Computes the square root of the sum of the squares of x, y, and z, without undue overflow or underflow at intermediate stages of the computation.

8) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by (5-7). If any argument has integral_type, it is cast to double. If any other argument is long double, then the return type is long double, otherwise it is double.

The value computed by the two-argument version of this function is the length of the hypotenuse of a right-angled triangle with sides of length x and y, or the distance of the point (x,y) from the origin (0,0), or the magnitude of a complex number x+iy

The value computed by the three-argument version of this function is the distance of the point (x,y,z) from the origin (0,0,0).
</code></pre>
<h2>Parameters</h2>
<p>x, y, z &#8211; values of floating-point or integral_types</p>
<h2>Return value</h2>
<p>1-4) If no errors occur, the hypotenuse of a right-angled triangle,<br />
√<br />
x2<br />
+y2<br />
, is returned.<br />
5-8) If no errors occur, the distance from origin in 3D space,<br />
√<br />
x2<br />
+y2<br />
+z2<br />
, is returned.<br />
If a range error due to overflow occurs, +HUGE_VAL, +HUGE_VALF, or +HUGE_VALL is returned.<br />
If a range error due to underflow occurs, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* hypot(x, y), hypot(y, x), and hypot(x, -y) are equivalent<br />
* if one of the arguments is ±0, hypot(x,y) is equivalent to fabs called with the non-zero argument<br />
* if one of the arguments is ±∞, hypot(x,y) returns +∞ even if the other argument is NaN<br />
* otherwise, if any of the arguments is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>Implementations usually guarantee precision of less than 1 ulp (units in the last place): GNU, BSD, Open64<br />
std::hypot(x, y) is equivalent to std::abs(std::complex&lt;double&gt;(x,y))<br />
POSIX_specifies that underflow may only occur when both arguments are subnormal and the correct result is also subnormal (this forbids naive implementations)<br />
Distance between two points (x1,y1,z1) and (x2,y2,z2)on 3D space can be calculated as std::hypot(x2-x1, y2-y1, z2-z1) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cfenv&gt;

#include &lt;cfloat&gt;

#include &lt;cstring&gt;
#pragma STDC FENV_ACCESS ON

int main()

{
    // typical usage
    std::cout &lt;&lt; &quot;(1,1) cartesian is (&quot; &lt;&lt; std::hypot(1, 1)
              &lt;&lt; ',' &lt;&lt; std::atan2(1, 1) &lt;&lt; &quot;) polar
&quot;;
    // special values
    std::cout &lt;&lt; &quot;hypot(NAN,INFINITY) = &quot; &lt;&lt; std::hypot(NAN, INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;hypot(DBL_MAX,DBL_MAX) = &quot; &lt;&lt; std::hypot(DBL_MAX, DBL_MAX) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno = ERANGE &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (fetestexcept(FE_OVERFLOW))
        std::cout &lt;&lt; &quot;    FE_OVERFLOW raised
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;(1,1) cartesian is (1.41421,0.785398) polar<br />
&nbsp;<wbr>&nbsp;hypot(NAN,INFINITY) = inf<br />
&nbsp;<wbr>&nbsp;hypot(DBL_MAX,DBL_MAX) = inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno = ERANGE Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_OVERFLOW raised</p>
<h2>See also</h2>
<p>pow<br />
powf<br />
powl raises a number to the given power (xy)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
sqrt<br />
sqrtf computes square root (<br />
sqrtl √<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
cbrt computes cubic root (<br />
cbrtf 3<br />
cbrtl √<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x)<br />
<i>(C++11)</i> <i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the magnitude of a complex number<br />
abs(std::complex) <i>(function template)</i> </p>
