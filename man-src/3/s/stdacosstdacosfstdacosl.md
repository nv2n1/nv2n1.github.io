---
title: "stdacosstdacosfstdacosl(3)"
name: "stdacosstdacosfstdacosl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdacosstdacosfstdacosl/"
description: "std::acos,std::acosf,std::acosl – std::acos,std::acosf,std::acosl"
---

<p>std::acos,std::acosf,std::acosl &#8211; std::acos,std::acosf,std::acosl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float acos ( float arg );<br />
float acosf( float arg ); <i>(since C++11)</i><br />
double acos ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double acos ( long double arg );<br />
long double acosl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double acos ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the principal value of the arc cosine of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the arc cosine of arg (arccos(arg)) in the range [0 , π], is returned.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
Domain error occurs if arg is outside the range [-1.0, 1.0]<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is +1, the value +0 is returned.<br />
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
    std::cout &lt;&lt; &quot;acos(-1) = &quot; &lt;&lt; acos(-1) &lt;&lt; '
'
              &lt;&lt; &quot;acos(0.0) = &quot; &lt;&lt; acos(0.0) &lt;&lt; &quot; 2*acos(0.0) = &quot; &lt;&lt; 2 * acos(0) &lt;&lt; '
'
              &lt;&lt; &quot;acos(0.5) = &quot; &lt;&lt; acos(0.5) &lt;&lt; &quot; 3*acos(0.5) = &quot; &lt;&lt; 3 * acos(0.5) &lt;&lt; '
'
              &lt;&lt; &quot;acos(1) = &quot; &lt;&lt; acos(1) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;acos(1.1) = &quot; &lt;&lt; acos(1.1) &lt;&lt; '
';
    if (errno == EDOM)
        std::cout &lt;&lt; &quot;    errno == EDOM: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised&quot; &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;acos(-1) = 3.14159<br />
&nbsp;<wbr>&nbsp;acos(0.0) = 1.5708 2*acos(0.0) = 3.14159<br />
&nbsp;<wbr>&nbsp;acos(0.5) = 1.0472 3*acos(0.5) = 3.14159<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-acos/">acos</a><code>(1)</code> = 0<br />
&nbsp;<wbr>&nbsp;acos(1.1) = nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == EDOM: Numerical argument out of domain<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>asin<br />
asinf<br />
asinl computes arc sine (arcsin(x))<br />
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
cos<br />
cosf<br />
cosl computes cosine (cos(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
acos(std::complex) computes arc cosine of a complex number (arccos(z))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::acos to each element of valarray<br />
acos(std::valarray) <i>(function template)</i> </p>
