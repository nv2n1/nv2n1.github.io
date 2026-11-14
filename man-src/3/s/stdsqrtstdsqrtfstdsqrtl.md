---
title: "stdsqrtstdsqrtfstdsqrtl(3)"
name: "stdsqrtstdsqrtfstdsqrtl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsqrtstdsqrtfstdsqrtl/"
description: "std::sqrt,std::sqrtf,std::sqrtl – std::sqrt,std::sqrtf,std::sqrtl"
---

<p>std::sqrt,std::sqrtf,std::sqrtl &#8211; std::sqrt,std::sqrtf,std::sqrtl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float sqrt ( float arg );<br />
float sqrtf( float arg ); <i>(since C++11)</i><br />
double sqrt ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double sqrt ( long double arg );<br />
long double sqrtl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double sqrt ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the square root of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; Value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, square root of arg (<br />
√<br />
arg), is returned.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling<br />
Domain error occurs if arg is less than zero.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is less than -0, FE_INVALID is raised and NaN is returned.<br />
* If the argument is +∞ or ±0, it is returned, unmodified.<br />
* If the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>std::sqrt is required by the IEEE standard to be exact. The only other operations required to be exact are the arithmetic_operators and the function std::fma. After rounding to the return type (using default rounding mode), the result of std::sqrt is indistinguishable from the infinitely precise result. In other words, the error is less than 0.5 ulp. Other functions, including std::pow, are not so constrained. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cfenv&gt;

#include &lt;cstring&gt;</code></pre>
<p>&nbsp;<wbr>&nbsp;#pragma STDC FENV_ACCESS ON </p>
<pre><code>int main()

{
    // normal use
    std::cout &lt;&lt; &quot;sqrt(100) = &quot; &lt;&lt; std::sqrt(100) &lt;&lt; '
'
              &lt;&lt; &quot;sqrt(2) = &quot; &lt;&lt; std::sqrt(2) &lt;&lt; '
'
              &lt;&lt; &quot;golden ratio = &quot; &lt;&lt; (1 + std::sqrt(5)) / 2 &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;sqrt(-0) = &quot; &lt;&lt; std::sqrt(-0.0) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;sqrt(-1.0) = &quot; &lt;&lt; std::sqrt(-1) &lt;&lt; '
';
    if (errno == EDOM)
        std::cout &lt;&lt; &quot;    errno = EDOM &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;sqrt(100) = 10<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/2-sqrt/">sqrt</a><code>(2)</code> = 1.41421<br />
&nbsp;<wbr>&nbsp;golden ratio = 1.61803<br />
&nbsp;<wbr>&nbsp;sqrt(-0) = -0<br />
&nbsp;<wbr>&nbsp;sqrt(-1.0) = -nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno = EDOM Numerical argument out of domain<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>pow<br />
powf<br />
powl raises a number to the given power (xy)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
cbrt computes cubic root (<br />
cbrtf 3<br />
cbrtl √<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x)<br />
<i>(C++11)</i> <i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
hypot computes square root of the sum of the squares of two given numbers (<br />
hypotf √<br />
hypotl x2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+y2<br />
<i>(C++11)</i> )<br />
<i>(C++11)</i> <i>(function)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex square root in the range of the right half-plane<br />
sqrt(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::sqrt to each element of valarray<br />
sqrt(std::valarray) <i>(function template)</i> </p>
