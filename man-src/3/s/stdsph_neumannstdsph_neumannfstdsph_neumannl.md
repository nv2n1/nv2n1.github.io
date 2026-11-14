---
title: "stdsph_neumannstdsph_neumannfstdsph_neumannl(3)"
name: "stdsph_neumannstdsph_neumannfstdsph_neumannl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsph_neumannstdsph_neumannfstdsph_neumannl/"
description: "std::sph_neumann,std::sph_neumannf,std::sph_neumannl – std::sph_neumann,std::sph_neumannf,std::sph_neumannl"
---

<p>std::sph_neumann,std::sph_neumannf,std::sph_neumannl &#8211; std::sph_neumann,std::sph_neumannf,std::sph_neumannl</p>
<h2>Synopsis</h2>
<pre><code>double sph_neumann ( unsigned n, double x );

float sph_neumann ( unsigned n, float x );

long double sph_neumann ( unsigned n, long double x ); (1) (since C++17)

float sph_neumannf( unsigned n, float x );

long double sph_neumannl( unsigned n, long double x );

double sph_neumann( unsigned n, IntegralType x );      (2) (since C++17)</code></pre>
<p>1) Computes the spherical_Bessel_function_of_the_second_kind, also known as the spherical Neumann function, of n and x.<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>n &#8211; the order of the function<br />
x &#8211; the argument of the function</p>
<h2>Return value</h2>
<p>If no errors occur, returns the value of the spherical Bessel function of the second kind (spherical Neumann function) of n and x, that is n<br />
n(x) = (π/2x)1/2<br />
N<br />
n+1/2(x) where N<br />
n(x) is std::cyl_neumann(n,x) and x≥0 </p>
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
    std::cout &lt;&lt; &quot;n_1(&quot; &lt;&lt; x &lt;&lt; &quot;) = &quot; &lt;&lt; std::sph_neumann(1, x) &lt;&lt; '
';
    // exact solution for n_1
    std::cout &lt;&lt; &quot;-(cos x)/x^2 - (sin x)/x = &quot;
              &lt;&lt; -std::cos(x) / (x * x) - std::sin(x) / x &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;n_1(1.2345) = -0.981201<br />
&nbsp;<wbr>&nbsp;-(cos x)/x^2 &#8211; (sin x)/x = -0.981201</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Spherical_Bessel_Function_of_the_Second_Kind.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
<h2>See also</h2>
<p>cyl_neumann<br />
cyl_neumannf<br />
cyl_neumannl cylindrical Neumann functions<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
sph_bessel<br />
sph_besself<br />
sph_bessell spherical Bessel functions (of the first kind)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
