---
title: "procfs(5)"
name: "procfs"
section: "5"
letter: "p"
url: "/docs/linux/man/5-procfs/"
description: "proc – process information pseudo-filesystem"
---

<p>proc &#8211; process information pseudo-filesystem</p>
<h2>Description</h2>
<p>The <code>proc</code> filesystem is a pseudo-filesystem which provides an interface to kernel data structures. It is commonly mounted at <i>/proc</i>. Typically, it is mounted automatically by the system, but it can also be mounted manually using a command such as: </p>
<p> mount -t proc proc /proc </p>
<p> Most of the files in the <code>proc</code> filesystem are read-only, but some files are writable, allowing kernel variables to be changed.</p>
<h3>Mount options</h3>
<p>The <code>proc</code> filesystem supports the following mount options:</p>
<dl>
<dt><code>hidepid</code>=<i>n</i> (since Linux 3.3)</p>
<dd>This option controls who can access the information in <i>/proc/[pid]</i> directories. The argument, <i>n</i>, is one of the following values:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>Everybody may access all <i>/proc/[pid]</i> directories. This is the traditional behavior, and the default if this mount option is not specified.</p>
<dt>1</p>
<dd>Users may not access files and subdirectories inside any <i>/proc/[pid]</i> directories but their own (the <i>/proc/[pid]</i> directories themselves remain visible). Sensitive files such as <i>/proc/[pid]/cmdline</i> and <i>/proc/[pid]/status</i> are now protected against other users. This makes it impossible to learn whether any user is running a specific program (so long as the program doesn&#8217;t otherwise reveal itself by its behavior).</p>
<dt>2</p>
<dd>As for mode 1, but in addition the <i>/proc/[pid]</i> directories belonging to other users become invisible. This means that <i>/proc/[pid]</i> entries can no longer be used to discover the PIDs on the system. This doesn&#8217;t hide the fact that a process with a specific PID value exists (it can be learned by other means, for example, by &quot;kill -0 $PID&quot;), but it hides a process&#8217;s UID and GID, which could otherwise be learned by employing <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) on a <i>/proc/[pid]</i> directory. This greatly complicates an attacker&#8217;s task of gathering information about running processes (e.g., discovering whether some daemon is running with elevated privileges, whether another user is running some sensitive program, whether other users are running any program at all, and so on).</dl>
</dl>
<dt><code>gid</code>=<i>gid</i> (since Linux 3.3)</p>
<dd>Specifies the ID of a group whose members are authorized to learn process information otherwise prohibited by <code>hidepid</code> (i.e., users in this group behave as though <i>/proc</i> was mounted with <i>hidepid=0</i>). This group should be used instead of approaches such as putting nonroot users into the <code><a href="/docs/linux/man/5-sudoers/">sudoers</a></code>(5) file.</dl>
<h3>Overview</h3>
<p>Underneath <i>/proc</i>, there are the following general groups of files and subdirectories:</p>
<dl>
<dt><i>/proc/[pid]</i> subdirectories</p>
<dd>Each one of these subdirectories contains files and subdirectories exposing information about the process with the corresponding process ID.</p>
<dd>Underneath each of the <i>/proc/[pid]</i> directories, a <i>task</i> subdirectory contains subdirectories of the form <i>task/[tid]</i>, which contain corresponding information about each of the threads in the process, where <i>tid</i> is the kernel thread ID of the thread.</p>
<dd>The <i>/proc/[pid]</i> subdirectories are visible when iterating through <i>/proc</i> with <code><a href="/docs/linux/man/2-getdents/">getdents</a></code>(2) (and thus are visible when one uses <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) to view the contents of <i>/proc</i>).</p>
<dt><i>/proc/[tid]</i> subdirectories</p>
<dd>Each one of these subdirectories contains files and subdirectories exposing information about the thread with the corresponding thread ID. The contents of these directories are the same as the corresponding <i>/proc/[pid]/task/[tid]</i> directories.</p>
<dd>The <i>/proc/[tid]</i> subdirectories are <i>not</i> visible when iterating through <i>/proc</i> with <code><a href="/docs/linux/man/2-getdents/">getdents</a></code>(2) (and thus are <i>not</i> visible when one uses <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) to view the contents of <i>/proc</i>).</p>
<dt><i>/proc/self</i></p>
<dd>When a process accesses this magic symbolic link, it resolves to the process&#8217;s own <i>/proc/[pid]</i> directory.</p>
<dt><i>/proc/thread-self</i></p>
<dd>When a thread accesses this magic symbolic link, it resolves to the process&#8217;s own <i>/proc/self/task/[tid]</i> directory.</p>
<dt><i>/proc/[a-z]*</i></p>
<dd>Various other files and subdirectories under <i>/proc</i> expose system-wide information.</dl>
<p> All of the above are described in more detail below.</p>
<h3>Files and directories</h3>
<p>The following list provides details of many of the files and directories under the <i>/proc</i> hierarchy.</p>
<dl>
<dt><i>/proc/[pid]</i></p>
<dd>There is a numerical subdirectory for each running process; the subdirectory is named by the process ID. Each <i>/proc/[pid]</i> subdirectory contains the pseudo-files and directories described below.</p>
<dd>The files inside each <i>/proc/[pid]</i> directory are normally owned by the effective user and effective group ID of the process. However, as a security measure, the ownership is made <i>root:root</i> if the process&#8217;s &quot;dumpable&quot; attribute is set to a value other than 1.</p>
<dd>Before Linux 4.11, <i>root:root</i> meant the &quot;global&quot; root user ID and group ID (i.e., UID 0 and GID 0 in the initial user namespace). Since Linux 4.11, if the process is in a noninitial user namespace that has a valid mapping for user (group) ID 0 inside the namespace, then the user (group) ownership of the files under <i>/proc/[pid]</i> is instead made the same as the root user (group) ID of the namespace. This means that inside a container, things work as expected for the container &quot;root&quot; user.</p>
<dd>The process&#8217;s &quot;dumpable&quot; attribute may change for the following reasons:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>The attribute was explicitly set via the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_DUMPABLE</code> operation.</p>
<dt>*</p>
<dd>The attribute was reset to the value in the file <i>/proc/sys/fs/suid_dumpable</i> (described below), for the reasons described in <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2).</dl>
</dl>
<dd>Resetting the &quot;dumpable&quot; attribute to 1 reverts the ownership of the <i>/proc/[pid]/*</i> files to the process&#8217;s effective UID and GID. Note, however, that if the effective UID or GID is subsequently modified, then the &quot;dumpable&quot; attribute may be reset, as described in <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2). Therefore, it may be desirable to reset the &quot;dumpable&quot; attribute <i>after</i> making any desired changes to the process&#8217;s effective UID or GID.</p>
<dt><i>/proc/[pid]/attr</i></p>
<dd>The files in this directory provide an API for security modules. The contents of this directory are files that can be read and written in order to set security-related attributes. This directory was added to support SELinux, but the intention was that the API be general enough to support other security modules. For the purpose of explanation, examples of how SELinux uses these files are provided below.</p>
<dd>This directory is present only if the kernel was configured with <code>CONFIG_SECURITY</code>.</p>
<dt><i>/proc/[pid]/attr/current</i> (since Linux 2.6.0)</p>
<dd>The contents of this file represent the current security attributes of the process.</p>
<dd>In SELinux, this file is used to get the security context of a process. Prior to Linux 2.6.11, this file could not be used to set the security context (a write was always denied), since SELinux limited process security transitions to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) (see the description of <i>/proc/[pid]/attr/exec</i>, below). Since Linux 2.6.11, SELinux lifted this restriction and began supporting &quot;set&quot; operations via writes to this node if authorized by policy, although use of this operation is only suitable for applications that are trusted to maintain any desired separation between the old and new security contexts.</p>
<dd>Prior to Linux 2.6.28, SELinux did not allow threads within a multithreaded process to set their security context via this node as it would yield an inconsistency among the security contexts of the threads sharing the same memory space. Since Linux 2.6.28, SELinux lifted this restriction and began supporting &quot;set&quot; operations for threads within a multithreaded process if the new security context is bounded by the old security context, where the bounded relation is defined in policy and guarantees that the new security context has a subset of the permissions of the old security context.</p>
<dd>Other security modules may choose to support &quot;set&quot; operations via writes to this node.</p>
<dt><i>/proc/[pid]/attr/exec</i> (since Linux 2.6.0)</p>
<dd>This file represents the attributes to assign to the process upon a subsequent <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dd>In SELinux, this is needed to support role/domain transitions, and <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) is the preferred point to make such transitions because it offers better control over the initialization of the process in the new security label and the inheritance of state. In SELinux, this attribute is reset on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) so that the new program reverts to the default behavior for any <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) calls that it may make. In SELinux, a process can set only its own <i>/proc/[pid]/attr/exec</i> attribute.</p>
<dt><i>/proc/[pid]/attr/fscreate</i> (since Linux 2.6.0)</p>
<dd>This file represents the attributes to assign to files created by subsequent calls to <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2), and <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2)</p>
<dd>SELinux employs this file to support creation of a file (using the aforementioned system calls) in a secure state, so that there is no risk of inappropriate access being obtained between the time of creation and the time that attributes are set. In SELinux, this attribute is reset on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so that the new program reverts to the default behavior for any file creation calls it may make, but the attribute will persist across multiple file creation calls within a program unless it is explicitly reset. In SELinux, a process can set only its own <i>/proc/[pid]/attr/fscreate</i> attribute.</p>
<dt><i>/proc/[pid]/attr/keycreate</i> (since Linux 2.6.18)</p>
<dd>If a process writes a security context into this file, all subsequently created keys (<code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2)) will be labeled with this context. For further information, see the kernel source file <i>Documentation/security/keys/core.rst</i> (or file <i>Documentation/security/keys.txt</i> on Linux between 3.0 and 4.13, or <i>Documentation/keys.txt</i> before Linux 3.0).</p>
<dt><i>/proc/[pid]/attr/prev</i> (since Linux 2.6.0)</p>
<dd>This file contains the security context of the process before the last <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2); that is, the previous value of <i>/proc/[pid]/attr/current</i>.</p>
<dt><i>/proc/[pid]/attr/socketcreate</i> (since Linux 2.6.18)</p>
<dd>If a process writes a security context into this file, all subsequently created sockets will be labeled with this context.</p>
<dt><i>/proc/[pid]/autogroup</i> (since Linux 2.6.38)</p>
<dd>See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</p>
<dt><i>/proc/[pid]/auxv</i> (since 2.6.0)</p>
<dd>This contains the contents of the ELF interpreter information passed to the process at exec time. The format is one <i>unsigned long</i> ID plus one <i>unsigned long</i> value for each entry. The last entry contains two zeros. See also <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3).</p>
<dd>Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).</p>
<dt><i>/proc/[pid]/cgroup</i> (since Linux 2.6.24)</p>
<dd>See <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7).</p>
<dt><i>/proc/[pid]/clear_refs</i> (since Linux 2.6.22)</p>
<dd>
<dd>This is a write-only file, writable only by owner of the process.</p>
<dd>The following values may be written to the file:</p>
<dl>
<dd>
<dl>
<dt>1 (since Linux 2.6.22)</p>
<dd>Reset the PG_Referenced and ACCESSED/YOUNG bits for all the pages associated with the process. (Before kernel 2.6.32, writing any nonzero value to this file had this effect.)</p>
<dt>2 (since Linux 2.6.32)</p>
<dd>Reset the PG_Referenced and ACCESSED/YOUNG bits for all anonymous pages associated with the process.</p>
<dt>3 (since Linux 2.6.32)</p>
<dd>Reset the PG_Referenced and ACCESSED/YOUNG bits for all file-mapped pages associated with the process.</dl>
</dl>
<dd>Clearing the PG_Referenced and ACCESSED/YOUNG bits provides a method to measure approximately how much memory a process is using. One first inspects the values in the &quot;Referenced&quot; fields for the VMAs shown in <i>/proc/[pid]/smaps</i> to get an idea of the memory footprint of the process. One then clears the PG_Referenced and ACCESSED/YOUNG bits and, after some measured time interval, once again inspects the values in the &quot;Referenced&quot; fields to get an idea of the change in memory footprint of the process during the measured interval. If one is interested only in inspecting the selected mapping types, then the value 2 or 3 can be used instead of 1.</p>
<dd>Further values can be written to affect different properties:</p>
<dl>
<dd>
<dl>
<dt>4 (since Linux 3.11)</p>
<dd>Clear the soft-dirty bit for all the pages associated with the process. This is used (in conjunction with <i>/proc/[pid]/pagemap</i>) by the check-point restore system to discover which pages of a process have been dirtied since the file <i>/proc/[pid]/clear_refs</i> was written to.</p>
<dt>5 (since Linux 4.0)</p>
<dd>Reset the peak resident set size (&quot;high water mark&quot;) to the process&#8217;s current resident set size value.</dl>
</dl>
<dd>Writing any value to <i>/proc/[pid]/clear_refs</i> other than those listed above has no effect.</p>
<dd>The <i>/proc/[pid]/clear_refs</i> file is present only if the <code>CONFIG_PROC_PAGE_MONITOR</code> kernel configuration option is enabled.</p>
<dt><i>/proc/[pid]/cmdline</i></p>
<dd>This read-only file holds the complete command line for the process, unless the process is a zombie. In the latter case, there is nothing in this file: that is, a read on this file will return 0 characters. The command-line arguments appear in this file as a set of strings separated by null bytes (&#8216;
