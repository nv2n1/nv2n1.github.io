---
title: "stdexpintstdexpintfstdexpintl(3)"
name: "stdexpintstdexpintfstdexpintl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexpintstdexpintfstdexpintl/"
description: "std::expint,std::expintf,std::expintl – std::expint,std::expintf,std::expintl"
---

<p>std::expint,std::expintf,std::expintl &#8211; std::expint,std::expintf,std::expintl</p>
<h2>Synopsis</h2>
<pre><code>double expint( double arg );

float expint( float arg );

long double expint( long double arg );  (1) (since C++17)

float expintf( float arg );

long double expintl( long double arg );

double expint( IntegralType arg );      (2) (since C++17)</code></pre>
<p>1) Computes the exponential_integral of arg.<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the exponential integral of arg, that is -∫∞<br />
-arg<br />
e-t<br />
t<br />
dt, is returned. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If the argument is ±0, -∞ is returned</p>
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
    std::cout &lt;&lt; &quot;Ei(0) = &quot; &lt;&lt; std::expint(0) &lt;&lt; '
'
              &lt;&lt; &quot;Ei(1) = &quot; &lt;&lt; std::expint(1) &lt;&lt; '
'
              &lt;&lt; &quot;Gompetz constant = &quot; &lt;&lt; -std::exp(1) * std::expint(-1) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Ei<code>(0)</code> = -inf<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-ei/">Ei</a><code>(1)</code> = 1.89512<br />
&nbsp;<wbr>&nbsp;Gompetz constant = 0.596347</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Exponential_Integral.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
