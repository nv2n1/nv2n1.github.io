---
title: "stdlgammastdlgammafstdlgammal(3)"
name: "stdlgammastdlgammafstdlgammal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlgammastdlgammafstdlgammal/"
description: "std::lgamma,std::lgammaf,std::lgammal – std::lgamma,std::lgammaf,std::lgammal"
---

<p>std::lgamma,std::lgammaf,std::lgammal &#8211; std::lgamma,std::lgammaf,std::lgammal</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float lgamma ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float lgammaf( float arg );<br />
double lgamma ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double lgamma ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double lgammal( long double arg );<br />
double lgamma ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the natural logarithm of the absolute value of the gamma_function of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the value of the logarithm of the gamma function of arg, that is log<br />
e|∫∞<br />
0targ-1<br />
e-t dt|, is returned.<br />
If a pole error occurs, +HUGE_VAL, +HUGE_VALF, or +HUGE_VALL is returned.<br />
If a range error due to overflow occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If arg is zero or is an integer less than zero, a pole error may occur.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is 1, +0 is returned<br />
* If the argument is 2, +0 is returned<br />
* If the argument is ±0, +∞ is returned and FE_DIVBYZERO is raised<br />
* If the argument is a negative integer, +∞ is returned and FE_DIVBYZERO is raised<br />
* If the argument is ±∞, +∞ is returned.<br />
* If the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>If arg is a natural number, std::lgamma(arg) is the logarithm of the factorial of arg-1.<br />
The POSIX_version_of_lgamma is not thread-safe: each execution of the function stores the sign of the gamma function of arg in the static external variable signgam. Some implementations provide lgamma_r, which takes a pointer to user-provided storage for singgam as the second parameter, and is thread-safe.<br />
There is a non-standard function named gamma in various implementations, but its definition is inconsistent. For example, glibc and 4.2BSD version of gamma executes lgamma, but 4.4BSD version of gamma executes tgamma. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cstring&gt;

#include &lt;cfenv&gt;

#pragma STDC FENV_ACCESS ON

const double pi = std::acos(-1);

int main()

{
    std::cout &lt;&lt; &quot;lgamma(10) = &quot; &lt;&lt; std::lgamma(10)
              &lt;&lt; &quot;,  log(9!) = &quot; &lt;&lt; std::log(2 * 3 * 4 * 5 * 6 * 7 * 8 * 9) &lt;&lt; '
'
              &lt;&lt; &quot;lgamma(0.5) = &quot; &lt;&lt; std::lgamma(0.5)
              &lt;&lt; &quot; , log(sqrt(pi)) = &quot; &lt;&lt; std::log(std::sqrt(pi)) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;lgamma(1) = &quot; &lt;&lt; std::lgamma(1) &lt;&lt; '
'
              &lt;&lt; &quot;lgamma(+Inf) = &quot; &lt;&lt; std::lgamma(INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;lgamma(0) = &quot; &lt;&lt; std::lgamma(0) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno == ERANGE: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout &lt;&lt; &quot;    FE_DIVBYZERO raised
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;lgamma<code>(10)</code> = 12.8018, log(9!) = 12.8018<br />
&nbsp;<wbr>&nbsp;lgamma(0.5) = 0.572365 , log(sqrt(pi)) = 0.572365<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-lgamma/">lgamma</a><code>(1)</code> = 0<br />
&nbsp;<wbr>&nbsp;lgamma(+Inf) = inf<br />
&nbsp;<wbr>&nbsp;lgamma<code>(0)</code> = inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_DIVBYZERO raised</p>
<h2>See also</h2>
<p>tgamma<br />
tgammaf<br />
tgammal gamma function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Log_Gamma_Function.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
