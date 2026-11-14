---
title: "stdatan2stdatan2fstdatan2l(3)"
name: "stdatan2stdatan2fstdatan2l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatan2stdatan2fstdatan2l/"
description: "std::atan2,std::atan2f,std::atan2l – std::atan2,std::atan2f,std::atan2l"
---

<p>std::atan2,std::atan2f,std::atan2l &#8211; std::atan2,std::atan2f,std::atan2l</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float atan2 ( float y, float x );<br />
float atan2f( float y, float x ); <i>(since C++11)</i><br />
double atan2 ( double y, double x ); <code>(1)</code> <code>(2)</code><br />
long double atan2 ( long double y, long double x );<br />
long double atan2l( long double y, long double x ); <code>(3)</code> <i>(since C++11)</i><br />
Promoted atan2 ( Arithmetic1 y, Arithmetic2 x ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the arc tangent of y/x using the signs of arguments to determine the correct quadrant.<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by 1-3). If any argument has integral_type, it is cast to double. If any argument is long double, then the return type Promoted is also long double, otherwise the return type is always double. </p>
<h2>Parameters</h2>
<p>x, y &#8211; values of floating-point or integral_types</p>
<h2>Return value</h2>
<p>If no errors occur, the arc tangent of y/x (arctan( </p>
<p>y<br />
x </p>
<p>)) in the range [-π , +π] radians, is returned.<br />
Y argument</p>
<h2>Return value</h2>
<p>X argument<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
Domain error may occur if x and y are both zero.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If x and y are both zero, domain error does not occur<br />
* If x and y are both zero, range error does not occur either<br />
* If y is zero, pole error does not occur<br />
* If y is ±0 and x is negative or -0, ±π is returned<br />
* If y is ±0 and x is positive or +0, ±0 is returned<br />
* If y is ±∞ and x is finite, ±π/2 is returned<br />
* If y is ±∞ and x is -∞, ±3π/4 is returned<br />
* If y is ±∞ and x is +∞, ±π/4 is returned<br />
* If x is ±0 and y is negative, -π/2 is returned<br />
* If x is ±0 and y is positive, +π/2 is returned<br />
* If x is -∞ and y is finite and positive, +π is returned<br />
* If x is -∞ and y is finite and negative, -π is returned<br />
* If x is +∞ and y is finite and positive, +0 is returned<br />
* If x is +∞ and y is finite and negative, -0 is returned<br />
* If either x is NaN or y is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>std::atan2(y, x) is equivalent to std::arg(std::complex&lt;double&gt;(x,y))<br />
POSIX_specifies that in case of underflow, y/x is the value returned, and if that is not supported, and implementation-defined value no greater than DBL_MIN, FLT_MIN, and LDBL_MIN is returned. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;
int main()

{
    // normal usage: the signs of the two arguments determine the quadrant
    std::cout &lt;&lt; &quot;(+1,+1) cartesian is (&quot; &lt;&lt; hypot(1, 1)
              &lt;&lt; ',' &lt;&lt; atan2(1, 1) &lt;&lt; &quot;) polar
&quot; // atan2(1,1) = +pi/4, Quad I
              &lt;&lt; &quot;(+1,-1) cartesian is (&quot; &lt;&lt; hypot(1, -1)
              &lt;&lt; ',' &lt;&lt; atan2(1, -1) &lt;&lt; &quot;) polar
&quot; // atan2(1, -1) = +3pi/4, Quad II
              &lt;&lt; &quot;(-1,-1) cartesian is (&quot; &lt;&lt; hypot(-1, -1)
              &lt;&lt; ',' &lt;&lt; atan2(-1, -1) &lt;&lt; &quot;) polar
&quot; // atan2(-1,-1) = -3pi/4, Quad III
              &lt;&lt; &quot;(-1,+1) cartesian is (&quot; &lt;&lt; hypot(-1, 1)
              &lt;&lt; ',' &lt;&lt; atan2(-1, 1) &lt;&lt; &quot;) polar
&quot;; // atan2(-1,-1) = -pi/4, Quad IV
    // special values
    std::cout &lt;&lt; &quot;atan2(0, 0) = &quot; &lt;&lt; atan2(0, 0)
              &lt;&lt; &quot; atan2(0,-0) = &quot; &lt;&lt; atan2(0, -0.0) &lt;&lt; '
'
              &lt;&lt; &quot;atan2(7, 0) = &quot; &lt;&lt; atan2(7, 0)
              &lt;&lt; &quot; atan2(7,-0) = &quot; &lt;&lt; atan2(7, -0.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;(+1,+1) cartesian is (1.41421,0.785398) polar<br />
&nbsp;<wbr>&nbsp;(+1,-1) cartesian is (1.41421,2.35619) polar<br />
&nbsp;<wbr>&nbsp;(-1,-1) cartesian is (1.41421,-2.35619) polar<br />
&nbsp;<wbr>&nbsp;(-1,+1) cartesian is (1.41421,-0.785398) polar<br />
&nbsp;<wbr>&nbsp;atan2(0, 0) = 0 atan2(0,-0) = 3.14159<br />
&nbsp;<wbr>&nbsp;atan2(7, 0) = 1.5708 atan2(7,-0) = 1.5708</p>
<h2>See also</h2>
<p>asin<br />
asinf<br />
asinl computes arc sine (arcsin(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
acos<br />
acosf<br />
acosl computes arc cosine (arccos(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
atan<br />
atanf<br />
atanl computes arc tangent (arctan(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the phase angle<br />
arg <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::atan2 to a valarray and a value<br />
atan2(std::valarray) <i>(function template)</i> </p>
