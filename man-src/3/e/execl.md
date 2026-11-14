---
title: "execl(3)"
name: "execl"
section: "3"
letter: "e"
url: "/docs/linux/man/3-execl/"
description: "execl, execlp, execle, execv, execvp, execvpe – execute a file"
---

<h2 class="name">NAME</h2>
<p> execl, execlp, execle, execv, execvp, execvpe &#8211; execute a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
extern char **environ;
int execl(const char *pathname, const char *arg, ...
          /* (char  *) NULL */);
int execlp(const char *file, const char *arg, ...
           /* (char  *) NULL */);
int execle(const char *pathname, const char *arg, ...
           /*, (char *) NULL, char *const envp[] */);
int execv(const char *pathname, char *const argv[]);
int execvp(const char *file, char *const argv[]);
int execvpe(const char *file, char *const argv[],
            char *const envp[]);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>execvpe</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>exec</code>() family of functions replaces the current process image with a new process image. The functions described in this manual page are layered on top of <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). (See the manual page for <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) for further details about the replacement of the current process image.) </p>
<p> The initial argument for these functions is the name of a file that is to be executed. </p>
<p> The functions can be grouped based on the letters following the &quot;exec&quot; prefix.</p>
<h3>l &#8211; execl(), execlp(), execle()</h3>
<p> The <i>const char&nbsp;*arg</i> and subsequent ellipses can be thought of as <i>arg0</i>, <i>arg1</i>, &#8230;, <i>argn</i>. Together they describe a list of one or more pointers to null-terminated strings that represent the argument list available to the executed program. The first argument, by convention, should point to the filename associated with the file being executed. The list of arguments <i>must</i> be terminated by a null pointer, and, since these are variadic functions, this pointer must be cast <i>(char&nbsp;*) NULL</i>. </p>
<p> By contrast with the &#8216;l&#8217; functions, the &#8216;v&#8217; functions (below) specify the command-line arguments of the executed program as a vector.</p>
<h3>v &#8211; execv(), execvp(), execvpe()</h3>
<p> The <i>char&nbsp;*const argv[]</i> argument is an array of pointers to null-terminated strings that represent the argument list available to the new program. The first argument, by convention, should point to the filename associated with the file being executed. The array of pointers <i>must</i> be terminated by a null pointer.</p>
<h3>e &#8211; execle(), execvpe()</h3>
<p> The environment of the caller is specified via the argument <i>envp</i>. The <i>envp</i> argument is an array of pointers to null-terminated strings and <i>must</i> be terminated by a null pointer. </p>
<p> All other <code>exec</code>() functions (which do not include &#8216;e&#8217; in the suffix) take the environment for the new process image from the external variable <i>environ</i> in the calling process.</p>
<h3>p &#8211; execlp(), execvp(), execvpe()</h3>
<p> These functions duplicate the actions of the shell in searching for an executable file if the specified filename does not contain a slash (/) character. The file is sought in the colon-separated list of directory pathnames specified in the <code>PATH</code> environment variable. If this variable isn&#8217;t defined, the path list defaults to a list that includes the directories returned by <i>confstr(_CS_PATH)</i> (which typically returns the value &quot;/bin:/usr/bin&quot;) and possibly also the current working directory; see NOTES for further details. </p>
<p> If the specified filename includes a slash character, then <code>PATH</code> is ignored, and the file at the specified pathname is executed. </p>
<p> In addition, certain errors are treated specially. </p>
<p> If permission is denied for a file (the attempted <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) failed with the error <code>EACCES</code>), these functions will continue searching the rest of the search path. If no other file is found, however, they will return with <i>errno</i> set to <code>EACCES</code>. </p>
<p> If the header of a file isn&#8217;t recognized (the attempted <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) failed with the error <code>ENOEXEC</code>), these functions will execute the shell (<i>/bin/sh</i>) with the path of the file as its first argument. (If this attempt fails, no further searching is done.) </p>
<p> All other <code>exec</code>() functions (which do not include &#8216;p&#8217; in the suffix) take as their first argument a (relative or absolute) pathname that identifies the program to be executed.</p>
<h2>RETURN VALUE</h2>
<p> The <code>exec</code>() functions return only if an error has occurred. The return value is -1, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> All of these functions may fail and set <i>errno</i> for any of the errors specified for <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h2>VERSIONS</h2>
<p> The <code>execvpe</code>() function first appeared in glibc 2.11.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>execl</code>(), <code>execle</code>(), <code>execv</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>execlp</code>(), <code>execvp</code>(), <code>execvpe</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008. </p>
<p> The <code>execvpe</code>() function is a GNU extension.</p>
<h2>NOTES</h2>
<p> The default search path (used when the environment does not contain the variable <code>PATH</code>) shows some variation across systems. It generally includes <i>/bin</i> and <i>/usr/bin</i> (in that order) and may also include the current working directory. On some other systems, the current working is included after <i>/bin</i> and <i>/usr/bin</i>, as an anti-Trojan-horse measure. The glibc implementation long followed the traditional default where the current working directory is included at the start of the search path. However, some code refactoring during the development of glibc 2.24 caused the current working directory to be dropped altogether from the default search path. This accidental behavior change is considered mildly beneficial, and won&#8217;t be reverted. </p>
<p> The behavior of <code>execlp</code>() and <code>execvp</code>() when errors occur while attempting to execute the file is historic practice, but has not traditionally been documented and is not specified by the POSIX standard. BSD (and possibly other systems) do an automatic sleep and retry if <code>ETXTBSY</code> is encountered. Linux treats it as a hard error and returns immediately. </p>
<p> Traditionally, the functions <code>execlp</code>() and <code>execvp</code>() ignored all errors except for the ones described above and <code>ENOMEM</code> and <code>E2BIG</code>, upon which they returned. They now return if any error other than the ones described above occurs.</p>
<h2>BUGS</h2>
<p> Before glibc 2.24, <code>execl</code>() and <code>execle</code>() employed <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3) internally and were consequently not async-signal-safe, in violation of the requirements of POSIX.1. This was fixed in glibc 2.24.</p>
<h3>Architecture-specific details</h3>
<p> On sparc and sparc64, <code>execv</code>() is provided as a system call by the kernel (with the prototype shown above) for compatibility with SunOS. This function is <i>not</i> employed by the <code>execv</code>() wrapper function on those architectures.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-execveat/">execveat</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2), <code><a href="/docs/linux/man/3-fexecve/">fexecve</a></code>(3), <code><a href="/docs/linux/man/3-system/">system</a></code>(3), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
