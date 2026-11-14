---
title: "kcmp(2)"
name: "kcmp"
section: "2"
letter: "k"
url: "/docs/linux/man/2-kcmp/"
description: "kcmp – compare two processes to determine if they share a kernel resource"
---

<h2 class="name">NAME</h2>
<p> kcmp &#8211; compare two processes to determine if they share a kernel resource </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/kcmp.h&gt;
int kcmp(pid_t pid1, pid_t pid2, int type,
         unsigned long idx1, unsigned long idx2);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>kcmp</code>() system call can be used to check whether the two processes identified by <i>pid1</i> and <i>pid2</i> share a kernel resource such as virtual memory, file descriptors, and so on. </p>
<p> Permission to employ <code>kcmp</code>() is governed by ptrace access mode <code>PTRACE_MODE_READ_REALCREDS</code> checks against both <i>pid1</i> and <i>pid2</i>; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2). </p>
<p> The <i>type</i> argument specifies which resource is to be compared in the two processes. It has one of the following values:</p>
<dl>
<dt><code>KCMP_FILE</code></p>
<dd> Check whether a file descriptor <i>idx1</i> in the process <i>pid1</i> refers to the same open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) as file descriptor <i>idx2</i> in the process <i>pid2</i>. The existence of two file descriptors that refer to the same open file description can occur as a result of <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2) (and similar) <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), or passing file descriptors via a domain socket (see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)).</p>
<dt><code>KCMP_FILES</code></p>
<dd> Check whether the processes share the same set of open file descriptors. The arguments <i>idx1</i> and <i>idx2</i> are ignored. See the discussion of the <code>CLONE_FILES</code> flag in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<dt><code>KCMP_FS</code></p>
<dd> Check whether the processes share the same filesystem information (i.e., file mode creation mask, working directory, and filesystem root). The arguments <i>idx1</i> and <i>idx2</i> are ignored. See the discussion of the <code>CLONE_FS</code> flag in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<dt><code>KCMP_IO</code></p>
<dd> Check whether the processes share I/O context. The arguments <i>idx1</i> and <i>idx2</i> are ignored. See the discussion of the <code>CLONE_IO</code> flag in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<dt><code>KCMP_SIGHAND</code></p>
<dd> Check whether the processes share the same table of signal dispositions. The arguments <i>idx1</i> and <i>idx2</i> are ignored. See the discussion of the <code>CLONE_SIGHAND</code> flag in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<dt><code>KCMP_SYSVSEM</code></p>
<dd> Check whether the processes share the same list of System V semaphore undo operations. The arguments <i>idx1</i> and <i>idx2</i> are ignored. See the discussion of the <code>CLONE_SYSVSEM</code> flag in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<dt><code>KCMP_VM</code></p>
<dd> Check whether the processes share the same address space. The arguments <i>idx1</i> and <i>idx2</i> are ignored. See the discussion of the <code>CLONE_VM</code> flag in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<dt><code>KCMP_EPOLL_TFD</code> (since Linux 4.13)</p>
<dd> Check whether the file descriptor <i>idx1</i> of the process <i>pid1</i> is present in the <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) instance described by <i>idx2</i> of the process <i>pid2</i>. The argument <i>idx2</i> is a pointer to a structure where the target file is described. This structure has the form:</dl>
<p> struct kcmp_epoll_slot {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 efd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 tfd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 toff; }; </p>
<p> Within this structure, <i>efd</i> is an epoll file descriptor returned from <code><a href="/docs/linux/man/2-epoll_create/">epoll_create</a></code>(2), <i>tfd</i> is a target file descriptor number, and <i>toff</i> is a target file offset counted from zero. Several different targets may be registered with the same file descriptor number and setting a specific offset helps to investigate each of them. </p>
<p> Note the <code>kcmp</code>() is not protected against false positives which may occur if the processes are currently running. One should stop the processes by sending <code>SIGSTOP</code> (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)) prior to inspection with this system call to obtain meaningful results.</p>
<h2>RETURN VALUE</h2>
<p> The return value of a successful call to <code>kcmp</code>() is simply the result of arithmetic comparison of kernel pointers (when the kernel compares resources, it uses their memory addresses). </p>
<p> The easiest way to explain is to consider an example. Suppose that <i>v1</i> and <i>v2</i> are the addresses of appropriate resources, then the return value is one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> <i>v1</i> is equal to <i>v2</i>; in other words, the two processes share the resource.</p>
<dt>1</p>
<dd> <i>v1</i> is less than <i>v2</i>.</p>
<dt>2</p>
<dd> <i>v1</i> is greater than <i>v2</i>.</p>
<dt>3</p>
<dd> <i>v1</i> is not equal to <i>v2</i>, but ordering information is unavailable.</dl>
</dl>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> <code>kcmp</code>() was designed to return values suitable for sorting. This is particularly handy if one needs to compare a large number of file descriptors.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>type</i> is <code>KCMP_FILE</code> and <i>fd1</i> or <i>fd2</i> is not an open file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> The epoll slot addressed by <i>idx2</i> is outside of the user&#8217;s address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>type</i> is invalid.</p>
<dt><code>ENOENT</code></p>
<dd> The target file is not present in <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) instance.</p>
<dt><code>EPERM</code></p>
<dd> Insufficient permission to inspect process resources. The <code>CAP_SYS_PTRACE</code> capability is required to inspect processes that you do not own. Other ptrace limitations may also apply, such as <code>CONFIG_SECURITY_YAMA</code>, which, when <i>/proc/sys/kernel/yama/ptrace_scope</i> is 2, limits <code>kcmp</code>() to child processes; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2).</p>
<dt><code>ESRCH</code></p>
<dd> Process <i>pid1</i> or <i>pid2</i> does not exist.</dl>
<h2>VERSIONS</h2>
<p> The <code>kcmp</code>() system call first appeared in Linux 3.5.</p>
<h2>CONFORMING TO</h2>
<p> <code>kcmp</code>() is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> This system call is available only if the kernel was configured with <code>CONFIG_CHECKPOINT_RESTORE</code>. The main use of the system call is for the checkpoint/restore in user space (CRIU) feature. The alternative to this system call would have been to expose suitable process information via the <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) filesystem; this was deemed to be unsuitable for security reasons. </p>
<p> See <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) for some background information on the shared resources referred to on this page.</p>
<h2>EXAMPLES</h2>
<p> The program below uses <code>kcmp</code>() to test whether pairs of file descriptors refer to the same open file description. The program tests different cases for the file descriptor pairs, as described in the program output. An example run of the program is as follows: </p>
<p> $ <code>./a.out</code> Parent PID is 1144 Parent opened file on FD 3 </p>
<p> PID of child of fork() is 1145 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Compare duplicate FDs from different processes:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>kcmp(1145, 1144, KCMP_FILE, 3, 3) ==&gt; same<br />
 Child opened file on FD 4 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Compare FDs from distinct open()s in same process:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>kcmp(1145, 1145, KCMP_FILE, 3, 4) ==&gt; different<br />
 Child duplicated FD 3 to create FD 5 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Compare duplicated FDs in same process:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>kcmp(1145, 1145, KCMP_FILE, 3, 5) ==&gt; same</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;sys/syscall.h&gt; #include &lt;sys/wait.h&gt; #include &lt;sys/stat.h&gt; #include &lt;stdint.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;unistd.h&gt; #include &lt;fcntl.h&gt; #include &lt;linux/kcmp.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static int kcmp(pid_t pid1, pid_t pid2, int type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long idx1, unsigned long idx2) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return syscall(SYS_kcmp, pid1, pid2, type, idx1, idx2); } </p>
<p> static void test_kcmp(char *msg, pid_t pid1, pid_t pid2, int fd_a, int fd_b) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;	%s
&quot;, msg);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;		kcmp(%jd,&nbsp;%jd, KCMP_FILE,&nbsp;%d,&nbsp;%d)&nbsp;==&gt;&nbsp;%s
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;pid1,&nbsp;(intmax_t)&nbsp;pid2, fd_a, fd_b,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(kcmp(pid1, pid2, KCMP_FILE, fd_a, fd_b)&nbsp;==&nbsp;0)&nbsp;?<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;same&quot;&nbsp;:&nbsp;&quot;different&quot;); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd1, fd2, fd3;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char pathname[]&nbsp;=&nbsp;&quot;/tmp/kcmp.test&quot;; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd1&nbsp;=&nbsp;open(pathname, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd1&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;open&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Parent PID is&nbsp;%jd
&quot;,&nbsp;(intmax_t)&nbsp;getpid());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Parent opened file on FD&nbsp;%d

&quot;, fd1); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(fork())&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case -1:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;fork&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case 0:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;PID of child of fork()&nbsp;is&nbsp;%jd
&quot;,&nbsp;(intmax_t)&nbsp;getpid()); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;test_kcmp(&quot;Compare duplicate FDs from different processes:&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;getpid(), getppid(), fd1, fd1); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd2&nbsp;=&nbsp;open(pathname, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd2&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;open&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Child opened file on FD&nbsp;%d
&quot;, fd2); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;test_kcmp(&quot;Compare FDs from distinct open()s in same process:&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;getpid(), getpid(), fd1, fd2); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd3&nbsp;=&nbsp;dup(fd1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd3&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;dup&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Child duplicated FD&nbsp;%d to create FD&nbsp;%d
&quot;, fd1, fd3); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;test_kcmp(&quot;Compare duplicated FDs in same process:&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;getpid(), getpid(), fd1, fd3);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wait(NULL);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
