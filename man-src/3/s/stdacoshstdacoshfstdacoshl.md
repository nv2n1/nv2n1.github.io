---
title: "stdacoshstdacoshfstdacoshl(3)"
name: "stdacoshstdacoshfstdacoshl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdacoshstdacoshfstdacoshl/"
description: "std::acosh,std::acoshf,std::acoshl – std::acosh,std::acoshf,std::acoshl"
---

<p>std::acosh,std::acoshf,std::acoshl &#8211; std::acosh,std::acoshf,std::acoshl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float acosh ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float acoshf( float arg );<br />
double acosh ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double acosh ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double acoshl( long double arg );<br />
double acosh ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the inverse hyperbolic cosine of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the inverse hyperbolic cosine of arg (cosh-1<br />
(arg), or arcosh(arg)) on the interval [0, +∞], is returned.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported) </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the argument is less than 1, a domain error occurs.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if the argument is less than 1, FE_INVALID is raised an NaN is returned<br />
* if the argument is 1, +0 is returned<br />
* if the argument is +∞, +∞ is returned<br />
* if the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>Although the C standard (to which C++ refers for this function) names this function &quot;arc hyperbolic cosine&quot;, the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is &quot;inverse hyperbolic cosine&quot; (used by POSIX) or &quot;area hyperbolic cosine&quot;. </p>
<h2>Examples</h2>
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
    std::cout &lt;&lt; &quot;acosh(1) = &quot; &lt;&lt; std::acosh(1) &lt;&lt; '
'
              &lt;&lt; &quot;acosh(10) = &quot; &lt;&lt; std::acosh(10) &lt;&lt; '
'
              &lt;&lt; &quot;acosh(DBL_MAX) = &quot; &lt;&lt; std::acosh(DBL_MAX) &lt;&lt; '
'
              &lt;&lt; &quot;acosh(Inf) = &quot; &lt;&lt; std::acosh(INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;acosh(0.5) = &quot; &lt;&lt; std::acosh(0.5) &lt;&lt; '
';
    if (errno == EDOM)
        std::cout &lt;&lt; &quot;    errno == EDOM: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-acosh/">acosh</a><code>(1)</code> = 0<br />
&nbsp;<wbr>&nbsp;acosh<code>(10)</code> = 2.99322<br />
&nbsp;<wbr>&nbsp;acosh(DBL_MAX) = 710.476<br />
&nbsp;<wbr>&nbsp;acosh(Inf) = inf<br />
&nbsp;<wbr>&nbsp;acosh(0.5) = -nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == EDOM: Numerical argument out of domain<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>asinh<br />
asinhf<br />
asinhl computes the inverse hyperbolic sine (arsinh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
atanh<br />
atanhf<br />
atanhl computes the inverse hyperbolic tangent (artanh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
cosh<br />
coshf<br />
coshl computes hyperbolic cosine (ch(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
acosh(std::complex) computes area hyperbolic cosine of a complex number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Inverse_Hyperbolic_Cosine.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
