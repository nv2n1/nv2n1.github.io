---
title: "clone3(2)"
name: "clone3"
section: "2"
letter: "c"
url: "/docs/linux/man/2-clone3/"
---

<h2 class="name">NAME</h2>
 

 clone, __clone2, clone3 - create a child process 

<h2>SYNOPSIS</h2>

 <pre><code>
/* Prototype for the glibc wrapper function */
#define _GNU_SOURCE
#include &lt;sched.h&gt;
int clone(int (*fn)(void *), void *stack, int flags, void *arg, ...
          /* pid_t *parent_tid, void *tls, pid_t *child_tid */);
/* For the prototype of the raw clone() system call, see NOTES */
long clone3(struct clone_args *cl_args, size_t size);
</code></pre> 

 <i>Note</i>: There is not yet a glibc wrapper for <b>clone3</b>(); see NOTES.

<h2>DESCRIPTION</h2>

 These system calls create a new (&quot;child&quot;) process, in a manner similar to <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2). 

 By contrast with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2), these system calls provide more precise control over what pieces of execution context are shared between the calling process and the child process. For example, using these system calls, the caller can control whether or not the two processes share the virtual address space, the table of file descriptors, and the table of signal handlers. These system calls also allow the new child process to be placed in separate <b><a HREF="/docs/linux/man/7-namespaces/">namespaces</a></b>(7). 

 Note that in this manual page, &quot;calling process&quot; normally corresponds to &quot;parent process&quot;. But see the descriptions of <b>CLONE_PARENT</b> and <b>CLONE_THREAD</b> below. 

 This page describes the following interfaces:
<dl>
<dt>*
<dd> The glibc <b>clone</b>() wrapper function and the underlying system call on which it is based. The main text describes the wrapper function; the differences for the raw system call are described toward the end of this page.
<dt>*
<dd> The newer <b>clone3</b>() system call.</dl>
 

 In the remainder of this page, the terminology &quot;the clone call&quot; is used when noting details that apply to all of these interfaces,

<h3>The clone() wrapper function</h3>

 When the child process is created with the <b>clone</b>() wrapper function, it commences execution by calling the function pointed to by the argument <i>fn</i>. (This differs from <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2), where execution continues in the child from the point of the <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2) call.) The <i>arg</i> argument is passed as the argument of the function <i>fn</i>. 

 When the <i>fn</i>(<i>arg</i>) function returns, the child process terminates. The integer returned by <i>fn</i> is the exit status for the child process. The child process may also terminate explicitly by calling <b><a HREF="/docs/linux/man/2-exit/">exit</a></b>(2) or after receiving a fatal signal. 

 The <i>stack</i> argument specifies the location of the stack used by the child process. Since the child and calling process may share memory, it is not possible for the child process to execute in the same stack as the calling process. The calling process must therefore set up memory space for the child stack and pass a pointer to this space to <b>clone</b>(). Stacks grow downward on all processors that run Linux (except the HP PA processors), so <i>stack</i> usually points to the topmost address of the memory space set up for the child stack. Note that <b>clone</b>() does not provide a means whereby the caller can inform the kernel of the size of the stack area. 

 The remaining arguments to <b>clone</b>() are discussed below.

<h3>clone3()</h3>

 The <b>clone3</b>() system call provides a superset of the functionality of the older <b>clone</b>() interface. It also provides a number of API improvements, including: space for additional flags bits; cleaner separation in the use of various arguments; and the ability to specify the size of the child's stack area. 

 As with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2), <b>clone3</b>() returns in both the parent and the child. It returns 0 in the child process and returns the PID of the child in the parent. 

 The <i>cl_args</i> argument of <b>clone3</b>() is a structure of the following form: 

 struct clone_args { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags bit mask&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 pidfd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Where to store PID file descriptor 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(<i>pid_t&nbsp;*</i>)&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 child_tid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Where to store child TID, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in child's memory&nbsp;(<i>pid_t&nbsp;*</i>)&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 parent_tid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Where to store child TID, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in parent's memory&nbsp;(<i>int&nbsp;*</i>)&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 exit_signal;&nbsp;<wbr>&nbsp;/*&nbsp;Signal to deliver to parent on 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;child termination&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 stack;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pointer to lowest byte of stack&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 stack_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of stack&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 tls;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Location of new TLS&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 set_tid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pointer to a&nbsp;<i>pid_t</i>&nbsp;array 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 5.5)&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 set_tid_size;&nbsp;/*&nbsp;Number of elements in&nbsp;<i>set_tid</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 5.5)&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 cgroup;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File descriptor for target cgroup 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of child&nbsp;(since Linux 5.7)&nbsp;*/ }; 

 The <i>size</i> argument that is supplied to <b>clone3</b>() should be initialized to the size of this structure. (The existence of the <i>size</i> argument permits future extensions to the <i>clone_args</i> structure.) 

 The stack for the child process is specified via <i>cl_args.stack</i>, which points to the lowest byte of the stack area, and <i>cl_args.stack_size</i>, which specifies the size of the stack in bytes. In the case where the <b>CLONE_VM</b> flag (see below) is specified, a stack must be explicitly allocated and specified. Otherwise, these two fields can be specified as NULL and 0, which causes the child to use the same stack area as the parent (in the child's own virtual address space). 

 The remaining fields in the <i>cl_args</i> argument are discussed below.

<h3>Equivalence between clone() and clone3() arguments</h3>

 Unlike the older <b>clone</b>() interface, where arguments are passed individually, in the newer <b>clone3</b>() interface the arguments are packaged into the <i>clone_args</i> structure shown above. This structure allows for a superset of the information passed via the <b>clone</b>() arguments. 

 The following table shows the equivalence between the arguments of <b>clone</b>() and the fields in the <i>clone_args</i> argument supplied to <b>clone3</b>():
<dl>
<dt>
<dd> <table> <tr VALIGN=top><td><b>clone()</b></td><td><b>clone3()</b></td><td><b>Notes</b>
</td></tr> <tr VALIGN=top><td></td><td><i>cl_args</i> field</td><td>
</td></tr> <tr VALIGN=top><td><i>flags &amp; ~0xff</i></td><td><i>flags</i></td><td>For most flags; details below
</td></tr> <tr VALIGN=top><td><i>parent_tid</i></td><td><i>pidfd</i></td><td>See CLONE_PIDFD
</td></tr> <tr VALIGN=top><td><i>child_tid</i></td><td><i>child_tid</i></td><td>See CLONE_CHILD_SETTID
</td></tr> <tr VALIGN=top><td><i>parent_tid</i></td><td><i>parent_tid</i></td><td>See CLONE_PARENT_SETTID
</td></tr> <tr VALIGN=top><td><i>flags &amp; 0xff</i></td><td><i>exit_signal</i></td><td>
</td></tr> <tr VALIGN=top><td><i>stack</i></td><td><i>stack</i></td><td>
</td></tr> <tr VALIGN=top><td><i>---</i></td><td><i>stack_size</i></td><td>
</td></tr> <tr VALIGN=top><td><i>tls</i></td><td><i>tls</i></td><td>See CLONE_SETTLS
</td></tr> <tr VALIGN=top><td><i>---</i></td><td><i>set_tid</i></td><td>See below for details
</td></tr> <tr VALIGN=top><td><i>---</i></td><td><i>set_tid_size</i></td><td>
</td></tr> <tr VALIGN=top><td><i>---</i></td><td><i>cgroup</i></td><td>See CLONE_INTO_CGROUP
</td></tr> </table></dl>

<h3>The child termination signal</h3>

 When the child process terminates, a signal may be sent to the parent. The termination signal is specified in the low byte of <i>flags</i> (<b>clone</b>()) or in <i>cl_args.exit_signal</i> (<b>clone3</b>()). If this signal is specified as anything other than <b>SIGCHLD</b>, then the parent process must specify the <b>__WALL</b> or <b>__WCLONE</b> options when waiting for the child with <b><a HREF="/docs/linux/man/2-wait/">wait</a></b>(2). If no signal (i.e., zero) is specified, then the parent process is not signaled when the child terminates.

<h3>The set_tid array</h3>

 By default, the kernel chooses the next sequential PID for the new process in each of the PID namespaces where it is present. When creating a process with <b>clone3</b>(), the <i>set_tid</i> array (available since Linux 5.5) can be used to select specific PIDs for the process in some or all of the PID namespaces where it is present. If the PID of the newly created process should be set only for the current PID namespace or in the newly created PID namespace (if <i>flags</i> contains <b>CLONE_NEWPID</b>) then the first element in the <i>set_tid</i> array has to be the desired PID and <i>set_tid_size</i> needs to be 1. 

 If the PID of the newly created process should have a certain value in multiple PID namespaces, then the <i>set_tid</i> array can have multiple entries. The first entry defines the PID in the most deeply nested PID namespace and each of the following entries contains the PID in the corresponding ancestor PID namespace. The number of PID namespaces in which a PID should be set is defined by <i>set_tid_size</i> which cannot be larger than the number of currently nested PID namespaces. 

 To create a process with the following PIDs in a PID namespace hierarchy:
<dl>
<dt>
<dd> <table> <tr VALIGN=top><td><b>PID NS level</b></td><td><b>Requested PID</b></td><td><b>Notes</b>
</td></tr> <tr VALIGN=top><td>0</td><td>31496</td><td>Outermost PID namespace
</td></tr> <tr VALIGN=top><td>1</td><td>42</td><td>
</td></tr> <tr VALIGN=top><td>2</td><td>7</td><td>Innermost PID namespace
</td></tr> </table></dl>
 

 Set the array to: 

 set_tid[0] = 7; set_tid[1] = 42; set_tid[2] = 31496; set_tid_size = 3; 

 If only the PIDs in the two innermost PID namespaces need to be specified, set the array to: 

 set_tid[0] = 7; set_tid[1] = 42; set_tid_size = 2; 

 The PID in the PID namespaces outside the two innermost PID namespaces will be selected the same way as any other PID is selected. 

 The <i>set_tid</i> feature requires <b>CAP_SYS_ADMIN</b> or (since Linux 5.9) <b>CAP_CHECKPOINT_RESTORE</b> in all owning user namespaces of the target PID namespaces. 

 Callers may only choose a PID greater than 1 in a given PID namespace if an <b>init</b> process (i.e., a process with PID 1) already exists in that namespace. Otherwise the PID entry for this PID namespace must be 1.

<h3>The flags mask</h3>

 Both <b>clone</b>() and <b>clone3</b>() allow a flags bit mask that modifies their behavior and allows the caller to specify what is shared between the calling process and the child process. This bit mask---the <i>flags</i> argument of <b>clone</b>() or the <i>cl_args.flags</i> field passed to <b>clone3</b>()---is referred to as the <i>flags</i> mask in the remainder of this page. 

 The <i>flags</i> mask is specified as a bitwise-OR of zero or more of the constants listed below. Except as noted below, these flags are available (and have the same effect) in both <b>clone</b>() and <b>clone3</b>().
<dl>
<dt><b>CLONE_CHILD_CLEARTID</b> (since Linux 2.5.49)
<dd> Clear (zero) the child thread ID at the location pointed to by <i>child_tid</i> (<b>clone</b>()) or <i>cl_args.child_tid</i> (<b>clone3</b>()) in child memory when the child exits, and do a wakeup on the futex at that address. The address involved may be changed by the <b><a HREF="/docs/linux/man/2-set_tid_address/">set_tid_address</a></b>(2) system call. This is used by threading libraries.
<dt><b>CLONE_CHILD_SETTID</b> (since Linux 2.5.49)
<dd> Store the child thread ID at the location pointed to by <i>child_tid</i> (<b>clone</b>()) or <i>cl_args.child_tid</i> (<b>clone3</b>()) in the child's memory. The store operation completes before the clone call returns control to user space in the child process. (Note that the store operation may not have completed before the clone call returns in the parent process, which will be relevant if the <b>CLONE_VM</b> flag is also employed.)
<dt><b>CLONE_CLEAR_SIGHAND</b> (since Linux 5.5)
<dd> By default, signal dispositions in the child thread are the same as in the parent. If this flag is specified, then all signals that are handled in the parent are reset to their default dispositions (<b>SIG_DFL</b>) in the child.
<dt>
<dd> Specifying this flag together with <b>CLONE_SIGHAND</b> is nonsensical and disallowed.
<dt><b>CLONE_DETACHED</b> (historical)
<dd> For a while (during the Linux 2.5 development series) there was a <b>CLONE_DETACHED</b> flag, which caused the parent not to receive a signal when the child terminated. Ultimately, the effect of this flag was subsumed under the <b>CLONE_THREAD</b> flag and by the time Linux 2.6.0 was released, this flag had no effect. Starting in Linux 2.6.2, the need to give this flag together with <b>CLONE_THREAD</b> disappeared.
<dt>
<dd> This flag is still defined, but it is usually ignored when calling <b>clone</b>(). However, see the description of <b>CLONE_PIDFD</b> for some exceptions.
<dt><b>CLONE_FILES</b> (since Linux 2.0)
<dd> If <b>CLONE_FILES</b> is set, the calling process and the child process share the same file descriptor table. Any file descriptor created by the calling process or by the child process is also valid in the other process. Similarly, if one of the processes closes a file descriptor, or changes its associated flags (using the <b><a HREF="/docs/linux/man/2-fcntl/">fcntl</a></b>(2) <b>F_SETFD</b> operation), the other process is also affected. If a process sharing a file descriptor table calls <b><a HREF="/docs/linux/man/2-execve/">execve</a></b>(2), its file descriptor table is duplicated (unshared).
<dt>
<dd> If <b>CLONE_FILES</b> is not set, the child process inherits a copy of all file descriptors opened in the calling process at the time of the clone call. Subsequent operations that open or close file descriptors, or change file descriptor flags, performed by either the calling process or the child process do not affect the other process. Note, however, that the duplicated file descriptors in the child refer to the same open file descriptions as the corresponding file descriptors in the calling process, and thus share file offsets and file status flags (see <b><a HREF="/docs/linux/man/2-open/">open</a></b>(2)).
<dt><b>CLONE_FS</b> (since Linux 2.0)
<dd> If <b>CLONE_FS</b> is set, the caller and the child process share the same filesystem information. This includes the root of the filesystem, the current working directory, and the umask. Any call to <b><a HREF="/docs/linux/man/2-chroot/">chroot</a></b>(2), <b><a HREF="/docs/linux/man/2-chdir/">chdir</a></b>(2), or <b><a HREF="/docs/linux/man/2-umask/">umask</a></b>(2) performed by the calling process or the child process also affects the other process.
<dt>
<dd> If <b>CLONE_FS</b> is not set, the child process works on a copy of the filesystem information of the calling process at the time of the clone call. Calls to <b><a HREF="/docs/linux/man/2-chroot/">chroot</a></b>(2), <b><a HREF="/docs/linux/man/2-chdir/">chdir</a></b>(2), or <b><a HREF="/docs/linux/man/2-umask/">umask</a></b>(2) performed later by one of the processes do not affect the other process.
<dt><b>CLONE_INTO_CGROUP</b> (since Linux 5.7)
<dd> By default, a child process is placed in the same version 2 cgroup as its parent. The <b>CLONE_INTO_CGROUP</b> flag allows the child process to be created in a different version 2 cgroup. (Note that <b>CLONE_INTO_CGROUP</b> has effect only for version 2 cgroups.)
<dt>
<dd> In order to place the child process in a different cgroup, the caller specifies <b>CLONE_INTO_CGROUP</b> in <i>cl_args.flags</i> and passes a file descriptor that refers to a version 2 cgroup in the <i>cl_args.cgroup</i> field. (This file descriptor can be obtained by opening a cgroup v2 directory using either the <b>O_RDONLY</b> or the <b>O_PATH</b> flag.) Note that all of the usual restrictions (described in <b><a HREF="/docs/linux/man/7-cgroups/">cgroups</a></b>(7)) on placing a process into a version 2 cgroup apply.
<dt>
<dd> Among the possible use cases for <b>CLONE_INTO_CGROUP</b> are the following:
<dl>
<dt>
<dd>
<dl>
<dt>*
<dd> Spawning a process into a cgroup different from the parent's cgroup makes it possible for a service manager to directly spawn new services into dedicated cgroups. This eliminates the accounting jitter that would be caused if the child process was first created in the same cgroup as the parent and then moved into the target cgroup. Furthermore, spawning the child process directly into a target cgroup is significantly cheaper than moving the child process into the target cgroup after it has been created.
<dt>*
<dd> The <b>CLONE_INTO_CGROUP</b> flag also allows the creation of frozen child processes by spawning them into a frozen cgroup. (See <b><a HREF="/docs/linux/man/7-cgroups/">cgroups</a></b>(7) for a description of the freezer controller.)
<dt>*
<dd> For threaded applications (or even thread implementations which make use of cgroups to limit individual threads), it is possible to establish a fixed cgroup layout before spawning each thread directly into its target cgroup.</dl>
</dl>

<dt><b>CLONE_IO</b> (since Linux 2.6.25)
<dd> If <b>CLONE_IO</b> is set, then the new process shares an I/O context with the calling process. If this flag is not set, then (as with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2)) the new process has its own I/O context.
<dt>
<dd> The I/O context is the I/O scope of the disk scheduler (i.e., what the I/O scheduler uses to model scheduling of a process's I/O). If processes share the same I/O context, they are treated as one by the I/O scheduler. As a consequence, they get to share disk time. For some I/O schedulers, if two processes share an I/O context, they will be allowed to interleave their disk access. If several threads are doing I/O on behalf of the same process (<b><a HREF="/docs/linux/man/3-aio_read/">aio_read</a></b>(3), for instance), they should employ <b>CLONE_IO</b> to get better I/O performance.
<dt>
<dd> If the kernel is not configured with the <b>CONFIG_BLOCK</b> option, this flag is a no-op.
<dt><b>CLONE_NEWCGROUP</b> (since Linux 4.6)
<dd> Create the process in a new cgroup namespace. If this flag is not set, then (as with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2)) the process is created in the same cgroup namespaces as the calling process.
<dt>
<dd> For further information on cgroup namespaces, see <b><a HREF="/docs/linux/man/7-cgroup_namespaces/">cgroup_namespaces</a></b>(7).
<dt>
<dd> Only a privileged process (<b>CAP_SYS_ADMIN</b>) can employ <b>CLONE_NEWCGROUP</b>.
<dt><b>CLONE_NEWIPC</b> (since Linux 2.6.19)
<dd> If <b>CLONE_NEWIPC</b> is set, then create the process in a new IPC namespace. If this flag is not set, then (as with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2)), the process is created in the same IPC namespace as the calling process.
<dt>
<dd> For further information on IPC namespaces, see <b><a HREF="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></b>(7).
<dt>
<dd> Only a privileged process (<b>CAP_SYS_ADMIN</b>) can employ <b>CLONE_NEWIPC</b>. This flag can't be specified in conjunction with <b>CLONE_SYSVSEM</b>.
<dt><b>CLONE_NEWNET</b> (since Linux 2.6.24)
<dd> (The implementation of this flag was completed only by about kernel version 2.6.29.)
<dt>
<dd> If <b>CLONE_NEWNET</b> is set, then create the process in a new network namespace. If this flag is not set, then (as with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2)) the process is created in the same network namespace as the calling process.
<dt>
<dd> For further information on network namespaces, see <b><a HREF="/docs/linux/man/7-network_namespaces/">network_namespaces</a></b>(7).
<dt>
<dd> Only a privileged process (<b>CAP_SYS_ADMIN</b>) can employ <b>CLONE_NEWNET</b>.
<dt><b>CLONE_NEWNS</b> (since Linux 2.4.19)
<dd> If <b>CLONE_NEWNS</b> is set, the cloned child is started in a new mount namespace, initialized with a copy of the namespace of the parent. If <b>CLONE_NEWNS</b> is not set, the child lives in the same mount namespace as the parent.
<dt>
<dd> For further information on mount namespaces, see <b><a HREF="/docs/linux/man/7-namespaces/">namespaces</a></b>(7) and <b><a HREF="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></b>(7).
<dt>
<dd> Only a privileged process (<b>CAP_SYS_ADMIN</b>) can employ <b>CLONE_NEWNS</b>. It is not permitted to specify both <b>CLONE_NEWNS</b> and <b>CLONE_FS</b> in the same clone call.
<dt><b>CLONE_NEWPID</b> (since Linux 2.6.24)
<dd> If <b>CLONE_NEWPID</b> is set, then create the process in a new PID namespace. If this flag is not set, then (as with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2)) the process is created in the same PID namespace as the calling process.
<dt>
<dd> For further information on PID namespaces, see <b><a HREF="/docs/linux/man/7-namespaces/">namespaces</a></b>(7) and <b><a HREF="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></b>(7).
<dt>
<dd> Only a privileged process (<b>CAP_SYS_ADMIN</b>) can employ <b>CLONE_NEWPID</b>. This flag can't be specified in conjunction with <b>CLONE_THREAD</b> or <b>CLONE_PARENT</b>.
<dt><b>CLONE_NEWUSER</b>
<dd> (This flag first became meaningful for <b>clone</b>() in Linux 2.6.23, the current <b>clone</b>() semantics were merged in Linux 3.5, and the final pieces to make the user namespaces completely usable were merged in Linux 3.8.)
<dt>
<dd> If <b>CLONE_NEWUSER</b> is set, then create the process in a new user namespace. If this flag is not set, then (as with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2)) the process is created in the same user namespace as the calling process.
<dt>
<dd> For further information on user namespaces, see <b><a HREF="/docs/linux/man/7-namespaces/">namespaces</a></b>(7) and <b><a HREF="/docs/linux/man/7-user_namespaces/">user_namespaces</a></b>(7).
<dt>
<dd> Before Linux 3.8, use of <b>CLONE_NEWUSER</b> required that the caller have three capabilities: <b>CAP_SYS_ADMIN</b>, <b>CAP_SETUID</b>, and <b>CAP_SETGID</b>. Starting with Linux 3.8, no privileges are needed to create a user namespace.
<dt>
<dd> This flag can't be specified in conjunction with <b>CLONE_THREAD</b> or <b>CLONE_PARENT</b>. For security reasons, <b>CLONE_NEWUSER</b> cannot be specified in conjunction with <b>CLONE_FS</b>.
<dt><b>CLONE_NEWUTS</b> (since Linux 2.6.19)
<dd> If <b>CLONE_NEWUTS</b> is set, then create the process in a new UTS namespace, whose identifiers are initialized by duplicating the identifiers from the UTS namespace of the calling process. If this flag is not set, then (as with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2)) the process is created in the same UTS namespace as the calling process.
<dt>
<dd> For further information on UTS namespaces, see <b><a HREF="/docs/linux/man/7-uts_namespaces/">uts_namespaces</a></b>(7).
<dt>
<dd> Only a privileged process (<b>CAP_SYS_ADMIN</b>) can employ <b>CLONE_NEWUTS</b>.
<dt><b>CLONE_PARENT</b> (since Linux 2.3.12)
<dd> If <b>CLONE_PARENT</b> is set, then the parent of the new child (as returned by <b><a HREF="/docs/linux/man/2-getppid/">getppid</a></b>(2)) will be the same as that of the calling process.
<dt>
<dd> If <b>CLONE_PARENT</b> is not set, then (as with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2)) the child's parent is the calling process.
<dt>
<dd> Note that it is the parent process, as returned by <b><a HREF="/docs/linux/man/2-getppid/">getppid</a></b>(2), which is signaled when the child terminates, so that if <b>CLONE_PARENT</b> is set, then the parent of the calling process, rather than the calling process itself, will be signaled.
<dt>
<dd> The <b>CLONE_PARENT</b> flag can't be used in clone calls by the global init process (PID 1 in the initial PID namespace) and init processes in other PID namespaces. This restriction prevents the creation of multi-rooted process trees as well as the creation of unreapable zombies in the initial PID namespace.
<dt><b>CLONE_PARENT_SETTID</b> (since Linux 2.5.49)
<dd> Store the child thread ID at the location pointed to by <i>parent_tid</i> (<b>clone</b>()) or <i>cl_args.parent_tid</i> (<b>clone3</b>()) in the parent's memory. (In Linux 2.5.32-2.5.48 there was a flag <b>CLONE_SETTID</b> that did this.) The store operation completes before the clone call returns control to user space.
<dt><b>CLONE_PID</b> (Linux 2.0 to 2.5.15)
<dd> If <b>CLONE_PID</b> is set, the child process is created with the same process ID as the calling process. This is good for hacking the system, but otherwise of not much use. From Linux 2.3.21 onward, this flag could be specified only by the system boot process (PID 0). The flag disappeared completely from the kernel sources in Linux 2.5.16. Subsequently, the kernel silently ignored this bit if it was specified in the <i>flags</i> mask. Much later, the same bit was recycled for use as the <b>CLONE_PIDFD</b> flag.
<dt><b>CLONE_PIDFD</b> (since Linux 5.2)
<dd> If this flag is specified, a PID file descriptor referring to the child process is allocated and placed at a specified location in the parent's memory. The close-on-exec flag is set on this new file descriptor. PID file descriptors can be used for the purposes described in <b><a HREF="/docs/linux/man/2-pidfd_open/">pidfd_open</a></b>(2).
<dl>
<dt>
<dd>
<dl>
<dt>*
<dd> When using <b>clone3</b>(), the PID file descriptor is placed at the location pointed to by <i>cl_args.pidfd</i>.
<dt>*
<dd> When using <b>clone</b>(), the PID file descriptor is placed at the location pointed to by <i>parent_tid</i>. Since the <i>parent_tid</i> argument is used to return the PID file descriptor, <b>CLONE_PIDFD</b> cannot be used with <b>CLONE_PARENT_SETTID</b> when calling <b>clone</b>().</dl>
</dl>

<dt>
<dd> It is currently not possible to use this flag together with <b>CLONE_THREAD.</b> This means that the process identified by the PID file descriptor will always be a thread group leader.
<dt>
<dd> If the obsolete <b>CLONE_DETACHED</b> flag is specified alongside <b>CLONE_PIDFD</b> when calling <b>clone</b>(), an error is returned. An error also results if <b>CLONE_DETACHED</b> is specified when calling <b>clone3</b>(). This error behavior ensures that the bit corresponding to <b>CLONE_DETACHED</b> can be reused for further PID file descriptor features in the future.
<dt><b>CLONE_PTRACE</b> (since Linux 2.2)
<dd> If <b>CLONE_PTRACE</b> is specified, and the calling process is being traced, then trace the child also (see <b><a HREF="/docs/linux/man/2-ptrace/">ptrace</a></b>(2)).
<dt><b>CLONE_SETTLS</b> (since Linux 2.5.32)
<dd> The TLS (Thread Local Storage) descriptor is set to <i>tls</i>.
<dt>
<dd> The interpretation of <i>tls</i> and the resulting effect is architecture dependent. On x86, <i>tls</i> is interpreted as a <i>struct user_desc&nbsp;*</i> (see <b><a HREF="/docs/linux/man/2-set_thread_area/">set_thread_area</a></b>(2)). On x86-64 it is the new value to be set for the %fs base register (see the <b>ARCH_SET_FS</b> argument to <b><a HREF="/docs/linux/man/2-arch_prctl/">arch_prctl</a></b>(2)). On architectures with a dedicated TLS register, it is the new value of that register.
<dt>
<dd> Use of this flag requires detailed knowledge and generally it should not be used except in libraries implementing threading.
<dt><b>CLONE_SIGHAND</b> (since Linux 2.0)
<dd> If <b>CLONE_SIGHAND</b> is set, the calling process and the child process share the same table of signal handlers. If the calling process or child process calls <b><a HREF="/docs/linux/man/2-sigaction/">sigaction</a></b>(2) to change the behavior associated with a signal, the behavior is changed in the other process as well. However, the calling process and child processes still have distinct signal masks and sets of pending signals. So, one of them may block or unblock signals using <b><a HREF="/docs/linux/man/2-sigprocmask/">sigprocmask</a></b>(2) without affecting the other process.
<dt>
<dd> If <b>CLONE_SIGHAND</b> is not set, the child process inherits a copy of the signal handlers of the calling process at the time of the clone call. Calls to <b><a HREF="/docs/linux/man/2-sigaction/">sigaction</a></b>(2) performed later by one of the processes have no effect on the other process.
<dt>
<dd> Since Linux 2.6.0, the <i>flags</i> mask must also include <b>CLONE_VM</b> if <b>CLONE_SIGHAND</b> is specified
<dt><b>CLONE_STOPPED</b> (since Linux 2.6.0)
<dd> If <b>CLONE_STOPPED</b> is set, then the child is initially stopped (as though it was sent a <b>SIGSTOP</b> signal), and must be resumed by sending it a <b>SIGCONT</b> signal.
<dt>
<dd> This flag was <i>deprecated</i> from Linux 2.6.25 onward, and was <i>removed</i> altogether in Linux 2.6.38. Since then, the kernel silently ignores it without error. Starting with Linux 4.6, the same bit was reused for the <b>CLONE_NEWCGROUP</b> flag.
<dt><b>CLONE_SYSVSEM</b> (since Linux 2.5.10)
<dd> If <b>CLONE_SYSVSEM</b> is set, then the child and the calling process share a single list of System V semaphore adjustment (<i>semadj</i>) values (see <b><a HREF="/docs/linux/man/2-semop/">semop</a></b>(2)). In this case, the shared list accumulates <i>semadj</i> values across all processes sharing the list, and semaphore adjustments are performed only when the last process that is sharing the list terminates (or ceases sharing the list using <b><a HREF="/docs/linux/man/2-unshare/">unshare</a></b>(2)). If this flag is not set, then the child has a separate <i>semadj</i> list that is initially empty.
<dt><b>CLONE_THREAD</b> (since Linux 2.4.0)
<dd> If <b>CLONE_THREAD</b> is set, the child is placed in the same thread group as the calling process. To make the remainder of the discussion of <b>CLONE_THREAD</b> more readable, the term &quot;thread&quot; is used to refer to the processes within a thread group.
<dt>
<dd> Thread groups were a feature added in Linux 2.4 to support the POSIX threads notion of a set of threads that share a single PID. Internally, this shared PID is the so-called thread group identifier (TGID) for the thread group. Since Linux 2.4, calls to <b><a HREF="/docs/linux/man/2-getpid/">getpid</a></b>(2) return the TGID of the caller.
<dt>
<dd> The threads within a group can be distinguished by their (system-wide) unique thread IDs (TID). A new thread's TID is available as the function result returned to the caller, and a thread can obtain its own TID using <b><a HREF="/docs/linux/man/2-gettid/">gettid</a></b>(2).
<dt>
<dd> When a clone call is made without specifying <b>CLONE_THREAD</b>, then the resulting thread is placed in a new thread group whose TGID is the same as the thread's TID. This thread is the <i>leader</i> of the new thread group.
<dt>
<dd> A new thread created with <b>CLONE_THREAD</b> has the same parent process as the process that made the clone call (i.e., like <b>CLONE_PARENT</b>), so that calls to <b><a HREF="/docs/linux/man/2-getppid/">getppid</a></b>(2) return the same value for all of the threads in a thread group. When a <b>CLONE_THREAD</b> thread terminates, the thread that created it is not sent a <b>SIGCHLD</b> (or other termination) signal; nor can the status of such a thread be obtained using <b><a HREF="/docs/linux/man/2-wait/">wait</a></b>(2). (The thread is said to be <i>detached</i>.)
<dt>
<dd> After all of the threads in a thread group terminate the parent process of the thread group is sent a <b>SIGCHLD</b> (or other termination) signal.
<dt>
<dd> If any of the threads in a thread group performs an <b><a HREF="/docs/linux/man/2-execve/">execve</a></b>(2), then all threads other than the thread group leader are terminated, and the new program is executed in the thread group leader.
<dt>
<dd> If one of the threads in a thread group creates a child using <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2), then any thread in the group can <b><a HREF="/docs/linux/man/2-wait/">wait</a></b>(2) for that child.
<dt>
<dd> Since Linux 2.5.35, the <i>flags</i> mask must also include <b>CLONE_SIGHAND</b> if <b>CLONE_THREAD</b> is specified (and note that, since Linux 2.6.0, <b>CLONE_SIGHAND</b> also requires <b>CLONE_VM</b> to be included).
<dt>
<dd> Signal dispositions and actions are process-wide: if an unhandled signal is delivered to a thread, then it will affect (terminate, stop, continue, be ignored in) all members of the thread group.
<dt>
<dd> Each thread has its own signal mask, as set by <b><a HREF="/docs/linux/man/2-sigprocmask/">sigprocmask</a></b>(2).
<dt>
<dd> A signal may be process-directed or thread-directed. A process-directed signal is targeted at a thread group (i.e., a TGID), and is delivered to an arbitrarily selected thread from among those that are not blocking the signal. A signal may be process-directed because it was generated by the kernel for reasons other than a hardware exception, or because it was sent using <b><a HREF="/docs/linux/man/2-kill/">kill</a></b>(2) or <b><a HREF="/docs/linux/man/3-sigqueue/">sigqueue</a></b>(3). A thread-directed signal is targeted at (i.e., delivered to) a specific thread. A signal may be thread directed because it was sent using <b><a HREF="/docs/linux/man/2-tgkill/">tgkill</a></b>(2) or <b><a HREF="/docs/linux/man/3-pthread_sigqueue/">pthread_sigqueue</a></b>(3), or because the thread executed a machine language instruction that triggered a hardware exception (e.g., invalid memory access triggering <b>SIGSEGV</b> or a floating-point exception triggering <b>SIGFPE</b>).
<dt>
<dd> A call to <b><a HREF="/docs/linux/man/2-sigpending/">sigpending</a></b>(2) returns a signal set that is the union of the pending process-directed signals and the signals that are pending for the calling thread.
<dt>
<dd> If a process-directed signal is delivered to a thread group, and the thread group has installed a handler for the signal, then the handler will be invoked in exactly one, arbitrarily selected member of the thread group that has not blocked the signal. If multiple threads in a group are waiting to accept the same signal using <b><a HREF="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></b>(2), the kernel will arbitrarily select one of these threads to receive the signal.
<dt><b>CLONE_UNTRACED</b> (since Linux 2.5.46)
<dd> If <b>CLONE_UNTRACED</b> is specified, then a tracing process cannot force <b>CLONE_PTRACE</b> on this child process.
<dt><b>CLONE_VFORK</b> (since Linux 2.2)
<dd> If <b>CLONE_VFORK</b> is set, the execution of the calling process is suspended until the child releases its virtual memory resources via a call to <b><a HREF="/docs/linux/man/2-execve/">execve</a></b>(2) or <b><a HREF="/docs/linux/man/2-_exit/">_exit</a></b>(2) (as with <b><a HREF="/docs/linux/man/2-vfork/">vfork</a></b>(2)).
<dt>
<dd> If <b>CLONE_VFORK</b> is not set, then both the calling process and the child are schedulable after the call, and an application should not rely on execution occurring in any particular order.
<dt><b>CLONE_VM</b> (since Linux 2.0)
<dd> If <b>CLONE_VM</b> is set, the calling process and the child process run in the same memory space. In particular, memory writes performed by the calling process or by the child process are also visible in the other process. Moreover, any memory mapping or unmapping performed with <b><a HREF="/docs/linux/man/2-mmap/">mmap</a></b>(2) or <b><a HREF="/docs/linux/man/2-munmap/">munmap</a></b>(2) by the child or calling process also affects the other process.
<dt>
<dd> If <b>CLONE_VM</b> is not set, the child process runs in a separate copy of the memory space of the calling process at the time of the clone call. Memory writes or file mappings/unmappings performed by one of the processes do not affect the other, as with <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2).
<dt>
<dd> If the <b>CLONE_VM</b> flag is specified and the <b>CLONE_VM</b> flag is not specified, then any alternate signal stack that was established by <b><a HREF="/docs/linux/man/2-sigaltstack/">sigaltstack</a></b>(2) is cleared in the child process.</dl>

<h2>RETURN VALUE</h2>

 On success, the thread ID of the child process is returned in the caller's thread of execution. On failure, -1 is returned in the caller's context, no child process will be created, and <i>errno</i> will be set appropriately.

<h2>ERRORS</h2>

<dl>
<dt><b>EAGAIN</b>
<dd> Too many processes are already running; see <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2).
<dt><b>EBUSY</b> (<b>clone3</b>() only)
<dd> <b>CLONE_INTO_CGROUP</b> was specified in <i>cl_args.flags</i>, but the file descriptor specified in <i>cl_args.cgroup</i> refers to a version 2 cgroup in which a domain controller is enabled.
<dt><b>EEXIST</b> (<b>clone3</b>() only)
<dd> One (or more) of the PIDs specified in <i>set_tid</i> already exists in the corresponding PID namespace.
<dt><b>EINVAL</b>
<dd> Both <b>CLONE_SIGHAND</b> and <b>CLONE_CLEAR_SIGHAND</b> were specified in the <i>flags</i> mask.
<dt><b>EINVAL</b>
<dd> <b>CLONE_SIGHAND</b> was specified in the <i>flags</i> mask, but <b>CLONE_VM</b> was not. (Since Linux 2.6.0.)
<dt><b>EINVAL</b>
<dd> <b>CLONE_THREAD</b> was specified in the <i>flags</i> mask, but <b>CLONE_SIGHAND</b> was not. (Since Linux 2.5.35.)
<dt><b>EINVAL</b>
<dd> <b>CLONE_THREAD</b> was specified in the <i>flags</i> mask, but the current process previously called <b><a HREF="/docs/linux/man/2-unshare/">unshare</a></b>(2) with the <b>CLONE_NEWPID</b> flag or used <b><a HREF="/docs/linux/man/2-setns/">setns</a></b>(2) to reassociate itself with a PID namespace.
<dt><b>EINVAL</b>
<dd> Both <b>CLONE_FS</b> and <b>CLONE_NEWNS</b> were specified in the <i>flags</i> mask.
<dt><b>EINVAL</b> (since Linux 3.9)
<dd> Both <b>CLONE_NEWUSER</b> and <b>CLONE_FS</b> were specified in the <i>flags</i> mask.
<dt><b>EINVAL</b>
<dd> Both <b>CLONE_NEWIPC</b> and <b>CLONE_SYSVSEM</b> were specified in the <i>flags</i> mask.
<dt><b>EINVAL</b>
<dd> One (or both) of <b>CLONE_NEWPID</b> or <b>CLONE_NEWUSER</b> and one (or both) of <b>CLONE_THREAD</b> or <b>CLONE_PARENT</b> were specified in the <i>flags</i> mask.
<dt><b>EINVAL</b> (since Linux 2.6.32)
<dd> <b>CLONE_PARENT</b> was specified, and the caller is an init process.
<dt><b>EINVAL</b>
<dd> Returned by the glibc <b>clone</b>() wrapper function when <i>fn</i> or <i>stack</i> is specified as NULL.
<dt><b>EINVAL</b>
<dd> <b>CLONE_NEWIPC</b> was specified in the <i>flags</i> mask, but the kernel was not configured with the <b>CONFIG_SYSVIPC</b> and <b>CONFIG_IPC_NS</b> options.
<dt><b>EINVAL</b>
<dd> <b>CLONE_NEWNET</b> was specified in the <i>flags</i> mask, but the kernel was not configured with the <b>CONFIG_NET_NS</b> option.
<dt><b>EINVAL</b>
<dd> <b>CLONE_NEWPID</b> was specified in the <i>flags</i> mask, but the kernel was not configured with the <b>CONFIG_PID_NS</b> option.
<dt><b>EINVAL</b>
<dd> <b>CLONE_NEWUSER</b> was specified in the <i>flags</i> mask, but the kernel was not configured with the <b>CONFIG_USER_NS</b> option.
<dt><b>EINVAL</b>
<dd> <b>CLONE_NEWUTS</b> was specified in the <i>flags</i> mask, but the kernel was not configured with the <b>CONFIG_UTS_NS</b> option.
<dt><b>EINVAL</b>
<dd> <i>stack</i> is not aligned to a suitable boundary for this architecture. For example, on aarch64, <i>stack</i> must be a multiple of 16.
<dt><b>EINVAL</b> (<b>clone3</b>() only)
<dd> <b>CLONE_DETACHED</b> was specified in the <i>flags</i> mask.
<dt><b>EINVAL</b> (<b>clone</b>() only)
<dd> <b>CLONE_PIDFD</b> was specified together with <b>CLONE_DETACHED</b> in the <i>flags</i> mask.
<dt><b>EINVAL</b>
<dd> <b>CLONE_PIDFD</b> was specified together with <b>CLONE_THREAD</b> in the <i>flags</i> mask.
<dt><b>EINVAL </b>(<b>clone</b>() only)
<dd> <b>CLONE_PIDFD</b> was specified together with <b>CLONE_PARENT_SETTID</b> in the <i>flags</i> mask.
<dt><b>EINVAL</b> (<b>clone3</b>() only)
<dd> <i>set_tid_size</i> is greater than the number of nested PID namespaces.
<dt><b>EINVAL</b> (<b>clone3</b>() only)
<dd> One of the PIDs specified in <i>set_tid</i> was an invalid.
<dt><b>EINVAL</b> (AArch64 only, Linux 4.6 and earlier)
<dd> <i>stack</i> was not aligned to a 126-bit boundary.
<dt><b>ENOMEM</b>
<dd> Cannot allocate sufficient memory to allocate a task structure for the child, or to copy those parts of the caller's context that need to be copied.
<dt><b>ENOSPC</b> (since Linux 3.7)
<dd> <b>CLONE_NEWPID</b> was specified in the <i>flags</i> mask, but the limit on the nesting depth of PID namespaces would have been exceeded; see <b><a HREF="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></b>(7).
<dt><b>ENOSPC</b> (since Linux 4.9; beforehand <b>EUSERS</b>)
<dd> <b>CLONE_NEWUSER</b> was specified in the <i>flags</i> mask, and the call would cause the limit on the number of nested user namespaces to be exceeded. See <b><a HREF="/docs/linux/man/7-user_namespaces/">user_namespaces</a></b>(7).
<dt>
<dd> From Linux 3.11 to Linux 4.8, the error diagnosed in this case was <b>EUSERS</b>.
<dt><b>ENOSPC</b> (since Linux 4.9)
<dd> One of the values in the <i>flags</i> mask specified the creation of a new user namespace, but doing so would have caused the limit defined by the corresponding file in <i>/proc/sys/user</i> to be exceeded. For further details, see <b><a HREF="/docs/linux/man/7-namespaces/">namespaces</a></b>(7).
<dt><b>EOPNOTSUPP</b> (<b>clone3</b>() only)
<dd> <b>CLONE_INTO_CGROUP</b> was specified in <i>cl_args.flags</i>, but the file descriptor specified in <i>cl_args.cgroup</i> refers to a version 2 cgroup that is in the <i>domain invalid</i> state.
<dt><b>EPERM</b>
<dd> <b>CLONE_NEWCGROUP</b>, <b>CLONE_NEWIPC</b>, <b>CLONE_NEWNET</b>, <b>CLONE_NEWNS</b>, <b>CLONE_NEWPID</b>, or <b>CLONE_NEWUTS</b> was specified by an unprivileged process (process without <b>CAP_SYS_ADMIN</b>).
<dt><b>EPERM</b>
<dd> <b>CLONE_PID</b> was specified by a process other than process 0. (This error occurs only on Linux 2.5.15 and earlier.)
<dt><b>EPERM</b>
<dd> <b>CLONE_NEWUSER</b> was specified in the <i>flags</i> mask, but either the effective user ID or the effective group ID of the caller does not have a mapping in the parent namespace (see <b><a HREF="/docs/linux/man/7-user_namespaces/">user_namespaces</a></b>(7)).
<dt><b>EPERM</b> (since Linux 3.9)
<dd> <b>CLONE_NEWUSER</b> was specified in the <i>flags</i> mask and the caller is in a chroot environment (i.e., the caller's root directory does not match the root directory of the mount namespace in which it resides).
<dt><b>EPERM</b> (<b>clone3</b>() only)
<dd> <i>set_tid_size</i> was greater than zero, and the caller lacks the <b>CAP_SYS_ADMIN</b> capability in one or more of the user namespaces that own the corresponding PID namespaces.
<dt><b>ERESTARTNOINTR</b> (since Linux 2.6.17)
<dd> System call was interrupted by a signal and will be restarted. (This can be seen only during a trace.)
<dt><b>EUSERS</b> (Linux 3.11 to Linux 4.8)
<dd> <b>CLONE_NEWUSER</b> was specified in the <i>flags</i> mask, and the limit on the number of nested user namespaces would be exceeded. See the discussion of the <b>ENOSPC</b> error above.</dl>

<h2>VERSIONS</h2>

 The <b>clone3</b>() system call first appeared in Linux 5.3.

<h2>CONFORMING TO</h2>

 These system calls are Linux-specific and should not be used in programs intended to be portable.

<h2>NOTES</h2>

 One use of these systems calls is to implement threads: multiple flows of control in a program that run concurrently in a shared address space. 

 Glibc does not provide a wrapper for <b>clone3</b>(); call it using <b><a HREF="/docs/linux/man/2-syscall/">syscall</a></b>(2). 

 Note that the glibc <b>clone</b>() wrapper function makes some changes in the memory pointed to by <i>stack</i> (changes required to set the stack up correctly for the child) <i>before</i> invoking the <b>clone</b>() system call. So, in cases where <b>clone</b>() is used to recursively create children, do not use the buffer employed for the parent's stack as the stack of the child. 

 The <b><a HREF="/docs/linux/man/2-kcmp/">kcmp</a></b>(2) system call can be used to test whether two processes share various resources such as a file descriptor table, System V semaphore undo operations, or a virtual address space. 

 Handlers registered using <b><a HREF="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></b>(3) are not executed during a clone call. 

 In the Linux 2.4.x series, <b>CLONE_THREAD</b> generally does not make the parent of the new thread the same as the parent of the calling process. However, for kernel versions 2.4.7 to 2.4.18 the <b>CLONE_THREAD</b> flag implied the <b>CLONE_PARENT</b> flag (as in Linux 2.6.0 and later). 

 On i386, <b>clone</b>() should not be called through vsyscall, but directly through <i>int $0x80</i>.

<h3>C library/kernel differences</h3>

 The raw <b>clone</b>() system call corresponds more closely to <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2) in that execution in the child continues from the point of the call. As such, the <i>fn</i> and <i>arg</i> arguments of the <b>clone</b>() wrapper function are omitted. 

 In contrast to the glibc wrapper, the raw <b>clone</b>() system call accepts NULL as a <i>stack</i> argument (and <b>clone3</b>() likewise allows <i>cl_args.stack</i> to be NULL). In this case, the child uses a duplicate of the parent's stack. (Copy-on-write semantics ensure that the child gets separate copies of stack pages when either process modifies the stack.) In this case, for correct operation, the <b>CLONE_VM</b> option should not be specified. (If the child <i>shares</i> the parent's memory because of the use of the <b>CLONE_VM</b> flag, then no copy-on-write duplication occurs and chaos is likely to result.) 

 The order of the arguments also differs in the raw system call, and there are variations in the arguments across architectures, as detailed in the following paragraphs. 

 The raw system call interface on x86-64 and some other architectures (including sh, tile, and alpha) is: 

 <b>long clone(unsigned long </b><i>flags</i><b>, void *</b><i>stack</i><b>,</b> <b> int *</b><i>parent_tid</i><b>, int *</b><i>child_tid</i><b>,</b> <b> unsigned long </b><i>tls</i><b>);</b> 

 On x86-32, and several other common architectures (including score, ARM, ARM 64, PA-RISC, arc, Power PC, xtensa, and MIPS), the order of the last two arguments is reversed: 

 <b>long clone(unsigned long </b><i>flags</i><b>, void *</b><i>stack</i><b>,</b> <b> int *</b><i>parent_tid</i><b>, unsigned long </b><i>tls</i><b>,</b> <b> int *</b><i>child_tid</i><b>);</b> 

 On the cris and s390 architectures, the order of the first two arguments is reversed: 

 <b>long clone(void *</b><i>stack</i><b>, unsigned long </b><i>flags</i><b>,</b> <b> int *</b><i>parent_tid</i><b>, int *</b><i>child_tid</i><b>,</b> <b> unsigned long </b><i>tls</i><b>);</b> 

 On the microblaze architecture, an additional argument is supplied: 

 <b>long clone(unsigned long </b><i>flags</i><b>, void *</b><i>stack</i><b>,</b> <b> int </b><i>stack_size</i><b>,</b><i></i> /* Size of stack */ <b> int *</b><i>parent_tid</i><b>, int *</b><i>child_tid</i><b>,</b> <b> unsigned long </b><i>tls</i><b>);</b>

<h3>blackfin, m68k, and sparc</h3>

 The argument-passing conventions on blackfin, m68k, and sparc are different from the descriptions above. For details, see the kernel (and glibc) source.

<h3>ia64</h3>

 On ia64, a different interface is used: 

 <b>int __clone2(int (*</b><i>fn</i><b>)(void *),</b> <b> void *</b><i>stack_base</i><b>, size_t </b><i>stack_size</i><b>,</b> <b> int </b><i>flags</i><b>, void *</b><i>arg</i><b>, ...</b> <b> /* pid_t *</b><i>parent_tid</i><b>, struct user_desc *</b><i>tls</i><b>,</b> <b> pid_t *</b><i>child_tid</i><b> */ );</b> 

 The prototype shown above is for the glibc wrapper function; for the system call itself, the prototype can be described as follows (it is identical to the <b>clone</b>() prototype on microblaze): 

 <b>long clone2(unsigned long </b><i>flags</i><b>, void *</b><i>stack_base</i><b>,</b> <b> int </b><i>stack_size</i><b>,</b><i></i> /* Size of stack */ <b> int *</b><i>parent_tid</i><b>, int *</b><i>child_tid</i><b>,</b> <b> unsigned long </b><i>tls</i><b>);</b> 

 <b>__clone2</b>() operates in the same way as <b>clone</b>(), except that <i>stack_base</i> points to the lowest address of the child's stack area, and <i>stack_size</i> specifies the size of the stack pointed to by <i>stack_base</i>.

<h3>Linux 2.4 and earlier</h3>

 In Linux 2.4 and earlier, <b>clone</b>() does not take arguments <i>parent_tid</i>, <i>tls</i>, and <i>child_tid</i>.

<h2>BUGS</h2>

 GNU C library versions 2.3.4 up to and including 2.24 contained a wrapper function for <b><a HREF="/docs/linux/man/2-getpid/">getpid</a></b>(2) that performed caching of PIDs. This caching relied on support in the glibc wrapper for <b>clone</b>(), but limitations in the implementation meant that the cache was not up to date in some circumstances. In particular, if a signal was delivered to the child immediately after the <b>clone</b>() call, then a call to <b><a HREF="/docs/linux/man/2-getpid/">getpid</a></b>(2) in a handler for the signal could return the PID of the calling process (&quot;the parent&quot;), if the clone wrapper had not yet had a chance to update the PID cache in the child. (This discussion ignores the case where the child was created using <b>CLONE_THREAD</b>, when <b><a HREF="/docs/linux/man/2-getpid/">getpid</a></b>(2) <i>should</i> return the same value in the child and in the process that called <b>clone</b>(), since the caller and the child are in the same thread group. The stale-cache problem also does not occur if the <i>flags</i> argument includes <b>CLONE_VM</b>.) To get the truth, it was sometimes necessary to use code such as the following: 

 #include &lt;syscall.h&gt; 

 pid_t mypid; 

 mypid = syscall(SYS_getpid); 

 Because of the stale-cache problem, as well as other problems noted in <b><a HREF="/docs/linux/man/2-getpid/">getpid</a></b>(2), the PID caching feature was removed in glibc 2.25.

<h2>EXAMPLES</h2>

 The following program demonstrates the use of <b>clone</b>() to create a child process that executes in a separate UTS namespace. The child changes the hostname in its UTS namespace. Both parent and child then display the system hostname, making it possible to see that the hostname differs in the UTS namespaces of the parent and child. For an example of the use of this program, see <b><a HREF="/docs/linux/man/2-setns/">setns</a></b>(2). 

 Within the sample program, we allocate the memory that is to be used for the child's stack using <b><a HREF="/docs/linux/man/2-mmap/">mmap</a></b>(2) rather than <b><a HREF="/docs/linux/man/3-malloc/">malloc</a></b>(3) for the following reasons:
<dl>
<dt>*
<dd> <b><a HREF="/docs/linux/man/2-mmap/">mmap</a></b>(2) allocates a block of memory that starts on a page boundary and is a multiple of the page size. This is useful if we want to establish a guard page (a page with protection <b>PROT_NONE</b>) at the end of the stack using <b><a HREF="/docs/linux/man/2-mprotect/">mprotect</a></b>(2).
<dt>*
<dd> We can specify the <b>MAP_STACK</b> flag to request a mapping that is suitable for a stack. For the moment, this flag is a no-op on Linux, but it exists and has effect on some other systems, so we should include it for portability.</dl>

<h3>Program source</h3>

 #define _GNU_SOURCE #include &lt;sys/wait.h&gt; #include &lt;sys/utsname.h&gt; #include &lt;sched.h&gt; #include &lt;string.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;sys/mman.h&gt; 

 #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) 

 static int /* Start function for cloned child */ childFunc(void *arg) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct utsname uts; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Change hostname in UTS namespace of child&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sethostname(arg, strlen(arg))&nbsp;==&nbsp;-1) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;sethostname&quot;); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Retrieve and display hostname&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(uname(&amp;uts)&nbsp;==&nbsp;-1) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;uname&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;uts.nodename in child:&nbsp;<wbr>&nbsp;%s\n&quot;, uts.nodename); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Keep the namespace open for a while, by sleeping. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This allows some experimentation--for example, another 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;process might join the namespace.&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sleep(200); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Child terminates now&nbsp;*/ } 

 #define STACK_SIZE (1024 * 1024) /* Stack size for cloned child */ 

 int main(int argc, char *argv[]) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*stack;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Start of stack buffer&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*stackTop;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;End of stack buffer&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t pid; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct utsname uts; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;child-hostname&gt;\n&quot;, argv[0]); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Allocate memory to be used for the stack of the child&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stack&nbsp;=&nbsp;mmap(NULL, STACK_SIZE, PROT_READ | PROT_WRITE, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MAP_PRIVATE | MAP_ANONYMOUS | MAP_STACK, -1, 0); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(stack&nbsp;==&nbsp;MAP_FAILED) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mmap&quot;); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stackTop&nbsp;=&nbsp;stack&nbsp;+&nbsp;STACK_SIZE;&nbsp;<wbr>&nbsp;/*&nbsp;Assume stack grows downward&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create child that has its own UTS namespace; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;child commences execution in childFunc()&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid&nbsp;=&nbsp;clone(childFunc, stackTop, CLONE_NEWUTS | SIGCHLD, argv[1]); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pid&nbsp;==&nbsp;-1) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;clone&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;clone()&nbsp;returned&nbsp;%jd\n&quot;,&nbsp;(intmax_t)&nbsp;pid); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Parent falls through to here&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a HREF="/docs/linux/man/1-sleep/">sleep</a>(1);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Give child time to change its hostname&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display hostname in parent's UTS namespace. This will be 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;different from hostname in child's UTS namespace.&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(uname(&amp;uts)&nbsp;==&nbsp;-1) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;uname&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;uts.nodename in parent:&nbsp;%s\n&quot;, uts.nodename); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(waitpid(pid, NULL, 0)&nbsp;==&nbsp;-1)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for child&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;waitpid&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;child has terminated\n&quot;); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/2-fork/">fork</a></b>(2), <b><a HREF="/docs/linux/man/2-futex/">futex</a></b>(2), <b><a HREF="/docs/linux/man/2-getpid/">getpid</a></b>(2), <b><a HREF="/docs/linux/man/2-gettid/">gettid</a></b>(2), <b><a HREF="/docs/linux/man/2-kcmp/">kcmp</a></b>(2), <b><a HREF="/docs/linux/man/2-mmap/">mmap</a></b>(2), <b><a HREF="/docs/linux/man/2-pidfd_open/">pidfd_open</a></b>(2), <b><a HREF="/docs/linux/man/2-set_thread_area/">set_thread_area</a></b>(2), <b><a HREF="/docs/linux/man/2-set_tid_address/">set_tid_address</a></b>(2), <b><a HREF="/docs/linux/man/2-setns/">setns</a></b>(2), <b><a HREF="/docs/linux/man/2-tkill/">tkill</a></b>(2), <b><a HREF="/docs/linux/man/2-unshare/">unshare</a></b>(2), <b><a HREF="/docs/linux/man/2-wait/">wait</a></b>(2), <b><a HREF="/docs/linux/man/7-capabilities/">capabilities</a></b>(7), <b><a HREF="/docs/linux/man/7-namespaces/">namespaces</a></b>(7), <b><a HREF="/docs/linux/man/7-pthreads/">pthreads</a></b>(7)

<h2>COLOPHON</h2>

 This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 

<h2>Index</h2>


