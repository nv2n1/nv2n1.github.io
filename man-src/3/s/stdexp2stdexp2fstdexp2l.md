---
title: "stdexp2stdexp2fstdexp2l(3)"
name: "stdexp2stdexp2fstdexp2l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexp2stdexp2fstdexp2l/"
description: "std::exp2,std::exp2f,std::exp2l – std::exp2,std::exp2f,std::exp2l"
---

<p>std::exp2,std::exp2f,std::exp2l &#8211; std::exp2,std::exp2f,std::exp2l</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float exp2 ( float n ); <code>(1)</code> <i>(since C++11)</i><br />
float exp2f( float n );<br />
double exp2 ( double n ); <code>(2)</code> <i>(since C++11)</i><br />
long double exp2 ( long double n ); <code>(3)</code> <i>(since C++11)</i><br />
long double exp2l( long double n );<br />
double exp2 ( IntegralType n ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes 2 raised to the given power n<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>n &#8211; value of floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the base-2 exponential of n (2n<br />
) is returned.<br />
If a range error due to overflow occurs, +HUGE_VAL, +HUGE_VALF, or +HUGE_VALL is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is ±0, 1 is returned<br />
* If the argument is -∞, +0 is returned<br />
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
    std::cout &lt;&lt; &quot;exp2(4) = &quot; &lt;&lt; std::exp2(4) &lt;&lt; '
'
              &lt;&lt; &quot;exp2(0.5) = &quot; &lt;&lt; std::exp2(0.5) &lt;&lt; '
'
              &lt;&lt; &quot;exp2(-4) = &quot; &lt;&lt; std::exp2(-4) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;exp2(-0) = &quot; &lt;&lt; std::exp2(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;exp2(-Inf) = &quot; &lt;&lt; std::exp2(-INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;exp2(1024) = &quot; &lt;&lt; std::exp2(1024) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno == ERANGE: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout &lt;&lt; &quot;    FE_OVERFLOW raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/4-exp2/">exp2</a><code>(4)</code> = 16<br />
&nbsp;<wbr>&nbsp;exp2(0.5) = 1.41421<br />
&nbsp;<wbr>&nbsp;exp2(-4) = 0.0625<br />
&nbsp;<wbr>&nbsp;exp2(-0) = 1<br />
&nbsp;<wbr>&nbsp;exp2(-Inf) = 0<br />
&nbsp;<wbr>&nbsp;exp2(1024) = inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_OVERFLOW raised</p>
<h2>See also</h2>
<p>exp<br />
expf<br />
expl returns e raised to the given power (ex)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
expm1<br />
expm1f<br />
expm1l returns e raised to the given power, minus one (ex-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
log2<br />
log2f<br />
log2l base 2 logarithm of the given number (log2(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
