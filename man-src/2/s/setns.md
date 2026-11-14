---
title: "setns(2)"
name: "setns"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setns/"
description: "setns – reassociate thread with a namespace"
---

<h2 class="name">NAME</h2>
<p> setns &#8211; reassociate thread with a namespace </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sched.h&gt;
int setns(int fd, int nstype);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>setns</code>() system call allows the calling thread to move into different namespaces. The <i>fd</i> argument is one of the following:</p>
<dl>
<dt>&bull;</p>
<dd> a file descriptor referring to one of the magic links in a <i>/proc/[pid]/ns/</i> directory (or a bind mount to such a link);</p>
<dt>&bull;</p>
<dd> a PID file descriptor (see <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2)).</dl>
<p> The <i>nstype</i> argument is interpreted differently in each case.</p>
<h3>fd refers to a /proc/[pid]/ns/ link</h3>
<p> If <i>fd</i> refers to a <i>/proc/[pid]/ns/</i> link, then <code>setns</code>() reassociates the calling thread with the namespace associated with that link, subject to any constraints imposed by the <i>nstype</i> argument. In this usage, each call to <code>setns</code>() changes just one of the caller&#8217;s namespace memberships. </p>
<p> The <i>nstype</i> argument specifies which type of namespace the calling thread may be reassociated with. This argument can have <i>one</i> of the following values:</p>
<dl>
<dt><code>0</code></p>
<dd> Allow any type of namespace to be joined.</p>
<dt><code>CLONE_NEWCGROUP</code> (since Linux 4.6)</p>
<dd> <i>fd</i> must refer to a cgroup namespace.</p>
<dt><code>CLONE_NEWIPC</code> (since Linux 3.0)</p>
<dd> <i>fd</i> must refer to an IPC namespace.</p>
<dt><code>CLONE_NEWNET</code> (since Linux 3.0)</p>
<dd> <i>fd</i> must refer to a network namespace.</p>
<dt><code>CLONE_NEWNS</code> (since Linux 3.8)</p>
<dd> <i>fd</i> must refer to a mount namespace.</p>
<dt><code>CLONE_NEWPID</code> (since Linux 3.8)</p>
<dd> <i>fd</i> must refer to a descendant PID namespace.</p>
<dt><code>CLONE_NEWTIME</code> (since Linux 5.8)</p>
<dd> <i>fd</i> must refer to a time namespace.</p>
<dt><code>CLONE_NEWUSER</code> (since Linux 3.8)</p>
<dd> <i>fd</i> must refer to a user namespace.</p>
<dt><code>CLONE_NEWUTS</code> (since Linux 3.0)</p>
<dd> <i>fd</i> must refer to a UTS namespace.</dl>
<p> Specifying <i>nstype</i> as 0 suffices if the caller knows (or does not care) what type of namespace is referred to by <i>fd</i>. Specifying a nonzero value for <i>nstype</i> is useful if the caller does not know what type of namespace is referred to by <i>fd</i> and wants to ensure that the namespace is of a particular type. (The caller might not know the type of the namespace referred to by <i>fd</i> if the file descriptor was opened by another process and, for example, passed to the caller via a UNIX domain socket.)</p>
<h3>fd is a PID file descriptor</h3>
<p> Since Linux 5.8, <i>fd</i> may refer to a PID file descriptor obtained from <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2) or <code><a href="/docs/linux/man/3-clone/">clone</a></code>(3). In this usage, <code>setns</code>() atomically moves the calling thread into one or more of the same namespaces as the thread referred to by <i>fd</i>. </p>
<p> The <i>nstype</i> argument is a bit mask specified by ORing together <i>one or more</i> of the <code>CLONE_NEW*</code> namespace constants listed above. The caller is moved into each of the target thread&#8217;s namespaces that is specified in <i>nstype</i>; the caller&#8217;s memberships in the remaining namespaces are left unchanged. </p>
<p> For example, the following code would move the caller into the same user, network, and UTS namespaces as PID 1234, but would leave the caller&#8217;s other namespace memberships unchanged: </p>
<p> int fd = pidfd_open(1234, 0); setns(fd, CLONE_NEWUSER | CLONE_NEWNET | CLONE_NEWUTS);</p>
<h3>Details for specific namespace types</h3>
<p> Note the following details and restrictions when reassociating with specific namespace types:</p>
<dl>
<dt>User namespaces</p>
<dd> A process reassociating itself with a user namespace must have the <code>CAP_SYS_ADMIN</code> capability in the target user namespace. (This necessarily implies that it is only possible to join a descendant user namespace.) Upon successfully joining a user namespace, a process is granted all capabilities in that namespace, regardless of its user and group IDs.</p>
<dt>
<dd> A multithreaded process may not change user namespace with <code>setns</code>().</p>
<dt>
<dd> It is not permitted to use <code>setns</code>() to reenter the caller&#8217;s current user namespace. This prevents a caller that has dropped capabilities from regaining those capabilities via a call to <code>setns</code>().</p>
<dt>
<dd> For security reasons, a process can&#8217;t join a new user namespace if it is sharing filesystem-related attributes (the attributes whose sharing is controlled by the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_FS</code> flag) with another process.</p>
<dt>
<dd> For further details on user namespaces, see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</p>
<dt>Mount namespaces</p>
<dd> Changing the mount namespace requires that the caller possess both <code>CAP_SYS_CHROOT</code> and <code>CAP_SYS_ADMIN</code> capabilities in its own user namespace and <code>CAP_SYS_ADMIN</code> in the user namespace that owns the target mount namespace.</p>
<dt>
<dd> A process can&#8217;t join a new mount namespace if it is sharing filesystem-related attributes (the attributes whose sharing is controlled by the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_FS</code> flag) with another process.</p>
<dt>
<dd> See <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7) for details on the interaction of user namespaces and mount namespaces.</p>
<dt>PID namespaces</p>
<dd> In order to reassociate itself with a new PID namespace, the caller must have the <code>CAP_SYS_ADMIN</code> capability both in its own user namespace and in the user namespace that owns the target PID namespace.</p>
<dt>
<dd> Reassociating the PID namespace has somewhat different from other namespace types. Reassociating the calling thread with a PID namespace changes only the PID namespace that subsequently created child processes of the caller will be placed in; it does not change the PID namespace of the caller itself.</p>
<dt>
<dd> Reassociating with a PID namespace is allowed only if the target PID namespace is a descendant (child, grandchild, etc.) of, or is the same as, the current PID namespace of the caller.</p>
<dt>
<dd> For further details on PID namespaces, see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7).</p>
<dt>Cgroup namespaces</p>
<dd> In order to reassociate itself with a new cgroup namespace, the caller must have the <code>CAP_SYS_ADMIN</code> capability both in its own user namespace and in the user namespace that owns the target cgroup namespace.</p>
<dt>
<dd> Using <code>setns</code>() to change the caller&#8217;s cgroup namespace does not change the caller&#8217;s cgroup memberships.</p>
<dt>Network, IPC, time, and UTS namespaces</p>
<dd> In order to reassociate itself with a new network, IPC, time, or UTS namespace, the caller must have the <code>CAP_SYS_ADMIN</code> capability both in its own user namespace and in the user namespace that owns the target namespace.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>setns</code>() returns 0. On failure, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> refers to a namespace whose type does not match that specified in <i>nstype</i>.</p>
<dt><code>EINVAL</code></p>
<dd> There is problem with reassociating the thread with the specified namespace.</p>
<dt>
<dd> <code>EINVAL</code> The caller tried to join an ancestor (parent, grandparent, and so on) PID namespace.</p>
<dt><code>EINVAL</code></p>
<dd> The caller attempted to join the user namespace in which it is already a member.</p>
<dt><code>EINVAL</code></p>
<dd> The caller shares filesystem (<code>CLONE_FS</code>) state (in particular, the root directory) with other processes and tried to join a new user namespace.</p>
<dt><code>EINVAL</code></p>
<dd> The caller is multithreaded and tried to join a new user namespace.</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> is a PID file descriptor and <i>nstype</i> is invalid (e.g., it is 0).</p>
<dt><code>ENOMEM</code></p>
<dd> Cannot allocate sufficient memory to change the specified namespace.</p>
<dt><code>EPERM</code></p>
<dd> The calling thread did not have the required capability for this operation.</p>
<dt><code>ESRCH</code></p>
<dd> <i>fd</i> is a PID file descriptor but the process it refers to no longer exists (i.e., it has terminated and been waited on).</dl>
<h2>VERSIONS</h2>
<p> The <code>setns</code>() system call first appeared in Linux in kernel 3.0; library support was added to glibc in version 2.14.</p>
<h2>CONFORMING TO</h2>
<p> The <code>setns</code>() system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> For further information on the <i>/proc/[pid]/ns/</i> magic links, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7). </p>
<p> Not all of the attributes that can be shared when a new thread is created using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) can be changed using <code>setns</code>().</p>
<h2>EXAMPLES</h2>
<p> The program below takes two or more arguments. The first argument specifies the pathname of a namespace file in an existing <i>/proc/[pid]/ns/</i> directory. The remaining arguments specify a command and its arguments. The program opens the namespace file, joins that namespace using <code>setns</code>(), and executes the specified command inside that namespace. </p>
<p> The following shell session demonstrates the use of this program (compiled as a binary named <i>ns_exec</i>) in conjunction with the <code>CLONE_NEWUTS</code> example program in the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) man page (complied as a binary named <i>newuts</i>). </p>
<p> We begin by executing the example program in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) in the background. That program creates a child in a separate UTS namespace. The child changes the hostname in its namespace, and then both processes display the hostnames in their UTS namespaces, so that we can see that they are different. </p>
<p> $ <code>su</code> # Need privilege for namespace operations Password: # <code>./newuts bizarro &amp;</code> [1] 3549 clone() returned 3550 uts.nodename in child: bizarro uts.nodename in parent: antero # <code>uname -n</code> # Verify hostname in the shell antero </p>
<p> We then run the program shown below, using it to execute a shell. Inside that shell, we verify that the hostname is the one set by the child created by the first program: </p>
<p> # <code>./ns_exec /proc/3550/ns/uts /bin/bash</code> # <code>uname -n</code> # Executed in shell started by ns_exec bizarro</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;fcntl.h&gt; #include &lt;sched.h&gt; #include &lt;unistd.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s&nbsp;/proc/PID/ns/FILE cmd args&#8230;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Get file descriptor for namespace;&nbsp;the file descriptor is opened<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;with O_CLOEXEC so as to ensure that it is not inherited by the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;program that is later executed.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(argv[1], O_RDONLY | O_CLOEXEC);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;open&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(setns(fd, 0)&nbsp;==&nbsp;-1)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Join that namespace&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;setns&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;execvp(argv[2],&nbsp;&amp;argv[2]);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Execute a command in namespace&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;execvp&quot;); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nsenter/">nsenter</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
