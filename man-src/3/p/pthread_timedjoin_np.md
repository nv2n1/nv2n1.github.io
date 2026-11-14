---
title: "pthread_timedjoin_np(3)"
name: "pthread_timedjoin_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_timedjoin_np/"
description: "pthread_tryjoin_np, pthread_timedjoin_np – try to join with a terminated thread"
---

<p>pthread_tryjoin_np, pthread_timedjoin_np &#8211; try to join with a terminated thread</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pthread.h&gt;

int pthread_tryjoin_np(pthread_t thread, void **retval);

int pthread_timedjoin_np(pthread_t thread, void **retval,
                         const struct timespec *abstime);</code></pre>
<p> Compile and link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p>These functions operate in the same way as <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3), except for the differences described on this page. The <code>pthread_tryjoin_np</code>() function performs a nonblocking join with the thread <i>thread</i>, returning the exit status of the thread in <i>*retval</i>. If <i>thread</i> has not yet terminated, then instead of blocking, as is done by <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3), the call returns an error. The <code>pthread_timedjoin_np</code>() function performs a join-with-timeout. If <i>thread</i> has not yet terminated, then the call blocks until a maximum time, specified in <i>abstime</i>, measured against the <code>CLOCK_REALTIME</code> clock. If the timeout expires before <i>thread</i> terminates, the call returns an error. The <i>abstime</i> argument is a structure of the following form, specifying an absolute time measured since the Epoch (see <code><a href="/docs/linux/man/2-time/">time</a></code>(2)): struct timespec {<br />
    time_t tv_sec; /* seconds */<br />
    long tv_nsec;  /* nanoseconds */<br />
};</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return an error number.</p>
<h2>Errors</h2>
<p>These functions can fail with the same errors as <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3). <code>pthread_tryjoin_np</code>() can in addition fail with the following error:</p>
<dl>
<dt><code>EBUSY</code></p>
<dd><i>thread</i> had not yet terminated at the time of the call.</dl>
<p> <code>pthread_timedjoin_np</code>() can in addition fail with the following errors:</p>
<dl>
<dt><code>ETIMEDOUT</code></p>
<dd>The call timed out before <i>thread</i> terminated.</p>
<dt><code>EINVAL</code></p>
<dd><i>abstime</i> value is invalid (<i>tv_sec</i> is less than 0 or <i>tv_nsec</i> is greater than 1e9).</dl>
<p> <code>pthread_timedjoin_np</code>() never returns the error <code>EINTR</code>.</p>
<h2>Versions</h2>
<p>These functions first appeared in glibc in version 2.3.3.</p>
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
<td> <code>pthread_tryjoin_np</code>(), <code>pthread_timedjoin_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are nonstandard GNU extensions; hence the suffix &quot;_np&quot; (nonportable) in the names.</p>
<h2>Examples</h2>
<p>The following code waits to join for up to 5 seconds: struct timespec ts;<br />
int s; &#8230; </p>
<pre><code>if (clock_gettime(CLOCK_REALTIME, &amp;ts) == -1) {
    /* Handle error */
}
ts.tv_sec += 5;
s = pthread_timedjoin_np(thread, NULL, &amp;ts);
if (s != 0) {
    /* Handle error */
}</code></pre>
<h2>Bugs</h2>
<p>The <code>pthread_timedjoin_np</code>() function measures time by internally calculating a relative sleep interval that is then measured against the <code>CLOCK_MONOTONIC</code> clock instead of the <code>CLOCK_REALTIME</code> clock. Consequently, the timeout is unaffected by discontinuous changes to the <code>CLOCK_REALTIME</code> clock.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3), <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
