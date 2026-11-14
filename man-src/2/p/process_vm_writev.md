---
title: "process_vm_writev(2)"
name: "process_vm_writev"
section: "2"
letter: "p"
url: "/docs/linux/man/2-process_vm_writev/"
description: "process_vm_readv, process_vm_writev – transfer data between process address spaces"
---

<h2 class="name">NAME</h2>
<p> process_vm_readv, process_vm_writev &#8211; transfer data between process address spaces </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/uio.h&gt;
ssize_t process_vm_readv(pid_t pid,
                         const struct iovec *local_iov,
                         unsigned long liovcnt,
                         const struct iovec *remote_iov,
                         unsigned long riovcnt,
                         unsigned long flags);
ssize_t process_vm_writev(pid_t pid,
                          const struct iovec *local_iov,
                          unsigned long liovcnt,
                          const struct iovec *remote_iov,
                          unsigned long riovcnt,
                          unsigned long flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>process_vm_readv</code>(), <code>process_vm_writev</code>():</p>
<dl>
<dt>
<dd> <code>_GNU_SOURCE</code></dl>
<h2>DESCRIPTION</h2>
<p> These system calls transfer data between the address space of the calling process (&quot;the local process&quot;) and the process identified by <i>pid</i> (&quot;the remote process&quot;). The data moves directly between the address spaces of the two processes, without passing through kernel space. </p>
<p> The <code>process_vm_readv</code>() system call transfers data from the remote process to the local process. The data to be transferred is identified by <i>remote_iov</i> and <i>riovcnt</i>: <i>remote_iov</i> is a pointer to an array describing address ranges in the process <i>pid</i>, and <i>riovcnt</i> specifies the number of elements in <i>remote_iov</i>. The data is transferred to the locations specified by <i>local_iov</i> and <i>liovcnt</i>: <i>local_iov</i> is a pointer to an array describing address ranges in the calling process, and <i>liovcnt</i> specifies the number of elements in <i>local_iov</i>. </p>
<p> The <code>process_vm_writev</code>() system call is the converse of <code>process_vm_readv</code>()&#8212;it transfers data from the local process to the remote process. Other than the direction of the transfer, the arguments <i>liovcnt</i>, <i>local_iov</i>, <i>riovcnt</i>, and <i>remote_iov</i> have the same meaning as for <code>process_vm_readv</code>(). </p>
<p> The <i>local_iov</i> and <i>remote_iov</i> arguments point to an array of <i>iovec</i> structures, defined in <i>&lt;sys/uio.h&gt;</i> as: </p>
<p> struct iovec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;*iov_base;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Starting address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t iov_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes to transfer&nbsp;*/ }; </p>
<p> Buffers are processed in array order. This means that <code>process_vm_readv</code>() completely fills <i>local_iov[0]</i> before proceeding to <i>local_iov[1]</i>, and so on. Likewise, <i>remote_iov[0]</i> is completely read before proceeding to <i>remote_iov[1]</i>, and so on. </p>
<p> Similarly, <code>process_vm_writev</code>() writes out the entire contents of <i>local_iov[0]</i> before proceeding to <i>local_iov[1]</i>, and it completely fills <i>remote_iov[0]</i> before proceeding to <i>remote_iov[1]</i>. </p>
<p> The lengths of <i>remote_iov[i].iov_len</i> and <i>local_iov[i].iov_len</i> do not have to be the same. Thus, it is possible to split a single local buffer into multiple remote buffers, or vice versa. </p>
<p> The <i>flags</i> argument is currently unused and must be set to 0. </p>
<p> The values specified in the <i>liovcnt</i> and <i>riovcnt</i> arguments must be less than or equal to <code>IOV_MAX</code> (defined in <i>&lt;limits.h&gt;</i> or accessible via the call <i>sysconf(_SC_IOV_MAX)</i>). </p>
<p> The count arguments and <i>local_iov</i> are checked before doing any transfers. If the counts are too big, or <i>local_iov</i> is invalid, or the addresses refer to regions that are inaccessible to the local process, none of the vectors will be processed and an error will be returned immediately. </p>
<p> Note, however, that these system calls do not check the memory regions in the remote process until just before doing the read/write. Consequently, a partial read/write (see RETURN VALUE) may result if one of the <i>remote_iov</i> elements points to an invalid memory region in the remote process. No further reads/writes will be attempted beyond that point. Keep this in mind when attempting to read data of unknown length (such as C strings that are null-terminated) from a remote process, by avoiding spanning memory pages (typically 4 KiB) in a single remote <i>iovec</i> element. (Instead, split the remote read into two <i>remote_iov</i> elements and have them merge back into a single write <i>local_iov</i> entry. The first read entry goes up to the page boundary, while the second starts on the next page boundary.) </p>
<p> Permission to read from or write to another process is governed by a ptrace access mode <code>PTRACE_MODE_ATTACH_REALCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>process_vm_readv</code>() returns the number of bytes read and <code>process_vm_writev</code>() returns the number of bytes written. This return value may be less than the total number of requested bytes, if a partial read/write occurred. (Partial transfers apply at the granularity of <i>iovec</i> elements. These system calls won&#8217;t perform a partial transfer that splits a single <i>iovec</i> element.) The caller should check the return value to determine whether a partial read/write occurred. </p>
<p> On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> The memory described by <i>local_iov</i> is outside the caller&#8217;s accessible address space.</p>
<dt><code>EFAULT</code></p>
<dd> The memory described by <i>remote_iov</i> is outside the accessible address space of the process <i>pid</i>.</p>
<dt><code>EINVAL</code></p>
<dd> The sum of the <i>iov_len</i> values of either <i>local_iov</i> or <i>remote_iov</i> overflows a <i>ssize_t</i> value.</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> is not 0.</p>
<dt><code>EINVAL</code></p>
<dd> <i>liovcnt</i> or <i>riovcnt</i> is too large.</p>
<dt><code>ENOMEM</code></p>
<dd> Could not allocate memory for internal copies of the <i>iovec</i> structures.</p>
<dt><code>EPERM</code></p>
<dd> The caller does not have permission to access the address space of the process <i>pid</i>.</p>
<dt><code>ESRCH</code></p>
<dd> No process with ID <i>pid</i> exists.</dl>
<h2>VERSIONS</h2>
<p> These system calls were added in Linux 3.2. Support is provided in glibc since version 2.15.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are nonstandard Linux extensions.</p>
<h2>NOTES</h2>
<p> The data transfers performed by <code>process_vm_readv</code>() and <code>process_vm_writev</code>() are not guaranteed to be atomic in any way. </p>
<p> These system calls were designed to permit fast message passing by allowing messages to be exchanged with a single copy operation (rather than the double copy that would be required when using, for example, shared memory or pipes).</p>
<h2>EXAMPLES</h2>
<p> The following code sample demonstrates the use of <code>process_vm_readv</code>(). It reads 20 bytes at the address 0x10000 from the process with PID 10 and writes the first 10 bytes into <i>buf1</i> and the second 10 bytes into <i>buf2</i>. </p>
<p> #include &lt;sys/uio.h&gt; </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct iovec local[2];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct iovec remote[1];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf1[10];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf2[10];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t nread;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t pid&nbsp;=&nbsp;10;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID of remote process&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;local[0].iov_base&nbsp;=&nbsp;buf1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;local[0].iov_len&nbsp;=&nbsp;10;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;local[1].iov_base&nbsp;=&nbsp;buf2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;local[1].iov_len&nbsp;=&nbsp;10;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;remote[0].iov_base&nbsp;=&nbsp;(void&nbsp;*)&nbsp;0x10000;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;remote[0].iov_len&nbsp;=&nbsp;20; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nread&nbsp;=&nbsp;process_vm_readv(pid, local, 2, remote, 1, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nread&nbsp;!=&nbsp;20)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0; }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2), <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
