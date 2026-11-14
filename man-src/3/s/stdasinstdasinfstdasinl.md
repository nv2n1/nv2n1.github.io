---
title: "stdasinstdasinfstdasinl(3)"
name: "stdasinstdasinfstdasinl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdasinstdasinfstdasinl/"
description: "std::asin,std::asinf,std::asinl – std::asin,std::asinf,std::asinl"
---

<p>std::asin,std::asinf,std::asinl &#8211; std::asin,std::asinf,std::asinl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float asin ( float arg );<br />
float asinf( float arg ); <i>(since C++11)</i><br />
double asin ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double asin ( long double arg );<br />
long double asinl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double asin ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the principal value of the arc sine of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the arc sine of arg (arcsin(arg)) in the range [-<br />
π<br />
2<br />
, +<br />
π<br />
2<br />
], is returned.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
Domain error occurs if arg is outside the range [-1.0, 1.0]<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is ±0, it is returned unmodified<br />
* If |arg| &gt; 1, a domain error occurs and NaN is returned.<br />
* if the argument is NaN, NaN is returned</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

#include &lt;cerrno&gt;

#include &lt;cfenv&gt;

#include &lt;cstring&gt;
#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;asin(1.0) = &quot; &lt;&lt; asin(1) &lt;&lt; '
'
              &lt;&lt; &quot;2*asin(1.0) = &quot; &lt;&lt; 2 * asin(1) &lt;&lt; '
'
              &lt;&lt; &quot;asin(-0.5) = &quot; &lt;&lt; asin(-0.5) &lt;&lt; '
'
              &lt;&lt; &quot;6*asin(-0.5) =&quot; &lt;&lt; 6 * asin(-0.5) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;asin(0.0) = &quot; &lt;&lt; asin(0) &lt;&lt; &quot; asin(-0.0)=&quot; &lt;&lt; asin(-0.0) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;asin(1.1) = &quot; &lt;&lt; asin(1.1) &lt;&lt; '
';
    if (errno == EDOM)
        std::cout &lt;&lt; &quot;    errno == EDOM: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised&quot; &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;asin(1.0) = 1.5708<br />
&nbsp;<wbr>&nbsp;2*asin(1.0) = 3.14159<br />
&nbsp;<wbr>&nbsp;asin(-0.5) = -0.523599<br />
&nbsp;<wbr>&nbsp;6*asin(-0.5) = -3.14159<br />
&nbsp;<wbr>&nbsp;asin(0.0) = 0 asin(-0.0)=-0<br />
&nbsp;<wbr>&nbsp;asin(1.1) = nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == EDOM: Numerical argument out of domain<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>acos<br />
acosf<br />
acosl computes arc cosine (arccos(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
atan<br />
atanf<br />
atanl computes arc tangent (arctan(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
atan2<br />
atan2f<br />
atan2l arc tangent, using signs to determine quadrants<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
sin<br />
sinf<br />
sinl computes sine (sin(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
asin(std::complex) computes arc sine of a complex number (arcsin(z))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::asin to each element of valarray<br />
asin(std::valarray) <i>(function template)</i> </p>
