---
title: "stdassoc_laguerrestdassoc_laguerrefstdassoc_laguerrel(3)"
name: "stdassoc_laguerrestdassoc_laguerrefstdassoc_laguerrel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdassoc_laguerrestdassoc_laguerrefstdassoc_laguerrel/"
description: "std::assoc_laguerre,std::assoc_laguerref,std::assoc_laguerrel – std::assoc_laguerre,std::assoc_laguerref,std::assoc_laguerrel"
---

<p>std::assoc_laguerre,std::assoc_laguerref,std::assoc_laguerrel &#8211; std::assoc_laguerre,std::assoc_laguerref,std::assoc_laguerrel</p>
<h2>Synopsis</h2>
<pre><code>double assoc_laguerre(unsigned int n, unsigned int m, double x);

float assoc_laguerre(unsigned int n, unsigned int m, float x);

long double assoc_laguerre(unsigned int n, unsigned int m, long double x);
(1)(since C++ 17)

    float assoc_laguerref(unsigned int n, unsigned int m, float x);

long double assoc_laguerrel(unsigned int n, unsigned int m, long double x);

double assoc_laguerre(unsigned int n, unsigned int m, IntegralType x);
(2)(since C++ 17)</code></pre>
<p>1) Computes the associated_Laguerre_polynomials of the degree n, order m, and argument x<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>n &#8211; the degree of the polymonial, a value of unsigned integer type<br />
m &#8211; the order of the polynomial, a value of unsigned integer type<br />
x &#8211; the argument, a value of a floating-point or integral type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the associated Laguerre polynomial of x, that is \((-1)^m \: rac{ \mathsf{d} ^ m}{ \mathsf{d}x ^ m} \, \mathsf{L}_{n+m}(x)\)(-1)m<br />
dm<br />
dxm<br />
L<br />
n+m(x), is returned (where \(\mathsf{L}_{n+m}(x)\)L<br />
n+m(x) is the unassociated Laguerre polynomial, std::laguerre(n+m, x)). </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If x is negative, a domain error may occur<br />
* If n or m is greater or equal to 128, the behavior is implementation-defined.</p>
<h2>Notes</h2>
<p>Implementations that do not support C++ 17, but support ISO_29124 : 2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.</p>
<p>                                                                                                                                                                                               Implementations that do not support ISO 29124 : 2010 but support TR 19768 : 2007(TR1),<br />
    provide this function in the header tr1 / cmath and namespace std::tr1</p>
<p>                                                  An implementation of this function is also available_in_boost.math</p>
<p>                                                      The associated Laguerre polynomials are the polynomial solutions of the equation \(x\ddot{y} + (m + 1 &#8211; x)\dot{y} + ny = 0\) xy,<br />
    ,</p>
<p>    +(m + 1 &#8211; x) y,</p>
<p>    +ny = 0</p>
<p>    The first few are : *assoc_laguerre(0, m, x) = 1</p>
<p>                                                   * assoc_laguerre(1, m, x) = -x + m + 1</p>
<p>                                                                                            * assoc_laguerre(2, m, x) =<br />
&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;2<br />
&nbsp;<wbr>&nbsp;[x2<br />
&nbsp;<wbr>&nbsp;-2(m+2)x+(m+1)(m+2)]<br />
* assoc_laguerre(3, m, x) =<br />
&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;6<br />
&nbsp;<wbr>&nbsp;[-x3<br />
&nbsp;<wbr>&nbsp;-3(m+3)x2<br />
&nbsp;<wbr>&nbsp;-3(m+2)(m+3)x+(m+1)(m+2)(m+3)] </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

double L1(unsigned m, double x)
{
    return -x + m + 1;
}

double L2(unsigned m, double x)
{
    return 0.5 * (x * x - 2 * (m + 2) * x + (m + 1) * (m + 2));
}

int main()

{
    // spot-checks
    std::cout &lt;&lt; std::assoc_laguerre(1, 10, 0.5) &lt;&lt; '=' &lt;&lt; L1(10, 0.5) &lt;&lt; '
'
              &lt;&lt; std::assoc_laguerre(2, 10, 0.5) &lt;&lt; '=' &lt;&lt; L2(10, 0.5) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;10.5=10.5<br />
&nbsp;<wbr>&nbsp;60.125=60.125</p>
<h2>See also</h2>
<p>laguerre<br />
laguerref<br />
laguerrel Laguerre polynomials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Associated_Laguerre_Polynomial.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
