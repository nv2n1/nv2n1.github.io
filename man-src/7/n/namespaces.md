---
title: "namespaces(7)"
name: "namespaces"
section: "7"
letter: "n"
url: "/docs/linux/man/7-namespaces/"
description: "namespaces – overview of Linux namespaces"
---

<p>namespaces &#8211; overview of Linux namespaces</p>
<h2>Description</h2>
<p>A namespace wraps a global system resource in an abstraction that makes it appear to the processes within the namespace that they have their own isolated instance of the global resource. Changes to the global resource are visible to other processes that are members of the namespace, but are invisible to other processes. One use of namespaces is to implement containers. </p>
<p> This page provides pointers to information on the various namespace types, describes the associated <i>/proc</i> files, and summarizes the APIs for working with namespaces.</p>
<h3>Namespace types</h3>
<p>The following table shows the namespace types available on Linux. The second column of the table shows the flag value that is used to specify the namespace type in various APIs. The third column identifies the manual page that provides details on the namespace type. The last column is a summary of the resources that are isolated by the namespace type. </p>
<table>
<tr VALIGN=top>
<td><code>Namespace</code></td>
<td><code>Flag</code></td>
<td><code>Page</code></td>
<td><code>Isolates</code>
</td>
</tr>
<tr VALIGN=top>
<td>Cgroup&nbsp;</td>
<td><code>CLONE_NEWCGROUP&nbsp;</code></td>
<td><code><a href="/docs/linux/man/7-cgroup_namespaces/">cgroup_namespaces</a></code>(7)&nbsp;</td>
<td>Cgroup root directory
</td>
</tr>
<tr VALIGN=top>
<td>IPC&nbsp;</td>
<td><code>CLONE_NEWIPC&nbsp;</code></td>
<td><code><a href="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></code>(7)&nbsp;</td>
<td> System V IPC,<br />
 POSIX message queues
</td>
</tr>
<tr VALIGN=top>
<td>Network&nbsp;</td>
<td><code>CLONE_NEWNET&nbsp;</code></td>
<td><code><a href="/docs/linux/man/7-network_namespaces/">network_namespaces</a></code>(7)&nbsp;</td>
<td> Network devices,<br />
 stacks, ports, etc.
</td>
</tr>
<tr VALIGN=top>
<td>Mount&nbsp;</td>
<td><code>CLONE_NEWNS&nbsp;</code></td>
<td><code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7)&nbsp;</td>
<td>Mount points
</td>
</tr>
<tr VALIGN=top>
<td>PID&nbsp;</td>
<td><code>CLONE_NEWPID&nbsp;</code></td>
<td><code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7)&nbsp;</td>
<td>Process IDs
</td>
</tr>
<tr VALIGN=top>
<td>Time&nbsp;</td>
<td><code>CLONE_NEWTIME&nbsp;</code></td>
<td><code><a href="/docs/linux/man/7-time_namespaces/">time_namespaces</a></code>(7)&nbsp;</td>
<td> Boot and monotonic<br />
 clocks
</td>
</tr>
<tr VALIGN=top>
<td>User&nbsp;</td>
<td><code>CLONE_NEWUSER&nbsp;</code></td>
<td><code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)&nbsp;</td>
<td>User and group IDs
</td>
</tr>
<tr VALIGN=top>
<td>UTS&nbsp;</td>
<td><code>CLONE_NEWUTS&nbsp;</code></td>
<td><code><a href="/docs/linux/man/7-uts_namespaces/">uts_namespaces</a></code>(7)&nbsp;</td>
<td> Hostname and NIS<br />
 domain name
</td>
</tr>
</table>
<h3>The namespaces API</h3>
<p>As well as various <i>/proc</i> files described below, the namespaces API includes the following system calls:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)</p>
<dd>The <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) system call creates a new process. If the <i>flags</i> argument of the call specifies one or more of the <code>CLONE_NEW*</code> flags listed below, then new namespaces are created for each flag, and the child process is made a member of those namespaces. (This system call also implements a number of features unrelated to namespaces.)</p>
<dt><code><a href="/docs/linux/man/2-setns/">setns</a></code>(2)</p>
<dd>The <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) system call allows the calling process to join an existing namespace. The namespace to join is specified via a file descriptor that refers to one of the <i>/proc/[pid]/ns</i> files described below.</p>
<dt><code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2)</p>
<dd>The <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) system call moves the calling process to a new namespace. If the <i>flags</i> argument of the call specifies one or more of the <code>CLONE_NEW*</code> flags listed below, then new namespaces are created for each flag, and the calling process is made a member of those namespaces. (This system call also implements a number of features unrelated to namespaces.)</p>
<dt><code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)</p>
<dd>Various <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations can be used to discover information about namespaces. These operations are described in <code><a href="/docs/linux/man/2-ioctl_ns/">ioctl_ns</a></code>(2).</dl>
<p> Creation of new namespaces using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) in most cases requires the <code>CAP_SYS_ADMIN</code> capability, since, in the new namespace, the creator will have the power to change global resources that are visible to other processes that are subsequently created in, or join the namespace. User namespaces are the exception: since Linux 3.8, no privilege is required to create a user namespace.</p>
<h3>The /proc/[pid]/ns/ directory</h3>
<p>Each process has a <i>/proc/[pid]/ns/</i> subdirectory containing one entry for each namespace that supports being manipulated by <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2): </p>
<p> $ <code>ls -l /proc/$$/ns | awk &#8216;{print $1, $9, $10, $11}&#8217;</code> total 0 lrwxrwxrwx. cgroup -&gt; cgroup:[4026531835] lrwxrwxrwx. ipc -&gt; ipc:[4026531839] lrwxrwxrwx. mnt -&gt; mnt:[4026531840] lrwxrwxrwx. net -&gt; net:[4026531969] lrwxrwxrwx. pid -&gt; pid:[4026531836] lrwxrwxrwx. pid_for_children -&gt; pid:[4026531834] lrwxrwxrwx. time -&gt; time:[4026531834] lrwxrwxrwx. time_for_children -&gt; time:[4026531834] lrwxrwxrwx. user -&gt; user:[4026531837] lrwxrwxrwx. uts -&gt; uts:[4026531838] </p>
<p> Bind mounting (see <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2)) one of the files in this directory to somewhere else in the filesystem keeps the corresponding namespace of the process specified by <i>pid</i> alive even if all processes currently in the namespace terminate. </p>
<p> Opening one of the files in this directory (or a file that is bind mounted to one of these files) returns a file handle for the corresponding namespace of the process specified by <i>pid</i>. As long as this file descriptor remains open, the namespace will remain alive, even if all processes in the namespace terminate. The file descriptor can be passed to <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2). </p>
<p> In Linux 3.7 and earlier, these files were visible as hard links. Since Linux 3.8, they appear as symbolic links. If two processes are in the same namespace, then the device IDs and inode numbers of their <i>/proc/[pid]/ns/xxx</i> symbolic links will be the same; an application can check this using the <i>stat.st_dev</i> and <i>stat.st_ino</i> fields returned by <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2). The content of this symbolic link is a string containing the namespace type and inode number as in the following example: </p>
<p> $ <code>readlink /proc/$$/ns/uts</code> uts:[4026531838] </p>
<p> The symbolic links in this subdirectory are as follows:</p>
<dl>
<dt><i>/proc/[pid]/ns/cgroup</i> (since Linux 4.6)</p>
<dd>This file is a handle for the cgroup namespace of the process.</p>
<dt><i>/proc/[pid]/ns/ipc</i> (since Linux 3.0)</p>
<dd>This file is a handle for the IPC namespace of the process.</p>
<dt><i>/proc/[pid]/ns/mnt</i> (since Linux 3.8)</p>
<dd>This file is a handle for the mount namespace of the process.</p>
<dt><i>/proc/[pid]/ns/net</i> (since Linux 3.0)</p>
<dd>This file is a handle for the network namespace of the process.</p>
<dt><i>/proc/[pid]/ns/pid</i> (since Linux 3.8)</p>
<dd>This file is a handle for the PID namespace of the process. This handle is permanent for the lifetime of the process (i.e., a process&#8217;s PID namespace membership never changes).</p>
<dt><i>/proc/[pid]/ns/pid_for_children</i> (since Linux 4.12)</p>
<dd>This file is a handle for the PID namespace of child processes created by this process. This can change as a consequence of calls to <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) and <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) (see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7)), so the file may differ from <i>/proc/[pid]/ns/pid</i>. The symbolic link gains a value only after the first child process is created in the namespace. (Beforehand, <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2) of the symbolic link will return an empty buffer.)</p>
<dt><i>/proc/[pid]/ns/time</i> (since Linux 5.6)</p>
<dd>This file is a handle for the time namespace of the process.</p>
<dt><i>/proc/[pid]/ns/time_for_children</i> (since Linux 5.6)</p>
<dd>This file is a handle for the time namespace of child processes created by this process. This can change as a consequence of calls to <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) and <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) (see <code><a href="/docs/linux/man/7-time_namespaces/">time_namespaces</a></code>(7)), so the file may differ from <i>/proc/[pid]/ns/time</i>.</p>
<dt><i>/proc/[pid]/ns/user</i> (since Linux 3.8)</p>
<dd>This file is a handle for the user namespace of the process.</p>
<dt><i>/proc/[pid]/ns/uts</i> (since Linux 3.0)</p>
<dd>This file is a handle for the UTS namespace of the process.</dl>
<p> Permission to dereference or read (<code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2)) these symbolic links is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).</p>
<h3>The /proc/sys/user directory</h3>
<p>The files in the <i>/proc/sys/user</i> directory (which is present since Linux 4.9) expose limits on the number of namespaces of various types that can be created. The files are as follows:</p>
<dl>
<dt><i>max_cgroup_namespaces</i></p>
<dd>The value in this file defines a per-user limit on the number of cgroup namespaces that may be created in the user namespace.</p>
<dt><i>max_ipc_namespaces</i></p>
<dd>The value in this file defines a per-user limit on the number of ipc namespaces that may be created in the user namespace.</p>
<dt><i>max_mnt_namespaces</i></p>
<dd>The value in this file defines a per-user limit on the number of mount namespaces that may be created in the user namespace.</p>
<dt><i>max_net_namespaces</i></p>
<dd>The value in this file defines a per-user limit on the number of network namespaces that may be created in the user namespace.</p>
<dt><i>max_pid_namespaces</i></p>
<dd>The value in this file defines a per-user limit on the number of PID namespaces that may be created in the user namespace.</p>
<dt><i>max_time_namespaces</i> (since Linux 5.7)</p>
<dd>The value in this file defines a per-user limit on the number of time namespaces that may be created in the user namespace.</p>
<dt><i>max_user_namespaces</i></p>
<dd>The value in this file defines a per-user limit on the number of user namespaces that may be created in the user namespace.</p>
<dt><i>max_uts_namespaces</i></p>
<dd>The value in this file defines a per-user limit on the number of uts namespaces that may be created in the user namespace.</dl>
<p> Note the following details about these files:</p>
<dl>
<dt>*</p>
<dd>The values in these files are modifiable by privileged processes.</p>
<dt>*</p>
<dd>The values exposed by these files are the limits for the user namespace in which the opening process resides.</p>
<dt>*</p>
<dd>The limits are per-user. Each user in the same user namespace can create namespaces up to the defined limit.</p>
<dt>*</p>
<dd>The limits apply to all users, including UID 0.</p>
<dt>*</p>
<dd>These limits apply in addition to any other per-namespace limits (such as those for PID and user namespaces) that may be enforced.</p>
<dt>*</p>
<dd>Upon encountering these limits, <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) fail with the error <code>ENOSPC</code>.</p>
<dt>*</p>
<dd>For the initial user namespace, the default value in each of these files is half the limit on the number of threads that may be created (<i>/proc/sys/kernel/threads-max</i>). In all descendant user namespaces, the default value in each file is <code>MAXINT</code>.</p>
<dt>*</p>
<dd>When a namespace is created, the object is also accounted against ancestor namespaces. More precisely:</p>
<dl>
<dd>
<dl>
<dt>+</p>
<dd>Each user namespace has a creator UID.</p>
<dt>+</p>
<dd>When a namespace is created, it is accounted against the creator UIDs in each of the ancestor user namespaces, and the kernel ensures that the corresponding namespace limit for the creator UID in the ancestor namespace is not exceeded.</p>
<dt>+</p>
<dd>The aforementioned point ensures that creating a new user namespace cannot be used as a means to escape the limits in force in the current user namespace.</dl>
</dl>
</dl>
<h3>Namespace lifetime</h3>
<p>Absent any other factors, a namespace is automatically torn down when the last process in the namespace terminates or leaves the namespace. However, there are a number of other factors that may pin a namespace into existence even though it has no member processes. These factors include the following:</p>
<dl>
<dt>*</p>
<dd>An open file descriptor or a bind mount exists for the corresponding <i>/proc/[pid]/ns/*</i> file.</p>
<dt>*</p>
<dd>The namespace is hierarchical (i.e., a PID or user namespace), and has a child namespace.</p>
<dt>*</p>
<dd>It is a user namespace that owns one or more nonuser namespaces.</p>
<dt>*</p>
<dd>It is a PID namespace, and there is a process that refers to the namespace via a <i>/proc/[pid]/ns/pid_for_children</i> symbolic link.</p>
<dt>*</p>
<dd>It is a time namespace, and there is a process that refers to the namespace via a <i>/proc/[pid]/ns/time_for_children</i> symbolic link.</p>
<dt>*</p>
<dd>It is an IPC namespace, and a corresponding mount of an <i>mqueue</i> filesystem (see <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)) refers to this namespace.</p>
<dt>*</p>
<dd>It is a PID namespace, and a corresponding mount of a <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) filesystem refers to this namespace.</dl>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nsenter/">nsenter</a></code>(1), <code><a href="/docs/linux/man/1-readlink/">readlink</a></code>(1), <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_ns/">ioctl_ns</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-cgroup_namespaces/">cgroup_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-network_namespaces/">network_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-uts_namespaces/">uts_namespaces</a></code>(7), <code><a href="/docs/linux/man/8-lsns/">lsns</a></code>(8), <code><a href="/docs/linux/man/8-pam_namespace/">pam_namespace</a></code>(8), <code><a href="/docs/linux/man/8-switch_root/">switch_root</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
