---
title: "stdlog2stdlog2fstdlog2l(3)"
name: "stdlog2stdlog2fstdlog2l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlog2stdlog2fstdlog2l/"
description: "std::log2,std::log2f,std::log2l – std::log2,std::log2f,std::log2l"
---

<p>std::log2,std::log2f,std::log2l &#8211; std::log2,std::log2f,std::log2l</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float log2 ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float log2f( float arg );<br />
double log2 ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double log2 ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double log2l( long double arg );<br />
double log2 ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the binary (base-2) logarithm of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the base-2 logarithm of arg (log<br />
2(arg) or lb(arg)) is returned.<br />
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
<h2>Notes</h2>
<p>For integer arg, the binary logarithm can be interpreted as the zero-based index of the most significant 1 bit in the input. </p>
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
    std::cout &lt;&lt; &quot;log2(65536) = &quot; &lt;&lt; std::log2(65536) &lt;&lt; '
'
              &lt;&lt; &quot;log2(0.125) = &quot; &lt;&lt; std::log2(0.125) &lt;&lt; '
'
              &lt;&lt; &quot;log2(0x020f) = &quot; &lt;&lt; std::log2(0x020f)
              &lt;&lt; &quot; (highest set bit is in position 9)
&quot;
              &lt;&lt; &quot;base-5 logarithm of 125 = &quot; &lt;&lt; std::log2(125) / std::log2(5) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;log2(1) = &quot; &lt;&lt; std::log2(1) &lt;&lt; '
'
              &lt;&lt; &quot;log2(+Inf) = &quot; &lt;&lt; std::log2(INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;log2(0) = &quot; &lt;&lt; std::log2(0) &lt;&lt; '
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
<p>&nbsp;<wbr>&nbsp;log2(65536) = 16<br />
&nbsp;<wbr>&nbsp;log2(0.125) = -3<br />
&nbsp;<wbr>&nbsp;log2(0x020f) = 9.04166 (highest set bit is in position 9)<br />
&nbsp;<wbr>&nbsp;base-5 logarithm of 125 = 3<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-log2/">log2</a><code>(1)</code> = 0<br />
&nbsp;<wbr>&nbsp;log2(+Inf) = inf<br />
&nbsp;<wbr>&nbsp;log2<code>(0)</code> = -inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_DIVBYZERO raised</p>
<h2>See also</h2>
<p>log<br />
logf<br />
logl computes natural (base e) logarithm (ln(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
log10<br />
log10f<br />
log10l computes common (base 10) logarithm (log10(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
log1p<br />
log1pf<br />
log1pl natural logarithm (to base e) of 1 plus the given number (ln(1+x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
exp2<br />
exp2f<br />
exp2l returns 2 raised to the given power (2x)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
