---
title: "math_error(7)"
name: "math_error"
section: "7"
letter: "m"
url: "/docs/linux/man/7-math_error/"
description: "math_error – detecting errors from mathematical functions"
---

<p>math_error &#8211; detecting errors from mathematical functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;
#include &lt;errno.h&gt;
#include &lt;fenv.h&gt;</code></pre>
<h2>Description</h2>
<p>When an error occurs, most library functions indicate this fact by returning a special value (e.g., -1 or NULL). Because they typically return a floating-point number, the mathematical functions declared in <i>&lt;math.h&gt;</i> indicate an error using other mechanisms. There are two error-reporting mechanisms: the older one sets <i>errno</i>; the newer one uses the floating-point exception mechanism (the use of <code><a href="/docs/linux/man/3-feclearexcept/">feclearexcept</a></code>(3) and <code><a href="/docs/linux/man/3-fetestexcept/">fetestexcept</a></code>(3), as outlined below) described in <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3). </p>
<p> A portable program that needs to check for an error from a mathematical function should set <i>errno</i> to zero, and make the following call </p>
<p> feclearexcept(FE_ALL_EXCEPT); </p>
<p> before calling a mathematical function. </p>
<p> Upon return from the mathematical function, if <i>errno</i> is nonzero, or the following call (see <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3)) returns nonzero </p>
<p> fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_UNDERFLOW); </p>
<p> then an error occurred in the mathematical function. </p>
<p> The error conditions that can occur for mathematical functions are described below.</p>
<h3>Domain error</h3>
<p>A <i>domain error</i> occurs when a mathematical function is supplied with an argument whose value falls outside the domain for which the function is defined (e.g., giving a negative argument to <code><a href="/docs/linux/man/3-log/">log</a></code>(3)). When a domain error occurs, math functions commonly return a NaN (though some functions return a different value in this case); <i>errno</i> is set to <code>EDOM</code>, and an &quot;invalid&quot; (<code>FE_INVALID</code>) floating-point exception is raised.</p>
<h3>Pole error</h3>
<p>A <i>pole error</i> occurs when the mathematical result of a function is an exact infinity (e.g., the logarithm of 0 is negative infinity). When a pole error occurs, the function returns the (signed) value <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, depending on whether the function result type is <i>double</i>, <i>float</i>, or <i>long double</i>. The sign of the result is that which is mathematically correct for the function. <i>errno</i> is set to <code>ERANGE</code>, and a &quot;divide-by-zero&quot; (<code>FE_DIVBYZERO</code>) floating-point exception is raised.</p>
<h3>Range error</h3>
<p>A <i>range error</i> occurs when the magnitude of the function result means that it cannot be represented in the result type of the function. The return value of the function depends on whether the range error was an overflow or an underflow. </p>
<p> A floating result <i>overflows</i> if the result is finite, but is too large to represented in the result type. When an overflow occurs, the function returns the value <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, depending on whether the function result type is <i>double</i>, <i>float</i>, or <i>long double</i>. <i>errno</i> is set to <code>ERANGE</code>, and an &quot;overflow&quot; (<code>FE_OVERFLOW</code>) floating-point exception is raised. </p>
<p> A floating result <i>underflows</i> if the result is too small to be represented in the result type. If an underflow occurs, a mathematical function typically returns 0.0 (C99 says a function shall return &quot;an implementation-defined value whose magnitude is no greater than the smallest normalized positive number in the specified type&quot;). <i>errno</i> may be set to <code>ERANGE</code>, and an &quot;underflow&quot; (<code>FE_UNDERFLOW</code>) floating-point exception may be raised. </p>
<p> Some functions deliver a range error if the supplied argument value, or the correct function result, would be <i>subnormal</i>. A subnormal value is one that is nonzero, but with a magnitude that is so small that it can&#8217;t be presented in normalized form (i.e., with a 1 in the most significant bit of the significand). The representation of a subnormal number will contain one or more leading zeros in the significand.</p>
<h2>Notes</h2>
<p>The <i>math_errhandling</i> identifier specified by C99 and POSIX.1 is not supported by glibc. This identifier is supposed to indicate which of the two error-notification mechanisms (<i>errno</i>, exceptions retrievable via <code><a href="/docs/linux/man/3-fetestexcept/">fetestexcept</a></code>(3)) is in use. The standards require that at least one be in use, but permit both to be available. The current (version 2.8) situation under glibc is messy. Most (but not all) functions raise exceptions on errors. Some also set <i>errno</i>. A few functions set <i>errno</i>, but don&#8217;t raise an exception. A very few functions do neither. See the individual manual pages for details. To avoid the complexities of using <i>errno</i> and <code><a href="/docs/linux/man/3-fetestexcept/">fetestexcept</a></code>(3) for error checking, it is often advised that one should instead check for bad argument values before each call. For example, the following code ensures that <code><a href="/docs/linux/man/3-log/">log</a></code>(3)&#8217;s argument is not a NaN and is not zero (a pole error) or less than zero (a domain error): </p>
<pre><code>double x, r;
if (isnan(x) || islessequal(x, 0)) {
    /* Deal with NaN / pole error / domain error */
}
r = log(x);</code></pre>
<p> The discussion on this page does not apply to the complex mathematical functions (i.e., those declared by <i>&lt;complex.h&gt;</i>), which in general are not required to return errors by C99 and POSIX.1. The <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) <i>-fno-math-errno</i> option causes the executable to employ implementations of some mathematical functions that are faster than the standard implementations, but do not set <i>errno</i> on error. (The <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) <i>-ffast-math</i> option also enables <i>-fno-math-errno</i>.) An error can still be tested for using <code><a href="/docs/linux/man/3-fetestexcept/">fetestexcept</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3), <code><a href="/docs/linux/man/3-fpclassify/">fpclassify</a></code>(3), <code><a href="/docs/linux/man/3-infinity/">INFINITY</a></code>(3), <code><a href="/docs/linux/man/3-isgreater/">isgreater</a></code>(3), <code><a href="/docs/linux/man/3-matherr/">matherr</a></code>(3), <code><a href="/docs/linux/man/3-nan/">nan</a></code>(3) </p>
<p> <i>info libc</i></p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
