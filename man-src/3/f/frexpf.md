---
title: "frexpf(3)"
name: "frexpf"
section: "3"
letter: "f"
url: "/docs/linux/man/3-frexpf/"
---

<h2 class="name">NAME</h2>
 

 frexp, frexpf, frexpl - convert floating-point number to fractional and integral components 

<h2>SYNOPSIS</h2>

 <pre><code>
#include &lt;math.h&gt;
double frexp(double x, int *exp);
float frexpf(float x, int *exp);
long double frexpl(long double x, int *exp);
</code></pre> 

 Link with <i>-lm</i>. 

 Feature Test Macro Requirements for glibc (see <b><a HREF="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></b>(7)): 

 <b>frexpf</b>(), <b>frexpl</b>():
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>

<h2>DESCRIPTION</h2>

 These functions are used to split the number <i>x</i> into a normalized fraction and an exponent which is stored in <i>exp</i>.

<h2>RETURN VALUE</h2>

 These functions return the normalized fraction. If the argument <i>x</i> is not zero, the normalized fraction is <i>x</i> times a power of two, and its absolute value is always in the range 1/2 (inclusive) to 1 (exclusive), that is, [0.5,1). 

 If <i>x</i> is zero, then the normalized fraction is zero and zero is stored in <i>exp</i>. 

 If <i>x</i> is a NaN, a NaN is returned, and the value of <i>*exp</i> is unspecified. 

 If <i>x</i> is positive infinity (negative infinity), positive infinity (negative infinity) is returned, and the value of <i>*exp</i> is unspecified.

<h2>ERRORS</h2>

 No errors occur.

<h2>ATTRIBUTES</h2>

 For an explanation of the terms used in this section, see <b><a HREF="/docs/linux/man/7-attributes/">attributes</a></b>(7). <table BORDER> <tr VALIGN=top><td><b>Interface</b></td><td><b>Attribute</b></td><td><b>Value</b>
</td></tr> <tr VALIGN=top><td> <b>frexp</b>(), <b>frexpf</b>(), <b>frexpl</b>() </td><td>Thread safety</td><td>MT-Safe
</td></tr> </table>

<h2>CONFORMING TO</h2>

 C99, POSIX.1-2001, POSIX.1-2008. 

 The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.

<h2>EXAMPLES</h2>

 The program below produces results such as the following: 

 $<b> ./a.out 2560</b> frexp(2560, &amp;e) = 0.625: 0.625 * 2ha12 = 2560 $<b> ./a.out -4</b> frexp(-4, &amp;e) = -0.5: -0.5 * 2ha3 = -4

<h3>Program source</h3>

 #include &lt;math.h&gt; #include &lt;float.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; 

 int main(int argc, char *argv[]) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double x, r; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int exp; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x&nbsp;=&nbsp;strtod(argv[1], NULL); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;r&nbsp;=&nbsp;frexp(x,&nbsp;&amp;exp); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;frexp(%g,&nbsp;&amp;e)&nbsp;=&nbsp;%g:&nbsp;%g&nbsp;*&nbsp;%dha%d&nbsp;=&nbsp;%g\n&quot;, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x, r, r, FLT_RADIX, exp, x); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/3-ldexp/">ldexp</a></b>(3), <b><a HREF="/docs/linux/man/3-modf/">modf</a></b>(3)

<h2>COLOPHON</h2>

 This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 

<h2>Index</h2>


