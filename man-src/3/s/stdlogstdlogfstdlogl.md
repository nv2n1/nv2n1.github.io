---
title: "stdlogstdlogfstdlogl(3)"
name: "stdlogstdlogfstdlogl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlogstdlogfstdlogl/"
description: "std::log,std::logf,std::logl – std::log,std::logf,std::logl"
---

<p>std::log,std::logf,std::logl &#8211; std::log,std::logf,std::logl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float log ( float arg );<br />
float logf( float arg ); <i>(since C++11)</i><br />
double log ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double log ( long double arg );<br />
long double logl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double log ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the natural (base e) logarithm of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the natural (base-e) logarithm of arg (ln(arg) or log<br />
e(arg)) is returned.<br />
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
    std::cout &lt;&lt; &quot;log(1) = &quot; &lt;&lt; std::log(1) &lt;&lt; '
'
              &lt;&lt; &quot;base-5 logarithm of 125 = &quot; &lt;&lt; std::log(125) / std::log(5) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;log(1) = &quot; &lt;&lt; std::log(1) &lt;&lt; '
'
              &lt;&lt; &quot;log(+Inf) = &quot; &lt;&lt; std::log(INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;log(0) = &quot; &lt;&lt; std::log(0) &lt;&lt; '
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
<p>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-log/">log</a><code>(1)</code> = 0<br />
&nbsp;<wbr>&nbsp;base-5 logarithm of 125 = 3<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-log/">log</a><code>(1)</code> = 0<br />
&nbsp;<wbr>&nbsp;log(+Inf) = inf<br />
&nbsp;<wbr>&nbsp;log<code>(0)</code> = -inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_DIVBYZERO raised</p>
<h2>See also</h2>
<p>log10<br />
log10f<br />
log10l computes common (base 10) logarithm (log10(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
log2<br />
log2f<br />
log2l base 2 logarithm of the given number (log2(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
log1p<br />
log1pf<br />
log1pl natural logarithm (to base e) of 1 plus the given number (ln(1+x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
exp<br />
expf<br />
expl returns e raised to the given power (ex)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex natural logarithm with the branch cuts along the negative real axis<br />
log(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::log to each element of valarray<br />
log(std::valarray) <i>(function template)</i> </p>
