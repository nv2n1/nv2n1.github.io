---
title: "stdassoc_legendrestdassoc_legendrefstdassoc_legendrel(3)"
name: "stdassoc_legendrestdassoc_legendrefstdassoc_legendrel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdassoc_legendrestdassoc_legendrefstdassoc_legendrel/"
description: "std::assoc_legendre,std::assoc_legendref,std::assoc_legendrel – std::assoc_legendre,std::assoc_legendref,std::assoc_legendrel"
---

<p>std::assoc_legendre,std::assoc_legendref,std::assoc_legendrel &#8211; std::assoc_legendre,std::assoc_legendref,std::assoc_legendrel</p>
<h2>Synopsis</h2>
<pre><code>double assoc_legendre(unsigned int n, unsigned int m, double x);

float assoc_legendre(unsigned int n, unsigned int m, float x);

long double assoc_legendre(unsigned int n, unsigned int m, long double x);
(1)(since C++ 17)

    float assoc_legendref(unsigned int n, unsigned int m, float x);

long double assoc_legendrel(unsigned int n, unsigned int m, long double x);

double assoc_legendre(unsigned int n, unsigned int m, IntegralType x);
(2)(since C++ 17)</code></pre>
<p>1) Computes the associated_Legendre_polynomials of the degree n, order m, and argument x<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>n &#8211; the degree of the polynomial, a value of unsigned integer type<br />
m &#8211; the order of the polynomial, a value of unsigned integer type<br />
x &#8211; the argument, a value of a floating-point or integral type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the associated Legendre polynomial \(\mathsf{P}_n^m\)Pm<br />
n of x, that is \((1 &#8211; x^2) ^ {m/2} \: rac{ \mathsf{d} ^ m}{ \mathsf{d}x ^ m} \, \mathsf{P}_n(x)\)(1-x2<br />
)m/2<br />
dm<br />
dxm<br />
P<br />
n(x), is returned (where \(\mathsf{P}_n(x)\)P<br />
n(x) is the unassociated Legendre polynomial, std::legendre(n, x)).<br />
Note that the Condon-Shortley_phase_term \((-1)^m\)(-1)m<br />
is omitted from this definition. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If |x| &gt; 1, a domain error may occur<br />
* If n is greater or equal to 128, the behavior is implementation-defined.</p>
<h2>Notes</h2>
<p>Implementations that do not support C++17, but support ISO_29124:2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.<br />
Implementations that do not support ISO 29124:2010 but support TR 19768:2007 (TR1), provide this function in the header tr1/cmath and namespace std::tr1<br />
An implementation of this function is also available_in_boost.math as boost::math::legendre_p, except that the boost.math definition includes the Condon-Shortley phase term.<br />
The first few associated Legendre polynomials are: * assoc_legendre(0, 0, x) = 1</p>
<p>* assoc_legendre(1, 0, x) = x</p>
<p>* assoc_legendre(1, 1, x) = (1-x2</p>
<p>)1/2</p>
<p>* assoc_legendre(2, 0, x) =<br />
&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;2 (3&#215;2</p>
<p>-1)</p>
<p>* assoc_legendre(2, 1, x) = 3x(1-x2</p>
<p>)1/2</p>
<p>* assoc_legendre(2, 2, x) = 3(1-x2</p>
<p>)</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

double P20(double x)
{
    return 0.5 * (3 * x * x - 1);
}

double P21(double x)
{
    return 3.0 * x * std::sqrt(1 - x * x);
}

double P22(double x)
{
    return 3 * (1 - x * x);
}

int main()

{
    // spot-checks
    std::cout &lt;&lt; std::assoc_legendre(2, 0, 0.5) &lt;&lt; '=' &lt;&lt; P20(0.5) &lt;&lt; '
'
              &lt;&lt; std::assoc_legendre(2, 1, 0.5) &lt;&lt; '=' &lt;&lt; P21(0.5) &lt;&lt; '
'
              &lt;&lt; std::assoc_legendre(2, 2, 0.5) &lt;&lt; '=' &lt;&lt; P22(0.5) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;-0.125=-0.125<br />
&nbsp;<wbr>&nbsp;1.29904=1.29904<br />
&nbsp;<wbr>&nbsp;2.25=2.25</p>
<h2>See also</h2>
<p>legendre<br />
legendref<br />
legendrel Legendre polynomials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Associated_Legendre_Polynomial.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
