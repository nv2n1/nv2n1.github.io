---
title: "stdcosstdcosfstdcosl(3)"
name: "stdcosstdcosfstdcosl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcosstdcosfstdcosl/"
description: "std::cos,std::cosf,std::cosl – std::cos,std::cosf,std::cosl"
---

<p>std::cos,std::cosf,std::cosl &#8211; std::cos,std::cosf,std::cosl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float cos ( float arg );<br />
float cosf( float arg ); <i>(since C++11)</i><br />
double cos ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double cos ( long double arg );<br />
long double cosl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double cos ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the cosine of arg (measured in radians).<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value representing angle in radians, of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the cosine of arg (cos(arg)) in the range [-1 ; +1], is returned.<br />
The result may have little or no significance if the magnitude of arg is large <i>(until C++11)</i><br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if the argument is ±0, the result is 1.0<br />
* if the argument is ±∞, NaN is returned and FE_INVALID is raised<br />
* if the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>The case where the argument is infinite is not specified to be a domain error in C, but it is defined as a domain_error_in_POSIX </p>
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
    std::cout &lt;&lt; &quot;cos(pi/3) = &quot; &lt;&lt; std::cos(pi / 3) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi/2) = &quot; &lt;&lt; std::cos(pi / 2) &lt;&lt; '
'
              &lt;&lt; &quot;cos(-3*pi/4) = &quot; &lt;&lt; std::cos(-3 * pi / 4) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;cos(+0) = &quot; &lt;&lt; std::cos(0.0) &lt;&lt; '
'
              &lt;&lt; &quot;cos(-0) = &quot; &lt;&lt; std::cos(-0.0) &lt;&lt; '
';
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;cos(INFINITY) = &quot; &lt;&lt; std::cos(INFINITY) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;cos(pi/3) = 0.5<br />
&nbsp;<wbr>&nbsp;cos(pi/2) = 6.12323e-17<br />
&nbsp;<wbr>&nbsp;cos(-3*pi/4) = -0.707107<br />
&nbsp;<wbr>&nbsp;cos(+0) = 1<br />
&nbsp;<wbr>&nbsp;cos(-0) = 1<br />
&nbsp;<wbr>&nbsp;cos(INFINITY) = -nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>sin<br />
sinf<br />
sinl computes sine (sin(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
tan<br />
tanf<br />
tanl computes tangent (tan(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
acos<br />
acosf<br />
acosl computes arc cosine (arccos(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes cosine of a complex number (cos(z))<br />
cos(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::cos to each element of valarray<br />
cos(std::valarray) <i>(function template)</i> </p>
