---
title: "stdexpm1stdexpm1fstdexpm1l(3)"
name: "stdexpm1stdexpm1fstdexpm1l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexpm1stdexpm1fstdexpm1l/"
description: "std::expm1,std::expm1f,std::expm1l – std::expm1,std::expm1f,std::expm1l"
---

<p>std::expm1,std::expm1f,std::expm1l &#8211; std::expm1,std::expm1f,std::expm1l</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float expm1 ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float expm1f( float arg );<br />
double expm1 ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double expm1 ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double expm1l( long double arg );<br />
double expm1 ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the e (Euler&#8217;s number, 2.7182818) raised to the given power arg, minus 1.0. This function is more accurate than the expression std::exp(arg)-1.0 if arg is close to zero.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur earg<br />
-1 is returned.<br />
If a range error due to overflow occurs, +HUGE_VAL, +HUGE_VALF, or +HUGE_VALL is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is ±0, it is returned, unmodified<br />
* If the argument is -∞, -1 is returned<br />
* If the argument is +∞, +∞ is returned<br />
* If the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>The functions std::expm1 and std::log1p are useful for financial calculations, for example, when calculating small daily interest rates: (1+x)n<br />
-1 can be expressed as std::expm1(n * std::log1p(x)). These functions also simplify writing accurate inverse hyperbolic functions.<br />
For IEEE-compatible type double, overflow is guaranteed if 709.8 &lt; arg </p>
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
    std::cout &lt;&lt; &quot;expm1(1) = &quot; &lt;&lt; std::expm1(1) &lt;&lt; '
'
              &lt;&lt; &quot;Interest earned in 2 days on on $100, compounded daily at 1%
&quot;
              &lt;&lt; &quot; on a 30/360 calendar = &quot;
              &lt;&lt; 100 * std::expm1(2 * std::log1p(0.01 / 360)) &lt;&lt; '
'
              &lt;&lt; &quot;exp(1e-16)-1 = &quot; &lt;&lt; std::exp(1e-16) - 1
              &lt;&lt; &quot;, but expm1(1e-16) = &quot; &lt;&lt; std::expm1(1e-16) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;expm1(-0) = &quot; &lt;&lt; std::expm1(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;expm1(-Inf) = &quot; &lt;&lt; std::expm1(-INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;expm1(710) = &quot; &lt;&lt; std::expm1(710) &lt;&lt; '
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
<p>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-expm1/">expm1</a><code>(1)</code> = 1.71828<br />
&nbsp;<wbr>&nbsp;Interest earned in 2 days on on $100, compounded daily at 1%<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;on a 30/360 calendar = 0.00555563<br />
&nbsp;<wbr>&nbsp;exp(1e-16)-1 = 0 expm1(1e-16) = 1e-16<br />
&nbsp;<wbr>&nbsp;expm1(-0) = -0<br />
&nbsp;<wbr>&nbsp;expm1(-Inf) = -1<br />
&nbsp;<wbr>&nbsp;expm1(710) = inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Result too large<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_OVERFLOW raised</p>
<h2>See also</h2>
<p>exp<br />
expf<br />
expl returns e raised to the given power (ex)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
exp2<br />
exp2f<br />
exp2l returns 2 raised to the given power (2x)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
log1p<br />
log1pf<br />
log1pl natural logarithm (to base e) of 1 plus the given number (ln(1+x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
