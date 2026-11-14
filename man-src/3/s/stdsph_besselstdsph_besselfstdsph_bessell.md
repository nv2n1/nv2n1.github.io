---
title: "stdsph_besselstdsph_besselfstdsph_bessell(3)"
name: "stdsph_besselstdsph_besselfstdsph_bessell"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsph_besselstdsph_besselfstdsph_bessell/"
description: "std::sph_bessel,std::sph_besself,std::sph_bessell – std::sph_bessel,std::sph_besself,std::sph_bessell"
---

<p>std::sph_bessel,std::sph_besself,std::sph_bessell &#8211; std::sph_bessel,std::sph_besself,std::sph_bessell</p>
<h2>Synopsis</h2>
<pre><code>double sph_bessel ( unsigned n, double x );

float sph_bessel ( unsigned n, float x );

long double sph_bessel ( unsigned n, long double x ); (1) (since C++17)

float sph_besself( unsigned n, float x );

long double sph_bessell( unsigned n, long double x );

double sph_bessel( unsigned n, IntegralType x );      (2) (since C++17)</code></pre>
<p>1) Computes the spherical_Bessel_function_of_the_first_kind of n and x.<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>n &#8211; the order of the function<br />
x &#8211; the argument of the function</p>
<h2>Return value</h2>
<p>If no errors occur, returns the value of the spherical Bessel function of the first kind of n and x, that is j<br />
n(x) = (π/2x)1/2<br />
J<br />
n+1/2(x) where J<br />
n(x) is std::cyl_bessel_j(n,x) and x≥0 </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If n&gt;=128, the behavior is implementation-defined</p>
<h2>Notes</h2>
<p>Implementations that do not support C++17, but support ISO_29124:2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.<br />
Implementations that do not support ISO 29124:2010 but support TR 19768:2007 (TR1), provide this function in the header tr1/cmath and namespace std::tr1<br />
An implementation of this function is also available_in_boost.math </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

int main()

{
    // spot check for n == 1
    double x = 1.2345;
    std::cout &lt;&lt; &quot;j_1(&quot; &lt;&lt; x &lt;&lt; &quot;) = &quot; &lt;&lt; std::sph_bessel(1, x) &lt;&lt; '
';
    // exact solution for j_1
    std::cout &lt;&lt; &quot;(sin x)/x^2 - (cos x)/x = &quot; &lt;&lt; std::sin(x) / (x * x) - std::cos(x) / x &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;j_1(1.2345) = 0.352106<br />
&nbsp;<wbr>&nbsp;(sin x)/x^2 &#8211; (cos x)/x = 0.352106</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Spherical_Bessel_Function_of_the_First_Kind.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
<h2>See also</h2>
<p>cyl_bessel_j<br />
cyl_bessel_jf<br />
cyl_bessel_jl cylindrical Bessel functions (of the first kind)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
sph_neumann<br />
sph_neumannf<br />
sph_neumannl spherical Neumann functions<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
