---
title: "ioctl_userfaultfd(2)"
name: "ioctl_userfaultfd"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl_userfaultfd/"
description: "ioctl_userfaultfd – create a file descriptor for handling page faults in user space"
---

<h2 class="name">NAME</h2>
<p> ioctl_userfaultfd &#8211; create a file descriptor for handling page faults in user space </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/ioctl.h&gt;
int ioctl(int fd, int cmd, ...);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Various <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations can be performed on a userfaultfd object (created by a call to <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2)) using calls of the form: </p>
<p> ioctl(fd, cmd, argp); In the above, <i>fd</i> is a file descriptor referring to a userfaultfd object, <i>cmd</i> is one of the commands listed below, and <i>argp</i> is a pointer to a data structure that is specific to <i>cmd</i>. </p>
<p> The various <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations are described below. The <code>UFFDIO_API</code>, <code>UFFDIO_REGISTER</code>, and <code>UFFDIO_UNREGISTER</code> operations are used to <i>configure</i> userfaultfd behavior. These operations allow the caller to choose what features will be enabled and what kinds of events will be delivered to the application. The remaining operations are <i>range</i> operations. These operations enable the calling application to resolve page-fault events.</p>
<h3>UFFDIO_API</h3>
<p> (Since Linux 4.3.) Enable operation of the userfaultfd and perform API handshake. </p>
<p> The <i>argp</i> argument is a pointer to a <i>uffdio_api</i> structure, defined as: </p>
<p> struct uffdio_api {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 api;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Requested API version&nbsp;(input)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 features;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Requested features&nbsp;(input/output)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 ioctls;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Available ioctl()&nbsp;operations&nbsp;(output)&nbsp;*/ }; </p>
<p> The <i>api</i> field denotes the API version requested by the application. </p>
<p> The kernel verifies that it can support the requested API version, and sets the <i>features</i> and <i>ioctls</i> fields to bit masks representing all the available features and the generic <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations available. </p>
<p> For Linux kernel versions before 4.11, the <i>features</i> field must be initialized to zero before the call to <code>UFFDIO_API</code>, and zero (i.e., no feature bits) is placed in the <i>features</i> field by the kernel upon return from <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2). </p>
<p> Starting from Linux 4.11, the <i>features</i> field can be used to ask whether particular features are supported and explicitly enable userfaultfd features that are disabled by default. The kernel always reports all the available features in the <i>features</i> field. </p>
<p> To enable userfaultfd features the application should set a bit corresponding to each feature it wants to enable in the <i>features</i> field. If the kernel supports all the requested features it will enable them. Otherwise it will zero out the returned <i>uffdio_api</i> structure and return <code>EINVAL</code>. </p>
<p> The following feature bits may be set:</p>
<dl>
<dt><code>UFFD_FEATURE_EVENT_FORK</code> (since Linux 4.11)</p>
<dd> When this feature is enabled, the userfaultfd objects associated with a parent process are duplicated into the child process during <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and a <code>UFFD_EVENT_FORK</code> event is delivered to the userfaultfd monitor</p>
<dt><code>UFFD_FEATURE_EVENT_REMAP</code> (since Linux 4.11)</p>
<dd> If this feature is enabled, when the faulting process invokes <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2), the userfaultfd monitor will receive an event of type <code>UFFD_EVENT_REMAP</code>.</p>
<dt><code>UFFD_FEATURE_EVENT_REMOVE</code> (since Linux 4.11)</p>
<dd> If this feature is enabled, when the faulting process calls <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) with the <code>MADV_DONTNEED</code> or <code>MADV_REMOVE</code> advice value to free a virtual memory area the userfaultfd monitor will receive an event of type <code>UFFD_EVENT_REMOVE</code>.</p>
<dt><code>UFFD_FEATURE_EVENT_UNMAP</code> (since Linux 4.11)</p>
<dd> If this feature is enabled, when the faulting process unmaps virtual memory either explicitly with <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2), or implicitly during either <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) or <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2). the userfaultfd monitor will receive an event of type <code>UFFD_EVENT_UNMAP</code>.</p>
<dt><code>UFFD_FEATURE_MISSING_HUGETLBFS</code> (since Linux 4.11)</p>
<dd> If this feature bit is set, the kernel supports registering userfaultfd ranges on hugetlbfs virtual memory areas</p>
<dt><code>UFFD_FEATURE_MISSING_SHMEM</code> (since Linux 4.11)</p>
<dd> If this feature bit is set, the kernel supports registering userfaultfd ranges on shared memory areas. This includes all kernel shared memory APIs: System V shared memory, <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5), shared mappings of <i>/dev/zero</i>, <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) with the <code>MAP_SHARED</code> flag set, <code><a href="/docs/linux/man/2-memfd_create/">memfd_create</a></code>(2), and so on.</p>
<dt><code>UFFD_FEATURE_SIGBUS</code> (since Linux 4.14)</p>
<dd> If this feature bit is set, no page-fault events (<code>UFFD_EVENT_PAGEFAULT</code>) will be delivered. Instead, a <code>SIGBUS</code> signal will be sent to the faulting process. Applications using this feature will not require the use of a userfaultfd monitor for processing memory accesses to the regions registered with userfaultfd.</dl>
<p> The returned <i>ioctls</i> field can contain the following bits:</p>
<dl>
<dt><code>1 &lt;&lt; _UFFDIO_API</code></p>
<dd> The <code>UFFDIO_API</code> operation is supported.</p>
<dt><code>1 &lt;&lt; _UFFDIO_REGISTER</code></p>
<dd> The <code>UFFDIO_REGISTER</code> operation is supported.</p>
<dt><code>1 &lt;&lt; _UFFDIO_UNREGISTER</code></p>
<dd> The <code>UFFDIO_UNREGISTER</code> operation is supported.</dl>
<p> This <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation returns 0 on success. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error. Possible errors include:</p>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>argp</i> refers to an address that is outside the calling process&#8217;s accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The userfaultfd has already been enabled by a previous <code>UFFDIO_API</code> operation.</p>
<dt><code>EINVAL</code></p>
<dd> The API version requested in the <i>api</i> field is not supported by this kernel, or the <i>features</i> field passed to the kernel includes feature bits that are not supported by the current kernel version.</dl>
<h3>UFFDIO_REGISTER</h3>
<p> (Since Linux 4.3.) Register a memory address range with the userfaultfd object. The pages in the range must be &quot;compatible&quot;. </p>
<p> Up to Linux kernel 4.11, only private anonymous ranges are compatible for registering with <code>UFFDIO_REGISTER</code>. </p>
<p> Since Linux 4.11, hugetlbfs and shared memory ranges are also compatible with <code>UFFDIO_REGISTER</code>. </p>
<p> The <i>argp</i> argument is a pointer to a <i>uffdio_register</i> structure, defined as: </p>
<p> struct uffdio_range {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 start;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Start of range&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Length of range&nbsp;(bytes)&nbsp;*/ }; </p>
<p> struct uffdio_register {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct uffdio_range range;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Desired mode of operation&nbsp;(input)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 ioctls;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Available ioctl()&nbsp;operations&nbsp;(output)&nbsp;*/ }; </p>
<p> The <i>range</i> field defines a memory range starting at <i>start</i> and continuing for <i>len</i> bytes that should be handled by the userfaultfd. </p>
<p> The <i>mode</i> field defines the mode of operation desired for this memory region. The following values may be bitwise ORed to set the userfaultfd mode for the specified range:</p>
<dl>
<dt><code>UFFDIO_REGISTER_MODE_MISSING</code></p>
<dd> Track page faults on missing pages.</p>
<dt><code>UFFDIO_REGISTER_MODE_WP</code></p>
<dd> Track page faults on write-protected pages.</dl>
<p> Currently, the only supported mode is <code>UFFDIO_REGISTER_MODE_MISSING</code>. </p>
<p> If the operation is successful, the kernel modifies the <i>ioctls</i> bit-mask field to indicate which <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations are available for the specified range. This returned bit mask is as for <code>UFFDIO_API</code>. </p>
<p> This <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation returns 0 on success. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error. Possible errors include:</p>
<dl>
<dt><code>EBUSY</code></p>
<dd> A mapping in the specified range is registered with another userfaultfd object.</p>
<dt><code>EFAULT</code></p>
<dd> <i>argp</i> refers to an address that is outside the calling process&#8217;s accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid or unsupported bit was specified in the <i>mode</i> field; or the <i>mode</i> field was zero.</p>
<dt><code>EINVAL</code></p>
<dd> There is no mapping in the specified address range.</p>
<dt><code>EINVAL</code></p>
<dd> <i>range.start</i> or <i>range.len</i> is not a multiple of the system page size; or, <i>range.len</i> is zero; or these fields are otherwise invalid.</p>
<dt><code>EINVAL</code></p>
<dd> There as an incompatible mapping in the specified address range.</dl>
<h3>UFFDIO_UNREGISTER</h3>
<p> (Since Linux 4.3.) Unregister a memory address range from userfaultfd. The pages in the range must be &quot;compatible&quot; (see the description of <code>UFFDIO_REGISTER</code>.) </p>
<p> The address range to unregister is specified in the <i>uffdio_range</i> structure pointed to by <i>argp</i>. </p>
<p> This <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation returns 0 on success. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error. Possible errors include:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> Either the <i>start</i> or the <i>len</i> field of the <i>ufdio_range</i> structure was not a multiple of the system page size; or the <i>len</i> field was zero; or these fields were otherwise invalid.</p>
<dt><code>EINVAL</code></p>
<dd> There as an incompatible mapping in the specified address range.</p>
<dt><code>EINVAL</code></p>
<dd> There was no mapping in the specified address range.</dl>
<h3>UFFDIO_COPY</h3>
<p> (Since Linux 4.3.) Atomically copy a continuous memory chunk into the userfault registered range and optionally wake up the blocked thread. The source and destination addresses and the number of bytes to copy are specified by the <i>src</i>, <i>dst</i>, and <i>len</i> fields of the <i>uffdio_copy</i> structure pointed to by <i>argp</i>: </p>
<p> struct uffdio_copy {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 dst;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Destination of copy&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 src;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Source of copy&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes to copy&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags controlling behavior of copy&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s64 copy;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes copied, or negated error&nbsp;*/ }; </p>
<p> The following value may be bitwise ORed in <i>mode</i> to change the behavior of the <code>UFFDIO_COPY</code> operation:</p>
<dl>
<dt><code>UFFDIO_COPY_MODE_DONTWAKE</code></p>
<dd> Do not wake up the thread that waits for page-fault resolution</dl>
<p> The <i>copy</i> field is used by the kernel to return the number of bytes that was actually copied, or an error (a negated <i>errno</i>-style value). If the value returned in <i>copy</i> doesn&#8217;t match the value that was specified in <i>len</i>, the operation fails with the error <code>EAGAIN</code>. The <i>copy</i> field is output-only; it is not read by the <code>UFFDIO_COPY</code> operation. </p>
<p> This <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation returns 0 on success. In this case, the entire area was copied. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error. Possible errors include:</p>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The number of bytes copied (i.e., the value returned in the <i>copy</i> field) does not equal the value that was specified in the <i>len</i> field.</p>
<dt><code>EINVAL</code></p>
<dd> Either <i>dst</i> or <i>len</i> was not a multiple of the system page size, or the range specified by <i>src</i> and <i>len</i> or <i>dst</i> and <i>len</i> was invalid.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid bit was specified in the <i>mode</i> field.</p>
<dt><code>ENOENT</code> (since Linux 4.11)</p>
<dd> The faulting process has changed its virtual memory layout simultaneously with an outstanding <code>UFFDIO_COPY</code> operation.</p>
<dt><code>ENOSPC</code> (from Linux 4.11 until Linux 4.13)</p>
<dd> The faulting process has exited at the time of a <code>UFFDIO_COPY</code> operation.</p>
<dt><code>ESRCH</code> (since Linux 4.13)</p>
<dd> The faulting process has exited at the time of a <code>UFFDIO_COPY</code> operation.</dl>
<h3>UFFDIO_ZEROPAGE</h3>
<p> (Since Linux 4.3.) Zero out a memory range registered with userfaultfd. </p>
<p> The requested range is specified by the <i>range</i> field of the <i>uffdio_zeropage</i> structure pointed to by <i>argp</i>: </p>
<p> struct uffdio_zeropage {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct uffdio_range range;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags controlling behavior of copy&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s64 zeropage;&nbsp;/*&nbsp;Number of bytes zeroed, or negated error&nbsp;*/ }; </p>
<p> The following value may be bitwise ORed in <i>mode</i> to change the behavior of the <code>UFFDIO_ZEROPAGE</code> operation:</p>
<dl>
<dt><code>UFFDIO_ZEROPAGE_MODE_DONTWAKE</code></p>
<dd> Do not wake up the thread that waits for page-fault resolution.</dl>
<p> The <i>zeropage</i> field is used by the kernel to return the number of bytes that was actually zeroed, or an error in the same manner as <code>UFFDIO_COPY</code>. If the value returned in the <i>zeropage</i> field doesn&#8217;t match the value that was specified in <i>range.len</i>, the operation fails with the error <code>EAGAIN</code>. The <i>zeropage</i> field is output-only; it is not read by the <code>UFFDIO_ZEROPAGE</code> operation. </p>
<p> This <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation returns 0 on success. In this case, the entire area was zeroed. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error. Possible errors include:</p>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The number of bytes zeroed (i.e., the value returned in the <i>zeropage</i> field) does not equal the value that was specified in the <i>range.len</i> field.</p>
<dt><code>EINVAL</code></p>
<dd> Either <i>range.start</i> or <i>range.len</i> was not a multiple of the system page size; or <i>range.len</i> was zero; or the range specified was invalid.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid bit was specified in the <i>mode</i> field.</p>
<dt><code>ESRCH</code> (since Linux 4.13)</p>
<dd> The faulting process has exited at the time of a <code>UFFDIO_ZEROPAGE</code> operation.</dl>
<h3>UFFDIO_WAKE</h3>
<p> (Since Linux 4.3.) Wake up the thread waiting for page-fault resolution on a specified memory address range. </p>
<p> The <code>UFFDIO_WAKE</code> operation is used in conjunction with <code>UFFDIO_COPY</code> and <code>UFFDIO_ZEROPAGE</code> operations that have the <code>UFFDIO_COPY_MODE_DONTWAKE</code> or <code>UFFDIO_ZEROPAGE_MODE_DONTWAKE</code> bit set in the <i>mode</i> field. The userfault monitor can perform several <code>UFFDIO_COPY</code> and <code>UFFDIO_ZEROPAGE</code> operations in a batch and then explicitly wake up the faulting thread using <code>UFFDIO_WAKE</code>. </p>
<p> The <i>argp</i> argument is a pointer to a <i>uffdio_range</i> structure (shown above) that specifies the address range. </p>
<p> This <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation returns 0 on success. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error. Possible errors include:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> The <i>start</i> or the <i>len</i> field of the <i>ufdio_range</i> structure was not a multiple of the system page size; or <i>len</i> was zero; or the specified range was otherwise invalid.</dl>
<h2>RETURN VALUE</h2>
<p> See descriptions of the individual operations, above.</p>
<h2>ERRORS</h2>
<p> See descriptions of the individual operations, above. In addition, the following general errors can occur for all of the operations described above:</p>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>argp</i> does not point to a valid memory address.</p>
<dt><code>EINVAL</code></p>
<dd> (For all operations except <code>UFFDIO_API</code>.) The userfaultfd object has not yet been enabled (via the <code>UFFDIO_API</code> operation).</dl>
<h2>CONFORMING TO</h2>
<p> These <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations are Linux-specific.</p>
<h2>BUGS</h2>
<p> In order to detect available userfault features and enable some subset of those features the userfaultfd file descriptor must be closed after the first <code>UFFDIO_API</code> operation that queries features availability and reopened before the second <code>UFFDIO_API</code> operation that actually enables the desired features.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2) </p>
<p> <i>Documentation/admin-guide/mm/userfaultfd.rst</i> in the Linux kernel source tree</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
