---
title: "stdlaguerrestdlaguerrefstdlaguerrel(3)"
name: "stdlaguerrestdlaguerrefstdlaguerrel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlaguerrestdlaguerrefstdlaguerrel/"
description: "std::laguerre,std::laguerref,std::laguerrel – std::laguerre,std::laguerref,std::laguerrel"
---

<p>std::laguerre,std::laguerref,std::laguerrel &#8211; std::laguerre,std::laguerref,std::laguerrel</p>
<h2>Synopsis</h2>
<pre><code>double laguerre(unsigned int n, double x);

float laguerre(unsigned int n, float x);

long double laguerre(unsigned int n, long double x);
(1)(since C++ 17)

    float laguerref(unsigned int n, float x);

long double laguerrel(unsigned int n, long double x);

double laguerre(unsigned int n, IntegralType x);
(2)(since C++ 17)</code></pre>
<p>1) Computes the non-associated Laguerre_polynomials of the degree n and argument x<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>n &#8211; the degree of the polymonial, a value of unsigned integer type<br />
x &#8211; the argument, a value of a floating-point or integral type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the nonassociated Laguerre polynomial of x, that is<br />
ex<br />
n!<br />
dn<br />
dxn<br />
(xn<br />
e-x), is returned. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If x is negative, a domain error may occur<br />
* If n is greater or equal than 128, the behavior is implementation-defined</p>
<h2>Notes</h2>
<p>Implementations that do not support C++17, but support ISO_29124:2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.</p>
<p>Implementations that do not support ISO 29124:2010 but support TR 19768:2007 (TR1), provide this function in the header tr1/cmath and namespace std::tr1</p>
<p>An implementation of this function is also available_in_boost.math</p>
<p>The Laguerre polynomials are the polynomial solutions of the equation xy,,</p>
<p>+(1-x)y,</p>
<p>+ny = 0</p>
<p>The first few are:<br />
* laguerre(0, x) = 1</p>
<p>* laguerre(1, x) = -x + 1</p>
<p>* laguerre(2, x) =<br />
&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;2<br />
&nbsp;<wbr>&nbsp;[x2<br />
&nbsp;<wbr>&nbsp;-4x+2]<br />
* laguerre(3, x) =<br />
&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;6<br />
&nbsp;<wbr>&nbsp;[-x3<br />
&nbsp;<wbr>&nbsp;-9&#215;2<br />
&nbsp;<wbr>&nbsp;-18x+6] </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#define __STDCPP_WANT_MATH_SPEC_FUNCS__ 1

#include &lt;cmath&gt;

#include &lt;iostream&gt;

double L1(double x)
{
    return -x + 1;
}

double L2(double x)
{
    return 0.5 * (x * x - 4 * x + 2);
}

int main()

{
    // spot-checks
    std::cout &lt;&lt; std::laguerre(1, 0.5) &lt;&lt; '=' &lt;&lt; L1(0.5) &lt;&lt; '
'
              &lt;&lt; std::laguerre(2, 0.5) &lt;&lt; '=' &lt;&lt; L2(0.5) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0.5=0.5<br />
&nbsp;<wbr>&nbsp;0.125=0.125</p>
<h2>See also</h2>
<p>assoc_laguerre<br />
assoc_laguerref<br />
assoc_laguerrel associated Laguerre polynomials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Laguerre_Polynomial.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
