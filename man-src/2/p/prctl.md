---
title: "prctl(2)"
name: "prctl"
section: "2"
letter: "p"
url: "/docs/linux/man/2-prctl/"
description: "prctl – operations on a process or thread"
---

<h2 class="name">NAME</h2>
<p> prctl &#8211; operations on a process or thread </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/prctl.h&gt;
int prctl(int option, unsigned long arg2, unsigned long arg3,
          unsigned long arg4, unsigned long arg5);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>prctl</code>() manipulates various aspects of the behavior of the calling thread or process. </p>
<p> Note that careless use of some <code>prctl</code>() operations can confuse the user-space run-time environment, so these operations should be used with care. </p>
<p> <code>prctl</code>() is called with a first argument describing what to do (with values defined in <i>&lt;linux/prctl.h&gt;</i>), and further arguments with a significance depending on the first one. The first argument can be:</p>
<dl>
<dt><code>PR_CAP_AMBIENT</code> (since Linux 4.3)</p>
<dd> Reads or changes the ambient capability set of the calling thread, according to the value of <i>arg2</i>, which must be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PR_CAP_AMBIENT_RAISE</code></p>
<dd> The capability specified in <i>arg3</i> is added to the ambient set. The specified capability must already be present in both the permitted and the inheritable sets of the process. This operation is not permitted if the <code>SECBIT_NO_CAP_AMBIENT_RAISE</code> securebit is set.</p>
<dt><code>PR_CAP_AMBIENT_LOWER</code></p>
<dd> The capability specified in <i>arg3</i> is removed from the ambient set.</p>
<dt><code>PR_CAP_AMBIENT_IS_SET</code></p>
<dd> The <code>prctl</code>() call returns 1 if the capability in <i>arg3</i> is in the ambient set and 0 if it is not.</p>
<dt><code>PR_CAP_AMBIENT_CLEAR_ALL</code></p>
<dd> All capabilities will be removed from the ambient set. This operation requires setting <i>arg3</i> to zero.</dl>
</dl>
<dt>
<dd> In all of the above operations, <i>arg4</i> and <i>arg5</i> must be specified as 0.</p>
<dt>
<dd> Higher-level interfaces layered on top of the above operations are provided in the <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3) library in the form of <code><a href="/docs/linux/man/3-cap_get_ambient/">cap_get_ambient</a></code>(3), <code><a href="/docs/linux/man/3-cap_set_ambient/">cap_set_ambient</a></code>(3), and <code><a href="/docs/linux/man/3-cap_reset_ambient/">cap_reset_ambient</a></code>(3).</p>
<dt><code>PR_CAPBSET_READ</code> (since Linux 2.6.25)</p>
<dd> Return (as the function result) 1 if the capability specified in <i>arg2</i> is in the calling thread&#8217;s capability bounding set, or 0 if it is not. (The capability constants are defined in <i>&lt;linux/capability.h&gt;</i>.) The capability bounding set dictates whether the process can receive the capability through a file&#8217;s permitted capability set on a subsequent call to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt>
<dd> If the capability specified in <i>arg2</i> is not valid, then the call fails with the error <code>EINVAL</code>.</p>
<dt>
<dd> A higher-level interface layered on top of this operation is provided in the <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3) library in the form of <code><a href="/docs/linux/man/3-cap_get_bound/">cap_get_bound</a></code>(3).</p>
<dt><code>PR_CAPBSET_DROP</code> (since Linux 2.6.25)</p>
<dd> If the calling thread has the <code>CAP_SETPCAP</code> capability within its user namespace, then drop the capability specified by <i>arg2</i> from the calling thread&#8217;s capability bounding set. Any children of the calling thread will inherit the newly reduced bounding set.</p>
<dt>
<dd> The call fails with the error: <code>EPERM</code> if the calling thread does not have the <code>CAP_SETPCAP</code>; <code>EINVAL</code> if <i>arg2</i> does not represent a valid capability; or <code>EINVAL</code> if file capabilities are not enabled in the kernel, in which case bounding sets are not supported.</p>
<dt>
<dd> A higher-level interface layered on top of this operation is provided in the <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3) library in the form of <code><a href="/docs/linux/man/3-cap_drop_bound/">cap_drop_bound</a></code>(3).</p>
<dt><code>PR_SET_CHILD_SUBREAPER</code> (since Linux 3.4)</p>
<dd> If <i>arg2</i> is nonzero, set the &quot;child subreaper&quot; attribute of the calling process; if <i>arg2</i> is zero, unset the attribute.</p>
<dt>
<dd> A subreaper fulfills the role of <code><a href="/docs/linux/man/1-init/">init</a></code>(1) for its descendant processes. When a process becomes orphaned (i.e., its immediate parent terminates), then that process will be reparented to the nearest still living ancestor subreaper. Subsequently, calls to <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2) in the orphaned process will now return the PID of the subreaper process, and when the orphan terminates, it is the subreaper process that will receive a <code>SIGCHLD</code> signal and will be able to <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) on the process to discover its termination status.</p>
<dt>
<dd> The setting of the &quot;child subreaper&quot; attribute is not inherited by children created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2). The setting is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt>
<dd> Establishing a subreaper process is useful in session management frameworks where a hierarchical group of processes is managed by a subreaper process that needs to be informed when one of the processes&#8212;for example, a double-forked daemon&#8212;terminates (perhaps so that it can restart that process). Some <code><a href="/docs/linux/man/1-init/">init</a></code>(1) frameworks (e.g., <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)) employ a subreaper process for similar reasons.</p>
<dt><code>PR_GET_CHILD_SUBREAPER</code> (since Linux 3.4)</p>
<dd> Return the &quot;child subreaper&quot; setting of the caller, in the location pointed to by <i>(int&nbsp;*) arg2</i>.</p>
<dt><code>PR_SET_DUMPABLE</code> (since Linux 2.3.20)</p>
<dd> Set the state of the &quot;dumpable&quot; attribute, which determines whether core dumps are produced for the calling process upon delivery of a signal whose default behavior is to produce a core dump.</p>
<dt>
<dd> In kernels up to and including 2.6.12, <i>arg2</i> must be either 0 (<code>SUID_DUMP_DISABLE</code>, process is not dumpable) or 1 (<code>SUID_DUMP_USER</code>, process is dumpable). Between kernels 2.6.13 and 2.6.17, the value 2 was also permitted, which caused any binary which normally would not be dumped to be dumped readable by root only; for security reasons, this feature has been removed. (See also the description of <i>/proc/sys/fs/suid_dumpable</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).)</p>
<dt>
<dd> Normally, the &quot;dumpable&quot; attribute is set to 1. However, it is reset to the current value contained in the file <i>/proc/sys/fs/suid_dumpable</i> (which by default has the value 0), in the following circumstances:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> The process&#8217;s effective user or group ID is changed.</p>
<dt>*</p>
<dd> The process&#8217;s filesystem user or group ID is changed (see <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)).</p>
<dt>*</p>
<dd> The process executes (<code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)) a set-user-ID or set-group-ID program, resulting in a change of either the effective user ID or the effective group ID.</p>
<dt>*</p>
<dd> The process executes (<code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)) a program that has file capabilities (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)), but only if the permitted capabilities gained exceed those already permitted for the process.</dl>
</dl>
<dt>
<dd> Processes that are not dumpable can not be attached via <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) <code>PTRACE_ATTACH</code>; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) for further details.</p>
<dt>
<dd> If a process is not dumpable, the ownership of files in the process&#8217;s <i>/proc/[pid]</i> directory is affected as described in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt><code>PR_GET_DUMPABLE</code> (since Linux 2.3.20)</p>
<dd> Return (as the function result) the current state of the calling process&#8217;s dumpable attribute.</p>
<dt><code>PR_SET_ENDIAN</code> (since Linux 2.6.18, PowerPC only)</p>
<dd> Set the endian-ness of the calling process to the value given in <i>arg2</i>, which should be one of the following: <code>PR_ENDIAN_BIG</code>, <code>PR_ENDIAN_LITTLE</code>, or <code>PR_ENDIAN_PPC_LITTLE</code> (PowerPC pseudo little endian).</p>
<dt><code>PR_GET_ENDIAN</code> (since Linux 2.6.18, PowerPC only)</p>
<dd> Return the endian-ness of the calling process, in the location pointed to by <i>(int&nbsp;*) arg2</i>.</p>
<dt><code>PR_SET_FP_MODE</code> (since Linux 4.0, only on MIPS)</p>
<dd> On the MIPS architecture, user-space code can be built using an ABI which permits linking with code that has more restrictive floating-point (FP) requirements. For example, user-space code may be built to target the O32 FPXX ABI and linked with code built for either one of the more restrictive FP32 or FP64 ABIs. When more restrictive code is linked in, the overall requirement for the process is to use the more restrictive floating-point mode.</p>
<dt>
<dd> Because the kernel has no means of knowing in advance which mode the process should be executed in, and because these restrictions can change over the lifetime of the process, the <code>PR_SET_FP_MODE</code> operation is provided to allow control of the floating-point mode from user space.</p>
<dt>
<dd> The <i>(unsigned int) arg2</i> argument is a bit mask describing the floating-point mode used:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PR_FP_MODE_FR</code></p>
<dd> When this bit is <i>unset</i> (so called <code>FR=0</code> or <code>FR0</code> mode), the 32 floating-point registers are 32 bits wide, and 64-bit registers are represented as a pair of registers (even- and odd- numbered, with the even-numbered register containing the lower 32 bits, and the odd-numbered register containing the higher 32 bits).</p>
<dt>
<dd> When this bit is <i>set</i> (on supported hardware), the 32 floating-point registers are 64 bits wide (so called <code>FR=1</code> or <code>FR1</code> mode). Note that modern MIPS implementations (MIPS R6 and newer) support <code>FR=1</code> mode only.</p>
<dt>
<dd> Applications that use the O32 FP32 ABI can operate only when this bit is <i>unset</i> (<code>FR=0</code>; or they can be used with FRE enabled, see below). Applications that use the O32 FP64 ABI (and the O32 FP64A ABI, which exists to provide the ability to operate with existing FP32 code; see below) can operate only when this bit is <i>set</i> (<code>FR=1</code>). Applications that use the O32 FPXX ABI can operate with either <code>FR=0</code> or <code>FR=1</code>.</p>
<dt><code>PR_FP_MODE_FRE</code></p>
<dd> Enable emulation of 32-bit floating-point mode. When this mode is enabled, it emulates 32-bit floating-point operations by raising a reserved-instruction exception on every instruction that uses 32-bit formats and the kernel then handles the instruction in software. (The problem lies in the discrepancy of handling odd-numbered registers which are the high 32 bits of 64-bit registers with even numbers in <code>FR=0</code> mode and the lower 32-bit parts of odd-numbered 64-bit registers in <code>FR=1</code> mode.) Enabling this bit is necessary when code with the O32 FP32 ABI should operate with code with compatible the O32 FPXX or O32 FP64A ABIs (which require <code>FR=1</code> FPU mode) or when it is executed on newer hardware (MIPS R6 onwards) which lacks <code>FR=0</code> mode support when a binary with the FP32 ABI is used.</p>
<dt>
<dd> Note that this mode makes sense only when the FPU is in 64-bit mode (<code>FR=1</code>).</p>
<dt>
<dd> Note that the use of emulation inherently has a significant performance hit and should be avoided if possible.</dl>
</dl>
<dt>
<dd> In the N32/N64 ABI, 64-bit floating-point mode is always used, so FPU emulation is not required and the FPU always operates in <code>FR=1</code> mode.</p>
<dt>
<dd> This option is mainly intended for use by the dynamic linker (<code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)).</p>
<dt>
<dd> The arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt><code>PR_GET_FP_MODE</code> (since Linux 4.0, only on MIPS)</p>
<dd> Return (as the function result) the current floating-point mode (see the description of <code>PR_SET_FP_MODE</code> for details).</p>
<dt>
<dd> On success, the call returns a bit mask which represents the current floating-point mode.</p>
<dt>
<dd> The arguments <i>arg2</i>, <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt><code>PR_SET_FPEMU</code> (since Linux 2.4.18, 2.5.9, only on ia64)</p>
<dd> Set floating-point emulation control bits to <i>arg2</i>. Pass <code>PR_FPEMU_NOPRINT</code> to silently emulate floating-point operation accesses, or <code>PR_FPEMU_SIGFPE</code> to not emulate floating-point operations and send <code>SIGFPE</code> instead.</p>
<dt><code>PR_GET_FPEMU</code> (since Linux 2.4.18, 2.5.9, only on ia64)</p>
<dd> Return floating-point emulation control bits, in the location pointed to by <i>(int&nbsp;*) arg2</i>.</p>
<dt><code>PR_SET_FPEXC</code> (since Linux 2.4.21, 2.5.32, only on PowerPC)</p>
<dd> Set floating-point exception mode to <i>arg2</i>. Pass <code>PR_FP_EXC_SW_ENABLE</code> to use FPEXC for FP exception enables, <code>PR_FP_EXC_DIV</code> for floating-point divide by zero, <code>PR_FP_EXC_OVF</code> for floating-point overflow, <code>PR_FP_EXC_UND</code> for floating-point underflow, <code>PR_FP_EXC_RES</code> for floating-point inexact result, <code>PR_FP_EXC_INV</code> for floating-point invalid operation, <code>PR_FP_EXC_DISABLED</code> for FP exceptions disabled, <code>PR_FP_EXC_NONRECOV</code> for async nonrecoverable exception mode, <code>PR_FP_EXC_ASYNC</code> for async recoverable exception mode, <code>PR_FP_EXC_PRECISE</code> for precise exception mode.</p>
<dt><code>PR_GET_FPEXC</code> (since Linux 2.4.21, 2.5.32, only on PowerPC)</p>
<dd> Return floating-point exception mode, in the location pointed to by <i>(int&nbsp;*) arg2</i>.</p>
<dt><code>PR_SET_IO_FLUSHER</code> (since Linux 5.6)</p>
<dd> If a user process is involved in the block layer or filesystem I/O path, and can allocate memory while processing I/O requests it must set <i>arg2</i> to 1. This will put the process in the IO_FLUSHER state, which allows it special treatment to make progress when allocating memory. If <i>arg2</i> is 0, the process will clear the IO_FLUSHER state, and the default behavior will be used.</p>
<dt>
<dd> The calling process must have the <code>CAP_SYS_RESOURCE</code> capability.</p>
<dt>
<dd> <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> must be zero.</p>
<dt>
<dd> The IO_FLUSHER state is inherited by a child process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt>
<dd> Examples of IO_FLUSHER applications are FUSE daemons, SCSI device emulation daemons, and daemons that perform error handling like multipath path recovery applications.</p>
<dt><code>PR_GET_IO_FLUSHER (Since Linux 5.6)</code></p>
<dd> Return (as the function result) the IO_FLUSHER state of the caller. A value of 1 indicates that the caller is in the IO_FLUSHER state; 0 indicates that the caller is not in the IO_FLUSHER state.</p>
<dt>
<dd> The calling process must have the <code>CAP_SYS_RESOURCE</code> capability.</p>
<dt>
<dd> <i>arg2</i>, <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> must be zero.</p>
<dt><code>PR_SET_KEEPCAPS</code> (since Linux 2.2.18)</p>
<dd> Set the state of the calling thread&#8217;s &quot;keep capabilities&quot; flag. The effect of this flag is described in <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7). <i>arg2</i> must be either 0 (clear the flag) or 1 (set the flag). The &quot;keep capabilities&quot; value will be reset to 0 on subsequent calls to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>PR_GET_KEEPCAPS</code> (since Linux 2.2.18)</p>
<dd> Return (as the function result) the current state of the calling thread&#8217;s &quot;keep capabilities&quot; flag. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for a description of this flag.</p>
<dt><code>PR_MCE_KILL</code> (since Linux 2.6.32)</p>
<dd> Set the machine check memory corruption kill policy for the calling thread. If <i>arg2</i> is <code>PR_MCE_KILL_CLEAR</code>, clear the thread memory corruption kill policy and use the system-wide default. (The system-wide default is defined by <i>/proc/sys/vm/memory_failure_early_kill</i>; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).) If <i>arg2</i> is <code>PR_MCE_KILL_SET</code>, use a thread-specific memory corruption kill policy. In this case, <i>arg3</i> defines whether the policy is <i>early kill</i> (<code>PR_MCE_KILL_EARLY</code>), <i>late kill</i> (<code>PR_MCE_KILL_LATE</code>), or the system-wide default (<code>PR_MCE_KILL_DEFAULT</code>). Early kill means that the thread receives a <code>SIGBUS</code> signal as soon as hardware memory corruption is detected inside its address space. In late kill mode, the process is killed only when it accesses a corrupted page. See <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) for more information on the <code>SIGBUS</code> signal. The policy is inherited by children. The remaining unused <code>prctl</code>() arguments must be zero for future compatibility.</p>
<dt><code>PR_MCE_KILL_GET</code> (since Linux 2.6.32)</p>
<dd> Return (as the function result) the current per-process machine check kill policy. All unused <code>prctl</code>() arguments must be zero.</p>
<dt><code>PR_SET_MM</code> (since Linux 3.3)</p>
<dd> Modify certain kernel memory map descriptor fields of the calling process. Usually these fields are set by the kernel and dynamic loader (see <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) for more information) and a regular application should not use this feature. However, there are cases, such as self-modifying programs, where a program might find it useful to change its own memory map.</p>
<dt>
<dd> The calling process must have the <code>CAP_SYS_RESOURCE</code> capability. The value in <i>arg2</i> is one of the options below, while <i>arg3</i> provides a new value for the option. The <i>arg4</i> and <i>arg5</i> arguments must be zero if unused.</p>
<dt>
<dd> Before Linux 3.10, this feature is available only if the kernel is built with the <code>CONFIG_CHECKPOINT_RESTORE</code> option enabled.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PR_SET_MM_START_CODE</code></p>
<dd> Set the address above which the program text can run. The corresponding memory area must be readable and executable, but not writable or shareable (see <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2) and <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) for more information).</p>
<dt><code>PR_SET_MM_END_CODE</code></p>
<dd> Set the address below which the program text can run. The corresponding memory area must be readable and executable, but not writable or shareable.</p>
<dt><code>PR_SET_MM_START_DATA</code></p>
<dd> Set the address above which initialized and uninitialized (bss) data are placed. The corresponding memory area must be readable and writable, but not executable or shareable.</p>
<dt><code>PR_SET_MM_END_DATA</code></p>
<dd> Set the address below which initialized and uninitialized (bss) data are placed. The corresponding memory area must be readable and writable, but not executable or shareable.</p>
<dt><code>PR_SET_MM_START_STACK</code></p>
<dd> Set the start address of the stack. The corresponding memory area must be readable and writable.</p>
<dt><code>PR_SET_MM_START_BRK</code></p>
<dd> Set the address above which the program heap can be expanded with <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2) call. The address must be greater than the ending address of the current program data segment. In addition, the combined size of the resulting heap and the size of the data segment can&#8217;t exceed the <code>RLIMIT_DATA</code> resource limit (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)).</p>
<dt><code>PR_SET_MM_BRK</code></p>
<dd> Set the current <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2) value. The requirements for the address are the same as for the <code>PR_SET_MM_START_BRK</code> option.</dl>
<p> The following options are available since Linux 3.5.</p>
<dl>
<dt><code>PR_SET_MM_ARG_START</code></p>
<dd> Set the address above which the program command line is placed.</p>
<dt><code>PR_SET_MM_ARG_END</code></p>
<dd> Set the address below which the program command line is placed.</p>
<dt><code>PR_SET_MM_ENV_START</code></p>
<dd> Set the address above which the program environment is placed.</p>
<dt><code>PR_SET_MM_ENV_END</code></p>
<dd> Set the address below which the program environment is placed.</p>
<dt>
<dd> The address passed with <code>PR_SET_MM_ARG_START</code>, <code>PR_SET_MM_ARG_END</code>, <code>PR_SET_MM_ENV_START</code>, and <code>PR_SET_MM_ENV_END</code> should belong to a process stack area. Thus, the corresponding memory area must be readable, writable, and (depending on the kernel configuration) have the <code>MAP_GROWSDOWN</code> attribute set (see <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)).</p>
<dt><code>PR_SET_MM_AUXV</code></p>
<dd> Set a new auxiliary vector. The <i>arg3</i> argument should provide the address of the vector. The <i>arg4</i> is the size of the vector.</p>
<dt><code>PR_SET_MM_EXE_FILE</code></p>
<dd> Supersede the <i>/proc/pid/exe</i> symbolic link with a new one pointing to a new executable file identified by the file descriptor provided in <i>arg3</i> argument. The file descriptor should be obtained with a regular <code><a href="/docs/linux/man/2-open/">open</a></code>(2) call.</p>
<dt>
<dd> To change the symbolic link, one needs to unmap all existing executable memory areas, including those created by the kernel itself (for example the kernel usually creates at least one executable memory area for the ELF <i>.text</i> section).</p>
<dt>
<dd> In Linux 4.9 and earlier, the <code>PR_SET_MM_EXE_FILE</code> operation can be performed only once in a process&#8217;s lifetime; attempting to perform the operation a second time results in the error <code>EPERM</code>. This restriction was enforced for security reasons that were subsequently deemed specious, and the restriction was removed in Linux 4.10 because some user-space applications needed to perform this operation more than once.</dl>
<p> The following options are available since Linux 3.18.</p>
<dl>
<dt><code>PR_SET_MM_MAP</code></p>
<dd> Provides one-shot access to all the addresses by passing in a <i>struct prctl_mm_map</i> (as defined in <i>&lt;linux/prctl.h&gt;</i>). The <i>arg4</i> argument should provide the size of the struct.</p>
<dt>
<dd> This feature is available only if the kernel is built with the <code>CONFIG_CHECKPOINT_RESTORE</code> option enabled.</p>
<dt><code>PR_SET_MM_MAP_SIZE</code></p>
<dd> Returns the size of the <i>struct prctl_mm_map</i> the kernel expects. This allows user space to find a compatible struct. The <i>arg4</i> argument should be a pointer to an unsigned int.</p>
<dt>
<dd> This feature is available only if the kernel is built with the <code>CONFIG_CHECKPOINT_RESTORE</code> option enabled.</dl>
</dl>
<dt><code>PR_MPX_ENABLE_MANAGEMENT</code>, <code>PR_MPX_DISABLE_MANAGEMENT</code> (since Linux 3.19, removed in Linux 5.4; only on x86)</p>
<dd> Enable or disable kernel management of Memory Protection eXtensions (MPX) bounds tables. The <i>arg2</i>, <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> arguments must be zero.</p>
<dt>
<dd> MPX is a hardware-assisted mechanism for performing bounds checking on pointers. It consists of a set of registers storing bounds information and a set of special instruction prefixes that tell the CPU on which instructions it should do bounds enforcement. There is a limited number of these registers and when there are more pointers than registers, their contents must be &quot;spilled&quot; into a set of tables. These tables are called &quot;bounds tables&quot; and the MPX <code>prctl</code>() operations control whether the kernel manages their allocation and freeing.</p>
<dt>
<dd> When management is enabled, the kernel will take over allocation and freeing of the bounds tables. It does this by trapping the #BR exceptions that result at first use of missing bounds tables and instead of delivering the exception to user space, it allocates the table and populates the bounds directory with the location of the new table. For freeing, the kernel checks to see if bounds tables are present for memory which is not allocated, and frees them if so.</p>
<dt>
<dd> Before enabling MPX management using <code>PR_MPX_ENABLE_MANAGEMENT</code>, the application must first have allocated a user-space buffer for the bounds directory and placed the location of that directory in the <i>bndcfgu</i> register.</p>
<dt>
<dd> These calls fail if the CPU or kernel does not support MPX. Kernel support for MPX is enabled via the <code>CONFIG_X86_INTEL_MPX</code> configuration option. You can check whether the CPU supports MPX by looking for the <i>mpx</i> CPUID bit, like with the following command:</p>
<dt>
<dd> cat /proc/cpuinfo | grep &#8216; mpx &#8216;</p>
<dt>
<dd> A thread may not switch in or out of long (64-bit) mode while MPX is enabled.</p>
<dt>
<dd> All threads in a process are affected by these calls.</p>
<dt>
<dd> The child of a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits the state of MPX management. During <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), MPX management is reset to a state as if <code>PR_MPX_DISABLE_MANAGEMENT</code> had been called.</p>
<dt>
<dd> For further information on Intel MPX, see the kernel source file <i>Documentation/x86/intel_mpx.txt</i>.</p>
<dt>
<dd> Due to a lack of toolchain support, <code>PR_MPX_ENABLE_MANAGEMENT</code> and <code>PR_MPX_DISABLE_MANAGEMENT</code> are not supported in Linux 5.4 and later.</p>
<dt><code>PR_SET_NAME</code> (since Linux 2.6.9)</p>
<dd> Set the name of the calling thread, using the value in the location pointed to by <i>(char&nbsp;*) arg2</i>. The name can be up to 16 bytes long, including the terminating null byte. (If the length of the string, including the terminating null byte, exceeds 16 bytes, the string is silently truncated.) This is the same attribute that can be set via <code><a href="/docs/linux/man/3-pthread_setname_np/">pthread_setname_np</a></code>(3) and retrieved using <code><a href="/docs/linux/man/3-pthread_getname_np/">pthread_getname_np</a></code>(3). The attribute is likewise accessible via <i>/proc/self/task/[tid]/comm</i> (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)), where <i>[tid]</i> is the thread ID of the calling thread, as returned by <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2).</p>
<dt><code>PR_GET_NAME</code> (since Linux 2.6.11)</p>
<dd> Return the name of the calling thread, in the buffer pointed to by <i>(char&nbsp;*) arg2</i>. The buffer should allow space for up to 16 bytes; the returned string will be null-terminated.</p>
<dt><code>PR_SET_NO_NEW_PRIVS</code> (since Linux 3.5)</p>
<dd> Set the calling thread&#8217;s <i>no_new_privs</i> attribute to the value in <i>arg2</i>. With <i>no_new_privs</i> set to 1, <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) promises not to grant privileges to do anything that could not have been done without the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) call (for example, rendering the set-user-ID and set-group-ID mode bits, and file capabilities non-functional). Once set, the <i>no_new_privs</i> attribute cannot be unset. The setting of this attribute is inherited by children created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), and preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt>
<dd> Since Linux 4.10, the value of a thread&#8217;s <i>no_new_privs</i> attribute can be viewed via the <i>NoNewPrivs</i> field in the <i>/proc/[pid]/status</i> file.</p>
<dt>
<dd> For more information, see the kernel source file <i>Documentation/userspace-api/no_new_privs.rst</i> (or <i>Documentation/prctl/no_new_privs.txt</i> before Linux 4.13). See also <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2).</p>
<dt><code>PR_GET_NO_NEW_PRIVS</code> (since Linux 3.5)</p>
<dd> Return (as the function result) the value of the <i>no_new_privs</i> attribute for the calling thread. A value of 0 indicates the regular <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) behavior. A value of 1 indicates <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) will operate in the privilege-restricting mode described above.</p>
<dt><code>PR_PAC_RESET_KEYS</code> (since Linux 5.0, only on arm64)</p>
<dd> Securely reset the thread&#8217;s pointer authentication keys to fresh random values generated by the kernel.</p>
<dt>
<dd> The set of keys to be reset is specified by <i>arg2</i>, which must be a logical OR of zero or more of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PR_PAC_APIAKEY</code></p>
<dd> instruction authentication key A</p>
<dt><code>PR_PAC_APIBKEY</code></p>
<dd> instruction authentication key B</p>
<dt><code>PR_PAC_APDAKEY</code></p>
<dd> data authentication key A</p>
<dt><code>PR_PAC_APDBKEY</code></p>
<dd> data authentication key B</p>
<dt><code>PR_PAC_APGAKEY</code></p>
<dd> generic authentication &#8220;A&#8221; key.</p>
<dt>
<dd> (Yes folks, there really is no generic B key.)</dl>
</dl>
<dt>
<dd> As a special case, if <i>arg2</i> is zero, then all the keys are reset. Since new keys could be added in future, this is the recommended way to completely wipe the existing keys when establishing a clean execution context. Note that there is no need to use <code>PR_PAC_RESET_KEYS</code> in preparation for calling <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), since <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) resets all the pointer authentication keys.</p>
<dt>
<dd> The remaining arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> must all be zero.</p>
<dt>
<dd> If the arguments are invalid, and in particular if <i>arg2</i> contains set bits that are unrecognized or that correspond to a key not available on this platform, then the call fails with error <code>EINVAL</code>.</p>
<dt>
<dd> <code>Warning:</code> Because the compiler or run-time environment may be using some or all of the keys, a successful <code>PR_PAC_RESET_KEYS</code> may crash the calling process. The conditions for using it safely are complex and system-dependent. Don&#8217;t use it unless you know what you are doing.</p>
<dt>
<dd> For more information, see the kernel source file <i>Documentation/arm64/pointer-authentication.rst</i> (or <i>Documentation/arm64/pointer-authentication.txt</i> before Linux 5.3).</p>
<dt><code>PR_SET_PDEATHSIG</code> (since Linux 2.1.57)</p>
<dd> Set the parent-death signal of the calling process to <i>arg2</i> (either a signal value in the range 1..<code>NSIG</code>-1<code>,</code> or 0 to clear). This is the signal that the calling process will get when its parent dies.</p>
<dt>
<dd> <i>Warning</i>: the &quot;parent&quot; in this case is considered to be the <i>thread</i> that created this process. In other words, the signal will be sent when that thread terminates (via, for example, <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3)), rather than after all of the threads in the parent process terminate.</p>
<dt>
<dd> The parent-death signal is sent upon subsequent termination of the parent thread and also upon termination of each subreaper process (see the description of <code>PR_SET_CHILD_SUBREAPER</code> above) to which the caller is subsequently reparented. If the parent thread and all ancestor subreapers have already terminated by the time of the <code>PR_SET_PDEATHSIG</code> operation, then no parent-death signal is sent to the caller.</p>
<dt>
<dd> The parent-death signal is process-directed (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)) and, if the child installs a handler using the <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) <code>SA_SIGINFO</code> flag, the <i>si_pid</i> field of the <i>siginfo_t</i> argument of the handler contains the PID of the terminating parent process.</p>
<dt>
<dd> The parent-death signal setting is cleared for the child of a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). It is also (since Linux 2.4.36 / 2.6.23) cleared when executing a set-user-ID or set-group-ID binary, or a binary that has associated capabilities (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)); otherwise, this value is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). The parent-death signal setting is also cleared upon changes to any of the following thread credentials: effective user ID, effective group ID, filesystem user ID, or filesystem group ID.</p>
<dt><code>PR_GET_PDEATHSIG</code> (since Linux 2.3.15)</p>
<dd> Return the current value of the parent process death signal, in the location pointed to by <i>(int&nbsp;*) arg2</i>.</p>
<dt><code>PR_SET_PTRACER</code> (since Linux 3.4)</p>
<dd> This is meaningful only when the Yama LSM is enabled and in mode 1 (&quot;restricted ptrace&quot;, visible via <i>/proc/sys/kernel/yama/ptrace_scope</i>). When a &quot;ptracer process ID&quot; is passed in <i>arg2</i>, the caller is declaring that the ptracer process can <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) the calling process as if it were a direct process ancestor. Each <code>PR_SET_PTRACER</code> operation replaces the previous &quot;ptracer process ID&quot;. Employing <code>PR_SET_PTRACER</code> with <i>arg2</i> set to 0 clears the caller&#8217;s &quot;ptracer process ID&quot;. If <i>arg2</i> is <code>PR_SET_PTRACER_ANY</code>, the ptrace restrictions introduced by Yama are effectively disabled for the calling process.</p>
<dt>
<dd> For further information, see the kernel source file <i>Documentation/admin-guide/LSM/Yama.rst</i> (or <i>Documentation/security/Yama.txt</i> before Linux 4.13).</p>
<dt><code>PR_SET_SECCOMP</code> (since Linux 2.6.23)</p>
<dd> Set the secure computing (seccomp) mode for the calling thread, to limit the available system calls. The more recent <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) system call provides a superset of the functionality of <code>PR_SET_SECCOMP</code>.</p>
<dt>
<dd> The seccomp mode is selected via <i>arg2</i>. (The seccomp constants are defined in <i>&lt;linux/seccomp.h&gt;</i>.)</p>
<dt>
<dd> With <i>arg2</i> set to <code>SECCOMP_MODE_STRICT</code>, the only system calls that the thread is permitted to make are <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) (but not <code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2)), and <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2). Other system calls result in the delivery of a <code>SIGKILL</code> signal. Strict secure computing mode is useful for number-crunching applications that may need to execute untrusted byte code, perhaps obtained by reading from a pipe or socket. This operation is available only if the kernel is configured with <code>CONFIG_SECCOMP</code> enabled.</p>
<dt>
<dd> With <i>arg2</i> set to <code>SECCOMP_MODE_FILTER</code> (since Linux 3.5), the system calls allowed are defined by a pointer to a Berkeley Packet Filter passed in <i>arg3</i>. This argument is a pointer to <i>struct sock_fprog</i>; it can be designed to filter arbitrary system calls and system call arguments. This mode is available only if the kernel is configured with <code>CONFIG_SECCOMP_FILTER</code> enabled.</p>
<dt>
<dd> If <code>SECCOMP_MODE_FILTER</code> filters permit <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), then the seccomp mode is inherited by children created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2); if <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) is permitted, then the seccomp mode is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). If the filters permit <code>prctl</code>() calls, then additional filters can be added; they are run in order until the first non-allow result is seen.</p>
<dt>
<dd> For further information, see the kernel source file <i>Documentation/userspace-api/seccomp_filter.rst</i> (or <i>Documentation/prctl/seccomp_filter.txt</i> before Linux 4.13).</p>
<dt><code>PR_GET_SECCOMP</code> (since Linux 2.6.23)</p>
<dd> Return (as the function result) the secure computing mode of the calling thread. If the caller is not in secure computing mode, this operation returns 0; if the caller is in strict secure computing mode, then the <code>prctl</code>() call will cause a <code>SIGKILL</code> signal to be sent to the process. If the caller is in filter mode, and this system call is allowed by the seccomp filters, it returns 2; otherwise, the process is killed with a <code>SIGKILL</code> signal. This operation is available only if the kernel is configured with <code>CONFIG_SECCOMP</code> enabled.</p>
<dt>
<dd> Since Linux 3.8, the <i>Seccomp</i> field of the <i>/proc/[pid]/status</i> file provides a method of obtaining the same information, without the risk that the process is killed; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt><code>PR_SET_SECUREBITS</code> (since Linux 2.6.26)</p>
<dd> Set the &quot;securebits&quot; flags of the calling thread to the value supplied in <i>arg2</i>. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7).</p>
<dt><code>PR_GET_SECUREBITS</code> (since Linux 2.6.26)</p>
<dd> Return (as the function result) the &quot;securebits&quot; flags of the calling thread. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7).</p>
<dt><code>PR_GET_SPECULATION_CTRL</code> (since Linux 4.17)</p>
<dd> Return (as the function result) the state of the speculation misfeature specified in <i>arg2</i>. Currently, the only permitted value for this argument is <code>PR_SPEC_STORE_BYPASS</code> (otherwise the call fails with the error <code>ENODEV</code>).</p>
<dt>
<dd> The return value uses bits 0-3 with the following meaning:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PR_SPEC_PRCTL</code></p>
<dd> Mitigation can be controlled per thread by <code>PR_SET_SPECULATION_CTRL</code>.</p>
<dt><code>PR_SPEC_ENABLE</code></p>
<dd> The speculation feature is enabled, mitigation is disabled.</p>
<dt><code>PR_SPEC_DISABLE</code></p>
<dd> The speculation feature is disabled, mitigation is enabled.</p>
<dt><code>PR_SPEC_FORCE_DISABLE</code></p>
<dd> Same as <code>PR_SPEC_DISABLE</code> but cannot be undone.</p>
<dt><code>PR_SPEC_DISABLE_NOEXEC</code> (since Linux 5.1)</p>
<dd> Same as <code>PR_SPEC_DISABLE</code>, but the state will be cleared on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</dl>
</dl>
<dt>
<dd> If all bits are 0, then the CPU is not affected by the speculation misfeature.</p>
<dt>
<dd> If <code>PR_SPEC_PRCTL</code> is set, then per-thread control of the mitigation is available. If not set, <code>prctl</code>() for the speculation misfeature will fail.</p>
<dt>
<dd> The <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> arguments must be specified as 0; otherwise the call fails with the error <code>EINVAL</code>.</p>
<dt><code>PR_SET_SPECULATION_CTRL</code> (since Linux 4.17)</p>
<dd> Sets the state of the speculation misfeature specified in <i>arg2</i>. The speculation-misfeature settings are per-thread attributes.</p>
<dt>
<dd> Currently, <i>arg2</i> must be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PR_SPEC_STORE_BYPASS</code></p>
<dd> Set the state of the speculative store bypass misfeature.</p>
<dt><code>PR_SPEC_INDIRECT_BRANCH</code> (since Linux 4.20)</p>
<dd> Set the state of the indirect branch speculation misfeature.</dl>
</dl>
<dt>
<dd> If <i>arg2</i> does not have one of the above values, then the call fails with the error <code>ENODEV</code>.</p>
<dt>
<dd> The <i>arg3</i> argument is used to hand in the control value, which is one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PR_SPEC_ENABLE</code></p>
<dd> The speculation feature is enabled, mitigation is disabled.</p>
<dt><code>PR_SPEC_DISABLE</code></p>
<dd> The speculation feature is disabled, mitigation is enabled.</p>
<dt><code>PR_SPEC_FORCE_DISABLE</code></p>
<dd> Same as <code>PR_SPEC_DISABLE</code>, but cannot be undone. A subsequent <code>prctl</code>(<i>arg2</i>, <code>PR_SPEC_ENABLE</code>) with the same value for <i>arg2</i> will fail with the error <code>EPERM</code>.</p>
<dt><code>PR_SPEC_DISABLE_NOEXEC</code> (since Linux 5.1)</p>
<dd> Same as <code>PR_SPEC_DISABLE</code>, but the state will be cleared on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). Currently only supported for <i>arg2</i> equal to <code>PR_SPEC_STORE_BYPASS.</code></dl>
</dl>
<dt>
<dd> Any unsupported value in <i>arg3</i> will result in the call failing with the error <code>ERANGE</code>.</p>
<dt>
<dd> The <i>arg4</i> and <i>arg5</i> arguments must be specified as 0; otherwise the call fails with the error <code>EINVAL</code>.</p>
<dt>
<dd> The speculation feature can also be controlled by the <code>spec_store_bypass_disable</code> boot parameter. This parameter may enforce a read-only policy which will result in the <code>prctl</code>() call failing with the error <code>ENXIO</code>. For further details, see the kernel source file <i>Documentation/admin-guide/kernel-parameters.txt</i>.</p>
<dt><code>PR_SVE_SET_VL</code> (since Linux 4.15, only on arm64)</p>
<dd> Configure the thread&#8217;s SVE vector length, as specified by <i>(int) arg2</i>. Arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt>
<dd> The bits of <i>arg2</i> corresponding to <code>PR_SVE_VL_LEN_MASK</code> must be set to the desired vector length in bytes. This is interpreted as an upper bound: the kernel will select the greatest available vector length that does not exceed the value specified. In particular, specifying <code>SVE_VL_MAX</code> (defined in <i>&lt;asm/sigcontext.h&gt;)</i> for the <code>PR_SVE_VL_LEN_MASK</code> bits requests the maximum supported vector length.</p>
<dt>
<dd> In addition, the other bits of <i>arg2</i> must be set to one of the following combinations of flags:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Perform the change immediately. At the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) in the thread, the vector length will be reset to the value configured in <i>/proc/sys/abi/sve_default_vector_length</i>.</p>
<dt><code>PR_SVE_VL_INHERIT</code></p>
<dd> Perform the change immediately. Subsequent <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) calls will preserve the new vector length.</p>
<dt><code>PR_SVE_SET_VL_ONEXEC</code></p>
<dd> Defer the change, so that it is performed at the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) in the thread. Further <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) calls will reset the vector length to the value configured in <i>/proc/sys/abi/sve_default_vector_length</i>.</p>
<dt><code>PR_SVE_SET_VL_ONEXEC | PR_SVE_VL_INHERIT</code></p>
<dd> Defer the change, so that it is performed at the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) in the thread. Further <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) calls will preserve the new vector length.</dl>
</dl>
<dt>
<dd> In all cases, any previously pending deferred change is canceled.</p>
<dt>
<dd> The call fails with error <code>EINVAL</code> if SVE is not supported on the platform, if <i>arg2</i> is unrecognized or invalid, or the value in the bits of <i>arg2</i> corresponding to <code>PR_SVE_VL_LEN_MASK</code> is outside the range <code>SVE_VL_MIN</code>..<code>SVE_VL_MAX</code> or is not a multiple of 16.</p>
<dt>
<dd> On success, a nonnegative value is returned that describes the <i>selected</i> configuration. If <code>PR_SVE_SET_VL_ONEXEC</code> was included in <i>arg2</i>, then the configuration described by the return value will take effect at the next <code>execve</code>(). Otherwise, the configuration is already in effect when the <code>PR_SVE_SET_VL</code> call returns. In either case, the value is encoded in the same way as the return value of <code>PR_SVE_GET_VL</code>. Note that there is no explicit flag in the return value corresponding to <code>PR_SVE_SET_VL_ONEXEC</code>.</p>
<dt>
<dd> The configuration (including any pending deferred change) is inherited across <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<dt>
<dd> For more information, see the kernel source file <i>Documentation/arm64/sve.rst</i> (or <i>Documentation/arm64/sve.txt</i> before Linux 5.3).</p>
<dt>
<dd> <code>Warning:</code> Because the compiler or run-time environment may be using SVE, using this call without the <code>PR_SVE_SET_VL_ONEXEC</code> flag may crash the calling process. The conditions for using it safely are complex and system-dependent. Don&#8217;t use it unless you really know what you are doing.</p>
<dt><code>PR_SVE_GET_VL</code> (since Linux 4.15, only on arm64)</p>
<dd> Get the thread&#8217;s current SVE vector length configuration.</p>
<dt>
<dd> Arguments <i>arg2</i>, <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt>
<dd> Provided that the kernel and platform support SVE, this operation always succeeds, returning a nonnegative value that describes the <i>current</i> configuration. The bits corresponding to <code>PR_SVE_VL_LEN_MASK</code> contain the currently configured vector length in bytes. The bit corresponding to <code>PR_SVE_VL_INHERIT</code> indicates whether the vector length will be inherited across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt>
<dd> Note that there is no way to determine whether there is a pending vector length change that has not yet taken effect.</p>
<dt>
<dd> For more information, see the kernel source file <i>Documentation/arm64/sve.rst</i> (or <i>Documentation/arm64/sve.txt</i> before Linux 5.3).</p>
<dt><code>PR_SET_TAGGED_ADDR_CTRL</code> (since Linux 5.4, only on arm64)</p>
<dd> Controls support for passing tagged user-space addresses to the kernel (i.e., addresses where bits 56&#8212;63 are not all zero).</p>
<dt>
<dd> The level of support is selected by <i>arg2</i>, which can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Addresses that are passed for the purpose of being dereferenced by the kernel must be untagged.</p>
<dt><code>PR_TAGGED_ADDR_ENABLE</code></p>
<dd> Addresses that are passed for the purpose of being dereferenced by the kernel may be tagged, with the exceptions summarized below.</dl>
</dl>
<dt>
<dd> The remaining arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> must all be zero.</p>
<dt>
<dd> On success, the mode specified in <i>arg2</i> is set for the calling thread and the return value is 0. If the arguments are invalid, the mode specified in <i>arg2</i> is unrecognized, or if this feature is unsupported by the kernel or disabled via <i>/proc/sys/abi/tagged_addr_disabled</i>, the call fails with the error <code>EINVAL</code>.</p>
<dt>
<dd> In particular, if <code>prctl</code>(<code>PR_SET_TAGGED_ADDR_CTRL</code>, 0, 0, 0, 0) fails with <code>EINVAL</code>, then all addresses passed to the kernel must be untagged.</p>
<dt>
<dd> Irrespective of which mode is set, addresses passed to certain interfaces must always be untagged:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2), and the <i>new_address</i> argument of <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2).</p>
<dt>
<dd> (Prior to Linux 5.6 these accepted tagged addresses, but the behaviour may not be what you expect. Don&#8217;t rely on it.)</p>
<dt>&bull;</p>
<dd> &#8216;polymorphic&#8217; interfaces that accept pointers to arbitrary types cast to a <i>void *</i> or other generic type, specifically <code>prctl</code>(), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), and in general <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) (only certain specific <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) options allow tagged addresses).</dl>
</dl>
<dt>
<dd> This list of exclusions may shrink when moving from one kernel version to a later kernel version. While the kernel may make some guarantees for backwards compatibility reasons, for the purposes of new software the effect of passing tagged addresses to these interfaces is unspecified.</p>
<dt>
<dd> The mode set by this call is inherited across <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2). The mode is reset by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) to 0 (i.e., tagged addresses not permitted in the user/kernel ABI).</p>
<dt>
<dd> For more information, see the kernel source file <i>Documentation/arm64/tagged-address-abi.rst</i>.</p>
<dt>
<dd> <code>Warning:</code> This call is primarily intended for use by the run-time environment. A successful <code>PR_SET_TAGGED_ADDR_CTRL</code> call elsewhere may crash the calling process. The conditions for using it safely are complex and system-dependent. Don&#8217;t use it unless you know what you are doing.</p>
<dt><code>PR_GET_TAGGED_ADDR_CTRL</code> (since Linux 5.4, only on arm64)</p>
<dd> Returns the current tagged address mode for the calling thread.</p>
<dt>
<dd> Arguments <i>arg2</i>, <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> must all be zero.</p>
<dt>
<dd> If the arguments are invalid or this feature is disabled or unsupported by the kernel, the call fails with <code>EINVAL</code>. In particular, if <code>prctl</code>(<code>PR_GET_TAGGED_ADDR_CTRL</code>, 0, 0, 0, 0) fails with <code>EINVAL</code>, then this feature is definitely either unsupported, or disabled via <i>/proc/sys/abi/tagged_addr_disabled</i>. In this case, all addresses passed to the kernel must be untagged.</p>
<dt>
<dd> Otherwise, the call returns a nonnegative value describing the current tagged address mode, encoded in the same way as the <i>arg2</i> argument of <code>PR_SET_TAGGED_ADDR_CTRL</code>.</p>
<dt>
<dd> For more information, see the kernel source file <i>Documentation/arm64/tagged-address-abi.rst</i>.</p>
<dt><code>PR_TASK_PERF_EVENTS_DISABLE</code> (since Linux 2.6.31)</p>
<dd> Disable all performance counters attached to the calling process, regardless of whether the counters were created by this process or another process. Performance counters created by the calling process for other processes are unaffected. For more information on performance counters, see the Linux kernel source file <i>tools/perf/design.txt</i>.</p>
<dt>
<dd> Originally called <code>PR_TASK_PERF_COUNTERS_DISABLE</code>; renamed (retaining the same numerical value) in Linux 2.6.32.</p>
<dt><code>PR_TASK_PERF_EVENTS_ENABLE</code> (since Linux 2.6.31)</p>
<dd> The converse of <code>PR_TASK_PERF_EVENTS_DISABLE</code>; enable performance counters attached to the calling process.</p>
<dt>
<dd> Originally called <code>PR_TASK_PERF_COUNTERS_ENABLE</code>; renamed in Linux 2.6.32.</p>
<dt><code>PR_SET_THP_DISABLE</code> (since Linux 3.15)</p>
<dd> Set the state of the &quot;THP disable&quot; flag for the calling thread. If <i>arg2</i> has a nonzero value, the flag is set, otherwise it is cleared. Setting this flag provides a method for disabling transparent huge pages for jobs where the code cannot be modified, and using a malloc hook with <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) is not an option (i.e., statically allocated data). The setting of the &quot;THP disable&quot; flag is inherited by a child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>PR_GET_THP_DISABLE</code> (since Linux 3.15)</p>
<dd> Return (as the function result) the current setting of the &quot;THP disable&quot; flag for the calling thread: either 1, if the flag is set, or 0, if it is not.</p>
<dt><code>PR_GET_TID_ADDRESS</code> (since Linux 3.5)</p>
<dd> Return the <i>clear_child_tid</i> address set by <code><a href="/docs/linux/man/2-set_tid_address/">set_tid_address</a></code>(2) and the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_CHILD_CLEARTID</code> flag, in the location pointed to by <i>(int&nbsp;**)&nbsp;arg2</i>. This feature is available only if the kernel is built with the <code>CONFIG_CHECKPOINT_RESTORE</code> option enabled. Note that since the <code>prctl</code>() system call does not have a compat implementation for the AMD64 x32 and MIPS n32 ABIs, and the kernel writes out a pointer using the kernel&#8217;s pointer size, this operation expects a user-space buffer of 8 (not 4) bytes on these ABIs.</p>
<dt><code>PR_SET_TIMERSLACK</code> (since Linux 2.6.28)</p>
<dd> Each thread has two associated timer slack values: a &quot;default&quot; value, and a &quot;current&quot; value. This operation sets the &quot;current&quot; timer slack value for the calling thread. <i>arg2</i> is an unsigned long value, then maximum &quot;current&quot; value is ULONG_MAX and the minimum &quot;current&quot; value is 1. If the nanosecond value supplied in <i>arg2</i> is greater than zero, then the &quot;current&quot; value is set to this value. If <i>arg2</i> is equal to zero, the &quot;current&quot; timer slack is reset to the thread&#8217;s &quot;default&quot; timer slack value.</p>
<dt>
<dd> The &quot;current&quot; timer slack is used by the kernel to group timer expirations for the calling thread that are close to one another; as a consequence, timer expirations for the thread may be up to the specified number of nanoseconds late (but will never expire early). Grouping timer expirations can help reduce system power consumption by minimizing CPU wake-ups.</p>
<dt>
<dd> The timer expirations affected by timer slack are those set by <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2), <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), <code><a href="/docs/linux/man/2-epoll_pwait/">epoll_pwait</a></code>(2), <code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), and <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) (and thus the library functions implemented via futexes, including <code><a href="/docs/linux/man/3-pthread_cond_timedwait/">pthread_cond_timedwait</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutex_timedlock/">pthread_mutex_timedlock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_rwlock_timedrdlock/">pthread_rwlock_timedrdlock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_rwlock_timedwrlock/">pthread_rwlock_timedwrlock</a></code>(3), and <code><a href="/docs/linux/man/3-sem_timedwait/">sem_timedwait</a></code>(3)).</p>
<dt>
<dd> Timer slack is not applied to threads that are scheduled under a real-time scheduling policy (see <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2)).</p>
<dt>
<dd> When a new thread is created, the two timer slack values are made the same as the &quot;current&quot; value of the creating thread. Thereafter, a thread can adjust its &quot;current&quot; timer slack value via <code>PR_SET_TIMERSLACK</code>. The &quot;default&quot; value can&#8217;t be changed. The timer slack values of <i>init</i> (PID 1), the ancestor of all processes, are 50,000 nanoseconds (50 microseconds). The timer slack value is inherited by a child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), and is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt>
<dd> Since Linux 4.6, the &quot;current&quot; timer slack value of any process can be examined and changed via the file <i>/proc/[pid]/timerslack_ns</i>. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt><code>PR_GET_TIMERSLACK</code> (since Linux 2.6.28)</p>
<dd> Return (as the function result) the &quot;current&quot; timer slack value of the calling thread.</p>
<dt><code>PR_SET_TIMING</code> (since Linux 2.6.0)</p>
<dd> Set whether to use (normal, traditional) statistical process timing or accurate timestamp-based process timing, by passing <code>PR_TIMING_STATISTICAL</code> or <code>PR_TIMING_TIMESTAMP</code> to <i>arg2</i>. <code>PR_TIMING_TIMESTAMP</code> is not currently implemented (attempting to set this mode will yield the error <code>EINVAL</code>).</p>
<dt><code>PR_GET_TIMING</code> (since Linux 2.6.0)</p>
<dd> Return (as the function result) which process timing method is currently in use.</p>
<dt><code>PR_SET_TSC</code> (since Linux 2.6.26, x86 only)</p>
<dd> Set the state of the flag determining whether the timestamp counter can be read by the process. Pass <code>PR_TSC_ENABLE</code> to <i>arg2</i> to allow it to be read, or <code>PR_TSC_SIGSEGV</code> to generate a <code>SIGSEGV</code> when the process tries to read the timestamp counter.</p>
<dt><code>PR_GET_TSC</code> (since Linux 2.6.26, x86 only)</p>
<dd> Return the state of the flag determining whether the timestamp counter can be read, in the location pointed to by <i>(int&nbsp;*) arg2</i>.</p>
<dt><code>PR_SET_UNALIGN</code></p>
<dd> (Only on: ia64, since Linux 2.3.48; parisc, since Linux 2.6.15; PowerPC, since Linux 2.6.18; Alpha, since Linux 2.6.22; sh, since Linux 2.6.34; tile, since Linux 3.12) Set unaligned access control bits to <i>arg2</i>. Pass <code>PR_UNALIGN_NOPRINT</code> to silently fix up unaligned user accesses, or <code>PR_UNALIGN_SIGBUS</code> to generate <code>SIGBUS</code> on unaligned user access. Alpha also supports an additional flag with the value of 4 and no corresponding named constant, which instructs kernel to not fix up unaligned accesses (it is analogous to providing the <code>UAC_NOFIX</code> flag in <code>SSI_NVPAIRS</code> operation of the <code>setsysinfo</code>() system call on Tru64).</p>
<dt><code>PR_GET_UNALIGN</code></p>
<dd> (See <code>PR_SET_UNALIGN</code> for information on versions and architectures.) Return unaligned access control bits, in the location pointed to by <i>(unsigned int&nbsp;*) arg2</i>.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>PR_CAP_AMBIENT</code>+<code>PR_CAP_AMBIENT_IS_SET</code>, <code>PR_CAPBSET_READ</code>, <code>PR_GET_DUMPABLE</code>, <code>PR_GET_FP_MODE</code>, <code>PR_GET_IO_FLUSHER</code>, <code>PR_GET_KEEPCAPS</code>, <code>PR_MCE_KILL_GET</code>, <code>PR_GET_NO_NEW_PRIVS</code>, <code>PR_GET_SECUREBITS</code>, <code>PR_GET_SPECULATION_CTRL</code>, <code>PR_SVE_GET_VL</code>, <code>PR_SVE_SET_VL</code>, <code>PR_GET_TAGGED_ADDR_CTRL</code>, <code>PR_GET_THP_DISABLE</code>, <code>PR_GET_TIMING</code>, <code>PR_GET_TIMERSLACK</code>, and (if it returns) <code>PR_GET_SECCOMP</code> return the nonnegative values described above. All other <i>option</i> values return 0 on success. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> <i>option</i> is <code>PR_SET_SECCOMP</code> and <i>arg2</i> is <code>SECCOMP_MODE_FILTER</code>, but the process does not have the <code>CAP_SYS_ADMIN</code> capability or has not set the <i>no_new_privs</i> attribute (see the discussion of <code>PR_SET_NO_NEW_PRIVS</code> above).</p>
<dt><code>EACCES</code></p>
<dd> <i>option</i> is <code>PR_SET_MM</code>, and <i>arg3</i> is <code>PR_SET_MM_EXE_FILE</code>, the file is not executable.</p>
<dt><code>EBADF</code></p>
<dd> <i>option</i> is <code>PR_SET_MM</code>, <i>arg3</i> is <code>PR_SET_MM_EXE_FILE</code>, and the file descriptor passed in <i>arg4</i> is not valid.</p>
<dt><code>EBUSY</code></p>
<dd> <i>option</i> is <code>PR_SET_MM</code>, <i>arg3</i> is <code>PR_SET_MM_EXE_FILE</code>, and this the second attempt to change the <i>/proc/pid/exe</i> symbolic link, which is prohibited.</p>
<dt><code>EFAULT</code></p>
<dd> <i>arg2</i> is an invalid address.</p>
<dt><code>EFAULT</code></p>
<dd> <i>option</i> is <code>PR_SET_SECCOMP</code>, <i>arg2</i> is <code>SECCOMP_MODE_FILTER</code>, the system was built with <code>CONFIG_SECCOMP_FILTER</code>, and <i>arg3</i> is an invalid address.</p>
<dt><code>EINVAL</code></p>
<dd> The value of <i>option</i> is not recognized, or not supported on this system.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_MCE_KILL</code> or <code>PR_MCE_KILL_GET</code> or <code>PR_SET_MM</code>, and unused <code>prctl</code>() arguments were not specified as zero.</p>
<dt><code>EINVAL</code></p>
<dd> <i>arg2</i> is not valid value for this <i>option</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_SECCOMP</code> or <code>PR_GET_SECCOMP</code>, and the kernel was not configured with <code>CONFIG_SECCOMP</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_SECCOMP</code>, <i>arg2</i> is <code>SECCOMP_MODE_FILTER</code>, and the kernel was not configured with <code>CONFIG_SECCOMP_FILTER</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_MM</code>, and one of the following is true</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <i>arg4</i> or <i>arg5</i> is nonzero;</p>
<dt>*</p>
<dd> <i>arg3</i> is greater than <code>TASK_SIZE</code> (the limit on the size of the user address space for this architecture);</p>
<dt>*</p>
<dd> <i>arg2</i> is <code>PR_SET_MM_START_CODE</code>, <code>PR_SET_MM_END_CODE</code>, <code>PR_SET_MM_START_DATA</code>, <code>PR_SET_MM_END_DATA</code>, or <code>PR_SET_MM_START_STACK</code>, and the permissions of the corresponding memory area are not as required;</p>
<dt>*</p>
<dd> <i>arg2</i> is <code>PR_SET_MM_START_BRK</code> or <code>PR_SET_MM_BRK</code>, and <i>arg3</i> is less than or equal to the end of the data segment or specifies a value that would cause the <code>RLIMIT_DATA</code> resource limit to be exceeded.</dl>
</dl>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_PTRACER</code> and <i>arg2</i> is not 0, <code>PR_SET_PTRACER_ANY</code>, or the PID of an existing process.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_PDEATHSIG</code> and <i>arg2</i> is not a valid signal number.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_DUMPABLE</code> and <i>arg2</i> is neither <code>SUID_DUMP_DISABLE</code> nor <code>SUID_DUMP_USER</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_TIMING</code> and <i>arg2</i> is not <code>PR_TIMING_STATISTICAL</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_NO_NEW_PRIVS</code> and <i>arg2</i> is not equal to 1 or <i>arg3</i>, <i>arg4</i>, or <i>arg5</i> is nonzero.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_GET_NO_NEW_PRIVS</code> and <i>arg2</i>, <i>arg3</i>, <i>arg4</i>, or <i>arg5</i> is nonzero.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_THP_DISABLE</code> and <i>arg3</i>, <i>arg4</i>, or <i>arg5</i> is nonzero.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_GET_THP_DISABLE</code> and <i>arg2</i>, <i>arg3</i>, <i>arg4</i>, or <i>arg5</i> is nonzero.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_CAP_AMBIENT</code> and an unused argument (<i>arg4</i>, <i>arg5</i>, or, in the case of <code>PR_CAP_AMBIENT_CLEAR_ALL</code>, <i>arg3</i>) is nonzero; or <i>arg2</i> has an invalid value; or <i>arg2</i> is <code>PR_CAP_AMBIENT_LOWER</code>, <code>PR_CAP_AMBIENT_RAISE</code>, or <code>PR_CAP_AMBIENT_IS_SET</code> and <i>arg3</i> does not specify a valid capability.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> was <code>PR_GET_SPECULATION_CTRL</code> or <code>PR_SET_SPECULATION_CTRL</code> and unused arguments to <code>prctl</code>() are not 0. <code>EINVAL</code> <i>option</i> is <code>PR_PAC_RESET_KEYS</code> and the arguments are invalid or unsupported. See the description of <code>PR_PAC_RESET_KEYS</code> above for details.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SVE_SET_VL</code> and the arguments are invalid or unsupported, or SVE is not available on this platform. See the description of <code>PR_SVE_SET_VL</code> above for details.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SVE_GET_VL</code> and SVE is not available on this platform.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_SET_TAGGED_ADDR_CTRL</code> and the arguments are invalid or unsupported. See the description of <code>PR_SET_TAGGED_ADDR_CTRL</code> above for details.</p>
<dt><code>EINVAL</code></p>
<dd> <i>option</i> is <code>PR_GET_TAGGED_ADDR_CTRL</code> and the arguments are invalid or unsupported. See the description of <code>PR_GET_TAGGED_ADDR_CTRL</code> above for details.</p>
<dt><code>ENODEV</code></p>
<dd> <i>option</i> was <code>PR_SET_SPECULATION_CTRL</code> the kernel or CPU does not support the requested speculation misfeature.</p>
<dt><code>ENXIO</code></p>
<dd> <i>option</i> was <code>PR_MPX_ENABLE_MANAGEMENT</code> or <code>PR_MPX_DISABLE_MANAGEMENT</code> and the kernel or the CPU does not support MPX management. Check that the kernel and processor have MPX support.</p>
<dt><code>ENXIO</code></p>
<dd> <i>option</i> was <code>PR_SET_SPECULATION_CTRL</code> implies that the control of the selected speculation misfeature is not possible. See <code>PR_GET_SPECULATION_CTRL</code> for the bit fields to determine which option is available.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> <i>option</i> is <code>PR_SET_FP_MODE</code> and <i>arg2</i> has an invalid or unsupported value.</p>
<dt><code>EPERM</code></p>
<dd> <i>option</i> is <code>PR_SET_SECUREBITS</code>, and the caller does not have the <code>CAP_SETPCAP</code> capability, or tried to unset a &quot;locked&quot; flag, or tried to set a flag whose corresponding locked flag was set (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)).</p>
<dt><code>EPERM</code></p>
<dd> <i>option</i> is <code>PR_SET_SPECULATION_CTRL</code> wherein the speculation was disabled with <code>PR_SPEC_FORCE_DISABLE</code> and caller tried to enable it again.</p>
<dt><code>EPERM</code></p>
<dd> <i>option</i> is <code>PR_SET_KEEPCAPS</code>, and the caller&#8217;s <code>SECBIT_KEEP_CAPS_LOCKED</code> flag is set (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)).</p>
<dt><code>EPERM</code></p>
<dd> <i>option</i> is <code>PR_CAPBSET_DROP</code>, and the caller does not have the <code>CAP_SETPCAP</code> capability.</p>
<dt><code>EPERM</code></p>
<dd> <i>option</i> is <code>PR_SET_MM</code>, and the caller does not have the <code>CAP_SYS_RESOURCE</code> capability.</p>
<dt><code>EPERM</code></p>
<dd> <i>option</i> is <code>PR_CAP_AMBIENT</code> and <i>arg2</i> is <code>PR_CAP_AMBIENT_RAISE</code>, but either the capability specified in <i>arg3</i> is not present in the process&#8217;s permitted and inheritable capability sets, or the <code>PR_CAP_AMBIENT_LOWER</code> securebit has been set.</p>
<dt><code>ERANGE</code></p>
<dd> <i>option</i> was <code>PR_SET_SPECULATION_CTRL</code> and <i>arg3</i> is not <code>PR_SPEC_ENABLE</code>, <code>PR_SPEC_DISABLE</code>, <code>PR_SPEC_FORCE_DISABLE</code>, nor <code>PR_SPEC_DISABLE_NOEXEC</code>.</dl>
<h2>VERSIONS</h2>
<p> The <code>prctl</code>() system call was introduced in Linux 2.1.57.</p>
<h2>CONFORMING TO</h2>
<p> This call is Linux-specific. IRIX has a <code>prctl</code>() system call (also introduced in Linux 2.1.44 as irix_prctl on the MIPS architecture), with prototype </p>
<p> <code>ptrdiff_t prctl(int </code><i>option</i><code>, int </code><i>arg2</i><code>, int </code><i>arg3</i><code>);</code> </p>
<p> and options to get the maximum number of processes per user, get the maximum number of processors the calling process can use, find out whether a specified process is currently blocked, get or set the maximum stack size, and so on.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/5-core/">core</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
