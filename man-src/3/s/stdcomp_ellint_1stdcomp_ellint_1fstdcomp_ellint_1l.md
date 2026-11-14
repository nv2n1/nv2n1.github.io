---
title: "stdcomp_ellint_1stdcomp_ellint_1fstdcomp_ellint_1l(3)"
name: "stdcomp_ellint_1stdcomp_ellint_1fstdcomp_ellint_1l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcomp_ellint_1stdcomp_ellint_1fstdcomp_ellint_1l/"
description: "std::comp_ellint_1,std::comp_ellint_1f,std::comp_ellint_1l – std::comp_ellint_1,std::comp_ellint_1f,std::comp_ellint_1l"
---

<p>std::comp_ellint_1,std::comp_ellint_1f,std::comp_ellint_1l &#8211; std::comp_ellint_1,std::comp_ellint_1f,std::comp_ellint_1l</p>
<h2>Synopsis</h2>
<pre><code>double comp_ellint_1( double k );

float comp_ellint_1( float k );

long double comp_ellint_1( long double k );  (1) (since C++17)

float comp_ellint_1f( float k );

long double comp_ellint_1l( long double k );

double comp_ellint_1( IntegralType k );      (2) (since C++17)</code></pre>
<p>1) Computes the complete_elliptic_integral_of_the_first_kind of k.<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>k &#8211; elliptic modulus or eccentricity (a value of a floating-point or integral type)</p>
<h2>Return value</h2>
<p>If no errors occur, value of the complete elliptic integral of the first kind of k, that is ellint_1(k,π/2), is returned. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If |k|&gt;1, a domain error may occur</p>
<h2>Notes</h2>
<p>Implementations that do not support C++17, but support ISO_29124:2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.<br />
Implementations that do not support ISO 29124:2010 but support TR 19768:2007 (TR1), provide this function in the header tr1/cmath and namespace std::tr1<br />
An implementation of this function is also available_in_boost.math<br />
The period_of_a_pendulum of length l, given acceleration due to gravity g, and initial angle θ equals 4<br />
√<br />
l/gK(sin2<br />
(θ/2)), where K is std::comp_ellint_1. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

int main()

{
    double hpi = std::acos(-1) / 2;
    std::cout &lt;&lt; &quot;K(0) = &quot; &lt;&lt; std::comp_ellint_1(0) &lt;&lt; '
'
              &lt;&lt; &quot;π/2 = &quot; &lt;&lt; hpi &lt;&lt; '
'
              &lt;&lt; &quot;K(0.5) = &quot; &lt;&lt; std::comp_ellint_1(0.5) &lt;&lt; '
'
              &lt;&lt; &quot;F(0.5, π/2) = &quot; &lt;&lt; std::ellint_1(0.5, hpi) &lt;&lt; '
';
    std::cout &lt;&lt; &quot;Period of a pendulum length 1 m at 90 degree initial angle is &quot;
              &lt;&lt; 4 * std::sqrt(1 / 9.80665) *
                     std::comp_ellint_1(std::pow(std::sin(hpi / 2), 2))
              &lt;&lt; &quot; s
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;K<code>(0)</code> = 1.5708<br />
&nbsp;<wbr>&nbsp;π/2 = 1.5708<br />
&nbsp;<wbr>&nbsp;K(0.5) = 1.68575<br />
&nbsp;<wbr>&nbsp;F(0.5, π/2) = 1.68575<br />
&nbsp;<wbr>&nbsp;Period of a pendulum length 1 m at 90 degree initial angle is 2.15324 s</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Complete_Elliptic_Integral_of_the_First_Kind.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
<h2>See also</h2>
<p>ellint_1<br />
ellint_1f<br />
ellint_1l (incomplete) elliptic integral of the first kind<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
