---
title: "set_thread_area(2)"
name: "set_thread_area"
section: "2"
letter: "s"
url: "/docs/linux/man/2-set_thread_area/"
description: "get_thread_area, set_thread_area – manipulate thread-local storage information"
---

<h2 class="name">NAME</h2>
<p> get_thread_area, set_thread_area &#8211; manipulate thread-local storage information </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/unistd.h&gt;
#if defined __i386__ || defined __x86_64__
#include &lt;asm/ldt.h&gt;
int get_thread_area(struct user_desc *u_info);
int set_thread_area(struct user_desc *u_info);
#elif defined __m68k__
int get_thread_area(void);
int set_thread_area(unsigned long tp);
#elif defined __mips__
int set_thread_area(unsigned long addr);
#endif
</code></pre>
<p> <i>Note</i>: There are no glibc wrappers for these system calls; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> These calls provide architecture-specific support for a thread-local storage implementation. At the moment, <code>set_thread_area</code>() is available on m68k, MIPS, and x86 (both 32-bit and 64-bit variants); <code>get_thread_area</code>() is available on m68k and x86. </p>
<p> On m68k and MIPS, <code>set_thread_area</code>() allows storing an arbitrary pointer (provided in the <code>tp</code> argument on m68k and in the <code>addr</code> argument on MIPS) in the kernel data structure associated with the calling thread; this pointer can later be retrieved using <code>get_thread_area</code>() (see also NOTES for information regarding obtaining the thread pointer on MIPS). </p>
<p> On x86, Linux dedicates three global descriptor table (GDT) entries for thread-local storage. For more information about the GDT, see the Intel Software Developer&#8217;s Manual or the AMD Architecture Programming Manual. </p>
<p> Both of these system calls take an argument that is a pointer to a structure of the following type: </p>
<p> struct user_desc {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;entry_number;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;base_addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;limit;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;seg_32bit:1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;contents:2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;read_exec_only:1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;limit_in_pages:1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;seg_not_present:1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;useable:1; #ifdef __x86_64__<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;lm:1; #endif }; </p>
<p> <code>get_thread_area</code>() reads the GDT entry indicated by <i>u_info-&gt;entry_number</i> and fills in the rest of the fields in <i>u_info</i>. </p>
<p> <code>set_thread_area</code>() sets a TLS entry in the GDT. </p>
<p> The TLS array entry set by <code>set_thread_area</code>() corresponds to the value of <i>u_info-&gt;entry_number</i> passed in by the user. If this value is in bounds, <code>set_thread_area</code>() writes the TLS descriptor pointed to by <i>u_info</i> into the thread&#8217;s TLS array. </p>
<p> When <code>set_thread_area</code>() is passed an <i>entry_number</i> of -1, it searches for a free TLS entry. If <code>set_thread_area</code>() finds a free TLS entry, the value of <i>u_info-&gt;entry_number</i> is set upon return to show which entry was changed. </p>
<p> A <i>user_desc</i> is considered &quot;empty&quot; if <i>read_exec_only</i> and <i>seg_not_present</i> are set to 1 and all of the other fields are 0. If an &quot;empty&quot; descriptor is passed to <code>set_thread_area</code>(), the corresponding TLS entry will be cleared. See BUGS for additional details. </p>
<p> Since Linux 3.19, <code>set_thread_area</code>() cannot be used to write non-present segments, 16-bit segments, or code segments, although clearing a segment is still acceptable.</p>
<h2>RETURN VALUE</h2>
<p> On x86, these system calls return 0 on success, and -1 on failure, with <i>errno</i> set appropriately. </p>
<p> On MIPS and m68k, <code>set_thread_area</code>() always returns 0. On m68k, <code>get_thread_area</code>() returns the thread area pointer value (previously set via <code>set_thread_area</code>()).</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>u_info</i> is an invalid pointer.</p>
<dt><code>EINVAL</code></p>
<dd> <i>u_info-&gt;entry_number</i> is out of bounds.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>get_thread_area</code>() or <code>set_thread_area</code>() was invoked as a 64-bit system call.</p>
<dt><code>ESRCH</code></p>
<dd> (<code>set_thread_area</code>()) A free TLS entry could not be located.</dl>
<h2>VERSIONS</h2>
<p> <code>set_thread_area</code>() first appeared in Linux 2.5.29. <code>get_thread_area</code>() first appeared in Linux 2.5.32.</p>
<h2>CONFORMING TO</h2>
<p> <code>set_thread_area</code>() and <code>get_thread_area</code>() are Linux-specific and should not be used in programs that are intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide wrappers for these system calls, since they are generally intended for use only by threading libraries. In the unlikely event that you want to call them directly, use <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> <code><a href="/docs/linux/man/2-arch_prctl/">arch_prctl</a></code>(2) can interfere with <code>set_thread_area</code>() on x86. See <code><a href="/docs/linux/man/2-arch_prctl/">arch_prctl</a></code>(2) for more details. This is not normally a problem, as <code><a href="/docs/linux/man/2-arch_prctl/">arch_prctl</a></code>(2) is normally used only by 64-bit programs. </p>
<p> On MIPS, the current value of the thread area pointer can be obtained using the instruction: </p>
<p> rdhwr dest, $29 </p>
<p> This instruction traps and is handled by kernel.</p>
<h2>BUGS</h2>
<p> On 64-bit kernels before Linux 3.19, one of the padding bits in <i>user_desc</i>, if set, would prevent the descriptor from being considered empty (see <code><a href="/docs/linux/man/2-modify_ldt/">modify_ldt</a></code>(2)). As a result, the only reliable way to clear a TLS entry is to use <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3) to zero the entire <i>user_desc</i> structure, including padding bits, and then to set the <i>read_exec_only</i> and <i>seg_not_present</i> bits. On Linux 3.19, a <i>user_desc</i> consisting entirely of zeros except for <i>entry_number</i> will also be interpreted as a request to clear a TLS entry, but this behaved differently on older kernels. </p>
<p> Prior to Linux 3.19, the DS and ES segment registers must not reference TLS entries.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-arch_prctl/">arch_prctl</a></code>(2), <code><a href="/docs/linux/man/2-modify_ldt/">modify_ldt</a></code>(2), <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) (<code>PTRACE_GET_THREAD_AREA</code> and <code>PTRACE_SET_THREAD_AREA</code>)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
