---
title: "stdtgammastdtgammafstdtgammal(3)"
name: "stdtgammastdtgammafstdtgammal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtgammastdtgammafstdtgammal/"
description: "std::tgamma,std::tgammaf,std::tgammal – std::tgamma,std::tgammaf,std::tgammal"
---

<p>std::tgamma,std::tgammaf,std::tgammal &#8211; std::tgamma,std::tgammaf,std::tgammal</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float tgamma ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float tgammaf( float arg );<br />
double tgamma ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double tgamma ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double tgammal( long double arg );<br />
double tgamma ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the gamma_function of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the value of the gamma function of arg, that is \(\mathsf{\Gamma}(arg) = \int_0^\infty t^{arg-1} e^{-t} \mathsf{d}t\)∫∞<br />
0targ-1<br />
e-t dt, is returned<br />
If a domain error occurs, an implementation-defined value (NaN where supported) is returned.<br />
If a pole error occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned.<br />
If a range error due to overflow occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned.<br />
If a range error due to underflow occurs, the correct value (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If arg is zero or is an integer less than zero, a pole error or a domain error may occur.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is ±0, ±∞ is returned and FE_DIVBYZERO is raised<br />
* If the argument is a negative integer, NaN is returned and FE_INVALID is raised<br />
* If the argument is -∞, NaN is returned and FE_INVALID is raised<br />
* If the argument is +∞, +∞ is returned.<br />
* If the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>If arg is a natural number, std::tgamma(arg) is the factorial of arg-1. Many implementations calculate the exact integer-domain factorial if the argument is a sufficiently small integer.<br />
For IEEE-compatible type double, overflow happens if 0 &lt; x &lt; 1/DBL_MAX or if x &gt; 171.7<br />
POSIX_requires that a pole error occurs if the argument is zero, but a domain error occurs when the argument is a negative integer. It also specifies that in future, domain errors may be replaced by pole errors for negative integer arguments (in which case the return value in those cases would change from NaN to ±∞).<br />
There is a non-standard function named gamma in various implementations, but its definition is inconsistent. For example, glibc and 4.2BSD version of gamma executes lgamma, but 4.4BSD version of gamma executes tgamma. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cstring&gt;

#include &lt;cfenv&gt;

#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;tgamma(10) = &quot; &lt;&lt; std::tgamma(10)
              &lt;&lt; &quot;, 9! = &quot; &lt;&lt; 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 &lt;&lt; '
'
              &lt;&lt; &quot;tgamma(0.5) = &quot; &lt;&lt; std::tgamma(0.5)
              &lt;&lt; &quot;, sqrt(pi) = &quot; &lt;&lt; std::sqrt(std::acos(-1)) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;tgamma(1) = &quot; &lt;&lt; std::tgamma(1) &lt;&lt; '
'
              &lt;&lt; &quot;tgamma(+Inf) = &quot; &lt;&lt; std::tgamma(INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;tgamma(-1) = &quot; &lt;&lt; std::tgamma(-1) &lt;&lt; '
';
    if (errno == EDOM)
        std::cout &lt;&lt; &quot;    errno == EDOM: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;tgamma<code>(10)</code> = 362880, 9! = 362880<br />
&nbsp;<wbr>&nbsp;tgamma(0.5) = 1.77245, sqrt(pi) = 1.77245<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-tgamma/">tgamma</a><code>(1)</code> = 1<br />
&nbsp;<wbr>&nbsp;tgamma(+Inf) = inf<br />
&nbsp;<wbr>&nbsp;tgamma(-1) = nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == EDOM: Numerical argument out of domain<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>lgamma<br />
lgammaf<br />
lgammal natural logarithm of the gamma function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
beta<br />
betaf<br />
betal beta function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Gamma_Function.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
