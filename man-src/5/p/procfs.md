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
<dt><code>hidepid</code>=<i>n</i> (since Linux 3.3)</dt>
<dd>This option controls who can access the information in <i>/proc/[pid]</i> directories. The argument, <i>n</i>, is one of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt>0</dt>
<dd>Everybody may access all <i>/proc/[pid]</i> directories. This is the traditional behavior, and the default if this mount option is not specified.</dd>
<dt>1</dt>
<dd>Users may not access files and subdirectories inside any <i>/proc/[pid]</i> directories but their own (the <i>/proc/[pid]</i> directories themselves remain visible). Sensitive files such as <i>/proc/[pid]/cmdline</i> and <i>/proc/[pid]/status</i> are now protected against other users. This makes it impossible to learn whether any user is running a specific program (so long as the program doesn&#8217;t otherwise reveal itself by its behavior).</dd>
<dt>2</dt>
<dd>As for mode 1, but in addition the <i>/proc/[pid]</i> directories belonging to other users become invisible. This means that <i>/proc/[pid]</i> entries can no longer be used to discover the PIDs on the system. This doesn&#8217;t hide the fact that a process with a specific PID value exists (it can be learned by other means, for example, by &quot;kill -0 $PID&quot;), but it hides a process&#8217;s UID and GID, which could otherwise be learned by employing <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) on a <i>/proc/[pid]</i> directory. This greatly complicates an attacker&#8217;s task of gathering information about running processes (e.g., discovering whether some daemon is running with elevated privileges, whether another user is running some sensitive program, whether other users are running any program at all, and so on).</dd></dl>
</dl>
<dt><code>gid</code>=<i>gid</i> (since Linux 3.3)</dt>
<dd>Specifies the ID of a group whose members are authorized to learn process information otherwise prohibited by <code>hidepid</code> (i.e., users in this group behave as though <i>/proc</i> was mounted with <i>hidepid=0</i>). This group should be used instead of approaches such as putting nonroot users into the <code><a href="/docs/linux/man/5-sudoers/">sudoers</a></code>(5) file.</dd></dl>
<h3>Overview</h3>
<p>Underneath <i>/proc</i>, there are the following general groups of files and subdirectories:</p>
<dl>
<dt><i>/proc/[pid]</i> subdirectories</dt>
<dd>Each one of these subdirectories contains files and subdirectories exposing information about the process with the corresponding process ID.</dd>
<dd>Underneath each of the <i>/proc/[pid]</i> directories, a <i>task</i> subdirectory contains subdirectories of the form <i>task/[tid]</i>, which contain corresponding information about each of the threads in the process, where <i>tid</i> is the kernel thread ID of the thread.</dd>
<dd>The <i>/proc/[pid]</i> subdirectories are visible when iterating through <i>/proc</i> with <code><a href="/docs/linux/man/2-getdents/">getdents</a></code>(2) (and thus are visible when one uses <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) to view the contents of <i>/proc</i>).</dd>
<dt><i>/proc/[tid]</i> subdirectories</dt>
<dd>Each one of these subdirectories contains files and subdirectories exposing information about the thread with the corresponding thread ID. The contents of these directories are the same as the corresponding <i>/proc/[pid]/task/[tid]</i> directories.</dd>
<dd>The <i>/proc/[tid]</i> subdirectories are <i>not</i> visible when iterating through <i>/proc</i> with <code><a href="/docs/linux/man/2-getdents/">getdents</a></code>(2) (and thus are <i>not</i> visible when one uses <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) to view the contents of <i>/proc</i>).</dd>
<dt><i>/proc/self</i></dt>
<dd>When a process accesses this magic symbolic link, it resolves to the process&#8217;s own <i>/proc/[pid]</i> directory.</dd>
<dt><i>/proc/thread-self</i></dt>
<dd>When a thread accesses this magic symbolic link, it resolves to the process&#8217;s own <i>/proc/self/task/[tid]</i> directory.</dd>
<dt><i>/proc/[a-z]*</i></dt>
<dd>Various other files and subdirectories under <i>/proc</i> expose system-wide information.</dd></dl>
<p> All of the above are described in more detail below.</p>
<h3>Files and directories</h3>
<p>The following list provides details of many of the files and directories under the <i>/proc</i> hierarchy.</p>
<dl>
<dt><i>/proc/[pid]</i></dt>
<dd>There is a numerical subdirectory for each running process; the subdirectory is named by the process ID. Each <i>/proc/[pid]</i> subdirectory contains the pseudo-files and directories described below.</dd>
<dd>The files inside each <i>/proc/[pid]</i> directory are normally owned by the effective user and effective group ID of the process. However, as a security measure, the ownership is made <i>root:root</i> if the process&#8217;s &quot;dumpable&quot; attribute is set to a value other than 1.</dd>
<dd>Before Linux 4.11, <i>root:root</i> meant the &quot;global&quot; root user ID and group ID (i.e., UID 0 and GID 0 in the initial user namespace). Since Linux 4.11, if the process is in a noninitial user namespace that has a valid mapping for user (group) ID 0 inside the namespace, then the user (group) ownership of the files under <i>/proc/[pid]</i> is instead made the same as the root user (group) ID of the namespace. This means that inside a container, things work as expected for the container &quot;root&quot; user.</dd>
<dd>The process&#8217;s &quot;dumpable&quot; attribute may change for the following reasons:</dd>
<dl>
<dd>
</dd><dl>
<dt>*</dt>
<dd>The attribute was explicitly set via the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_DUMPABLE</code> operation.</dd>
<dt>*</dt>
<dd>The attribute was reset to the value in the file <i>/proc/sys/fs/suid_dumpable</i> (described below), for the reasons described in <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2).</dd></dl>
</dl>
<dd>Resetting the &quot;dumpable&quot; attribute to 1 reverts the ownership of the <i>/proc/[pid]/*</i> files to the process&#8217;s effective UID and GID. Note, however, that if the effective UID or GID is subsequently modified, then the &quot;dumpable&quot; attribute may be reset, as described in <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2). Therefore, it may be desirable to reset the &quot;dumpable&quot; attribute <i>after</i> making any desired changes to the process&#8217;s effective UID or GID.</dd>
<dt><i>/proc/[pid]/attr</i></dt>
<dd>The files in this directory provide an API for security modules. The contents of this directory are files that can be read and written in order to set security-related attributes. This directory was added to support SELinux, but the intention was that the API be general enough to support other security modules. For the purpose of explanation, examples of how SELinux uses these files are provided below.</dd>
<dd>This directory is present only if the kernel was configured with <code>CONFIG_SECURITY</code>.</dd>
<dt><i>/proc/[pid]/attr/current</i> (since Linux 2.6.0)</dt>
<dd>The contents of this file represent the current security attributes of the process.</dd>
<dd>In SELinux, this file is used to get the security context of a process. Prior to Linux 2.6.11, this file could not be used to set the security context (a write was always denied), since SELinux limited process security transitions to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) (see the description of <i>/proc/[pid]/attr/exec</i>, below). Since Linux 2.6.11, SELinux lifted this restriction and began supporting &quot;set&quot; operations via writes to this node if authorized by policy, although use of this operation is only suitable for applications that are trusted to maintain any desired separation between the old and new security contexts.</dd>
<dd>Prior to Linux 2.6.28, SELinux did not allow threads within a multithreaded process to set their security context via this node as it would yield an inconsistency among the security contexts of the threads sharing the same memory space. Since Linux 2.6.28, SELinux lifted this restriction and began supporting &quot;set&quot; operations for threads within a multithreaded process if the new security context is bounded by the old security context, where the bounded relation is defined in policy and guarantees that the new security context has a subset of the permissions of the old security context.</dd>
<dd>Other security modules may choose to support &quot;set&quot; operations via writes to this node.</dd>
<dt><i>/proc/[pid]/attr/exec</i> (since Linux 2.6.0)</dt>
<dd>This file represents the attributes to assign to the process upon a subsequent <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</dd>
<dd>In SELinux, this is needed to support role/domain transitions, and <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) is the preferred point to make such transitions because it offers better control over the initialization of the process in the new security label and the inheritance of state. In SELinux, this attribute is reset on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) so that the new program reverts to the default behavior for any <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) calls that it may make. In SELinux, a process can set only its own <i>/proc/[pid]/attr/exec</i> attribute.</dd>
<dt><i>/proc/[pid]/attr/fscreate</i> (since Linux 2.6.0)</dt>
<dd>This file represents the attributes to assign to files created by subsequent calls to <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2), and <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2)</dd>
<dd>SELinux employs this file to support creation of a file (using the aforementioned system calls) in a secure state, so that there is no risk of inappropriate access being obtained between the time of creation and the time that attributes are set. In SELinux, this attribute is reset on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so that the new program reverts to the default behavior for any file creation calls it may make, but the attribute will persist across multiple file creation calls within a program unless it is explicitly reset. In SELinux, a process can set only its own <i>/proc/[pid]/attr/fscreate</i> attribute.</dd>
<dt><i>/proc/[pid]/attr/keycreate</i> (since Linux 2.6.18)</dt>
<dd>If a process writes a security context into this file, all subsequently created keys (<code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2)) will be labeled with this context. For further information, see the kernel source file <i>Documentation/security/keys/core.rst</i> (or file <i>Documentation/security/keys.txt</i> on Linux between 3.0 and 4.13, or <i>Documentation/keys.txt</i> before Linux 3.0).</dd>
<dt><i>/proc/[pid]/attr/prev</i> (since Linux 2.6.0)</dt>
<dd>This file contains the security context of the process before the last <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2); that is, the previous value of <i>/proc/[pid]/attr/current</i>.</dd>
<dt><i>/proc/[pid]/attr/socketcreate</i> (since Linux 2.6.18)</dt>
<dd>If a process writes a security context into this file, all subsequently created sockets will be labeled with this context.</dd>
<dt><i>/proc/[pid]/autogroup</i> (since Linux 2.6.38)</dt>
<dd>See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</dd>
<dt><i>/proc/[pid]/auxv</i> (since 2.6.0)</dt>
<dd>This contains the contents of the ELF interpreter information passed to the process at exec time. The format is one <i>unsigned long</i> ID plus one <i>unsigned long</i> value for each entry. The last entry contains two zeros. See also <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3).</dd>
<dd>Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).</dd>
<dt><i>/proc/[pid]/cgroup</i> (since Linux 2.6.24)</dt>
<dd>See <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7).</dd>
<dt><i>/proc/[pid]/clear_refs</i> (since Linux 2.6.22)</dt>
<dd>
</dd><dd>This is a write-only file, writable only by owner of the process.</dd>
<dd>The following values may be written to the file:</dd>
<dl>
<dd>
</dd><dl>
<dt>1 (since Linux 2.6.22)</dt>
<dd>Reset the PG_Referenced and ACCESSED/YOUNG bits for all the pages associated with the process. (Before kernel 2.6.32, writing any nonzero value to this file had this effect.)</dd>
<dt>2 (since Linux 2.6.32)</dt>
<dd>Reset the PG_Referenced and ACCESSED/YOUNG bits for all anonymous pages associated with the process.</dd>
<dt>3 (since Linux 2.6.32)</dt>
<dd>Reset the PG_Referenced and ACCESSED/YOUNG bits for all file-mapped pages associated with the process.</dd></dl>
</dl>
<dd>Clearing the PG_Referenced and ACCESSED/YOUNG bits provides a method to measure approximately how much memory a process is using. One first inspects the values in the &quot;Referenced&quot; fields for the VMAs shown in <i>/proc/[pid]/smaps</i> to get an idea of the memory footprint of the process. One then clears the PG_Referenced and ACCESSED/YOUNG bits and, after some measured time interval, once again inspects the values in the &quot;Referenced&quot; fields to get an idea of the change in memory footprint of the process during the measured interval. If one is interested only in inspecting the selected mapping types, then the value 2 or 3 can be used instead of 1.</dd>
<dd>Further values can be written to affect different properties:</dd>
<dl>
<dd>
</dd><dl>
<dt>4 (since Linux 3.11)</dt>
<dd>Clear the soft-dirty bit for all the pages associated with the process. This is used (in conjunction with <i>/proc/[pid]/pagemap</i>) by the check-point restore system to discover which pages of a process have been dirtied since the file <i>/proc/[pid]/clear_refs</i> was written to.</dd>
<dt>5 (since Linux 4.0)</dt>
<dd>Reset the peak resident set size (&quot;high water mark&quot;) to the process&#8217;s current resident set size value.</dd></dl>
</dl>
<dd>Writing any value to <i>/proc/[pid]/clear_refs</i> other than those listed above has no effect.</dd>
<dd>The <i>/proc/[pid]/clear_refs</i> file is present only if the <code>CONFIG_PROC_PAGE_MONITOR</code> kernel configuration option is enabled.</dd>
<dt><i>/proc/[pid]/cmdline</i></dt>
<dd>This read-only file holds the complete command line for the process, unless the process is a zombie. In the latter case, there is nothing in this file: that is, a read on this file will return 0 characters. The command-line arguments appear in this file as a set of strings separated by null bytes (&#8216;\0&#8217;), with a further null byte after the last string.  </dd>
<dd>  If, after an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), the process modifies its <i>argv</i> strings, those changes will show up here. This is not the same thing as modifying the <i>argv</i> array.  </dd>
<dd>  Furthermore, a process may change the memory location that this file refers via <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) operations such as <code>PR_SET_MM_ARG_START</code>.  </dd>
<dd>  Think of this file as the command line that the process wants you to see.  </dd>
<dt><i>/proc/[pid]/comm</i> (since Linux 2.6.33) </dt>
<dd>  This file exposes the process&#8217;s <i>comm</i> value---that is, the command name associated with the process. Different threads in the same process may have different <i>comm</i> values, accessible via <i>/proc/[pid]/task/[tid]/comm</i>. A thread may modify its <i>comm</i> value, or that of any of other thread in the same thread group (see the discussion of <code>CLONE_THREAD</code> in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)), by writing to the file <i>/proc/self/task/[tid]/comm</i>. Strings longer than <code>TASK_COMM_LEN</code> (16) characters (including the terminating null byte) are silently truncated.  </dd>
<dd>  This file provides a superset of the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_NAME</code> and <code>PR_GET_NAME</code> operations, and is employed by <code><a href="/docs/linux/man/3-pthread_setname_np/">pthread_setname_np</a></code>(3) when used to rename threads other than the caller. The value in this file is used for the <i>%e</i> specifier in <i>/proc/sys/kernel/core_pattern</i>; see <code><a href="/docs/linux/man/5-core/">core</a></code>(5).  </dd>
<dt><i>/proc/[pid]/coredump_filter</i> (since Linux 2.6.23) </dt>
<dd>  See <code><a href="/docs/linux/man/5-core/">core</a></code>(5).  </dd>
<dt><i>/proc/[pid]/cpuset</i> (since Linux 2.6.12) </dt>
<dd>  See <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7).  </dd>
<dt><i>/proc/[pid]/cwd</i> </dt>
<dd>  This is a symbolic link to the current working directory of the process. To find out the current working directory of process 20, for instance, you can do this:  </dd>
<dd>  $<code> cd /proc/20/cwd; pwd -P</code>  </dd>
<dd>  In a multithreaded process, the contents of this symbolic link are not available if the main thread has already terminated (typically by calling <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3)).  </dd>
<dd>  Permission to dereference or read (<code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2)) this symbolic link is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[pid]/environ</i> </dt>
<dd>  This file contains the initial environment that was set when the currently executing program was started via <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). The entries are separated by null bytes (&#8216;\0&#8217;), and there may be a null byte at the end. Thus, to print out the environment of process 1, you would do:  </dd>
<dd>  $<code> cat /proc/1/environ | tr &#8216;\000&#8217; &#8216;\n&#8217;</code>  </dd>
<dd>  If, after an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), the process modifies its environment (e.g., by calling functions such as <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3) or modifying the <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) variable directly), this file will <i>not</i> reflect those changes.  </dd>
<dd>  Furthermore, a process may change the memory location that this file refers via <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) operations such as <code>PR_SET_MM_ENV_START</code>.  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[pid]/exe</i> </dt>
<dd>  Under Linux 2.2 and later, this file is a symbolic link containing the actual pathname of the executed command. This symbolic link can be dereferenced normally; attempting to open it will open the executable. You can even type <i>/proc/[pid]/exe</i> to run another copy of the same executable that is being run by process [pid]. If the pathname has been unlinked, the symbolic link will contain the string &#8216;(deleted)&#8216; appended to the original pathname. In a multithreaded process, the contents of this symbolic link are not available if the main thread has already terminated (typically by calling <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3)).  </dd>
<dd>  Permission to dereference or read (<code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2)) this symbolic link is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dd>  Under Linux 2.0 and earlier, <i>/proc/[pid]/exe</i> is a pointer to the binary which was executed, and appears as a symbolic link. A <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2) call on this file under Linux 2.0 returns a string in the format:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[device]:inode  </dd>
<dd>  For example, [0301]:1502 would be inode 1502 on device major 03 (IDE, MFM, etc. drives) minor 01 (first partition on the first drive).  </dd>
<dd>  <code><a href="/docs/linux/man/1-find/">find</a></code>(1) with the <i>-inum</i> option can be used to locate the file.  </dd>
<dt><i>/proc/[pid]/fd/</i> </dt>
<dd>  This is a subdirectory containing one entry for each file which the process has open, named by its file descriptor, and which is a symbolic link to the actual file. Thus, 0 is standard input, 1 standard output, 2 standard error, and so on.  </dd>
<dd>  For file descriptors for pipes and sockets, the entries will be symbolic links whose content is the file type with the inode. A <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2) call on this file returns a string in the format:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type:[inode]  </dd>
<dd>  For example, <i>socket:[2248868]</i> will be a socket and its inode is 2248868. For sockets, that inode can be used to find more information in one of the files under <i>/proc/net/</i>.  </dd>
<dd>  For file descriptors that have no corresponding inode (e.g., file descriptors produced by <code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2), <code><a href="/docs/linux/man/2-epoll_create/">epoll_create</a></code>(2), <code><a href="/docs/linux/man/2-eventfd/">eventfd</a></code>(2), <code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2), <code><a href="/docs/linux/man/2-perf_event_open/">perf_event_open</a></code>(2), <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2), <code><a href="/docs/linux/man/2-timerfd_create/">timerfd_create</a></code>(2), and <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2)), the entry will be a symbolic link with contents of the form  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;anon_inode:&lt;file-type&gt;  </dd>
<dd>  In many cases (but not all), the <i>file-type</i> is surrounded by square brackets.  </dd>
<dd>  For example, an epoll file descriptor will have a symbolic link whose content is the string <i>anon_inode:[eventpoll]</i>.  </dd>
<dd>  In a multithreaded process, the contents of this directory are not available if the main thread has already terminated (typically by calling <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3)).  </dd>
<dd>  Programs that take a filename as a command-line argument, but don&#8217;t take input from standard input if no argument is supplied, and programs that write to a file named as a command-line argument, but don&#8217;t send their output to standard output if no argument is supplied, can nevertheless be made to use standard input or standard output by using <i>/proc/[pid]/fd</i> files as command-line arguments. For example, assuming that <i>-i</i> is the flag designating an input file and <i>-o</i> is the flag designating an output file:  </dd>
<dd>  $<code> foobar -i /proc/self/fd/0 -o /proc/self/fd/1 ...</code>  </dd>
<dd>  and you have a working filter.  </dd>
<dd>  <i>/proc/self/fd/N</i> is approximately the same as <i>/dev/fd/N</i> in some UNIX and UNIX-like systems. Most Linux MAKEDEV scripts symbolically link <i>/dev/fd</i> to <i>/proc/self/fd</i>, in fact.  </dd>
<dd>  Most systems provide symbolic links <i>/dev/stdin</i>, <i>/dev/stdout</i>, and <i>/dev/stderr</i>, which respectively link to the files <i>0</i>, <i>1</i>, and <i>2</i> in <i>/proc/self/fd</i>. Thus the example command above could be written as:  </dd>
<dd>  $<code> foobar -i /dev/stdin -o /dev/stdout ...</code>  </dd>
<dd>  Permission to dereference or read (<code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2)) the symbolic links in this directory is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dd>  Note that for file descriptors referring to inodes (pipes and sockets, see above), those inodes still have permission bits and ownership information distinct from those of the <i>/proc/[pid]/fd</i> entry, and that the owner may differ from the user and group IDs of the process. An unprivileged process may lack permissions to open them, as in this example:  </dd>
<dd>  $<code> echo test | sudo -u nobody cat</code> test $<code> echo test | sudo -u nobody cat /proc/self/fd/0</code> cat: /proc/self/fd/0: Permission denied  </dd>
<dd>  File descriptor 0 refers to the pipe created by the shell and owned by that shell&#8217;s user, which is not <i>nobody</i>, so <code>cat</code> does not have permission to create a new file descriptor to read from that inode, even though it can still read from its existing file descriptor 0.  </dd>
<dt><i>/proc/[pid]/fdinfo/</i> (since Linux 2.6.22) </dt>
<dd>  This is a subdirectory containing one entry for each file which the process has open, named by its file descriptor. The files in this directory are readable only by the owner of the process. The contents of each file can be read to obtain information about the corresponding file descriptor. The content depends on the type of file referred to by the corresponding file descriptor.  </dd>
<dd>  For regular files and directories, we see something like:  </dd>
<dd>  $<code> cat /proc/12015/fdinfo/4</code> pos: 1000 flags: 01002002 mnt_id: 21  </dd>
<dd>  The fields are as follows:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>pos</i> </dt>
<dd>  This is a decimal number showing the file offset.  </dd>
<dt><i>flags</i> </dt>
<dd>  This is an octal number that displays the file access mode and file status flags (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)). If the close-on-exec file descriptor flag is set, then <i>flags</i> will also include the value <code>O_CLOEXEC</code>.  </dd>
<dd>  Before Linux 3.1, this field incorrectly displayed the setting of <code>O_CLOEXEC</code> at the time the file was opened, rather than the current setting of the close-on-exec flag.  </dd>
<dt><i>mnt_id</i> </dt>
<dd>  This field, present since Linux 3.15, is the ID of the mount point containing this file. See the description of <i>/proc/[pid]/mountinfo</i>.  </dd></dl>
 </dl>
 <dd>  For eventfd file descriptors (see <code><a href="/docs/linux/man/2-eventfd/">eventfd</a></code>(2)), we see (since Linux 3.8) the following fields:  </dd>
<dd>  pos:<code>&nbsp;</code>0<br />
 flags:<code>&nbsp;<wbr>&nbsp;</code>02<br />
 mnt_id:<code>&nbsp;</code>10<br />
 eventfd-count: 40  </dd>
<dd>  <i>eventfd-count</i> is the current value of the eventfd counter, in hexadecimal.  </dd>
<dd>  For epoll file descriptors (see <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7)), we see (since Linux 3.8) the following fields:  </dd>
<dd>  pos:<code>&nbsp;</code>0<br />
 flags:<code>&nbsp;<wbr>&nbsp;</code>02<br />
 mnt_id:<code>&nbsp;</code>10<br />
 tfd: 9 events: 19 data: 74253d2500000009 tfd: 7 events: 19 data: 74253d2500000007  </dd>
<dd>  Each of the lines beginning <i>tfd</i> describes one of the file descriptors being monitored via the epoll file descriptor (see <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2) for some details). The <i>tfd</i> field is the number of the file descriptor. The <i>events</i> field is a hexadecimal mask of the events being monitored for this file descriptor. The <i>data</i> field is the data value associated with this file descriptor.  </dd>
<dd>  For signalfd file descriptors (see <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2)), we see (since Linux 3.8) the following fields:  </dd>
<dd>  pos:<code>&nbsp;</code>0<br />
 flags:<code>&nbsp;<wbr>&nbsp;</code>02<br />
 mnt_id:<code>&nbsp;</code>10<br />
 sigmask:<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0000000000000006<br />
  </dd>
<dd>  <i>sigmask</i> is the hexadecimal mask of signals that are accepted via this signalfd file descriptor. (In this example, bits 2 and 3 are set, corresponding to the signals <code>SIGINT</code> and <code>SIGQUIT</code>; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).)  </dd>
<dd>  For inotify file descriptors (see <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7)), we see (since Linux 3.8) the following fields:  </dd>
<dd>  pos:<code>&nbsp;</code>0<br />
 flags:<code>&nbsp;<wbr>&nbsp;</code>00<br />
 mnt_id:<code>&nbsp;</code>11<br />
 inotify wd:2 ino:7ef82a sdev:800001 mask:800afff ignored_mask:0 fhandle-bytes:8 fhandle-type:1 f_handle:2af87e00220ffd73 inotify wd:1 ino:192627 sdev:800001 mask:800afff ignored_mask:0 fhandle-bytes:8 fhandle-type:1 f_handle:27261900802dfd73  </dd>
<dd>  Each of the lines beginning with &quot;inotify&quot; displays information about one file or directory that is being monitored. The fields in this line are as follows:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>wd</i> </dt>
<dd>  A watch descriptor number (in decimal).  </dd>
<dt><i>ino</i> </dt>
<dd>  The inode number of the target file (in hexadecimal).  </dd>
<dt><i>sdev</i> </dt>
<dd>  The ID of the device where the target file resides (in hexadecimal).  </dd>
<dt><i>mask</i> </dt>
<dd>  The mask of events being monitored for the target file (in hexadecimal).  </dd></dl>
 </dl>
 <dd>  If the kernel was built with exportfs support, the path to the target file is exposed as a file handle, via three hexadecimal fields: <i>fhandle-bytes</i>, <i>fhandle-type</i>, and <i>f_handle</i>.  </dd>
<dd>  For fanotify file descriptors (see <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7)), we see (since Linux 3.8) the following fields:  </dd>
<dd>  pos:<code>&nbsp;</code>0<br />
 flags:<code>&nbsp;<wbr>&nbsp;</code>02<br />
 mnt_id:<code>&nbsp;</code>11<br />
 fanotify flags:0 event-flags:88002 fanotify ino:19264f sdev:800001 mflags:0 mask:1 ignored_mask:0 fhandle-bytes:8 fhandle-type:1 f_handle:4f261900a82dfd73  </dd>
<dd>  The fourth line displays information defined when the fanotify group was created via <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2):  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>flags</i> </dt>
<dd>  The <i>flags</i> argument given to <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2) (expressed in hexadecimal).  </dd>
<dt><i>event-flags</i> </dt>
<dd>  The <i>event_f_flags</i> argument given to <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2) (expressed in hexadecimal).  </dd></dl>
 </dl>
 <dd>  Each additional line shown in the file contains information about one of the marks in the fanotify group. Most of these fields are as for inotify, except:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>mflags</i> </dt>
<dd>  The flags associated with the mark (expressed in hexadecimal).  </dd>
<dt><i>mask</i> </dt>
<dd>  The events mask for this mark (expressed in hexadecimal).  </dd>
<dt><i>ignored_mask</i> </dt>
<dd>  The mask of events that are ignored for this mark (expressed in hexadecimal).  </dd></dl>
 </dl>
 <dd>  For details on these fields, see <code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2).  </dd>
<dd>  For timerfd file descriptors (see <code><a href="/docs/linux/man/2-timerfd/">timerfd</a></code>(2)), we see (since Linux 3.17) the following fields:  </dd>
<dd>  pos: 0 flags: 02004002 mnt_id: 13 clockid: 0 ticks: 0 settime flags: 03 it_value: (7695568592, 640020877) it_interval: (0, 0)  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>clockid</i> </dt>
<dd>  This is the numeric value of the clock ID (corresponding to one of the <code>CLOCK_*</code> constants defined via <i>&lt;time.h&gt;</i>) that is used to mark the progress of the timer (in this example, 0 is <code>CLOCK_REALTIME</code>).  </dd>
<dt><i>ticks</i> </dt>
<dd>  This is the number of timer expirations that have occurred, (i.e., the value that <code><a href="/docs/linux/man/2-read/">read</a></code>(2) on it would return).  </dd>
<dt><i>settime flags</i> </dt>
<dd>  This field lists the flags with which the timerfd was last armed (see <code><a href="/docs/linux/man/2-timerfd_settime/">timerfd_settime</a></code>(2)), in octal (in this example, both <code>TFD_TIMER_ABSTIME</code> and <code>TFD_TIMER_CANCEL_ON_SET</code> are set).  </dd>
<dt><i>it_value</i> </dt>
<dd>  This field contains the amount of time until the timer will next expire, expressed in seconds and nanoseconds. This is always expressed as a relative value, regardless of whether the timer was created using the <code>TFD_TIMER_ABSTIME</code> flag.  </dd>
<dt><i>it_interval</i> </dt>
<dd>  This field contains the interval of the timer, in seconds and nanoseconds. (The <i>it_value</i> and <i>it_interval</i> fields contain the values that <code><a href="/docs/linux/man/2-timerfd_gettime/">timerfd_gettime</a></code>(2) on this file descriptor would return.)  </dd></dl>
 </dl>
 <dt><i>/proc/[pid]/gid_map</i> (since Linux 3.5) </dt>
<dd>  See <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).  </dd>
<dt><i>/proc/[pid]/io</i> (since kernel 2.6.20) </dt>
<dd>  This file contains I/O statistics for the process, for example:  </dd>
<dd>  #<code> cat /proc/3828/io</code> rchar: 323934931 wchar: 323929600 syscr: 632687 syscw: 632675 read_bytes: 0 write_bytes: 323932160 cancelled_write_bytes: 0  </dd>
<dd>  The fields are as follows:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>rchar</i>: characters read </dt>
<dd>  The number of bytes which this task has caused to be read from storage. This is simply the sum of bytes which this process passed to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and similar system calls. It includes things such as terminal I/O and is unaffected by whether or not actual physical disk I/O was required (the read might have been satisfied from pagecache).  </dd>
<dt><i>wchar</i>: characters written </dt>
<dd>  The number of bytes which this task has caused, or shall cause to be written to disk. Similar caveats apply here as with <i>rchar</i>.  </dd>
<dt><i>syscr</i>: read syscalls </dt>
<dd>  Attempt to count the number of read I/O operations---that is, system calls such as <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2).  </dd>
<dt><i>syscw</i>: write syscalls </dt>
<dd>  Attempt to count the number of write I/O operations---that is, system calls such as <code><a href="/docs/linux/man/2-write/">write</a></code>(2) and <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2).  </dd>
<dt><i>read_bytes</i>: bytes read </dt>
<dd>  Attempt to count the number of bytes which this process really did cause to be fetched from the storage layer. This is accurate for block-backed filesystems.  </dd>
<dt><i>write_bytes</i>: bytes written </dt>
<dd>  Attempt to count the number of bytes which this process caused to be sent to the storage layer.  </dd>
<dt><i>cancelled_write_bytes</i>: </dt>
<dd>  The big inaccuracy here is truncate. If a process writes 1 MB to a file and then deletes the file, it will in fact perform no writeout. But it will have been accounted as having caused 1 MB of write. In other words: this field represents the number of bytes which this process caused to not happen, by truncating pagecache. A task can cause &quot;negative&quot; I/O too. If this task truncates some dirty pagecache, some I/O which another task has been accounted for (in its <i>write_bytes</i>) will not be happening.  </dd></dl>
 </dl>
 <dd>  <i>Note</i>: In the current implementation, things are a bit racy on 32-bit systems: if process A reads process B&#8217;s <i>/proc/[pid]/io</i> while process B is updating one of these 64-bit counters, process A could see an intermediate result.  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[pid]/limits</i> (since Linux 2.6.24) </dt>
<dd>  This file displays the soft limit, hard limit, and units of measurement for each of the process&#8217;s resource limits (see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)). Up to and including Linux 2.6.35, this file is protected to allow reading only by the real UID of the process. Since Linux 2.6.36, this file is readable by all users on the system.  </dd>
<dt><i>/proc/[pid]/map_files/</i> (since kernel 3.3) </dt>
<dd>  This subdirectory contains entries corresponding to memory-mapped files (see <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)). Entries are named by memory region start and end address pair (expressed as hexadecimal numbers), and are symbolic links to the mapped files themselves. Here is an example, with the output wrapped and reformatted to fit on an 80-column display:  </dd>
<dd>  #<code> ls -l /proc/self/map_files/</code> lr--------. 1 root root 64 Apr 16 21:31 <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3252e00000-3252e20000 -&gt;&nbsp;/usr/lib64/ld-2.15.so ...  </dd>
<dd>  Although these entries are present for memory regions that were mapped with the <code>MAP_FILE</code> flag, the way anonymous shared memory (regions created with the <code>MAP_ANON | MAP_SHARED</code> flags) is implemented in Linux means that such regions also appear on this directory. Here is an example where the target file is the deleted <i>/dev/zero</i> one:  </dd>
<dd>  lrw-------. 1 root root 64 Apr 16 21:33 <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7fc075d2f000-7fc075e6f000 -&gt;&nbsp;/dev/zero&nbsp;(deleted)  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dd>  Until kernel version 4.3, this directory appeared only if the <code>CONFIG_CHECKPOINT_RESTORE</code> kernel configuration option was enabled.  </dd>
<dd>  Capabilities are required to read the contents of the symbolic links in this directory: before Linux 5.9, the reading process requires <code>CAP_SYS_ADMIN</code> in the initial user namespace; since Linux 5.9, the reading process must have either <code>CAP_SYS_ADMIN</code> or <code>CAP_CHECKPOINT_RESTORE</code> in the user namespace where it resides.  </dd>
<dt><i>/proc/[pid]/maps</i> </dt>
<dd>  A file containing the currently mapped memory regions and their access permissions. See <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) for some further information about memory mappings.  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dd>  The format of the file is:  </dd>
<dd>  <i>address perms offset dev inode pathname</i> 00400000-00452000 r-xp 00000000 08:02 173521 /usr/bin/dbus-daemon 00651000-00652000 r--p 00051000 08:02 173521 /usr/bin/dbus-daemon 00652000-00655000 rw-p 00052000 08:02 173521 /usr/bin/dbus-daemon 00e03000-00e24000 rw-p 00000000 00:00 0 [heap] 00e24000-011f7000 rw-p 00000000 00:00 0 [heap] ... 35b1800000-35b1820000 r-xp 00000000 08:02 135522 /usr/lib64/ld-2.15.so 35b1a1f000-35b1a20000 r--p 0001f000 08:02 135522 /usr/lib64/ld-2.15.so 35b1a20000-35b1a21000 rw-p 00020000 08:02 135522 /usr/lib64/ld-2.15.so 35b1a21000-35b1a22000 rw-p 00000000 00:00 0 35b1c00000-35b1dac000 r-xp 00000000 08:02 135870 /usr/lib64/libc-2.15.so 35b1dac000-35b1fac000 ---p 001ac000 08:02 135870 /usr/lib64/libc-2.15.so 35b1fac000-35b1fb0000 r--p 001ac000 08:02 135870 /usr/lib64/libc-2.15.so 35b1fb0000-35b1fb2000 rw-p 001b0000 08:02 135870 /usr/lib64/libc-2.15.so ... f2c6ff8c000-7f2c7078c000 rw-p 00000000 00:00 0 [stack:986] ... 7fffb2c0d000-7fffb2c2e000 rw-p 00000000 00:00 0 [stack] 7fffb2d48000-7fffb2d49000 r-xp 00000000 00:00 0 [vdso]  </dd>
<dd>  The <i>address</i> field is the address space in the process that the mapping occupies. The <i>perms</i> field is a set of permissions:  </dd>
<dd>  r = read w = write x = execute s = shared p = private (copy on write)  </dd>
<dd>  The <i>offset</i> field is the offset into the file/whatever; <i>dev</i> is the device (major:minor); <i>inode</i> is the inode on that device. 0 indicates that no inode is associated with the memory region, as would be the case with BSS (uninitialized data).  </dd>
<dd>  The <i>pathname</i> field will usually be the file that is backing the mapping. For ELF files, you can easily coordinate with the <i>offset</i> field by looking at the Offset field in the ELF program headers (<i>readelf -l</i>).  </dd>
<dd>  There are additional helpful pseudo-paths:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>[stack]</i> </dt>
<dd>  The initial process&#8217;s (also known as the main thread&#8217;s) stack.  </dd>
<dt><i>[stack:&lt;tid&gt;]</i> (from Linux 3.4 to 4.4) </dt>
<dd>  A thread&#8217;s stack (where the <i>&lt;tid&gt;</i> is a thread ID). It corresponds to the <i>/proc/[pid]/task/[tid]/</i> path. This field was removed in Linux 4.5, since providing this information for a process with large numbers of threads is expensive.  </dd>
<dt><i>[vdso]</i> </dt>
<dd>  The virtual dynamically linked shared object. See <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).  </dd>
<dt><i>[heap]</i> </dt>
<dd>  The process&#8217;s heap.  </dd></dl>
 </dl>
 <dd>  If the <i>pathname</i> field is blank, this is an anonymous mapping as obtained via <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). There is no easy way to coordinate this back to a process&#8217;s source, short of running it through <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1), or similar.  </dd>
<dd>  <i>pathname</i> is shown unescaped except for newline characters, which are replaced with an octal escape sequence. As a result, it is not possible to determine whether the original pathname contained a newline character or the literal <i>\012</i> character sequence.  </dd>
<dd>  If the mapping is file-backed and the file has been deleted, the string &quot; (deleted)&quot; is appended to the pathname. Note that this is ambiguous too.  </dd>
<dd>  Under Linux 2.0, there is no field giving pathname.  </dd>
<dt><i>/proc/[pid]/mem</i> </dt>
<dd>  This file can be used to access the pages of a process&#8217;s memory through <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), and <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2).  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_ATTACH_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[pid]/mountinfo</i> (since Linux 2.6.26) </dt>
<dd>  This file contains information about mount points in the process&#8217;s mount namespace (see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7)). It supplies various information (e.g., propagation state, root of mount for bind mounts, identifier for each mount and its parent) that is missing from the (older) <i>/proc/[pid]/mounts</i> file, and fixes various other problems with that file (e.g., nonextensibility, failure to distinguish per-mount versus per-superblock options).  </dd>
<dd>  The file contains lines of the form:  </dd>
<dd>  36 35 98:0 /mnt1 /mnt2 rw,noatime master:1 &#8211; ext3 /dev/root rw,errors=continue (1)(2)(3) (4) (5) (6) (7) (8) (9) (10) (11)  </dd>
<dd>  The numbers in parentheses are labels for the descriptions below:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>(1)</dt>
<dd>  mount ID: a unique ID for the mount (may be reused after <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2)).  </dd>
<dt>(2)</dt>
<dd>  parent ID: the ID of the parent mount (or of self for the root of this mount namespace&#8217;s mount tree).  </dd>
<dd>  If a new mount is stacked on top of a previous existing mount (so that it hides the existing mount) at pathname P, then the parent of the new mount is the previous mount at that location. Thus, when looking at all the mounts stacked at a particular location, the top-most mount is the one that is not the parent of any other mount at the same location. (Note, however, that this top-most mount will be accessible only if the longest path subprefix of P that is a mount point is not itself hidden by a stacked mount.)  </dd>
<dd>  If the parent mount point lies outside the process&#8217;s root directory (see <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2)), the ID shown here won&#8217;t have a corresponding record in <i>mountinfo</i> whose mount ID (field 1) matches this parent mount ID (because mount points that lie outside the process&#8217;s root directory are not shown in <i>mountinfo</i>). As a special case of this point, the process&#8217;s root mount point may have a parent mount (for the initramfs filesystem) that lies outside the process&#8217;s root directory, and an entry for that mount point will not appear in <i>mountinfo</i>.  </dd>
<dt>(3)</dt>
<dd>  major:minor: the value of <i>st_dev</i> for files on this filesystem (see <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)).  </dd>
<dt>(4)</dt>
<dd>  root: the pathname of the directory in the filesystem which forms the root of this mount.  </dd>
<dt>(5)</dt>
<dd>  mount point: the pathname of the mount point relative to the process&#8217;s root directory.  </dd>
<dt>(6)</dt>
<dd>  mount options: per-mount options (see <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2)).  </dd>
<dt>(7)</dt>
<dd>  optional fields: zero or more fields of the form &quot;tag[:value]&quot;; see below.  </dd>
<dt>(8)</dt>
<dd>  separator: the end of the optional fields is marked by a single hyphen.  </dd>
<dt>(9)</dt>
<dd>  filesystem type: the filesystem type in the form &quot;type[.subtype]&quot;.  </dd>
<dt>(10)</dt>
<dd>  mount source: filesystem-specific information or &quot;none&quot;.  </dd>
<dt>(11)</dt>
<dd>  super options: per-superblock options (see <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2)).  </dd></dl>
 </dl>
 <dd>  Currently, the possible optional fields are <i>shared</i>, <i>master</i>, <i>propagate_from</i>, and <i>unbindable</i>. See <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7) for a description of these fields. Parsers should ignore all unrecognized optional fields.  </dd>
<dd>  For more information on mount propagation see: <i>Documentation/filesystems/sharedsubtree.txt</i> in the Linux kernel source tree.  </dd>
<dt><i>/proc/[pid]/mounts</i> (since Linux 2.4.19) </dt>
<dd>  This file lists all the filesystems currently mounted in the process&#8217;s mount namespace (see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7)). The format of this file is documented in <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5).  </dd>
<dd>  Since kernel version 2.6.15, this file is pollable: after opening the file for reading, a change in this file (i.e., a filesystem mount or unmount) causes <code><a href="/docs/linux/man/2-select/">select</a></code>(2) to mark the file descriptor as having an exceptional condition, and <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) and <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) mark the file as having a priority event (<code>POLLPRI</code>). (Before Linux 2.6.30, a change in this file was indicated by the file descriptor being marked as readable for <code><a href="/docs/linux/man/2-select/">select</a></code>(2), and being marked as having an error condition for <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) and <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2).)  </dd>
<dt><i>/proc/[pid]/mountstats</i> (since Linux 2.6.17) </dt>
<dd>  This file exports information (statistics, configuration information) about the mount points in the process&#8217;s mount namespace (see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7)). Lines in this file have the form:  </dd>
<dd>  device /dev/sda7 mounted on /home with fstype ext3 [stats] ( 1 ) ( 2 ) (3 ) ( 4 )  </dd>
<dd>  The fields in each line are:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>(1)</dt>
<dd>  The name of the mounted device (or &quot;nodevice&quot; if there is no corresponding device).  </dd>
<dt>(2)</dt>
<dd>  The mount point within the filesystem tree.  </dd>
<dt>(3)</dt>
<dd>  The filesystem type.  </dd>
<dt>(4)</dt>
<dd>  Optional statistics and configuration information. Currently (as at Linux 2.6.26), only NFS filesystems export information via this field.  </dd></dl>
 </dl>
 <dd>  This file is readable only by the owner of the process.  </dd>
<dt><i>/proc/[pid]/net</i> (since Linux 2.6.25) </dt>
<dd>  See the description of <i>/proc/net</i>.  </dd>
<dt><i>/proc/[pid]/ns/</i> (since Linux 3.0) </dt>
<dd>  This is a subdirectory containing one entry for each namespace that supports being manipulated by <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2). For more information, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7).  </dd>
<dt><i>/proc/[pid]/numa_maps</i> (since Linux 2.6.14) </dt>
<dd>  See <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7).  </dd>
<dt><i>/proc/[pid]/oom_adj</i> (since Linux 2.6.11) </dt>
<dd>  This file can be used to adjust the score used to select which process should be killed in an out-of-memory (OOM) situation. The kernel uses this value for a bit-shift operation of the process&#8217;s <i>oom_score</i> value: valid values are in the range -16 to +15, plus the special value -17, which disables OOM-killing altogether for this process. A positive score increases the likelihood of this process being killed by the OOM-killer; a negative score decreases the likelihood.  </dd>
<dd>  The default value for this file is 0; a new process inherits its parent&#8217;s <i>oom_adj</i> setting. A process must be privileged (<code>CAP_SYS_RESOURCE</code>) to update this file.  </dd>
<dd>  Since Linux 2.6.36, use of this file is deprecated in favor of <i>/proc/[pid]/oom_score_adj</i>.  </dd>
<dt><i>/proc/[pid]/oom_score</i> (since Linux 2.6.11) </dt>
<dd>  This file displays the current score that the kernel gives to this process for the purpose of selecting a process for the OOM-killer. A higher score means that the process is more likely to be selected by the OOM-killer. The basis for this score is the amount of memory used by the process, with increases (+) or decreases (-) for factors including:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>*</dt>
<dd>  whether the process is privileged (-).  </dd></dl>
 </dl>
 <dd>  Before kernel 2.6.36 the following factors were also used in the calculation of oom_score:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>*</dt>
<dd>  whether the process creates a lot of children using <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) (+);  </dd>
<dt>*</dt>
<dd>  whether the process has been running a long time, or has used a lot of CPU time (-);  </dd>
<dt>*</dt>
<dd>  whether the process has a low nice value (i.e., &gt; 0) (+); and  </dd>
<dt>*</dt>
<dd>  whether the process is making direct hardware access (-).  </dd></dl>
 </dl>
 <dd>  The <i>oom_score</i> also reflects the adjustment specified by the <i>oom_score_adj</i> or <i>oom_adj</i> setting for the process.  </dd>
<dt><i>/proc/[pid]/oom_score_adj</i> (since Linux 2.6.36) </dt>
<dd>  This file can be used to adjust the badness heuristic used to select which process gets killed in out-of-memory conditions.  </dd>
<dd>  The badness heuristic assigns a value to each candidate task ranging from 0 (never kill) to 1000 (always kill) to determine which process is targeted. The units are roughly a proportion along that range of allowed memory the process may allocate from, based on an estimation of its current memory and swap use. For example, if a task is using all allowed memory, its badness score will be 1000. If it is using half of its allowed memory, its score will be 500.  </dd>
<dd>  There is an additional factor included in the badness score: root processes are given 3% extra memory over other tasks.  </dd>
<dd>  The amount of &quot;allowed&quot; memory depends on the context in which the OOM-killer was called. If it is due to the memory assigned to the allocating task&#8217;s cpuset being exhausted, the allowed memory represents the set of mems assigned to that cpuset (see <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7)). If it is due to a mempolicy&#8217;s node(s) being exhausted, the allowed memory represents the set of mempolicy nodes. If it is due to a memory limit (or swap limit) being reached, the allowed memory is that configured limit. Finally, if it is due to the entire system being out of memory, the allowed memory represents all allocatable resources.  </dd>
<dd>  The value of <i>oom_score_adj</i> is added to the badness score before it is used to determine which task to kill. Acceptable values range from -1000 (OOM_SCORE_ADJ_MIN) to +1000 (OOM_SCORE_ADJ_MAX). This allows user space to control the preference for OOM-killing, ranging from always preferring a certain task or completely disabling it from OOM killing. The lowest possible value, -1000, is equivalent to disabling OOM-killing entirely for that task, since it will always report a badness score of 0.  </dd>
<dd>  Consequently, it is very simple for user space to define the amount of memory to consider for each task. Setting an <i>oom_score_adj</i> value of +500, for example, is roughly equivalent to allowing the remainder of tasks sharing the same system, cpuset, mempolicy, or memory controller resources to use at least 50% more memory. A value of -500, on the other hand, would be roughly equivalent to discounting 50% of the task&#8217;s allowed memory from being considered as scoring against the task.  </dd>
<dd>  For backward compatibility with previous kernels, <i>/proc/[pid]/oom_adj</i> can still be used to tune the badness score. Its value is scaled linearly with <i>oom_score_adj</i>.  </dd>
<dd>  Writing to <i>/proc/[pid]/oom_score_adj</i> or <i>/proc/[pid]/oom_adj</i> will change the other with its scaled value.  </dd>
<dd>  The <code><a href="/docs/linux/man/1-choom/">choom</a></code>(1) program provides a command-line interface for adjusting the <i>oom_score_adj</i> value of a running process or a newly executed command.  </dd>
<dt><i>/proc/[pid]/pagemap</i> (since Linux 2.6.25) </dt>
<dd>  This file shows the mapping of each of the process&#8217;s virtual pages into physical page frames or swap area. It contains one 64-bit value for each virtual page, with the bits set as follows:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>63</dt>
<dd>  If set, the page is present in RAM.  </dd>
<dt>62</dt>
<dd>  If set, the page is in swap space  </dd>
<dt>61 (since Linux 3.5)</dt>
<dd>  The page is a file-mapped page or a shared anonymous page.  </dd>
<dt>60-57 (since Linux 3.11)</dt>
<dd>  Zero  </dd>
<dt>56 (since Linux 4.2)</dt>
<dd>  The page is exclusively mapped.  </dd>
<dt>55 (since Linux 3.11)</dt>
<dd>  PTE is soft-dirty (see the kernel source file <i>Documentation/admin-guide/mm/soft-dirty.rst</i>).  </dd>
<dt>54-0</dt>
<dd>  If the page is present in RAM (bit 63), then these bits provide the page frame number, which can be used to index <i>/proc/kpageflags</i> and <i>/proc/kpagecount</i>. If the page is present in swap (bit 62), then bits 4-0 give the swap type, and bits 54-5 encode the swap offset.  </dd></dl>
 </dl>
 <dd>  Before Linux 3.11, bits 60-55 were used to encode the base-2 log of the page size.  </dd>
<dd>  To employ <i>/proc/[pid]/pagemap</i> efficiently, use <i>/proc/[pid]/maps</i> to determine which areas of memory are actually mapped and seek to skip over unmapped regions.  </dd>
<dd>  The <i>/proc/[pid]/pagemap</i> file is present only if the <code>CONFIG_PROC_PAGE_MONITOR</code> kernel configuration option is enabled.  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[pid]/personality</i> (since Linux 2.6.28) </dt>
<dd>  This read-only file exposes the process&#8217;s execution domain, as set by <code><a href="/docs/linux/man/2-personality/">personality</a></code>(2). The value is displayed in hexadecimal notation.  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_ATTACH_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[pid]/root</i> </dt>
<dd>  UNIX and Linux support the idea of a per-process root of the filesystem, set by the <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) system call. This file is a symbolic link that points to the process&#8217;s root directory, and behaves in the same way as <i>exe</i>, and <i>fd/*</i>.  </dd>
<dd>  Note however that this file is not merely a symbolic link. It provides the same view of the filesystem (including namespaces and the set of per-process mounts) as the process itself. An example illustrates this point. In one terminal, we start a shell in new user and mount namespaces, and in that shell we create some new mount points:  </dd>
<dd>  $ <code>PS1=&#8216;sh1# &#8216; unshare -Urnm</code> sh1# <code>mount -t tmpfs tmpfs /etc</code> # Mount empty tmpfs at /etc sh1# <code>mount --bind /usr /dev</code> # Mount /usr at /dev sh1# <code>echo $$</code> 27123  </dd>
<dd>  In a second terminal window, in the initial mount namespace, we look at the contents of the corresponding mounts in the initial and new namespaces:  </dd>
<dd>  $ <code>PS1=&#8216;sh2# &#8216; sudo sh</code> sh2# <code>ls /etc | wc -l</code> # In initial NS 309 sh2# <code>ls /proc/27123/root/etc | wc -l</code> # /etc in other NS 0 # The empty tmpfs dir sh2# <code>ls /dev | wc -l</code> # In initial NS 205 sh2# <code>ls /proc/27123/root/dev | wc -l</code> # /dev in other NS 11 # Actually bind <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;mounted to&nbsp;/usr sh2# <code>ls /usr | wc -l</code> # /usr in initial NS 11  </dd>
<dd>  In a multithreaded process, the contents of the <i>/proc/[pid]/root</i> symbolic link are not available if the main thread has already terminated (typically by calling <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3)).  </dd>
<dd>  Permission to dereference or read (<code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2)) this symbolic link is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[pid]/seccomp</i> (Linux 2.6.12 to 2.6.22) </dt>
<dd>  This file can be used to read and change the process&#8217;s secure computing (seccomp) mode setting. It contains the value 0 if the process is not in seccomp mode, and 1 if the process is in strict seccomp mode (see <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2)). Writing 1 to this file places the process irreversibly in strict seccomp mode. (Further attempts to write to the file fail with the <code>EPERM</code> error.)  </dd>
<dd>  In Linux 2.6.23, this file went away, to be replaced by the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_GET_SECCOMP</code> and <code>PR_SET_SECCOMP</code> operations (and later by <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) and the <i>Seccomp</i> field in <i>/proc/[pid]/status</i>).  </dd>
<dt><i>/proc/[pid]/setgroups</i> (since Linux 3.19) </dt>
<dd>  See <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).  </dd>
<dt><i>/proc/[pid]/smaps</i> (since Linux 2.6.14) </dt>
<dd>  This file shows memory consumption for each of the process&#8217;s mappings. (The <code><a href="/docs/linux/man/1-pmap/">pmap</a></code>(1) command displays similar information, in a form that may be easier for parsing.) For each mapping there is a series of lines such as the following:  </dd>
<dd>  00400000-0048a000 r-xp 00000000 fd:03 960637 /bin/bash Size: 552 kB Rss: 460 kB Pss: 100 kB Shared_Clean: 452 kB Shared_Dirty: 0 kB Private_Clean: 8 kB Private_Dirty: 0 kB Referenced: 460 kB Anonymous: 0 kB AnonHugePages: 0 kB ShmemHugePages: 0 kB ShmemPmdMapped: 0 kB Swap: 0 kB KernelPageSize: 4 kB MMUPageSize: 4 kB KernelPageSize: 4 kB MMUPageSize: 4 kB Locked: 0 kB ProtectionKey: 0 VmFlags: rd ex mr mw me dw  </dd>
<dd>  The first of these lines shows the same information as is displayed for the mapping in <i>/proc/[pid]/maps</i>. The following lines show the size of the mapping, the amount of the mapping that is currently resident in RAM (&quot;Rss&quot;), the process&#8217;s proportional share of this mapping (&quot;Pss&quot;), the number of clean and dirty shared pages in the mapping, and the number of clean and dirty private pages in the mapping. &quot;Referenced&quot; indicates the amount of memory currently marked as referenced or accessed. &quot;Anonymous&quot; shows the amount of memory that does not belong to any file. &quot;Swap&quot; shows how much would-be-anonymous memory is also used, but out on swap.  </dd>
<dd>  The &quot;KernelPageSize&quot; line (available since Linux 2.6.29) is the page size used by the kernel to back the virtual memory area. This matches the size used by the MMU in the majority of cases. However, one counter-example occurs on PPC64 kernels whereby a kernel using 64 kB as a base page size may still use 4 kB pages for the MMU on older processors. To distinguish the two attributes, the &quot;MMUPageSize&quot; line (also available since Linux 2.6.29) reports the page size used by the MMU.  </dd>
<dd>  The &quot;Locked&quot; indicates whether the mapping is locked in memory or not.  </dd>
<dd>  The &quot;ProtectionKey&quot; line (available since Linux 4.9, on x86 only) contains the memory protection key (see <code><a href="/docs/linux/man/7-pkeys/">pkeys</a></code>(7)) associated with the virtual memory area. This entry is present only if the kernel was built with the <code>CONFIG_X86_INTEL_MEMORY_PROTECTION_KEYS</code> configuration option (since Linux 4.6).  </dd>
<dd>  The &quot;VmFlags&quot; line (available since Linux 3.8) represents the kernel flags associated with the virtual memory area, encoded using the following two-letter codes:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rd&nbsp;<wbr>&nbsp;- readable <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wr&nbsp;<wbr>&nbsp;- writable <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ex&nbsp;<wbr>&nbsp;- executable <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh&nbsp;<wbr>&nbsp;- shared <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mr&nbsp;<wbr>&nbsp;- may read <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mw&nbsp;<wbr>&nbsp;- may write <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;me&nbsp;<wbr>&nbsp;- may execute <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ms&nbsp;<wbr>&nbsp;- may share <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gd&nbsp;<wbr>&nbsp;- stack segment grows down <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pf&nbsp;<wbr>&nbsp;- pure PFN range <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dw&nbsp;<wbr>&nbsp;- disabled write to the mapped file <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo&nbsp;<wbr>&nbsp;- pages are locked in memory <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;io&nbsp;<wbr>&nbsp;- memory mapped I/O area <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sr&nbsp;<wbr>&nbsp;- sequential read advise provided <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rr&nbsp;<wbr>&nbsp;- random read advise provided <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dc&nbsp;<wbr>&nbsp;- do not copy area on fork <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;de&nbsp;<wbr>&nbsp;- do not expand area on remapping <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ac&nbsp;<wbr>&nbsp;- area is accountable <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nr&nbsp;<wbr>&nbsp;- swap space is not reserved for the area <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ht&nbsp;<wbr>&nbsp;- area uses huge tlb pages <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sf&nbsp;<wbr>&nbsp;- perform synchronous page faults&nbsp;(since Linux 4.15) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nl&nbsp;<wbr>&nbsp;- non-linear mapping&nbsp;(removed in Linux 4.0) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ar&nbsp;<wbr>&nbsp;- architecture specific flag <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wf&nbsp;<wbr>&nbsp;- wipe on fork&nbsp;(since Linux 4.14) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dd&nbsp;<wbr>&nbsp;- do not include area into core dump <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sd&nbsp;<wbr>&nbsp;- soft-dirty flag&nbsp;(since Linux 3.13) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mm&nbsp;<wbr>&nbsp;- mixed map area <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hg&nbsp;<wbr>&nbsp;- huge page advise flag <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nh&nbsp;<wbr>&nbsp;- no-huge page advise flag <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mg&nbsp;<wbr>&nbsp;- mergeable advise flag <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;um&nbsp;<wbr>&nbsp;- userfaultfd missing pages tracking&nbsp;(since Linux 4.3) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uw&nbsp;<wbr>&nbsp;- userfaultfd wprotect pages tracking&nbsp;(since Linux 4.3)  </dd>
<dd>  The <i>/proc/[pid]/smaps</i> file is present only if the <code>CONFIG_PROC_PAGE_MONITOR</code> kernel configuration option is enabled.  </dd>
<dt><i>/proc/[pid]/stack</i> (since Linux 2.6.29) </dt>
<dd>  This file provides a symbolic trace of the function calls in this process&#8217;s kernel stack. This file is provided only if the kernel was built with the <code>CONFIG_STACKTRACE</code> configuration option.  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_ATTACH_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[pid]/stat</i> </dt>
<dd>  Status information about the process. This is used by <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). It is defined in the kernel source file <i>fs/proc/array.c</i>.  </dd>
<dd>  The fields, in order, with their proper <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) format specifiers, are listed below. Whether or not certain of these fields display valid information is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code>&nbsp;|&nbsp;<code>PTRACE_MODE_NOAUDIT</code> check (refer to <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)). If the check denies access, then the field value is displayed as 0. The affected fields are indicated with the marking [PT].  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>(1) <i>pid</i> &nbsp;%d</dt>
<dd>  <br />
 The process ID.  </dd>
<dt>(2) <i>comm</i> &nbsp;%s</dt>
<dd>  The filename of the executable, in parentheses. Strings longer than <code>TASK_COMM_LEN</code> (16) characters (including the terminating null byte) are silently truncated. This is visible whether or not the executable is swapped out.  </dd>
<dt>(3) <i>state</i> &nbsp;%c</dt>
<dd>  One of the following characters, indicating process state:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>R</dt>
<dd>  Running  </dd>
<dt>S</dt>
<dd>  Sleeping in an interruptible wait  </dd>
<dt>D</dt>
<dd>  Waiting in uninterruptible disk sleep  </dd>
<dt>Z</dt>
<dd>  Zombie  </dd>
<dt>T</dt>
<dd>  Stopped (on a signal) or (before Linux 2.6.33) trace stopped  </dd>
<dt>t</dt>
<dd>  Tracing stop (Linux 2.6.33 onward)  </dd>
<dt>W</dt>
<dd>  Paging (only before Linux 2.6.0)  </dd>
<dt>X</dt>
<dd>  Dead (from Linux 2.6.0 onward)  </dd>
<dt>x</dt>
<dd>  Dead (Linux 2.6.33 to 3.13 only)  </dd>
<dt>K</dt>
<dd>  Wakekill (Linux 2.6.33 to 3.13 only)  </dd>
<dt>W</dt>
<dd>  Waking (Linux 2.6.33 to 3.13 only)  </dd>
<dt>P</dt>
<dd>  Parked (Linux 3.9 to 3.13 only)  </dd></dl>
 </dl>
 <dt>(4) <i>ppid</i> &nbsp;%d</dt>
<dd>  The PID of the parent of this process.  </dd>
<dt>(5) <i>pgrp</i> &nbsp;%d</dt>
<dd>  The process group ID of the process.  </dd>
<dt>(6) <i>session</i> &nbsp;%d</dt>
<dd>  The session ID of the process.  </dd>
<dt>(7) <i>tty_nr</i> &nbsp;%d</dt>
<dd>  The controlling terminal of the process. (The minor device number is contained in the combination of bits 31 to 20 and 7 to 0; the major device number is in bits 15 to 8.)  </dd>
<dt>(8) <i>tpgid</i> &nbsp;%d</dt>
<dd>  The ID of the foreground process group of the controlling terminal of the process.  </dd>
<dt>(9) <i>flags</i> &nbsp;%u</dt>
<dd>  The kernel flags word of the process. For bit meanings, see the PF_* defines in the Linux kernel source file <i>include/linux/sched.h</i>. Details depend on the kernel version.  </dd>
<dd>  The format for this field was %lu before Linux 2.6.  </dd>
<dt>(10) <i>minflt</i> &nbsp;%lu</dt>
<dd>  The number of minor faults the process has made which have not required loading a memory page from disk.  </dd>
<dt>(11) <i>cminflt</i> &nbsp;%lu</dt>
<dd>  The number of minor faults that the process&#8217;s waited-for children have made.  </dd>
<dt>(12) <i>majflt</i> &nbsp;%lu</dt>
<dd>  The number of major faults the process has made which have required loading a memory page from disk.  </dd>
<dt>(13) <i>cmajflt</i> &nbsp;%lu</dt>
<dd>  The number of major faults that the process&#8217;s waited-for children have made.  </dd>
<dt>(14) <i>utime</i> &nbsp;%lu</dt>
<dd>  Amount of time that this process has been scheduled in user mode, measured in clock ticks (divide by <i>sysconf(_SC_CLK_TCK)</i>). This includes guest time, <i>guest_time</i> (time spent running a virtual CPU, see below), so that applications that are not aware of the guest time field do not lose that time from their calculations.  </dd>
<dt>(15) <i>stime</i> &nbsp;%lu</dt>
<dd>  Amount of time that this process has been scheduled in kernel mode, measured in clock ticks (divide by <i>sysconf(_SC_CLK_TCK)</i>).  </dd>
<dt>(16) <i>cutime</i> &nbsp;%ld</dt>
<dd>  Amount of time that this process&#8217;s waited-for children have been scheduled in user mode, measured in clock ticks (divide by <i>sysconf(_SC_CLK_TCK)</i>). (See also <code><a href="/docs/linux/man/2-times/">times</a></code>(2).) This includes guest time, <i>cguest_time</i> (time spent running a virtual CPU, see below).  </dd>
<dt>(17) <i>cstime</i> &nbsp;%ld</dt>
<dd>  Amount of time that this process&#8217;s waited-for children have been scheduled in kernel mode, measured in clock ticks (divide by <i>sysconf(_SC_CLK_TCK)</i>).  </dd>
<dt>(18) <i>priority</i> &nbsp;%ld</dt>
<dd>  (Explanation for Linux 2.6) For processes running a real-time scheduling policy (<i>policy</i> below; see <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2)), this is the negated scheduling priority, minus one; that is, a number in the range -2 to -100, corresponding to real-time priorities 1 to 99. For processes running under a non-real-time scheduling policy, this is the raw nice value (<code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2)) as represented in the kernel. The kernel stores nice values as numbers in the range 0 (high) to 39 (low), corresponding to the user-visible nice range of -20 to 19.  </dd>
<dd>  Before Linux 2.6, this was a scaled value based on the scheduler weighting given to this process.  </dd>
<dt>(19) <i>nice</i> &nbsp;%ld</dt>
<dd>  The nice value (see <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2)), a value in the range 19 (low priority) to -20 (high priority).  </dd>
<dt>(20) <i>num_threads</i> &nbsp;%ld</dt>
<dd>  Number of threads in this process (since Linux 2.6). Before kernel 2.6, this field was hard coded to 0 as a placeholder for an earlier removed field.  </dd>
<dt>(21) <i>itrealvalue</i> &nbsp;%ld</dt>
<dd>  The time in jiffies before the next <code>SIGALRM</code> is sent to the process due to an interval timer. Since kernel 2.6.17, this field is no longer maintained, and is hard coded as 0.  </dd>
<dt>(22) <i>starttime</i> &nbsp;%llu</dt>
<dd>  The time the process started after system boot. In kernels before Linux 2.6, this value was expressed in jiffies. Since Linux 2.6, the value is expressed in clock ticks (divide by <i>sysconf(_SC_CLK_TCK)</i>).  </dd>
<dd>  The format for this field was %lu before Linux 2.6.  </dd>
<dt>(23) <i>vsize</i> &nbsp;%lu</dt>
<dd>  Virtual memory size in bytes.  </dd>
<dt>(24) <i>rss</i> &nbsp;%ld</dt>
<dd>  Resident Set Size: number of pages the process has in real memory. This is just the pages which count toward text, data, or stack space. This does not include pages which have not been demand-loaded in, or which are swapped out. This value is inaccurate; see <i>/proc/[pid]/statm</i> below.  </dd>
<dt>(25) <i>rsslim</i> &nbsp;%lu</dt>
<dd>  Current soft limit in bytes on the rss of the process; see the description of <code>RLIMIT_RSS</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2).  </dd>
<dt>(26) <i>startcode</i> &nbsp;%lu &nbsp;[PT]</dt>
<dd>  The address above which program text can run.  </dd>
<dt>(27) <i>endcode</i> &nbsp;%lu &nbsp;[PT]</dt>
<dd>  The address below which program text can run.  </dd>
<dt>(28) <i>startstack</i> &nbsp;%lu &nbsp;[PT]</dt>
<dd>  The address of the start (i.e., bottom) of the stack.  </dd>
<dt>(29) <i>kstkesp</i> &nbsp;%lu &nbsp;[PT]</dt>
<dd>  The current value of ESP (stack pointer), as found in the kernel stack page for the process.  </dd>
<dt>(30) <i>kstkeip</i> &nbsp;%lu &nbsp;[PT]</dt>
<dd>  The current EIP (instruction pointer).  </dd>
<dt>(31) <i>signal</i> &nbsp;%lu</dt>
<dd>  The bitmap of pending signals, displayed as a decimal number. Obsolete, because it does not provide information on real-time signals; use <i>/proc/[pid]/status</i> instead.  </dd>
<dt>(32) <i>blocked</i> &nbsp;%lu</dt>
<dd>  The bitmap of blocked signals, displayed as a decimal number. Obsolete, because it does not provide information on real-time signals; use <i>/proc/[pid]/status</i> instead.  </dd>
<dt>(33) <i>sigignore</i> &nbsp;%lu</dt>
<dd>  The bitmap of ignored signals, displayed as a decimal number. Obsolete, because it does not provide information on real-time signals; use <i>/proc/[pid]/status</i> instead.  </dd>
<dt>(34) <i>sigcatch</i> &nbsp;%lu</dt>
<dd>  The bitmap of caught signals, displayed as a decimal number. Obsolete, because it does not provide information on real-time signals; use <i>/proc/[pid]/status</i> instead.  </dd>
<dt>(35) <i>wchan</i> &nbsp;%lu &nbsp;[PT]</dt>
<dd>  This is the &quot;channel&quot; in which the process is waiting. It is the address of a location in the kernel where the process is sleeping. The corresponding symbolic name can be found in <i>/proc/[pid]/wchan</i>.  </dd>
<dt>(36) <i>nswap</i> &nbsp;%lu</dt>
<dd>  Number of pages swapped (not maintained).  </dd>
<dt>(37) <i>cnswap</i> &nbsp;%lu</dt>
<dd>  Cumulative <i>nswap</i> for child processes (not maintained).  </dd>
<dt>(38) <i>exit_signal</i> &nbsp;%d &nbsp;(since Linux 2.1.22)</dt>
<dd>  Signal to be sent to parent when we die.  </dd>
<dt>(39) <i>processor</i> &nbsp;%d &nbsp;(since Linux 2.2.8)</dt>
<dd>  CPU number last executed on.  </dd>
<dt>(40) <i>rt_priority</i> &nbsp;%u &nbsp;(since Linux 2.5.19)</dt>
<dd>  Real-time scheduling priority, a number in the range 1 to 99 for processes scheduled under a real-time policy, or 0, for non-real-time processes (see <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2)).  </dd>
<dt>(41) <i>policy</i> &nbsp;%u &nbsp;(since Linux 2.5.19)</dt>
<dd>  Scheduling policy (see <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2)). Decode using the SCHED_* constants in <i>linux/sched.h</i>.  </dd>
<dd>  The format for this field was %lu before Linux 2.6.22.  </dd>
<dt>(42) <i>delayacct_blkio_ticks</i> &nbsp;%llu &nbsp;(since Linux 2.6.18)</dt>
<dd>  Aggregated block I/O delays, measured in clock ticks (centiseconds).  </dd>
<dt>(43) <i>guest_time</i> &nbsp;%lu &nbsp;(since Linux 2.6.24)</dt>
<dd>  Guest time of the process (time spent running a virtual CPU for a guest operating system), measured in clock ticks (divide by <i>sysconf(_SC_CLK_TCK)</i>).  </dd>
<dt>(44) <i>cguest_time</i> &nbsp;%ld &nbsp;(since Linux 2.6.24)</dt>
<dd>  Guest time of the process&#8217;s children, measured in clock ticks (divide by <i>sysconf(_SC_CLK_TCK)</i>).  </dd>
<dt>(45) <i>start_data</i> &nbsp;%lu &nbsp;(since Linux 3.3) &nbsp;[PT]</dt>
<dd>  Address above which program initialized and uninitialized (BSS) data are placed.  </dd>
<dt>(46) <i>end_data</i> &nbsp;%lu &nbsp;(since Linux 3.3) &nbsp;[PT]</dt>
<dd>  Address below which program initialized and uninitialized (BSS) data are placed.  </dd>
<dt>(47) <i>start_brk</i> &nbsp;%lu &nbsp;(since Linux 3.3) &nbsp;[PT]</dt>
<dd>  Address above which program heap can be expanded with <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2).  </dd>
<dt>(48) <i>arg_start</i> &nbsp;%lu &nbsp;(since Linux 3.5) &nbsp;[PT]</dt>
<dd>  Address above which program command-line arguments (<i>argv</i>) are placed.  </dd>
<dt>(49) <i>arg_end</i> &nbsp;%lu &nbsp;(since Linux 3.5) &nbsp;[PT]</dt>
<dd>  Address below program command-line arguments (<i>argv</i>) are placed.  </dd>
<dt>(50) <i>env_start</i> &nbsp;%lu &nbsp;(since Linux 3.5) &nbsp;[PT]</dt>
<dd>  Address above which program environment is placed.  </dd>
<dt>(51) <i>env_end</i> &nbsp;%lu &nbsp;(since Linux 3.5) &nbsp;[PT]</dt>
<dd>  Address below which program environment is placed.  </dd>
<dt>(52) <i>exit_code</i> &nbsp;%d &nbsp;(since Linux 3.5) &nbsp;[PT]</dt>
<dd>  The thread&#8217;s exit status in the form reported by <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2).  </dd></dl>
 </dl>
 <dt><i>/proc/[pid]/statm</i> </dt>
<dd>  Provides information about memory usage, measured in pages. The columns are:  </dd>
<dd>  size (1) total program size <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(same as VmSize in&nbsp;<i>/proc/[pid]/status</i>) resident (2) resident set size <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(inaccurate;&nbsp;same as VmRSS in&nbsp;<i>/proc/[pid]/status</i>) shared (3) number of resident shared pages <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(i.e., backed by a file) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(inaccurate;&nbsp;same as RssFile+RssShmem in <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>/proc/[pid]/status</i>) text (4) text (code) lib (5) library (unused since Linux 2.6; always 0) data (6) data + stack dt (7) dirty pages (unused since Linux 2.6; always 0)  </dd>
<dd>  Some of these values are inaccurate because of a kernel-internal scalability optimization. If accurate values are required, use <i>/proc/[pid]/smaps</i> or <i>/proc/[pid]/smaps_rollup</i> instead, which are much slower but provide accurate, detailed information.  </dd>
<dt><i>/proc/[pid]/status</i> </dt>
<dd>  Provides much of the information in <i>/proc/[pid]/stat</i> and <i>/proc/[pid]/statm</i> in a format that&#8217;s easier for humans to parse. Here&#8217;s an example:  </dd>
<dd>  $<code> cat /proc/$$/status</code> Name: bash Umask: 0022 State: S (sleeping) Tgid: 17248 Ngid: 0 Pid: 17248 PPid: 17200 TracerPid: 0 Uid: 1000 1000 1000 1000 Gid: 100 100 100 100 FDSize: 256 Groups: 16 33 100 NStgid: 17248 NSpid: 17248 NSpgid: 17248 NSsid: 17200 VmPeak:<code>&nbsp;</code> 131168 kB<br />
 VmSize:<code>&nbsp;</code> 131168 kB<br />
 VmLck:<code>&nbsp;<wbr>&nbsp;</code> 0 kB<br />
 VmPin:<code>&nbsp;<wbr>&nbsp;</code> 0 kB<br />
 VmHWM:<code>&nbsp;<wbr>&nbsp;</code> 13484 kB<br />
 VmRSS:<code>&nbsp;<wbr>&nbsp;</code> 13484 kB<br />
 RssAnon:<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code> 10264 kB<br />
 RssFile:<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code> 3220 kB<br />
 RssShmem:<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code> 0 kB<br />
 VmData:<code>&nbsp;</code> 10332 kB<br />
 VmStk:<code>&nbsp;<wbr>&nbsp;</code> 136 kB<br />
 VmExe:<code>&nbsp;<wbr>&nbsp;</code> 992 kB<br />
 VmLib:<code>&nbsp;<wbr>&nbsp;</code> 2104 kB<br />
 VmPTE:<code>&nbsp;<wbr>&nbsp;</code> 76 kB<br />
 VmPMD:<code>&nbsp;<wbr>&nbsp;</code> 12 kB<br />
 VmSwap:<code>&nbsp;</code> 0 kB<br />
 HugetlbPages: 0 kB <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code># 4.4<br />
 CoreDumping:<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0 # 4.15<br />
 Threads: 1 SigQ: 0/3067 SigPnd: 0000000000000000 ShdPnd: 0000000000000000 SigBlk: 0000000000010000 SigIgn: 0000000000384004 SigCgt: 000000004b813efb CapInh: 0000000000000000 CapPrm: 0000000000000000 CapEff: 0000000000000000 CapBnd: ffffffffffffffff CapAmb:<code>&nbsp;</code>0000000000000000<br />
 NoNewPrivs: 0 Seccomp: 0 Speculation_Store_Bypass: vulnerable Cpus_allowed: 00000001 Cpus_allowed_list: 0 Mems_allowed: 1 Mems_allowed_list: 0 voluntary_ctxt_switches: 150 nonvoluntary_ctxt_switches: 545  </dd>
<dd>  The fields are as follows:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>Name</i> </dt>
<dd>  Command run by this process. Strings longer than <code>TASK_COMM_LEN</code> (16) characters (including the terminating null byte) are silently truncated.  </dd>
<dt><i>Umask</i> </dt>
<dd>  Process umask, expressed in octal with a leading zero; see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2). (Since Linux 4.7.)  </dd>
<dt><i>State</i> </dt>
<dd>  Current state of the process. One of &quot;R (running)&quot;, &quot;S (sleeping)&quot;, &quot;D (disk sleep)&quot;, &quot;T (stopped)&quot;, &quot;t (tracing stop)&quot;, &quot;Z (zombie)&quot;, or &quot;X (dead)&quot;.  </dd>
<dt><i>Tgid</i> </dt>
<dd>  Thread group ID (i.e., Process ID).  </dd>
<dt><i>Ngid</i> </dt>
<dd>  NUMA group ID (0 if none; since Linux 3.13).  </dd>
<dt><i>Pid</i> </dt>
<dd>  Thread ID (see <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2)).  </dd>
<dt><i>PPid</i> </dt>
<dd>  PID of parent process.  </dd>
<dt><i>TracerPid</i> </dt>
<dd>  PID of process tracing this process (0 if not being traced).  </dd>
<dt><i>Uid</i>, <i>Gid</i> </dt>
<dd>  Real, effective, saved set, and filesystem UIDs (GIDs).  </dd>
<dt><i>FDSize</i> </dt>
<dd>  Number of file descriptor slots currently allocated.  </dd>
<dt><i>Groups</i> </dt>
<dd>  Supplementary group list.  </dd>
<dt><i>NStgid</i> </dt>
<dd>  Thread group ID (i.e., PID) in each of the PID namespaces of which <i>[pid]</i> is a member. The leftmost entry shows the value with respect to the PID namespace of the process that mounted this procfs (or the root namespace if mounted by the kernel), followed by the value in successively nested inner namespaces. (Since Linux 4.1.)  </dd>
<dt><i>NSpid</i> </dt>
<dd>  Thread ID in each of the PID namespaces of which <i>[pid]</i> is a member. The fields are ordered as for <i>NStgid</i>. (Since Linux 4.1.)  </dd>
<dt><i>NSpgid</i> </dt>
<dd>  Process group ID in each of the PID namespaces of which <i>[pid]</i> is a member. The fields are ordered as for <i>NStgid</i>. (Since Linux 4.1.)  </dd>
<dt><i>NSsid</i> </dt>
<dd>  descendant namespace session ID hierarchy Session ID in each of the PID namespaces of which <i>[pid]</i> is a member. The fields are ordered as for <i>NStgid</i>. (Since Linux 4.1.)  </dd>
<dt><i>VmPeak</i> </dt>
<dd>  Peak virtual memory size.  </dd>
<dt><i>VmSize</i> </dt>
<dd>  Virtual memory size.  </dd>
<dt><i>VmLck</i> </dt>
<dd>  Locked memory size (see <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2)).  </dd>
<dt><i>VmPin</i> </dt>
<dd>  Pinned memory size (since Linux 3.2). These are pages that can&#8217;t be moved because something needs to directly access physical memory.  </dd>
<dt><i>VmHWM</i> </dt>
<dd>  Peak resident set size (&quot;high water mark&quot;). This value is inaccurate; see <i>/proc/[pid]/statm</i> above.  </dd>
<dt><i>VmRSS</i> </dt>
<dd>  Resident set size. Note that the value here is the sum of <i>RssAnon</i>, <i>RssFile</i>, and <i>RssShmem</i>. This value is inaccurate; see <i>/proc/[pid]/statm</i> above.  </dd>
<dt><i>RssAnon</i> </dt>
<dd>  Size of resident anonymous memory. (since Linux 4.5). This value is inaccurate; see <i>/proc/[pid]/statm</i> above.  </dd>
<dt><i>RssFile</i> </dt>
<dd>  Size of resident file mappings. (since Linux 4.5). This value is inaccurate; see <i>/proc/[pid]/statm</i> above.  </dd>
<dt><i>RssShmem</i> </dt>
<dd>  Size of resident shared memory (includes System V shared memory, mappings from <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5), and shared anonymous mappings). (since Linux 4.5).  </dd>
<dt><i>VmData</i>, <i>VmStk</i>, <i>VmExe</i> </dt>
<dd>  Size of data, stack, and text segments. This value is inaccurate; see <i>/proc/[pid]/statm</i> above.  </dd>
<dt><i>VmLib</i> </dt>
<dd>  Shared library code size.  </dd>
<dt><i>VmPTE</i> </dt>
<dd>  Page table entries size (since Linux 2.6.10).  </dd>
<dt><i>VmPMD</i> </dt>
<dd>  Size of second-level page tables (added in Linux 4.0; removed in Linux 4.15).  </dd>
<dt><i>VmSwap</i> </dt>
<dd>  Swapped-out virtual memory size by anonymous private pages; shmem swap usage is not included (since Linux 2.6.34). This value is inaccurate; see <i>/proc/[pid]/statm</i> above.  </dd>
<dt><i>HugetlbPages</i> </dt>
<dd>  Size of hugetlb memory portions (since Linux 4.4).  </dd>
<dt><i>CoreDumping</i> </dt>
<dd>  Contains the value 1 if the process is currently dumping core, and 0 if it is not (since Linux 4.15). This information can be used by a monitoring process to avoid killing a process that is currently dumping core, which could result in a corrupted core dump file.  </dd>
<dt><i>Threads</i> </dt>
<dd>  Number of threads in process containing this thread.  </dd>
<dt><i>SigQ</i> </dt>
<dd>  This field contains two slash-separated numbers that relate to queued signals for the real user ID of this process. The first of these is the number of currently queued signals for this real user ID, and the second is the resource limit on the number of queued signals for this process (see the description of <code>RLIMIT_SIGPENDING</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).  </dd>
<dt><i>SigPnd</i>, <i>ShdPnd</i> </dt>
<dd>  Mask (expressed in hexadecimal) of signals pending for thread and for process as a whole (see <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7) and <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)).  </dd>
<dt><i>SigBlk</i>, <i>SigIgn</i>, <i>SigCgt</i> </dt>
<dd>  Masks (expressed in hexadecimal) indicating signals being blocked, ignored, and caught (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)).  </dd>
<dt><i>CapInh</i>, <i>CapPrm</i>, <i>CapEff</i> </dt>
<dd>  Masks (expressed in hexadecimal) of capabilities enabled in inheritable, permitted, and effective sets (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)).  </dd>
<dt><i>CapBnd</i> </dt>
<dd>  Capability bounding set, expressed in hexadecimal (since Linux 2.6.26, see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)).  </dd>
<dt><i>CapAmb</i> </dt>
<dd>  Ambient capability set, expressed in hexadecimal (since Linux 4.3, see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)).  </dd>
<dt><i>NoNewPrivs</i> </dt>
<dd>  Value of the <i>no_new_privs</i> bit (since Linux 4.10, see <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2)).  </dd>
<dt><i>Seccomp</i> </dt>
<dd>  Seccomp mode of the process (since Linux 3.8, see <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2)). 0 means <code>SECCOMP_MODE_DISABLED</code>; 1 means <code>SECCOMP_MODE_STRICT</code>; 2 means <code>SECCOMP_MODE_FILTER</code>. This field is provided only if the kernel was built with the <code>CONFIG_SECCOMP</code> kernel configuration option enabled.  </dd>
<dt><i>Speculation_Store_Bypass</i> </dt>
<dd>  Speculation flaw mitigation state (since Linux 4.17, see <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2)).  </dd>
<dt><i>Cpus_allowed</i> </dt>
<dd>  Hexadecimal mask of CPUs on which this process may run (since Linux 2.6.24, see <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7)).  </dd>
<dt><i>Cpus_allowed_list</i> </dt>
<dd>  Same as previous, but in &quot;list format&quot; (since Linux 2.6.26, see <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7)).  </dd>
<dt><i>Mems_allowed</i> </dt>
<dd>  Mask of memory nodes allowed to this process (since Linux 2.6.24, see <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7)).  </dd>
<dt><i>Mems_allowed_list</i> </dt>
<dd>  Same as previous, but in &quot;list format&quot; (since Linux 2.6.26, see <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7)).  </dd>
<dt><i>voluntary_ctxt_switches</i>, <i>nonvoluntary_ctxt_switches</i> </dt>
<dd>  Number of voluntary and involuntary context switches (since Linux 2.6.23).  </dd></dl>
 </dl>
 <dt><i>/proc/[pid]/syscall</i> (since Linux 2.6.27) </dt>
<dd>  This file exposes the system call number and argument registers for the system call currently being executed by the process, followed by the values of the stack pointer and program counter registers. The values of all six argument registers are exposed, although most system calls use fewer registers.  </dd>
<dd>  If the process is blocked, but not in a system call, then the file displays -1 in place of the system call number, followed by just the values of the stack pointer and program counter. If process is not blocked, then the file contains just the string &quot;running&quot;.  </dd>
<dd>  This file is present only if the kernel was configured with <code>CONFIG_HAVE_ARCH_TRACEHOOK</code>.  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_ATTACH_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[pid]/task</i> (since Linux 2.6.0) </dt>
<dd>  This is a directory that contains one subdirectory for each thread in the process. The name of each subdirectory is the numerical thread ID (<i>[tid]</i>) of the thread (see <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2)).  </dd>
<dd>  Within each of these subdirectories, there is a set of files with the same names and contents as under the <i>/proc/[pid]</i> directories. For attributes that are shared by all threads, the contents for each of the files under the <i>task/[tid]</i> subdirectories will be the same as in the corresponding file in the parent <i>/proc/[pid]</i> directory (e.g., in a multithreaded process, all of the <i>task/[tid]/cwd</i> files will have the same value as the <i>/proc/[pid]/cwd</i> file in the parent directory, since all of the threads in a process share a working directory). For attributes that are distinct for each thread, the corresponding files under <i>task/[tid]</i> may have different values (e.g., various fields in each of the <i>task/[tid]/status</i> files may be different for each thread), or they might not exist in <i>/proc/[pid]</i> at all.  </dd>
<dd>  In a multithreaded process, the contents of the <i>/proc/[pid]/task</i> directory are not available if the main thread has already terminated (typically by calling <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3)).  </dd>
<dt><i>/proc/[pid]/task/[tid]/children</i> (since Linux 3.5) </dt>
<dd>  A space-separated list of child tasks of this task. Each child task is represented by its TID.  </dd>
<dd>  This option is intended for use by the checkpoint-restore (CRIU) system, and reliably provides a list of children only if all of the child processes are stopped or frozen. It does not work properly if children of the target task exit while the file is being read! Exiting children may cause non-exiting children to be omitted from the list. This makes this interface even more unreliable than classic PID-based approaches if the inspected task and its children aren&#8217;t frozen, and most code should probably not use this interface.  </dd>
<dd>  Until Linux 4.2, the presence of this file was governed by the <code>CONFIG_CHECKPOINT_RESTORE</code> kernel configuration option. Since Linux 4.2, it is governed by the <code>CONFIG_PROC_CHILDREN</code> option.  </dd>
<dt><i>/proc/[pid]/timers</i> (since Linux 3.10) </dt>
<dd>  A list of the POSIX timers for this process. Each timer is listed with a line that starts with the string &quot;ID:&quot;. For example:  </dd>
<dd>  ID: 1 signal: 60/00007fff86e452a8 notify: signal/pid.2634 ClockID: 0 ID: 0 signal: 60/00007fff86e452a8 notify: signal/pid.2634 ClockID: 1  </dd>
<dd>  The lines shown for each timer have the following meanings:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>ID</i> </dt>
<dd>  The ID for this timer. This is not the same as the timer ID returned by <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2); rather, it is the same kernel-internal ID that is available via the <i>si_timerid</i> field of the <i>siginfo_t</i> structure (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)).  </dd>
<dt><i>signal</i> </dt>
<dd>  This is the signal number that this timer uses to deliver notifications followed by a slash, and then the <i>sigev_value</i> value supplied to the signal handler. Valid only for timers that notify via a signal.  </dd>
<dt><i>notify</i> </dt>
<dd>  The part before the slash specifies the mechanism that this timer uses to deliver notifications, and is one of &quot;thread&quot;, &quot;signal&quot;, or &quot;none&quot;. Immediately following the slash is either the string &quot;tid&quot; for timers with <code>SIGEV_THREAD_ID</code> notification, or &quot;pid&quot; for timers that notify by other mechanisms. Following the &quot;.&quot; is the PID of the process (or the kernel thread ID of the thread) that will be delivered a signal if the timer delivers notifications via a signal.  </dd>
<dt><i>ClockID</i> </dt>
<dd>  This field identifies the clock that the timer uses for measuring time. For most clocks, this is a number that matches one of the user-space <code>CLOCK_*</code> constants exposed via <i>&lt;time.h&gt;</i>. <code>CLOCK_PROCESS_CPUTIME_ID</code> timers display with a value of -6 in this field. <code>CLOCK_THREAD_CPUTIME_ID</code> timers display with a value of -2 in this field.  </dd></dl>
 </dl>
 <dd>  This file is available only when the kernel was configured with <code>CONFIG_CHECKPOINT_RESTORE</code>.  </dd>
<dt><i>/proc/[pid]/timerslack_ns</i> (since Linux 4.6) </dt>
<dd>  This file exposes the process&#8217;s &quot;current&quot; timer slack value, expressed in nanoseconds. The file is writable, allowing the process&#8217;s timer slack value to be changed. Writing 0 to this file resets the &quot;current&quot; timer slack to the &quot;default&quot; timer slack value. For further details, see the discussion of <code>PR_SET_TIMERSLACK</code> in <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2).  </dd>
<dd>  Initially, permission to access this file was governed by a ptrace access mode <code>PTRACE_MODE_ATTACH_FSCREDS</code> check (see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)). However, this was subsequently deemed too strict a requirement (and had the side effect that requiring a process to have the <code>CAP_SYS_PTRACE</code> capability would also allow it to view and change any process&#8217;s memory). Therefore, since Linux 4.9, only the (weaker) <code>CAP_SYS_NICE</code> capability is required to access this file.  </dd>
<dt><i>/proc/[pid]/uid_map</i>, <i>/proc/[pid]/gid_map</i> (since Linux 3.5) </dt>
<dd>  See <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).  </dd>
<dt><i>/proc/[pid]/wchan</i> (since Linux 2.6.0) </dt>
<dd>  The symbolic name corresponding to the location in the kernel where the process is sleeping.  </dd>
<dd>  Permission to access this file is governed by a ptrace access mode <code>PTRACE_MODE_READ_FSCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/[tid]</i> </dt>
<dd>  There is a numerical subdirectory for each running thread that is not a thread group leader (i.e., a thread whose thread ID is not the same as its process ID); the subdirectory is named by the thread ID. Each one of these subdirectories contains files and subdirectories exposing information about the thread with the thread ID <i>tid</i>. The contents of these directories are the same as the corresponding <i>/proc/[pid]/task/[tid]</i> directories.  </dd>
<dd>  The <i>/proc/[tid]</i> subdirectories are <i>not</i> visible when iterating through <i>/proc</i> with <code><a href="/docs/linux/man/2-getdents/">getdents</a></code>(2) (and thus are <i>not</i> visible when one uses <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) to view the contents of <i>/proc</i>). However, the pathnames of these directories are visible to (i.e., usable as arguments in) system calls that operate on pathnames.  </dd>
<dt><i>/proc/apm</i> </dt>
<dd>  Advanced power management version and battery information when <code>CONFIG_APM</code> is defined at kernel compilation time.  </dd>
<dt><i>/proc/buddyinfo</i> </dt>
<dd>  This file contains information which is used for diagnosing memory fragmentation issues. Each line starts with the identification of the node and the name of the zone which together identify a memory region. This is then followed by the count of available chunks of a certain order in which these zones are split. The size in bytes of a certain order is given by the formula:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(2^order)&nbsp;*&nbsp;PAGE_SIZE  </dd>
<dd>  The binary buddy allocator algorithm inside the kernel will split one chunk into two chunks of a smaller order (thus with half the size) or combine two contiguous chunks into one larger chunk of a higher order (thus with double the size) to satisfy allocation requests and to counter memory fragmentation. The order matches the column number, when starting to count at zero.  </dd>
<dd>  For example on an x86-64 system: Node 0, zone DMA 1 1 1 0 2 1 1 0 1 1 3 Node 0, zone DMA32 65 47 4 81 52 28 13 10 5 1 404 Node 0, zone Normal 216 55 189 101 84 38 37 27 5 3 587  </dd>
<dd>  In this example, there is one node containing three zones and there are 11 different chunk sizes. If the page size is 4 kilobytes, then the first zone called <i>DMA</i> (on x86 the first 16 megabyte of memory) has 1 chunk of 4 kilobytes (order 0) available and has 3 chunks of 4 megabytes (order 10) available.  </dd>
<dd>  If the memory is heavily fragmented, the counters for higher order chunks will be zero and allocation of large contiguous areas will fail.  </dd>
<dd>  Further information about the zones can be found in <i>/proc/zoneinfo</i>.  </dd>
<dt><i>/proc/bus</i> </dt>
<dd>  Contains subdirectories for installed busses.  </dd>
<dt><i>/proc/bus/pccard</i> </dt>
<dd>  Subdirectory for PCMCIA devices when <code>CONFIG_PCMCIA</code> is set at kernel compilation time.  </dd>
<dt><i>/proc/bus/pccard/drivers</i> </dt>
<dd>   </dd>
<dt><i>/proc/bus/pci</i> </dt>
<dd>  Contains various bus subdirectories and pseudo-files containing information about PCI busses, installed devices, and device drivers. Some of these files are not ASCII.  </dd>
<dt><i>/proc/bus/pci/devices</i> </dt>
<dd>  Information about PCI devices. They may be accessed through <code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8) and <code><a href="/docs/linux/man/8-setpci/">setpci</a></code>(8).  </dd>
<dt><i>/proc/cgroups</i> (since Linux 2.6.24) </dt>
<dd>  See <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7).  </dd>
<dt><i>/proc/cmdline</i> </dt>
<dd>  Arguments passed to the Linux kernel at boot time. Often done via a boot manager such as <code><a href="/docs/linux/man/8-lilo/">lilo</a></code>(8) or <code><a href="/docs/linux/man/8-grub/">grub</a></code>(8).  </dd>
<dt><i>/proc/config.gz</i> (since Linux 2.6) </dt>
<dd>  This file exposes the configuration options that were used to build the currently running kernel, in the same format as they would be shown in the <i>.config</i> file that resulted when configuring the kernel (using <i>make xconfig</i>, <i>make config</i>, or similar). The file contents are compressed; view or search them using <code><a href="/docs/linux/man/1-zcat/">zcat</a></code>(1) and <code><a href="/docs/linux/man/1-zgrep/">zgrep</a></code>(1). As long as no changes have been made to the following file, the contents of <i>/proc/config.gz</i> are the same as those provided by:  </dd>
<dd>  cat /lib/modules/$(uname -r)/build/.config  </dd>
<dd>  <i>/proc/config.gz</i> is provided only if the kernel is configured with <code>CONFIG_IKCONFIG_PROC</code>.  </dd>
<dt><i>/proc/crypto</i> </dt>
<dd>  A list of the ciphers provided by the kernel crypto API. For details, see the kernel <i>Linux Kernel Crypto API</i> documentation available under the kernel source directory <i>Documentation/crypto/</i> (or <i>Documentation/DocBook</i> before 4.10; the documentation can be built using a command such as <i>make htmldocs</i> in the root directory of the kernel source tree).  </dd>
<dt><i>/proc/cpuinfo</i> </dt>
<dd>  This is a collection of CPU and system architecture dependent items, for each supported architecture a different list. Two common entries are <i>processor</i> which gives CPU number and <i>bogomips</i>; a system constant that is calculated during kernel initialization. SMP machines have information for each CPU. The <code><a href="/docs/linux/man/1-lscpu/">lscpu</a></code>(1) command gathers its information from this file.  </dd>
<dt><i>/proc/devices</i> </dt>
<dd>  Text listing of major numbers and device groups. This can be used by MAKEDEV scripts for consistency with the kernel.  </dd>
<dt><i>/proc/diskstats</i> (since Linux 2.5.69) </dt>
<dd>  This file contains disk I/O statistics for each disk device. See the Linux kernel source file <i>Documentation/iostats.txt</i> for further information.  </dd>
<dt><i>/proc/dma</i> </dt>
<dd>  This is a list of the registered <i>ISA</i> DMA (direct memory access) channels in use.  </dd>
<dt><i>/proc/driver</i> </dt>
<dd>  Empty subdirectory.  </dd>
<dt><i>/proc/execdomains</i> </dt>
<dd>  List of the execution domains (ABI personalities).  </dd>
<dt><i>/proc/fb</i> </dt>
<dd>  Frame buffer information when <code>CONFIG_FB</code> is defined during kernel compilation.  </dd>
<dt><i>/proc/filesystems</i> </dt>
<dd>  A text listing of the filesystems which are supported by the kernel, namely filesystems which were compiled into the kernel or whose kernel modules are currently loaded. (See also <code><a href="/docs/linux/man/5-filesystems/">filesystems</a></code>(5).) If a filesystem is marked with &quot;nodev&quot;, this means that it does not require a block device to be mounted (e.g., virtual filesystem, network filesystem).  </dd>
<dd>  Incidentally, this file may be used by <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) when no filesystem is specified and it didn&#8217;t manage to determine the filesystem type. Then filesystems contained in this file are tried (excepted those that are marked with &quot;nodev&quot;).  </dd>
<dt><i>/proc/fs</i> </dt>
<dd>  Contains subdirectories that in turn contain files with information about (certain) mounted filesystems.  </dd>
<dt><i>/proc/ide</i> </dt>
<dd>  This directory exists on systems with the IDE bus. There are directories for each IDE channel and attached device. Files include:  </dd>
<dd>  cache buffer size in KB capacity number of sectors driver driver version geometry physical and logical geometry identify in hexadecimal media media type model manufacturer&#8217;s model number settings drive settings smart_thresholds IDE disk management thresholds (in hex) smart_values IDE disk management values (in hex)  </dd>
<dd>  The <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8) utility provides access to this information in a friendly format.  </dd>
<dt><i>/proc/interrupts</i> </dt>
<dd>  This is used to record the number of interrupts per CPU per IO device. Since Linux 2.6.24, for the i386 and x86-64 architectures, at least, this also includes interrupts internal to the system (that is, not associated with a device as such), such as NMI (nonmaskable interrupt), LOC (local timer interrupt), and for SMP systems, TLB (TLB flush interrupt), RES (rescheduling interrupt), CAL (remote function call interrupt), and possibly others. Very easy to read formatting, done in ASCII.  </dd>
<dt><i>/proc/iomem</i> </dt>
<dd>  I/O memory map in Linux 2.4.  </dd>
<dt><i>/proc/ioports</i> </dt>
<dd>  This is a list of currently registered Input-Output port regions that are in use.  </dd>
<dt><i>/proc/kallsyms</i> (since Linux 2.5.71) </dt>
<dd>  This holds the kernel exported symbol definitions used by the <code>modules</code>(X) tools to dynamically link and bind loadable modules. In Linux 2.5.47 and earlier, a similar file with slightly different syntax was named <i>ksyms</i>.  </dd>
<dt><i>/proc/kcore</i> </dt>
<dd>  This file represents the physical memory of the system and is stored in the ELF core file format. With this pseudo-file, and an unstripped kernel (<i>/usr/src/linux/vmlinux</i>) binary, GDB can be used to examine the current state of any kernel data structures.  </dd>
<dd>  The total length of the file is the size of physical memory (RAM) plus 4 KiB.  </dd>
<dt><i>/proc/keys</i> (since Linux 2.6.10) </dt>
<dd>  See <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7).  </dd>
<dt><i>/proc/key-users</i> (since Linux 2.6.10) </dt>
<dd>  See <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7).  </dd>
<dt><i>/proc/kmsg</i> </dt>
<dd>  This file can be used instead of the <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) system call to read kernel messages. A process must have superuser privileges to read this file, and only one process should read this file. This file should not be read if a syslog process is running which uses the <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) system call facility to log kernel messages.  </dd>
<dd>  Information in this file is retrieved with the <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1) program.  </dd>
<dt><i>/proc/kpagecgroup</i> (since Linux 4.3) </dt>
<dd>  This file contains a 64-bit inode number of the memory cgroup each page is charged to, indexed by page frame number (see the discussion of <i>/proc/[pid]/pagemap</i>).  </dd>
<dd>  The <i>/proc/kpagecgroup</i> file is present only if the <code>CONFIG_MEMCG</code> kernel configuration option is enabled.  </dd>
<dt><i>/proc/kpagecount</i> (since Linux 2.6.25) </dt>
<dd>  This file contains a 64-bit count of the number of times each physical page frame is mapped, indexed by page frame number (see the discussion of <i>/proc/[pid]/pagemap</i>).  </dd>
<dd>  The <i>/proc/kpagecount</i> file is present only if the <code>CONFIG_PROC_PAGE_MONITOR</code> kernel configuration option is enabled.  </dd>
<dt><i>/proc/kpageflags</i> (since Linux 2.6.25) </dt>
<dd>  This file contains 64-bit masks corresponding to each physical page frame; it is indexed by page frame number (see the discussion of <i>/proc/[pid]/pagemap</i>). The bits are as follows:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 &#8211; KPF_LOCKED <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 &#8211; KPF_ERROR <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 &#8211; KPF_REFERENCED <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3 &#8211; KPF_UPTODATE <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 &#8211; KPF_DIRTY <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5 &#8211; KPF_LRU <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6 &#8211; KPF_ACTIVE <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7 &#8211; KPF_SLAB <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8 &#8211; KPF_WRITEBACK <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;9 &#8211; KPF_RECLAIM <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;10 &#8211; KPF_BUDDY <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;11 &#8211; KPF_MMAP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;12 &#8211; KPF_ANON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;13 &#8211; KPF_SWAPCACHE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;14 &#8211; KPF_SWAPBACKED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;15 &#8211; KPF_COMPOUND_HEAD&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;16 &#8211; KPF_COMPOUND_TAIL&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;17 &#8211; KPF_HUGE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;18 &#8211; KPF_UNEVICTABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;19 &#8211; KPF_HWPOISON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;20 &#8211; KPF_NOPAGE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.31) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;21 &#8211; KPF_KSM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.32) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;22 &#8211; KPF_THP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 3.4) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;23 &#8211; KPF_BALLOON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 3.18) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;24 &#8211; KPF_ZERO_PAGE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 4.0) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;25 &#8211; KPF_IDLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 4.3)  </dd>
<dd>  For further details on the meanings of these bits, see the kernel source file <i>Documentation/admin-guide/mm/pagemap.rst</i>. Before kernel 2.6.29, <code>KPF_WRITEBACK</code>, <code>KPF_RECLAIM</code>, <code>KPF_BUDDY</code>, and <code>KPF_LOCKED</code> did not report correctly.  </dd>
<dd>  The <i>/proc/kpageflags</i> file is present only if the <code>CONFIG_PROC_PAGE_MONITOR</code> kernel configuration option is enabled.  </dd>
<dt><i>/proc/ksyms</i> (Linux 1.1.23-2.5.47) </dt>
<dd>  See <i>/proc/kallsyms</i>.  </dd>
<dt><i>/proc/loadavg</i> </dt>
<dd>  The first three fields in this file are load average figures giving the number of jobs in the run queue (state R) or waiting for disk I/O (state D) averaged over 1, 5, and 15 minutes. They are the same as the load average numbers given by <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1) and other programs. The fourth field consists of two numbers separated by a slash (/). The first of these is the number of currently runnable kernel scheduling entities (processes, threads). The value after the slash is the number of kernel scheduling entities that currently exist on the system. The fifth field is the PID of the process that was most recently created on the system.  </dd>
<dt><i>/proc/locks</i> </dt>
<dd>  This file shows current file locks (<code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) and leases (<code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)).  </dd>
<dd>  An example of the content shown in this file is the following:  </dd>
<dd>  1: POSIX ADVISORY READ 5433 08:01:7864448 128 128 2: FLOCK ADVISORY WRITE 2001 08:01:7864554 0 EOF 3: FLOCK ADVISORY WRITE 1568 00:2f:32388 0 EOF 4: POSIX ADVISORY WRITE 699 00:16:28457 0 EOF 5: POSIX ADVISORY WRITE 764 00:16:21448 0 0 6: POSIX ADVISORY READ 3548 08:01:7867240 1 1 7: POSIX ADVISORY READ 3548 08:01:7865567 1826 2335 8: OFDLCK ADVISORY WRITE -1 08:01:8713209 128 191  </dd>
<dd>  The fields shown in each line are as follows:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>(1)</dt>
<dd>  The ordinal position of the lock in the list.  </dd>
<dt>(2)</dt>
<dd>  The lock type. Values that may appear here include:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><code>FLOCK</code> </dt>
<dd>  This is a BSD file lock created using <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2).  </dd>
<dt><code>OFDLCK</code> </dt>
<dd>  This is an open file description (OFD) lock created using <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).  </dd>
<dt><code>POSIX</code> </dt>
<dd>  This is a POSIX byte-range lock created using <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).  </dd></dl>
 </dl>
 <dt>(3)</dt>
<dd>  Among the strings that can appear here are the following:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><code>ADVISORY</code> </dt>
<dd>  This is an advisory lock.  </dd>
<dt><code>MANDATORY</code> </dt>
<dd>  This is a mandatory lock.  </dd></dl>
 </dl>
 <dt>(4)</dt>
<dd>  The type of lock. Values that can appear here are:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><code>READ</code> </dt>
<dd>  This is a POSIX or OFD read lock, or a BSD shared lock.  </dd>
<dt><code>WRITE</code> </dt>
<dd>  This is a POSIX or OFD write lock, or a BSD exclusive lock.  </dd></dl>
 </dl>
 <dt>(5)</dt>
<dd>  The PID of the process that owns the lock.  </dd>
<dd>  Because OFD locks are not owned by a single process (since multiple processes may have file descriptors that refer to the same open file description), the value -1 is displayed in this field for OFD locks. (Before kernel 4.14, a bug meant that the PID of the process that initially acquired the lock was displayed instead of the value -1.)  </dd>
<dt>(6)</dt>
<dd>  Three colon-separated subfields that identify the major and minor device ID of the device containing the filesystem where the locked file resides, followed by the inode number of the locked file.  </dd>
<dt>(7)</dt>
<dd>  The byte offset of the first byte of the lock. For BSD locks, this value is always 0.  </dd>
<dt>(8)</dt>
<dd>  The byte offset of the last byte of the lock. <code>EOF</code> in this field means that the lock extends to the end of the file. For BSD locks, the value shown is always <i>EOF</i>.  </dd></dl>
 </dl>
 <dd>  Since Linux 4.9, the list of locks shown in <i>/proc/locks</i> is filtered to show just the locks for the processes in the PID namespace (see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7)) for which the <i>/proc</i> filesystem was mounted. (In the initial PID namespace, there is no filtering of the records shown in this file.)  </dd>
<dd>  The <code><a href="/docs/linux/man/8-lslocks/">lslocks</a></code>(8) command provides a bit more information about each lock.  </dd>
<dt><i>/proc/malloc</i> (only up to and including Linux 2.2) </dt>
<dd>  This file is present only if <code>CONFIG_DEBUG_MALLOC</code> was defined during compilation.  </dd>
<dt><i>/proc/meminfo</i> </dt>
<dd>  This file reports statistics about memory usage on the system. It is used by <code><a href="/docs/linux/man/1-free/">free</a></code>(1) to report the amount of free and used memory (both physical and swap) on the system as well as the shared memory and buffers used by the kernel. Each line of the file consists of a parameter name, followed by a colon, the value of the parameter, and an option unit of measurement (e.g., &quot;kB&quot;). The list below describes the parameter names and the format specifier required to read the field value. Except as noted below, all of the fields have been present since at least Linux 2.6.0. Some fields are displayed only if the kernel was configured with various options; those dependencies are noted in the list.  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>MemTotal</i> %lu </dt>
<dd>  Total usable RAM (i.e., physical RAM minus a few reserved bits and the kernel binary code).  </dd>
<dt><i>MemFree</i> %lu </dt>
<dd>  The sum of <i>LowFree</i>+<i>HighFree</i>.  </dd>
<dt><i>MemAvailable</i> %lu (since Linux 3.14) </dt>
<dd>  An estimate of how much memory is available for starting new applications, without swapping.  </dd>
<dt><i>Buffers</i> %lu </dt>
<dd>  Relatively temporary storage for raw disk blocks that shouldn&#8217;t get tremendously large (20 MB or so).  </dd>
<dt><i>Cached</i> %lu </dt>
<dd>  In-memory cache for files read from the disk (the page cache). Doesn&#8217;t include <i>SwapCached</i>.  </dd>
<dt><i>SwapCached</i> %lu </dt>
<dd>  Memory that once was swapped out, is swapped back in but still also is in the swap file. (If memory pressure is high, these pages don&#8217;t need to be swapped out again because they are already in the swap file. This saves I/O.)  </dd>
<dt><i>Active</i> %lu </dt>
<dd>  Memory that has been used more recently and usually not reclaimed unless absolutely necessary.  </dd>
<dt><i>Inactive</i> %lu </dt>
<dd>  Memory which has been less recently used. It is more eligible to be reclaimed for other purposes.  </dd>
<dt><i>Active(anon)</i> %lu (since Linux 2.6.28) </dt>
<dd>  [To be documented.]  </dd>
<dt><i>Inactive(anon)</i> %lu (since Linux 2.6.28) </dt>
<dd>  [To be documented.]  </dd>
<dt><i>Active(file)</i> %lu (since Linux 2.6.28) </dt>
<dd>  [To be documented.]  </dd>
<dt><i>Inactive(file)</i> %lu (since Linux 2.6.28) </dt>
<dd>  [To be documented.]  </dd>
<dt><i>Unevictable</i> %lu (since Linux 2.6.28) </dt>
<dd>  (From Linux 2.6.28 to 2.6.30, <code>CONFIG_UNEVICTABLE_LRU</code> was required.) [To be documented.]  </dd>
<dt><i>Mlocked</i> %lu (since Linux 2.6.28) </dt>
<dd>  (From Linux 2.6.28 to 2.6.30, <code>CONFIG_UNEVICTABLE_LRU</code> was required.) [To be documented.]  </dd>
<dt><i>HighTotal</i> %lu </dt>
<dd>  (Starting with Linux 2.6.19, <code>CONFIG_HIGHMEM</code> is required.) Total amount of highmem. Highmem is all memory above ~860 MB of physical memory. Highmem areas are for use by user-space programs, or for the page cache. The kernel must use tricks to access this memory, making it slower to access than lowmem.  </dd>
<dt><i>HighFree</i> %lu </dt>
<dd>  (Starting with Linux 2.6.19, <code>CONFIG_HIGHMEM</code> is required.) Amount of free highmem.  </dd>
<dt><i>LowTotal</i> %lu </dt>
<dd>  (Starting with Linux 2.6.19, <code>CONFIG_HIGHMEM</code> is required.) Total amount of lowmem. Lowmem is memory which can be used for everything that highmem can be used for, but it is also available for the kernel&#8217;s use for its own data structures. Among many other things, it is where everything from <i>Slab</i> is allocated. Bad things happen when you&#8217;re out of lowmem.  </dd>
<dt><i>LowFree</i> %lu </dt>
<dd>  (Starting with Linux 2.6.19, <code>CONFIG_HIGHMEM</code> is required.) Amount of free lowmem.  </dd>
<dt><i>MmapCopy</i> %lu (since Linux 2.6.29) </dt>
<dd>  (<code>CONFIG_MMU</code> is required.) [To be documented.]  </dd>
<dt><i>SwapTotal</i> %lu </dt>
<dd>  Total amount of swap space available.  </dd>
<dt><i>SwapFree</i> %lu </dt>
<dd>  Amount of swap space that is currently unused.  </dd>
<dt><i>Dirty</i> %lu </dt>
<dd>  Memory which is waiting to get written back to the disk.  </dd>
<dt><i>Writeback</i> %lu </dt>
<dd>  Memory which is actively being written back to the disk.  </dd>
<dt><i>AnonPages</i> %lu (since Linux 2.6.18) </dt>
<dd>  Non-file backed pages mapped into user-space page tables.  </dd>
<dt><i>Mapped</i> %lu </dt>
<dd>  Files which have been mapped into memory (with <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)), such as libraries.  </dd>
<dt><i>Shmem</i> %lu (since Linux 2.6.32) </dt>
<dd>  Amount of memory consumed in <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) filesystems.  </dd>
<dt><i>KReclaimable</i> %lu (since Linux 4.20) </dt>
<dd>  Kernel allocations that the kernel will attempt to reclaim under memory pressure. Includes <i>SReclaimable</i> (below), and other direct allocations with a shrinker.  </dd>
<dt><i>Slab</i> %lu </dt>
<dd>  In-kernel data structures cache. (See <code><a href="/docs/linux/man/5-slabinfo/">slabinfo</a></code>(5).)  </dd>
<dt><i>SReclaimable</i> %lu (since Linux 2.6.19) </dt>
<dd>  Part of <i>Slab</i>, that might be reclaimed, such as caches.  </dd>
<dt><i>SUnreclaim</i> %lu (since Linux 2.6.19) </dt>
<dd>  Part of <i>Slab</i>, that cannot be reclaimed on memory pressure.  </dd>
<dt><i>KernelStack</i> %lu (since Linux 2.6.32) </dt>
<dd>  Amount of memory allocated to kernel stacks.  </dd>
<dt><i>PageTables</i> %lu (since Linux 2.6.18) </dt>
<dd>  Amount of memory dedicated to the lowest level of page tables.  </dd>
<dt><i>Quicklists</i> %lu (since Linux 2.6.27) </dt>
<dd>  (<code>CONFIG_QUICKLIST</code> is required.) [To be documented.]  </dd>
<dt><i>NFS_Unstable</i> %lu (since Linux 2.6.18) </dt>
<dd>  NFS pages sent to the server, but not yet committed to stable storage.  </dd>
<dt><i>Bounce</i> %lu (since Linux 2.6.18) </dt>
<dd>  Memory used for block device &quot;bounce buffers&quot;.  </dd>
<dt><i>WritebackTmp</i> %lu (since Linux 2.6.26) </dt>
<dd>  Memory used by FUSE for temporary writeback buffers.  </dd>
<dt><i>CommitLimit</i> %lu (since Linux 2.6.10) </dt>
<dd>  This is the total amount of memory currently available to be allocated on the system, expressed in kilobytes. This limit is adhered to only if strict overcommit accounting is enabled (mode 2 in <i>/proc/sys/vm/overcommit_memory</i>). The limit is calculated according to the formula described under <i>/proc/sys/vm/overcommit_memory</i>. For further details, see the kernel source file <i>Documentation/vm/overcommit-accounting.rst</i>.  </dd>
<dt><i>Committed_AS</i> %lu </dt>
<dd>  The amount of memory presently allocated on the system. The committed memory is a sum of all of the memory which has been allocated by processes, even if it has not been &quot;used&quot; by them as of yet. A process which allocates 1 GB of memory (using <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) or similar), but touches only 300 MB of that memory will show up as using only 300 MB of memory even if it has the address space allocated for the entire 1 GB.  </dd>
<dd>  This 1 GB is memory which has been &quot;committed&quot; to by the VM and can be used at any time by the allocating application. With strict overcommit enabled on the system (mode 2 in <i>/proc/sys/vm/overcommit_memory</i>), allocations which would exceed the <i>CommitLimit</i> will not be permitted. This is useful if one needs to guarantee that processes will not fail due to lack of memory once that memory has been successfully allocated.  </dd>
<dt><i>VmallocTotal</i> %lu </dt>
<dd>  Total size of vmalloc memory area.  </dd>
<dt><i>VmallocUsed</i> %lu </dt>
<dd>  Amount of vmalloc area which is used. Since Linux 4.4, this field is no longer calculated, and is hard coded as 0. See <i>/proc/vmallocinfo</i>.  </dd>
<dt><i>VmallocChunk</i> %lu </dt>
<dd>  Largest contiguous block of vmalloc area which is free. Since Linux 4.4, this field is no longer calculated and is hard coded as 0. See <i>/proc/vmallocinfo</i>.  </dd>
<dt><i>HardwareCorrupted</i> %lu (since Linux 2.6.32) </dt>
<dd>  (<code>CONFIG_MEMORY_FAILURE</code> is required.) [To be documented.]  </dd>
<dt><i>LazyFree</i> %lu (since Linux 4.12) </dt>
<dd>  Shows the amount of memory marked by <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) <code>MADV_FREE</code>.  </dd>
<dt><i>AnonHugePages</i> %lu (since Linux 2.6.38) </dt>
<dd>  (<code>CONFIG_TRANSPARENT_HUGEPAGE</code> is required.) Non-file backed huge pages mapped into user-space page tables.  </dd>
<dt><i>ShmemHugePages</i> %lu (since Linux 4.8) </dt>
<dd>  (<code>CONFIG_TRANSPARENT_HUGEPAGE</code> is required.) Memory used by shared memory (shmem) and <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) allocated with huge pages.  </dd>
<dt><i>ShmemPmdMapped</i> %lu (since Linux 4.8) </dt>
<dd>  (<code>CONFIG_TRANSPARENT_HUGEPAGE</code> is required.) Shared memory mapped into user space with huge pages.  </dd>
<dt><i>CmaTotal</i> %lu (since Linux 3.1) </dt>
<dd>  Total CMA (Contiguous Memory Allocator) pages. (<code>CONFIG_CMA</code> is required.)  </dd>
<dt><i>CmaFree</i> %lu (since Linux 3.1) </dt>
<dd>  Free CMA (Contiguous Memory Allocator) pages. (<code>CONFIG_CMA</code> is required.)  </dd>
<dt><i>HugePages_Total</i> %lu </dt>
<dd>  (<code>CONFIG_HUGETLB_PAGE</code> is required.) The size of the pool of huge pages.  </dd>
<dt><i>HugePages_Free</i> %lu </dt>
<dd>  (<code>CONFIG_HUGETLB_PAGE</code> is required.) The number of huge pages in the pool that are not yet allocated.  </dd>
<dt><i>HugePages_Rsvd</i> %lu (since Linux 2.6.17) </dt>
<dd>  (<code>CONFIG_HUGETLB_PAGE</code> is required.) This is the number of huge pages for which a commitment to allocate from the pool has been made, but no allocation has yet been made. These reserved huge pages guarantee that an application will be able to allocate a huge page from the pool of huge pages at fault time.  </dd>
<dt><i>HugePages_Surp</i> %lu (since Linux 2.6.24) </dt>
<dd>  (<code>CONFIG_HUGETLB_PAGE</code> is required.) This is the number of huge pages in the pool above the value in <i>/proc/sys/vm/nr_hugepages</i>. The maximum number of surplus huge pages is controlled by <i>/proc/sys/vm/nr_overcommit_hugepages</i>.  </dd>
<dt><i>Hugepagesize</i> %lu </dt>
<dd>  (<code>CONFIG_HUGETLB_PAGE</code> is required.) The size of huge pages.  </dd>
<dt><i>DirectMap4k</i> %lu (since Linux 2.6.27) </dt>
<dd>  Number of bytes of RAM linearly mapped by kernel in 4 kB pages. (x86.)  </dd>
<dt><i>DirectMap4M</i> %lu (since Linux 2.6.27) </dt>
<dd>  Number of bytes of RAM linearly mapped by kernel in 4 MB pages. (x86 with <code>CONFIG_X86_64</code> or <code>CONFIG_X86_PAE</code> enabled.)  </dd>
<dt><i>DirectMap2M</i> %lu (since Linux 2.6.27) </dt>
<dd>  Number of bytes of RAM linearly mapped by kernel in 2 MB pages. (x86 with neither <code>CONFIG_X86_64</code> nor <code>CONFIG_X86_PAE</code> enabled.)  </dd>
<dt><i>DirectMap1G</i> %lu (since Linux 2.6.27) </dt>
<dd>  (x86 with <code>CONFIG_X86_64</code> and <code>CONFIG_X86_DIRECT_GBPAGES</code> enabled.)  </dd></dl>
 </dl>
 <dt><i>/proc/modules</i> </dt>
<dd>  A text list of the modules that have been loaded by the system. See also <code><a href="/docs/linux/man/8-lsmod/">lsmod</a></code>(8).  </dd>
<dt><i>/proc/mounts</i> </dt>
<dd>  Before kernel 2.4.19, this file was a list of all the filesystems currently mounted on the system. With the introduction of per-process mount namespaces in Linux 2.4.19 (see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7)), this file became a link to <i>/proc/self/mounts</i>, which lists the mount points of the process&#8217;s own mount namespace. The format of this file is documented in <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5).  </dd>
<dt><i>/proc/mtrr</i> </dt>
<dd>  Memory Type Range Registers. See the Linux kernel source file <i>Documentation/x86/mtrr.txt</i> (or <i>Documentation/mtrr.txt</i> before Linux 2.6.28) for details.  </dd>
<dt><i>/proc/net</i> </dt>
<dd>  This directory contains various files and subdirectories containing information about the networking layer. The files contain ASCII structures and are, therefore, readable with <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1). However, the standard <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8) suite provides much cleaner access to these files.  </dd>
<dd>  With the advent of network namespaces, various information relating to the network stack is virtualized (see <code><a href="/docs/linux/man/7-network_namespaces/">network_namespaces</a></code>(7)). Thus, since Linux 2.6.25, <i>/proc/net</i> is a symbolic link to the directory <i>/proc/self/net</i>, which contains the same files and directories as listed below. However, these files and directories now expose information for the network namespace of which the process is a member.  </dd>
<dt><i>/proc/net/arp</i> </dt>
<dd>  This holds an ASCII readable dump of the kernel ARP table used for address resolutions. It will show both dynamically learned and preprogrammed ARP entries. The format is:  </dd>
<dd>  IP address HW type Flags HW address Mask Device 192.168.0.50 0x1 0x2 00:50:BF:25:68:F3 * eth0 192.168.0.250 0x1 0xc 00:00:00:00:00:00 * eth0  </dd>
<dd>  Here &quot;IP address&quot; is the IPv4 address of the machine and the &quot;HW type&quot; is the hardware type of the address from RFC 826. The flags are the internal flags of the ARP structure (as defined in <i>/usr/include/linux/if_arp.h</i>) and the &quot;HW address&quot; is the data link layer mapping for that IP address if it is known.  </dd>
<dt><i>/proc/net/dev</i> </dt>
<dd>  The dev pseudo-file contains network device status information. This gives the number of received and sent packets, the number of errors and collisions and other basic statistics. These are used by the <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) program to report device status. The format is:  </dd>
<dd>  Inter-| Receive | Transmit <br />
&nbsp;face |bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;packets errs drop fifo frame compressed multicast|bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;packets errs drop fifo colls carrier compressed <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo: 2776770&nbsp;<wbr>&nbsp;<wbr>&nbsp;11307&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;2776770&nbsp;<wbr>&nbsp;<wbr>&nbsp;11307&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 <br />
&nbsp;<wbr>&nbsp;eth0: 1215645&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2751&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;1782404&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4324&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;427&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 <br />
&nbsp;<wbr>&nbsp;ppp0: 1622270&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5552&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;354130&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5669&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 <br />
&nbsp;<wbr>&nbsp;tap0:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7714&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;81&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7714&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;81&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0  </dd>
<dt><i>/proc/net/dev_mcast</i> </dt>
<dd>  Defined in <i>/usr/src/linux/net/core/dev_mcast.c</i>:  </dd>
<dd>  indx interface_name dmi_u dmi_g dmi_address 2 eth0 1 0 01005e000001 3 eth1 1 0 01005e000001 4 eth2 1 0 01005e000001  </dd>
<dt><i>/proc/net/igmp</i> </dt>
<dd>  Internet Group Management Protocol. Defined in <i>/usr/src/linux/net/core/igmp.c</i>.  </dd>
<dt><i>/proc/net/rarp</i> </dt>
<dd>  This file uses the same format as the <i>arp</i> file and contains the current reverse mapping database used to provide <code><a href="/docs/linux/man/8-rarp/">rarp</a></code>(8) reverse address lookup services. If RARP is not configured into the kernel, this file will not be present.  </dd>
<dt><i>/proc/net/raw</i> </dt>
<dd>  Holds a dump of the RAW socket table. Much of the information is not of use apart from debugging. The &quot;sl&quot; value is the kernel hash slot for the socket, the &quot;local_address&quot; is the local address and protocol number pair. &quot;St&quot; is the internal status of the socket. The &quot;tx_queue&quot; and &quot;rx_queue&quot; are the outgoing and incoming data queue in terms of kernel memory usage. The &quot;tr&quot;, &quot;tm-&gt;when&quot;, and &quot;rexmits&quot; fields are not used by RAW. The &quot;uid&quot; field holds the effective UID of the creator of the socket.  </dd>
<dt><i>/proc/net/snmp</i> </dt>
<dd>  This file holds the ASCII data needed for the IP, ICMP, TCP, and UDP management information bases for an SNMP agent.  </dd>
<dt><i>/proc/net/tcp</i> </dt>
<dd>  Holds a dump of the TCP socket table. Much of the information is not of use apart from debugging. The &quot;sl&quot; value is the kernel hash slot for the socket, the &quot;local_address&quot; is the local address and port number pair. The &quot;rem_address&quot; is the remote address and port number pair (if connected). &quot;St&quot; is the internal status of the socket. The &quot;tx_queue&quot; and &quot;rx_queue&quot; are the outgoing and incoming data queue in terms of kernel memory usage. The &quot;tr&quot;, &quot;tm-&gt;when&quot;, and &quot;rexmits&quot; fields hold internal information of the kernel socket state and are useful only for debugging. The &quot;uid&quot; field holds the effective UID of the creator of the socket.  </dd>
<dt><i>/proc/net/udp</i> </dt>
<dd>  Holds a dump of the UDP socket table. Much of the information is not of use apart from debugging. The &quot;sl&quot; value is the kernel hash slot for the socket, the &quot;local_address&quot; is the local address and port number pair. The &quot;rem_address&quot; is the remote address and port number pair (if connected). &quot;St&quot; is the internal status of the socket. The &quot;tx_queue&quot; and &quot;rx_queue&quot; are the outgoing and incoming data queue in terms of kernel memory usage. The &quot;tr&quot;, &quot;tm-&gt;when&quot;, and &quot;rexmits&quot; fields are not used by UDP. The &quot;uid&quot; field holds the effective UID of the creator of the socket. The format is:  </dd>
<dd>  sl local_address rem_address st tx_queue rx_queue tr rexmits tm-&gt;when uid <br />
&nbsp;1: 01642C89:0201 0C642C89:03FF 01 00000000:00000001 01:000071BA 00000000 0 <br />
&nbsp;1: 00000000:0801 00000000:0000 0A 00000000:00000000 00:00000000 6F000100 0 <br />
&nbsp;1: 00000000:0201 00000000:0000 0A 00000000:00000000 00:00000000 00000000 0  </dd>
<dt><i>/proc/net/unix</i> </dt>
<dd>  Lists the UNIX domain sockets present within the system and their status. The format is:  </dd>
<dd>  Num RefCount Protocol Flags Type St Inode Path <br />
&nbsp;0: 00000002 00000000 00000000 0001 03&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;42 <br />
&nbsp;1: 00000001 00000000 00010000 0001 01&nbsp;<wbr>&nbsp;1948&nbsp;/dev/printer  </dd>
<dd>  The fields are as follows:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>Num</i>: </dt>
<dd>  the kernel table slot number.  </dd>
<dt><i>RefCount</i>: </dt>
<dd>  the number of users of the socket.  </dd>
<dt><i>Protocol</i>: </dt>
<dd>  currently always 0.  </dd>
<dt><i>Flags</i>: </dt>
<dd>  the internal kernel flags holding the status of the socket.  </dd>
<dt><i>Type</i>: </dt>
<dd>  the socket type. For <code>SOCK_STREAM</code> sockets, this is 0001; for <code>SOCK_DGRAM</code> sockets, it is 0002; and for <code>SOCK_SEQPACKET</code> sockets, it is 0005.  </dd>
<dt><i>St</i>: </dt>
<dd>  the internal state of the socket.  </dd>
<dt><i>Inode</i>: </dt>
<dd>  the inode number of the socket.  </dd>
<dt><i>Path</i>: </dt>
<dd>  the bound pathname (if any) of the socket. Sockets in the abstract namespace are included in the list, and are shown with a <i>Path</i> that commences with the character &#8216;@&#8216;.  </dd></dl>
 </dl>
 <dt><i>/proc/net/netfilter/nfnetlink_queue</i> </dt>
<dd>  This file contains information about netfilter user-space queueing, if used. Each line represents a queue. Queues that have not been subscribed to by user space are not shown.  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;4207&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;2 65535&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;1 <br />
&nbsp;<wbr>&nbsp;(1)&nbsp;<wbr>&nbsp;<wbr>&nbsp;(2)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(3)(4)&nbsp;<wbr>&nbsp;(5)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(6)&nbsp;<wbr>&nbsp;<wbr>&nbsp;(7)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(8)  </dd>
<dd>  The fields in each line are:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>(1)</dt>
<dd>  The ID of the queue. This matches what is specified in the <code>--queue-num</code> or <code>--queue-balance</code> options to the <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) NFQUEUE target. See <code><a href="/docs/linux/man/8-iptables-extensions/">iptables-extensions</a></code>(8) for more information.  </dd>
<dt>(2)</dt>
<dd>  The netlink port ID subscribed to the queue.  </dd>
<dt>(3)</dt>
<dd>  The number of packets currently queued and waiting to be processed by the application.  </dd>
<dt>(4)</dt>
<dd>  The copy mode of the queue. It is either 1 (metadata only) or 2 (also copy payload data to user space).  </dd>
<dt>(5)</dt>
<dd>  Copy range; that is, how many bytes of packet payload should be copied to user space at most.  </dd>
<dt>(6)</dt>
<dd>  queue dropped. Number of packets that had to be dropped by the kernel because too many packets are already waiting for user space to send back the mandatory accept/drop verdicts.  </dd>
<dt>(7)</dt>
<dd>  queue user dropped. Number of packets that were dropped within the netlink subsystem. Such drops usually happen when the corresponding socket buffer is full; that is, user space is not able to read messages fast enough.  </dd>
<dt>(8)</dt>
<dd>  sequence number. Every queued packet is associated with a (32-bit) monotonically increasing sequence number. This shows the ID of the most recent packet queued.  </dd></dl>
 </dl>
 <dd>  The last number exists only for compatibility reasons and is always 1.  </dd>
<dt><i>/proc/partitions</i> </dt>
<dd>  Contains the major and minor numbers of each partition as well as the number of 1024-byte blocks and the partition name.  </dd>
<dt><i>/proc/pci</i> </dt>
<dd>  This is a listing of all PCI devices found during kernel initialization and their configuration.  </dd>
<dd>  This file has been deprecated in favor of a new <i>/proc</i> interface for PCI (<i>/proc/bus/pci</i>). It became optional in Linux 2.2 (available with <code>CONFIG_PCI_OLD_PROC</code> set at kernel compilation). It became once more nonoptionally enabled in Linux 2.4. Next, it was deprecated in Linux 2.6 (still available with <code>CONFIG_PCI_LEGACY_PROC</code> set), and finally removed altogether since Linux 2.6.17.  </dd>
<dt><i>/proc/profile</i> (since Linux 2.4) </dt>
<dd>  This file is present only if the kernel was booted with the <i>profile=1</i> command-line option. It exposes kernel profiling information in a binary format for use by <code><a href="/docs/linux/man/1-readprofile/">readprofile</a></code>(1). Writing (e.g., an empty string) to this file resets the profiling counters; on some architectures, writing a binary integer &quot;profiling multiplier&quot; of size <i>sizeof(int)</i> sets the profiling interrupt frequency.  </dd>
<dt><i>/proc/scsi</i> </dt>
<dd>  A directory with the <i>scsi</i> mid-level pseudo-file and various SCSI low-level driver directories, which contain a file for each SCSI host in this system, all of which give the status of some part of the SCSI IO subsystem. These files contain ASCII structures and are, therefore, readable with <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1).  </dd>
<dd>  You can also write to some of the files to reconfigure the subsystem or switch certain features on or off.  </dd>
<dt><i>/proc/scsi/scsi</i> </dt>
<dd>  This is a listing of all SCSI devices known to the kernel. The listing is similar to the one seen during bootup. scsi currently supports only the <i>add-single-device</i> command which allows root to add a hotplugged device to the list of known devices.  </dd>
<dd>  The command  </dd>
<dd>  echo &#8216;scsi add-single-device 1 0 5 0&#8217; &gt; /proc/scsi/scsi  </dd>
<dd>  will cause host scsi1 to scan on SCSI channel 0 for a device on ID 5 LUN 0. If there is already a device known on this address or the address is invalid, an error will be returned.  </dd>
<dt><i>/proc/scsi/[drivername]</i> </dt>
<dd>  <i>[drivername]</i> can currently be NCR53c7xx, aha152x, aha1542, aha1740, aic7xxx, buslogic, eata_dma, eata_pio, fdomain, in2000, pas16, qlogic, scsi_debug, seagate, t128, u15-24f, ultrastore, or wd7000. These directories show up for all drivers that registered at least one SCSI HBA. Every directory contains one file per registered host. Every host-file is named after the number the host was assigned during initialization.  </dd>
<dd>  Reading these files will usually show driver and host configuration, statistics, and so on.  </dd>
<dd>  Writing to these files allows different things on different hosts. For example, with the <i>latency</i> and <i>nolatency</i> commands, root can switch on and off command latency measurement code in the eata_dma driver. With the <i>lockup</i> and <i>unlock</i> commands, root can control bus lockups simulated by the scsi_debug driver.  </dd>
<dt><i>/proc/self</i> </dt>
<dd>  This directory refers to the process accessing the <i>/proc</i> filesystem, and is identical to the <i>/proc</i> directory named by the process ID of the same process.  </dd>
<dt><i>/proc/slabinfo</i> </dt>
<dd>  Information about kernel caches. See <code><a href="/docs/linux/man/5-slabinfo/">slabinfo</a></code>(5) for details.  </dd>
<dt><i>/proc/stat</i> </dt>
<dd>  kernel/system statistics. Varies with architecture. Common entries include:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>cpu 10132153 290696 3084719 46828483 16683 0 25195 0 175628 0</i> </dt>
<dd>  <i>cpu0 1393280 32966 572056 13343292 6130 0 17875 0 23933 0</i> The amount of time, measured in units of USER_HZ (1/100ths of a second on most architectures, use <i>sysconf(_SC_CLK_TCK)</i> to obtain the right value), that the system (&quot;cpu&quot; line) or the specific CPU (&quot;cpu <i>N</i>&quot; line) spent in various states:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>user</i> </dt>
<dd>  (1) Time spent in user mode.  </dd>
<dt><i>nice</i> </dt>
<dd>  (2) Time spent in user mode with low priority (nice).  </dd>
<dt><i>system</i> </dt>
<dd>  (3) Time spent in system mode.  </dd>
<dt><i>idle</i> </dt>
<dd>  (4) Time spent in the idle task. This value should be USER_HZ times the second entry in the <i>/proc/uptime</i> pseudo-file.  </dd>
<dt><i>iowait</i> (since Linux 2.5.41) </dt>
<dd>  (5) Time waiting for I/O to complete. This value is not reliable, for the following reasons:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>1.</dt>
<dd>  The CPU will not wait for I/O to complete; iowait is the time that a task is waiting for I/O to complete. When a CPU goes into idle state for outstanding task I/O, another task will be scheduled on this CPU.  </dd>
<dt>2.</dt>
<dd>  On a multi-core CPU, the task waiting for I/O to complete is not running on any CPU, so the iowait of each CPU is difficult to calculate.  </dd>
<dt>3.</dt>
<dd>  The value in this field may <i>decrease</i> in certain conditions.  </dd></dl>
 </dl>
 <dt><i>irq</i> (since Linux 2.6.0) </dt>
<dd>  (6) Time servicing interrupts.  </dd>
<dt><i>softirq</i> (since Linux 2.6.0) </dt>
<dd>  (7) Time servicing softirqs.  </dd>
<dt><i>steal</i> (since Linux 2.6.11) </dt>
<dd>  (8) Stolen time, which is the time spent in other operating systems when running in a virtualized environment  </dd>
<dt><i>guest</i> (since Linux 2.6.24) </dt>
<dd>  (9) Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel.  </dd>
<dt><i>guest_nice</i> (since Linux 2.6.33) </dt>
<dd>  (10) Time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel).  </dd></dl>
 </dl>
 <dt><i>page 5741 1808</i></dt>
<dd>  The number of pages the system paged in and the number that were paged out (from disk).  </dd>
<dt><i>swap 1 0</i></dt>
<dd>  The number of swap pages that have been brought in and out.  </dd>
<dd>  <i>intr 1462898</i> This line shows counts of interrupts serviced since boot time, for each of the possible system interrupts. The first column is the total of all interrupts serviced including unnumbered architecture specific interrupts; each subsequent column is the total for that particular numbered interrupt. Unnumbered interrupts are not shown, only summed into the total.  </dd>
<dt><i>disk_io: (2,0):(31,30,5764,1,2) (3,0):</i>...</dt>
<dd>  (major,disk_idx):(noinfo, read_io_ops, blks_read, write_io_ops, blks_written) <br />
 (Linux 2.4 only)  </dd>
<dt><i>ctxt 115315</i></dt>
<dd>  The number of context switches that the system underwent.  </dd>
<dt><i>btime 769041601</i></dt>
<dd>  boot time, in seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC).  </dd>
<dt><i>processes 86031</i></dt>
<dd>  Number of forks since boot.  </dd>
<dt><i>procs_running 6</i></dt>
<dd>  Number of processes in runnable state. (Linux 2.5.45 onward.)  </dd>
<dt><i>procs_blocked 2</i></dt>
<dd>  Number of processes blocked waiting for I/O to complete. (Linux 2.5.45 onward.)  </dd>
<dt><i>softirq 229245889 94 60001584 13619 5175704 2471304 28 51212741 59130143 0 51240672</i> </dt>
<dd>  This line shows the number of softirq for all CPUs. The first column is the total of all softirqs and each subsequent column is the total for particular softirq. (Linux 2.6.31 onward.)  </dd></dl>
 </dl>
 <dt><i>/proc/swaps</i> </dt>
<dd>  Swap areas in use. See also <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8).  </dd>
<dt><i>/proc/sys</i> </dt>
<dd>  This directory (present since 1.3.57) contains a number of files and subdirectories corresponding to kernel variables. These variables can be read and in some cases modified using the <i>/proc</i> filesystem, and the (deprecated) <code><a href="/docs/linux/man/2-sysctl/">sysctl</a></code>(2) system call.  </dd>
<dd>  String values may be terminated by either &#8216;\0&#8217; or &#8216;\n&#8217;.  </dd>
<dd>  Integer and long values may be written either in decimal or in hexadecimal notation (e.g., 0x3FFF). When writing multiple integer or long values, these may be separated by any of the following whitespace characters: &#8216;&nbsp;&#8216;, &#8216;\t&#8217;, or &#8216;\n&#8217;. Using other separators leads to the error <code>EINVAL</code>.  </dd>
<dt><i>/proc/sys/abi</i> (since Linux 2.4.10) </dt>
<dd>  This directory may contain files with application binary information. See the Linux kernel source file <i>Documentation/sysctl/abi.txt</i> for more information.  </dd>
<dt><i>/proc/sys/debug</i> </dt>
<dd>  This directory may be empty.  </dd>
<dt><i>/proc/sys/dev</i> </dt>
<dd>  This directory contains device-specific information (e.g., <i>dev/cdrom/info</i>). On some systems, it may be empty.  </dd>
<dt><i>/proc/sys/fs</i> </dt>
<dd>  This directory contains the files and subdirectories for kernel variables related to filesystems.  </dd>
<dt><i>/proc/sys/fs/aio-max-nr</i> and <i>/proc/sys/fs/aio-nr</i> (since Linux 2.6.4) </dt>
<dd>  <i>aio-nr</i> is the running total of the number of events specified by <code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2) calls for all currently active AIO contexts. If <i>aio-nr</i> reaches <i>aio-max-nr</i>, then <code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2) will fail with the error <code>EAGAIN</code>. Raising <i>aio-max-nr</i> does not result in the preallocation or resizing of any kernel data structures.  </dd>
<dt><i>/proc/sys/fs/binfmt_misc</i> </dt>
<dd>  Documentation for files in this directory can be found in the Linux kernel source in the file <i>Documentation/admin-guide/binfmt-misc.rst</i> (or in <i>Documentation/binfmt_misc.txt</i> on older kernels).  </dd>
<dt><i>/proc/sys/fs/dentry-state</i> (since Linux 2.2) </dt>
<dd>  This file contains information about the status of the directory cache (dcache). The file contains six numbers, <i>nr_dentry</i>, <i>nr_unused</i>, <i>age_limit</i> (age in seconds), <i>want_pages</i> (pages requested by system) and two dummy values.  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>*</dt>
<dd>  <i>nr_dentry</i> is the number of allocated dentries (dcache entries). This field is unused in Linux 2.2.  </dd>
<dt>*</dt>
<dd>  <i>nr_unused</i> is the number of unused dentries.  </dd>
<dt>*</dt>
<dd>  <i>age_limit</i> is the age in seconds after which dcache entries can be reclaimed when memory is short.  </dd>
<dt>*</dt>
<dd>  <i>want_pages</i> is nonzero when the kernel has called shrink_dcache_pages() and the dcache isn&#8217;t pruned yet.  </dd></dl>
 </dl>
 <dt><i>/proc/sys/fs/dir-notify-enable</i> </dt>
<dd>  This file can be used to disable or enable the <i>dnotify</i> interface described in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) on a system-wide basis. A value of 0 in this file disables the interface, and a value of 1 enables it.  </dd>
<dt><i>/proc/sys/fs/dquot-max</i> </dt>
<dd>  This file shows the maximum number of cached disk quota entries. On some (2.4) systems, it is not present. If the number of free cached disk quota entries is very low and you have some awesome number of simultaneous system users, you might want to raise the limit.  </dd>
<dt><i>/proc/sys/fs/dquot-nr</i> </dt>
<dd>  This file shows the number of allocated disk quota entries and the number of free disk quota entries.  </dd>
<dt><i>/proc/sys/fs/epoll</i> (since Linux 2.6.28) </dt>
<dd>  This directory contains the file <i>max_user_watches</i>, which can be used to limit the amount of kernel memory consumed by the <i>epoll</i> interface. For further details, see <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7).  </dd>
<dt><i>/proc/sys/fs/file-max</i> </dt>
<dd>  This file defines a system-wide limit on the number of open files for all processes. System calls that fail when encountering this limit fail with the error <code>ENFILE</code>. (See also <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), which can be used by a process to set the per-process limit, <code>RLIMIT_NOFILE</code>, on the number of files it may open.) If you get lots of error messages in the kernel log about running out of file handles (open file descriptions) (look for &quot;VFS: file-max limit &lt;number&gt; reached&quot;), try increasing this value:  </dd>
<dd>  echo 100000 &gt; /proc/sys/fs/file-max  </dd>
<dd>  Privileged processes (<code>CAP_SYS_ADMIN</code>) can override the <i>file-max</i> limit.  </dd>
<dt><i>/proc/sys/fs/file-nr</i> </dt>
<dd>  This (read-only) file contains three numbers: the number of allocated file handles (i.e., the number of open file descriptions; see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)); the number of free file handles; and the maximum number of file handles (i.e., the same value as <i>/proc/sys/fs/file-max</i>). If the number of allocated file handles is close to the maximum, you should consider increasing the maximum. Before Linux 2.6, the kernel allocated file handles dynamically, but it didn&#8217;t free them again. Instead the free file handles were kept in a list for reallocation; the &quot;free file handles&quot; value indicates the size of that list. A large number of free file handles indicates that there was a past peak in the usage of open file handles. Since Linux 2.6, the kernel does deallocate freed file handles, and the &quot;free file handles&quot; value is always zero.  </dd>
<dt><i>/proc/sys/fs/inode-max</i> (only present until Linux 2.2) </dt>
<dd>  This file contains the maximum number of in-memory inodes. This value should be 3-4 times larger than the value in <i>file-max</i>, since <i>stdin</i>, <i>stdout</i> and network sockets also need an inode to handle them. When you regularly run out of inodes, you need to increase this value.  </dd>
<dd>  Starting with Linux 2.4, there is no longer a static limit on the number of inodes, and this file is removed.  </dd>
<dt><i>/proc/sys/fs/inode-nr</i> </dt>
<dd>  This file contains the first two values from <i>inode-state</i>.  </dd>
<dt><i>/proc/sys/fs/inode-state</i> </dt>
<dd>  This file contains seven numbers: <i>nr_inodes</i>, <i>nr_free_inodes</i>, <i>preshrink</i>, and four dummy values (always zero).  </dd>
<dd>  <i>nr_inodes</i> is the number of inodes the system has allocated. <i>nr_free_inodes</i> represents the number of free inodes.  </dd>
<dd>  <i>preshrink</i> is nonzero when the <i>nr_inodes</i> &gt; <i>inode-max</i> and the system needs to prune the inode list instead of allocating more; since Linux 2.4, this field is a dummy value (always zero).  </dd>
<dt><i>/proc/sys/fs/inotify</i> (since Linux 2.6.13) </dt>
<dd>  This directory contains files <i>max_queued_events</i>, <i>max_user_instances</i>, and <i>max_user_watches</i>, that can be used to limit the amount of kernel memory consumed by the <i>inotify</i> interface. For further details, see <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7).  </dd>
<dt><i>/proc/sys/fs/lease-break-time</i> </dt>
<dd>  This file specifies the grace period that the kernel grants to a process holding a file lease (<code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) after it has sent a signal to that process notifying it that another process is waiting to open the file. If the lease holder does not remove or downgrade the lease within this grace period, the kernel forcibly breaks the lease.  </dd>
<dt><i>/proc/sys/fs/leases-enable</i> </dt>
<dd>  This file can be used to enable or disable file leases (<code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) on a system-wide basis. If this file contains the value 0, leases are disabled. A nonzero value enables leases.  </dd>
<dt><i>/proc/sys/fs/mount-max</i> (since Linux 4.9) </dt>
<dd>  The value in this file specifies the maximum number of mounts that may exist in a mount namespace. The default value in this file is 100,000.  </dd>
<dt><i>/proc/sys/fs/mqueue</i> (since Linux 2.6.6) </dt>
<dd>  This directory contains files <i>msg_max</i>, <i>msgsize_max</i>, and <i>queues_max</i>, controlling the resources used by POSIX message queues. See <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7) for details.  </dd>
<dt><i>/proc/sys/fs/nr_open</i> (since Linux 2.6.25) </dt>
<dd>  This file imposes a ceiling on the value to which the <code>RLIMIT_NOFILE</code> resource limit can be raised (see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)). This ceiling is enforced for both unprivileged and privileged process. The default value in this file is 1048576. (Before Linux 2.6.25, the ceiling for <code>RLIMIT_NOFILE</code> was hard-coded to the same value.)  </dd>
<dt><i>/proc/sys/fs/overflowgid</i> and <i>/proc/sys/fs/overflowuid</i> </dt>
<dd>  These files allow you to change the value of the fixed UID and GID. The default is 65534. Some filesystems support only 16-bit UIDs and GIDs, although in Linux UIDs and GIDs are 32 bits. When one of these filesystems is mounted with writes enabled, any UID or GID that would exceed 65535 is translated to the overflow value before being written to disk.  </dd>
<dt><i>/proc/sys/fs/pipe-max-size</i> (since Linux 2.6.35) </dt>
<dd>  See <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7).  </dd>
<dt><i>/proc/sys/fs/pipe-user-pages-hard</i> (since Linux 4.5) </dt>
<dd>  See <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7).  </dd>
<dt><i>/proc/sys/fs/pipe-user-pages-soft</i> (since Linux 4.5) </dt>
<dd>  See <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7).  </dd>
<dt><i>/proc/sys/fs/protected_fifos</i> (since Linux 4.19) </dt>
<dd>  The value in this file is/can be set to one of the following:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>0</dt>
<dd>  Writing to FIFOs is unrestricted.  </dd>
<dt>1</dt>
<dd>  Don&#8217;t allow <code>O_CREAT</code> <code><a href="/docs/linux/man/2-open/">open</a></code>(2) on FIFOs that the caller doesn&#8217;t own in world-writable sticky directories, unless the FIFO is owned by the owner of the directory.  </dd>
<dt>2</dt>
<dd>  As for the value 1, but the restriction also applies to group-writable sticky directories.  </dd></dl>
 </dl>
 <dd>  The intent of the above protections is to avoid unintentional writes to an attacker-controlled FIFO when a program expected to create a regular file.  </dd>
<dt><i>/proc/sys/fs/protected_hardlinks</i> (since Linux 3.6) </dt>
<dd>  When the value in this file is 0, no restrictions are placed on the creation of hard links (i.e., this is the historical behavior before Linux 3.6). When the value in this file is 1, a hard link can be created to a target file only if one of the following conditions is true:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>*</dt>
<dd>  The calling process has the <code>CAP_FOWNER</code> capability in its user namespace and the file UID has a mapping in the namespace.  </dd>
<dt>*</dt>
<dd>  The filesystem UID of the process creating the link matches the owner (UID) of the target file (as described in <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), a process&#8217;s filesystem UID is normally the same as its effective UID).  </dd>
<dt>*</dt>
<dd>  All of the following conditions are true:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>&bull;</dt>
<dd>  the target is a regular file;  </dd>
<dt>&bull;</dt>
<dd>  the target file does not have its set-user-ID mode bit enabled;  </dd>
<dt>&bull;</dt>
<dd>  the target file does not have both its set-group-ID and group-executable mode bits enabled; and  </dd>
<dt>&bull;</dt>
<dd>  the caller has permission to read and write the target file (either via the file&#8217;s permissions mask or because it has suitable capabilities).  </dd></dl>
 </dl>
 </dl>
 </dl>
 <dd>  The default value in this file is 0. Setting the value to 1 prevents a longstanding class of security issues caused by hard-link-based time-of-check, time-of-use races, most commonly seen in world-writable directories such as <i>/tmp</i>. The common method of exploiting this flaw is to cross privilege boundaries when following a given hard link (i.e., a root process follows a hard link created by another user). Additionally, on systems without separated partitions, this stops unauthorized users from &quot;pinning&quot; vulnerable set-user-ID and set-group-ID files against being upgraded by the administrator, or linking to special files.  </dd>
<dt><i>/proc/sys/fs/protected_regular</i> (since Linux 4.19) </dt>
<dd>  The value in this file is/can be set to one of the following:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>0</dt>
<dd>  Writing to regular files is unrestricted.  </dd>
<dt>1</dt>
<dd>  Don&#8217;t allow <code>O_CREAT</code> <code><a href="/docs/linux/man/2-open/">open</a></code>(2) on regular files that the caller doesn&#8217;t own in world-writable sticky directories, unless the regular file is owned by the owner of the directory.  </dd>
<dt>2</dt>
<dd>  As for the value 1, but the restriction also applies to group-writable sticky directories.  </dd></dl>
 </dl>
 <dd>  The intent of the above protections is similar to <i>protected_fifos</i>, but allows an application to avoid writes to an attacker-controlled regular file, where the application expected to create one.  </dd>
<dt><i>/proc/sys/fs/protected_symlinks</i> (since Linux 3.6) </dt>
<dd>  When the value in this file is 0, no restrictions are placed on following symbolic links (i.e., this is the historical behavior before Linux 3.6). When the value in this file is 1, symbolic links are followed only in the following circumstances:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>*</dt>
<dd>  the filesystem UID of the process following the link matches the owner (UID) of the symbolic link (as described in <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), a process&#8217;s filesystem UID is normally the same as its effective UID);  </dd>
<dt>*</dt>
<dd>  the link is not in a sticky world-writable directory; or  </dd>
<dt>*</dt>
<dd>  the symbolic link and its parent directory have the same owner (UID)  </dd></dl>
 </dl>
 <dd>  A system call that fails to follow a symbolic link because of the above restrictions returns the error <code>EACCES</code> in <i>errno</i>.  </dd>
<dd>  The default value in this file is 0. Setting the value to 1 avoids a longstanding class of security issues based on time-of-check, time-of-use races when accessing symbolic links.  </dd>
<dt><i>/proc/sys/fs/suid_dumpable</i> (since Linux 2.6.13) </dt>
<dd>  The value in this file is assigned to a process&#8217;s &quot;dumpable&quot; flag in the circumstances described in <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2). In effect, the value in this file determines whether core dump files are produced for set-user-ID or otherwise protected/tainted binaries. The &quot;dumpable&quot; setting also affects the ownership of files in a process&#8217;s <i>/proc/[pid]</i> directory, as described above.  </dd>
<dd>  Three different integer values can be specified:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>0&nbsp;(default)</i></dt>
<dd>  This provides the traditional (pre-Linux 2.6.13) behavior. A core dump will not be produced for a process which has changed credentials (by calling <code><a href="/docs/linux/man/2-seteuid/">seteuid</a></code>(2), <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2), or similar, or by executing a set-user-ID or set-group-ID program) or whose binary does not have read permission enabled.  </dd>
<dt><i>1&nbsp;(&quot;debug&quot;)</i></dt>
<dd>  All processes dump core when possible. (Reasons why a process might nevertheless not dump core are described in <code><a href="/docs/linux/man/5-core/">core</a></code>(5).) The core dump is owned by the filesystem user ID of the dumping process and no security is applied. This is intended for system debugging situations only: this mode is insecure because it allows unprivileged users to examine the memory contents of privileged processes.  </dd>
<dt><i>2&nbsp;(&quot;suidsafe&quot;)</i></dt>
<dd>  Any binary which normally would not be dumped (see &quot;0&quot; above) is dumped readable by root only. This allows the user to remove the core dump file but not to read it. For security reasons core dumps in this mode will not overwrite one another or other files. This mode is appropriate when administrators are attempting to debug problems in a normal environment.  </dd>
<dd>  Additionally, since Linux 3.6, <i>/proc/sys/kernel/core_pattern</i> must either be an absolute pathname or a pipe command, as detailed in <code><a href="/docs/linux/man/5-core/">core</a></code>(5). Warnings will be written to the kernel log if <i>core_pattern</i> does not follow these rules, and no core dump will be produced.  </dd></dl>
 </dl>
 <dd>  For details of the effect of a process&#8217;s &quot;dumpable&quot; setting on ptrace access mode checking, see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/sys/fs/super-max</i> </dt>
<dd>  This file controls the maximum number of superblocks, and thus the maximum number of mounted filesystems the kernel can have. You need increase only <i>super-max</i> if you need to mount more filesystems than the current value in <i>super-max</i> allows you to.  </dd>
<dt><i>/proc/sys/fs/super-nr</i> </dt>
<dd>  This file contains the number of filesystems currently mounted.  </dd>
<dt><i>/proc/sys/kernel</i> </dt>
<dd>  This directory contains files controlling a range of kernel parameters, as described below.  </dd>
<dt><i>/proc/sys/kernel/acct</i> </dt>
<dd>  This file contains three numbers: <i>highwater</i>, <i>lowwater</i>, and <i>frequency</i>. If BSD-style process accounting is enabled, these values control its behavior. If free space on filesystem where the log lives goes below <i>lowwater</i> percent, accounting suspends. If free space gets above <i>highwater</i> percent, accounting resumes. <i>frequency</i> determines how often the kernel checks the amount of free space (value is in seconds). Default values are 4, 2 and 30. That is, suspend accounting if 2% or less space is free; resume it if 4% or more space is free; consider information about amount of free space valid for 30 seconds.  </dd>
<dt><i>/proc/sys/kernel/auto_msgmni</i> (Linux 2.6.27 to 3.18) </dt>
<dd>  From Linux 2.6.27 to 3.18, this file was used to control recomputing of the value in <i>/proc/sys/kernel/msgmni</i> upon the addition or removal of memory or upon IPC namespace creation/removal. Echoing &quot;1&quot; into this file enabled <i>msgmni</i> automatic recomputing (and triggered a recomputation of <i>msgmni</i> based on the current amount of available memory and number of IPC namespaces). Echoing &quot;0&quot; disabled automatic recomputing. (Automatic recomputing was also disabled if a value was explicitly assigned to <i>/proc/sys/kernel/msgmni</i>.) The default value in <i>auto_msgmni</i> was 1.  </dd>
<dd>  Since Linux 3.19, the content of this file has no effect (because <i>msgmni</i> defaults to near the maximum value possible), and reads from this file always return the value &quot;0&quot;.  </dd>
<dt><i>/proc/sys/kernel/cap_last_cap</i> (since Linux 3.2) </dt>
<dd>  See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7).  </dd>
<dt><i>/proc/sys/kernel/cap-bound</i> (from Linux 2.2 to 2.6.24) </dt>
<dd>  This file holds the value of the kernel <i>capability bounding set</i> (expressed as a signed decimal number). This set is ANDed against the capabilities permitted to a process during <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). Starting with Linux 2.6.25, the system-wide capability bounding set disappeared, and was replaced by a per-thread bounding set; see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7).  </dd>
<dt><i>/proc/sys/kernel/core_pattern</i> </dt>
<dd>  See <code><a href="/docs/linux/man/5-core/">core</a></code>(5).  </dd>
<dt><i>/proc/sys/kernel/core_pipe_limit</i> </dt>
<dd>  See <code><a href="/docs/linux/man/5-core/">core</a></code>(5).  </dd>
<dt><i>/proc/sys/kernel/core_uses_pid</i> </dt>
<dd>  See <code><a href="/docs/linux/man/5-core/">core</a></code>(5).  </dd>
<dt><i>/proc/sys/kernel/ctrl-alt-del</i> </dt>
<dd>  This file controls the handling of Ctrl-Alt-Del from the keyboard. When the value in this file is 0, Ctrl-Alt-Del is trapped and sent to the <code><a href="/docs/linux/man/1-init/">init</a></code>(1) program to handle a graceful restart. When the value is greater than zero, Linux&#8217;s reaction to a Vulcan Nerve Pinch (tm) will be an immediate reboot, without even syncing its dirty buffers. Note: when a program (like dosemu) has the keyboard in &quot;raw&quot; mode, the ctrl-alt-del is intercepted by the program before it ever reaches the kernel tty layer, and it&#8217;s up to the program to decide what to do with it.  </dd>
<dt><i>/proc/sys/kernel/dmesg_restrict</i> (since Linux 2.6.37) </dt>
<dd>  The value in this file determines who can see kernel syslog contents. A value of 0 in this file imposes no restrictions. If the value is 1, only privileged users can read the kernel syslog. (See <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) for more details.) Since Linux 3.4, only users with the <code>CAP_SYS_ADMIN</code> capability may change the value in this file.  </dd>
<dt><i>/proc/sys/kernel/domainname</i> and <i>/proc/sys/kernel/hostname</i> </dt>
<dd>  can be used to set the NIS/YP domainname and the hostname of your box in exactly the same way as the commands <code><a href="/docs/linux/man/1-domainname/">domainname</a></code>(1) and <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1), that is:  </dd>
<dd>  #<code> echo &#8216;darkstar&#8217; &gt; /proc/sys/kernel/hostname</code> #<code> echo &#8216;mydomain&#8217; &gt; /proc/sys/kernel/domainname</code>  </dd>
<dd>  has the same effect as  </dd>
<dd>  #<code> hostname &#8216;darkstar&#8217;</code> #<code> domainname &#8216;mydomain&#8217;</code>  </dd>
<dd>  Note, however, that the classic darkstar.frop.org has the hostname &quot;darkstar&quot; and DNS (Internet Domain Name Server) domainname &quot;frop.org&quot;, not to be confused with the NIS (Network Information Service) or YP (Yellow Pages) domainname. These two domain names are in general different. For a detailed discussion see the <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1) man page.  </dd>
<dt><i>/proc/sys/kernel/hotplug</i> </dt>
<dd>  This file contains the pathname for the hotplug policy agent. The default value in this file is <i>/sbin/hotplug</i>.  </dd>
<dd>  <i>/proc/sys/kernel/htab-reclaim</i> (before Linux 2.4.9.2) (PowerPC only) If this file is set to a nonzero value, the PowerPC htab (see kernel file <i>Documentation/powerpc/ppc_htab.txt</i>) is pruned each time the system hits the idle loop.  </dd>
<dt><i>/proc/sys/kernel/keys/*</i> </dt>
<dd>  This directory contains various files that define parameters and limits for the key-management facility. These files are described in <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7).  </dd>
<dt><i>/proc/sys/kernel/kptr_restrict</i> (since Linux 2.6.38) </dt>
<dd>  The value in this file determines whether kernel addresses are exposed via <i>/proc</i> files and other interfaces. A value of 0 in this file imposes no restrictions. If the value is 1, kernel pointers printed using the <i>%pK</i> format specifier will be replaced with zeros unless the user has the <code>CAP_SYSLOG</code> capability. If the value is 2, kernel pointers printed using the <i>%pK</i> format specifier will be replaced with zeros regardless of the user&#8217;s capabilities. The initial default value for this file was 1, but the default was changed to 0 in Linux 2.6.39. Since Linux 3.4, only users with the <code>CAP_SYS_ADMIN</code> capability can change the value in this file.  </dd>
<dt><i>/proc/sys/kernel/l2cr</i> </dt>
<dd>  (PowerPC only) This file contains a flag that controls the L2 cache of G3 processor boards. If 0, the cache is disabled. Enabled if nonzero.  </dd>
<dt><i>/proc/sys/kernel/modprobe</i> </dt>
<dd>  This file contains the pathname for the kernel module loader. The default value is <i>/sbin/modprobe</i>. The file is present only if the kernel is built with the <code>CONFIG_MODULES</code> (<code>CONFIG_KMOD</code> in Linux 2.6.26 and earlier) option enabled. It is described by the Linux kernel source file <i>Documentation/kmod.txt</i> (present only in kernel 2.4 and earlier).  </dd>
<dt><i>/proc/sys/kernel/modules_disabled</i> (since Linux 2.6.31) </dt>
<dd>  A toggle value indicating if modules are allowed to be loaded in an otherwise modular kernel. This toggle defaults to off (0), but can be set true (1). Once true, modules can be neither loaded nor unloaded, and the toggle cannot be set back to false. The file is present only if the kernel is built with the <code>CONFIG_MODULES</code> option enabled.  </dd>
<dt><i>/proc/sys/kernel/msgmax</i> (since Linux 2.2) </dt>
<dd>  This file defines a system-wide limit specifying the maximum number of bytes in a single message written on a System V message queue.  </dd>
<dt><i>/proc/sys/kernel/msgmni</i> (since Linux 2.4) </dt>
<dd>  This file defines the system-wide limit on the number of message queue identifiers. See also <i>/proc/sys/kernel/auto_msgmni</i>.  </dd>
<dt><i>/proc/sys/kernel/msgmnb</i> (since Linux 2.2) </dt>
<dd>  This file defines a system-wide parameter used to initialize the <i>msg_qbytes</i> setting for subsequently created message queues. The <i>msg_qbytes</i> setting specifies the maximum number of bytes that may be written to the message queue.  </dd>
<dt><i>/proc/sys/kernel/ngroups_max</i> (since Linux 2.6.4) </dt>
<dd>  This is a read-only file that displays the upper limit on the number of a process&#8217;s group memberships.  </dd>
<dt><i>/proc/sys/kernel/ns_last_pid</i> (since Linux 3.3) </dt>
<dd>  See <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7).  </dd>
<dt><i>/proc/sys/kernel/ostype</i> and <i>/proc/sys/kernel/osrelease</i> </dt>
<dd>  These files give substrings of <i>/proc/version</i>.  </dd>
<dt><i>/proc/sys/kernel/overflowgid</i> and <i>/proc/sys/kernel/overflowuid</i> </dt>
<dd>  These files duplicate the files <i>/proc/sys/fs/overflowgid</i> and <i>/proc/sys/fs/overflowuid</i>.  </dd>
<dt><i>/proc/sys/kernel/panic</i> </dt>
<dd>  This file gives read/write access to the kernel variable <i>panic_timeout</i>. If this is zero, the kernel will loop on a panic; if nonzero, it indicates that the kernel should autoreboot after this number of seconds. When you use the software watchdog device driver, the recommended setting is 60.  </dd>
<dt><i>/proc/sys/kernel/panic_on_oops</i> (since Linux 2.5.68) </dt>
<dd>  This file controls the kernel&#8217;s behavior when an oops or BUG is encountered. If this file contains 0, then the system tries to continue operation. If it contains 1, then the system delays a few seconds (to give klogd time to record the oops output) and then panics. If the <i>/proc/sys/kernel/panic</i> file is also nonzero, then the machine will be rebooted.  </dd>
<dt><i>/proc/sys/kernel/pid_max</i> (since Linux 2.5.34) </dt>
<dd>  This file specifies the value at which PIDs wrap around (i.e., the value in this file is one greater than the maximum PID). PIDs greater than this value are not allocated; thus, the value in this file also acts as a system-wide limit on the total number of processes and threads. The default value for this file, 32768, results in the same range of PIDs as on earlier kernels. On 32-bit platforms, 32768 is the maximum value for <i>pid_max</i>. On 64-bit systems, <i>pid_max</i> can be set to any value up to 2^22 (<code>PID_MAX_LIMIT</code>, approximately 4 million).  </dd>
<dt><i>/proc/sys/kernel/powersave-nap</i> (PowerPC only) </dt>
<dd>  This file contains a flag. If set, Linux-PPC will use the &quot;nap&quot; mode of powersaving, otherwise the &quot;doze&quot; mode will be used.  </dd>
<dt><i>/proc/sys/kernel/printk</i> </dt>
<dd>  See <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2).  </dd>
<dt><i>/proc/sys/kernel/pty</i> (since Linux 2.6.4) </dt>
<dd>  This directory contains two files relating to the number of UNIX 98 pseudoterminals (see <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4)) on the system.  </dd>
<dt><i>/proc/sys/kernel/pty/max</i> </dt>
<dd>  This file defines the maximum number of pseudoterminals.  </dd>
<dt><i>/proc/sys/kernel/pty/nr</i> </dt>
<dd>  This read-only file indicates how many pseudoterminals are currently in use.  </dd>
<dt><i>/proc/sys/kernel/random</i> </dt>
<dd>  This directory contains various parameters controlling the operation of the file <i>/dev/random</i>. See <code><a href="/docs/linux/man/4-random/">random</a></code>(4) for further information.  </dd>
<dt><i>/proc/sys/kernel/random/uuid</i> (since Linux 2.4) </dt>
<dd>  Each read from this read-only file returns a randomly generated 128-bit UUID, as a string in the standard UUID format.  </dd>
<dt><i>/proc/sys/kernel/randomize_va_space</i> (since Linux 2.6.12) </dt>
<dd>  Select the address space layout randomization (ASLR) policy for the system (on architectures that support ASLR). Three values are supported for this file:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>0</dt>
<dd>  Turn ASLR off. This is the default for architectures that don&#8217;t support ASLR, and when the kernel is booted with the <i>norandmaps</i> parameter.  </dd>
<dt>1</dt>
<dd>  Make the addresses of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) allocations, the stack, and the VDSO page randomized. Among other things, this means that shared libraries will be loaded at randomized addresses. The text segment of PIE-linked binaries will also be loaded at a randomized address. This value is the default if the kernel was configured with <code>CONFIG_COMPAT_BRK</code>.  </dd>
<dt>2</dt>
<dd>  (Since Linux 2.6.25) Also support heap randomization. This value is the default if the kernel was not configured with <code>CONFIG_COMPAT_BRK</code>.  </dd></dl>
 </dl>
 <dt><i>/proc/sys/kernel/real-root-dev</i> </dt>
<dd>  This file is documented in the Linux kernel source file <i>Documentation/admin-guide/initrd.rst</i> (or <i>Documentation/initrd.txt</i> before Linux 4.10).  </dd>
<dt><i>/proc/sys/kernel/reboot-cmd</i> (Sparc only) </dt>
<dd>  This file seems to be a way to give an argument to the SPARC ROM/Flash boot loader. Maybe to tell it what to do after rebooting?  </dd>
<dt><i>/proc/sys/kernel/rtsig-max</i> </dt>
<dd>  (Only in kernels up to and including 2.6.7; see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)) This file can be used to tune the maximum number of POSIX real-time (queued) signals that can be outstanding in the system.  </dd>
<dt><i>/proc/sys/kernel/rtsig-nr</i> </dt>
<dd>  (Only in kernels up to and including 2.6.7.) This file shows the number of POSIX real-time signals currently queued.  </dd>
<dt><i>/proc/[pid]/sched_autogroup_enabled</i> (since Linux 2.6.38) </dt>
<dd>  See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).  </dd>
<dt><i>/proc/sys/kernel/sched_child_runs_first</i> (since Linux 2.6.23) </dt>
<dd>  If this file contains the value zero, then, after a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), the parent is first scheduled on the CPU. If the file contains a nonzero value, then the child is scheduled first on the CPU. (Of course, on a multiprocessor system, the parent and the child might both immediately be scheduled on a CPU.)  </dd>
<dt><i>/proc/sys/kernel/sched_rr_timeslice_ms</i> (since Linux 3.9) </dt>
<dd>  See <code><a href="/docs/linux/man/2-sched_rr_get_interval/">sched_rr_get_interval</a></code>(2).  </dd>
<dt><i>/proc/sys/kernel/sched_rt_period_us</i> (since Linux 2.6.25) </dt>
<dd>  See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).  </dd>
<dt><i>/proc/sys/kernel/sched_rt_runtime_us</i> (since Linux 2.6.25) </dt>
<dd>  See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).  </dd>
<dt><i>/proc/sys/kernel/seccomp</i> (since Linux 4.14) </dt>
<dd>  This directory provides additional seccomp information and configuration. See <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) for further details.  </dd>
<dt><i>/proc/sys/kernel/sem</i> (since Linux 2.4) </dt>
<dd>  This file contains 4 numbers defining limits for System V IPC semaphores. These fields are, in order:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>SEMMSL</dt>
<dd>  The maximum semaphores per semaphore set.  </dd>
<dt>SEMMNS</dt>
<dd>  A system-wide limit on the number of semaphores in all semaphore sets.  </dd>
<dt>SEMOPM</dt>
<dd>  The maximum number of operations that may be specified in a <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) call.  </dd>
<dt>SEMMNI</dt>
<dd>  A system-wide limit on the maximum number of semaphore identifiers.  </dd></dl>
 </dl>
 <dt><i>/proc/sys/kernel/sg-big-buff</i> </dt>
<dd>  This file shows the size of the generic SCSI device (sg) buffer. You can&#8217;t tune it just yet, but you could change it at compile time by editing <i>include/scsi/sg.h</i> and changing the value of <code>SG_BIG_BUFF</code>. However, there shouldn&#8217;t be any reason to change this value.  </dd>
<dt><i>/proc/sys/kernel/shm_rmid_forced</i> (since Linux 3.1) </dt>
<dd>  If this file is set to 1, all System V shared memory segments will be marked for destruction as soon as the number of attached processes falls to zero; in other words, it is no longer possible to create shared memory segments that exist independently of any attached process.  </dd>
<dd>  The effect is as though a <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2) <code>IPC_RMID</code> is performed on all existing segments as well as all segments created in the future (until this file is reset to 0). Note that existing segments that are attached to no process will be immediately destroyed when this file is set to 1. Setting this option will also destroy segments that were created, but never attached, upon termination of the process that created the segment with <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2).  </dd>
<dd>  Setting this file to 1 provides a way of ensuring that all System V shared memory segments are counted against the resource usage and resource limits (see the description of <code>RLIMIT_AS</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)) of at least one process.  </dd>
<dd>  Because setting this file to 1 produces behavior that is nonstandard and could also break existing applications, the default value in this file is 0. Set this file to 1 only if you have a good understanding of the semantics of the applications using System V shared memory on your system.  </dd>
<dt><i>/proc/sys/kernel/shmall</i> (since Linux 2.2) </dt>
<dd>  This file contains the system-wide limit on the total number of pages of System V shared memory.  </dd>
<dt><i>/proc/sys/kernel/shmmax</i> (since Linux 2.2) </dt>
<dd>  This file can be used to query and set the run-time limit on the maximum (System V IPC) shared memory segment size that can be created. Shared memory segments up to 1 GB are now supported in the kernel. This value defaults to <code>SHMMAX</code>.  </dd>
<dt><i>/proc/sys/kernel/shmmni</i> (since Linux 2.4) </dt>
<dd>  This file specifies the system-wide maximum number of System V shared memory segments that can be created.  </dd>
<dt><i>/proc/sys/kernel/sysctl_writes_strict</i> (since Linux 3.16) </dt>
<dd>  The value in this file determines how the file offset affects the behavior of updating entries in files under <i>/proc/sys</i>. The file has three possible values:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>-1</dt>
<dd>  This provides legacy handling, with no printk warnings. Each <code><a href="/docs/linux/man/2-write/">write</a></code>(2) must fully contain the value to be written, and multiple writes on the same file descriptor will overwrite the entire value, regardless of the file position.  </dd>
<dt>0</dt>
<dd>  (default) This provides the same behavior as for -1, but printk warnings are written for processes that perform writes when the file offset is not 0.  </dd>
<dt>1</dt>
<dd>  Respect the file offset when writing strings into <i>/proc/sys</i> files. Multiple writes will <i>append</i> to the value buffer. Anything written beyond the maximum length of the value buffer will be ignored. Writes to numeric <i>/proc/sys</i> entries must always be at file offset 0 and the value must be fully contained in the buffer provided to <code><a href="/docs/linux/man/2-write/">write</a></code>(2).  </dd></dl>
 </dl>
 <dt><i>/proc/sys/kernel/sysrq</i> </dt>
<dd>  This file controls the functions allowed to be invoked by the SysRq key. By default, the file contains 1 meaning that every possible SysRq request is allowed (in older kernel versions, SysRq was disabled by default, and you were required to specifically enable it at run-time, but this is not the case any more). Possible values in this file are:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>0</dt>
<dd>  Disable sysrq completely  </dd>
<dt>1</dt>
<dd>  Enable all functions of sysrq  </dd>
<dt>&gt; 1</dt>
<dd>  Bit mask of allowed sysrq functions, as follows:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>&nbsp;<wbr>&nbsp;2</dt>
<dd>  Enable control of console logging level  </dd>
<dt>&nbsp;<wbr>&nbsp;4</dt>
<dd>  Enable control of keyboard (SAK, unraw)  </dd>
<dt>&nbsp;<wbr>&nbsp;8</dt>
<dd>  Enable debugging dumps of processes etc.  </dd>
<dt>&nbsp;16</dt>
<dd>  Enable sync command  </dd>
<dt>&nbsp;32</dt>
<dd>  Enable remount read-only  </dd>
<dt>&nbsp;64</dt>
<dd>  Enable signaling of processes (term, kill, oom-kill)  </dd>
<dt>128</dt>
<dd>  Allow reboot/poweroff  </dd>
<dt>256</dt>
<dd>  Allow nicing of all real-time tasks  </dd></dl>
 </dl>
 </dl>
 </dl>
 <dd>  This file is present only if the <code>CONFIG_MAGIC_SYSRQ</code> kernel configuration option is enabled. For further details see the Linux kernel source file <i>Documentation/admin-guide/sysrq.rst</i> (or <i>Documentation/sysrq.txt</i> before Linux 4.10).  </dd>
<dt><i>/proc/sys/kernel/version</i> </dt>
<dd>  This file contains a string such as:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#5 Wed Feb 25 21:49:24 MET 1998  </dd>
<dd>  The &quot;#5&quot; means that this is the fifth kernel built from this source base and the date following it indicates the time the kernel was built.  </dd>
<dt><i>/proc/sys/kernel/threads-max</i> (since Linux 2.3.11) </dt>
<dd>  This file specifies the system-wide limit on the number of threads (tasks) that can be created on the system.  </dd>
<dd>  Since Linux 4.1, the value that can be written to <i>threads-max</i> is bounded. The minimum value that can be written is 20. The maximum value that can be written is given by the constant <code>FUTEX_TID_MASK</code> (0x3fffffff). If a value outside of this range is written to <i>threads-max</i>, the error <code>EINVAL</code> occurs.  </dd>
<dd>  The value written is checked against the available RAM pages. If the thread structures would occupy too much (more than 1/8th) of the available RAM pages, <i>threads-max</i> is reduced accordingly.  </dd>
<dt><i>/proc/sys/kernel/yama/ptrace_scope</i> (since Linux 3.5) </dt>
<dd>  See <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).  </dd>
<dt><i>/proc/sys/kernel/zero-paged</i> (PowerPC only) </dt>
<dd>  This file contains a flag. When enabled (nonzero), Linux-PPC will pre-zero pages in the idle loop, possibly speeding up get_free_pages.  </dd>
<dt><i>/proc/sys/net</i> </dt>
<dd>  This directory contains networking stuff. Explanations for some of the files under this directory can be found in <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7) and <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7).  </dd>
<dt><i>/proc/sys/net/core/bpf_jit_enable</i> </dt>
<dd>  See <code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2).  </dd>
<dt><i>/proc/sys/net/core/somaxconn</i> </dt>
<dd>  This file defines a ceiling value for the <i>backlog</i> argument of <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2); see the <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) manual page for details.  </dd>
<dt><i>/proc/sys/proc</i> </dt>
<dd>  This directory may be empty.  </dd>
<dt><i>/proc/sys/sunrpc</i> </dt>
<dd>  This directory supports Sun remote procedure call for network filesystem (NFS). On some systems, it is not present.  </dd>
<dt><i>/proc/sys/user</i> (since Linux 4.9) </dt>
<dd>  See <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7).  </dd>
<dt><i>/proc/sys/vm</i> </dt>
<dd>  This directory contains files for memory management tuning, buffer and cache management.  </dd>
<dt><i>/proc/sys/vm/admin_reserve_kbytes</i> (since Linux 3.10) </dt>
<dd>  This file defines the amount of free memory (in KiB) on the system that should be reserved for users with the capability <code>CAP_SYS_ADMIN</code>.  </dd>
<dd>  The default value in this file is the minimum of [3% of free pages, 8MiB] expressed as KiB. The default is intended to provide enough for the superuser to log in and kill a process, if necessary, under the default overcommit &#8216;guess&#8217; mode (i.e., 0 in <i>/proc/sys/vm/overcommit_memory</i>).  </dd>
<dd>  Systems running in &quot;overcommit never&quot; mode (i.e., 2 in <i>/proc/sys/vm/overcommit_memory</i>) should increase the value in this file to account for the full virtual memory size of the programs used to recover (e.g., <code><a href="/docs/linux/man/1-login/">login</a></code>(1) <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), and <code><a href="/docs/linux/man/1-top/">top</a></code>(1)) Otherwise, the superuser may not be able to log in to recover the system. For example, on x86-64 a suitable value is 131072 (128MiB reserved).  </dd>
<dd>  Changing the value in this file takes effect whenever an application requests memory.  </dd>
<dt><i>/proc/sys/vm/compact_memory</i> (since Linux 2.6.35) </dt>
<dd>  When 1 is written to this file, all zones are compacted such that free memory is available in contiguous blocks where possible. The effect of this action can be seen by examining <i>/proc/buddyinfo</i>.  </dd>
<dd>  Present only if the kernel was configured with <code>CONFIG_COMPACTION</code>.  </dd>
<dt><i>/proc/sys/vm/drop_caches</i> (since Linux 2.6.16) </dt>
<dd>  Writing to this file causes the kernel to drop clean caches, dentries, and inodes from memory, causing that memory to become free. This can be useful for memory management testing and performing reproducible filesystem benchmarks. Because writing to this file causes the benefits of caching to be lost, it can degrade overall system performance.  </dd>
<dd>  To free pagecache, use:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;echo 1&nbsp;&gt;&nbsp;/proc/sys/vm/drop_caches  </dd>
<dd>  To free dentries and inodes, use:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;echo 2&nbsp;&gt;&nbsp;/proc/sys/vm/drop_caches  </dd>
<dd>  To free pagecache, dentries and inodes, use:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;echo 3&nbsp;&gt;&nbsp;/proc/sys/vm/drop_caches  </dd>
<dd>  Because writing to this file is a nondestructive operation and dirty objects are not freeable, the user should run <code><a href="/docs/linux/man/1-sync/">sync</a></code>(1) first.  </dd>
<dt><i>/proc/sys/vm/legacy_va_layout</i> (since Linux 2.6.9) </dt>
<dd>  If nonzero, this disables the new 32-bit memory-mapping layout; the kernel will use the legacy (2.4) layout for all processes.  </dd>
<dt><i>/proc/sys/vm/memory_failure_early_kill</i> (since Linux 2.6.32) </dt>
<dd>  Control how to kill processes when an uncorrected memory error (typically a 2-bit error in a memory module) that cannot be handled by the kernel is detected in the background by hardware. In some cases (like the page still having a valid copy on disk), the kernel will handle the failure transparently without affecting any applications. But if there is no other up-to-date copy of the data, it will kill processes to prevent any data corruptions from propagating.  </dd>
<dd>  The file has one of the following values:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>1:</dt>
<dd>  Kill all processes that have the corrupted-and-not-reloadable page mapped as soon as the corruption is detected. Note that this is not supported for a few types of pages, such as kernel internally allocated data or the swap cache, but works for the majority of user pages.  </dd>
<dt>0:</dt>
<dd>  Unmap the corrupted page from all processes and kill a process only if it tries to access the page.  </dd></dl>
 </dl>
 <dd>  The kill is performed using a <code>SIGBUS</code> signal with <i>si_code</i> set to <code>BUS_MCEERR_AO</code>. Processes can handle this if they want to; see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) for more details.  </dd>
<dd>  This feature is active only on architectures/platforms with advanced machine check handling and depends on the hardware capabilities.  </dd>
<dd>  Applications can override the <i>memory_failure_early_kill</i> setting individually with the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_MCE_KILL</code> operation.  </dd>
<dd>  Present only if the kernel was configured with <code>CONFIG_MEMORY_FAILURE</code>.  </dd>
<dt><i>/proc/sys/vm/memory_failure_recovery</i> (since Linux 2.6.32) </dt>
<dd>  Enable memory failure recovery (when supported by the platform).  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>1:</dt>
<dd>  Attempt recovery.  </dd>
<dt>0:</dt>
<dd>  Always panic on a memory failure.  </dd></dl>
 </dl>
 <dd>  Present only if the kernel was configured with <code>CONFIG_MEMORY_FAILURE</code>.  </dd>
<dt><i>/proc/sys/vm/oom_dump_tasks</i> (since Linux 2.6.25) </dt>
<dd>  Enables a system-wide task dump (excluding kernel threads) to be produced when the kernel performs an OOM-killing. The dump includes the following information for each task (thread, process): thread ID, real user ID, thread group ID (process ID), virtual memory size, resident set size, the CPU that the task is scheduled on, oom_adj score (see the description of <i>/proc/[pid]/oom_adj</i>), and command name. This is helpful to determine why the OOM-killer was invoked and to identify the rogue task that caused it.  </dd>
<dd>  If this contains the value zero, this information is suppressed. On very large systems with thousands of tasks, it may not be feasible to dump the memory state information for each one. Such systems should not be forced to incur a performance penalty in OOM situations when the information may not be desired.  </dd>
<dd>  If this is set to nonzero, this information is shown whenever the OOM-killer actually kills a memory-hogging task.  </dd>
<dd>  The default value is 0.  </dd>
<dt><i>/proc/sys/vm/oom_kill_allocating_task</i> (since Linux 2.6.24) </dt>
<dd>  This enables or disables killing the OOM-triggering task in out-of-memory situations.  </dd>
<dd>  If this is set to zero, the OOM-killer will scan through the entire tasklist and select a task based on heuristics to kill. This normally selects a rogue memory-hogging task that frees up a large amount of memory when killed.  </dd>
<dd>  If this is set to nonzero, the OOM-killer simply kills the task that triggered the out-of-memory condition. This avoids a possibly expensive tasklist scan.  </dd>
<dd>  If <i>/proc/sys/vm/panic_on_oom</i> is nonzero, it takes precedence over whatever value is used in <i>/proc/sys/vm/oom_kill_allocating_task</i>.  </dd>
<dd>  The default value is 0.  </dd>
<dt><i>/proc/sys/vm/overcommit_kbytes</i> (since Linux 3.14) </dt>
<dd>  This writable file provides an alternative to <i>/proc/sys/vm/overcommit_ratio</i> for controlling the <i>CommitLimit</i> when <i>/proc/sys/vm/overcommit_memory</i> has the value 2. It allows the amount of memory overcommitting to be specified as an absolute value (in kB), rather than as a percentage, as is done with <i>overcommit_ratio</i>. This allows for finer-grained control of <i>CommitLimit</i> on systems with extremely large memory sizes.  </dd>
<dd>  Only one of <i>overcommit_kbytes</i> or <i>overcommit_ratio</i> can have an effect: if <i>overcommit_kbytes</i> has a nonzero value, then it is used to calculate <i>CommitLimit</i>, otherwise <i>overcommit_ratio</i> is used. Writing a value to either of these files causes the value in the other file to be set to zero.  </dd>
<dt><i>/proc/sys/vm/overcommit_memory</i> </dt>
<dd>  This file contains the kernel virtual memory accounting mode. Values are:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dd>  0: heuristic overcommit (this is the default) <br />
 1: always overcommit, never check <br />
 2: always check, never overcommit  </dd></dl>
 </dl>
 <dd>  In mode 0, calls of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) with <code>MAP_NORESERVE</code> are not checked, and the default check is very weak, leading to the risk of getting a process &quot;OOM-killed&quot;.  </dd>
<dd>  In mode 1, the kernel pretends there is always enough memory, until memory actually runs out. One use case for this mode is scientific computing applications that employ large sparse arrays. In Linux kernel versions before 2.6.0, any nonzero value implies mode 1.  </dd>
<dd>  In mode 2 (available since Linux 2.6), the total virtual address space that can be allocated (<i>CommitLimit</i> in <i>/proc/meminfo</i>) is calculated as  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CommitLimit&nbsp;=&nbsp;(total_RAM &#8211; total_huge_TLB)&nbsp;* <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;overcommit_ratio&nbsp;/&nbsp;100&nbsp;+&nbsp;total_swap  </dd>
<dd>  where:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>*</dt>
<dd>  <i>total_RAM</i> is the total amount of RAM on the system;  </dd>
<dt>*</dt>
<dd>  <i>total_huge_TLB</i> is the amount of memory set aside for huge pages;  </dd>
<dt>*</dt>
<dd>  <i>overcommit_ratio</i> is the value in <i>/proc/sys/vm/overcommit_ratio</i>; and  </dd>
<dt>*</dt>
<dd>  <i>total_swap</i> is the amount of swap space.  </dd></dl>
 </dl>
 <dd>  For example, on a system with 16 GB of physical RAM, 16 GB of swap, no space dedicated to huge pages, and an <i>overcommit_ratio</i> of 50, this formula yields a <i>CommitLimit</i> of 24 GB.  </dd>
<dd>  Since Linux 3.14, if the value in <i>/proc/sys/vm/overcommit_kbytes</i> is nonzero, then <i>CommitLimit</i> is instead calculated as:  </dd>
<dd>  <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CommitLimit&nbsp;=&nbsp;overcommit_kbytes&nbsp;+&nbsp;total_swap  </dd>
<dd>  See also the description of <i>/proc/sys/vm/admin_reserve_kbytes</i> and <i>/proc/sys/vm/user_reserve_kbytes</i>.  </dd>
<dt><i>/proc/sys/vm/overcommit_ratio</i> (since Linux 2.6.0) </dt>
<dd>  This writable file defines a percentage by which memory can be overcommitted. The default value in the file is 50. See the description of <i>/proc/sys/vm/overcommit_memory</i>.  </dd>
<dt><i>/proc/sys/vm/panic_on_oom</i> (since Linux 2.6.18) </dt>
<dd>  This enables or disables a kernel panic in an out-of-memory situation.  </dd>
<dd>  If this file is set to the value 0, the kernel&#8217;s OOM-killer will kill some rogue process. Usually, the OOM-killer is able to kill a rogue process and the system will survive.  </dd>
<dd>  If this file is set to the value 1, then the kernel normally panics when out-of-memory happens. However, if a process limits allocations to certain nodes using memory policies (<code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) <code>MPOL_BIND</code>) or cpusets (<code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7)) and those nodes reach memory exhaustion status, one process may be killed by the OOM-killer. No panic occurs in this case: because other nodes&#8217; memory may be free, this means the system as a whole may not have reached an out-of-memory situation yet.  </dd>
<dd>  If this file is set to the value 2, the kernel always panics when an out-of-memory condition occurs.  </dd>
<dd>  The default value is 0. 1 and 2 are for failover of clustering. Select either according to your policy of failover.  </dd>
<dt><i>/proc/sys/vm/swappiness</i> </dt>
<dd>  The value in this file controls how aggressively the kernel will swap memory pages. Higher values increase aggressiveness, lower values decrease aggressiveness. The default value is 60.  </dd>
<dt><i>/proc/sys/vm/user_reserve_kbytes</i> (since Linux 3.10) </dt>
<dd>  Specifies an amount of memory (in KiB) to reserve for user processes. This is intended to prevent a user from starting a single memory hogging process, such that they cannot recover (kill the hog). The value in this file has an effect only when <i>/proc/sys/vm/overcommit_memory</i> is set to 2 (&quot;overcommit never&quot; mode). In this case, the system reserves an amount of memory that is the minimum of [3% of current process size, <i>user_reserve_kbytes</i>].  </dd>
<dd>  The default value in this file is the minimum of [3% of free pages, 128MiB] expressed as KiB.  </dd>
<dd>  If the value in this file is set to zero, then a user will be allowed to allocate all free memory with a single process (minus the amount reserved by <i>/proc/sys/vm/admin_reserve_kbytes</i>). Any subsequent attempts to execute a command will result in &quot;fork: Cannot allocate memory&quot;.  </dd>
<dd>  Changing the value in this file takes effect whenever an application requests memory.  </dd>
<dt><i>/proc/sys/vm/unprivileged_userfaultfd</i> (since Linux 5.2) </dt>
<dd>  This (writable) file exposes a flag that controls whether unprivileged processes are allowed to employ <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2). If this file has the value 1, then unprivileged processes may use <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2). If this file has the value 0, then only processes that have the <code>CAP_SYS_PTRACE</code> capability may employ <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2). The default value in this file is 1.  </dd>
<dt><i>/proc/sysrq-trigger</i> (since Linux 2.4.21) </dt>
<dd>  Writing a character to this file triggers the same SysRq function as typing ALT-SysRq-&lt;character&gt; (see the description of <i>/proc/sys/kernel/sysrq</i>). This file is normally writable only by <i>root</i>. For further details see the Linux kernel source file <i>Documentation/admin-guide/sysrq.rst</i> (or <i>Documentation/sysrq.txt</i> before Linux 4.10).  </dd>
<dt><i>/proc/sysvipc</i> </dt>
<dd>  Subdirectory containing the pseudo-files <i>msg</i>, <i>sem</i> and <i>shm</i>. These files list the System V Interprocess Communication (IPC) objects (respectively: message queues, semaphores, and shared memory) that currently exist on the system, providing similar information to that available via <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1). These files have headers and are formatted (one IPC object per line) for easy understanding. <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7) provides further background on the information shown by these files.  </dd>
<dt><i>/proc/thread-self</i> (since Linux 3.17) </dt>
<dd>  This directory refers to the thread accessing the <i>/proc</i> filesystem, and is identical to the <i>/proc/self/task/[tid]</i> directory named by the process thread ID (<i>[tid]</i>) of the same thread.  </dd>
<dt><i>/proc/timer_list</i> (since Linux 2.6.21) </dt>
<dd>  This read-only file exposes a list of all currently pending (high-resolution) timers, all clock-event sources, and their parameters in a human-readable form.  </dd>
<dt><i>/proc/timer_stats</i> (from Linux 2.6.21 until Linux 4.10) </dt>
<dd>  This is a debugging facility to make timer (ab)use in a Linux system visible to kernel and user-space developers. It can be used by kernel and user-space developers to verify that their code does not make undue use of timers. The goal is to avoid unnecessary wakeups, thereby optimizing power consumption.  </dd>
<dd>  If enabled in the kernel (<code>CONFIG_TIMER_STATS</code>), but not used, it has almost zero run-time overhead and a relatively small data-structure overhead. Even if collection is enabled at run time, overhead is low: all the locking is per-CPU and lookup is hashed.  </dd>
<dd>  The <i>/proc/timer_stats</i> file is used both to control sampling facility and to read out the sampled information.  </dd>
<dd>  The <i>timer_stats</i> functionality is inactive on bootup. A sampling period can be started using the following command:  </dd>
<dd>  # echo 1 &gt; /proc/timer_stats  </dd>
<dd>  The following command stops a sampling period:  </dd>
<dd>  # echo 0 &gt; /proc/timer_stats  </dd>
<dd>  The statistics can be retrieved by:  </dd>
<dd>  $ cat /proc/timer_stats  </dd>
<dd>  While sampling is enabled, each readout from <i>/proc/timer_stats</i> will see newly updated statistics. Once sampling is disabled, the sampled information is kept until a new sample period is started. This allows multiple readouts.  </dd>
<dd>  Sample output from <i>/proc/timer_stats</i>:  </dd>
<dd>  $<code> cat /proc/timer_stats</code> Timer Stats Version: v0.3 Sample period: 1.764 s Collection: active <br />
&nbsp;<wbr>&nbsp;255,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 swapper/3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hrtimer_start_range_ns&nbsp;(tick_sched_timer) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;71,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 swapper/1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hrtimer_start_range_ns&nbsp;(tick_sched_timer) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;58,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 swapper/0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hrtimer_start_range_ns&nbsp;(tick_sched_timer) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4,&nbsp;<wbr>&nbsp;1694 gnome-shell&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mod_delayed_work_on&nbsp;(delayed_work_timer_fn) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;17,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7 rcu_sched&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rcu_gp_kthread&nbsp;(process_timeout) ... <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;4911 kworker/u16:0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mod_delayed_work_on&nbsp;(delayed_work_timer_fn) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;1D,&nbsp;<wbr>&nbsp;2522 kworker/0:0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;queue_delayed_work_on&nbsp;(delayed_work_timer_fn) 1029 total events, 583.333 events/sec  </dd>
<dd>  The output columns are:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt>*</dt>
<dd>  a count of the number of events, optionally (since Linux 2.6.23) followed by the letter &#8216;D&#8217; if this is a deferrable timer;  </dd>
<dt>*</dt>
<dd>  the PID of the process that initialized the timer;  </dd>
<dt>*</dt>
<dd>  the name of the process that initialized the timer;  </dd>
<dt>*</dt>
<dd>  the function where the timer was initialized; and  </dd>
<dt>*</dt>
<dd>  (in parentheses) the callback function that is associated with the timer.  </dd></dl>
 </dl>
 <dd>  During the Linux 4.11 development cycle, this file was removed because of security concerns, as it exposes information across namespaces. Furthermore, it is possible to obtain the same information via in-kernel tracing facilities such as ftrace.  </dd>
<dt><i>/proc/tty</i> </dt>
<dd>  Subdirectory containing the pseudo-files and subdirectories for tty drivers and line disciplines.  </dd>
<dt><i>/proc/uptime</i> </dt>
<dd>  This file contains two numbers (values in seconds): the uptime of the system (including time spent in suspend) and the amount of time spent in the idle process.  </dd>
<dt><i>/proc/version</i> </dt>
<dd>  This string identifies the kernel version that is currently running. It includes the contents of <i>/proc/sys/kernel/ostype</i>, <i>/proc/sys/kernel/osrelease</i>, and <i>/proc/sys/kernel/version</i>. For example:  </dd>
<dd>  Linux version 1.0.9 (quinlan [at] phaze) #1 Sat May 14 01:51:54 EDT 1994  </dd>
<dt><i>/proc/vmstat</i> (since Linux 2.6.0) </dt>
<dd>  This file displays various virtual memory statistics. Each line of this file contains a single name-value pair, delimited by white space. Some lines are present only if the kernel was configured with suitable options. (In some cases, the options required for particular files have changed across kernel versions, so they are not listed here. Details can be found by consulting the kernel source code.) The following fields may be present:  </dd>
<dl>
<dd>   </dd>
<dl>
 <dt><i>nr_free_pages</i> (since Linux 2.6.31) </dt>
<dd>   </dd>
<dt><i>nr_alloc_batch</i> (since Linux 3.12) </dt>
<dd>   </dd>
<dt><i>nr_inactive_anon</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>nr_active_anon</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>nr_inactive_file</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>nr_active_file</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>nr_unevictable</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>nr_mlock</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>nr_anon_pages</i> (since Linux 2.6.18) </dt>
<dd>   </dd>
<dt><i>nr_mapped</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>nr_file_pages</i> (since Linux 2.6.18) </dt>
<dd>   </dd>
<dt><i>nr_dirty</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>nr_writeback</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>nr_slab_reclaimable</i> (since Linux 2.6.19) </dt>
<dd>   </dd>
<dt><i>nr_slab_unreclaimable</i> (since Linux 2.6.19) </dt>
<dd>   </dd>
<dt><i>nr_page_table_pages</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>nr_kernel_stack</i> (since Linux 2.6.32) </dt>
<dd>  Amount of memory allocated to kernel stacks.  </dd>
<dt><i>nr_unstable</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>nr_bounce</i> (since Linux 2.6.12) </dt>
<dd>   </dd>
<dt><i>nr_vmscan_write</i> (since Linux 2.6.19) </dt>
<dd>   </dd>
<dt><i>nr_vmscan_immediate_reclaim</i> (since Linux 3.2) </dt>
<dd>   </dd>
<dt><i>nr_writeback_temp</i> (since Linux 2.6.26) </dt>
<dd>   </dd>
<dt><i>nr_isolated_anon</i> (since Linux 2.6.32) </dt>
<dd>   </dd>
<dt><i>nr_isolated_file</i> (since Linux 2.6.32) </dt>
<dd>   </dd>
<dt><i>nr_shmem</i> (since Linux 2.6.32) </dt>
<dd>  Pages used by shmem and <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5).  </dd>
<dt><i>nr_dirtied</i> (since Linux 2.6.37) </dt>
<dd>   </dd>
<dt><i>nr_written</i> (since Linux 2.6.37) </dt>
<dd>   </dd>
<dt><i>nr_pages_scanned</i> (since Linux 3.17) </dt>
<dd>   </dd>
<dt><i>numa_hit</i> (since Linux 2.6.18) </dt>
<dd>   </dd>
<dt><i>numa_miss</i> (since Linux 2.6.18) </dt>
<dd>   </dd>
<dt><i>numa_foreign</i> (since Linux 2.6.18) </dt>
<dd>   </dd>
<dt><i>numa_interleave</i> (since Linux 2.6.18) </dt>
<dd>   </dd>
<dt><i>numa_local</i> (since Linux 2.6.18) </dt>
<dd>   </dd>
<dt><i>numa_other</i> (since Linux 2.6.18) </dt>
<dd>   </dd>
<dt><i>workingset_refault</i> (since Linux 3.15) </dt>
<dd>   </dd>
<dt><i>workingset_activate</i> (since Linux 3.15) </dt>
<dd>   </dd>
<dt><i>workingset_nodereclaim</i> (since Linux 3.15) </dt>
<dd>   </dd>
<dt><i>nr_anon_transparent_hugepages</i> (since Linux 2.6.38) </dt>
<dd>   </dd>
<dt><i>nr_free_cma</i> (since Linux 3.7) </dt>
<dd>  Number of free CMA (Contiguous Memory Allocator) pages.  </dd>
<dt><i>nr_dirty_threshold</i> (since Linux 2.6.37) </dt>
<dd>   </dd>
<dt><i>nr_dirty_background_threshold</i> (since Linux 2.6.37) </dt>
<dd>   </dd>
<dt><i>pgpgin</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pgpgout</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pswpin</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pswpout</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pgalloc_dma</i> (since Linux 2.6.5) </dt>
<dd>   </dd>
<dt><i>pgalloc_dma32</i> (since Linux 2.6.16) </dt>
<dd>   </dd>
<dt><i>pgalloc_normal</i> (since Linux 2.6.5) </dt>
<dd>   </dd>
<dt><i>pgalloc_high</i> (since Linux 2.6.5) </dt>
<dd>   </dd>
<dt><i>pgalloc_movable</i> (since Linux 2.6.23) </dt>
<dd>   </dd>
<dt><i>pgfree</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pgactivate</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pgdeactivate</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pgfault</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pgmajfault</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pgrefill_dma</i> (since Linux 2.6.5) </dt>
<dd>   </dd>
<dt><i>pgrefill_dma32</i> (since Linux 2.6.16) </dt>
<dd>   </dd>
<dt><i>pgrefill_normal</i> (since Linux 2.6.5) </dt>
<dd>   </dd>
<dt><i>pgrefill_high</i> (since Linux 2.6.5) </dt>
<dd>   </dd>
<dt><i>pgrefill_movable</i> (since Linux 2.6.23) </dt>
<dd>   </dd>
<dt><i>pgsteal_kswapd_dma</i> (since Linux 3.4) </dt>
<dd>   </dd>
<dt><i>pgsteal_kswapd_dma32</i> (since Linux 3.4) </dt>
<dd>   </dd>
<dt><i>pgsteal_kswapd_normal</i> (since Linux 3.4) </dt>
<dd>   </dd>
<dt><i>pgsteal_kswapd_high</i> (since Linux 3.4) </dt>
<dd>   </dd>
<dt><i>pgsteal_kswapd_movable</i> (since Linux 3.4) </dt>
<dd>   </dd>
<dt><i>pgsteal_direct_dma</i> </dt>
<dd>   </dd>
<dt><i>pgsteal_direct_dma32</i> (since Linux 3.4) </dt>
<dd>   </dd>
<dt><i>pgsteal_direct_normal</i> (since Linux 3.4) </dt>
<dd>   </dd>
<dt><i>pgsteal_direct_high</i> (since Linux 3.4) </dt>
<dd>   </dd>
<dt><i>pgsteal_direct_movable</i> (since Linux 2.6.23) </dt>
<dd>   </dd>
<dt><i>pgscan_kswapd_dma</i> </dt>
<dd>   </dd>
<dt><i>pgscan_kswapd_dma32</i> (since Linux 2.6.16) </dt>
<dd>   </dd>
<dt><i>pgscan_kswapd_normal</i> (since Linux 2.6.5) </dt>
<dd>   </dd>
<dt><i>pgscan_kswapd_high</i> </dt>
<dd>   </dd>
<dt><i>pgscan_kswapd_movable</i> (since Linux 2.6.23) </dt>
<dd>   </dd>
<dt><i>pgscan_direct_dma</i> </dt>
<dd>   </dd>
<dt><i>pgscan_direct_dma32</i> (since Linux 2.6.16) </dt>
<dd>   </dd>
<dt><i>pgscan_direct_normal</i> </dt>
<dd>   </dd>
<dt><i>pgscan_direct_high</i> </dt>
<dd>   </dd>
<dt><i>pgscan_direct_movable</i> (since Linux 2.6.23) </dt>
<dd>   </dd>
<dt><i>pgscan_direct_throttle</i> (since Linux 3.6) </dt>
<dd>   </dd>
<dt><i>zone_reclaim_failed</i> (since linux 2.6.31) </dt>
<dd>   </dd>
<dt><i>pginodesteal</i> (since linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>slabs_scanned</i> (since linux 2.6.5) </dt>
<dd>   </dd>
<dt><i>kswapd_inodesteal</i> (since linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>kswapd_low_wmark_hit_quickly</i> (since 2.6.33) </dt>
<dd>   </dd>
<dt><i>kswapd_high_wmark_hit_quickly</i> (since 2.6.33) </dt>
<dd>   </dd>
<dt><i>pageoutrun</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>allocstall</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>pgrotated</i> (since Linux 2.6.0) </dt>
<dd>   </dd>
<dt><i>drop_pagecache</i> (since Linux 3.15) </dt>
<dd>   </dd>
<dt><i>drop_slab</i> (since Linux 3.15) </dt>
<dd>   </dd>
<dt><i>numa_pte_updates</i> (since Linux 3.8) </dt>
<dd>   </dd>
<dt><i>numa_huge_pte_updates</i> (since Linux 3.13) </dt>
<dd>   </dd>
<dt><i>numa_hint_faults</i> (since Linux 3.8) </dt>
<dd>   </dd>
<dt><i>numa_hint_faults_local</i> (since Linux 3.8) </dt>
<dd>   </dd>
<dt><i>numa_pages_migrated</i> (since Linux 3.8) </dt>
<dd>   </dd>
<dt><i>pgmigrate_success</i> (since Linux 3.8) </dt>
<dd>   </dd>
<dt><i>pgmigrate_fail</i> (since Linux 3.8) </dt>
<dd>   </dd>
<dt><i>compact_migrate_scanned</i> (since Linux 3.8) </dt>
<dd>   </dd>
<dt><i>compact_free_scanned</i> (since Linux 3.8) </dt>
<dd>   </dd>
<dt><i>compact_isolated</i> (since Linux 3.8) </dt>
<dd>   </dd>
<dt><i>compact_stall</i> (since Linux 2.6.35) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>compact_fail</i> (since Linux 2.6.35) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>compact_success</i> (since Linux 2.6.35) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>htlb_buddy_alloc_success</i> (since Linux 2.6.26) </dt>
<dd>   </dd>
<dt><i>htlb_buddy_alloc_fail</i> (since Linux 2.6.26) </dt>
<dd>   </dd>
<dt><i>unevictable_pgs_culled</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>unevictable_pgs_scanned</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>unevictable_pgs_rescued</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>unevictable_pgs_mlocked</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>unevictable_pgs_munlocked</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>unevictable_pgs_cleared</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>unevictable_pgs_stranded</i> (since Linux 2.6.28) </dt>
<dd>   </dd>
<dt><i>thp_fault_alloc</i> (since Linux 2.6.39) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>thp_fault_fallback</i> (since Linux 2.6.39) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>thp_collapse_alloc</i> (since Linux 2.6.39) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>thp_collapse_alloc_failed</i> (since Linux 2.6.39) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>thp_split</i> (since Linux 2.6.39) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>thp_zero_page_alloc</i> (since Linux 3.8) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>thp_zero_page_alloc_failed</i> (since Linux 3.8) </dt>
<dd>  See the kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i>.  </dd>
<dt><i>balloon_inflate</i> (since Linux 3.18) </dt>
<dd>   </dd>
<dt><i>balloon_deflate</i> (since Linux 3.18) </dt>
<dd>   </dd>
<dt><i>balloon_migrate</i> (since Linux 3.18) </dt>
<dd>   </dd>
<dt><i>nr_tlb_remote_flush</i> (since Linux 3.12) </dt>
<dd>   </dd>
<dt><i>nr_tlb_remote_flush_received</i> (since Linux 3.12) </dt>
<dd>   </dd>
<dt><i>nr_tlb_local_flush_all</i> (since Linux 3.12) </dt>
<dd>   </dd>
<dt><i>nr_tlb_local_flush_one</i> (since Linux 3.12) </dt>
<dd>   </dd>
<dt><i>vmacache_find_calls</i> (since Linux 3.16) </dt>
<dd>   </dd>
<dt><i>vmacache_find_hits</i> (since Linux 3.16) </dt>
<dd>   </dd>
<dt><i>vmacache_full_flushes</i> (since Linux 3.19) </dt>
<dd>   </dd></dl>
 </dl>
 <dt><i>/proc/zoneinfo</i> (since Linux 2.6.13) </dt>
<dd>  This file displays information about memory zones. This is useful for analyzing virtual memory behavior.  </dd></dl>
  <h2>NOTES</h2>
 Many files contain strings (e.g., the environment and command line) that are in the internal format, with subfields terminated by null bytes (&#8216;\0&#8217;). When inspecting such files, you may find that the results are more readable if you use a command of the following form to display them: <h2>SEE ALSO</h2>
 <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1), <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1), <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-free/">free</a></code>(1), <code><a href="/docs/linux/man/1-htop/">htop</a></code>(1), <code><a href="/docs/linux/man/1-init/">init</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-pstree/">pstree</a></code>(1), <code><a href="/docs/linux/man/1-tr/">tr</a></code>(1), <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1), <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2), <code><a href="/docs/linux/man/5-slabinfo/">slabinfo</a></code>(5), <code><a href="/docs/linux/man/5-sysfs/">sysfs</a></code>(5), <code><a href="/docs/linux/man/7-hier/">hier</a></code>(7), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7), <code><a href="/docs/linux/man/8-arp/">arp</a></code>(8), <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-lsmod/">lsmod</a></code>(8), <code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8), <code><a href="/docs/linux/man/8-procinfo/">procinfo</a></code>(8), <code><a href="/docs/linux/man/8-route/">route</a></code>(8), <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8) <h2>COLOPHON</h2>
 This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> <h2>Index</h2>
