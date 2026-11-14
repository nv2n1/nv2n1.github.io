---
title: "stdexpstdexpfstdexpl(3)"
name: "stdexpstdexpfstdexpl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexpstdexpfstdexpl/"
description: "std::exp,std::expf,std::expl – std::exp,std::expf,std::expl"
---

<p>std::exp,std::expf,std::expl &#8211; std::exp,std::expf,std::expl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float exp ( float arg );<br />
float expf( float arg ); <i>(since C++11)</i><br />
double exp ( double arg ); <code>(1)</code> <code>(2)</code><br />
long double exp ( long double arg );<br />
long double expl( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
double exp ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
Computes e (Euler&#8217;s number, 2.7182818&#8230;) raised to the given power arg<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, the base-e exponential of arg (earg<br />
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
<h2>Notes</h2>
<p>For IEEE-compatible type double, overflow is guaranteed if 709.8 &lt; arg, and underflow is guaranteed if arg &lt; -708.4 </p>
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
    std::cout &lt;&lt; &quot;exp(1) = &quot; &lt;&lt; std::exp(1) &lt;&lt; '
'
              &lt;&lt; &quot;FV of $100, continuously compounded at 3% for 1 year = &quot;
              &lt;&lt; 100 * std::exp(0.03) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;exp(-0) = &quot; &lt;&lt; std::exp(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;exp(-Inf) = &quot; &lt;&lt; std::exp(-INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;exp(710) = &quot; &lt;&lt; std::exp(710) &lt;&lt; '
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
<p>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-exp/">exp</a><code>(1)</code> = 2.71828<br />
&nbsp;<wbr>&nbsp;FV of $100, continuously compounded at 3% for 1 year = 103.045<br />
&nbsp;<wbr>&nbsp;exp(-0) = 1<br />
&nbsp;<wbr>&nbsp;exp(-Inf) = 0<br />
&nbsp;<wbr>&nbsp;exp(710) = inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_OVERFLOW raised</p>
<h2>See also</h2>
<p>exp2<br />
exp2f<br />
exp2l returns 2 raised to the given power (2x)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
expm1<br />
expm1f<br />
expm1l returns e raised to the given power, minus one (ex-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
log<br />
logf<br />
logl computes natural (base e) logarithm (ln(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex base e exponential<br />
exp(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::exp to each element of valarray<br />
exp(std::valarray) <i>(function template)</i> </p>
