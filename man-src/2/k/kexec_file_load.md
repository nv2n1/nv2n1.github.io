---
title: "kexec_file_load(2)"
name: "kexec_file_load"
section: "2"
letter: "k"
url: "/docs/linux/man/2-kexec_file_load/"
description: "kexec_load, kexec_file_load – load a new kernel for later execution"
---

<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/kexec.h&gt;
long kexec_load(unsigned long entry, unsigned long nr_segments,
                struct kexec_segment *segments, unsigned long flags);
long kexec_file_load(int kernel_fd, int initrd_fd,
                     unsigned long cmdline_len, const char *cmdline,
                     unsigned long flags);
</code></pre>
<p> <i>Note</i>: There are no glibc wrappers for these system calls; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>kexec_load</code>() system call loads a new kernel that can be executed later by <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2). </p>
<p> The <i>flags</i> argument is a bit mask that controls the operation of the call. The following values can be specified in <i>flags</i>:</p>
<dl>
<dt><code>KEXEC_ON_CRASH</code> (since Linux 2.6.13)</dt>
<dd> Execute the new kernel automatically on a system crash. This &quot;crash kernel&quot; is loaded into an area of reserved memory that is determined at boot time using the <i>crashkernel</i> kernel command-line parameter. The location of this reserved memory is exported to user space via the <i>/proc/iomem</i> file, in an entry labeled &quot;Crash kernel&quot;. A user-space application can parse this file and prepare a list of segments (see below) that specify this reserved memory as destination. If this flag is specified, the kernel checks that the target segments specified in <i>segments</i> fall within the reserved region.</dd>
<dt><code>KEXEC_PRESERVE_CONTEXT</code> (since Linux 2.6.27)</dt>
<dd> Preserve the system hardware and software states before executing the new kernel. This could be used for system suspend. This flag is available only if the kernel was configured with <code>CONFIG_KEXEC_JUMP</code>, and is effective only if <i>nr_segments</i> is greater than 0.</dd></dl>
<p> The high-order bits (corresponding to the mask 0xffff0000) of <i>flags</i> contain the architecture of the to-be-executed kernel. Specify (OR) the constant <code>KEXEC_ARCH_DEFAULT</code> to use the current architecture, or one of the following architecture constants <code>KEXEC_ARCH_386</code>, <code>KEXEC_ARCH_68K</code>, <code>KEXEC_ARCH_X86_64</code>, <code>KEXEC_ARCH_PPC</code>, <code>KEXEC_ARCH_PPC64</code>, <code>KEXEC_ARCH_IA_64</code>, <code>KEXEC_ARCH_ARM</code>, <code>KEXEC_ARCH_S390</code>, <code>KEXEC_ARCH_SH</code>, <code>KEXEC_ARCH_MIPS</code>, and <code>KEXEC_ARCH_MIPS_LE</code>. The architecture must be executable on the CPU of the system. </p>
<p> The <i>entry</i> argument is the physical entry address in the kernel image. The <i>nr_segments</i> argument is the number of segments pointed to by the <i>segments</i> pointer; the kernel imposes an (arbitrary) limit of 16 on the number of segments. The <i>segments</i> argument is an array of <i>kexec_segment</i> structures which define the kernel layout: </p>
<p> struct kexec_segment {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;*buf;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Buffer in user space&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;bufsz;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Buffer length in user space&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;*mem;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Physical address of kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;memsz;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Physical address length&nbsp;*/ }; </p>
<p> The kernel image defined by <i>segments</i> is copied from the calling process into the kernel either in regular memory or in reserved memory (if <code>KEXEC_ON_CRASH</code> is set). The kernel first performs various sanity checks on the information passed in <i>segments</i>. If these checks pass, the kernel copies the segment data to kernel memory. Each segment specified in <i>segments</i> is copied as follows:</p>
<dl>
<dt>*</dt>
<dd> <i>buf</i> and <i>bufsz</i> identify a memory region in the caller&#8217;s virtual address space that is the source of the copy. The value in <i>bufsz</i> may not exceed the value in the <i>memsz</i> field.</dd>
<dt>*</dt>
<dd> <i>mem</i> and <i>memsz</i> specify a physical address range that is the target of the copy. The values specified in both fields must be multiples of the system page size.</dd>
<dt>*</dt>
<dd> <i>bufsz</i> bytes are copied from the source buffer to the target kernel buffer. If <i>bufsz</i> is less than <i>memsz</i>, then the excess bytes in the kernel buffer are zeroed out.</dd></dl>
<p> In case of a normal kexec (i.e., the <code>KEXEC_ON_CRASH</code> flag is not set), the segment data is loaded in any available memory and is moved to the final destination at kexec reboot time (e.g., when the <code><a href="/docs/linux/man/8-kexec/">kexec</a></code>(8) command is executed with the <i>-e</i> option). </p>
<p> In case of kexec on panic (i.e., the <code>KEXEC_ON_CRASH</code> flag is set), the segment data is loaded to reserved memory at the time of the call, and, after a crash, the kexec mechanism simply passes control to that kernel. </p>
<p> The <code>kexec_load</code>() system call is available only if the kernel was configured with <code>CONFIG_KEXEC</code>.</p>
<h3>kexec_file_load()</h3>
<p> The <code>kexec_file_load</code>() system call is similar to <code>kexec_load</code>(), but it takes a different set of arguments. It reads the kernel to be loaded from the file referred to by the file descriptor <i>kernel_fd</i>, and the initrd (initial RAM disk) to be loaded from file referred to by the file descriptor <i>initrd_fd</i>. The <i>cmdline</i> argument is a pointer to a buffer containing the command line for the new kernel. The <i>cmdline_len</i> argument specifies size of the buffer. The last byte in the buffer must be a null byte (&#8216;\0&#8217;). </p>
<p> The <i>flags</i> argument is a bit mask which modifies the behavior of the call. The following values can be specified in <i>flags</i>: </p>
<dl>
<dt><code>KEXEC_FILE_UNLOAD</code></dt>
<dd> <p> Unload the currently loaded kernel. </p>
 </dd>
<dt><code>KEXEC_FILE_ON_CRASH</code></dt>
<dd> <p> Load the new kernel in the memory region reserved for the crash kernel (as for <code>KEXEC_ON_CRASH</code>). This kernel is booted if the currently running kernel crashes. </p>
 </dd>
<dt><code>KEXEC_FILE_NO_INITRAMFS</code></dt>
<dd> <p> Loading initrd/initramfs is optional. Specify this flag if no initramfs is being loaded. If this flag is set, the value passed in <i>initrd_fd</i> is ignored. </p>
 </dd></dl>
<p> The <code>kexec_file_load</code>() system call was added to provide support for systems where &quot;kexec&quot; loading should be restricted to only kernels that are signed. This system call is available only if the kernel was configured with <code>CONFIG_KEXEC_FILE</code>.  </p>
<h2>RETURN VALUE</h2>
<p> On success, these system calls returns 0. On error, -1 is returned and <i>errno</i> is set to indicate the error.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EADDRNOTAVAIL</code></dt>
<dd> <p> The <code>KEXEC_ON_CRASH</code> flags was specified, but the region specified by the <i>mem</i> and <i>memsz</i> fields of one of the <i>segments</i> entries lies outside the range of memory reserved for the crash kernel. </p>
 </dd>
<dt><code>EADDRNOTAVAIL</code></dt>
<dd> <p> The value in a <i>mem</i> or <i>memsz</i> field in one of the <i>segments</i> entries is not a multiple of the system page size. </p>
 </dd>
<dt><code>EBADF</code></dt>
<dd> <p> <i>kernel_fd</i> or <i>initrd_fd</i> is not a valid file descriptor. </p>
 </dd>
<dt><code>EBUSY</code></dt>
<dd> <p> Another crash kernel is already being loaded or a crash kernel is already in use. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> <i>flags</i> is invalid. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> The value of a <i>bufsz</i> field in one of the <i>segments</i> entries exceeds the value in the corresponding <i>memsz</i> field. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> <i>nr_segments</i> exceeds <code>KEXEC_SEGMENT_MAX</code> (16). </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> Two or more of the kernel target buffers overlap. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> The value in <i>cmdline[cmdline_len-1]</i> is not &#8216;\0&#8217;. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> The file referred to by <i>kernel_fd</i> or <i>initrd_fd</i> is empty (length zero). </p>
 </dd>
<dt><code>ENOEXEC</code></dt>
<dd> <p> <i>kernel_fd</i> does not refer to an open file, or the kernel can&#8217;t load this file. Currently, the file must be a bzImage and contain an x86 kernel that is loadable above 4 GiB in memory (see the kernel source file <i>Documentation/x86/boot.txt</i>). </p>
 </dd>
<dt><code>ENOMEM</code></dt>
<dd> <p> Could not allocate memory. </p>
 </dd>
<dt><code>EPERM</code></dt>
<dd> <p> The caller does not have the <code>CAP_SYS_BOOT</code> capability. </p>
 </dd></dl>
<h2>VERSIONS</h2>
<p> The <code>kexec_load</code>() system call first appeared in Linux 2.6.13. The <code>kexec_file_load</code>() system call first appeared in Linux 3.17.  </p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.  </p>
<h2>NOTES</h2>
<p> Currently, there is no glibc support for these system calls. Call them using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2), <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), <code><a href="/docs/linux/man/8-kexec/">kexec</a></code>(8) </p>
<p> The kernel source files <i>Documentation/kdump/kdump.txt</i> and <i>Documentation/admin-guide/kernel-parameters.txt</i>  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
