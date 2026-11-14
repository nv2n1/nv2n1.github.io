---
title: "stdcyl_bessel_istdcyl_bessel_ifstdcyl_bessel_il(3)"
name: "stdcyl_bessel_istdcyl_bessel_ifstdcyl_bessel_il"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcyl_bessel_istdcyl_bessel_ifstdcyl_bessel_il/"
description: "std::cyl_bessel_i,std::cyl_bessel_if,std::cyl_bessel_il – std::cyl_bessel_i,std::cyl_bessel_if,std::cyl_bessel_il"
---

<p>std::cyl_bessel_i,std::cyl_bessel_if,std::cyl_bessel_il &#8211; std::cyl_bessel_i,std::cyl_bessel_if,std::cyl_bessel_il</p>
<h2>Synopsis</h2>
<pre><code>double cyl_bessel_i( double ν, double x );

float cyl_bessel_if( float ν, float x );                  (1) (since C++17)

long double cyl_bessel_il( long double ν, long double x );

Promoted cyl_bessel_i( Arithmetic ν, Arithmetic x );      (2) (since C++17)</code></pre>
<p>1) Computes the regular_modified_cylindrical_Bessel_function of ν and x.<br />
2) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by <code>(1)</code>. If any argument has integral_type, it is cast to double. If any argument is long double, then the return type Promoted is also long double, otherwise the return type is always double. </p>
<h2>Parameters</h2>
<p>ν- the order of the function<br />
x &#8211; the argument of the function)</p>
<h2>Return value</h2>
<p>If no errors occur, value of the regular modified cylindrical Bessel function of ν and x, that is I<br />
ν(x) = Σ∞<br />
k=0<br />
(x/2)ν+2k<br />
k!Γ(ν+k+1)<br />
(for x≥0), is returned. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If the argument is NaN, NaN is returned and domain error is not reported<br />
* If ν&gt;=128, the behavior is implementation-defined</p>
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
    // spot check for ν == 0
    double x = 1.2345;
    std::cout &lt;&lt; &quot;I_0(&quot; &lt;&lt; x &lt;&lt; &quot;) = &quot; &lt;&lt; std::cyl_bessel_i(0, x) &lt;&lt; '
';
    // series expansion for I_0
    double fct = 1;
    double sum = 0;
    for (int k = 0; k &lt; 5; fct *= ++k) {
        sum += std::pow((x / 2), 2 * k) / std::pow(fct, 2);
        std::cout &lt;&lt; &quot;sum = &quot; &lt;&lt; sum &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;I_0(1.2345) = 1.41886<br />
&nbsp;<wbr>&nbsp;sum = 1<br />
&nbsp;<wbr>&nbsp;sum = 1.381<br />
&nbsp;<wbr>&nbsp;sum = 1.41729<br />
&nbsp;<wbr>&nbsp;sum = 1.41882<br />
&nbsp;<wbr>&nbsp;sum = 1.41886</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Modified_Bessel_Function_of_the_First_Kind.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
<h2>See also</h2>
<p>cyl_bessel_j<br />
cyl_bessel_jf<br />
cyl_bessel_jl cylindrical Bessel functions (of the first kind)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
