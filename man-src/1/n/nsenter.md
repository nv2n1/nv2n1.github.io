---
title: "nsenter(1)"
name: "nsenter"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nsenter/"
description: "nsenter – run program in different namespaces"
---

<h2 class="name">NAME</h2>
<p> nsenter &#8211; run program in different namespaces </p>
<h2>SYNOPSIS</h2>
<p> <code>nsenter</code> [options] [<i>program</i> [<i>arguments</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>nsenter</code> command executes <i>program</i> in the namespace(s) that are specified in the command-line options (described below). If <i>program</i> is not given, then &quot;${SHELL}&quot; is run (default: <i>/bin/sh</i>). </p>
<p> Enterable namespaces are: </p>
<p> <code>mount namespace</code></p>
<dl>
<dt>
<dd> Mounting and unmounting filesystems will not affect the rest of the system, except for filesystems which are explicitly marked as shared (with <code>mount &#8211;make-shared</code>; see <i>/proc/self/mountinfo</i> for the <code>shared</code> flag). For further details, see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7) and the discussion of the <code>CLONE_NEWNS</code> flag in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</dl>
<p> <code>UTS namespace</code></p>
<dl>
<dt>
<dd> Setting hostname or domainname will not affect the rest of the system. For further details, see <code><a href="/docs/linux/man/7-uts_namespaces/">uts_namespaces</a></code>(7).</dl>
<p> <code>IPC namespace</code></p>
<dl>
<dt>
<dd> The process will have an independent namespace for POSIX message queues as well as System V message queues, semaphore sets and shared memory segments. For further details, see <code><a href="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></code>(7).</dl>
<p> <code>network namespace</code></p>
<dl>
<dt>
<dd> The process will have independent IPv4 and IPv6 stacks, IP routing tables, firewall rules, the <i>/proc/net</i> and <i>/sys/class/net</i> directory trees, sockets, etc. For further details, see <code><a href="/docs/linux/man/7-network_namespaces/">network_namespaces</a></code>(7).</dl>
<p> <code>PID namespace</code></p>
<dl>
<dt>
<dd> Children will have a set of PID to process mappings separate from the <code>nsenter</code> process. <code>nsenter</code> will fork by default if changing the PID namespace, so that the new program and its children share the same PID namespace and are visible to each other. If <code>&#8211;no-fork</code> is used, the new program will be exec&#8217;ed without forking. For further details, see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7).</dl>
<p> <code>user namespace</code></p>
<dl>
<dt>
<dd> The process will have a distinct set of UIDs, GIDs and capabilities. For further details, see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</dl>
<p> <code>cgroup namespace</code></p>
<dl>
<dt>
<dd> The process will have a virtualized view of <i>/proc/self/cgroup</i>, and new cgroup mounts will be rooted at the namespace cgroup root. For further details, see <code><a href="/docs/linux/man/7-cgroup_namespaces/">cgroup_namespaces</a></code>(7).</dl>
<p> <code>time namespace</code></p>
<dl>
<dt>
<dd> The process can have a distinct view of <code>CLOCK_MONOTONIC</code> and/or <code>CLOCK_BOOTTIME</code> which can be changed using <i>/proc/self/timens_offsets</i>. For further details, see <code><a href="/docs/linux/man/7-time_namespaces/">time_namespaces</a></code>(7).</dl>
<h2>OPTIONS</h2>
<p> Various of the options below that relate to namespaces take an optional <i>file</i> argument. This should be one of the <i>/proc/[pid]/ns/*</i> files described in <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), or the pathname of a bind mount that was created on one of those files. </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Enter all namespaces of the target process by the default <i>/proc/[pid]/ns/*</i> namespace paths. The default paths to the target process namespaces may be overwritten by namespace specific options (e.g., <code>&#8211;all &#8211;mount</code>=[<i>path</i>]). </p>
<p> The user namespace will be ignored if the same as the caller&#8217;s current user namespace. It prevents a caller that has dropped capabilities from regaining those capabilities via a call to setns(). See <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) for more details.</dl>
<p> <code>-t</code>, <code>&#8211;target</code> <i>PID</i></p>
<dl>
<dt>
<dd> Specify a target process to get contexts from. The paths to the contexts specified by <i>pid</i> are: </p>
<p> <i>/proc/pid/ns/mnt</i></p>
<dl>
<dt>
<dd> the mount namespace</dl>
<p> <i>/proc/pid/ns/uts</i></p>
<dl>
<dt>
<dd> the UTS namespace</dl>
<p> <i>/proc/pid/ns/ipc</i></p>
<dl>
<dt>
<dd> the IPC namespace</dl>
<p> <i>/proc/pid/ns/net</i></p>
<dl>
<dt>
<dd> the network namespace</dl>
<p> <i>/proc/pid/ns/pid</i></p>
<dl>
<dt>
<dd> the PID namespace</dl>
<p> <i>/proc/pid/ns/user</i></p>
<dl>
<dt>
<dd> the user namespace</dl>
<p> <i>/proc/pid/ns/cgroup</i></p>
<dl>
<dt>
<dd> the cgroup namespace</dl>
<p> <i>/proc/pid/ns/time</i></p>
<dl>
<dt>
<dd> the time namespace</dl>
<p> <i>/proc/pid/root</i></p>
<dl>
<dt>
<dd> the root directory</dl>
<p> <i>/proc/pid/cwd</i></p>
<dl>
<dt>
<dd> the working directory respectively</dl>
</dl>
<p> <code>-m</code>, <code>&#8211;mount</code>[=<i>file</i>]</p>
<dl>
<dt>
<dd> Enter the mount namespace. If no file is specified, enter the mount namespace of the target process. If <i>file</i> is specified, enter the mount namespace specified by <i>file</i>.</dl>
<p> <code>-u</code>, <code>&#8211;uts</code>[=<i>file</i>]</p>
<dl>
<dt>
<dd> Enter the UTS namespace. If no file is specified, enter the UTS namespace of the target process. If <i>file</i> is specified, enter the UTS namespace specified by <i>file</i>.</dl>
<p> <code>-i</code>, <code>&#8211;ipc</code>[=<i>file</i>]</p>
<dl>
<dt>
<dd> Enter the IPC namespace. If no file is specified, enter the IPC namespace of the target process. If <i>file</i> is specified, enter the IPC namespace specified by <i>file</i>.</dl>
<p> <code>-n</code>, <code>&#8211;net</code>[=<i>file</i>]</p>
<dl>
<dt>
<dd> Enter the network namespace. If no file is specified, enter the network namespace of the target process. If <i>file</i> is specified, enter the network namespace specified by <i>file</i>.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code>[=<i>file</i>]</p>
<dl>
<dt>
<dd> Enter the PID namespace. If no file is specified, enter the PID namespace of the target process. If <i>file</i> is specified, enter the PID namespace specified by <i>file</i>.</dl>
<p> <code>-U</code>, <code>&#8211;user</code>[=<i>file</i>]</p>
<dl>
<dt>
<dd> Enter the user namespace. If no file is specified, enter the user namespace of the target process. If <i>file</i> is specified, enter the user namespace specified by <i>file</i>. See also the <code>&#8211;setuid</code> and <code>&#8211;setgid</code> options.</dl>
<p> <code>-C</code>, <code>&#8211;cgroup</code>[=<i>file</i>]</p>
<dl>
<dt>
<dd> Enter the cgroup namespace. If no file is specified, enter the cgroup namespace of the target process. If <i>file</i> is specified, enter the cgroup namespace specified by <i>file</i>.</dl>
<p> <code>-T</code>, <code>&#8211;time</code>[=<i>file</i>]</p>
<dl>
<dt>
<dd> Enter the time namespace. If no file is specified, enter the time namespace of the target process. If <i>file</i> is specified, enter the time namespace specified by <i>file</i>.</dl>
<p> <code>-G</code>, <code>&#8211;setgid</code> <i>gid</i></p>
<dl>
<dt>
<dd> Set the group ID which will be used in the entered namespace and drop supplementary groups. <code>nsenter</code> always sets GID for user namespaces, the default is 0.</dl>
<p> <code>-S</code>, <code>&#8211;setuid</code> <i>uid</i></p>
<dl>
<dt>
<dd> Set the user ID which will be used in the entered namespace. <code>nsenter</code> always sets UID for user namespaces, the default is 0.</dl>
<p> <code>&#8211;preserve-credentials</code></p>
<dl>
<dt>
<dd> Don&#8217;t modify UID and GID when enter user namespace. The default is to drops supplementary groups and sets GID and UID to 0.</dl>
<p> <code>-r</code>, <code>&#8211;root</code>[=<i>directory</i>]</p>
<dl>
<dt>
<dd> Set the root directory. If no directory is specified, set the root directory to the root directory of the target process. If directory is specified, set the root directory to the specified directory.</dl>
<p> <code>-w</code>, <code>&#8211;wd</code>[=<i>directory</i>]</p>
<dl>
<dt>
<dd> Set the working directory. If no directory is specified, set the working directory to the working directory of the target process. If directory is specified, set the working directory to the specified directory.</dl>
<p> <code>-F</code>, <code>&#8211;no-fork</code></p>
<dl>
<dt>
<dd> Do not fork before exec&#8217;ing the specified program. By default, when entering a PID namespace, <code>nsenter</code> calls <code>fork</code> before calling <code>exec</code> so that any children will also be in the newly entered PID namespace.</dl>
<p> <code>-Z</code>, <code>&#8211;follow-context</code></p>
<dl>
<dt>
<dd> Set the SELinux security context used for executing a new process according to already running process specified by <code>&#8211;target</code> PID. (The util-linux has to be compiled with SELinux support otherwise the option is unavailable.)</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>nsenter</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
