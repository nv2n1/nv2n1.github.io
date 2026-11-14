---
title: "initstate(3)"
name: "initstate"
section: "3"
letter: "i"
url: "/docs/linux/man/3-initstate/"
description: "random, srandom, initstate, setstate – random number generator"
---

<h2 class="name">NAME</h2>
<p> random, srandom, initstate, setstate &#8211; random number generator </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
long random(void);
void srandom(unsigned seed);
char *initstate(unsigned seed, char *state, size_t n);
char *setstate(char *state);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>random</code>(), <code>srandom</code>(), <code>initstate</code>(), <code>setstate</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>random</code>() function uses a nonlinear additive feedback random number generator employing a default table of size 31 long integers to return successive pseudo-random numbers in the range from 0 to 2^31 &#8211; 1. The period of this random number generator is very large, approximately <i>16&nbsp;*&nbsp;((2^31)&nbsp;&#8211; 1)</i>. </p>
<p> The <code>srandom</code>() function sets its argument as the seed for a new sequence of pseudo-random integers to be returned by <code>random</code>(). These sequences are repeatable by calling <code>srandom</code>() with the same seed value. If no seed value is provided, the <code>random</code>() function is automatically seeded with a value of 1. </p>
<p> The <code>initstate</code>() function allows a state array <i>state</i> to be initialized for use by <code>random</code>(). The size of the state array <i>n</i> is used by <code>initstate</code>() to decide how sophisticated a random number generator it should use&#8212;the larger the state array, the better the random numbers will be. Current &quot;optimal&quot; values for the size of the state array <i>n</i> are 8, 32, 64, 128, and 256 bytes; other amounts will be rounded down to the nearest known amount. Using less than 8 bytes results in an error. <i>seed</i> is the seed for the initialization, which specifies a starting point for the random number sequence, and provides for restarting at the same point. </p>
<p> The <code>setstate</code>() function changes the state array used by the <code>random</code>() function. The state array <i>state</i> is used for random number generation until the next call to <code>initstate</code>() or <code>setstate</code>(). <i>state</i> must first have been initialized using <code>initstate</code>() or be the result of a previous call of <code>setstate</code>().</p>
<h2>RETURN VALUE</h2>
<p> The <code>random</code>() function returns a value between 0 and <i>(2^31)&nbsp;&#8211; 1</i>. The <code>srandom</code>() function returns no value. </p>
<p> The <code>initstate</code>() function returns a pointer to the previous state array. On error, <i>errno</i> is set to indicate the cause. </p>
<p> On success, <code>setstate</code>() returns a pointer to the previous state array. On error, it returns NULL, with <i>errno</i> set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The <i>state</i> argument given to <code>setstate</code>() was NULL.</p>
<dt><code>EINVAL</code></p>
<dd> A state array of less than 8 bytes was specified to <code>initstate</code>().</dl>
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
<td> <code>random</code>(), <code>srandom</code>(),<br />
 <code>initstate</code>(), <code>setstate</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>NOTES</h2>
<p> The <code>random</code>() function should not be used in multithreaded programs where reproducible behavior is required. Use <code><a href="/docs/linux/man/3-random_r/">random_r</a></code>(3) for that purpose. </p>
<p> Random-number generation is a complex topic. <i>Numerical Recipes in C: The Art of Scientific Computing</i> (William H. Press, Brian P. Flannery, Saul A. Teukolsky, William T. Vetterling; New York: Cambridge University Press, 2007, 3rd ed.) provides an excellent discussion of practical random-number generation issues in Chapter 7 (Random Numbers). </p>
<p> For a more theoretical discussion which also covers many practical issues in depth, see Chapter 3 (Random Numbers) in Donald E. Knuth&#8217;s <i>The Art of Computer Programming</i>, volume 2 (Seminumerical Algorithms), 2nd ed.; Reading, Massachusetts: Addison-Wesley Publishing Company, 1981.</p>
<h2>BUGS</h2>
<p> According to POSIX, <code>initstate</code>() should return NULL on error. In the glibc implementation, <i>errno</i> is (as specified) set on error, but the function does not return NULL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2), <code><a href="/docs/linux/man/3-drand48/">drand48</a></code>(3), <code><a href="/docs/linux/man/3-rand/">rand</a></code>(3), <code><a href="/docs/linux/man/3-random_r/">random_r</a></code>(3), <code><a href="/docs/linux/man/3-srand/">srand</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
