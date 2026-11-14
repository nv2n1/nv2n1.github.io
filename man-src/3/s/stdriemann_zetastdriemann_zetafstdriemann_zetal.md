---
title: "stdriemann_zetastdriemann_zetafstdriemann_zetal(3)"
name: "stdriemann_zetastdriemann_zetafstdriemann_zetal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdriemann_zetastdriemann_zetafstdriemann_zetal/"
description: "std::riemann_zeta,std::riemann_zetaf,std::riemann_zetal – std::riemann_zeta,std::riemann_zetaf,std::riemann_zetal"
---

<p>std::riemann_zeta,std::riemann_zetaf,std::riemann_zetal &#8211; std::riemann_zeta,std::riemann_zetaf,std::riemann_zetal</p>
<h2>Synopsis</h2>
<pre><code>double riemann_zeta( double arg );

float riemann_zeta( float arg );

long double riemann_zeta( long double arg );  (1) (since C++17)

float riemann_zetaf( float arg );

long double riemann_zetal( long double arg );

double riemann_zeta( IntegralType arg );      (2) (since C++17)</code></pre>
<p>1) Computes the Riemann_zeta_function of arg.<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or integral type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the Riemann zeta function of arg, ζ(arg), defined for the entire real axis:<br />
&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;1-21-arg Σ∞</p>
<p>n=1(-1)n-1</p>
<p>n-arg</p>
<p>* For arg&lt;0, 2arg</p>
<p>πarg-1</p>
<p>sin(<br />
&nbsp;<wbr>&nbsp;πarg<br />
&nbsp;<wbr>&nbsp;2<br />
&nbsp;<wbr>&nbsp;)Γ(1−arg)ζ(1−arg) </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported</p>
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
    // spot checks for well-known values
    std::cout &lt;&lt; &quot;ζ(-1) = &quot; &lt;&lt; std::riemann_zeta(-1) &lt;&lt; '
'
              &lt;&lt; &quot;ζ(0) = &quot; &lt;&lt; std::riemann_zeta(0) &lt;&lt; '
'
              &lt;&lt; &quot;ζ(1) = &quot; &lt;&lt; std::riemann_zeta(1) &lt;&lt; '
'
              &lt;&lt; &quot;ζ(0.5) = &quot; &lt;&lt; std::riemann_zeta(0.5) &lt;&lt; '
'
              &lt;&lt; &quot;ζ(2) = &quot; &lt;&lt; std::riemann_zeta(2) &lt;&lt; ' '
              &lt;&lt; &quot;(π²/6 = &quot; &lt;&lt; std::pow(std::acos(-1), 2) / 6 &lt;&lt; &quot;)
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;ζ(-1) = -0.0833333<br />
&nbsp;<wbr>&nbsp;ζ<code>(0)</code> = -0.5<br />
&nbsp;<wbr>&nbsp;ζ<code>(1)</code> = inf<br />
&nbsp;<wbr>&nbsp;ζ(0.5) = -1.46035<br />
&nbsp;<wbr>&nbsp;ζ<code>(2)</code> = 1.64493 (π²/6 = 1.64493)</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Riemann_Zeta_Function.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
