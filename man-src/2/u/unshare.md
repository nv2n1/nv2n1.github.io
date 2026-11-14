---
title: "unshare(2)"
name: "unshare"
section: "2"
letter: "u"
url: "/docs/linux/man/2-unshare/"
description: "unshare – disassociate parts of the process execution context"
---

<h2 class="name">NAME</h2>
<p> unshare &#8211; disassociate parts of the process execution context </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE
#include &lt;sched.h&gt;
int unshare(int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>unshare</code>() allows a process (or thread) to disassociate parts of its execution context that are currently being shared with other processes (or threads). Part of the execution context, such as the mount namespace, is shared implicitly when a new process is created using <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2), while other parts, such as virtual memory, may be shared by explicit request when creating a process or thread using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2). </p>
<p> The main use of <code>unshare</code>() is to allow a process to control its shared execution context without creating a new process. </p>
<p> The <i>flags</i> argument is a bit mask that specifies which parts of the execution context should be unshared. This argument is specified by ORing together zero or more of the following constants:</p>
<dl>
<dt><code>CLONE_FILES</code></p>
<dd> Reverse the effect of the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_FILES</code> flag. Unshare the file descriptor table, so that the calling process no longer shares its file descriptors with any other process.</p>
<dt><code>CLONE_FS</code></p>
<dd> Reverse the effect of the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_FS</code> flag. Unshare filesystem attributes, so that the calling process no longer shares its root directory (<code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2)), current directory (<code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2)), or umask (<code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)) attributes with any other process.</p>
<dt><code>CLONE_NEWCGROUP</code> (since Linux 4.6)</p>
<dd> This flag has the same effect as the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_NEWCGROUP</code> flag. Unshare the cgroup namespace. Use of <code>CLONE_NEWCGROUP</code> requires the <code>CAP_SYS_ADMIN</code> capability.</p>
<dt><code>CLONE_NEWIPC</code> (since Linux 2.6.19)</p>
<dd> This flag has the same effect as the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_NEWIPC</code> flag. Unshare the IPC namespace, so that the calling process has a private copy of the IPC namespace which is not shared with any other process. Specifying this flag automatically implies <code>CLONE_SYSVSEM</code> as well. Use of <code>CLONE_NEWIPC</code> requires the <code>CAP_SYS_ADMIN</code> capability.</p>
<dt><code>CLONE_NEWNET</code> (since Linux 2.6.24)</p>
<dd> This flag has the same effect as the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_NEWNET</code> flag. Unshare the network namespace, so that the calling process is moved into a new network namespace which is not shared with any previously existing process. Use of <code>CLONE_NEWNET</code> requires the <code>CAP_SYS_ADMIN</code> capability.</p>
<dt><code>CLONE_NEWNS</code></p>
<dd> This flag has the same effect as the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_NEWNS</code> flag. Unshare the mount namespace, so that the calling process has a private copy of its namespace which is not shared with any other process. Specifying this flag automatically implies <code>CLONE_FS</code> as well. Use of <code>CLONE_NEWNS</code> requires the <code>CAP_SYS_ADMIN</code> capability. For further information, see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7).</p>
<dt><code>CLONE_NEWPID</code> (since Linux 3.8)</p>
<dd> This flag has the same effect as the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_NEWPID</code> flag. Unshare the PID namespace, so that the calling process has a new PID namespace for its children which is not shared with any previously existing process. The calling process is <i>not</i> moved into the new namespace. The first child created by the calling process will have the process ID 1 and will assume the role of <code><a href="/docs/linux/man/1-init/">init</a></code>(1) in the new namespace. <code>CLONE_NEWPID</code> automatically implies <code>CLONE_THREAD</code> as well. Use of <code>CLONE_NEWPID</code> requires the <code>CAP_SYS_ADMIN</code> capability. For further information, see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7).</p>
<dt><code>CLONE_NEWTIME</code> (since Linux 5.6)</p>
<dd> Unshare the time namespace, so that the calling process has a new time namespace for its children which is not shared with any previously existing process. The calling process is <i>not</i> moved into the new namespace. Use of <code>CLONE_NEWTIME</code> requires the <code>CAP_SYS_ADMIN</code> capability. For further information, see <code><a href="/docs/linux/man/7-time_namespaces/">time_namespaces</a></code>(7).</p>
<dt><code>CLONE_NEWUSER</code> (since Linux 3.8)</p>
<dd> This flag has the same effect as the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_NEWUSER</code> flag. Unshare the user namespace, so that the calling process is moved into a new user namespace which is not shared with any previously existing process. As with the child process created by <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_NEWUSER</code> flag, the caller obtains a full set of capabilities in the new namespace.</p>
<dt>
<dd> <code>CLONE_NEWUSER</code> requires that the calling process is not threaded; specifying <code>CLONE_NEWUSER</code> automatically implies <code>CLONE_THREAD</code>. Since Linux 3.9, <code>CLONE_NEWUSER</code> also automatically implies <code>CLONE_FS</code>. <code>CLONE_NEWUSER</code> requires that the user ID and group ID of the calling process are mapped to user IDs and group IDs in the user namespace of the calling process at the time of the call.</p>
<dt>
<dd> For further information on user namespaces, see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</p>
<dt><code>CLONE_NEWUTS</code> (since Linux 2.6.19)</p>
<dd> This flag has the same effect as the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_NEWUTS</code> flag. Unshare the UTS IPC namespace, so that the calling process has a private copy of the UTS namespace which is not shared with any other process. Use of <code>CLONE_NEWUTS</code> requires the <code>CAP_SYS_ADMIN</code> capability.</p>
<dt><code>CLONE_SYSVSEM</code> (since Linux 2.6.26)</p>
<dd> This flag reverses the effect of the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_SYSVSEM</code> flag. Unshare System V semaphore adjustment (<i>semadj</i>) values, so that the calling process has a new empty <i>semadj</i> list that is not shared with any other process. If this is the last process that has a reference to the process&#8217;s current <i>semadj</i> list, then the adjustments in that list are applied to the corresponding semaphores, as described in <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2).</dl>
<p> In addition, <code>CLONE_THREAD</code>, <code>CLONE_SIGHAND</code>, and <code>CLONE_VM</code> can be specified in <i>flags</i> if the caller is single threaded (i.e., it is not sharing its address space with another process or thread). In this case, these flags have no effect. (Note also that specifying <code>CLONE_THREAD</code> automatically implies <code>CLONE_VM</code>, and specifying <code>CLONE_VM</code> automatically implies <code>CLONE_SIGHAND</code>.) If the process is multithreaded, then the use of these flags results in an error. </p>
<p> If <i>flags</i> is specified as zero, then <code>unshare</code>() is a no-op; no changes are made to the calling process&#8217;s execution context.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero returned. On failure, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> An invalid bit was specified in <i>flags</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_THREAD</code>, <code>CLONE_SIGHAND</code>, or <code>CLONE_VM</code> was specified in <i>flags</i>, and the caller is multithreaded.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWIPC</code> was specified in <i>flags</i>, but the kernel was not configured with the <code>CONFIG_SYSVIPC</code> and <code>CONFIG_IPC_NS</code> options.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWNET</code> was specified in <i>flags</i>, but the kernel was not configured with the <code>CONFIG_NET_NS</code> option.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWPID</code> was specified in <i>flags</i>, but the kernel was not configured with the <code>CONFIG_PID_NS</code> option.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWUSER</code> was specified in <i>flags</i>, but the kernel was not configured with the <code>CONFIG_USER_NS</code> option.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWUTS</code> was specified in <i>flags</i>, but the kernel was not configured with the <code>CONFIG_UTS_NS</code> option.</p>
<dt><code>EINVAL</code></p>
<dd> <code>CLONE_NEWPID</code> was specified in <i>flags</i>, but the process has previously called <code>unshare</code>() with the <code>CLONE_NEWPID</code> flag.</p>
<dt><code>ENOMEM</code></p>
<dd> Cannot allocate sufficient memory to copy parts of caller&#8217;s context that need to be unshared.</p>
<dt><code>ENOSPC</code> (since Linux 3.7)</p>
<dd> <code>CLONE_NEWPID</code> was specified in flags, but the limit on the nesting depth of PID namespaces would have been exceeded; see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7).</p>
<dt><code>ENOSPC</code> (since Linux 4.9; beforehand <code>EUSERS</code>)</p>
<dd> <code>CLONE_NEWUSER</code> was specified in <i>flags</i>, and the call would cause the limit on the number of nested user namespaces to be exceeded. See <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</p>
<dt>
<dd> From Linux 3.11 to Linux 4.8, the error diagnosed in this case was <code>EUSERS</code>.</p>
<dt><code>ENOSPC</code> (since Linux 4.9)</p>
<dd> One of the values in <i>flags</i> specified the creation of a new user namespace, but doing so would have caused the limit defined by the corresponding file in <i>/proc/sys/user</i> to be exceeded. For further details, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7).</p>
<dt><code>EPERM</code></p>
<dd> The calling process did not have the required privileges for this operation.</p>
<dt><code>EPERM</code></p>
<dd> <code>CLONE_NEWUSER</code> was specified in <i>flags</i>, but either the effective user ID or the effective group ID of the caller does not have a mapping in the parent namespace (see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)).</p>
<dt><code>EPERM</code> (since Linux 3.9)</p>
<dd> <code>CLONE_NEWUSER</code> was specified in <i>flags</i> and the caller is in a chroot environment (i.e., the caller&#8217;s root directory does not match the root directory of the mount namespace in which it resides).</p>
<dt><code>EUSERS</code> (from Linux 3.11 to Linux 4.8)</p>
<dd> <code>CLONE_NEWUSER</code> was specified in <i>flags</i>, and the limit on the number of nested user namespaces would be exceeded. See the discussion of the <code>ENOSPC</code> error above.</dl>
<h2>VERSIONS</h2>
<p> The <code>unshare</code>() system call was added to Linux in kernel 2.6.16.</p>
<h2>CONFORMING TO</h2>
<p> The <code>unshare</code>() system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> Not all of the process attributes that can be shared when a new process is created using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) can be unshared using <code>unshare</code>(). In particular, as at kernel 3.8, <code>unshare</code>() does not implement flags that reverse the effects of <code>CLONE_SIGHAND</code>, <code>CLONE_THREAD</code>, or <code>CLONE_VM</code>. Such functionality may be added in the future, if required.</p>
<h2>EXAMPLES</h2>
<p> The program below provides a simple implementation of the <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1) command, which unshares one or more namespaces and executes the command supplied in its command-line arguments. Here&#8217;s an example of the use of this program, running a shell in a new mount namespace, and verifying that the original shell and the new shell are in separate mount namespaces: </p>
<p> $ <code>readlink /proc/$$/ns/mnt</code> mnt:[4026531840] $ <code>sudo ./unshare -m /bin/bash</code> # <code>readlink /proc/$$/ns/mnt</code> mnt:[4026532325] </p>
<p> The differing output of the two <code><a href="/docs/linux/man/1-readlink/">readlink</a></code>(1) commands shows that the two shells are in different mount namespaces.</p>
<h3>Program source</h3>
<p> /* unshare.c </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A simple implementation of the&nbsp;<a href="/docs/linux/man/1-unshare/">unshare</a>(1)&nbsp;command: unshare<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;namespaces and execute a command. */ #define _GNU_SOURCE #include &lt;sched.h&gt; #include &lt;unistd.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; </p>
<p> /* A simple error-handling function: print an error message based<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;on the value in&nbsp;&#8216;errno&#8217;&nbsp;and terminate the calling process&nbsp;*/ </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static void usage(char *pname) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;[options]&nbsp;program&nbsp;[arg&#8230;]
&quot;, pname);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Options can be:
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-C&nbsp;<wbr>&nbsp;<wbr>&nbsp;unshare cgroup namespace
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-i&nbsp;<wbr>&nbsp;<wbr>&nbsp;unshare IPC namespace
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-m&nbsp;<wbr>&nbsp;<wbr>&nbsp;unshare mount namespace
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-n&nbsp;<wbr>&nbsp;<wbr>&nbsp;unshare network namespace
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-p&nbsp;<wbr>&nbsp;<wbr>&nbsp;unshare PID namespace
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-t&nbsp;<wbr>&nbsp;<wbr>&nbsp;unshare time namespace
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-u&nbsp;<wbr>&nbsp;<wbr>&nbsp;unshare UTS namespace
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-U&nbsp;<wbr>&nbsp;<wbr>&nbsp;unshare user namespace
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int flags, opt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;((opt&nbsp;=&nbsp;getopt(argc, argv,&nbsp;&quot;CimnptuU&quot;))&nbsp;!=&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(opt)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;C&#8217;: flags |=&nbsp;CLONE_NEWCGROUP;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;i&#8217;: flags |=&nbsp;CLONE_NEWIPC;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;m&#8217;: flags |=&nbsp;CLONE_NEWNS;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;n&#8217;: flags |=&nbsp;CLONE_NEWNET;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;p&#8217;: flags |=&nbsp;CLONE_NEWPID;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;t&#8217;: flags |=&nbsp;CLONE_NEWTIME;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;u&#8217;: flags |=&nbsp;CLONE_NEWUTS;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;U&#8217;: flags |=&nbsp;CLONE_NEWUSER;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:&nbsp;<wbr>&nbsp;usage(argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(optind&nbsp;&gt;=&nbsp;argc)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;usage(argv[0]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(unshare(flags)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;unshare&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;execvp(argv[optind],&nbsp;&amp;argv[optind]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;execvp&quot;); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7) </p>
<p> <i>Documentation/userspace-api/unshare.rst</i> in the Linux kernel source tree (or <i>Documentation/unshare.txt</i> before Linux 4.12)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
