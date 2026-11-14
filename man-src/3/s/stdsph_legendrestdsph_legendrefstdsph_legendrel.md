---
title: "stdsph_legendrestdsph_legendrefstdsph_legendrel(3)"
name: "stdsph_legendrestdsph_legendrefstdsph_legendrel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsph_legendrestdsph_legendrefstdsph_legendrel/"
description: "std::sph_legendre,std::sph_legendref,std::sph_legendrel – std::sph_legendre,std::sph_legendref,std::sph_legendrel"
---

<p>std::sph_legendre,std::sph_legendref,std::sph_legendrel &#8211; std::sph_legendre,std::sph_legendref,std::sph_legendrel</p>
<h2>Synopsis</h2>
<pre><code>double sph_legendre ( unsigned l, unsigned m, double θ );

float sph_legendre ( unsigned l, unsigned m, float θ );

long double sph_legendre ( unsigned l, unsigned m, long double θ );(1) (since C++17)

float sph_legendref( unsigned l, unsigned m, float θ );

long double sph_legendrel( unsigned l, unsigned m, long double θ );

double sph_legendre ( unsigned l, unsigned m, IntegralType θ );    (2) (since C++17)</code></pre>
<p>1) Computes the spherical associated Legendre function of degree l, order m, and polar angle θ.<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>l &#8211; degree<br />
m &#8211; order<br />
θ- polar angle, measured in radians</p>
<h2>Return value</h2>
<p>If no errors occur, returns the value of the spherical associated Legendre function (that is, spherical harmonic with ϕ = 0) of l, m, and θ, where the spherical harmonic function is defined as Ym<br />
l(θ,ϕ) = (-1)m<br />
[<br />
(2l+1)(l-m)!<br />
4π(l+m)!<br />
]1/2<br />
Pm<br />
l(cosθ)eimϕ<br />
where Pm<br />
l(x) is std::assoc_legendre(l,m,x)) and |m|≤l<br />
Note that the Condon-Shortley_phase_term (-1)m<br />
is included in this definition because it is omitted from the definition of Pm<br />
l in std::assoc_legendre. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If l≥128, the behavior is implementation-defined</p>
<h2>Notes</h2>
<p>Implementations that do not support C++17, but support ISO_29124:2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.<br />
Implementations that do not support ISO 29124:2010 but support TR 19768:2007 (TR1), provide this function in the header tr1/cmath and namespace std::tr1<br />
An implementation of the spherical harmonic function is available_in_boost.math, and it reduces to this function when called with the parameter phi set to zero. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

int main()

{
    // spot check for l=3, m=0
    double x = 1.2345;
    std::cout &lt;&lt; &quot;Y_3^0(&quot; &lt;&lt; x &lt;&lt; &quot;) = &quot; &lt;&lt; std::sph_legendre(3, 0, x) &lt;&lt; '
';
    // exact solution
    double pi = std::acos(-1);
    std::cout &lt;&lt; &quot;exact solution = &quot;
              &lt;&lt; 0.25 * std::sqrt(7 / pi) * (5 * std::pow(std::cos(x), 3) - 3 * std::cos(x))
              &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Y_3^0(1.2345) = -0.302387<br />
&nbsp;<wbr>&nbsp;exact solution = -0.302387</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Spherical_Harmonic.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
<h2>See also</h2>
<p>assoc_legendre<br />
assoc_legendref<br />
assoc_legendrel associated Legendre polynomials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
