---
title: "srandom_r(3)"
name: "srandom_r"
section: "3"
letter: "s"
url: "/docs/linux/man/3-srandom_r/"
description: "random_r, srandom_r, initstate_r, setstate_r – reentrant random number generator"
---

<p>random_r, srandom_r, initstate_r, setstate_r &#8211; reentrant random number generator</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

int random_r(struct random_data *buf, int32_t *result);

int srandom_r(unsigned int seed, struct random_data *buf);

int initstate_r(unsigned int seed, char *statebuf,
                size_t statelen, struct random_data *buf);

int setstate_r(char *statebuf, struct random_data *buf);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>random_r</code>(), <code>srandom_r</code>(), <code>initstate_r</code>(), <code>setstate_r</code>():</p>
<dl>
<dd>/* Glibc since 2.19: */ _DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<h2>Description</h2>
<p>These functions are the reentrant equivalents of the functions described in <code><a href="/docs/linux/man/3-random/">random</a></code>(3). They are suitable for use in multithreaded programs where each thread needs to obtain an independent, reproducible sequence of random numbers. </p>
<p> The <code>random_r</code>() function is like <code><a href="/docs/linux/man/3-random/">random</a></code>(3), except that instead of using state information maintained in a global variable, it uses the state information in the argument pointed to by <i>buf</i>, which must have been previously initialized by <code>initstate_r</code>(). The generated random number is returned in the argument <i>result</i>. </p>
<p> The <code>srandom_r</code>() function is like <code><a href="/docs/linux/man/3-srandom/">srandom</a></code>(3), except that it initializes the seed for the random number generator whose state is maintained in the object pointed to by <i>buf</i>, which must have been previously initialized by <code>initstate_r</code>(), instead of the seed associated with the global state variable. </p>
<p> The <code>initstate_r</code>() function is like <code><a href="/docs/linux/man/3-initstate/">initstate</a></code>(3) except that it initializes the state in the object pointed to by <i>buf</i>, rather than initializing the global state variable. Before calling this function, the <i>buf.state</i> field must be initialized to NULL. The <code>initstate_r</code>() function records a pointer to the <i>statebuf</i> argument inside the structure pointed to by <i>buf</i>. Thus, <i>statebuf</i> should not be deallocated so long as <i>buf</i> is still in use. (So, <i>statebuf</i> should typically be allocated as a static variable, or allocated on the heap using <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) or similar.) </p>
<p> The <code>setstate_r</code>() function is like <code><a href="/docs/linux/man/3-setstate/">setstate</a></code>(3) except that it modifies the state in the object pointed to by <i>buf</i>, rather than modifying the global state variable. <i>state</i> must first have been initialized using <code>initstate_r</code>() or be the result of a previous call of <code>setstate_r</code>().</p>
<h2>Return Value</h2>
<p>All of these functions return 0 on success. On error, -1 is returned, with <i>errno</i> set to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>A state array of less than 8 bytes was specified to <code>initstate_r</code>().</p>
<dt><code>EINVAL</code></p>
<dd>The <i>statebuf</i> or <i>buf</i> argument to <code>setstate_r</code>() was NULL.</p>
<dt><code>EINVAL</code></p>
<dd>The <i>buf</i> or <i>result</i> argument to <code>random_r</code>() was NULL.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>random_r</code>(), <code>srandom_r</code>(),<br />
 <code>initstate_r</code>(), <code>setstate_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:buf
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are nonstandard glibc extensions.</p>
<h2>Bugs</h2>
<p>The <code>initstate_r</code>() interface is confusing. It appears that the <i>random_data</i> type is intended to be opaque, but the implementation requires the user to either initialize the <i>buf.state</i> field to NULL or zero out the entire structure before the call.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-drand48/">drand48</a></code>(3), <code><a href="/docs/linux/man/3-rand/">rand</a></code>(3), <code><a href="/docs/linux/man/3-random/">random</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
