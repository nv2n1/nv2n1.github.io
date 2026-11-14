---
title: "stdtanhstdtanhfstdtanhl(3)"
name: "stdtanhstdtanhfstdtanhl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtanhstdtanhfstdtanhl/"
description: "std::tanh,std::tanhf,std::tanhl – std::tanh,std::tanhf,std::tanhl"
---

<p>std::tanh,std::tanhf,std::tanhl &#8211; std::tanh,std::tanhf,std::tanhl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float tanh ( float arg );<br />
float tanhf( float arg ); <i>(since C++11)</i><br />
double tanh ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double tanh ( long double arg );<br />
long double tanhl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double tanh ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the hyperbolic tangent of arg<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the hyperbolic tangent of arg (tanh(arg), or<br />
earg<br />
-e-arg<br />
earg<br />
+e-arg<br />
) is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if the argument is ±0, ±0 is returned<br />
* If the argument is ±∞, ±1 is returned<br />
* if the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>POSIX_specifies that in case of underflow, arg is returned unmodified, and if that is not supported, and implementation-defined value no greater than DBL_MIN, FLT_MIN, and LDBL_MIN is returned. </p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;
int main()

{
    std::cout &lt;&lt; &quot;tanh(1) = &quot; &lt;&lt; std::tanh(1) &lt;&lt; '
'
              &lt;&lt; &quot;tanh(-1) = &quot; &lt;&lt; std::tanh(-1) &lt;&lt; '
'
              &lt;&lt; &quot;tanh(0.1)*sinh(0.2)-cosh(0.2) = &quot;
              &lt;&lt; std::tanh(0.1) * std::sinh(0.2) - std::cosh(0.2) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;tanh(+0) = &quot; &lt;&lt; std::tanh(+0.0) &lt;&lt; '
'
              &lt;&lt; &quot;tanh(-0) = &quot; &lt;&lt; std::tanh(-0.0) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-tanh/">tanh</a><code>(1)</code> = 0.761594<br />
&nbsp;<wbr>&nbsp;tanh(-1) = -0.761594<br />
&nbsp;<wbr>&nbsp;tanh(0.1)*sinh(0.2)-cosh(0.2) = -1<br />
&nbsp;<wbr>&nbsp;tanh(+0) = 0<br />
&nbsp;<wbr>&nbsp;tanh(-0) = -0</p>
<h2>See also</h2>
<p>sinh<br />
sinhf<br />
sinhl computes hyperbolic sine (sh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
cosh<br />
coshf<br />
coshl computes hyperbolic cosine (ch(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
atanh<br />
atanhf<br />
atanhl computes the inverse hyperbolic tangent (artanh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic tangent of a complex number<br />
tanh(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::tanh to each element of valarray<br />
tanh(std::valarray) <i>(function template)</i> </p>
