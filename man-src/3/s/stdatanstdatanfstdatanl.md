---
title: "stdatanstdatanfstdatanl(3)"
name: "stdatanstdatanfstdatanl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatanstdatanfstdatanl/"
description: "std::atan,std::atanf,std::atanl – std::atan,std::atanf,std::atanl"
---

<p>std::atan,std::atanf,std::atanl &#8211; std::atan,std::atanf,std::atanl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float atan ( float arg );<br />
float atanf( float arg ); <i>(since C++11)</i><br />
double atan ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double atan ( long double arg );<br />
long double atanl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double atan ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the principal value of the arc tangent of arg<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the arc tangent of arg (arctan(arg)) in the range [-<br />
π<br />
2<br />
, +<br />
π<br />
2<br />
] radians, is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is ±0, it is returned unmodified<br />
* If the argument is +∞, +π/2 is returned<br />
* If the argument is -∞, -π/2 is returned<br />
* if the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>POSIX_specifies that in case of underflow, arg is returned unmodified, and if that is not supported, and implementation-defined value no greater than DBL_MIN, FLT_MIN, and LDBL_MIN is returned. </p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;
int main()

{
    std::cout &lt;&lt; &quot;atan(1) = &quot; &lt;&lt; atan(1) &lt;&lt; &quot; 4*atan(1) = &quot; &lt;&lt; 4 * atan(1) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;atan(Inf) = &quot; &lt;&lt; atan(INFINITY)
              &lt;&lt; &quot; 2*atan(Inf) = &quot; &lt;&lt; 2 * atan(INFINITY) &lt;&lt; '
'
              &lt;&lt; &quot;atan(-0.0) = &quot; &lt;&lt; atan(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;atan(+0.0) = &quot; &lt;&lt; atan(0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-atan/">atan</a><code>(1)</code> = 0.785398 4*<a href="/docs/linux/man/1-atan/">atan</a>(1) = 3.14159<br />
&nbsp;<wbr>&nbsp;atan(Inf) = 1.5708 2*atan(Inf) = 3.14159<br />
&nbsp;<wbr>&nbsp;atan(-0.0) = -0<br />
&nbsp;<wbr>&nbsp;atan(+0.0) = 0</p>
<h2>See also</h2>
<p>asin<br />
asinf<br />
asinl computes arc sine (arcsin(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
acos<br />
acosf<br />
acosl computes arc cosine (arccos(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
atan2<br />
atan2f<br />
atan2l arc tangent, using signs to determine quadrants<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
tan<br />
tanf<br />
tanl computes tangent (tan(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
atan(std::complex) computes arc tangent of a complex number (arctan(z))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::atan to each element of valarray<br />
atan(std::valarray) <i>(function template)</i> </p>
