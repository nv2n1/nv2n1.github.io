---
title: "stdcomp_ellint_2stdcomp_ellint_2fstdcomp_ellint_2l(3)"
name: "stdcomp_ellint_2stdcomp_ellint_2fstdcomp_ellint_2l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcomp_ellint_2stdcomp_ellint_2fstdcomp_ellint_2l/"
description: "std::comp_ellint_2,std::comp_ellint_2f,std::comp_ellint_2l – std::comp_ellint_2,std::comp_ellint_2f,std::comp_ellint_2l"
---

<p>std::comp_ellint_2,std::comp_ellint_2f,std::comp_ellint_2l &#8211; std::comp_ellint_2,std::comp_ellint_2f,std::comp_ellint_2l</p>
<h2>Synopsis</h2>
<pre><code>double comp_ellint_2( double k);

float comp_ellint_2( float k );

long double comp_ellint_2( long double k );  (1) (since C++17)

float comp_ellint_2f( float k );

long double comp_ellint_2l( long double k );

double comp_ellint_2( IntegralType k );      (2) (since C++17)</code></pre>
<p>1) Computes the complete_elliptic_integral_of_the_second_kind of k.<br />
2) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(1)</code> after casting the argument to double. </p>
<h2>Parameters</h2>
<p>k &#8211; elliptic modulus or eccentricity (a value of a floating-point or integral type)</p>
<h2>Return value</h2>
<p>If no errors occur, value of the complete elliptic integral of the second kind of k, that is ellint_2(k,π/2), is returned. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If |k|&gt;1, a domain error may occur</p>
<h2>Notes</h2>
<p>Implementations that do not support C++17, but support ISO_29124:2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.</p>
<p>Implementations that do not support ISO 29124:2010 but support TR 19768:2007 (TR1), provide this function in the header tr1/cmath and namespace std::tr1</p>
<p>An implementation of this function is also available_in_boost.math</p>
<p>The perimeter of an ellipse with eccentricity k and semimajor axis a equals 4aE(k), where E is std::comp_ellint_2. When eccentricity equals 0, the ellipse degenerates to a circle with radius a and the perimeter equals 2πa, so E(0) = π/2. When eccentricity equals 1, the ellipse degenerates to a line of length 2a, whose perimeter is 4a, so E(1) = 1</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

int main()

{
    double hpi = std::acos(-1) / 2;
    std::cout &lt;&lt; &quot;E(0) = &quot; &lt;&lt; std::comp_ellint_2(0) &lt;&lt; '
'
              &lt;&lt; &quot;π/2 = &quot; &lt;&lt; hpi &lt;&lt; '
'
              &lt;&lt; &quot;E(1) = &quot; &lt;&lt; std::comp_ellint_2(1) &lt;&lt; '
'
              &lt;&lt; &quot;E(1, π/2) = &quot; &lt;&lt; std::ellint_2(1, hpi) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;E<code>(0)</code> = 1.5708<br />
&nbsp;<wbr>&nbsp;π/2 = 1.5708<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-e/">E</a><code>(1)</code> = 1<br />
&nbsp;<wbr>&nbsp;E(1, π/2) = 1</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Complete_Elliptic_Integral_of_the_Second_Kind.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
<h2>See also</h2>
<p>ellint_2<br />
ellint_2f<br />
ellint_2l (incomplete) elliptic integral of the second kind<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
