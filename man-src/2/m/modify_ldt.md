---
title: "modify_ldt(2)"
name: "modify_ldt"
section: "2"
letter: "m"
url: "/docs/linux/man/2-modify_ldt/"
description: "modify_ldt – get or set a per-process LDT entry"
---

<h2 class="name">NAME</h2>
<p> modify_ldt &#8211; get or set a per-process LDT entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
int modify_ldt(int func, void *ptr, unsigned long bytecount);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>modify_ldt</code>() reads or writes the local descriptor table (LDT) for a process. The LDT is an array of segment descriptors that can be referenced by user code. Linux allows processes to configure a per-process (actually per-mm) LDT. For more information about the LDT, see the Intel Software Developer&#8217;s Manual or the AMD Architecture Programming Manual. </p>
<p> When <i>func</i> is 0, <code>modify_ldt</code>() reads the LDT into the memory pointed to by <i>ptr</i>. The number of bytes read is the smaller of <i>bytecount</i> and the actual size of the LDT, although the kernel may act as though the LDT is padded with additional trailing zero bytes. On success, <code>modify_ldt</code>() will return the number of bytes read. </p>
<p> When <i>func</i> is 1 or 0x11, <code>modify_ldt</code>() modifies the LDT entry indicated by <i>ptr-&gt;entry_number</i>. <i>ptr</i> points to a <i>user_desc</i> structure and <i>bytecount</i> must equal the size of this structure. </p>
<p> The <i>user_desc</i> structure is defined in <i>&lt;asm/ldt.h&gt;</i> as: </p>
<p> struct user_desc {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;entry_number;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;base_addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;limit;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;seg_32bit:1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;contents:2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;read_exec_only:1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;limit_in_pages:1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;seg_not_present:1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;useable:1; }; </p>
<p> In Linux 2.4 and earlier, this structure was named <i>modify_ldt_ldt_s</i>. </p>
<p> The <i>contents</i> field is the segment type (data, expand-down data, non-conforming code, or conforming code). The other fields match their descriptions in the CPU manual, although <code>modify_ldt</code>() cannot set the hardware-defined &quot;accessed&quot; bit described in the CPU manual. </p>
<p> A <i>user_desc</i> is considered &quot;empty&quot; if <i>read_exec_only</i> and <i>seg_not_present</i> are set to 1 and all of the other fields are 0. An LDT entry can be cleared by setting it to an &quot;empty&quot; <i>user_desc</i> or, if <i>func</i> is 1, by setting both <i>base</i> and <i>limit</i> to 0. </p>
<p> A conforming code segment (i.e., one with <i>contents==3</i>) will be rejected if <i>func</i> is 1 or if <i>seg_not_present</i> is 0. </p>
<p> When <i>func</i> is 2, <code>modify_ldt</code>() will read zeros. This appears to be a leftover from Linux 2.4.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>modify_ldt</code>() returns either the actual number of bytes read (for reading) or 0 (for writing). On failure, <code>modify_ldt</code>() returns -1 and sets <i>errno</i> to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>ptr</i> points outside the address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>ptr</i> is 0, or <i>func</i> is 1 and <i>bytecount</i> is not equal to the size of the structure <i>user_desc</i>, or <i>func</i> is 1 or 0x11 and the new LDT entry has invalid values.</p>
<dt><code>ENOSYS</code></p>
<dd> <i>func</i> is neither 0, 1, 2, nor 0x11.</dl>
<h2>CONFORMING TO</h2>
<p> This call is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> <code>modify_ldt</code>() should not be used for thread-local storage, as it slows down context switches and only supports a limited number of threads. Threading libraries should use <code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2) or <code><a href="/docs/linux/man/2-arch_prctl/">arch_prctl</a></code>(2) instead, except on extremely old kernels that do not support those system calls. </p>
<p> The normal use for <code>modify_ldt</code>() is to run legacy 16-bit or segmented 32-bit code. Not all kernels allow 16-bit segments to be installed, however. </p>
<p> Even on 64-bit kernels, <code>modify_ldt</code>() cannot be used to create a long mode (i.e., 64-bit) code segment. The undocumented field &quot;lm&quot; in <i>user_desc</i> is not useful, and, despite its name, does not result in a long mode segment.</p>
<h2>BUGS</h2>
<p> On 64-bit kernels before Linux 3.19, setting the &quot;lm&quot; bit in <i>user_desc</i> prevents the descriptor from being considered empty. Keep in mind that the &quot;lm&quot; bit does not exist in the 32-bit headers, but these buggy kernels will still notice the bit even when set in a 32-bit process.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-arch_prctl/">arch_prctl</a></code>(2), <code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2), <code><a href="/docs/linux/man/2-vm86/">vm86</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
