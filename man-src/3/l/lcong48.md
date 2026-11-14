---
title: "lcong48(3)"
name: "lcong48"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lcong48/"
description: "drand48, erand48, lrand48, nrand48, mrand48, jrand48, srand48, seed48, lcong48 – generate uniformly distributed pseudo-random numbers"
---

<h2 class="name">NAME</h2>
<p> drand48, erand48, lrand48, nrand48, mrand48, jrand48, srand48, seed48, lcong48 &#8211; generate uniformly distributed pseudo-random numbers </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
double drand48(void);
double erand48(unsigned short xsubi[3]);
long lrand48(void);
long nrand48(unsigned short xsubi[3]);
long mrand48(void);
long jrand48(unsigned short xsubi[3]);
void srand48(long seedval);
unsigned short *seed48(unsigned short seed16v[3]);
void lcong48(unsigned short param[7]);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> All functions shown above: _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> These functions generate pseudo-random numbers using the linear congruential algorithm and 48-bit integer arithmetic. </p>
<p> The <code>drand48</code>() and <code>erand48</code>() functions return nonnegative double-precision floating-point values uniformly distributed over the interval [0.0, 1.0). </p>
<p> The <code>lrand48</code>() and <code>nrand48</code>() functions return nonnegative long integers uniformly distributed over the interval [0, 2^31). </p>
<p> The <code>mrand48</code>() and <code>jrand48</code>() functions return signed long integers uniformly distributed over the interval [-2^31, 2^31). </p>
<p> The <code>srand48</code>(), <code>seed48</code>(), and <code>lcong48</code>() functions are initialization functions, one of which should be called before using <code>drand48</code>(), <code>lrand48</code>() or <code>mrand48</code>(). The functions <code>erand48</code>(), <code>nrand48</code>(), and <code>jrand48</code>() do not require an initialization function to be called first. </p>
<p> All the functions work by generating a sequence of 48-bit integers, <i>Xi</i>, according to the linear congruential formula: </p>
<p> <code>Xn+1 = (aXn + c) mod m, where n &gt;= 0</code> </p>
<p> The parameter <i>m</i> = 2^48, hence 48-bit integer arithmetic is performed. Unless <code>lcong48</code>() is called, <i>a</i> and <i>c</i> are given by: </p>
<p> <code>a = 0x5DEECE66D</code> <code>c = 0xB</code> </p>
<p> The value returned by any of the functions <code>drand48</code>(), <code>erand48</code>(), <code>lrand48</code>(), <code>nrand48</code>(), <code>mrand48</code>() or <code>jrand48</code>() is computed by first generating the next 48-bit <i>Xi</i> in the sequence. Then the appropriate number of bits, according to the type of data item to be returned, is copied from the high-order bits of <i>Xi</i> and transformed into the returned value. </p>
<p> The functions <code>drand48</code>(), <code>lrand48</code>(), and <code>mrand48</code>() store the last 48-bit <i>Xi</i> generated in an internal buffer. The functions <code>erand48</code>(), <code>nrand48</code>(), and <code>jrand48</code>() require the calling program to provide storage for the successive <i>Xi</i> values in the array argument <i>xsubi</i>. The functions are initialized by placing the initial value of <i>Xi</i> into the array before calling the function for the first time. </p>
<p> The initializer function <code>srand48</code>() sets the high order 32-bits of <i>Xi</i> to the argument <i>seedval</i>. The low order 16-bits are set to the arbitrary value 0x330E. </p>
<p> The initializer function <code>seed48</code>() sets the value of <i>Xi</i> to the 48-bit value specified in the array argument <i>seed16v</i>. The previous value of <i>Xi</i> is copied into an internal buffer and a pointer to this buffer is returned by <code>seed48</code>(). </p>
<p> The initialization function <code>lcong48</code>() allows the user to specify initial values for <i>Xi</i>, <i>a</i>, and <i>c</i>. Array argument elements <i>param[0-2]</i> specify <i>Xi</i>, <i>param[3-5]</i> specify <i>a</i>, and <i>param[6]</i> specifies <i>c</i>. After <code>lcong48</code>() has been called, a subsequent call to either <code>srand48</code>() or <code>seed48</code>() will restore the standard values of <i>a</i> and <i>c</i>.</p>
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
<td> <code>drand48</code>(), <code>erand48</code>(), <code>lrand48</code>(), <code>nrand48</code>(), <code>mrand48</code>(), <code>jrand48</code>(), <code>srand48</code>(), <code>seed48</code>(), <code>lcong48</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:drand48
</td>
</tr>
</table>
<p> The above functions record global state information for the random number generator, so they are not thread-safe.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-rand/">rand</a></code>(3), <code><a href="/docs/linux/man/3-random/">random</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
