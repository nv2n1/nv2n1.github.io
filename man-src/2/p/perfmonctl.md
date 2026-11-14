---
title: "perfmonctl(2)"
name: "perfmonctl"
section: "2"
letter: "p"
url: "/docs/linux/man/2-perfmonctl/"
description: "perfmonctl – interface to IA-64 performance monitoring unit"
---

<h2 class="name">NAME</h2>
<p> perfmonctl &#8211; interface to IA-64 performance monitoring unit </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;perfmon.h&gt;
#include &lt;syscall.h&gt;
long perfmonctl(int fd, int cmd, void *arg, int narg);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The IA-64-specific <code>perfmonctl</code>() system call provides an interface to the PMU (performance monitoring unit). The PMU consists of PMD (performance monitoring data) registers and PMC (performance monitoring control) registers, which gather hardware statistics. </p>
<p> <code>perfmonctl</code>() applies the operation <i>cmd</i> to the input arguments specified by <i>arg</i>. The number of arguments is defined by <i>narg</i>. The <i>fd</i> argument specifies the perfmon context to operate on. </p>
<p> Supported values for <i>cmd</i> are:</p>
<dl>
<dt><code>PFM_CREATE_CONTEXT</code></p>
<dd>
perfmonctl(int fd, PFM_CREATE_CONTEXT, pfarg_context_t *ctxt, 1);<br />
 Set up a context.</p>
<dt>
<dd> The <i>fd</i> parameter is ignored. A new perfmon context is created as specified in <i>ctxt</i> and its file descriptor is returned in <i>ctxt-&gt;ctx_fd</i>.</p>
<dt>
<dd> The file descriptor can be used in subsequent calls to <code>perfmonctl</code>() and can be used to read event notifications (type <i>pfm_msg_t</i>) using <code><a href="/docs/linux/man/2-read/">read</a></code>(2). The file descriptor is pollable using <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7).</p>
<dt>
<dd> The context can be destroyed by calling <code><a href="/docs/linux/man/2-close/">close</a></code>(2) on the file descriptor.</p>
<dt><code>PFM_WRITE_PMCS</code></p>
<dd>
perfmonctl(int fd, PFM_WRITE_PMCS, pfarg_reg_t *pmcs, n);<br />
 Set PMC registers.</p>
<dt><code>PFM_WRITE_PMDS</code></p>
<dd>
perfmonctl(int fd, PFM_WRITE_PMDS, pfarg_reg_t *pmds, n);<br />
 Set PMD registers.</p>
<dt><code>PFM_READ_PMDS</code></p>
<dd>
perfmonctl(int fd, PFM_READ_PMDS, pfarg_reg_t *pmds, n);<br />
 Read PMD registers.</p>
<dt><code>PFM_START</code></p>
<dd>
perfmonctl(int fd, PFM_START, NULL, 0);<br />
 Start monitoring.</p>
<dt><code>PFM_STOP</code></p>
<dd>
perfmonctl(int fd, PFM_STOP, NULL, 0);<br />
 Stop monitoring.</p>
<dt><code>PFM_LOAD_CONTEXT</code></p>
<dd>
perfmonctl(int fd, PFM_LOAD_CONTEXT, pfarg_load_t *largs, 1);<br />
 Attach the context to a thread.</p>
<dt><code>PFM_UNLOAD_CONTEXT</code></p>
<dd>
perfmonctl(int fd, PFM_UNLOAD_CONTEXT, NULL, 0);<br />
 Detach the context from a thread.</p>
<dt><code>PFM_RESTART</code></p>
<dd>
perfmonctl(int fd, PFM_RESTART, NULL, 0);<br />
 Restart monitoring after receiving an overflow notification.</p>
<dt><code>PFM_GET_FEATURES</code></p>
<dd>
perfmonctl(int fd, PFM_GET_FEATURES, pfarg_features_t *arg, 1);</p>
<dt><code>PFM_DEBUG</code></p>
<dd>
perfmonctl(int fd, PFM_DEBUG, val, 0);<br />
 If <i>val</i> is nonzero, enable debugging mode, otherwise disable.</p>
<dt><code>PFM_GET_PMC_RESET_VAL</code></p>
<dd>
<pre><code>
perfmonctl(int fd, PFM_GET_PMC_RESET_VAL, pfarg_reg_t *req, n);
</code></pre>
<p> Reset PMC registers to default values.</dl>
<h2>RETURN VALUE</h2>
<p> <code>perfmonctl</code>() returns zero when the operation is successful. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>VERSIONS</h2>
<p> <code>perfmonctl</code>() is available since Linux 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>perfmonctl</code>() is Linux-specific and is available only on the IA-64 architecture.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gprof/">gprof</a></code>(1) </p>
<p> The perfmon2 interface specification</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
