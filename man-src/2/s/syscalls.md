---
title: "syscalls(2)"
name: "syscalls"
section: "2"
letter: "s"
url: "/docs/linux/man/2-syscalls/"
description: "syscalls – Linux system calls"
---

<h2 class="name">NAME</h2>
<p> syscalls &#8211; Linux system calls </p>
<h2>SYNOPSIS</h2>
<p> Linux system calls.</p>
<h2>DESCRIPTION</h2>
<p> The system call is the fundamental interface between an application and the Linux kernel.</p>
<h3>System calls and library wrapper functions</h3>
<p> System calls are generally not invoked directly, but rather via wrapper functions in glibc (or perhaps some other library). For details of direct invocation of a system call, see <code><a href="/docs/linux/man/2-intro/">intro</a></code>(2). Often, but not always, the name of the wrapper function is the same as the name of the system call that it invokes. For example, glibc contains a function <code>chdir</code>() which invokes the underlying &quot;chdir&quot; system call. </p>
<p> Often the glibc wrapper function is quite thin, doing little work other than copying arguments to the right registers before invoking the system call, and then setting <i>errno</i> appropriately after the system call has returned. (These are the same steps that are performed by <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), which can be used to invoke system calls for which no wrapper function is provided.) Note: system calls indicate a failure by returning a negative error number to the caller on architectures without a separate error register/flag, as noted in <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2); when this happens, the wrapper function negates the returned error number (to make it positive), copies it to <i>errno</i>, and returns -1 to the caller of the wrapper. </p>
<p> Sometimes, however, the wrapper function does some extra work before invoking the system call. For example, nowadays there are (for reasons described below) two related system calls, <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2) and <code><a href="/docs/linux/man/2-truncate64/">truncate64</a></code>(2), and the glibc <code>truncate</code>() wrapper function checks which of those system calls are provided by the kernel and determines which should be employed.</p>
<h3>System call list</h3>
<p> Below is a list of the Linux system calls. In the list, the <i>Kernel</i> column indicates the kernel version for those system calls that were new in Linux 2.2, or have appeared since that kernel version. Note the following points:</p>
<dl>
<dt>*</p>
<dd> Where no kernel version is indicated, the system call appeared in kernel 1.0 or earlier.</p>
<dt>*</p>
<dd> Where a system call is marked &quot;1.2&quot; this means the system call probably appeared in a 1.1.x kernel version, and first appeared in a stable kernel with 1.2. (Development of the 1.2 kernel was initiated from a branch of kernel 1.0.6 via the 1.1.x unstable kernel series.)</p>
<dt>*</p>
<dd> Where a system call is marked &quot;2.0&quot; this means the system call probably appeared in a 1.3.x kernel version, and first appeared in a stable kernel with 2.0. (Development of the 2.0 kernel was initiated from a branch of kernel 1.2.x, somewhere around 1.2.10, via the 1.3.x unstable kernel series.)</p>
<dt>*</p>
<dd> Where a system call is marked &quot;2.2&quot; this means the system call probably appeared in a 2.1.x kernel version, and first appeared in a stable kernel with 2.2.0. (Development of the 2.2 kernel was initiated from a branch of kernel 2.0.21 via the 2.1.x unstable kernel series.)</p>
<dt>*</p>
<dd> Where a system call is marked &quot;2.4&quot; this means the system call probably appeared in a 2.3.x kernel version, and first appeared in a stable kernel with 2.4.0. (Development of the 2.4 kernel was initiated from a branch of kernel 2.2.8 via the 2.3.x unstable kernel series.)</p>
<dt>*</p>
<dd> Where a system call is marked &quot;2.6&quot; this means the system call probably appeared in a 2.5.x kernel version, and first appeared in a stable kernel with 2.6.0. (Development of kernel 2.6 was initiated from a branch of kernel 2.4.15 via the 2.5.x unstable kernel series.)</p>
<dt>*</p>
<dd> Starting with kernel 2.6.0, the development model changed, and new system calls may appear in each 2.6.x release. In this case, the exact version number where the system call appeared is shown. This convention continues with the 3.x kernel series, which followed on from kernel 2.6.39; and the 4.x kernel series, which followed on from kernel 3.19; and the 5.x kernel series, which followed on from kernel 4.20.</p>
<dt>*</p>
<dd> In some cases, a system call was added to a stable kernel series after it branched from the previous stable kernel series, and then backported into the earlier stable kernel series. For example some system calls that appeared in 2.6.x were also backported into a 2.4.x release after 2.4.15. When this is so, the version where the system call appeared in both of the major kernel series is listed.</dl>
<p> The list of system calls that are available as at kernel 5.10 (or in a few cases only on older kernels) is as follows: </p>
<table>
<tr VALIGN=top>
<td><code>System call</code>&nbsp;<wbr>&nbsp;</td>
<td><code>Kernel</code></td>
<td><code>Notes</code>
</td>
</tr>
<tr VALIGN=top>
<td></td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-_llseek/">_llseek</a></code>(2)</td>
<td>1.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-_newselect/">_newselect</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-_sysctl/">_sysctl</a></code>(2)</td>
<td>2.0</td>
<td>Removed in 5.5
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-accept/">accept</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-accept4/">accept4</a></code>(2)</td>
<td>2.6.28</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-access/">access</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-acct/">acct</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2)</td>
<td>2.6.10</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-alloc_hugepages/">alloc_hugepages</a></code>(2)</td>
<td>2.5.36</td>
<td>Removed in 2.5.44
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-arc_gettls/">arc_gettls</a></code>(2)</td>
<td>3.9</td>
<td>ARC only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-arc_settls/">arc_settls</a></code>(2)</td>
<td>3.9</td>
<td>ARC only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-arc_usr_cmpxchg/">arc_usr_cmpxchg</a></code>(2)</td>
<td>4.9</td>
<td>ARC only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-arch_prctl/">arch_prctl</a></code>(2)</td>
<td>2.6</td>
<td>x86_64, x86 since 4.12
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-atomic_barrier/">atomic_barrier</a></code>(2)</td>
<td>2.6.34</td>
<td>m68k only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-atomic_cmpxchg_32/">atomic_cmpxchg_32</a></code>(2)</td>
<td>2.6.34</td>
<td>m68k only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-bdflush/">bdflush</a></code>(2)</td>
<td>1.2</td>
<td> Deprecated (does nothing)<br />
 since 2.6
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-bind/">bind</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2)</td>
<td>3.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-brk/">brk</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-breakpoint/">breakpoint</a></code>(2)</td>
<td>2.2</td>
<td> ARM OABI only, defined with<br />
 <code>__ARM_NR</code> prefix
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-cacheflush/">cacheflush</a></code>(2)</td>
<td>1.2</td>
<td>Not on x86
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-capget/">capget</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-capset/">capset</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-chown/">chown</a></code>(2)</td>
<td>2.2</td>
<td> See <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2) for<br />
 version details
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-chown32/">chown32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-clock_adjtime/">clock_adjtime</a></code>(2)</td>
<td>2.6.39</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-clone2/">clone2</a></code>(2)</td>
<td>2.4</td>
<td>IA-64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-clone3/">clone3</a></code>(2)</td>
<td>5.3</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-close/">close</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-close_range/">close_range</a></code>(2)</td>
<td>5.9</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-connect/">connect</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-copy_file_range/">copy_file_range</a></code>(2)</td>
<td>4.5</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-creat/">creat</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-create_module/">create_module</a></code>(2)</td>
<td>1.0</td>
<td>Removed in 2.6
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-delete_module/">delete_module</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-dup/">dup</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-dup2/">dup2</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-dup3/">dup3</a></code>(2)</td>
<td>2.6.27</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-epoll_create/">epoll_create</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-epoll_create1/">epoll_create1</a></code>(2)</td>
<td>2.6.27</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-epoll_pwait/">epoll_pwait</a></code>(2)</td>
<td>2.6.19</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-eventfd/">eventfd</a></code>(2)</td>
<td>2.6.22</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-eventfd2/">eventfd2</a></code>(2)</td>
<td>2.6.27</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-execv/">execv</a></code>(2)</td>
<td>2.0</td>
<td> SPARC/SPARC64 only, for<br />
 compatibility with SunOS
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-execveat/">execveat</a></code>(2)</td>
<td>3.19</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-exit/">exit</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-faccessat/">faccessat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-faccessat2/">faccessat2</a></code>(2)</td>
<td>5.8</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fadvise64/">fadvise64</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fadvise64_64/">fadvise64_64</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2)</td>
<td>2.6.23</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2)</td>
<td>2.6.37</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2)</td>
<td>2.6.37</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchmodat/">fchmodat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchown32/">fchown32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchownat/">fchownat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fcntl64/">fcntl64</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fgetxattr/">fgetxattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-finit_module/">finit_module</a></code>(2)</td>
<td>3.8</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-flistxattr/">flistxattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-flock/">flock</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-free_hugepages/">free_hugepages</a></code>(2)</td>
<td>2.5.36</td>
<td>Removed in 2.5.44
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fremovexattr/">fremovexattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fsconfig/">fsconfig</a></code>(2)</td>
<td>5.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fsetxattr/">fsetxattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fsmount/">fsmount</a></code>(2)</td>
<td>5.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fsopen/">fsopen</a></code>(2)</td>
<td>5.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fspick/">fspick</a></code>(2)</td>
<td>5.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fstat64/">fstat64</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fstatat64/">fstatat64</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fstatfs/">fstatfs</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fstatfs64/">fstatfs64</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ftruncate64/">ftruncate64</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-futex/">futex</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-futimesat/">futimesat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-get_kernel_syms/">get_kernel_syms</a></code>(2)</td>
<td>1.0</td>
<td>Removed in 2.6
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a></code>(2)</td>
<td>2.6.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2)</td>
<td>2.6.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-get_thread_area/">get_thread_area</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-get_tls/">get_tls</a></code>(2)</td>
<td>4.15</td>
<td> ARM OABI only, has<br />
 <code>__ARM_NR</code> prefix
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getcpu/">getcpu</a></code>(2)</td>
<td>2.6.19</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getcwd/">getcwd</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getdents/">getdents</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getdents64/">getdents64</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getdomainname/">getdomainname</a></code>(2)</td>
<td>2.2</td>
<td> SPARC, SPARC64; available<br />
 as <code><a href="/docs/linux/man/2-osf_getdomainname/">osf_getdomainname</a></code>(2)<br />
 on Alpha since Linux 2.0
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getdtablesize/">getdtablesize</a></code>(2)</td>
<td>2.0</td>
<td> SPARC (removed in 2.6.26),<br />
 available on Alpha as<br />
 <code><a href="/docs/linux/man/2-osf_getdtablesize/">osf_getdtablesize</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getegid/">getegid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getegid32/">getegid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-geteuid32/">geteuid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getgid32/">getgid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getgroups/">getgroups</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getgroups32/">getgroups32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2)</td>
<td>2.0</td>
<td> Alpha, was available on<br />
 SPARC up to Linux 2.6.26
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getitimer/">getitimer</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getpagesize/">getpagesize</a></code>(2)</td>
<td>2.0</td>
<td>Not on x86
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getpgid/">getpgid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getpgrp/">getpgrp</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2)</td>
<td>3.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getresgid/">getresgid</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getresgid32/">getresgid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getresuid/">getresuid</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getresuid32/">getresuid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getsid/">getsid</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2)</td>
<td>2.4.11</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getuid32/">getuid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getunwind/">getunwind</a></code>(2)</td>
<td>2.4.8</td>
<td>IA-64 only; deprecated
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getxattr/">getxattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getxgid/">getxgid</a></code>(2)</td>
<td>2.0</td>
<td>Alpha only; see NOTES
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getxpid/">getxpid</a></code>(2)</td>
<td>2.0</td>
<td>Alpha only; see NOTES
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getxuid/">getxuid</a></code>(2)</td>
<td>2.0</td>
<td>Alpha only; see NOTES
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-init_module/">init_module</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2)</td>
<td>2.6.13</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2)</td>
<td>2.6.13</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-inotify_init1/">inotify_init1</a></code>(2)</td>
<td>2.6.27</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-inotify_rm_watch/">inotify_rm_watch</a></code>(2)</td>
<td>2.6.13</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-io_cancel/">io_cancel</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-io_destroy/">io_destroy</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-io_pgetevents/">io_pgetevents</a></code>(2)</td>
<td>4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-io_uring_enter/">io_uring_enter</a></code>(2)</td>
<td>5.1</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-io_uring_register/">io_uring_register</a></code>(2)</td>
<td>5.1</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-io_uring_setup/">io_uring_setup</a></code>(2)</td>
<td>5.1</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-iopl/">iopl</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ioprio_get/">ioprio_get</a></code>(2)</td>
<td>2.6.13</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ioprio_set/">ioprio_set</a></code>(2)</td>
<td>2.6.13</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2)</td>
<td>3.5</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-kern_features/">kern_features</a></code>(2)</td>
<td>3.7</td>
<td>SPARC64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-kexec_file_load/">kexec_file_load</a></code>(2)</td>
<td>3.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-kexec_load/">kexec_load</a></code>(2)</td>
<td>2.6.13</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2)</td>
<td>2.6.10</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-kill/">kill</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lchown/">lchown</a></code>(2)</td>
<td>1.0</td>
<td> See <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2) for<br />
 version details
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lchown32/">lchown32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lgetxattr/">lgetxattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-link/">link</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-linkat/">linkat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-listen/">listen</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-listxattr/">listxattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-llistxattr/">llistxattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lookup_dcookie/">lookup_dcookie</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lremovexattr/">lremovexattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lsetxattr/">lsetxattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lstat64/">lstat64</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2)</td>
<td>2.6.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-memory_ordering/">memory_ordering</a></code>(2)</td>
<td>2.2</td>
<td>SPARC64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-membarrier/">membarrier</a></code>(2)</td>
<td>3.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-memfd_create/">memfd_create</a></code>(2)</td>
<td>3.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-migrate_pages/">migrate_pages</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mincore/">mincore</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mkdirat/">mkdirat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mknodat/">mknodat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mlock2/">mlock2</a></code>(2)</td>
<td>4.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mmap2/">mmap2</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-modify_ldt/">modify_ldt</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mount/">mount</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-move_mount/">move_mount</a></code>(2)</td>
<td>5.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-move_pages/">move_pages</a></code>(2)</td>
<td>2.6.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mq_getsetattr/">mq_getsetattr</a></code>(2)</td>
<td>2.6.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mq_notify/">mq_notify</a></code>(2)</td>
<td>2.6.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mq_open/">mq_open</a></code>(2)</td>
<td>2.6.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mq_timedreceive/">mq_timedreceive</a></code>(2)</td>
<td>2.6.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mq_timedsend/">mq_timedsend</a></code>(2)</td>
<td>2.6.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mq_unlink/">mq_unlink</a></code>(2)</td>
<td>2.6.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-msync/">msync</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-munlock/">munlock</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-munlockall/">munlockall</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-name_to_handle_at/">name_to_handle_at</a></code>(2)</td>
<td>2.6.39</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-newfstatat/">newfstatat</a></code>(2)</td>
<td>2.6.16</td>
<td>See <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-nfsservctl/">nfsservctl</a></code>(2)</td>
<td>2.2</td>
<td>Removed in 3.1
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-nice/">nice</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-old_adjtimex/">old_adjtimex</a></code>(2)</td>
<td>2.0</td>
<td>Alpha only; see NOTES
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-old_getrlimit/">old_getrlimit</a></code>(2)</td>
<td>2.4</td>
<td> Old variant of <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)<br />
 that used a different value<br />
 for <code>RLIM_INFINITY</code>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-oldfstat/">oldfstat</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-oldlstat/">oldlstat</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-oldolduname/">oldolduname</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-oldstat/">oldstat</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-oldumount/">oldumount</a></code>(2)</td>
<td>2.4.116</td>
<td> Name of the old <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2)<br />
 syscall on Alpha
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-olduname/">olduname</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-open/">open</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-open_by_handle_at/">open_by_handle_at</a></code>(2)</td>
<td>2.6.39</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-open_tree/">open_tree</a></code>(2)</td>
<td>5.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-openat/">openat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-openat2/">openat2</a></code>(2)</td>
<td>5.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-or1k_atomic/">or1k_atomic</a></code>(2)</td>
<td>3.1</td>
<td>OpenRISC 1000 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pause/">pause</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pciconfig_iobase/">pciconfig_iobase</a></code>(2)</td>
<td>2.2.15; 2.4</td>
<td>Not on x86
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pciconfig_read/">pciconfig_read</a></code>(2)</td>
<td>2.0.26; 2.2</td>
<td>Not on x86
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pciconfig_write/">pciconfig_write</a></code>(2)</td>
<td>2.0.26; 2.2</td>
<td>Not on x86
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-perf_event_open/">perf_event_open</a></code>(2)</td>
<td>2.6.31</td>
<td> Was perf_counter_open() in<br />
 2.6.31; renamed in 2.6.32
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-personality/">personality</a></code>(2)</td>
<td>1.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-perfctr/">perfctr</a></code>(2)</td>
<td>2.2</td>
<td>SPARC only; removed in 2.6.34
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-perfmonctl/">perfmonctl</a></code>(2)</td>
<td>2.4</td>
<td>IA-64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pidfd_getfd/">pidfd_getfd</a></code>(2)</td>
<td>5.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pidfd_send_signal/">pidfd_send_signal</a></code>(2)</td>
<td>5.1</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2)</td>
<td>5.3</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pipe2/">pipe2</a></code>(2)</td>
<td>2.6.27</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pkey_alloc/">pkey_alloc</a></code>(2)</td>
<td>4.8</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pkey_free/">pkey_free</a></code>(2)</td>
<td>4.8</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pkey_mprotect/">pkey_mprotect</a></code>(2)</td>
<td>4.8</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-poll/">poll</a></code>(2)</td>
<td>2.0.36; 2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pread64/">pread64</a></code>(2)</td>
<td></td>
<td> Added as &quot;pread&quot; in 2.2;<br />
 renamed &quot;pread64&quot; in 2.6
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-preadv/">preadv</a></code>(2)</td>
<td>2.6.30</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-preadv2/">preadv2</a></code>(2)</td>
<td>4.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-prlimit64/">prlimit64</a></code>(2)</td>
<td>2.6.36</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-process_madvise/">process_madvise</a></code>(2)</td>
<td>5.10</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-process_vm_readv/">process_vm_readv</a></code>(2)</td>
<td>3.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-process_vm_writev/">process_vm_writev</a></code>(2)</td>
<td>3.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pselect6/">pselect6</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pwrite64/">pwrite64</a></code>(2)</td>
<td></td>
<td> Added as &quot;pwrite&quot; in 2.2;<br />
 renamed &quot;pwrite64&quot; in 2.6
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pwritev/">pwritev</a></code>(2)</td>
<td>2.6.30</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pwritev2/">pwritev2</a></code>(2)</td>
<td>4.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-query_module/">query_module</a></code>(2)</td>
<td>2.2</td>
<td>Removed in 2.6
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-readahead/">readahead</a></code>(2)</td>
<td>2.4.13</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-readdir/">readdir</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-readlinkat/">readlinkat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-readv/">readv</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-recv/">recv</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-recvmmsg/">recvmmsg</a></code>(2)</td>
<td>2.6.33</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-remap_file_pages/">remap_file_pages</a></code>(2)</td>
<td>2.6</td>
<td>Deprecated since 3.16
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-removexattr/">removexattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rename/">rename</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-renameat/">renameat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-renameat2/">renameat2</a></code>(2)</td>
<td>3.15</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2)</td>
<td>2.6.10</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-riscv_flush_icache/">riscv_flush_icache</a></code>(2)</td>
<td>4.15</td>
<td>RISC-V only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rseq/">rseq</a></code>(2)</td>
<td>4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rt_sigaction/">rt_sigaction</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rt_sigpending/">rt_sigpending</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rt_sigprocmask/">rt_sigprocmask</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rt_sigqueueinfo/">rt_sigqueueinfo</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rt_sigreturn/">rt_sigreturn</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rt_sigsuspend/">rt_sigsuspend</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rt_sigtimedwait/">rt_sigtimedwait</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rt_tgsigqueueinfo/">rt_tgsigqueueinfo</a></code>(2)</td>
<td>2.6.31</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rtas/">rtas</a></code>(2)</td>
<td>2.6.2</td>
<td>PowerPC/PowerPC64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-s390_runtime_instr/">s390_runtime_instr</a></code>(2)</td>
<td>3.7</td>
<td>s390 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-s390_pci_mmio_read/">s390_pci_mmio_read</a></code>(2)</td>
<td>3.19</td>
<td>s390 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-s390_pci_mmio_write/">s390_pci_mmio_write</a></code>(2)</td>
<td>3.19</td>
<td>s390 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-s390_sthyi/">s390_sthyi</a></code>(2)</td>
<td>4.15</td>
<td>s390 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-s390_guarded_storage/">s390_guarded_storage</a></code>(2)</td>
<td>4.12</td>
<td>s390 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_get_affinity/">sched_get_affinity</a></code>(2)</td>
<td>2.6</td>
<td> Name of <code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2)<br />
 on SPARC and SPARC64
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_getattr/">sched_getattr</a></code>(2)</td>
<td>3.14</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_getparam/">sched_getparam</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_rr_get_interval/">sched_rr_get_interval</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_set_affinity/">sched_set_affinity</a></code>(2)</td>
<td>2.6</td>
<td> Name of <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2)<br />
 on SPARC and SPARC64
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2)</td>
<td>3.14</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2)</td>
<td>3.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-select/">select</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-semget/">semget</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-semop/">semop</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-semtimedop/">semtimedop</a></code>(2)</td>
<td>2.6; 2.4.22</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-send/">send</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sendfile/">sendfile</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sendfile64/">sendfile64</a></code>(2)</td>
<td>2.6; 2.4.19</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sendmmsg/">sendmmsg</a></code>(2)</td>
<td>3.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2)</td>
<td>2.6.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-set_robust_list/">set_robust_list</a></code>(2)</td>
<td>2.6.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-set_tid_address/">set_tid_address</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-set_tls/">set_tls</a></code>(2)</td>
<td>2.6.11</td>
<td> ARM OABI/EABI only (constant<br />
 has <code>__ARM_NR</code> prefix)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setdomainname/">setdomainname</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setfsgid/">setfsgid</a></code>(2)</td>
<td>1.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setfsgid32/">setfsgid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2)</td>
<td>1.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setfsuid32/">setfsuid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setgid32/">setgid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setgroups32/">setgroups32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sethae/">sethae</a></code>(2)</td>
<td>2.0</td>
<td>Alpha only; see NOTES
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setns/">setns</a></code>(2)</td>
<td>3.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setpgrp/">setpgrp</a></code>(2)</td>
<td>2.0</td>
<td> Alternative name for<br />
 <code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2) on Alpha
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setregid/">setregid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setregid32/">setregid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setresgid/">setresgid</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setresgid32/">setresgid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setresuid32/">setresuid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setreuid32/">setreuid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setuid32/">setuid32</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setup/">setup</a></code>(2)</td>
<td>1.0</td>
<td>Removed in 2.2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setxattr/">setxattr</a></code>(2)</td>
<td>2.6; 2.4.18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sgetmask/">sgetmask</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-signal/">signal</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2)</td>
<td>2.6.22</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-signalfd4/">signalfd4</a></code>(2)</td>
<td>2.6.27</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-socket/">socket</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2)</td>
<td>2.0</td>
<td>See notes on <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-spill/">spill</a></code>(2)</td>
<td>2.6.13</td>
<td>Xtensa only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-splice/">splice</a></code>(2)</td>
<td>2.6.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-spu_create/">spu_create</a></code>(2)</td>
<td>2.6.16</td>
<td>PowerPC/PowerPC64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-spu_run/">spu_run</a></code>(2)</td>
<td>2.6.16</td>
<td>PowerPC/PowerPC64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ssetmask/">ssetmask</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-stat64/">stat64</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-statfs64/">statfs64</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-statx/">statx</a></code>(2)</td>
<td>4.11</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-stime/">stime</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-subpage_prot/">subpage_prot</a></code>(2)</td>
<td>2.6.25</td>
<td>PowerPC/PowerPC64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-swapcontext/">swapcontext</a></code>(2)</td>
<td>2.6.3</td>
<td>PowerPC/PowerPC64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-switch_endian/">switch_endian</a></code>(2)</td>
<td>4.1</td>
<td>PowerPC64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-swapoff/">swapoff</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-swapon/">swapon</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-symlinkat/">symlinkat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sync/">sync</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sync_file_range/">sync_file_range</a></code>(2)</td>
<td>2.6.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sync_file_range2/">sync_file_range2</a></code>(2)</td>
<td>2.6.22</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-syncfs/">syncfs</a></code>(2)</td>
<td>2.6.39</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sys_debug_setcontext/">sys_debug_setcontext</a></code>(2)</td>
<td>2.6.11</td>
<td>PowerPC only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2)</td>
<td>1.0</td>
<td> Still available on ARM OABI<br />
 and MIPS O32 ABI
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sysfs/">sysfs</a></code>(2)</td>
<td>1.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sysinfo/">sysinfo</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sysmips/">sysmips</a></code>(2)</td>
<td>2.6.0</td>
<td>MIPS only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-tee/">tee</a></code>(2)</td>
<td>2.6.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-time/">time</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timer_delete/">timer_delete</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2)</td>
<td>2.6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timerfd_create/">timerfd_create</a></code>(2)</td>
<td>2.6.25</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timerfd_gettime/">timerfd_gettime</a></code>(2)</td>
<td>2.6.25</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timerfd_settime/">timerfd_settime</a></code>(2)</td>
<td>2.6.25</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-times/">times</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-tkill/">tkill</a></code>(2)</td>
<td>2.6; 2.4.22</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-truncate64/">truncate64</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ugetrlimit/">ugetrlimit</a></code>(2)</td>
<td>2.4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-umount/">umount</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-umount2/">umount2</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-uname/">uname</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-unlinkat/">unlinkat</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2)</td>
<td>2.6.16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-uselib/">uselib</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ustat/">ustat</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2)</td>
<td>4.3</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-usr26/">usr26</a></code>(2)</td>
<td>2.4.8.1</td>
<td>ARM OABI only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-usr32/">usr32</a></code>(2)</td>
<td>2.4.8.1</td>
<td>ARM OABI only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-utime/">utime</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2)</td>
<td>2.6.22</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-utrap_install/">utrap_install</a></code>(2)</td>
<td>2.2</td>
<td>SPARC64 only
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2)</td>
<td>2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-vhangup/">vhangup</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-vm86old/">vm86old</a></code>(2)</td>
<td>1.0</td>
<td> Was &quot;vm86&quot;; renamed in<br />
 2.0.28/2.2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-vm86/">vm86</a></code>(2)</td>
<td>2.0.28; 2.2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-vmsplice/">vmsplice</a></code>(2)</td>
<td>2.6.17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-waitid/">waitid</a></code>(2)</td>
<td>2.6.10</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-write/">write</a></code>(2)</td>
<td>1.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-writev/">writev</a></code>(2)</td>
<td>2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-xtensa/">xtensa</a></code>(2)</td>
<td>2.6.13</td>
<td>Xtensa only
</td>
</tr>
</table>
<p> On many platforms, including x86-32, socket calls are all multiplexed (via glibc wrapper functions) through <code><a href="/docs/linux/man/2-socketcall/">socketcall</a></code>(2) and similarly System V IPC calls are multiplexed through <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2). </p>
<p> Although slots are reserved for them in the system call table, the following system calls are not implemented in the standard kernel: <code><a href="/docs/linux/man/2-afs_syscall/">afs_syscall</a></code>(2), <code><a href="/docs/linux/man/2-break/">break</a></code>(2), <code><a href="/docs/linux/man/2-ftime/">ftime</a></code>(2), <code><a href="/docs/linux/man/2-getpmsg/">getpmsg</a></code>(2), <code><a href="/docs/linux/man/2-gtty/">gtty</a></code>(2), <code><a href="/docs/linux/man/2-idle/">idle</a></code>(2), <code><a href="/docs/linux/man/2-lock/">lock</a></code>(2), <code><a href="/docs/linux/man/2-madvise1/">madvise1</a></code>(2), <code><a href="/docs/linux/man/2-mpx/">mpx</a></code>(2), <code><a href="/docs/linux/man/2-phys/">phys</a></code>(2), <code><a href="/docs/linux/man/2-prof/">prof</a></code>(2), <code><a href="/docs/linux/man/2-profil/">profil</a></code>(2), <code><a href="/docs/linux/man/2-putpmsg/">putpmsg</a></code>(2), <code><a href="/docs/linux/man/2-security/">security</a></code>(2), <code><a href="/docs/linux/man/2-stty/">stty</a></code>(2), <code><a href="/docs/linux/man/2-tuxcall/">tuxcall</a></code>(2), <code><a href="/docs/linux/man/2-ulimit/">ulimit</a></code>(2), and <code><a href="/docs/linux/man/2-vserver/">vserver</a></code>(2) (see also <code><a href="/docs/linux/man/2-unimplemented/">unimplemented</a></code>(2)). However, <code><a href="/docs/linux/man/3-ftime/">ftime</a></code>(3), <code><a href="/docs/linux/man/3-profil/">profil</a></code>(3), and <code><a href="/docs/linux/man/3-ulimit/">ulimit</a></code>(3) exist as library routines. The slot for <code><a href="/docs/linux/man/2-phys/">phys</a></code>(2) is in use since kernel 2.1.116 for <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2); <code><a href="/docs/linux/man/2-phys/">phys</a></code>(2) will never be implemented. The <code><a href="/docs/linux/man/2-getpmsg/">getpmsg</a></code>(2) and <code><a href="/docs/linux/man/2-putpmsg/">putpmsg</a></code>(2) calls are for kernels patched to support STREAMS, and may never be in the standard kernel. </p>
<p> There was briefly <code><a href="/docs/linux/man/2-set_zone_reclaim/">set_zone_reclaim</a></code>(2), added in Linux 2.6.13, and removed in 2.6.16; this system call was never available to user space.</p>
<h3>System calls on removed ports</h3>
<p> Some system calls only ever existed on Linux architectures that have since been removed from the kernel:</p>
<dl>
<dt>AVR32 (port removed in Linux 4.12)</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2)</dl>
</dl>
<dt>Blackfin (port removed in Linux 4.17)</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-bfin_spinlock/">bfin_spinlock</a></code>(2) (added in Linux 2.6.22)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-dma_memcpy/">dma_memcpy</a></code>(2) (added in Linux 2.6.22)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2) (added in Linux 2.6.22)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2) (added in Linux 2.6.22)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-sram_alloc/">sram_alloc</a></code>(2) (added in Linux 2.6.22)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-sram_free/">sram_free</a></code>(2) (added in Linux 2.6.22)</dl>
</dl>
<dt>Metag (port removed in Linux 4.17)</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-metag_get_tls/">metag_get_tls</a></code>(2) (add in Linux 3.9)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-metag_set_fpu_flags/">metag_set_fpu_flags</a></code>(2) (add in Linux 3.9)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-metag_set_tls/">metag_set_tls</a></code>(2) (add in Linux 3.9)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-metag_setglobalbit/">metag_setglobalbit</a></code>(2) (add in Linux 3.9)</dl>
</dl>
<dt>Tile (port removed in Linux 4.17)</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-cmpxchg_badaddr/">cmpxchg_badaddr</a></code>(2) (added in Linux 2.6.36)</dl>
</dl>
</dl>
<h2>NOTES</h2>
<p> Roughly speaking, the code belonging to the system call with number __NR_xxx defined in <i>/usr/include/asm/unistd.h</i> can be found in the Linux kernel source in the routine <i>sys_xxx</i>(). There are many exceptions, however, mostly because older system calls were superseded by newer ones, and this has been treated somewhat unsystematically. On platforms with proprietary operating-system emulation, such as sparc, sparc64, and alpha, there are many additional system calls; mips64 also contains a full set of 32-bit system calls. </p>
<p> Over time, changes to the interfaces of some system calls have been necessary. One reason for such changes was the need to increase the size of structures or scalar values passed to the system call. Because of these changes, certain architectures (notably, longstanding 32-bit architectures such as i386) now have various groups of related system calls (e.g., <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2) and <code><a href="/docs/linux/man/2-truncate64/">truncate64</a></code>(2)) which perform similar tasks, but which vary in details such as the size of their arguments. (As noted earlier, applications are generally unaware of this: the glibc wrapper functions do some work to ensure that the right system call is invoked, and that ABI compatibility is preserved for old binaries.) Examples of systems calls that exist in multiple versions are the following:</p>
<dl>
<dt>*</p>
<dd> By now there are three different versions of <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2): <i>sys_stat</i>() (slot <i>__NR_oldstat</i>), <i>sys_newstat</i>() (slot <i>__NR_stat</i>), and <i>sys_stat64</i>() (slot <i>__NR_stat64</i>), with the last being the most current. A similar story applies for <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) and <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2).</p>
<dt>*</p>
<dd> Similarly, the defines <i>__NR_oldolduname</i>, <i>__NR_olduname</i>, and <i>__NR_uname</i> refer to the routines <i>sys_olduname</i>(), <i>sys_uname</i>(), and <i>sys_newuname</i>().</p>
<dt>*</p>
<dd> In Linux 2.0, a new version of <code><a href="/docs/linux/man/2-vm86/">vm86</a></code>(2) appeared, with the old and the new kernel routines being named <i>sys_vm86old</i>() and <i>sys_vm86</i>().</p>
<dt>*</p>
<dd> In Linux 2.4, a new version of <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2) appeared, with the old and the new kernel routines being named <i>sys_old_getrlimit</i>() (slot <i>__NR_getrlimit</i>) and <i>sys_getrlimit</i>() (slot <i>__NR_ugetrlimit</i>).</p>
<dt>*</p>
<dd> Linux 2.4 increased the size of user and group IDs from 16 to 32 bits. To support this change, a range of system calls were added (e.g., <code><a href="/docs/linux/man/2-chown32/">chown32</a></code>(2), <code><a href="/docs/linux/man/2-getuid32/">getuid32</a></code>(2), <code><a href="/docs/linux/man/2-getgroups32/">getgroups32</a></code>(2), <code><a href="/docs/linux/man/2-setresuid32/">setresuid32</a></code>(2)), superseding earlier calls of the same name without the &quot;32&quot; suffix.</p>
<dt>*</p>
<dd> Linux 2.4 added support for applications on 32-bit architectures to access large files (i.e., files for which the sizes and file offsets can&#8217;t be represented in 32 bits.) To support this change, replacements were required for system calls that deal with file offsets and sizes. Thus the following system calls were added: <code><a href="/docs/linux/man/2-fcntl64/">fcntl64</a></code>(2), <code><a href="/docs/linux/man/2-getdents64/">getdents64</a></code>(2), <code><a href="/docs/linux/man/2-stat64/">stat64</a></code>(2), <code><a href="/docs/linux/man/2-statfs64/">statfs64</a></code>(2), <code><a href="/docs/linux/man/2-truncate64/">truncate64</a></code>(2), and their analogs that work with file descriptors or symbolic links. These system calls supersede the older system calls which, except in the case of the &quot;stat&quot; calls, have the same name without the &quot;64&quot; suffix.</p>
<dt>
<dd> On newer platforms that only have 64-bit file access and 32-bit UIDs/GIDs (e.g., alpha, ia64, s390x, x86-64), there is just a single version of the UID/GID and file access system calls. On platforms (typically, 32-bit platforms) where the *64 and *32 calls exist, the other versions are obsolete.</p>
<dt>*</p>
<dd> The <i>rt_sig*</i> calls were added in kernel 2.2 to support the addition of real-time signals (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)). These system calls supersede the older system calls of the same name without the &quot;rt_&quot; prefix.</p>
<dt>*</p>
<dd> The <code><a href="/docs/linux/man/2-select/">select</a></code>(2) and <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) system calls use five or more arguments, which caused problems in the way argument passing on the i386 used to be set up. Thus, while other architectures have <i>sys_select</i>() and <i>sys_mmap</i>() corresponding to <i>__NR_select</i> and <i>__NR_mmap</i>, on i386 one finds <i>old_select</i>() and <i>old_mmap</i>() (routines that use a pointer to an argument block) instead. These days passing five arguments is not a problem any more, and there is a <i>__NR__newselect</i> that corresponds directly to <i>sys_select</i>() and similarly <i>__NR_mmap2</i>. s390x is the only 64-bit architecture that has <i>old_mmap</i>().</dl>
<h3>Architecture-specific details: Alpha</h3>
<dl>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-getxgid/">getxgid</a></code>(2) returns a pair of GID and effective GID via registers <code>r0</code> and <code>r20</code>; it is provided instead of <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2) and <code><a href="/docs/linux/man/2-getegid/">getegid</a></code>(2).</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-getxpid/">getxpid</a></code>(2) returns a pair of PID and parent PID via registers <code>r0</code> and <code>r20</code>; it is provided instead of <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) and <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2).</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-old_adjtimex/">old_adjtimex</a></code>(2) is a variant of <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2) that uses <i>struct timeval32</i>, for compatibility with OSF/1.</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-getxuid/">getxuid</a></code>(2) returns a pair of GID and effective GID via registers <code>r0</code> and <code>r20</code>; it is provided instead of <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2) and <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2).</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-sethae/">sethae</a></code>(2) is used for configuring the Host Address Extension register on low-cost Alphas in order to access address space beyond first 27 bits.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-intro/">intro</a></code>(2), <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), <code><a href="/docs/linux/man/2-unimplemented/">unimplemented</a></code>(2), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/7-libc/">libc</a></code>(7), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
