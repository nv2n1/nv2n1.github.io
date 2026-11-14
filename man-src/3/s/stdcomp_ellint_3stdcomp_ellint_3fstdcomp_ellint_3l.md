---
title: "stdcomp_ellint_3stdcomp_ellint_3fstdcomp_ellint_3l(3)"
name: "stdcomp_ellint_3stdcomp_ellint_3fstdcomp_ellint_3l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcomp_ellint_3stdcomp_ellint_3fstdcomp_ellint_3l/"
description: "std::comp_ellint_3,std::comp_ellint_3f,std::comp_ellint_3l – std::comp_ellint_3,std::comp_ellint_3f,std::comp_ellint_3l"
---

<p>std::comp_ellint_3,std::comp_ellint_3f,std::comp_ellint_3l &#8211; std::comp_ellint_3,std::comp_ellint_3f,std::comp_ellint_3l</p>
<h2>Synopsis</h2>
<pre><code>double comp_ellint_3( double k, double ν );

float comp_ellint_3f( float k, float ν );                  (1) (since C++17)

long double comp_ellint_3l( long double k, long double ν );

Promoted comp_ellint_3( Arithmetic k, Arithmetic ν );      (2) (since C++17)</code></pre>
<p>1) Computes the complete_elliptic_integral_of_the_third_kind of the arguments k and ν.<br />
2) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by <code>(1)</code>. If any argument has integral_type, it is cast to double. If any argument is long double, then the return type Promoted is also long double, otherwise the return type is always double. </p>
<h2>Parameters</h2>
<p>k &#8211; elliptic modulus or eccentricity (a value of a floating-point or integral type)<br />
ν- elliptic characteristic (a value of floating-point or integral type)</p>
<h2>Return value</h2>
<p>If no errors occur, value of the complete elliptic integral of the third kind of k and ν, that is std::ellint_3(k,ν,π/2), is returned. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If |k|&gt;1, a domain error may occur</p>
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
    double hpi = std::acos(-1) / 2;
    std::cout &lt;&lt; &quot;Π(0.5,0) = &quot; &lt;&lt; std::comp_ellint_3(0.5, 0) &lt;&lt; '
'
              &lt;&lt; &quot;K(0.5) = &quot; &lt;&lt; std::comp_ellint_1(0.5) &lt;&lt; '
'
              &lt;&lt; &quot;Π(0,0) = &quot; &lt;&lt; std::comp_ellint_3(0, 0) &lt;&lt; '
'
              &lt;&lt; &quot;π/2 = &quot; &lt;&lt; hpi &lt;&lt; '
'
              &lt;&lt; &quot;Π(0.5,1) = &quot; &lt;&lt; std::comp_ellint_3(0.5, 1) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Π(0.5,0) = 1.68575<br />
&nbsp;<wbr>&nbsp;K(0.5) = 1.68575<br />
&nbsp;<wbr>&nbsp;Π(0,0) = 1.5708<br />
&nbsp;<wbr>&nbsp;π/2 = 1.5708<br />
&nbsp;<wbr>&nbsp;Π(0.5,1) = inf</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Elliptic_Integral_of_the_Second_Kind.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
<h2>See also</h2>
<p>ellint_3<br />
ellint_3f<br />
ellint_3l (incomplete) elliptic integral of the third kind<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
