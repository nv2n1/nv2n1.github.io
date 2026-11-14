---
title: "stdcyl_bessel_kstdcyl_bessel_kfstdcyl_bessel_kl(3)"
name: "stdcyl_bessel_kstdcyl_bessel_kfstdcyl_bessel_kl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcyl_bessel_kstdcyl_bessel_kfstdcyl_bessel_kl/"
description: "std::cyl_bessel_k,std::cyl_bessel_kf,std::cyl_bessel_kl – std::cyl_bessel_k,std::cyl_bessel_kf,std::cyl_bessel_kl"
---

<p>std::cyl_bessel_k,std::cyl_bessel_kf,std::cyl_bessel_kl &#8211; std::cyl_bessel_k,std::cyl_bessel_kf,std::cyl_bessel_kl</p>
<h2>Synopsis</h2>
<pre><code>double cyl_bessel_k( double ν, double x );

float cyl_bessel_kf( float ν, float x );                  (1) (since C++17)

long double cyl_bessel_kl( long double ν, long double x );

Promoted cyl_bessel_k( Arithmetic ν, Arithmetic x );      (2) (since C++17)</code></pre>
<p>1) Computes the irregular_modified_cylindrical_Bessel_function (also known as modified Bessel function of the second kind) of ν and x.<br />
2) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by <code>(1)</code>. If any argument has integral_type, it is cast to double. If any argument is long double, then the return type Promoted is also long double, otherwise the return type is always double. </p>
<h2>Parameters</h2>
<p>ν- the order of the function<br />
x &#8211; the argument of the function)</p>
<h2>Return value</h2>
<p>If no errors occur, value of the irregular modified cylindrical Bessel function (modified Bessel function of the second kind) of ν and x, is returned, that is K<br />
ν(x) =<br />
π<br />
2<br />
I<br />
-ν(x)-I<br />
ν(x)<br />
sin(νπ)<br />
(where I<br />
ν(x) is std::cyl_bessel_i(ν,x)) for x≥0 and non-integer ν; for integer ν a limit is used. </p>
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
    double pi = std::acos(-1);
    double x = 1.2345;
    // spot check for ν == 0.5
    std::cout &lt;&lt; &quot;K_.5(&quot; &lt;&lt; x &lt;&lt; &quot;) = &quot; &lt;&lt; std::cyl_bessel_k(.5, x) &lt;&lt; '
'
              &lt;&lt; &quot;calculated via I = &quot; &lt;&lt; (pi / 2) * (std::cyl_bessel_i(-.5, x) - std::cyl_bessel_i(.5, x)) / std::sin(.5 * pi) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;K_.5(1.2345) = 0.32823<br />
&nbsp;<wbr>&nbsp;calculated via I = 0.32823</p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Modified_Bessel_Function_of_the_Second_Kind.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
<h2>See also</h2>
<p>cyl_bessel_i<br />
cyl_bessel_if<br />
cyl_bessel_il regular modified cylindrical Bessel functions<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
cyl_bessel_j<br />
cyl_bessel_jf<br />
cyl_bessel_jl cylindrical Bessel functions (of the first kind)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
