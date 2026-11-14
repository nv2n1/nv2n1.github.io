---
title: "stdasinhstdasinhfstdasinhl(3)"
name: "stdasinhstdasinhfstdasinhl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdasinhstdasinhfstdasinhl/"
description: "std::asinh,std::asinhf,std::asinhl – std::asinh,std::asinhf,std::asinhl"
---

<p>std::asinh,std::asinhf,std::asinhl &#8211; std::asinh,std::asinhf,std::asinhl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float asinh ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float asinhf( float arg );<br />
double asinh ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double asinh ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double asinhl( long double arg );<br />
double asinh ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the inverse hyperbolic sine of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the inverse hyperbolic sine of arg (sinh-1<br />
(arg), or arsinh(arg)), is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if the argument is ±0 or ±∞, it is returned unmodified<br />
* if the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>Although the C standard (to which C++ refers for this function) names this function &quot;arc hyperbolic sine&quot;, the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is &quot;inverse hyperbolic sine&quot; (used by POSIX) or &quot;area hyperbolic sine&quot;. </p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;
int main()

{
    std::cout &lt;&lt; &quot;asinh(1) = &quot; &lt;&lt; std::asinh(1) &lt;&lt; '
'
              &lt;&lt; &quot;asinh(-1) = &quot; &lt;&lt; std::asinh(-1) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;asinh(+0) = &quot; &lt;&lt; std::asinh(+0.0) &lt;&lt; '
'
              &lt;&lt; &quot;asinh(-0) = &quot; &lt;&lt; std::asinh(-0.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-asinh/">asinh</a><code>(1)</code> = 0.881374<br />
&nbsp;<wbr>&nbsp;asinh(-1) = -0.881374<br />
&nbsp;<wbr>&nbsp;asinh(+0) = 0<br />
&nbsp;<wbr>&nbsp;asinh(-0) = -0</p>
<h2>See also</h2>
<p>acosh<br />
acoshf<br />
acoshl computes the inverse hyperbolic cosine (arcosh(x))<br />
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
sinh<br />
sinhf<br />
sinhl computes hyperbolic sine (sh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
asinh(std::complex) computes area hyperbolic sine of a complex number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Inverse_Hyperbolic_Sine.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
