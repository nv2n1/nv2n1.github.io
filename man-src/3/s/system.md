---
title: "system(3)"
name: "system"
section: "3"
letter: "s"
url: "/docs/linux/man/3-system/"
description: "system – execute a shell command"
---

<p>system &#8211; execute a shell command</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

int system(const char *command);</code></pre>
<h2>Description</h2>
<p>The <code>system</code>() library function uses <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) to create a child process that executes the shell command specified in <i>command</i> using <code><a href="/docs/linux/man/3-execl/">execl</a></code>(3) as follows: </p>
<p> execl(&quot;/bin/sh&quot;, &quot;sh&quot;, &quot;-c&quot;, command, (char *) NULL); </p>
<p> <code>system</code>() returns after the command has been completed. </p>
<p> During execution of the command, <code>SIGCHLD</code> will be blocked, and <code>SIGINT</code> and <code>SIGQUIT</code> will be ignored, in the process that calls <code>system</code>(). (These signals will be handled according to their defaults inside the child process that executes <i>command</i>.) </p>
<p> If <i>command</i> is NULL, then <code>system</code>() returns a status indicating whether a shell is available on the system.</p>
<h2>Return Value</h2>
<p>The return value of <code>system</code>() is one of the following:</p>
<dl>
<dt>*</p>
<dd>If <i>command</i> is NULL, then a nonzero value if a shell is available, or 0 if no shell is available.</p>
<dt>*</p>
<dd>If a child process could not be created, or its status could not be retrieved, the return value is -1 and <i>errno</i> is set to indicate the error.</p>
<dt>*</p>
<dd>If a shell could not be executed in the child process, then the return value is as though the child shell terminated by calling <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) with the status 127.</p>
<dt>*</p>
<dd>If all system calls succeed, then the return value is the termination status of the child shell used to execute <i>command</i>. (The termination status of a shell is the termination status of the last command it executes.)</dl>
<p> In the last two cases, the return value is a &quot;wait status&quot; that can be examined using the macros described in <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2). (i.e., <code>WIFEXITED</code>(), <code>WEXITSTATUS</code>(), and so on). </p>
<p> <code>system</code>() does not affect the wait status of any other children.</p>
<h2>Errors</h2>
<p><code>system</code>() can fail with any of the same errors as <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2).</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>system</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C89, C99.</p>
<h2>Notes</h2>
<p><code>system</code>() provides simplicity and convenience: it handles all of the details of calling <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/3-execl/">execl</a></code>(3), and <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2), as well as the necessary manipulations of signals; in addition, the shell performs the usual substitutions and I/O redirections for <i>command</i>. The main cost of <code>system</code>() is inefficiency: additional system calls are required to create the process that runs the shell and to execute the shell. If the <code>_XOPEN_SOURCE</code> feature test macro is defined (before including <i>any</i> header files), then the macros described in <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) (<code>WEXITSTATUS</code>(), etc.) are made available when including <i>&lt;stdlib.h&gt;</i>. As mentioned, <code>system</code>() ignores <code>SIGINT</code> and <code>SIGQUIT</code>. This may make programs that call it from a loop uninterruptible, unless they take care themselves to check the exit status of the child. For example: </p>
<pre><code>while (something) {
    int ret = system(&quot;foo&quot;);
    if (WIFSIGNALED(ret) &amp;&amp;
        (WTERMSIG(ret) == SIGINT || WTERMSIG(ret) == SIGQUIT))
        break;
}</code></pre>
<p> According to POSIX.1, it is unspecified whether handlers registered using <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3) are called during the execution of <code>system</code>(). In the glibc implementation, such handlers are not called. In versions of glibc before 2.1.3, the check for the availability of <i>/bin/sh</i> was not actually performed if <i>command</i> was NULL; instead it was always assumed to be available, and <code>system</code>() always returned 1 in this case. Since glibc 2.1.3, this check is performed because, even though POSIX.1-2001 requires a conforming implementation to provide a shell, that shell may not be available or executable if the calling program has previously called <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) (which is not specified by POSIX.1-2001). It is possible for the shell command to terminate with a status of 127, which yields a <code>system</code>() return value that is indistinguishable from the case where a shell could not be executed in the child process.</p>
<h3>Caveats</h3>
<p>Do not use <code>system</code>() from a privileged program (a set-user-ID or set-group-ID program, or a program with capabilities) because strange values for some environment variables might be used to subvert system integrity. For example, <code>PATH</code> could be manipulated so that an arbitrary program is executed with privilege. Use the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) family of functions instead, but not <code><a href="/docs/linux/man/3-execlp/">execlp</a></code>(3) or <code><a href="/docs/linux/man/3-execvp/">execvp</a></code>(3) (which also use the <code>PATH</code> environment variable to search for an executable). <code>system</code>() will not, in fact, work properly from programs with set-user-ID or set-group-ID privileges on systems on which <i>/bin/sh</i> is bash version 2: as a security measure, bash 2 drops privileges on startup. (Debian uses a different shell, <code><a href="/docs/linux/man/1-dash/">dash</a></code>(1), which does not do this when invoked as <code>sh</code>.) Any user input that is employed as part of <i>command</i> should be <i>carefully</i> sanitized, to ensure that unexpected shell commands or command options are not executed. Such risks are especially grave when using <code>system</code>() from a privileged program.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
