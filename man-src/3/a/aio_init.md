---
title: "aio_init(3)"
name: "aio_init"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aio_init/"
description: "aio_init – asynchronous I/O initialization"
---

<h2 class="name">NAME</h2>
<p> aio_init &#8211; asynchronous I/O initialization </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;aio.h&gt;
void aio_init(const struct aioinit *init);
</code></pre>
<p> Link with <i>-lrt</i>.</p>
<h2>DESCRIPTION</h2>
<p> The GNU-specific <code>aio_init</code>() function allows the caller to provide tuning hints to the glibc POSIX AIO implementation. Use of this function is optional, but to be effective, it must be called before employing any other functions in the POSIX AIO API. </p>
<p> The tuning information is provided in the buffer pointed to by the argument <i>init</i>. This buffer is a structure of the following form: </p>
<p> struct aioinit {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int aio_threads;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of threads&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int aio_num;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of expected simultaneous<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requests&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int aio_locks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Not used&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int aio_usedba;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Not used&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int aio_debug;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Not used&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int aio_numusers;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Not used&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int aio_idle_time;&nbsp;<wbr>&nbsp;/*&nbsp;Number of seconds before idle thread<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;terminates&nbsp;(since glibc 2.2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int aio_reserved; }; </p>
<p> The following fields are used in the <i>aioinit</i> structure:</p>
<dl>
<dt><i>aio_threads</i></p>
<dd> This field specifies the maximum number of worker threads that may be used by the implementation. If the number of outstanding I/O operations exceeds this limit, then excess operations will be queued until a worker thread becomes free. If this field is specified with a value less than 1, the value 1 is used. The default value is 20.</p>
<dt><i>aio_num</i></p>
<dd> This field should specify the maximum number of simultaneous I/O requests that the caller expects to enqueue. If a value less than 32 is specified for this field, it is rounded up to 32. The default value is 64.</p>
<dt><i>aio_idle_time</i></p>
<dd> This field specifies the amount of time in seconds that a worker thread should wait for further requests before terminating, after having completed a previous request. The default value is 1.</dl>
<h2>VERSIONS</h2>
<p> The <code>aio_init</code>() function is available since glibc 2.1.</p>
<h2>CONFORMING TO</h2>
<p> This function is a GNU extension.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
