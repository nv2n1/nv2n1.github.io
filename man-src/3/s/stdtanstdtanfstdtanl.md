---
title: "stdtanstdtanfstdtanl(3)"
name: "stdtanstdtanfstdtanl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtanstdtanfstdtanl/"
description: "std::tan,std::tanf,std::tanl – std::tan,std::tanf,std::tanl"
---

<p>std::tan,std::tanf,std::tanl &#8211; std::tan,std::tanf,std::tanl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float tan ( float arg );<br />
float tanf( float arg ); <i>(since C++11)</i><br />
double tan ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double tan ( long double arg );<br />
long double tanl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double tan ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the tangent of arg (measured in radians).<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value representing angle in radians, of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the tangent of arg (tan(arg)) is returned.<br />
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
The function has mathematical poles at π(1/2 + n); however no common floating-point representation is able to represent π/2 exactly, thus there is no value of the argument for which a pole error occurs. </p>
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
    std::cout &lt;&lt; &quot;tan  (pi/4) = &quot; &lt;&lt; std::tan(pi / 4) &lt;&lt; '
'      // 45 deg.
              &lt;&lt; &quot;tan(3*pi/4) = &quot; &lt;&lt; std::tan(3 * pi / 4) &lt;&lt; '
'  // 135 deg
              &lt;&lt; &quot;tan(5*pi/4) = &quot; &lt;&lt; std::tan(5 * pi / 4) &lt;&lt; '
'  // -135 deg
              &lt;&lt; &quot;tan(7*pi/4) = &quot; &lt;&lt; std::tan(7 * pi / 4) &lt;&lt; '
'; // -45 deg
    // special values
    std::cout &lt;&lt; &quot;tan(+0) = &quot; &lt;&lt; std::tan(0.0) &lt;&lt; '
'
              &lt;&lt; &quot;tan(-0) = &quot; &lt;&lt; std::tan(-0.0) &lt;&lt; '
';
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;tan(INFINITY) = &quot; &lt;&lt; std::tan(INFINITY) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;tan (pi/4) = 1<br />
&nbsp;<wbr>&nbsp;tan(3*pi/4) = -1<br />
&nbsp;<wbr>&nbsp;tan(5*pi/4) = 1<br />
&nbsp;<wbr>&nbsp;tan(7*pi/4) = -1<br />
&nbsp;<wbr>&nbsp;tan(+0) = 0<br />
&nbsp;<wbr>&nbsp;tan(-0) = -0<br />
&nbsp;<wbr>&nbsp;tan(INFINITY) = -nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>sin<br />
sinf<br />
sinl computes sine (sin(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
cos<br />
cosf<br />
cosl computes cosine (cos(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
atan<br />
atanf<br />
atanl computes arc tangent (arctan(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes tangent of a complex number (tan(z))<br />
tan(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::tan to each element of valarray<br />
tan(std::valarray) <i>(function template)</i> </p>
