---
title: "syscall(2)"
name: "syscall"
section: "2"
letter: "s"
url: "/docs/linux/man/2-syscall/"
description: "syscall – indirect system call"
---

<h2 class="name">NAME</h2>
<p> syscall &#8211; indirect system call </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/syscall.h&gt; /* For SYS_xxx definitions */
#include &lt;unistd.h&gt;
long syscall(long number, ...);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>syscall</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.19:</p>
<dd> _DEFAULT_SOURCE</p>
<dt>Before glibc 2.19:</p>
<dd> _BSD_SOURCE || _SVID_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>syscall</code>() is a small library function that invokes the system call whose assembly language interface has the specified <i>number</i> with the specified arguments. Employing <code>syscall</code>() is useful, for example, when invoking a system call that has no wrapper function in the C library. </p>
<p> <code>syscall</code>() saves CPU registers before making the system call, restores the registers upon return from the system call, and stores any error returned by the system call in <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3). </p>
<p> Symbolic constants for system call numbers can be found in the header file <i>&lt;sys/syscall.h&gt;</i>.</p>
<h2>RETURN VALUE</h2>
<p> The return value is defined by the system call being invoked. In general, a 0 return value indicates success. A -1 return value indicates an error, and an error number is stored in <i>errno</i>.</p>
<h2>NOTES</h2>
<p> <code>syscall</code>() first appeared in 4BSD.</p>
<h3>Architecture-specific requirements</h3>
<p> Each architecture ABI has its own requirements on how system call arguments are passed to the kernel. For system calls that have a glibc wrapper (e.g., most system calls), glibc handles the details of copying arguments to the right registers in a manner suitable for the architecture. However, when using <code>syscall</code>() to make a system call, the caller might need to handle architecture-dependent details; this requirement is most commonly encountered on certain 32-bit architectures. </p>
<p> For example, on the ARM architecture Embedded ABI (EABI), a 64-bit value (e.g., <i>long long</i>) must be aligned to an even register pair. Thus, using <code>syscall</code>() instead of the wrapper provided by glibc, the <code><a href="/docs/linux/man/2-readahead/">readahead</a></code>(2) system call would be invoked as follows on the ARM architecture with the EABI in little endian mode: </p>
<p> syscall(SYS_readahead, fd, 0,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(unsigned int)&nbsp;(offset&nbsp;&amp;&nbsp;0xFFFFFFFF),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(unsigned int)&nbsp;(offset&nbsp;&gt;&gt;&nbsp;32),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count); </p>
<p> Since the offset argument is 64 bits, and the first argument (<i>fd</i>) is passed in <i>r0</i>, the caller must manually split and align the 64-bit value so that it is passed in the <i>r2</i>/<i>r3</i> register pair. That means inserting a dummy value into <i>r1</i> (the second argument of 0). Care also must be taken so that the split follows endian conventions (according to the C ABI for the platform). </p>
<p> Similar issues can occur on MIPS with the O32 ABI, on PowerPC and parisc with the 32-bit ABI, and on Xtensa. </p>
<p> Note that while the parisc C ABI also uses aligned register pairs, it uses a shim layer to hide the issue from user space. </p>
<p> The affected system calls are <code><a href="/docs/linux/man/2-fadvise64_64/">fadvise64_64</a></code>(2), <code><a href="/docs/linux/man/2-ftruncate64/">ftruncate64</a></code>(2), <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2), <code><a href="/docs/linux/man/2-pread64/">pread64</a></code>(2), <code><a href="/docs/linux/man/2-pwrite64/">pwrite64</a></code>(2), <code><a href="/docs/linux/man/2-readahead/">readahead</a></code>(2), <code><a href="/docs/linux/man/2-sync_file_range/">sync_file_range</a></code>(2), and <code><a href="/docs/linux/man/2-truncate64/">truncate64</a></code>(2). </p>
<p> This does not affect syscalls that manually split and assemble 64-bit values such as <code><a href="/docs/linux/man/2-_llseek/">_llseek</a></code>(2), <code><a href="/docs/linux/man/2-preadv/">preadv</a></code>(2), <code><a href="/docs/linux/man/2-preadv2/">preadv2</a></code>(2), <code><a href="/docs/linux/man/2-pwritev/">pwritev</a></code>(2), and <code><a href="/docs/linux/man/2-pwritev2/">pwritev2</a></code>(2). Welcome to the wonderful world of historical baggage.</p>
<h3>Architecture calling conventions</h3>
<p> Every architecture has its own way of invoking and passing arguments to the kernel. The details for various architectures are listed in the two tables below. </p>
<p> The first table lists the instruction used to transition to kernel mode (which might not be the fastest or best way to transition to the kernel, so you might have to refer to <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7)), the register used to indicate the system call number, the register(s) used to return the system call result, and the register used to signal an error. </p>
<table>
<tr VALIGN=top>
<td>Arch/ABI&nbsp;<wbr>&nbsp;</td>
<td>Instruction&nbsp;<wbr>&nbsp;</td>
<td>System&nbsp;<wbr>&nbsp;</td>
<td>Ret&nbsp;<wbr>&nbsp;</td>
<td>Ret&nbsp;</td>
<td>Error&nbsp;<wbr>&nbsp;</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;</td>
<td>&nbsp;<wbr>&nbsp;</td>
<td>call #&nbsp;<wbr>&nbsp;</td>
<td>val&nbsp;<wbr>&nbsp;</td>
<td>val2&nbsp;</td>
<td>&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>alpha&nbsp;<wbr>&nbsp;</td>
<td>callsys&nbsp;<wbr>&nbsp;</td>
<td>v0&nbsp;<wbr>&nbsp;</td>
<td>v0&nbsp;<wbr>&nbsp;</td>
<td>a4&nbsp;</td>
<td>a3&nbsp;<wbr>&nbsp;</td>
<td>1, 6
</td>
</tr>
<tr VALIGN=top>
<td>arc&nbsp;<wbr>&nbsp;</td>
<td>trap0&nbsp;<wbr>&nbsp;</td>
<td>r8&nbsp;<wbr>&nbsp;</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>arm/OABI&nbsp;<wbr>&nbsp;</td>
<td>swi NR&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>2
</td>
</tr>
<tr VALIGN=top>
<td>arm/EABI&nbsp;<wbr>&nbsp;</td>
<td>swi 0x0&nbsp;<wbr>&nbsp;</td>
<td>r7&nbsp;<wbr>&nbsp;</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>r1&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>arm64&nbsp;<wbr>&nbsp;</td>
<td>svc #0&nbsp;<wbr>&nbsp;</td>
<td>w8&nbsp;<wbr>&nbsp;</td>
<td>x0&nbsp;<wbr>&nbsp;</td>
<td>x1&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>blackfin&nbsp;<wbr>&nbsp;</td>
<td>excpt 0x0&nbsp;<wbr>&nbsp;</td>
<td>P0&nbsp;<wbr>&nbsp;</td>
<td>R0&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>i386&nbsp;<wbr>&nbsp;</td>
<td>int $0x80&nbsp;<wbr>&nbsp;</td>
<td>eax&nbsp;<wbr>&nbsp;</td>
<td>eax&nbsp;<wbr>&nbsp;</td>
<td>edx&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ia64&nbsp;<wbr>&nbsp;</td>
<td>break 0x100000&nbsp;<wbr>&nbsp;</td>
<td>r15&nbsp;<wbr>&nbsp;</td>
<td>r8&nbsp;<wbr>&nbsp;</td>
<td>r9&nbsp;</td>
<td>r10&nbsp;<wbr>&nbsp;</td>
<td>1, 6
</td>
</tr>
<tr VALIGN=top>
<td>m68k&nbsp;<wbr>&nbsp;</td>
<td>trap #0&nbsp;<wbr>&nbsp;</td>
<td>d0&nbsp;<wbr>&nbsp;</td>
<td>d0&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>microblaze&nbsp;<wbr>&nbsp;</td>
<td>brki r14,8&nbsp;<wbr>&nbsp;</td>
<td>r12&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>mips&nbsp;<wbr>&nbsp;</td>
<td>syscall&nbsp;<wbr>&nbsp;</td>
<td>v0&nbsp;<wbr>&nbsp;</td>
<td>v0&nbsp;<wbr>&nbsp;</td>
<td>v1&nbsp;</td>
<td>a3&nbsp;<wbr>&nbsp;</td>
<td>1, 6
</td>
</tr>
<tr VALIGN=top>
<td>nios2&nbsp;<wbr>&nbsp;</td>
<td>trap&nbsp;<wbr>&nbsp;</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>r7&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>parisc&nbsp;<wbr>&nbsp;</td>
<td>ble 0x100(%sr2, %r0)&nbsp;<wbr>&nbsp;</td>
<td>r20&nbsp;<wbr>&nbsp;</td>
<td>r28&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>powerpc&nbsp;<wbr>&nbsp;</td>
<td>sc&nbsp;<wbr>&nbsp;</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>powerpc64&nbsp;<wbr>&nbsp;</td>
<td>sc&nbsp;<wbr>&nbsp;</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>cr0.SO&nbsp;<wbr>&nbsp;</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>riscv&nbsp;<wbr>&nbsp;</td>
<td>ecall&nbsp;<wbr>&nbsp;</td>
<td>a7&nbsp;<wbr>&nbsp;</td>
<td>a0&nbsp;<wbr>&nbsp;</td>
<td>a1&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>s390&nbsp;<wbr>&nbsp;</td>
<td>svc 0&nbsp;<wbr>&nbsp;</td>
<td>r1&nbsp;<wbr>&nbsp;</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>3
</td>
</tr>
<tr VALIGN=top>
<td>s390x&nbsp;<wbr>&nbsp;</td>
<td>svc 0&nbsp;<wbr>&nbsp;</td>
<td>r1&nbsp;<wbr>&nbsp;</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>3
</td>
</tr>
<tr VALIGN=top>
<td>superh&nbsp;<wbr>&nbsp;</td>
<td>trap #0x17&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>r1&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>4, 6
</td>
</tr>
<tr VALIGN=top>
<td>sparc/32&nbsp;<wbr>&nbsp;</td>
<td>t 0x10&nbsp;<wbr>&nbsp;</td>
<td>g1&nbsp;<wbr>&nbsp;</td>
<td>o0&nbsp;<wbr>&nbsp;</td>
<td>o1&nbsp;</td>
<td>psr/csr&nbsp;<wbr>&nbsp;</td>
<td>1, 6
</td>
</tr>
<tr VALIGN=top>
<td>sparc/64&nbsp;<wbr>&nbsp;</td>
<td>t 0x6d&nbsp;<wbr>&nbsp;</td>
<td>g1&nbsp;<wbr>&nbsp;</td>
<td>o0&nbsp;<wbr>&nbsp;</td>
<td>o1&nbsp;</td>
<td>psr/csr&nbsp;<wbr>&nbsp;</td>
<td>1, 6
</td>
</tr>
<tr VALIGN=top>
<td>tile&nbsp;<wbr>&nbsp;</td>
<td>swint1&nbsp;<wbr>&nbsp;</td>
<td>R10&nbsp;<wbr>&nbsp;</td>
<td>R00&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>R01&nbsp;<wbr>&nbsp;</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>x86-64&nbsp;<wbr>&nbsp;</td>
<td>syscall&nbsp;<wbr>&nbsp;</td>
<td>rax&nbsp;<wbr>&nbsp;</td>
<td>rax&nbsp;<wbr>&nbsp;</td>
<td>rdx&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>5
</td>
</tr>
<tr VALIGN=top>
<td>x32&nbsp;<wbr>&nbsp;</td>
<td>syscall&nbsp;<wbr>&nbsp;</td>
<td>rax&nbsp;<wbr>&nbsp;</td>
<td>rax&nbsp;<wbr>&nbsp;</td>
<td>rdx&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>5
</td>
</tr>
<tr VALIGN=top>
<td>xtensa&nbsp;<wbr>&nbsp;</td>
<td>syscall&nbsp;<wbr>&nbsp;</td>
<td>a2&nbsp;<wbr>&nbsp;</td>
<td>a2&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
</table>
<p> Notes:</p>
<dl>
<dt>[1]</p>
<dd> On a few architectures, a register is used as a boolean (0 indicating no error, and -1 indicating an error) to signal that the system call failed. The actual error value is still contained in the return register. On sparc, the carry bit (<i>csr</i>) in the processor status register (<i>psr</i>) is used instead of a full register. On powerpc64, the summary overflow bit (<i>SO</i>) in field 0 of the condition register (<i>cr0</i>) is used.</p>
<dt>[2]</p>
<dd> <i>NR</i> is the system call number.</p>
<dt>[3]</p>
<dd> For s390 and s390x, <i>NR</i> (the system call number) may be passed directly with <i>svc NR</i> if it is less than 256.</p>
<dt>[4]</p>
<dd> On SuperH, the trap number controls the maximum number of arguments passed. A <i>trap&nbsp;#0x10</i> can be used with only 0-argument system calls, a <i>trap&nbsp;#0x11</i> can be used with 0- or 1-argument system calls, and so on up to <i>trap #0x17</i> for 7-argument system calls.</p>
<dt>[5]</p>
<dd> The x32 ABI shares syscall table with x86-64 ABI, but there are some nuances:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> In order to indicate that a system call is called under the x32 ABI, an additional bit, <code>__X32_SYSCALL_BIT</code>, is bitwise-ORed with the system call number. The ABI used by a process affects some process behaviors, including signal handling or system call restarting.</p>
<dt>&bull;</p>
<dd> Since x32 has different sizes for <i>long</i> and pointer types, layouts of some (but not all; <i>struct timeval</i> or <i>struct rlimit</i> are 64-bit, for example) structures are different. In order to handle this, additional system calls are added to the system call table, starting from number 512 (without the <code>__X32_SYSCALL_BIT</code>). For example, <code>__NR_readv</code> is defined as 19 for the x86-64 ABI and as <i>__X32_SYSCALL_BIT</i> | <i></i><code>515</code> for the x32 ABI. Most of these additional system calls are actually identical to the system calls used for providing i386 compat. There are some notable exceptions, however, such as <code><a href="/docs/linux/man/2-preadv2/">preadv2</a></code>(2), which uses <i>struct iovec</i> entities with 4-byte pointers and sizes (&quot;compat_iovec&quot; in kernel terms), but passes an 8-byte <i>pos</i> argument in a single register and not two, as is done in every other ABI.</dl>
</dl>
<dt>[6]</p>
<dd> Some architectures (namely, Alpha, IA-64, MIPS, SuperH, sparc/32, and sparc/64) use an additional register (&quot;Retval2&quot; in the above table) to pass back a second return value from the <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) system call; Alpha uses this technique in the architecture-specific <code><a href="/docs/linux/man/2-getxpid/">getxpid</a></code>(2), <code><a href="/docs/linux/man/2-getxuid/">getxuid</a></code>(2), and <code><a href="/docs/linux/man/2-getxgid/">getxgid</a></code>(2) system calls as well. Other architectures do not use the second return value register in the system call interface, even if it is defined in the System V ABI.</dl>
<p> The second table shows the registers used to pass the system call arguments. </p>
<table>
<tr VALIGN=top>
<td>Arch/ABI</td>
<td>arg1&nbsp;<wbr>&nbsp;</td>
<td>arg2&nbsp;<wbr>&nbsp;</td>
<td>arg3&nbsp;<wbr>&nbsp;</td>
<td>arg4&nbsp;<wbr>&nbsp;</td>
<td>arg5&nbsp;<wbr>&nbsp;</td>
<td>arg6&nbsp;<wbr>&nbsp;</td>
<td>arg7&nbsp;<wbr>&nbsp;</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=9>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>alpha</td>
<td>a0&nbsp;<wbr>&nbsp;</td>
<td>a1&nbsp;<wbr>&nbsp;</td>
<td>a2&nbsp;<wbr>&nbsp;</td>
<td>a3&nbsp;<wbr>&nbsp;</td>
<td>a4&nbsp;<wbr>&nbsp;</td>
<td>a5&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>arc</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>r1&nbsp;<wbr>&nbsp;</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>r4&nbsp;<wbr>&nbsp;</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>arm/OABI</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>r1&nbsp;<wbr>&nbsp;</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>r4&nbsp;<wbr>&nbsp;</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>r6&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>arm/EABI</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>r1&nbsp;<wbr>&nbsp;</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>r4&nbsp;<wbr>&nbsp;</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>r6&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>arm64</td>
<td>x0&nbsp;<wbr>&nbsp;</td>
<td>x1&nbsp;<wbr>&nbsp;</td>
<td>x2&nbsp;<wbr>&nbsp;</td>
<td>x3&nbsp;<wbr>&nbsp;</td>
<td>x4&nbsp;<wbr>&nbsp;</td>
<td>x5&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>blackfin</td>
<td>R0&nbsp;<wbr>&nbsp;</td>
<td>R1&nbsp;<wbr>&nbsp;</td>
<td>R2&nbsp;<wbr>&nbsp;</td>
<td>R3&nbsp;<wbr>&nbsp;</td>
<td>R4&nbsp;<wbr>&nbsp;</td>
<td>R5&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>i386</td>
<td>ebx&nbsp;<wbr>&nbsp;</td>
<td>ecx&nbsp;<wbr>&nbsp;</td>
<td>edx&nbsp;<wbr>&nbsp;</td>
<td>esi&nbsp;<wbr>&nbsp;</td>
<td>edi&nbsp;<wbr>&nbsp;</td>
<td>ebp&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ia64</td>
<td>out0&nbsp;<wbr>&nbsp;</td>
<td>out1&nbsp;<wbr>&nbsp;</td>
<td>out2&nbsp;<wbr>&nbsp;</td>
<td>out3&nbsp;<wbr>&nbsp;</td>
<td>out4&nbsp;<wbr>&nbsp;</td>
<td>out5&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>m68k</td>
<td>d1&nbsp;<wbr>&nbsp;</td>
<td>d2&nbsp;<wbr>&nbsp;</td>
<td>d3&nbsp;<wbr>&nbsp;</td>
<td>d4&nbsp;<wbr>&nbsp;</td>
<td>d5&nbsp;<wbr>&nbsp;</td>
<td>a0&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>microblaze</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>r6&nbsp;<wbr>&nbsp;</td>
<td>r7&nbsp;<wbr>&nbsp;</td>
<td>r8&nbsp;<wbr>&nbsp;</td>
<td>r9&nbsp;<wbr>&nbsp;</td>
<td>r10&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>mips/o32</td>
<td>a0&nbsp;<wbr>&nbsp;</td>
<td>a1&nbsp;<wbr>&nbsp;</td>
<td>a2&nbsp;<wbr>&nbsp;</td>
<td>a3&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>mips/n32,64</td>
<td>a0&nbsp;<wbr>&nbsp;</td>
<td>a1&nbsp;<wbr>&nbsp;</td>
<td>a2&nbsp;<wbr>&nbsp;</td>
<td>a3&nbsp;<wbr>&nbsp;</td>
<td>a4&nbsp;<wbr>&nbsp;</td>
<td>a5&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>nios2</td>
<td>r4&nbsp;<wbr>&nbsp;</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>r6&nbsp;<wbr>&nbsp;</td>
<td>r7&nbsp;<wbr>&nbsp;</td>
<td>r8&nbsp;<wbr>&nbsp;</td>
<td>r9&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>parisc</td>
<td>r26&nbsp;<wbr>&nbsp;</td>
<td>r25&nbsp;<wbr>&nbsp;</td>
<td>r24&nbsp;<wbr>&nbsp;</td>
<td>r23&nbsp;<wbr>&nbsp;</td>
<td>r22&nbsp;<wbr>&nbsp;</td>
<td>r21&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>powerpc</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>r4&nbsp;<wbr>&nbsp;</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>r6&nbsp;<wbr>&nbsp;</td>
<td>r7&nbsp;<wbr>&nbsp;</td>
<td>r8&nbsp;<wbr>&nbsp;</td>
<td>r9&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>powerpc64</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>r4&nbsp;<wbr>&nbsp;</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>r6&nbsp;<wbr>&nbsp;</td>
<td>r7&nbsp;<wbr>&nbsp;</td>
<td>r8&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>riscv</td>
<td>a0&nbsp;<wbr>&nbsp;</td>
<td>a1&nbsp;<wbr>&nbsp;</td>
<td>a2&nbsp;<wbr>&nbsp;</td>
<td>a3&nbsp;<wbr>&nbsp;</td>
<td>a4&nbsp;<wbr>&nbsp;</td>
<td>a5&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>s390</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>r4&nbsp;<wbr>&nbsp;</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>r6&nbsp;<wbr>&nbsp;</td>
<td>r7&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>s390x</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>r3&nbsp;<wbr>&nbsp;</td>
<td>r4&nbsp;<wbr>&nbsp;</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>r6&nbsp;<wbr>&nbsp;</td>
<td>r7&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>superh</td>
<td>r4&nbsp;<wbr>&nbsp;</td>
<td>r5&nbsp;<wbr>&nbsp;</td>
<td>r6&nbsp;<wbr>&nbsp;</td>
<td>r7&nbsp;<wbr>&nbsp;</td>
<td>r0&nbsp;<wbr>&nbsp;</td>
<td>r1&nbsp;<wbr>&nbsp;</td>
<td>r2&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>sparc/32</td>
<td>o0&nbsp;<wbr>&nbsp;</td>
<td>o1&nbsp;<wbr>&nbsp;</td>
<td>o2&nbsp;<wbr>&nbsp;</td>
<td>o3&nbsp;<wbr>&nbsp;</td>
<td>o4&nbsp;<wbr>&nbsp;</td>
<td>o5&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>sparc/64</td>
<td>o0&nbsp;<wbr>&nbsp;</td>
<td>o1&nbsp;<wbr>&nbsp;</td>
<td>o2&nbsp;<wbr>&nbsp;</td>
<td>o3&nbsp;<wbr>&nbsp;</td>
<td>o4&nbsp;<wbr>&nbsp;</td>
<td>o5&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>tile</td>
<td>R00&nbsp;<wbr>&nbsp;</td>
<td>R01&nbsp;<wbr>&nbsp;</td>
<td>R02&nbsp;<wbr>&nbsp;</td>
<td>R03&nbsp;<wbr>&nbsp;</td>
<td>R04&nbsp;<wbr>&nbsp;</td>
<td>R05&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>x86-64</td>
<td>rdi&nbsp;<wbr>&nbsp;</td>
<td>rsi&nbsp;<wbr>&nbsp;</td>
<td>rdx&nbsp;<wbr>&nbsp;</td>
<td>r10&nbsp;<wbr>&nbsp;</td>
<td>r8&nbsp;<wbr>&nbsp;</td>
<td>r9&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>x32</td>
<td>rdi&nbsp;<wbr>&nbsp;</td>
<td>rsi&nbsp;<wbr>&nbsp;</td>
<td>rdx&nbsp;<wbr>&nbsp;</td>
<td>r10&nbsp;<wbr>&nbsp;</td>
<td>r8&nbsp;<wbr>&nbsp;</td>
<td>r9&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>xtensa</td>
<td>a6&nbsp;<wbr>&nbsp;</td>
<td>a3&nbsp;<wbr>&nbsp;</td>
<td>a4&nbsp;<wbr>&nbsp;</td>
<td>a5&nbsp;<wbr>&nbsp;</td>
<td>a8&nbsp;<wbr>&nbsp;</td>
<td>a9&nbsp;<wbr>&nbsp;</td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
</table>
<p> Notes:</p>
<dl>
<dt>[1]</p>
<dd> The mips/o32 system call convention passes arguments 5 through 8 on the user stack.</dl>
<p> Note that these tables don&#8217;t cover the entire calling convention&#8212;some architectures may indiscriminately clobber other registers not listed here.</p>
<h2>EXAMPLES</h2>
<p> #define _GNU_SOURCE #include &lt;unistd.h&gt; #include &lt;sys/syscall.h&gt; #include &lt;sys/types.h&gt; #include &lt;signal.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t tid; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tid&nbsp;=&nbsp;syscall(SYS_gettid);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;syscall(SYS_tgkill, getpid(), tid, SIGHUP); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-_syscall/">_syscall</a></code>(2), <code><a href="/docs/linux/man/2-intro/">intro</a></code>(2), <code><a href="/docs/linux/man/2-syscalls/">syscalls</a></code>(2), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
