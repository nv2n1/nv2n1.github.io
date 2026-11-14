---
title: "stdsinhstdsinhfstdsinhl(3)"
name: "stdsinhstdsinhfstdsinhl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsinhstdsinhfstdsinhl/"
description: "std::sinh,std::sinhf,std::sinhl – std::sinh,std::sinhf,std::sinhl"
---

<p>std::sinh,std::sinhf,std::sinhl &#8211; std::sinh,std::sinhf,std::sinhl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float sinh ( float arg );<br />
float sinhf( float arg ); <i>(since C++11)</i><br />
double sinh ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double sinh ( long double arg );<br />
long double sinhl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double sinh ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the hyperbolic sine of arg<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the hyperbolic sine of arg (sinh(arg), or<br />
earg<br />
-e-arg<br />
2<br />
) is returned.<br />
If a range error due to overflow occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if the argument is ±0 or ±∞, it is returned unmodified<br />
* if the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>POSIX_specifies that in case of underflow, arg is returned unmodified, and if that is not supported, and implementation-defined value no greater than DBL_MIN, FLT_MIN, and LDBL_MIN is returned. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cstring&gt;

#include &lt;cfenv&gt;
#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;sinh(1) = &quot; &lt;&lt; std::sinh(1) &lt;&lt; '
'
              &lt;&lt; &quot;sinh(-1) = &quot; &lt;&lt; std::sinh(-1) &lt;&lt; '
'
              &lt;&lt; &quot;log(sinh(1)+cosh(1)) = &quot;
              &lt;&lt; std::log(std::sinh(1) + std::cosh(1)) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;sinh(+0) = &quot; &lt;&lt; std::sinh(0.0) &lt;&lt; '
'
              &lt;&lt; &quot;sinh(-0) = &quot; &lt;&lt; std::sinh(-0.0) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;sinh(710.5) = &quot; &lt;&lt; std::sinh(710.5) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno == ERANGE: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout &lt;&lt; &quot;    FE_OVERFLOW raised
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-sinh/">sinh</a><code>(1)</code> = 1.1752<br />
&nbsp;<wbr>&nbsp;sinh(-1) = -1.1752<br />
&nbsp;<wbr>&nbsp;log(<a href="/docs/linux/man/1-sinh/">sinh</a><code>(1)</code>+<a href="/docs/linux/man/1-cosh/">cosh</a>(1)) = 1<br />
&nbsp;<wbr>&nbsp;sinh(+0) = 0<br />
&nbsp;<wbr>&nbsp;sinh(-0) = -0<br />
&nbsp;<wbr>&nbsp;sinh(710.5) = inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_OVERFLOW raised</p>
<h2>See also</h2>
<p>cosh<br />
coshf<br />
coshl computes hyperbolic cosine (ch(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
tanh<br />
tanhf<br />
tanhl hyperbolic tangent<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
asinh<br />
asinhf<br />
asinhl computes the inverse hyperbolic sine (arsinh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic sine of a complex number (sh(z))<br />
sinh(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::sinh to each element of valarray<br />
sinh(std::valarray) <i>(function template)</i> </p>
