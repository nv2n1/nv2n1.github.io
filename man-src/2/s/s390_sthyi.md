---
title: "s390_sthyi(2)"
name: "s390_sthyi"
section: "2"
letter: "s"
url: "/docs/linux/man/2-s390_sthyi/"
description: "s390_sthyi – emulate STHYI instruction"
---

<h2 class="name">NAME</h2>
<p> s390_sthyi &#8211; emulate STHYI instruction </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;asm/unistd.h&gt;
int s390_sthyi(unsigned long function_code, void *resp_buffer,
               uint64_t *return_code, unsigned long flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>s390_sthyi</code>() system call emulates the STHYI (Store Hypervisor Information) instruction. It provides hardware resource information for the machine and its virtualization levels. This includes CPU type and capacity, as well as the machine model and other metrics. </p>
<p> The <i>function_code</i> argument indicates which function to perform. The following code(s) are supported:</p>
<dl>
<dt>0</p>
<dd> Return CP (Central Processor) and IFL (Integrated Facility for Linux) capacity information.</dl>
<p> The <i>resp_buffer</i> argument specifies the address of a response buffer. When the <i>function_code</i> is 0, the buffer must be one page (4K) in size. If the system call returns 0, the response buffer will be filled with CPU capacity information. Otherwise, the response buffer&#8217;s content is unchanged. </p>
<p> The <i>return_code</i> argument stores the return code of the STHYI instruction, using one of the following values:</p>
<dl>
<dt>0</p>
<dd> Success.</p>
<dt>4</p>
<dd> Unsupported function code.</dl>
<p> For further details about <i>return_code</i>, <i>function_code</i>, and <i>resp_buffer</i>, see the reference given in NOTES. </p>
<p> The <i>flags</i> argument is provided to allow for future extensions and currently must be set to 0.</p>
<h2>RETURN VALUE</h2>
<p> On success (that is: emulation succeeded), the return value of <code>s390_sthyi</code>() matches the condition code of the STHYI instructions, which is a value in the range [0..3]. A return value of 0 indicates that CPU capacity information is stored in <i>*resp_buffer</i>. A return value of 3 indicates &quot;unsupported function code&quot; and the content of <i>*resp_buffer</i> is unchanged. The return values 1 and 2 are reserved. </p>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> The value specified in <i>resp_buffer</i> or <i>return_code</i> is not a valid address.</p>
<dt><code>EINVAL</code></p>
<dd> The value specified in <i>flags</i> is nonzero.</p>
<dt><code>ENOMEM</code></p>
<dd> Allocating memory for handling the CPU capacity information failed.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The value specified in <i>function_code</i> is not valid.</dl>
<h2>VERSIONS</h2>
<p> This system call is available since Linux 4.15.</p>
<h2>CONFORMING TO</h2>
<p> This Linux-specific system call is available only on the s390 architecture.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call, use <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) to call it. </p>
<p> For details of the STHYI instruction, see the documentation page </p>
<p> When the system call interface is used, the response buffer doesn&#8217;t have to fulfill alignment requirements described in the STHYI instruction definition. </p>
<p> The kernel caches the response (for up to one second, as of Linux 4.16). Subsequent system call invocations may return the cached response.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
