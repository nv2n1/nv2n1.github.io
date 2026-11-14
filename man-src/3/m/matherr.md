---
title: "matherr(3)"
name: "matherr"
section: "3"
letter: "m"
url: "/docs/linux/man/3-matherr/"
description: "matherr – SVID math library exception handling"
---

<h2 class="name">NAME</h2>
<p> matherr &#8211; SVID math library exception handling </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
int matherr(struct exception *exc);
extern _LIB_VERSION_TYPE _LIB_VERSION;
</code></pre>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: the mechanism described in this page is no longer supported by glibc. Before glibc 2.27, it had been marked as obsolete. Since glibc 2.27, the mechanism has been removed altogether. New applications should use the techniques described in <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) and <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3). This page documents the <code>matherr</code>() mechanism as an aid for maintaining and porting older applications. </p>
<p> The System V Interface Definition (SVID) specifies that various math functions should invoke a function called <code>matherr</code>() if a math exception is detected. This function is called before the math function returns; after <code>matherr</code>() returns, the system then returns to the math function, which in turn returns to the caller. </p>
<p> To employ <code>matherr</code>(), the programmer must define the <code>_SVID_SOURCE</code> feature test macro (before including <i>any</i> header files), and assign the value <code>_SVID_</code> to the external variable <code>_LIB_VERSION</code>. </p>
<p> The system provides a default version of <code>matherr</code>(). This version does nothing, and returns zero (see below for the significance of this). The default <code>matherr</code>() can be overridden by a programmer-defined version, which will be invoked when an exception occurs. The function is invoked with one argument, a pointer to an <i>exception</i> structure, defined as follows: </p>
<p> struct exception {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Exception type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;*name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Name of function causing exception&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double arg1;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;1st argument to function&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double arg2;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;2nd argument to function&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double retval;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Function return value&nbsp;*/ } </p>
<p> The <i>type</i> field has one of the following values:</p>
<dl>
<dt><code>DOMAIN</code></p>
<dd> A domain error occurred (the function argument was outside the range for which the function is defined). The return value depends on the function; <i>errno</i> is set to <code>EDOM</code>.</p>
<dt><code>SING</code></p>
<dd> A pole error occurred (the function result is an infinity). The return value in most cases is <code>HUGE</code> (the largest single precision floating-point number), appropriately signed. In most cases, <i>errno</i> is set to <code>EDOM</code>.</p>
<dt><code>OVERFLOW</code></p>
<dd> An overflow occurred. In most cases, the value <code>HUGE</code> is returned, and <i>errno</i> is set to <code>ERANGE</code>.</p>
<dt><code>UNDERFLOW</code></p>
<dd> An underflow occurred. 0.0 is returned, and <i>errno</i> is set to <code>ERANGE</code>.</p>
<dt><code>TLOSS</code></p>
<dd> Total loss of significance. 0.0 is returned, and <i>errno</i> is set to <code>ERANGE</code>.</p>
<dt><code>PLOSS</code></p>
<dd> Partial loss of significance. This value is unused on glibc (and many other systems).</dl>
<p> The <i>arg1</i> and <i>arg2</i> fields are the arguments supplied to the function (<i>arg2</i> is undefined for functions that take only one argument). </p>
<p> The <i>retval</i> field specifies the return value that the math function will return to its caller. The programmer-defined <code>matherr</code>() can modify this field to change the return value of the math function. </p>
<p> If the <code>matherr</code>() function returns zero, then the system sets <i>errno</i> as described above, and may print an error message on standard error (see below). </p>
<p> If the <code>matherr</code>() function returns a nonzero value, then the system does not set <i>errno</i>, and doesn&#8217;t print an error message.</p>
<h3>Math functions that employ matherr()</h3>
<p> The table below lists the functions and circumstances in which <code>matherr</code>() is called. The &quot;Type&quot; column indicates the value assigned to <i>exc-&gt;type</i> when calling <code>matherr</code>(). The &quot;Result&quot; column is the default return value assigned to <i>exc-&gt;retval</i>. </p>
<p> The &quot;Msg?&quot; and &quot;errno&quot; columns describe the default behavior if <code>matherr</code>() returns zero. If the &quot;Msg?&quot; columns contains &quot;y&quot;, then the system prints an error message on standard error. </p>
<p> The table uses the following notations and abbreviations: </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>x first argument to function</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>y second argument to function</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>fin finite value for argument</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>neg negative value for argument</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>int integral value for argument</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>o/f result overflowed</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>u/f result underflowed</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>|x| absolute value of x</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>X_TLOSS is a constant defined in <i>&lt;math.h&gt;</i></td>
<td>
</td>
</tr>
</table>
</dl>
<table>
<tr VALIGN=top>
<td><code>Function</code></td>
<td><code>Type</code></td>
<td><code>Result</code></td>
<td ALIGN=center><code>Msg?</code></td>
<td><code>errno</code>
</td>
</tr>
<tr VALIGN=top>
<td>acos(|x|&gt;1)</td>
<td>DOMAIN</td>
<td>HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>asin(|x|&gt;1)</td>
<td>DOMAIN</td>
<td>HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>atan2(0,0)</td>
<td>DOMAIN</td>
<td>HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>acosh(x&lt;1)</td>
<td>DOMAIN</td>
<td>NAN</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>-HUGE_VAL</td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>cosh(fin) o/f</td>
<td>OVERFLOW</td>
<td>HUGE</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>sinh(fin) o/f</td>
<td>OVERFLOW</td>
<td>(x&gt;0.0) ?</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>HUGE : -HUGE</td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>sqrt(x&lt;0)</td>
<td>DOMAIN</td>
<td>0.0</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>hypot(fin,fin) o/f</td>
<td>OVERFLOW</td>
<td>HUGE</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>exp(fin) o/f</td>
<td>OVERFLOW</td>
<td>HUGE</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>exp(fin) u/f</td>
<td>UNDERFLOW</td>
<td>0.0</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>exp2(fin) o/f</td>
<td>OVERFLOW</td>
<td>HUGE</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>exp2(fin) u/f</td>
<td>UNDERFLOW</td>
<td>0.0</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>exp10(fin) o/f</td>
<td>OVERFLOW</td>
<td>HUGE</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>exp10(fin) u/f</td>
<td>UNDERFLOW</td>
<td>0.0</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>j0(|x|&gt;X_TLOSS)</td>
<td>TLOSS</td>
<td>0.0</td>
<td ALIGN=center>y</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>j1(|x|&gt;X_TLOSS)</td>
<td>TLOSS</td>
<td>0.0</td>
<td ALIGN=center>y</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>jn(|x|&gt;X_TLOSS)</td>
<td>TLOSS</td>
<td>0.0</td>
<td ALIGN=center>y</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>y0(x&gt;X_TLOSS)</td>
<td>TLOSS</td>
<td>0.0</td>
<td ALIGN=center>y</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>y1(x&gt;X_TLOSS)</td>
<td>TLOSS</td>
<td>0.0</td>
<td ALIGN=center>y</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>yn(x&gt;X_TLOSS)</td>
<td>TLOSS</td>
<td>0.0</td>
<td ALIGN=center>y</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>y0(0)</td>
<td>DOMAIN</td>
<td>-HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>y0(x&lt;0)</td>
<td>DOMAIN</td>
<td>-HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>y1(0)</td>
<td>DOMAIN</td>
<td>-HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>y1(x&lt;0)</td>
<td>DOMAIN</td>
<td>-HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>yn(n,0)</td>
<td>DOMAIN</td>
<td>-HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>yn(x&lt;0)</td>
<td>DOMAIN</td>
<td>-HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>lgamma(fin) o/f</td>
<td>OVERFLOW</td>
<td>HUGE</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>lgamma(-int) or</td>
<td>SING</td>
<td>HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;lgamma(0)</td>
<td></td>
<td></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>tgamma(fin) o/f</td>
<td>OVERFLOW</td>
<td>HUGE_VAL</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>tgamma(-int)</td>
<td>SING</td>
<td>NAN</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>tgamma(0)</td>
<td>SING</td>
<td>copysign(</td>
<td ALIGN=center>y</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>HUGE_VAL,x)</td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>log(0)</td>
<td>SING</td>
<td>-HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>log(x&lt;0)</td>
<td>DOMAIN</td>
<td>-HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>log2(0)</td>
<td>SING</td>
<td>-HUGE</td>
<td ALIGN=center>n</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>log10(x&lt;0)</td>
<td>DOMAIN</td>
<td>-HUGE</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>pow(0.0,0.0)</td>
<td>DOMAIN</td>
<td>0.0</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>pow(x,y) o/f</td>
<td>OVERFLOW</td>
<td>HUGE</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>pow(x,y) u/f</td>
<td>UNDERFLOW</td>
<td>0.0</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>pow(NaN,0.0)</td>
<td>DOMAIN</td>
<td>x</td>
<td ALIGN=center>n</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>0**neg</td>
<td>DOMAIN</td>
<td>0.0</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>scalb() o/f</td>
<td>OVERFLOW</td>
<td>(x&gt;0.0) ?</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>HUGE_VAL :</td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>-HUGE_VAL</td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>scalb() u/f</td>
<td>UNDERFLOW</td>
<td>copysign(</td>
<td ALIGN=center>n</td>
<td>ERANGE
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;<wbr>&nbsp;0.0,x)</td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>fmod(x,0)</td>
<td>DOMAIN</td>
<td>x</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>remainder(x,0)</td>
<td>DOMAIN</td>
<td>NAN</td>
<td ALIGN=center>y</td>
<td>EDOM
</td>
</tr>
<tr VALIGN=top>
<td>For an explanation of the terms used in this section, see</td>
<td></td>
<td></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>allbox;</td>
<td></td>
<td></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>lb lb lb</td>
<td></td>
<td></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>l l l.</td>
<td></td>
<td></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Interface</td>
<td>Attribute</td>
<td>Value</td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
 <code>matherr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe</td>
<td ALIGN=center></td>
<td>
</td>
</tr>
</table>
<h2>EXAMPLES</h2>
<p> The example program demonstrates the use of <code>matherr</code>() when calling <code><a href="/docs/linux/man/3-log/">log</a></code>(3). The program takes up to three command-line arguments. The first argument is the floating-point number to be given to <code><a href="/docs/linux/man/3-log/">log</a></code>(3). If the optional second argument is provided, then <code>_LIB_VERSION</code> is set to <code>_SVID_</code> so that <code>matherr</code>() is called, and the integer supplied in the command-line argument is used as the return value from <code>matherr</code>(). If the optional third command-line argument is supplied, then it specifies an alternative return value that <code>matherr</code>() should assign as the return value of the math function. </p>
<p> The following example run, where <code><a href="/docs/linux/man/3-log/">log</a></code>(3) is given an argument of 0.0, does not use <code>matherr</code>(): </p>
<p> $<code> ./a.out 0.0</code> errno: Numerical result out of range x=-inf </p>
<p> In the following run, <code>matherr</code>() is called, and returns 0: </p>
<p> $<code> ./a.out 0.0 0</code> matherr SING exception in log() function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;args:&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.000000, 0.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retval: -340282346638528859811704183484516925440.000000 log: SING error errno: Numerical argument out of domain x=-340282346638528859811704183484516925440.000000 </p>
<p> The message &quot;log: SING error&quot; was printed by the C library. </p>
<p> In the following run, <code>matherr</code>() is called, and returns a nonzero value: </p>
<p> $<code> ./a.out 0.0 1</code> matherr SING exception in log() function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;args:&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.000000, 0.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retval: -340282346638528859811704183484516925440.000000 x=-340282346638528859811704183484516925440.000000 </p>
<p> In this case, the C library did not print a message, and <i>errno</i> was not set. </p>
<p> In the following run, <code>matherr</code>() is called, changes the return value of the math function, and returns a nonzero value: </p>
<p> $<code> ./a.out 0.0 1 12345.0</code> matherr SING exception in log() function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;args:&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.000000, 0.000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retval: -340282346638528859811704183484516925440.000000 x=12345.000000</p>
<h3>Program source</h3>
<p> #define _SVID_SOURCE #include &lt;errno.h&gt; #include &lt;math.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> static int matherr_ret = 0; /* Value that matherr()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;should return&nbsp;*/ static int change_retval = 0; /* Should matherr() change<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function&#8217;s return value?&nbsp;*/ static double new_retval; /* New function return value */ </p>
<p> int matherr(struct exception *exc) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;matherr&nbsp;%s exception in&nbsp;%s()&nbsp;function
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(exc-&gt;type&nbsp;==&nbsp;DOMAIN)&nbsp;?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;DOMAIN&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(exc-&gt;type&nbsp;==&nbsp;OVERFLOW)&nbsp;?&nbsp;<wbr>&nbsp;&quot;OVERFLOW&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(exc-&gt;type&nbsp;==&nbsp;UNDERFLOW)&nbsp;?&nbsp;&quot;UNDERFLOW&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(exc-&gt;type&nbsp;==&nbsp;SING)&nbsp;?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;SING&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(exc-&gt;type&nbsp;==&nbsp;TLOSS)&nbsp;?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;TLOSS&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(exc-&gt;type&nbsp;==&nbsp;PLOSS)&nbsp;?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;PLOSS&quot;&nbsp;:&nbsp;&quot;???&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exc-&gt;name);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;args:&nbsp;<wbr>&nbsp;<wbr>&nbsp;%f,&nbsp;%f
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exc-&gt;arg1, exc-&gt;arg2);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retval:&nbsp;%f
&quot;, exc-&gt;retval); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(change_retval)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exc-&gt;retval&nbsp;=&nbsp;new_retval; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return matherr_ret; } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double x; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;argval&gt;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;&nbsp;[&lt;matherr-ret&gt;&nbsp;[&lt;new-func-retval&gt;]]
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_LIB_VERSION&nbsp;=&nbsp;_SVID_;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;matherr_ret&nbsp;=&nbsp;atoi(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;change_retval&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_retval&nbsp;=&nbsp;atof(argv[3]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x&nbsp;=&nbsp;log(atof(argv[1]));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;!=&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;errno&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;x=%f
&quot;, x);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3), <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
