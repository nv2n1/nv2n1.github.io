---
title: "pthread_attr_getsigmask_np(3)"
name: "pthread_attr_getsigmask_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_getsigmask_np/"
description: "pthread_attr_setsigmask_np, pthread_attr_getsigmask_np – set/get signal mask attribute in thread attributes object"
---

<p>pthread_attr_setsigmask_np, pthread_attr_getsigmask_np &#8211; set/get signal mask attribute in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pthread.h&gt;

int pthread_attr_setsigmask_np(pthread_attr_t *attr,
                               const sigset_t *sigmask);
int pthread_attr_getsigmask_np(const pthread_attr_t *attr,
                               sigset_t *sigmask);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_attr_setsigmask_np</code>() function sets the signal mask attribute of the thread attributes object referred to by <i>attr</i> to the value specified in <i>*sigmask</i>. If <i>sigmask</i> is specified as NULL, then any existing signal mask attribute in <i>attr</i> is unset. </p>
<p> The <code>pthread_attr_getsigmask_np</code>() function returns the signal mask attribute of the thread attributes object referred to by <i>attr</i> in the buffer pointed to by <i>sigmask</i>. If the signal mask attribute is currently unset, then this function returns the special value <code>PTHREAD_ATTR_NO_SIGMASK_NP</code> as its result.</p>
<h2>Return Value</h2>
<p>The <code>pthread_attr_setsigmask_np</code>() function returns 0 on success, or a nonzero error number on failure. </p>
<p> the <code>pthread_attr_getsigmask_np</code>() function returns either 0 or <code>PTHREAD_ATTR_NO_SIGMASK_NP</code>. When 0 is returned, the signal mask attribute is returned via <i>sigmask</i>. A return value of <code>PTHREAD_ATTR_NO_SIGMASK_NP</code> indicates that the signal mask attribute is not set in <i>attr</i>. </p>
<p> On error, these functions return a positive error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd>(<code>pthread_attr_setsigmask_np</code>()) Could not allocate memory.</dl>
<h2>Versions</h2>
<p>These functions are provided by glibc since version 2.32.</p>
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
<td> <code>pthread_attr_setsigmask_np</code>(), <code>pthread_attr_getsigmask_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are nonstandard GNU extensions; hence the suffix &quot;_np&quot; (nonportable) in the names.</p>
<h2>Notes</h2>
<p>The signal mask attribute determines the signal mask that will be assigned to a thread created using the thread attributes object <i>attr</i>. If this attribute is not set, then a thread created using <i>attr</i> will inherit a copy of the creating thread&#8217;s signal mask. </p>
<p> For more details on signal masks, see <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2). For a description of a set of macros that can be used to manipulate and inspect signals sets, see <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3). </p>
<p> In the absence of <code>pthread_attr_setsigmask_np</code>() it is possible to create a thread with a desired signal mask as follows:</p>
<dl>
<dt>&bull;</p>
<dd>The creating thread uses <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3) to save its current signal mask and set its mask to block all signals.</p>
<dt>&bull;</p>
<dd>The new thread is then created using <code>pthread_create</code>(); the new thread will inherit the creating thread&#8217;s signal mask.</p>
<dt>&bull;</p>
<dd>The new thread sets its signal mask to the desired value using <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3).</p>
<dt>&bull;</p>
<dd>The creating thread restores its signal mask to the original value.</dl>
<p> Following the above steps, there is no possibility for the new thread to receive a signal before it has adjusted its signal mask to the desired value.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-signals/">signals</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
