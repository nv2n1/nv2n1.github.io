---
title: "clone(2)"
name: "clone"
section: "2"
letter: "c"
url: "/docs/linux/man/2-clone/"
description: "clone, __clone2, clone3 – create a child process"
---

<h2 class="name">NAME</h2>
<p> clone, __clone2, clone3 &#8211; create a child process </p>
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
<p> <i>Note</i>: There is not yet a glibc wrapper for <code>clone3</code>(); see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> These system calls create a new (&quot;child&quot;) process, in a manner similar to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). </p>
<p> By contrast with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), these system calls provide more precise control over what pieces of execution context are shared between the calling process and the child process. For example, using these system calls, the caller can control whether or not the two processes share the virtual address space, the table of file descriptors, and the table of signal handlers. These system calls also allow the new child process to be placed in separate <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7). </p>
<p> Note that in this manual page, &quot;calling process&quot; normally corresponds to &quot;parent process&quot;. But see the descriptions of <code>CLONE_PARENT</code> and <code>CLONE_THREAD</code> below. </p>
<p> This page describes the following interfaces:</p>
<dl>
<dt>*</p>
<dd> The glibc <code>clone</code>() wrapper function and the underlying system call on which it is based. The main text describes the wrapper function; the differences for the raw system call are described toward the end of this page.</p>
<dt>*</p>
<dd> The newer <code>clone3</code>() system call.</dl>
<p> In the remainder of this page, the terminology &quot;the clone call&quot; is used when noting details that apply to all of these interfaces,</p>
<h3>The clone() wrapper function</h3>
<p> When the child process is created with the <code>clone</code>() wrapper function, it commences execution by calling the function pointed to by the argument <i>fn</i>. (This differs from <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), where execution continues in the child from the point of the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) call.) The <i>arg</i> argument is passed as the argument of the function <i>fn</i>. </p>
<p> When the <i>fn</i>(<i>arg</i>) function returns, the child process terminates. The integer returned by <i>fn</i> is the exit status for the child process. The child process may also terminate explicitly by calling <code><a href="/docs/linux/man/2-exit/">exit</a></code>(2) or after receiving a fatal signal. </p>
<p> The <i>stack</i> argument specifies the location of the stack used by the child process. Since the child and calling process may share memory, it is not possible for the child process to execute in the same stack as the calling process. The calling process must therefore set up memory space for the child stack and pass a pointer to this space to <code>clone</code>(). Stacks grow downward on all processors that run Linux (except the HP PA processors), so <i>stack</i> usually points to the topmost address of the memory space set up for the child stack. Note that <code>clone</code>() does not provide a means whereby the caller can inform the kernel of the size of the stack area. </p>
<p> The remaining arguments to <code>clone</code>() are discussed below.</p>
<h3>clone3()</h3>
<p> The <code>clone3</code>() system call provides a superset of the functionality of the older <code>clone</code>() interface. It also provides a number of API improvements, including: space for additional flags bits; cleaner separation in the use of various arguments; and the ability to specify the size of the child&#8217;s stack area. </p>
<p> As with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code>clone3</code>() returns in both the parent and the child. It returns 0 in the child process and returns the PID of the child in the parent. </p>
<p> The <i>cl_args</i> argument of <code>clone3</code>() is a structure of the following form: </p>
<p> struct clone_args {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags bit mask&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 pidfd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Where to store PID file descriptor<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(<i>pid_t&nbsp;*</i>)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 child_tid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Where to store child TID,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in child&#8217;s memory&nbsp;(<i>pid_t&nbsp;*</i>)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 parent_tid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Where to store child TID,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in parent&#8217;s memory&nbsp;(<i>int&nbsp;*</i>)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 exit_signal;&nbsp;<wbr>&nbsp;/*&nbsp;Signal to deliver to parent on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;child termination&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 stack;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pointer to lowest byte of stack&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 stack_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of stack&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 tls;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Location of new TLS&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 set_tid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pointer to a&nbsp;<i>pid_t</i>&nbsp;array<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 5.5)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 set_tid_size;&nbsp;/*&nbsp;Number of elements in&nbsp;<i>set_tid</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 5.5)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 cgroup;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File descriptor for target cgroup<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of child&nbsp;(since Linux 5.7)&nbsp;*/ }; </p>
<p> The <i>size</i> argument that is supplied to <code>clone3</code>() should be initialized to the size of this structure. (The existence of the <i>size</i> argument permits future extensions to the <i>clone_args</i> structure.) </p>
<p> The stack for the child process is specified via <i>cl_args.stack</i>, which points to the lowest byte of the stack area, and <i>cl_args.stack_size</i>, which specifies the size of the stack in bytes. In the case where the <code>CLONE_VM</code> flag (see below) is specified, a stack must be explicitly allocated and specified. Otherwise, these two fields can be specified as NULL and 0, which causes the child to use the same stack area as the parent (in the child&#8217;s own virtual address space). </p>
<p> The remaining fields in the <i>cl_args</i> argument are discussed below.</p>
<h3>Equivalence between clone() and clone3() arguments</h3>
<p> Unlike the older <code>clone</code>() interface, where arguments are passed individually, in the newer <code>clone3</code>() interface the arguments are packaged into the <i>clone_args</i> structure shown above. This structure allows for a superset of the information passed via the <code>clone</code>() arguments. </p>
<p> The following table shows the equivalence between the arguments of <code>clone</code>() and the fields in the <i>clone_args</i> argument supplied to <code>clone3</code>():</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><code>clone()</code></td>
<td><code>clone3()</code></td>
<td><code>Notes</code>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><i>cl_args</i> field</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>flags &amp; ~0xff</i></td>
<td><i>flags</i></td>
<td>For most flags; details below
</td>
</tr>
<tr VALIGN=top>
<td><i>parent_tid</i></td>
<td><i>pidfd</i></td>
<td>See CLONE_PIDFD
</td>
</tr>
<tr VALIGN=top>
<td><i>child_tid</i></td>
<td><i>child_tid</i></td>
<td>See CLONE_CHILD_SETTID
</td>
</tr>
<tr VALIGN=top>
<td><i>parent_tid</i></td>
<td><i>parent_tid</i></td>
<td>See CLONE_PARENT_SETTID
</td>
</tr>
<tr VALIGN=top>
<td><i>flags &amp; 0xff</i></td>
<td><i>exit_signal</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>stack</i></td>
<td><i>stack</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>&#8212;</i></td>
<td><i>stack_size</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>tls</i></td>
<td><i>tls</i></td>
<td>See CLONE_SETTLS
</td>
</tr>
<tr VALIGN=top>
<td><i>&#8212;</i></td>
<td><i>set_tid</i></td>
<td>See below for details
</td>
</tr>
<tr VALIGN=top>
<td><i>&#8212;</i></td>
<td><i>set_tid_size</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>&#8212;</i></td>
<td><i>cgroup</i></td>
<td>See CLONE_INTO_CGROUP
</td>
</tr>
</table>
</dl>
<h3>The child termination signal</h3>
<p> When the child process terminates, a signal may be sent to the parent. The termination signal is specified in the low byte of <i>flags</i> (<code>clone</code>()) or in <i>cl_args.exit_signal</i> (<code>clone3</code>()). If this signal is specified as anything other than <code>SIGCHLD</code>, then the parent process must specify the <code>__WALL</code> or <code>__WCLONE</code> options when waiting for the child with <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2). If no signal (i.e., zero) is specified, then the parent process is not signaled when the child terminates.</p>
<h3>The set_tid array</h3>
<p> By default, the kernel chooses the next sequential PID for the new process in each of the PID namespaces where it is present. When creating a process with <code>clone3</code>(), the <i>set_tid</i> array (available since Linux 5.5) can be used to select specific PIDs for the process in some or all of the PID namespaces where it is present. If the PID of the newly created process should be set only for the current PID namespace or in the newly created PID namespace (if <i>flags</i> contains <code>CLONE_NEWPID</code>) then the first element in the <i>set_tid</i> array has to be the desired PID and <i>set_tid_size</i> needs to be 1. </p>
<p> If the PID of the newly created process should have a certain value in multiple PID namespaces, then the <i>set_tid</i> array can have multiple entries. The first entry defines the PID in the most deeply nested PID namespace and each of the following entries contains the PID in the corresponding ancestor PID namespace. The number of PID namespaces in which a PID should be set is defined by <i>set_tid_size</i> which cannot be larger than the number of currently nested PID namespaces. </p>
<p> To create a process with the following PIDs in a PID namespace hierarchy:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><code>PID NS level</code></td>
<td><code>Requested PID</code></td>
<td><code>Notes</code>
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>31496</td>
<td>Outermost PID namespace
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>42</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>7</td>
<td>Innermost PID namespace
</td>
</tr>
</table>
</dl>
<p> Set the array to: </p>
<p> set_tid[0] = 7; set_tid[1] = 42; set_tid[2] = 31496; set_tid_size = 3; </p>
<p> If only the PIDs in the two innermost PID namespaces need to be specified, set the array to: </p>
<p> set_tid[0] = 7; set_tid[1] = 42; set_tid_size = 2; </p>
<p> The PID in the PID namespaces outside the two innermost PID namespaces will be selected the same way as any other PID is selected. </p>
<p> The <i>set_tid</i> feature requires <code>CAP_SYS_ADMIN</code> or (since Linux 5.9) <code>CAP_CHECKPOINT_RESTORE</code> in all owning user namespaces of the target PID namespaces. </p>
<p> Callers may only choose a PID greater than 1 in a given PID namespace if an <code>init</code> process (i.e., a process with PID 1) already exists in that namespace. Otherwise the PID entry for this PID namespace must be 1.</p>
<h3>The flags mask</h3>
<p> Both <code>clone</code>() and <code>clone3</code>() allow a flags bit mask that modifies their behavior and allows the caller to specify what is shared between the calling process and the child process. This bit mask&#8212;the <i>flags</i> argument of <code>clone</code>() or the <i>cl_args.flags</i> field passed to <code>clone3</code>()&#8212;is referred to as the <i>flags</i> mask in the remainder of this page. </p>
<p> The <i>flags</i> mask is specified as a bitwise-OR of zero or more of the constants listed below. Except as noted below, these flags are available (and have the same effect) in both <code>clone</code>() and <code>clone3</code>().</p>
<dl>
<dt><code>CLONE_CHILD_CLEARTID</code> (since Linux 2.5.49)</p>
<dd> Clear (zero) the child thread ID at the location pointed to by <i>child_tid</i> (<code>clone</code>()) or <i>cl_args.child_tid</i> (<code>clone3</code>()) in child memory when the child exits, and do a wakeup on the futex at that address. The address involved may be changed by the <code><a href="/docs/linux/man/2-set_tid_address/">set_tid_address</a></code>(2) system call. This is used by threading libraries.</p>
<dt><code>CLONE_CHILD_SETTID</code> (since Linux 2.5.49)</p>
<dd> Store the child thread ID at the location pointed to by <i>child_tid</i> (<code>clone</code>()) or <i>cl_args.child_tid</i> (<code>clone3</code>()) in the child&#8217;s memory. The store operation completes before the clone call returns control to user space in the child process. (Note that the store operation may not have completed before the clone call returns in the parent process, which will be relevant if the <code>CLONE_VM</code> flag is also employed.)</p>
<dt><code>CLONE_CLEAR_SIGHAND</code> (since Linux 5.5)</p>
<dd> By default, signal dispositions in the child thread are the same as in the parent. If this flag is specified, then all signals that are handled in the parent are reset to their default dispositions (<code>SIG_DFL</code>) in the child.</p>
<dt>
<dd> Specifying this flag together with <code>CLONE_SIGHAND</code> is nonsensical and disallowed.</p>
<dt><code>CLONE_DETACHED</code> (historical)</p>
<dd> For a while (during the Linux 2.5 development series) there was a <code>CLONE_DETACHED</code> flag, which caused the parent not to receive a signal when the child terminated. Ultimately, the effect of this flag was subsumed under the <code>CLONE_THREAD</code> flag and by the time Linux 2.6.0 was released, this flag had no effect. Starting in Linux 2.6.2, the need to give this flag together with <code>CLONE_THREAD</code> disappeared.</p>
<dt>
<dd> This flag is still defined, but it is usually ignored when calling <code>clone</code>(). However, see the description of <code>CLONE_PIDFD</code> for some exceptions.</p>
<dt><code>CLONE_FILES</code> (since Linux 2.0)</p>
<dd> If <code>CLONE_FILES</code> is set, the calling process and the child process share the same file descriptor table. Any file descriptor created by the calling process or by the child process is also valid in the other process. Similarly, if one of the processes closes a file descriptor, or changes its associated flags (using the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETFD</code> operation), the other process is also affected. If a process sharing a file descriptor table calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), its file descriptor table is duplicated (unshared).</p>
<dt>
<dd> If <code>CLONE_FILES</code> is not set, the child process inherits a copy of all file descriptors opened in the calling process at the time of the clone call. Subsequent operations that open or close file descriptors, or change file descriptor flags, performed by either the calling process or the child process do not affect the other process. Note, however, that the duplicated file descriptors in the child refer to the same open file descriptions as the corresponding file descriptors in the calling process, and thus share file offsets and file status flags (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)).</p>
<dt><code>CLONE_FS</code> (since Linux 2.0)</p>
<dd> If <code>CLONE_FS</code> is set, the caller and the child process share the same filesystem information. This includes the root of the filesystem, the current working directory, and the umask. Any call to <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2), or <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) performed by the calling process or the child process also affects the other process.</p>
<dt>
<dd> If <code>CLONE_FS</code> is not set, the child process works on a copy of the filesystem information of the calling process at the time of the clone call. Calls to <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2), or <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) performed later by one of the processes do not affect the other process.</p>
<dt><code>CLONE_INTO_CGROUP</code> (since Linux 5.7)</p>
<dd> By default, a child process is placed in the same version 2 cgroup as its parent. The <code>CLONE_INTO_CGROUP</code> flag allows the child process to be created in a different version 2 cgroup. (Note that <code>CLONE_INTO_CGROUP</code> has effect only for version 2 cgroups.)</p>
<dt>
<dd> In order to place the child process in a different cgroup, the caller specifies <code>CLONE_INTO_CGROUP</code> in <i>cl_args.flags</i> and passes a file descriptor that refers to a version 2 cgroup in the <i>cl_args.cgroup</i> field. (This file descriptor can be obtained by opening a cgroup v2 directory using either the <code>O_RDONLY</code> or the <code>O_PATH</code> flag.) Note that all of the usual restrictions (described in <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7)) on placing a process into a version 2 cgroup apply.</p>
<dt>
<dd> Among the possible use cases for <code>CLONE_INTO_CGROUP</code> are the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Spawning a process into a cgroup different from the parent&#8217;s cgroup makes it possible for a service manager to directly spawn new services into dedicated cgroups. This eliminates the accounting jitter that would be caused if the child process was first created in the same cgroup as the parent and then moved into the target cgroup. Furthermore, spawning the child process directly into a target cgroup is significantly cheaper than moving the child process into the target cgroup after it has been created.</p>
<dt>*</p>
<dd> The <code>CLONE_INTO_CGROUP</code> flag also allows the creation of frozen child processes by spawning them into a frozen cgroup. (See <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7) for a description of the freezer controller.)</p>
<dt>*</p>
<dd> For threaded applications (or even thread implementations which make use of cgroups to limit individual threads), it is possible to establish a fixed cgroup layout before spawning each thread directly into its target cgroup.</dl>
</dl>
<dt><code>CLONE_IO</code> (since Linux 2.6.25)</p>
<dd> If <code>CLONE_IO</code> is set, then the new process shares an I/O context with the calling process. If this flag is not set, then (as with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)) the new process has its own I/O context.</p>
<dt>
<dd> The I/O context is the I/O scope of the disk scheduler (i.e., what the I/O scheduler uses to model scheduling of a process&#8217;s I/O). If processes share the same I/O context, they are treated as one by the I/O scheduler. As a consequence, they get to share disk time. For some I/O schedulers, if two processes share an I/O context, they will be allowed to interleave their disk access. If several threads are doing I/O on behalf of the same process (<code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), for instance), they should employ <code>CLONE_IO</code> to get better I/O performance.</p>
<dt>
<dd> If the kernel is not configured with the <code>CONFIG_BLOCK</code> option, this flag is a no-op.</p>
<dt><code>CLONE_NEWCGROUP</code> (since Linux 4.6)</p>
<dd> Create the process in a new cgroup namespace. If this flag is not set, then (as with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)) the process is created in the same cgroup namespaces as the calling process.</p>
<dt>
<dd> For further information on cgroup namespaces, see <code><a href="/docs/linux/man/7-cgroup_namespaces/">cgroup_namespaces</a></code>(7).</p>
<dt>
<dd> Only a privileged process (<code>CAP_SYS_ADMIN</code>) can employ <code>CLONE_NEWCGROUP</code>.</p>
<dt><code>CLONE_NEWIPC</code> (since Linux 2.6.19)</p>
<dd> If <code>CLONE_NEWIPC</code> is set, then create the process in a new IPC namespace. If this flag is not set, then (as with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)), the process is created in the same IPC namespace as the calling process.</p>
<dt>
<dd> For further information on IPC namespaces, see <code><a href="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></code>(7).</p>
<dt>
<dd> Only a privileged process (<code>CAP_SYS_ADMIN</code>) can employ <code>CLONE_NEWIPC</code>. This flag can&#8217;t be specified in conjunction with <code>CLONE_SYSVSEM</code>.</p>
<dt><code>CLONE_NEWNET</code> (since Linux 2.6.24)</p>
<dd> (The implementation of this flag was completed only by about kernel version 2.6.29.)</p>
<dt>
<dd> If <code>CLONE_NEWNET</code> is set, then create the process in a new network namespace. If this flag is not set, then (as with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)) the process is created in the same network namespace as the calling process.</p>
<dt>
<dd> For further information on network namespaces, see <code><a href="/docs/linux/man/7-network_namespaces/">network_namespaces</a></code>(7).</p>
<dt>
<dd> Only a privileged process (<code>CAP_SYS_ADMIN</code>) can employ <code>CLONE_NEWNET</code>.</p>
<dt><code>CLONE_NEWNS</code> (since Linux 2.4.19)</p>
<dd> If <code>CLONE_NEWNS</code> is set, the cloned child is started in a new mount namespace, initialized with a copy of the namespace of the parent. If <code>CLONE_NEWNS</code> is not set, the child lives in the same mount namespace as the parent.</p>
<dt>
<dd> For further information on mount namespaces, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7) and <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7).</p>
<dt>
<dd> Only a privileged process (<code>CAP_SYS_ADMIN</code>) can employ <code>CLONE_NEWNS</code>. It is not permitted to specify both <code>CLONE_NEWNS</code> and <code>CLONE_FS</code> in the same clone call.</p>
<dt><code>CLONE_NEWPID</code> (since Linux 2.6.24)</p>
<dd> If <code>CLONE_NEWPID</code> is set, then create the process in a new PID namespace. If this flag is not set, then (as with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)) the process is created in the same PID namespace as the calling process.</p>
<dt>
<dd> For further information on PID namespaces, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7) and <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7).</p>
<dt>
<dd> Only a privileged process (<code>CAP_SYS_ADMIN</code>) can employ <code>CLONE_NEWPID</code>. This flag can&#8217;t be specified in conjunction with <code>CLONE_THREAD</code> or <code>CLONE_PARENT</code>.</p>
<dt><code>CLONE_NEWUSER</code></p>
<dd> (This flag first became meaningful for <code>clone</code>() in Linux 2.6.23, the current <code>clone</code>() semantics were merged in Linux 3.5, and the final pieces to make the user namespaces completely usable were merged in Linux 3.8.)</p>
<dt>
<dd> If <code>CLONE_NEWUSER</code> is set, then create the process in a new user namespace. If this flag is not set, then (as with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)) the process is created in the same user namespace as the calling process.</p>
<dt>
<dd> For further information on user namespaces, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7) and <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</p>
<dt>
<dd> Before Linux 3.8, use of <code>CLONE_NEWUSER</code> required that the caller have three capabilities: <code>CAP_SYS_ADMIN</code>, <code>CAP_SETUID</code>, and <code>CAP_SETGID</code>. Starting with Linux 3.8, no privileges are needed to create a user namespace.</p>
<dt>
<dd> This flag can&#8217;t be specified in conjunction with <code>CLONE_THREAD</code> or <code>CLONE_PARENT</code>. For security reasons, <code>CLONE_NEWUSER</code> cannot be specified in conjunction with <code>CLONE_FS</code>.</p>
<dt><code>CLONE_NEWUTS</code> (since Linux 2.6.19)</p>
<dd> If <code>CLONE_NEWUTS</code> is set, then create the process in a new UTS namespace, whose identifiers are initialized by duplicating the identifiers from the UTS namespace of the calling process. If this flag is not set, then (as with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)) the process is created in the same UTS namespace as the calling process.</p>
<dt>
<dd> For further information on UTS namespaces, see <code><a href="/docs/linux/man/7-uts_namespaces/">uts_namespaces</a></code>(7).</p>
<dt>
<dd> Only a privileged process (<code>CAP_SYS_ADMIN</code>) can employ <code>CLONE_NEWUTS</code>.</p>
<dt><code>CLONE_PARENT</code> (since Linux 2.3.12)</p>
<dd> If <code>CLONE_PARENT</code> is set, then the parent of the new child (as returned by <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2)) will be the same as that of the calling process.</p>
<dt>
<dd> If <code>CLONE_PARENT</code> is not set, then (as with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)) the child&#8217;s parent is the calling process.</p>
<dt>
<dd> Note that it is the parent process, as returned by <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2), which is signaled when the child terminates, so that if <code>CLONE_PARENT</code> is set, then the parent of the calling process, rather than the calling process itself, will be signaled.</p>
<dt>
<dd> The <code>CLONE_PARENT</code> flag can&#8217;t be used in clone calls by the global init process (PID 1 in the initial PID namespace) and init processes in other PID namespaces. This restriction prevents the creation of multi-rooted process trees as well as the creation of unreapable zombies in the initial PID namespace.</p>
<dt><code>CLONE_PARENT_SETTID</code> (since Linux 2.5.49)</p>
<dd> Store the child thread ID at the location pointed to by <i>parent_tid</i> (<code>clone</code>()) or <i>cl_args.parent_tid</i> (<code>clone3</code>()) in the parent&#8217;s memory. (In Linux 2.5.32-2.5.48 there was a flag <code>CLONE_SETTID</code> that did this.) The store operation completes before the clone call returns control to user space.</p>
<dt><code>CLONE_PID</code> (Linux 2.0 to 2.5.15)</p>
<dd> If <code>CLONE_PID</code> is set, the child process is created with the same process ID as the calling process. This is good for hacking the system, but otherwise of not much use. From Linux 2.3.21 onward, this flag could be specified only by the system boot process (PID 0). The flag disappeared completely from the kernel sources in Linux 2.5.16. Subsequently, the kernel silently ignored this bit if it was specified in the <i>flags</i> mask. Much later, the same bit was recycled for use as the <code>CLONE_PIDFD</code> flag.</p>
<dt><code>CLONE_PIDFD</code> (since Linux 5.2)</p>
<dd> If this flag is specified, a PID file descriptor referring to the child process is allocated and placed at a specified location in the parent&#8217;s memory. The close-on-exec flag is set on this new file descriptor. PID file descriptors can be used for the purposes described in <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2).</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> When using <code>clone3</code>(), the PID file descriptor is placed at the location pointed to by <i>cl_args.pidfd</i>.</p>
<dt>*</p>
<dd> When using <code>clone</code>(), the PID file descriptor is placed at the location pointed to by <i>parent_tid</i>. Since the <i>parent_tid</i> argument is used to return the PID file descriptor, <code>CLONE_PIDFD</code> cannot be used with <code>CLONE_PARENT_SETTID</code> when calling <code>clone</code>().</dl>
</dl>
<dt>
<dd> It is currently not possible to use this flag together with <code>CLONE_THREAD.</code> This means that the process identified by the PID file descriptor will always be a thread group leader.</p>
<dt>
<dd> If the obsolete <code>CLONE_DETACHED</code> flag is specified alongside <code>CLONE_PIDFD</code> when calling <code>clone</code>(), an error is returned. An error also results if <code>CLONE_DETACHED</code> is specified when calling <code>clone3</code>(). This error behavior ensures that the bit corresponding to <code>CLONE_DETACHED</code> can be reused for further PID file descriptor features in the future.</p>
<dt><code>CLONE_PTRACE</code> (since Linux 2.2)</p>
<dd> If <code>CLONE_PTRACE</code> is specified, and the calling process is being traced, then trace the child also (see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)).</p>
<dt><code>CLONE_SETTLS</code> (since Linux 2.5.32)</p>
<dd> The TLS (Thread Local Storage) descriptor is set to <i>tls</i>.</p>
<dt>
<dd> The interpretation of <i>tls</i> and the resulting effect is architecture dependent. On x86, <i>tls</i> is interpreted as a <i>struct user_desc&nbsp;*</i> (see <code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2)). On x86-64 it is the new value to be set for the %fs base register (see the <code>ARCH_SET_FS</code> argument to <code><a href="/docs/linux/man/2-arch_prctl/">arch_prctl</a></code>(2)). On architectures with a dedicated TLS register, it is the new value of that register.</p>
<dt>
<dd> Use of this flag requires detailed knowledge and generally it should not be used except in libraries implementing threading.</p>
<dt><code>CLONE_SIGHAND</code> (since Linux 2.0)</p>
<dd> If <code>CLONE_SIGHAND</code> is set, the calling process and the child process share the same table of signal handlers. If the calling process or child process calls <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) to change the behavior associated with a signal, the behavior is changed in the other process as well. However, the calling process and child processes still have distinct signal masks and sets of pending signals. So, one of them may block or unblock signals using <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) without affecting the other process.</p>
<dt>
<dd> If <code>CLONE_SIGHAND</code> is not set, the child process inherits a copy of the signal handlers of the calling process at the time of the clone call. Calls to <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) performed later by one of the processes have no effect on the other process.</p>
<dt>
<dd> Since Linux 2.6.0, the <i>flags</i> mask must also include <code>CLONE_VM</code> if <code>CLONE_SIGHAND</code> is specified</p>
<dt><code>CLONE_STOPPED</code> (since Linux 2.6.0)</p>
<dd> If <code>CLONE_STOPPED</code> is set, then the child is initially stopped (as though it was sent a <code>SIGSTOP</code> signal), and must be resumed by sending it a <code>SIGCONT</code> signal.</p>
<dt>
<dd> This flag was <i>deprecated</i> from Linux 2.6.25 onward, and was <i>removed</i> altogether in Linux 2.6.38. Since then, the kernel silently ignores it without error. Starting with Linux 4.6, the same bit was reused for the <code>CLONE_NEWCGROUP</code> flag.</p>
<dt><code>CLONE_SYSVSEM</code> (since Linux 2.5.10)</p>
<dd> If <code>CLONE_SYSVSEM</code> is set, then the child and the calling process share a single list of System V semaphore adjustment (<i>semadj</i>) values (see <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2)). In this case, the shared list accumulates <i>semadj</i> values across all processes sharing the list, and semaphore adjustments are performed only when the last process that is sharing the list terminates (or ceases sharing the list using <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2)). If this flag is not set, then the child has a separate <i>semadj</i> list that is initially empty.</p>
<dt><code>CLONE_THREAD</code> (since Linux 2.4.0)</p>
<dd> If <code>CLONE_THREAD</code> is set, the child is placed in the same thread group as the calling process. To make the remainder of the discussion of <code>CLONE_THREAD</code> more readable, the term &quot;thread&quot; is used to refer to the processes within a thread group.</p>
<dt>
<dd> Thread groups were a feature added in Linux 2.4 to support the POSIX threads notion of a set of threads that share a single PID. Internally, this shared PID is the so-called thread group identifier (TGID) for the thread group. Since Linux 2.4, calls to <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) return the TGID of the caller.</p>
<dt>
<dd> The threads within a group can be distinguished by their (system-wide) unique thread IDs (TID). A new thread&#8217;s TID is available as the function result returned to the caller, and a thread can obtain its own TID using <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2).</p>
<dt>
<dd> When a clone call is made without specifying <code>CLONE_THREAD</code>, then the resulting thread is placed in a new thread group whose TGID is the same as the thread&#8217;s TID. This thread is the <i>leader</i> of the new thread group.</p>
<dt>
<dd> A new thread created with <code>CLONE_THREAD</code> has the same parent process as the process that made the clone call (i.e., like <code>CLONE_PARENT</code>), so that calls to <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2) return the same value for all of the threads in a thread group. When a <code>CLONE_THREAD</code> thread terminates, the thread that created it is not sent a <code>SIGCHLD</code> (or other termination) signal; nor can the status of such a thread be obtained using <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2). (The thread is said to be <i>detached</i>.)</p>
<dt>
<dd> After all of the threads in a thread group terminate the parent process of the thread group is sent a <code>SIGCHLD</code> (or other termination) signal.</p>
<dt>
<dd> If any of the threads in a thread group performs an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), then all threads other than the thread group leader are terminated, and the new program is executed in the thread group leader.</p>
<dt>
<dd> If one of the threads in a thread group creates a child using <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), then any thread in the group can <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) for that child.</p>
<dt>
<dd> Since Linux 2.5.35, the <i>flags</i> mask must also include <code>CLONE_SIGHAND</code> if <code>CLONE_THREAD</code> is specified (and note that, since Linux 2.6.0, <code>CLONE_SIGHAND</code> also requires <code>CLONE_VM</code> to be included).</p>
<dt>
<dd> Signal dispositions and actions are process-wide: if an unhandled signal is delivered to a thread, then it will affect (terminate, stop, continue, be ignored in) all members of the thread group.</p>
<dt>
<dd> Each thread has its own signal mask, as set by <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2).</p>
<dt>
<dd> A signal may be process-directed or thread-directed. A process-directed signal is targeted at a thread group (i.e., a TGID), and is delivered to an arbitrarily selected thread from among those that are not blocking the signal. A signal may be process-directed because it was generated by the kernel for reasons other than a hardware exception, or because it was sent using <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) or <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3). A thread-directed signal is targeted at (i.e., delivered to) a specific thread. A signal may be thread directed because it was sent using <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2) or <code><a href="/docs/linux/man/3-pthread_sigqueue/">pthread_sigqueue</a></code>(3), or because the thread executed a machine language instruction that triggered a hardware exception (e.g., invalid memory access triggering <code>SIGSEGV</code> or a floating-point exception triggering <code>SIGFPE</code>).</p>
<dt>
<dd> A call to <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2) returns a signal set that is the union of the pending process-directed signals and the signals that are pending for the calling thread.</p>
<dt>
<dd> If a process-directed signal is delivered to a thread group, and the thread group has installed a handler for the signal, then the handler will be invoked in exactly one, arbitrarily selected member of the thread group that has not blocked the signal. If multiple threads in a group are waiting to accept the same signal using <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), the kernel will arbitrarily select one of these threads to receive the signal.</p>
<dt><code>CLONE_UNTRACED</code> (since Linux 2.5.46)</p>
<dd> If <code>CLONE_UNTRACED</code> is specified, then a tracing process cannot force <code>CLONE_PTRACE</code> on this child process.</p>
<dt><code>CLONE_VFORK</code> (since Linux 2.2)</p>
<dd> If <code>CLONE_VFORK</code> is set, the execution of the calling process is suspended until the child releases its virtual memory resources via a call to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) or <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) (as with <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2)).</p>
<dt>
<dd> If <code>CLONE_VFORK</code> is not set, then both the calling process and the child are schedulable after the call, and an application should not rely on execution occurring in any particular order.</p>
<dt><code>CLONE_VM</code> (since Linux 2.0)</p>
<dd> If <code>CLONE_VM</code> is set, the calling process and the child process run in the same memory space. In particular, memory writes performed by the calling process or by the child process are also visible in the other process. Moreover, any memory mapping or unmapping performed with <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) or <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2) by the child or calling process also affects the other process.</p>
<dt>
<dd> If <code>CLONE_VM</code> is not set, the child process runs in a separate copy of the memory space of the calling process at the time of the clone call. Memory writes or file mappings/unmappings performed by one of the processes do not affect the other, as with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2).</p>
<dt>
<dd> If the <code>CLONE_VM</code> flag is specified and the <code>CLONE_VM</code> flag is not specified, then any alternate signal stack that was established by <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2) is cleared in the child process.</dl>
<h2>RETURN VALUE</h2>
<p> On success, the thread ID of the child process is returned in the caller&#8217;s thread of execution. On failure, -1 is returned in the caller&#8217;s context, no child process will be created, and <i>errno</i> will be set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> Too many processes are already running; see <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2).</p>
<dt><code>EBUSY</code> (<code>clone3</code>() only)</p>
<dd> <code>CLONE_INTO_CGROUP</code> was specified in <i>cl_args.flags</i>, but the file descriptor specified in <i>cl_args.cgroup</i> refers to a version 2 cgroup in which a domain controller is enabled.</p>
<dt><code>EEXIST</code> (<code>clone3</code>() only)</p>
<dd> One (or more) of the PIDs specified in <i>set_tid</i> already exists in the corresponding PID namespace.</p>
<dt><code>EINVAL</code></p>
<dd> Both <code>CLONE_SIGHAND</code> and <code>CLONE_CLEAR_SIGHAND</code> were specified in the <i>flags</i> mask.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_SIGHAND</code> was specified in the <i>flags</i> mask, but <code>CLONE_VM</code> was not. (Since Linux 2.6.0.)</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_THREAD</code> was specified in the <i>flags</i> mask, but <code>CLONE_SIGHAND</code> was not. (Since Linux 2.5.35.)</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_THREAD</code> was specified in the <i>flags</i> mask, but the current process previously called <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) with the <code>CLONE_NEWPID</code> flag or used <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) to reassociate itself with a PID namespace.</p>
<dt><code>EINVAL</code></p>
<dd> Both <code>CLONE_FS</code> and <code>CLONE_NEWNS</code> were specified in the <i>flags</i> mask.</p>
<dt><code>EINVAL</code> (since Linux 3.9)</p>
<dd> Both <code>CLONE_NEWUSER</code> and <code>CLONE_FS</code> were specified in the <i>flags</i> mask.</p>
<dt><code>EINVAL</code></p>
<dd> Both <code>CLONE_NEWIPC</code> and <code>CLONE_SYSVSEM</code> were specified in the <i>flags</i> mask.</p>
<dt><code>EINVAL</code></p>
<dd> One (or both) of <code>CLONE_NEWPID</code> or <code>CLONE_NEWUSER</code> and one (or both) of <code>CLONE_THREAD</code> or <code>CLONE_PARENT</code> were specified in the <i>flags</i> mask.</p>
<dt><code>EINVAL</code> (since Linux 2.6.32)</p>
<dd> <code>CLONE_PARENT</code> was specified, and the caller is an init process.</p>
<dt><code>EINVAL</code></p>
<dd> Returned by the glibc <code>clone</code>() wrapper function when <i>fn</i> or <i>stack</i> is specified as NULL.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWIPC</code> was specified in the <i>flags</i> mask, but the kernel was not configured with the <code>CONFIG_SYSVIPC</code> and <code>CONFIG_IPC_NS</code> options.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWNET</code> was specified in the <i>flags</i> mask, but the kernel was not configured with the <code>CONFIG_NET_NS</code> option.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWPID</code> was specified in the <i>flags</i> mask, but the kernel was not configured with the <code>CONFIG_PID_NS</code> option.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWUSER</code> was specified in the <i>flags</i> mask, but the kernel was not configured with the <code>CONFIG_USER_NS</code> option.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWUTS</code> was specified in the <i>flags</i> mask, but the kernel was not configured with the <code>CONFIG_UTS_NS</code> option.</p>
<dt><code>EINVAL</code></p>
<dd> <i>stack</i> is not aligned to a suitable boundary for this architecture. For example, on aarch64, <i>stack</i> must be a multiple of 16.</p>
<dt><code>EINVAL</code> (<code>clone3</code>() only)</p>
<dd> <code>CLONE_DETACHED</code> was specified in the <i>flags</i> mask.</p>
<dt><code>EINVAL</code> (<code>clone</code>() only)</p>
<dd> <code>CLONE_PIDFD</code> was specified together with <code>CLONE_DETACHED</code> in the <i>flags</i> mask.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_PIDFD</code> was specified together with <code>CLONE_THREAD</code> in the <i>flags</i> mask.</p>
<dt><code>EINVAL </code>(<code>clone</code>() only)</p>
<dd> <code>CLONE_PIDFD</code> was specified together with <code>CLONE_PARENT_SETTID</code> in the <i>flags</i> mask.</p>
<dt><code>EINVAL</code> (<code>clone3</code>() only)</p>
<dd> <i>set_tid_size</i> is greater than the number of nested PID namespaces.</p>
<dt><code>EINVAL</code> (<code>clone3</code>() only)</p>
<dd> One of the PIDs specified in <i>set_tid</i> was an invalid.</p>
<dt><code>EINVAL</code> (AArch64 only, Linux 4.6 and earlier)</p>
<dd> <i>stack</i> was not aligned to a 126-bit boundary.</p>
<dt><code>ENOMEM</code></p>
<dd> Cannot allocate sufficient memory to allocate a task structure for the child, or to copy those parts of the caller&#8217;s context that need to be copied.</p>
<dt><code>ENOSPC</code> (since Linux 3.7)</p>
<dd> <code>CLONE_NEWPID</code> was specified in the <i>flags</i> mask, but the limit on the nesting depth of PID namespaces would have been exceeded; see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7).</p>
<dt><code>ENOSPC</code> (since Linux 4.9; beforehand <code>EUSERS</code>)</p>
<dd> <code>CLONE_NEWUSER</code> was specified in the <i>flags</i> mask, and the call would cause the limit on the number of nested user namespaces to be exceeded. See <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</p>
<dt>
<dd> From Linux 3.11 to Linux 4.8, the error diagnosed in this case was <code>EUSERS</code>.</p>
<dt><code>ENOSPC</code> (since Linux 4.9)</p>
<dd> One of the values in the <i>flags</i> mask specified the creation of a new user namespace, but doing so would have caused the limit defined by the corresponding file in <i>/proc/sys/user</i> to be exceeded. For further details, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7).</p>
<dt><code>EOPNOTSUPP</code> (<code>clone3</code>() only)</p>
<dd> <code>CLONE_INTO_CGROUP</code> was specified in <i>cl_args.flags</i>, but the file descriptor specified in <i>cl_args.cgroup</i> refers to a version 2 cgroup that is in the <i>domain invalid</i> state.</p>
<dt><code>EPERM</code></p>
<dd> <code>CLONE_NEWCGROUP</code>, <code>CLONE_NEWIPC</code>, <code>CLONE_NEWNET</code>, <code>CLONE_NEWNS</code>, <code>CLONE_NEWPID</code>, or <code>CLONE_NEWUTS</code> was specified by an unprivileged process (process without <code>CAP_SYS_ADMIN</code>).</p>
<dt><code>EPERM</code></p>
<dd> <code>CLONE_PID</code> was specified by a process other than process 0. (This error occurs only on Linux 2.5.15 and earlier.)</p>
<dt><code>EPERM</code></p>
<dd> <code>CLONE_NEWUSER</code> was specified in the <i>flags</i> mask, but either the effective user ID or the effective group ID of the caller does not have a mapping in the parent namespace (see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)).</p>
<dt><code>EPERM</code> (since Linux 3.9)</p>
<dd> <code>CLONE_NEWUSER</code> was specified in the <i>flags</i> mask and the caller is in a chroot environment (i.e., the caller&#8217;s root directory does not match the root directory of the mount namespace in which it resides).</p>
<dt><code>EPERM</code> (<code>clone3</code>() only)</p>
<dd> <i>set_tid_size</i> was greater than zero, and the caller lacks the <code>CAP_SYS_ADMIN</code> capability in one or more of the user namespaces that own the corresponding PID namespaces.</p>
<dt><code>ERESTARTNOINTR</code> (since Linux 2.6.17)</p>
<dd> System call was interrupted by a signal and will be restarted. (This can be seen only during a trace.)</p>
<dt><code>EUSERS</code> (Linux 3.11 to Linux 4.8)</p>
<dd> <code>CLONE_NEWUSER</code> was specified in the <i>flags</i> mask, and the limit on the number of nested user namespaces would be exceeded. See the discussion of the <code>ENOSPC</code> error above.</dl>
<h2>VERSIONS</h2>
<p> The <code>clone3</code>() system call first appeared in Linux 5.3.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> One use of these systems calls is to implement threads: multiple flows of control in a program that run concurrently in a shared address space. </p>
<p> Glibc does not provide a wrapper for <code>clone3</code>(); call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> Note that the glibc <code>clone</code>() wrapper function makes some changes in the memory pointed to by <i>stack</i> (changes required to set the stack up correctly for the child) <i>before</i> invoking the <code>clone</code>() system call. So, in cases where <code>clone</code>() is used to recursively create children, do not use the buffer employed for the parent&#8217;s stack as the stack of the child. </p>
<p> The <code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2) system call can be used to test whether two processes share various resources such as a file descriptor table, System V semaphore undo operations, or a virtual address space. </p>
<p> Handlers registered using <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3) are not executed during a clone call. </p>
<p> In the Linux 2.4.x series, <code>CLONE_THREAD</code> generally does not make the parent of the new thread the same as the parent of the calling process. However, for kernel versions 2.4.7 to 2.4.18 the <code>CLONE_THREAD</code> flag implied the <code>CLONE_PARENT</code> flag (as in Linux 2.6.0 and later). </p>
<p> On i386, <code>clone</code>() should not be called through vsyscall, but directly through <i>int $0x80</i>.</p>
<h3>C library/kernel differences</h3>
<p> The raw <code>clone</code>() system call corresponds more closely to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) in that execution in the child continues from the point of the call. As such, the <i>fn</i> and <i>arg</i> arguments of the <code>clone</code>() wrapper function are omitted. </p>
<p> In contrast to the glibc wrapper, the raw <code>clone</code>() system call accepts NULL as a <i>stack</i> argument (and <code>clone3</code>() likewise allows <i>cl_args.stack</i> to be NULL). In this case, the child uses a duplicate of the parent&#8217;s stack. (Copy-on-write semantics ensure that the child gets separate copies of stack pages when either process modifies the stack.) In this case, for correct operation, the <code>CLONE_VM</code> option should not be specified. (If the child <i>shares</i> the parent&#8217;s memory because of the use of the <code>CLONE_VM</code> flag, then no copy-on-write duplication occurs and chaos is likely to result.) </p>
<p> The order of the arguments also differs in the raw system call, and there are variations in the arguments across architectures, as detailed in the following paragraphs. </p>
<p> The raw system call interface on x86-64 and some other architectures (including sh, tile, and alpha) is: </p>
<p> <code>long clone(unsigned long </code><i>flags</i><code>, void *</code><i>stack</i><code>,</code> <code> int *</code><i>parent_tid</i><code>, int *</code><i>child_tid</i><code>,</code> <code> unsigned long </code><i>tls</i><code>);</code> </p>
<p> On x86-32, and several other common architectures (including score, ARM, ARM 64, PA-RISC, arc, Power PC, xtensa, and MIPS), the order of the last two arguments is reversed: </p>
<p> <code>long clone(unsigned long </code><i>flags</i><code>, void *</code><i>stack</i><code>,</code> <code> int *</code><i>parent_tid</i><code>, unsigned long </code><i>tls</i><code>,</code> <code> int *</code><i>child_tid</i><code>);</code> </p>
<p> On the cris and s390 architectures, the order of the first two arguments is reversed: </p>
<p> <code>long clone(void *</code><i>stack</i><code>, unsigned long </code><i>flags</i><code>,</code> <code> int *</code><i>parent_tid</i><code>, int *</code><i>child_tid</i><code>,</code> <code> unsigned long </code><i>tls</i><code>);</code> </p>
<p> On the microblaze architecture, an additional argument is supplied: </p>
<p> <code>long clone(unsigned long </code><i>flags</i><code>, void *</code><i>stack</i><code>,</code> <code> int </code><i>stack_size</i><code>,</code><i></i> /* Size of stack */ <code> int *</code><i>parent_tid</i><code>, int *</code><i>child_tid</i><code>,</code> <code> unsigned long </code><i>tls</i><code>);</code></p>
<h3>blackfin, m68k, and sparc</h3>
<p> The argument-passing conventions on blackfin, m68k, and sparc are different from the descriptions above. For details, see the kernel (and glibc) source.</p>
<h3>ia64</h3>
<p> On ia64, a different interface is used: </p>
<p> <code>int __clone2(int (*</code><i>fn</i><code>)(void *),</code> <code> void *</code><i>stack_base</i><code>, size_t </code><i>stack_size</i><code>,</code> <code> int </code><i>flags</i><code>, void *</code><i>arg</i><code>, &#8230;</code> <code> /* pid_t *</code><i>parent_tid</i><code>, struct user_desc *</code><i>tls</i><code>,</code> <code> pid_t *</code><i>child_tid</i><code> */ );</code> </p>
<p> The prototype shown above is for the glibc wrapper function; for the system call itself, the prototype can be described as follows (it is identical to the <code>clone</code>() prototype on microblaze): </p>
<p> <code>long clone2(unsigned long </code><i>flags</i><code>, void *</code><i>stack_base</i><code>,</code> <code> int </code><i>stack_size</i><code>,</code><i></i> /* Size of stack */ <code> int *</code><i>parent_tid</i><code>, int *</code><i>child_tid</i><code>,</code> <code> unsigned long </code><i>tls</i><code>);</code> </p>
<p> <code>__clone2</code>() operates in the same way as <code>clone</code>(), except that <i>stack_base</i> points to the lowest address of the child&#8217;s stack area, and <i>stack_size</i> specifies the size of the stack pointed to by <i>stack_base</i>.</p>
<h3>Linux 2.4 and earlier</h3>
<p> In Linux 2.4 and earlier, <code>clone</code>() does not take arguments <i>parent_tid</i>, <i>tls</i>, and <i>child_tid</i>.</p>
<h2>BUGS</h2>
<p> GNU C library versions 2.3.4 up to and including 2.24 contained a wrapper function for <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) that performed caching of PIDs. This caching relied on support in the glibc wrapper for <code>clone</code>(), but limitations in the implementation meant that the cache was not up to date in some circumstances. In particular, if a signal was delivered to the child immediately after the <code>clone</code>() call, then a call to <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) in a handler for the signal could return the PID of the calling process (&quot;the parent&quot;), if the clone wrapper had not yet had a chance to update the PID cache in the child. (This discussion ignores the case where the child was created using <code>CLONE_THREAD</code>, when <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) <i>should</i> return the same value in the child and in the process that called <code>clone</code>(), since the caller and the child are in the same thread group. The stale-cache problem also does not occur if the <i>flags</i> argument includes <code>CLONE_VM</code>.) To get the truth, it was sometimes necessary to use code such as the following: </p>
<p> #include &lt;syscall.h&gt; </p>
<p> pid_t mypid; </p>
<p> mypid = syscall(SYS_getpid); </p>
<p> Because of the stale-cache problem, as well as other problems noted in <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2), the PID caching feature was removed in glibc 2.25.</p>
<h2>EXAMPLES</h2>
<p> The following program demonstrates the use of <code>clone</code>() to create a child process that executes in a separate UTS namespace. The child changes the hostname in its UTS namespace. Both parent and child then display the system hostname, making it possible to see that the hostname differs in the UTS namespaces of the parent and child. For an example of the use of this program, see <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2). </p>
<p> Within the sample program, we allocate the memory that is to be used for the child&#8217;s stack using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) rather than <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) for the following reasons:</p>
<dl>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) allocates a block of memory that starts on a page boundary and is a multiple of the page size. This is useful if we want to establish a guard page (a page with protection <code>PROT_NONE</code>) at the end of the stack using <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2).</p>
<dt>*</p>
<dd> We can specify the <code>MAP_STACK</code> flag to request a mapping that is suitable for a stack. For the moment, this flag is a no-op on Linux, but it exists and has effect on some other systems, so we should include it for portability.</dl>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;sys/wait.h&gt; #include &lt;sys/utsname.h&gt; #include &lt;sched.h&gt; #include &lt;string.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;sys/mman.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static int /* Start function for cloned child */ childFunc(void *arg) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct utsname uts; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Change hostname in UTS namespace of child&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sethostname(arg, strlen(arg))&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;sethostname&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Retrieve and display hostname&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(uname(&amp;uts)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;uname&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;uts.nodename in child:&nbsp;<wbr>&nbsp;%s
&quot;, uts.nodename); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Keep the namespace open for a while, by sleeping.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This allows some experimentation&#8211;for example, another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;process might join the namespace.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sleep(200); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Child terminates now&nbsp;*/ } </p>
<p> #define STACK_SIZE (1024 * 1024) /* Stack size for cloned child */ </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*stack;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Start of stack buffer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*stackTop;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;End of stack buffer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t pid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct utsname uts; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;child-hostname&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Allocate memory to be used for the stack of the child&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stack&nbsp;=&nbsp;mmap(NULL, STACK_SIZE, PROT_READ | PROT_WRITE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MAP_PRIVATE | MAP_ANONYMOUS | MAP_STACK, -1, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(stack&nbsp;==&nbsp;MAP_FAILED)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mmap&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stackTop&nbsp;=&nbsp;stack&nbsp;+&nbsp;STACK_SIZE;&nbsp;<wbr>&nbsp;/*&nbsp;Assume stack grows downward&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create child that has its own UTS namespace;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;child commences execution in childFunc()&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid&nbsp;=&nbsp;clone(childFunc, stackTop, CLONE_NEWUTS | SIGCHLD, argv[1]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pid&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;clone&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;clone()&nbsp;returned&nbsp;%jd
&quot;,&nbsp;(intmax_t)&nbsp;pid); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Parent falls through to here&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-sleep/">sleep</a>(1);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Give child time to change its hostname&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display hostname in parent&#8217;s UTS namespace. This will be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;different from hostname in child&#8217;s UTS namespace.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(uname(&amp;uts)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;uname&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;uts.nodename in parent:&nbsp;%s
&quot;, uts.nodename); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(waitpid(pid, NULL, 0)&nbsp;==&nbsp;-1)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for child&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;waitpid&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;child has terminated
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2), <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2), <code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2), <code><a href="/docs/linux/man/2-set_tid_address/">set_tid_address</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-tkill/">tkill</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
