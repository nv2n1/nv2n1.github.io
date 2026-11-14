---
title: "kexec_file_load(2)"
name: "kexec_file_load"
section: "2"
letter: "k"
url: "/docs/linux/man/2-kexec_file_load/"
description: "kexec_load, kexec_file_load – load a new kernel for later execution"
---

<h2 class="name">NAME</h2>
<p> kexec_load, kexec_file_load &#8211; load a new kernel for later execution </p>
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
<dt><code>KEXEC_ON_CRASH</code> (since Linux 2.6.13)</p>
<dd> Execute the new kernel automatically on a system crash. This &quot;crash kernel&quot; is loaded into an area of reserved memory that is determined at boot time using the <i>crashkernel</i> kernel command-line parameter. The location of this reserved memory is exported to user space via the <i>/proc/iomem</i> file, in an entry labeled &quot;Crash kernel&quot;. A user-space application can parse this file and prepare a list of segments (see below) that specify this reserved memory as destination. If this flag is specified, the kernel checks that the target segments specified in <i>segments</i> fall within the reserved region.</p>
<dt><code>KEXEC_PRESERVE_CONTEXT</code> (since Linux 2.6.27)</p>
<dd> Preserve the system hardware and software states before executing the new kernel. This could be used for system suspend. This flag is available only if the kernel was configured with <code>CONFIG_KEXEC_JUMP</code>, and is effective only if <i>nr_segments</i> is greater than 0.</dl>
<p> The high-order bits (corresponding to the mask 0xffff0000) of <i>flags</i> contain the architecture of the to-be-executed kernel. Specify (OR) the constant <code>KEXEC_ARCH_DEFAULT</code> to use the current architecture, or one of the following architecture constants <code>KEXEC_ARCH_386</code>, <code>KEXEC_ARCH_68K</code>, <code>KEXEC_ARCH_X86_64</code>, <code>KEXEC_ARCH_PPC</code>, <code>KEXEC_ARCH_PPC64</code>, <code>KEXEC_ARCH_IA_64</code>, <code>KEXEC_ARCH_ARM</code>, <code>KEXEC_ARCH_S390</code>, <code>KEXEC_ARCH_SH</code>, <code>KEXEC_ARCH_MIPS</code>, and <code>KEXEC_ARCH_MIPS_LE</code>. The architecture must be executable on the CPU of the system. </p>
<p> The <i>entry</i> argument is the physical entry address in the kernel image. The <i>nr_segments</i> argument is the number of segments pointed to by the <i>segments</i> pointer; the kernel imposes an (arbitrary) limit of 16 on the number of segments. The <i>segments</i> argument is an array of <i>kexec_segment</i> structures which define the kernel layout: </p>
<p> struct kexec_segment {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;*buf;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Buffer in user space&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;bufsz;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Buffer length in user space&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;*mem;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Physical address of kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;memsz;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Physical address length&nbsp;*/ }; </p>
<p> The kernel image defined by <i>segments</i> is copied from the calling process into the kernel either in regular memory or in reserved memory (if <code>KEXEC_ON_CRASH</code> is set). The kernel first performs various sanity checks on the information passed in <i>segments</i>. If these checks pass, the kernel copies the segment data to kernel memory. Each segment specified in <i>segments</i> is copied as follows:</p>
<dl>
<dt>*</p>
<dd> <i>buf</i> and <i>bufsz</i> identify a memory region in the caller&#8217;s virtual address space that is the source of the copy. The value in <i>bufsz</i> may not exceed the value in the <i>memsz</i> field.</p>
<dt>*</p>
<dd> <i>mem</i> and <i>memsz</i> specify a physical address range that is the target of the copy. The values specified in both fields must be multiples of the system page size.</p>
<dt>*</p>
<dd> <i>bufsz</i> bytes are copied from the source buffer to the target kernel buffer. If <i>bufsz</i> is less than <i>memsz</i>, then the excess bytes in the kernel buffer are zeroed out.</dl>
<p> In case of a normal kexec (i.e., the <code>KEXEC_ON_CRASH</code> flag is not set), the segment data is loaded in any available memory and is moved to the final destination at kexec reboot time (e.g., when the <code><a href="/docs/linux/man/8-kexec/">kexec</a></code>(8) command is executed with the <i>-e</i> option). </p>
<p> In case of kexec on panic (i.e., the <code>KEXEC_ON_CRASH</code> flag is set), the segment data is loaded to reserved memory at the time of the call, and, after a crash, the kexec mechanism simply passes control to that kernel. </p>
<p> The <code>kexec_load</code>() system call is available only if the kernel was configured with <code>CONFIG_KEXEC</code>.</p>
<h3>kexec_file_load()</h3>
<p> The <code>kexec_file_load</code>() system call is similar to <code>kexec_load</code>(), but it takes a different set of arguments. It reads the kernel to be loaded from the file referred to by the file descriptor <i>kernel_fd</i>, and the initrd (initial RAM disk) to be loaded from file referred to by the file descriptor <i>initrd_fd</i>. The <i>cmdline</i> argument is a pointer to a buffer containing the command line for the new kernel. The <i>cmdline_len</i> argument specifies size of the buffer. The last byte in the buffer must be a null byte (&#8216;
