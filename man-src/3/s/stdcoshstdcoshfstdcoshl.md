---
title: "stdcoshstdcoshfstdcoshl(3)"
name: "stdcoshstdcoshfstdcoshl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcoshstdcoshfstdcoshl/"
description: "std::cosh,std::coshf,std::coshl – std::cosh,std::coshf,std::coshl"
---

<p>std::cosh,std::coshf,std::coshl &#8211; std::cosh,std::coshf,std::coshl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float cosh ( float arg );<br />
float coshf( float arg ); <i>(since C++11)</i><br />
double cosh ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double cosh ( long double arg );<br />
long double coshl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double cosh ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the hyperbolic cosine of arg<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the hyperbolic cosine of arg (cosh(arg), or<br />
earg<br />
+e-arg<br />
2<br />
) is returned.<br />
If a range error due to overflow occurs, +HUGE_VAL, +HUGE_VALF, or +HUGE_VALL is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if the argument is ±0, 1 is returned<br />
* If the argument is ±∞, +∞ is returned<br />
* if the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>For the IEEE-compatible type double, if |arg| &gt; 710.5, then cosh(arg) overflows. </p>
<h2>Example</h2>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cstring&gt;

#include &lt;cfenv&gt;
#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;cosh(1) = &quot; &lt;&lt; std::cosh(1) &lt;&lt; '
'
              &lt;&lt; &quot;cosh(-1) = &quot; &lt;&lt; std::cosh(-1) &lt;&lt; '
'
              &lt;&lt; &quot;log(sinh(1)+cosh(1)=&quot; &lt;&lt; std::log(std::sinh(1) + std::cosh(1)) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;cosh(+0) = &quot; &lt;&lt; std::cosh(0.0) &lt;&lt; '
'
              &lt;&lt; &quot;cosh(-0) = &quot; &lt;&lt; std::cosh(-0.0) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;cosh(710.5) = &quot; &lt;&lt; std::cosh(710.5) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno == ERANGE: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout &lt;&lt; &quot;    FE_OVERFLOW raised
&quot;;
}
</code></pre>
<h2>See also</h2>
<p>sinh<br />
sinhf<br />
sinhl computes hyperbolic sine (sh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
tanh<br />
tanhf<br />
tanhl hyperbolic tangent<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
acosh<br />
acoshf<br />
acoshl computes the inverse hyperbolic cosine (arcosh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic cosine of a complex number (ch(z))<br />
cosh(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::cosh to each element of valarray<br />
cosh(std::valarray) <i>(function template)</i> </p>
