---
title: "stdhermitestdhermitefstdhermitel(3)"
name: "stdhermitestdhermitefstdhermitel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhermitestdhermitefstdhermitel/"
description: "std::hermite,std::hermitef,std::hermitel – std::hermite,std::hermitef,std::hermitel"
---

<p>std::hermite,std::hermitef,std::hermitel &#8211; std::hermite,std::hermitef,std::hermitel</p>
<h2>Synopsis</h2>
<pre><code>double hermite(unsigned int n, double x);

float hermite(unsigned int n, float x);

long double hermite(unsigned int n, long double x);
(1)(since C++ 17)

    float hermitef(unsigned int n, float x);

long double hermitel(unsigned int n, long double x);

double hermite(unsigned int n, IntegralType x);
(2)(since C++ 17)</code></pre>
<p>1) Computes the (physicist&#8217;s) Hermite_polynomials of the degree n and argument x<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>n &#8211; the degree of the polynomial<br />
x &#8211; the argument, a value of a floating-point or integral type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the order-nHermite polynomial of x, that is (-1)n<br />
ex2<br />
dn<br />
dxn<br />
e-x2<br />
, is returned. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If n is greater or equal than 128, the behavior is implementation-defined</p>
<h2>Notes</h2>
<p>Implementations that do not support C++17, but support ISO_29124:2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.</p>
<p>Implementations that do not support ISO 29124:2010 but support TR 19768:2007 (TR1), provide this function in the header tr1/cmath and namespace std::tr1</p>
<p>An implementation of this function is also available_in_boost.math</p>
<p>The Hermite polynomials are the polynomial solutions of the equation u,,</p>
<p>-2xu,</p>
<p>= -2nu</p>
<p>The first few are:<br />
* hermite(0, x) = 1</p>
<p>* hermite(1, x) = 2x</p>
<p>* hermite(2, x) = 4&#215;2</p>
<p>-2</p>
<p>* hermite(3, x) = 8&#215;3</p>
<p>-12x</p>
<p>* hermite(4, x) = 16&#215;4</p>
<p>-48&#215;2</p>
<p>+12</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

double H3(double x)
{
    return 8 * std::pow(x, 3) - 12 * x;
}

double H4(double x)
{
    return 16 * std::pow(x, 4) - 48 * x * x + 12;
}

int main()

{
    // spot-checks
    std::cout &lt;&lt; std::hermite(3, 10) &lt;&lt; '=' &lt;&lt; H3(10) &lt;&lt; '
'
              &lt;&lt; std::hermite(4, 10) &lt;&lt; '=' &lt;&lt; H4(10) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;7880=7880<br />
&nbsp;<wbr>&nbsp;155212=155212</p>
<h2>See also</h2>
<p>laguerre<br />
laguerref<br />
laguerrel Laguerre polynomials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
legendre<br />
legendref<br />
legendrel Legendre polynomials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;&quot;Hermite_Polynomial.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
