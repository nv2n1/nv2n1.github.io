---
title: "fedisableexcept(3)"
name: "fedisableexcept"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fedisableexcept/"
description: "feclearexcept, fegetexceptflag, feraiseexcept, fesetexceptflag, fetestexcept, fegetenv, fegetround, feholdexcept, fesetround, fesetenv, feupdateenv, feenableexcept, fedisableexcept, fegetexcept – f..."
---

<h2 class="name">NAME</h2>
<p> feclearexcept, fegetexceptflag, feraiseexcept, fesetexceptflag, fetestexcept, fegetenv, fegetround, feholdexcept, fesetround, fesetenv, feupdateenv, feenableexcept, fedisableexcept, fegetexcept &#8211; floating-point rounding and exception handling </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fenv.h&gt;
int feclearexcept(int excepts);
int fegetexceptflag(fexcept_t *flagp, int excepts);
int feraiseexcept(int excepts);
int fesetexceptflag(const fexcept_t *flagp, int excepts);
int fetestexcept(int excepts);
int fegetround(void);
int fesetround(int rounding_mode);
int fegetenv(fenv_t *envp);
int feholdexcept(fenv_t *envp);
int fesetenv(const fenv_t *envp);
int feupdateenv(const fenv_t *envp);
</code></pre>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These eleven functions were defined in C99, and describe the handling of floating-point rounding and exceptions (overflow, zero-divide, etc.).</p>
<h3>Exceptions</h3>
<p> The <i>divide-by-zero</i> exception occurs when an operation on finite numbers produces infinity as exact answer. </p>
<p> The <i>overflow</i> exception occurs when a result has to be represented as a floating-point number, but has (much) larger absolute value than the largest (finite) floating-point number that is representable. </p>
<p> The <i>underflow</i> exception occurs when a result has to be represented as a floating-point number, but has smaller absolute value than the smallest positive normalized floating-point number (and would lose much accuracy when represented as a denormalized number). </p>
<p> The <i>inexact</i> exception occurs when the rounded result of an operation is not equal to the infinite precision result. It may occur whenever <i>overflow</i> or <i>underflow</i> occurs. </p>
<p> The <i>invalid</i> exception occurs when there is no well-defined result for an operation, as for 0/0 or infinity &#8211; infinity or sqrt(-1).</p>
<h3>Exception handling</h3>
<p> Exceptions are represented in two ways: as a single bit (exception present/absent), and these bits correspond in some implementation-defined way with bit positions in an integer, and also as an opaque structure that may contain more information about the exception (perhaps the code address where it occurred). </p>
<p> Each of the macros <code>FE_DIVBYZERO</code>, <code>FE_INEXACT</code>, <code>FE_INVALID</code>, <code>FE_OVERFLOW</code>, <code>FE_UNDERFLOW</code> is defined when the implementation supports handling of the corresponding exception, and if so then defines the corresponding bit(s), so that one can call exception handling functions, for example, using the integer argument <code>FE_OVERFLOW</code>|<code>FE_UNDERFLOW</code>. Other exceptions may be supported. The macro <code>FE_ALL_EXCEPT</code> is the bitwise OR of all bits corresponding to supported exceptions. </p>
<p> The <code>feclearexcept</code>() function clears the supported exceptions represented by the bits in its argument. </p>
<p> The <code>fegetexceptflag</code>() function stores a representation of the state of the exception flags represented by the argument <i>excepts</i> in the opaque object <i>*flagp</i>. </p>
<p> The <code>feraiseexcept</code>() function raises the supported exceptions represented by the bits in <i>excepts</i>. </p>
<p> The <code>fesetexceptflag</code>() function sets the complete status for the exceptions represented by <i>excepts</i> to the value <i>*flagp</i>. This value must have been obtained by an earlier call of <code>fegetexceptflag</code>() with a last argument that contained all bits in <i>excepts</i>. </p>
<p> The <code>fetestexcept</code>() function returns a word in which the bits are set that were set in the argument <i>excepts</i> and for which the corresponding exception is currently set.</p>
<h3>Rounding mode</h3>
<p> The rounding mode determines how the result of floating-point operations is treated when the result cannot be exactly represented in the significand. Various rounding modes may be provided: round to nearest (the default), round up (toward positive infinity), round down (toward negative infinity), and round toward zero. </p>
<p> Each of the macros <code>FE_TONEAREST</code>, <code>FE_UPWARD</code>, <code>FE_DOWNWARD</code>, and <code>FE_TOWARDZERO</code> is defined when the implementation supports getting and setting the corresponding rounding direction. </p>
<p> The <code>fegetround</code>() function returns the macro corresponding to the current rounding mode. </p>
<p> The <code>fesetround</code>() function sets the rounding mode as specified by its argument and returns zero when it was successful. </p>
<p> C99 and POSIX.1-2008 specify an identifier, <code>FLT_ROUNDS</code>, defined in <i>&lt;float.h&gt;</i>, which indicates the implementation-defined rounding behavior for floating-point addition. This identifier has one of the following values:</p>
<dl>
<dt>-1</p>
<dd> The rounding mode is not determinable.</p>
<dt>0</p>
<dd> Rounding is toward 0.</p>
<dt>1</p>
<dd> Rounding is toward nearest number.</p>
<dt>2</p>
<dd> Rounding is toward positive infinity.</p>
<dt>3</p>
<dd> Rounding is toward negative infinity.</dl>
<p> Other values represent machine-dependent, nonstandard rounding modes. </p>
<p> The value of <code>FLT_ROUNDS</code> should reflect the current rounding mode as set by <code>fesetround</code>() (but see BUGS).</p>
<h3>Floating-point environment</h3>
<p> The entire floating-point environment, including control modes and status flags, can be handled as one opaque object, of type <i>fenv_t</i>. The default environment is denoted by <code>FE_DFL_ENV</code> (of type <i>const fenv_t&nbsp;*</i>). This is the environment setup at program start and it is defined by ISO C to have round to nearest, all exceptions cleared and a nonstop (continue on exceptions) mode. </p>
<p> The <code>fegetenv</code>() function saves the current floating-point environment in the object <i>*envp</i>. </p>
<p> The <code>feholdexcept</code>() function does the same, then clears all exception flags, and sets a nonstop (continue on exceptions) mode, if available. It returns zero when successful. </p>
<p> The <code>fesetenv</code>() function restores the floating-point environment from the object <i>*envp</i>. This object must be known to be valid, for example, the result of a call to <code>fegetenv</code>() or <code>feholdexcept</code>() or equal to <code>FE_DFL_ENV</code>. This call does not raise exceptions. </p>
<p> The <code>feupdateenv</code>() function installs the floating-point environment represented by the object <i>*envp</i>, except that currently raised exceptions are not cleared. After calling this function, the raised exceptions will be a bitwise OR of those previously set with those in <i>*envp</i>. As before, the object <i>*envp</i> must be known to be valid.</p>
<h2>RETURN VALUE</h2>
<p> These functions return zero on success and nonzero if an error occurred.</p>
<h2>VERSIONS</h2>
<p> These functions first appeared in glibc in version 2.1.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>feclearexcept</code>(), <code>fegetexceptflag</code>(), <code>feraiseexcept</code>(), <code>fesetexceptflag</code>(), <code>fetestexcept</code>(), <code>fegetround</code>(), <code>fesetround</code>(), <code>fegetenv</code>(), <code>feholdexcept</code>(), <code>fesetenv</code>(), <code>feupdateenv</code>(), <code>feenableexcept</code>(), <code>fedisableexcept</code>(), <code>fegetexcept</code>() </td>
<td>Thread safety</td>
<td> MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> IEC 60559 (IEC 559:1989), ANSI/IEEE 854, C99, POSIX.1-2001.</p>
<h2>NOTES</h2>
<h3>Glibc notes</h3>
<p> If possible, the GNU C Library defines a macro <code>FE_NOMASK_ENV</code> which represents an environment where every exception raised causes a trap to occur. You can test for this macro using <code>#ifdef</code>. It is defined only if <code>_GNU_SOURCE</code> is defined. The C99 standard does not define a way to set individual bits in the floating-point mask, for example, to trap on specific flags. Since version 2.2, glibc supports the functions <code>feenableexcept</code>() and <code>fedisableexcept</code>() to set individual floating-point traps, and <code>fegetexcept</code>() to query the state. </p>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;fenv.h&gt;
int feenableexcept(int excepts);
int fedisableexcept(int excepts);
int fegetexcept(void);
</code></pre>
<p> The <code>feenableexcept</code>() and <code>fedisableexcept</code>() functions enable (disable) traps for each of the exceptions represented by <i>excepts</i> and return the previous set of enabled exceptions when successful, and -1 otherwise. The <code>fegetexcept</code>() function returns the set of all currently enabled exceptions.</p>
<h2>BUGS</h2>
<p> C99 specifies that the value of <code>FLT_ROUNDS</code> should reflect changes to the current rounding mode, as set by <code>fesetround</code>(). Currently, this does not occur: <code>FLT_ROUNDS</code> always has the value 1.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
