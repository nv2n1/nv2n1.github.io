---
title: "vdso(7)"
name: "vdso"
section: "7"
letter: "v"
url: "/docs/linux/man/7-vdso/"
description: "vdso – overview of the virtual ELF dynamic shared object"
---

<p>vdso &#8211; overview of the virtual ELF dynamic shared object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/auxv.h&gt;
void *vdso = (uintptr_t)getauxval(AT_SYSINFO_EHDR);</code></pre>
<h2>Description</h2>
<p>The &quot;vDSO&quot; (virtual dynamic shared object) is a small shared library that the kernel automatically maps into the address space of all user-space applications. Applications usually do not need to concern themselves with these details as the vDSO is most commonly called by the C library. This way you can code in the normal way using standard functions and the C library will take care of using any functionality that is available via the vDSO. </p>
<p> Why does the vDSO exist at all? There are some system calls the kernel provides that user-space code ends up using frequently, to the point that such calls can dominate overall performance. This is due both to the frequency of the call as well as the context-switch overhead that results from exiting user space and entering the kernel. </p>
<p> The rest of this documentation is geared toward the curious and/or C library writers rather than general developers. If you&#8217;re trying to call the vDSO in your own application rather than using the C library, you&#8217;re most likely doing it wrong.</p>
<h3>Example background</h3>
<p>Making system calls can be slow. In x86 32-bit systems, you can trigger a software interrupt (<i>int $0x80</i>) to tell the kernel you wish to make a system call. However, this instruction is expensive: it goes through the full interrupt-handling paths in the processor&#8217;s microcode as well as in the kernel. Newer processors have faster (but backward incompatible) instructions to initiate system calls. Rather than require the C library to figure out if this functionality is available at run time, the C library can use functions provided by the kernel in the vDSO. </p>
<p> Note that the terminology can be confusing. On x86 systems, the vDSO function used to determine the preferred method of making a system call is named &quot;__kernel_vsyscall&quot;, but on x86-64, the term &quot;vsyscall&quot; also refers to an obsolete way to ask the kernel what time it is or what CPU the caller is on. </p>
<p> One frequently used system call is <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2). This system call is called both directly by user-space applications as well as indirectly by the C library. Think timestamps or timing loops or polling&#8212;all of these frequently need to know what time it is right now. This information is also not secret&#8212;any application in any privilege mode (root or any unprivileged user) will get the same answer. Thus the kernel arranges for the information required to answer this question to be placed in memory the process can access. Now a call to <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2) changes from a system call to a normal function call and a few memory accesses.</p>
<h3>Finding the vDSO</h3>
<p>The base address of the vDSO (if one exists) is passed by the kernel to each program in the initial auxiliary vector (see <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3)), via the <code>AT_SYSINFO_EHDR</code> tag. </p>
<p> You must not assume the vDSO is mapped at any particular location in the user&#8217;s memory map. The base address will usually be randomized at run time every time a new process image is created (at <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) time). This is done for security reasons, to prevent &quot;return-to-libc&quot; attacks. </p>
<p> For some architectures, there is also an <code>AT_SYSINFO</code> tag. This is used only for locating the vsyscall entry point and is frequently omitted or set to 0 (meaning it&#8217;s not available). This tag is a throwback to the initial vDSO work (see <i>History</i> below) and its use should be avoided.</p>
<h3>File format</h3>
<p>Since the vDSO is a fully formed ELF image, you can do symbol lookups on it. This allows new symbols to be added with newer kernel releases, and allows the C library to detect available functionality at run time when running under different kernel versions. Oftentimes the C library will do detection with the first call and then cache the result for subsequent calls. </p>
<p> All symbols are also versioned (using the GNU version format). This allows the kernel to update the function signature without breaking backward compatibility. This means changing the arguments that the function accepts as well as the return value. Thus, when looking up a symbol in the vDSO, you must always include the version to match the ABI you expect. </p>
<p> Typically the vDSO follows the naming convention of prefixing all symbols with &quot;__vdso_&quot; or &quot;__kernel_&quot; so as to distinguish them from other standard symbols. For example, the &quot;gettimeofday&quot; function is named &quot;__vdso_gettimeofday&quot;. </p>
<p> You use the standard C calling conventions when calling any of these functions. No need to worry about weird register or stack behavior.</p>
<h2>Notes</h2>
<h3>Source</h3>
<p>When you compile the kernel, it will automatically compile and link the vDSO code for you. You will frequently find it under the architecture-specific directory: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;find arch/$ARCH/&nbsp;-name&nbsp;&#8216;*vdso*.so*&#8217;&nbsp;-o -name&nbsp;&#8216;*gate*.so*&#8217;</p>
<h3>vDSO names</h3>
<p>The name of the vDSO varies across architectures. It will often show up in things like glibc&#8217;s <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1) output. The exact name should not matter to any code, so do not hardcode it. </p>
<table>
<tr VALIGN=top>
<td>user ABI</td>
<td>vDSO name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>aarch64</td>
<td>linux-vdso.so.1
</td>
</tr>
<tr VALIGN=top>
<td>arm</td>
<td>linux-vdso.so.1
</td>
</tr>
<tr VALIGN=top>
<td>ia64</td>
<td>linux-gate.so.1
</td>
</tr>
<tr VALIGN=top>
<td>mips</td>
<td>linux-vdso.so.1
</td>
</tr>
<tr VALIGN=top>
<td>ppc/32</td>
<td>linux-vdso32.so.1
</td>
</tr>
<tr VALIGN=top>
<td>ppc/64</td>
<td>linux-vdso64.so.1
</td>
</tr>
<tr VALIGN=top>
<td>riscv</td>
<td>linux-vdso.so.1
</td>
</tr>
<tr VALIGN=top>
<td>s390</td>
<td>linux-vdso32.so.1
</td>
</tr>
<tr VALIGN=top>
<td>s390x</td>
<td>linux-vdso64.so.1
</td>
</tr>
<tr VALIGN=top>
<td>sh</td>
<td>linux-gate.so.1
</td>
</tr>
<tr VALIGN=top>
<td>i386</td>
<td>linux-gate.so.1
</td>
</tr>
<tr VALIGN=top>
<td>x86-64</td>
<td>linux-vdso.so.1
</td>
</tr>
<tr VALIGN=top>
<td>x86/x32</td>
<td>linux-vdso.so.1
</td>
</tr>
</table>
<h3><a href="/docs/linux/man/1-strace/">strace</a>(1), <a href="/docs/linux/man/2-seccomp/">seccomp</a>(2), and the vDSO</h3>
<p>When tracing systems calls with <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1), symbols (system calls) that are exported by the vDSO will <i>not</i> appear in the trace output. Those system calls will likewise not be visible to <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) filters.</p>
<h2>Architecture-Specific Notes</h2>
<p>The subsections below provide architecture-specific notes on the vDSO. </p>
<p> Note that the vDSO that is used is based on the ABI of your user-space code and not the ABI of the kernel. Thus, for example, when you run an i386 32-bit ELF binary, you&#8217;ll get the same vDSO regardless of whether you run it under an i386 32-bit kernel or under an x86-64 64-bit kernel. Therefore, the name of the user-space ABI should be used to determine which of the sections below is relevant.</p>
<h3>ARM functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_gettimeofday</td>
<td>LINUX_2.6 (exported since Linux 4.1)
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_clock_gettime</td>
<td>LINUX_2.6 (exported since Linux 4.1)
</td>
</tr>
</table>
<p> Additionally, the ARM port has a code page full of utility functions. Since it&#8217;s just a raw page of code, there is no ELF information for doing symbol lookups or versioning. It does provide support for different versions though. </p>
<p> For information on this code page, it&#8217;s best to refer to the kernel documentation as it&#8217;s extremely detailed and covers everything you need to know: <i>Documentation/arm/kernel_user_helpers.txt</i>.</p>
<h3>aarch64 functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_rt_sigreturn</td>
<td>LINUX_2.6.39
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_gettimeofday</td>
<td>LINUX_2.6.39
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_gettime</td>
<td>LINUX_2.6.39
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_getres</td>
<td>LINUX_2.6.39
</td>
</tr>
</table>
<h3>bfin (Blackfin) functions (port removed in Linux 4.17)</h3>
<p>As this CPU lacks a memory management unit (MMU), it doesn&#8217;t set up a vDSO in the normal sense. Instead, it maps at boot time a few raw functions into a fixed location in memory. User-space applications then call directly into that region. There is no provision for backward compatibility beyond sniffing raw opcodes, but as this is an embedded CPU, it can get away with things&#8212;some of the object formats it runs aren&#8217;t even ELF based (they&#8217;re bFLT/FLAT). </p>
<p> For information on this code page, it&#8217;s best to refer to the public documentation:<br />
 <a rel="nofollow" href="http://docs.blackfin.uclinux.org/doku.php?id=linux-kernel:fixed-code">http://docs.blackfin.uclinux.org/doku.php?id=linux-kernel:fixed-code</a></p>
<h3>mips functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_gettimeofday</td>
<td>LINUX_2.6 (exported since Linux 4.4)
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_gettime</td>
<td>LINUX_2.6 (exported since Linux 4.4)
</td>
</tr>
</table>
<h3>ia64 (Itanium) functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sigtramp</td>
<td>LINUX_2.5
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_syscall_via_break</td>
<td>LINUX_2.5
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_syscall_via_epc</td>
<td>LINUX_2.5
</td>
</tr>
</table>
<p> The Itanium port is somewhat tricky. In addition to the vDSO above, it also has &quot;light-weight system calls&quot; (also known as &quot;fast syscalls&quot; or &quot;fsys&quot;). You can invoke these via the <i>__kernel_syscall_via_epc</i> vDSO helper. The system calls listed here have the same semantics as if you called them directly via <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), so refer to the relevant documentation for each. The table below lists the functions available via this mechanism. </p>
<table>
<tr VALIGN=top>
<td>function
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>clock_gettime
</td>
</tr>
<tr VALIGN=top>
<td>getcpu
</td>
</tr>
<tr VALIGN=top>
<td>getpid
</td>
</tr>
<tr VALIGN=top>
<td>getppid
</td>
</tr>
<tr VALIGN=top>
<td>gettimeofday
</td>
</tr>
<tr VALIGN=top>
<td>set_tid_address
</td>
</tr>
</table>
<h3>parisc (hppa) functions</h3>
<p>The parisc port has a code page with utility functions called a gateway page. Rather than use the normal ELF auxiliary vector approach, it passes the address of the page to the process via the SR2 register. The permissions on the page are such that merely executing those addresses automatically executes with kernel privileges and not in user space. This is done to match the way HP-UX works. </p>
<p> Since it&#8217;s just a raw page of code, there is no ELF information for doing symbol lookups or versioning. Simply call into the appropriate offset via the branch instruction, for example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ble&nbsp;&lt;offset&gt;(%sr2,&nbsp;%r0) </p>
<table>
<tr VALIGN=top>
<td>offset</td>
<td>function
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>00b0</td>
<td>lws_entry (CAS operations)
</td>
</tr>
<tr VALIGN=top>
<td>00e0</td>
<td>set_thread_pointer (used by glibc)
</td>
</tr>
<tr VALIGN=top>
<td>0100</td>
<td>linux_gateway_entry (syscall)
</td>
</tr>
</table>
<h3>ppc/32 functions</h3>
<p>The table below lists the symbols exported by the vDSO. The functions marked with a <i>*</i> are available only when the kernel is a PowerPC64 (64-bit) kernel. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_getres</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_gettime</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_datapage_offset</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_get_syscall_map</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_get_tbfreq</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_getcpu <i>*</i></td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_gettimeofday</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sigtramp_rt32</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sigtramp32</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sync_dicache</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sync_dicache_p5</td>
<td>LINUX_2.6.15
</td>
</tr>
</table>
<p> The <code>CLOCK_REALTIME_COARSE</code> and <code>CLOCK_MONOTONIC_COARSE</code> clocks are <i>not</i> supported by the <i>__kernel_clock_getres</i> and <i>__kernel_clock_gettime</i> interfaces; the kernel falls back to the real system call.</p>
<h3>ppc/64 functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_getres</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_gettime</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_datapage_offset</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_get_syscall_map</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_get_tbfreq</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_getcpu</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_gettimeofday</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sigtramp_rt64</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sync_dicache</td>
<td>LINUX_2.6.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sync_dicache_p5</td>
<td>LINUX_2.6.15
</td>
</tr>
</table>
<p> The <code>CLOCK_REALTIME_COARSE</code> and <code>CLOCK_MONOTONIC_COARSE</code> clocks are <i>not</i> supported by the <i>__kernel_clock_getres</i> and <i>__kernel_clock_gettime</i> interfaces; the kernel falls back to the real system call.</p>
<h3>riscv functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_rt_sigreturn</td>
<td>LINUX_4.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_gettimeofday</td>
<td>LINUX_4.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_gettime</td>
<td>LINUX_4.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_getres</td>
<td>LINUX_4.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_getcpu</td>
<td>LINUX_4.15
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_flush_icache</td>
<td>LINUX_4.15
</td>
</tr>
</table>
<h3>s390 functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_getres</td>
<td>LINUX_2.6.29
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_gettime</td>
<td>LINUX_2.6.29
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_gettimeofday</td>
<td>LINUX_2.6.29
</td>
</tr>
</table>
<h3>s390x functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_getres</td>
<td>LINUX_2.6.29
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_clock_gettime</td>
<td>LINUX_2.6.29
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_gettimeofday</td>
<td>LINUX_2.6.29
</td>
</tr>
</table>
<h3>sh (SuperH) functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_rt_sigreturn</td>
<td>LINUX_2.6
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sigreturn</td>
<td>LINUX_2.6
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_vsyscall</td>
<td>LINUX_2.6
</td>
</tr>
</table>
<h3>i386 functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_sigreturn</td>
<td>LINUX_2.5
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_rt_sigreturn</td>
<td>LINUX_2.5
</td>
</tr>
<tr VALIGN=top>
<td>__kernel_vsyscall</td>
<td>LINUX_2.5
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_clock_gettime</td>
<td>LINUX_2.6 (exported since Linux 3.15)
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_gettimeofday</td>
<td>LINUX_2.6 (exported since Linux 3.15)
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_time</td>
<td>LINUX_2.6 (exported since Linux 3.15)
</td>
</tr>
</table>
<h3>x86-64 functions</h3>
<p>The table below lists the symbols exported by the vDSO. All of these symbols are also available without the &quot;__vdso_&quot; prefix, but you should ignore those and stick to the names below. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_clock_gettime</td>
<td>LINUX_2.6
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_getcpu</td>
<td>LINUX_2.6
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_gettimeofday</td>
<td>LINUX_2.6
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_time</td>
<td>LINUX_2.6
</td>
</tr>
</table>
<h3>x86/x32 functions</h3>
<p>The table below lists the symbols exported by the vDSO. </p>
<table>
<tr VALIGN=top>
<td>symbol</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_clock_gettime</td>
<td>LINUX_2.6
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_getcpu</td>
<td>LINUX_2.6
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_gettimeofday</td>
<td>LINUX_2.6
</td>
</tr>
<tr VALIGN=top>
<td>__vdso_time</td>
<td>LINUX_2.6
</td>
</tr>
</table>
<h3>History</h3>
<p>The vDSO was originally just a single function&#8212;the vsyscall. In older kernels, you might see that name in a process&#8217;s memory map rather than &quot;vdso&quot;. Over time, people realized that this mechanism was a great way to pass more functionality to user space, so it was reconceived as a vDSO in the current format.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-syscalls/">syscalls</a></code>(2), <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) </p>
<p> The documents, examples, and source code in the Linux source code tree: </p>
<p> Documentation/ABI/stable/vdso Documentation/ia64/fsys.txt Documentation/vDSO/* (includes examples of using the vDSO) </p>
<p> find arch/ -iname &#8216;*vdso*&#8217; -o -iname &#8216;*gate*&#8217;</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
