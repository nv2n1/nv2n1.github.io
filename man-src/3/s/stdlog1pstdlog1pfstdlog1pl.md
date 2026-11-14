---
title: "stdlog1pstdlog1pfstdlog1pl(3)"
name: "stdlog1pstdlog1pfstdlog1pl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlog1pstdlog1pfstdlog1pl/"
description: "std::log1p,std::log1pf,std::log1pl – std::log1p,std::log1pf,std::log1pl"
---

<p>std::log1p,std::log1pf,std::log1pl &#8211; std::log1p,std::log1pf,std::log1pl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float log1p ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float log1pf( float arg );<br />
double log1p ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double log1p ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double log1pl( long double arg );<br />
double log1p ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the natural (base e) logarithm of 1+arg. This function is more precise than the expression std::log(1+arg) if arg is close to zero.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur ln(1+arg) is returned.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a pole error occurs, -HUGE_VAL, -HUGE_VALF, or -HUGE_VALL is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
Domain error occurs if arg is less than -1.<br />
Pole error may occur if arg is -1.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is ±0, it is returned unmodified<br />
* If the argument is -1, -∞ is returned and FE_DIVBYZERO is raised.<br />
* If the argument is less than -1, NaN is returned and FE_INVALID is raised.<br />
* If the argument is +∞, +∞ is returned<br />
* If the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>The functions std::expm1 and std::log1p are useful for financial calculations, for example, when calculating small daily interest rates: (1+x)n<br />
-1 can be expressed as std::expm1(n * std::log1p(x)). These functions also simplify writing accurate inverse hyperbolic functions. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cfenv&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cstring&gt;

#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;log1p(0) = &quot; &lt;&lt; log1p(0) &lt;&lt; '
'
              &lt;&lt; &quot;Interest earned in 2 days on on $100, compounded daily at 1%
&quot;
              &lt;&lt; &quot; on a 30/360 calendar = &quot;
              &lt;&lt; 100 * expm1(2 * log1p(0.01 / 360)) &lt;&lt; '
'
              &lt;&lt; &quot;log(1+1e-16) = &quot; &lt;&lt; std::log(1 + 1e-16)
              &lt;&lt; &quot; log1p(1e-16) = &quot; &lt;&lt; std::log1p(1e-16) &lt;&lt; '
';
    // special values
    std::cout &lt;&lt; &quot;log1p(-0) = &quot; &lt;&lt; std::log1p(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;log1p(+Inf) = &quot; &lt;&lt; std::log1p(INFINITY) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;log1p(-1) = &quot; &lt;&lt; std::log1p(-1) &lt;&lt; '
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
<p>&nbsp;<wbr>&nbsp;log1p<code>(0)</code> = 0<br />
&nbsp;<wbr>&nbsp;Interest earned in 2 days on on $100, compounded daily at 1%<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;on a 30/360 calendar = 0.00555563<br />
&nbsp;<wbr>&nbsp;log(1+1e-16) = 0 log1p(1e-16) = 1e-16<br />
&nbsp;<wbr>&nbsp;log1p(-0) = -0<br />
&nbsp;<wbr>&nbsp;log1p(+Inf) = inf<br />
&nbsp;<wbr>&nbsp;log1p(-1) = -inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Result too large<br />
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
log2<br />
log2f<br />
log2l base 2 logarithm of the given number (log2(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
expm1<br />
expm1f<br />
expm1l returns e raised to the given power, minus one (ex-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
