---
title: "stdatanhstdatanhstdatanhl(3)"
name: "stdatanhstdatanhstdatanhl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatanhstdatanhstdatanhl/"
description: "std::atanh,std::atanh,std::atanhl – std::atanh,std::atanh,std::atanhl"
---

<p>std::atanh,std::atanh,std::atanhl &#8211; std::atanh,std::atanh,std::atanhl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float atanh ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float atanhf( float arg );<br />
double atanh ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double atanh ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double atanhl( long double arg );<br />
double atanh ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the inverse hyperbolic tangent of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the inverse hyperbolic tangent of arg (tanh-1<br />
(arg), or artanh(arg)), is returned.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a pole error occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned (with the correct sign).<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the argument is not on the interval [-1, +1], a range error occurs.<br />
If the argument is ±1, a pole error occurs.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if the argument is ±0, it is returned unmodified<br />
* if the argument is ±1, ±∞ is returned and FE_DIVBYZERO is raised.<br />
* if |arg|&gt;1, NaN is returned and FE_INVALID is raised.<br />
* if the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>Although the C standard (to which C++ refers for this function) names this function &quot;arc hyperbolic tangent&quot;, the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is &quot;inverse hyperbolic tangent&quot; (used by POSIX) or &quot;area hyperbolic tangent&quot;.<br />
POSIX_specifies that in case of underflow, arg is returned unmodified, and if that is not supported, an implementation-defined value no greater than DBL_MIN, FLT_MIN, and LDBL_MIN is returned. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfloat&gt;

#include &lt;cerrno&gt;

#include &lt;cfenv&gt;

#include &lt;cstring&gt;

#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;atanh(0) = &quot; &lt;&lt; std::atanh(0) &lt;&lt; '
'
              &lt;&lt; &quot;atanh(-0) = &quot; &lt;&lt; std::atanh(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;atanh(0.9) = &quot; &lt;&lt; std::atanh(0.9) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;atanh(-1) = &quot; &lt;&lt; std::atanh(-1) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno == ERANGE: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout &lt;&lt; &quot;    FE_DIVBYZERO raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;atanh<code>(0)</code> = 0<br />
&nbsp;<wbr>&nbsp;atanh(-0) = -0<br />
&nbsp;<wbr>&nbsp;atanh(0.9) = 1.47222<br />
&nbsp;<wbr>&nbsp;atanh(-1) = -inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_DIVBYZERO raised</p>
<h2>See also</h2>
<p>asinh<br />
asinhf<br />
asinhl computes the inverse hyperbolic sine (arsinh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
acosh<br />
acoshf<br />
acoshl computes the inverse hyperbolic cosine (arcosh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
tanh<br />
tanhf<br />
tanhl hyperbolic tangent<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
atanh(std::complex) computes area hyperbolic tangent of a complex number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Inverse_Hyperbolic_Tangent.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
