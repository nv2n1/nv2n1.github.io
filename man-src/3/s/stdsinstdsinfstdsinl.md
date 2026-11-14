---
title: "stdsinstdsinfstdsinl(3)"
name: "stdsinstdsinfstdsinl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsinstdsinfstdsinl/"
description: "std::sin,std::sinf,std::sinl – std::sin,std::sinf,std::sinl"
---

<p>std::sin,std::sinf,std::sinl &#8211; std::sin,std::sinf,std::sinl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float sin ( float arg );<br />
float sinf( float arg ); <i>(since C++11)</i><br />
double sin ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double sin ( long double arg );<br />
long double sinl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double sin ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the sine of arg (measured in radians).<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value representing angle in radians, of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the sine of arg (sin(arg)) in the range [-1 ; +1], is returned.<br />
The result may have little or no significance if the magnitude of arg is large <i>(until C++11)</i><br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if the argument is ±0, it is returned unmodified<br />
* if the argument is ±∞, NaN is returned and FE_INVALID is raised<br />
* if the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>The case where the argument is infinite is not specified to be a domain error in C (to which C++ defers), but it is defined as a domain_error_in_POSIX<br />
POSIX also specifies that in case of underflow, arg is returned unmodified, and if that is not supported, an implementation-defined value no greater than DBL_MIN, FLT_MIN, and LDBL_MIN is returned. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cfenv&gt;
#pragma STDC FENV_ACCESS ON

const double pi = std::acos(-1);

int main()

{
    // typical usage
    std::cout &lt;&lt; &quot;sin(pi/6) = &quot; &lt;&lt; std::sin(pi / 6) &lt;&lt; '
'
              &lt;&lt; &quot;sin(pi/2) = &quot; &lt;&lt; std::sin(pi / 2) &lt;&lt; '
'
              &lt;&lt; &quot;sin(-3*pi/4) = &quot; &lt;&lt; std::sin(-3 * pi / 4) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;sin(+0) = &quot; &lt;&lt; std::sin(0.0) &lt;&lt; '
'
              &lt;&lt; &quot;sin(-0) = &quot; &lt;&lt; std::sin(-0.0) &lt;&lt; '
';
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;sin(INFINITY) = &quot; &lt;&lt; std::sin(INFINITY) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;sin(pi/6) = 0.5<br />
&nbsp;<wbr>&nbsp;sin(pi/2) = 1<br />
&nbsp;<wbr>&nbsp;sin(-3*pi/4) = -0.707107<br />
&nbsp;<wbr>&nbsp;sin(+0) = 0<br />
&nbsp;<wbr>&nbsp;sin(-0) = -0<br />
&nbsp;<wbr>&nbsp;sin(INFINITY) = -nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>cos<br />
cosf<br />
cosl computes cosine (cos(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
tan<br />
tanf<br />
tanl computes tangent (tan(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
asin<br />
asinf<br />
asinl computes arc sine (arcsin(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes sine of a complex number (sin(z))<br />
sin(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::sin to each element of valarray<br />
sin(std::valarray) <i>(function template)</i> </p>
