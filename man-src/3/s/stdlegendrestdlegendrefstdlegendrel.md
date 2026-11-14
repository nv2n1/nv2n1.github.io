---
title: "stdlegendrestdlegendrefstdlegendrel(3)"
name: "stdlegendrestdlegendrefstdlegendrel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlegendrestdlegendrefstdlegendrel/"
description: "std::legendre,std::legendref,std::legendrel – std::legendre,std::legendref,std::legendrel"
---

<p>std::legendre,std::legendref,std::legendrel &#8211; std::legendre,std::legendref,std::legendrel</p>
<h2>Synopsis</h2>
<pre><code>double legendre(unsigned int n, double x);

float legendre(unsigned int n, float x);

long double legendre(unsigned int n, long double x);
(1)(since C++ 17)

    float legendref(unsigned int n, float x);

long double legendrel(unsigned int n, long double x);

double legendre(unsigned int n, IntegralType x);
(2)(since C++ 17)</code></pre>
<p>1) Computes the unassociated Legendre_polynomials of the degree n and argument x<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>n &#8211; the degree of the polynomial<br />
x &#8211; the argument, a value of a floating-point or integral type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the order-n unassociated Legendre polynomial of x, that is \(\mathsf{P}_n(x) = rac{1}{2^n n!} rac{\mathsf{d}^n}{\mathsf{d}x^n} (x^2-1)^n \)<br />
1<br />
2n<br />
n!<br />
dn<br />
dxn<br />
(x2<br />
-1)n<br />
, is returned. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* The function is not required to be defined for |x|&gt;1<br />
* If n is greater or equal than 128, the behavior is implementation-defined</p>
<h2>Notes</h2>
<p>Implementations that do not support C++17, but support ISO_29124:2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.<br />
Implementations that do not support ISO 29124:2010 but support TR 19768:2007 (TR1), provide this function in the header tr1/cmath and namespace std::tr1<br />
An implementation of this function is also available_in_boost.math<br />
The first few Legendre polynomials are: * legendre(0, x) = 1</p>
<p>* legendre(1, x) = x</p>
<p>* legendre(2, x) =<br />
&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;2<br />
&nbsp;<wbr>&nbsp;(3&#215;2<br />
&nbsp;<wbr>&nbsp;-1)<br />
* legendre(3, x) =<br />
&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;2<br />
&nbsp;<wbr>&nbsp;(5&#215;3<br />
&nbsp;<wbr>&nbsp;-3x)<br />
* legendre(4, x) =<br />
&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;8<br />
&nbsp;<wbr>&nbsp;(35&#215;4<br />
&nbsp;<wbr>&nbsp;-30&#215;2<br />
&nbsp;<wbr>&nbsp;+3) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

double P3(double x)
{
    return 0.5 * (5 * std::pow(x, 3) - 3 * x);
}

double P4(double x)
{
    return 0.125 * (35 * std::pow(x, 4) - 30 * x * x + 3);
}

int main()

{
    // spot-checks
    std::cout &lt;&lt; std::legendre(3, 0.25) &lt;&lt; '=' &lt;&lt; P3(0.25) &lt;&lt; '
'
              &lt;&lt; std::legendre(4, 0.25) &lt;&lt; '=' &lt;&lt; P4(0.25) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;-0.335938=-0.335938<br />
&nbsp;<wbr>&nbsp;0.157715=0.157715</p>
<h2>See also</h2>
<p>laguerre<br />
laguerref<br />
laguerrel Laguerre polynomials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
hermite<br />
hermitef<br />
hermitel Hermite polynomials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Legendre_Polynomial.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
