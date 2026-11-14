---
title: "fadvise64_64(2)"
name: "fadvise64_64"
section: "2"
letter: "f"
url: "/docs/linux/man/2-fadvise64_64/"
description: "posix_fadvise – predeclare an access pattern for file data"
---

<h2 class="name">NAME</h2>
<p> posix_fadvise &#8211; predeclare an access pattern for file data </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fcntl.h&gt;
int posix_fadvise(int fd, off_t offset, off_t len, int advice);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>posix_fadvise</code>():</p>
<dl>
<dt>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> Programs can use <code>posix_fadvise</code>() to announce an intention to access file data in a specific pattern in the future, thus allowing the kernel to perform appropriate optimizations. </p>
<p> The <i>advice</i> applies to a (not necessarily existent) region starting at <i>offset</i> and extending for <i>len</i> bytes (or until the end of the file if <i>len</i> is 0) within the file referred to by <i>fd</i>. The <i>advice</i> is not binding; it merely constitutes an expectation on behalf of the application. </p>
<p> Permissible values for <i>advice</i> include:</p>
<dl>
<dt><code>POSIX_FADV_NORMAL</code></p>
<dd> Indicates that the application has no advice to give about its access pattern for the specified data. If no advice is given for an open file, this is the default assumption.</p>
<dt><code>POSIX_FADV_SEQUENTIAL</code></p>
<dd> The application expects to access the specified data sequentially (with lower offsets read before higher ones).</p>
<dt><code>POSIX_FADV_RANDOM</code></p>
<dd> The specified data will be accessed in random order.</p>
<dt><code>POSIX_FADV_NOREUSE</code></p>
<dd> The specified data will be accessed only once.</p>
<dt>
<dd> In kernels before 2.6.18, <code>POSIX_FADV_NOREUSE</code> had the same semantics as <code>POSIX_FADV_WILLNEED</code>. This was probably a bug; since kernel 2.6.18, this flag is a no-op.</p>
<dt><code>POSIX_FADV_WILLNEED</code></p>
<dd> The specified data will be accessed in the near future.</p>
<dt>
<dd> <code>POSIX_FADV_WILLNEED</code> initiates a nonblocking read of the specified region into the page cache. The amount of data read may be decreased by the kernel depending on virtual memory load. (A few megabytes will usually be fully satisfied, and more is rarely useful.)</p>
<dt><code>POSIX_FADV_DONTNEED</code></p>
<dd> The specified data will not be accessed in the near future.</p>
<dt>
<dd> <code>POSIX_FADV_DONTNEED</code> attempts to free cached pages associated with the specified region. This is useful, for example, while streaming large files. A program may periodically request the kernel to free cached data that has already been used, so that more useful cached pages are not discarded instead.</p>
<dt>
<dd> Requests to discard partial pages are ignored. It is preferable to preserve needed data than discard unneeded data. If the application requires that data be considered for discarding, then <i>offset</i> and <i>len</i> must be page-aligned.</p>
<dt>
<dd> The implementation <i>may</i> attempt to write back dirty pages in the specified region, but this is not guaranteed. Any unwritten dirty pages will not be freed. If the application wishes to ensure that dirty pages will be released, it should call <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) or <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2) first.</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, an error number is returned.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> The <i>fd</i> argument was not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid value was specified for <i>advice</i>.</p>
<dt><code>ESPIPE</code></p>
<dd> The specified file descriptor refers to a pipe or FIFO. (<code>ESPIPE</code> is the error specified by POSIX, but before kernel version 2.6.16, Linux returned <code>EINVAL</code> in this case.)</dl>
<h2>VERSIONS</h2>
<p> Kernel support first appeared in Linux 2.5.60; the underlying system call is called <code>fadvise64</code>(). Library support has been provided since glibc version 2.2, via the wrapper function <code>posix_fadvise</code>(). </p>
<p> Since Linux 3.18, support for the underlying system call is optional, depending on the setting of the <code>CONFIG_ADVISE_SYSCALLS</code> configuration option.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008. Note that the type of the <i>len</i> argument was changed from <i>size_t</i> to <i>off_t</i> in POSIX.1-2001 TC1.</p>
<h2>NOTES</h2>
<p> Under Linux, <code>POSIX_FADV_NORMAL</code> sets the readahead window to the default size for the backing device; <code>POSIX_FADV_SEQUENTIAL</code> doubles this size, and <code>POSIX_FADV_RANDOM</code> disables file readahead entirely. These changes affect the entire file, not just the specified region (but other open file handles to the same file are unaffected). </p>
<p> The contents of the kernel buffer cache can be cleared via the <i>/proc/sys/vm/drop_caches</i> interface described in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5). </p>
<p> One can obtain a snapshot of which pages of a file are resident in the buffer cache by opening a file, mapping it with <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), and then applying <code><a href="/docs/linux/man/2-mincore/">mincore</a></code>(2) to the mapping.</p>
<h3>C library/kernel differences</h3>
<p> The name of the wrapper function in the C library is <code>posix_fadvise</code>(). The underlying system call is called <code>fadvise64</code>() (or, on some architectures, <code>fadvise64_64</code>()); the difference between the two is that the former system call assumes that the type of the <i>len</i> argument is <i>size_t</i>, while the latter expects <i>loff_t</i> there.</p>
<h3>Architecture-specific variants</h3>
<p> Some architectures require 64-bit arguments to be aligned in a suitable pair of registers (see <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) for further detail). On such architectures, the call signature of <code>posix_fadvise</code>() shown in the SYNOPSIS would force a register to be wasted as padding between the <i>fd</i> and <i>offset</i> arguments. Therefore, these architectures define a version of the system call that orders the arguments suitably, but is otherwise exactly the same as <code>posix_fadvise</code>(). </p>
<p> For example, since Linux 2.6.14, ARM has the following system call: </p>
<p> <code>long arm_fadvise64_64(int </code><i>fd</i><code>, int </code><i>advice</i><code>,</code> <code> loff_t </code><i>offset</i><code>, loff_t </code><i>len</i><code>);</code> </p>
<p> These architecture-specific details are generally hidden from applications by the glibc <code>posix_fadvise</code>() wrapper function, which invokes the appropriate architecture-specific system call.</p>
<h2>BUGS</h2>
<p> In kernels before 2.6.6, if <i>len</i> was specified as 0, then this was interpreted literally as &quot;zero bytes&quot;, rather than as meaning &quot;all bytes through to the end of the file&quot;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fincore/">fincore</a></code>(1), <code><a href="/docs/linux/man/2-mincore/">mincore</a></code>(2), <code><a href="/docs/linux/man/2-readahead/">readahead</a></code>(2), <code><a href="/docs/linux/man/2-sync_file_range/">sync_file_range</a></code>(2), <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3), <code><a href="/docs/linux/man/3-posix_madvise/">posix_madvise</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
