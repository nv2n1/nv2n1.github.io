---
title: "stdabsfloatstdfabsstdfabsfstdfabsl(3)"
name: "stdabsfloatstdfabsstdfabsfstdfabsl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdabsfloatstdfabsstdfabsfstdfabsl/"
description: "std::abs(float),std::fabs,std::fabsf,std::fabsl – std::abs(float),std::fabs,std::fabsf,std::fabsl"
---

<p>std::abs(float),std::fabs,std::fabsf,std::fabsl &#8211; std::abs(float),std::fabs,std::fabsf,std::fabsl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
Defined in header &lt;cstdlib&gt; <i>(since C++17)</i><br />
float abs( float arg ); <code>(1)</code><br />
double abs( double arg ); <code>(2)</code><br />
long double abs( long double arg ); <code>(3)</code><br />
Defined in header &lt;cmath&gt;<br />
float fabs ( float arg );<br />
float fabsf( float arg ); <i>(since C++11)</i><br />
double fabs ( double arg ); <code>(4)</code> <code>(5)</code><br />
long double fabs ( long double arg );<br />
long double fabsl( long double arg ); <code>(6)</code> <i>(since C++11)</i><br />
double fabs ( IntegralType arg ); <code>(7)</code> <i>(since C++11)</i><br />
1-6) Computes the absolute value of a floating point value arg.<br />
7) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(5)</code> (the argument is cast to double).<br />
For integral arguments, the_integral_overloads_of_std::abs are likely better matches. If std::abs is called with an argument of type X such that std::is_unsigned&lt;X&gt;::value is true and X cannot be converted to int by integral_promotion, the program is ill-formed. <i>(since C++17)</i> </p>
<h2>Parameters</h2>
<p>arg &#8211; Value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If successful, returns the absolute value of arg (|arg|). The value returned is exact and does not depend on any rounding modes. </p>
<h2>Error handling</h2>
<p>This function is not subject to any of the error conditions specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is ±0, +0 is returned<br />
* If the argument is ±∞, +∞ is returned<br />
* If the argument is NaN, NaN is returned</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;
int main()

{
    std::cout &lt;&lt; &quot;abs(+3.0) = &quot; &lt;&lt; std::abs(+3.0) &lt;&lt; '
'
              &lt;&lt; &quot;abs(-3.0) = &quot; &lt;&lt; std::abs(-3.0) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;abs(-0.0) = &quot; &lt;&lt; std::abs(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;abs(-Inf) = &quot; &lt;&lt; std::abs(-INFINITY) &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;abs(+3.0) = 3<br />
&nbsp;<wbr>&nbsp;abs(-3.0) = 3<br />
&nbsp;<wbr>&nbsp;abs(-0.0) = 0<br />
&nbsp;<wbr>&nbsp;abs(-Inf) = inf </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
LWG_2735 C++11 std::abs was erroneously required to have overloads for integer types returning double removed the requirement</p>
<h2>See also</h2>
<p>abs(int)<br />
labs<br />
llabs computes absolute value of an integral value (|x|)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
copysign<br />
copysignf<br />
copysignl copies the sign of a floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
signbit checks if the given number is negative<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the magnitude of a complex number<br />
abs(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::abs to each element of valarray<br />
abs(std::valarray) <i>(function template)</i> </p>
