---
title: "stdlog10stdlog10fstdlog10l(3)"
name: "stdlog10stdlog10fstdlog10l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlog10stdlog10fstdlog10l/"
description: "std::log10,std::log10f,std::log10l – std::log10,std::log10f,std::log10l"
---

<p>std::log10,std::log10f,std::log10l &#8211; std::log10,std::log10f,std::log10l</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float log10 ( float arg );<br />
float log10f( float arg ); <i>(since C++11)</i><br />
double log10 ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double log10 ( long double arg );<br />
long double log10l( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double log10 ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the common (base-10) logarithm of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the common (base-10) logarithm of arg (log<br />
10(arg) or lg(arg)) is returned.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a pole error occurs, -HUGE_VAL, -HUGE_VALF, or -HUGE_VALL is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
Domain error occurs if arg is less than zero.<br />
Pole error may occur if arg is zero.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is ±0, -∞ is returned and FE_DIVBYZERO is raised.<br />
* If the argument is 1, +0 is returned<br />
* If the argument is negative, NaN is returned and FE_INVALID is raised.<br />
* If the argument is +∞, +∞ is returned<br />
* If the argument is NaN, NaN is returned</p>
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
    std::cout &lt;&lt; &quot;log10(1000) = &quot; &lt;&lt; std::log10(1000) &lt;&lt; '
'
              &lt;&lt; &quot;log10(0.001) = &quot; &lt;&lt; std::log10(0.001) &lt;&lt; '
'
              &lt;&lt; &quot;base-5 logarithm of 125 = &quot; &lt;&lt; std::log10(125) / std::log10(5) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;log10(1) = &quot; &lt;&lt; std::log10(1) &lt;&lt; '
'
              &lt;&lt; &quot;log10(+Inf) = &quot; &lt;&lt; std::log10(INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;log10(0) = &quot; &lt;&lt; std::log10(0) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno == ERANGE: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout &lt;&lt; &quot;    FE_DIVBYZERO raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;log10(1000) = 3<br />
&nbsp;<wbr>&nbsp;log10(0.001) = -3<br />
&nbsp;<wbr>&nbsp;base-5 logarithm of 125 = 3<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-log10/">log10</a><code>(1)</code> = 0<br />
&nbsp;<wbr>&nbsp;log10(+Inf) = inf<br />
&nbsp;<wbr>&nbsp;log10<code>(0)</code> = -inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_DIVBYZERO raised</p>
<h2>See also</h2>
<p>log<br />
logf<br />
logl computes natural (base e) logarithm (ln(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
log2<br />
log2f<br />
log2l base 2 logarithm of the given number (log2(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
log1p<br />
log1pf<br />
log1pl natural logarithm (to base e) of 1 plus the given number (ln(1+x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex common logarithm with the branch cuts along the negative real axis<br />
log10(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::log10 to each element of valarray<br />
log10(std::valarray) <i>(function template)</i> </p>
