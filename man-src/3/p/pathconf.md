---
title: "pathconf(3)"
name: "pathconf"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pathconf/"
description: "fpathconf, pathconf – get configuration values for files"
---

<p>fpathconf, pathconf &#8211; get configuration values for files</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unistd.h&gt;

long fpathconf(int fd, int name);
long pathconf(const char *path, int name);</code></pre>
<h2>Description</h2>
<p><code>fpathconf</code>() gets a value for the configuration option <i>name</i> for the open file descriptor <i>fd</i>. </p>
<p> <code>pathconf</code>() gets a value for configuration option <i>name</i> for the filename <i>path</i>. </p>
<p> The corresponding macros defined in <i>&lt;unistd.h&gt;</i> are minimum values; if an application wants to take advantage of values which may change, a call to <code>fpathconf</code>() or <code>pathconf</code>() can be made, which may yield more liberal results. </p>
<p> Setting <i>name</i> equal to one of the following constants returns the following configuration options:</p>
<dl>
<dt><code>_PC_LINK_MAX</code></p>
<dd>The maximum number of links to the file. If <i>fd</i> or <i>path</i> refer to a directory, then the value applies to the whole directory. The corresponding macro is <code>_POSIX_LINK_MAX</code>.</p>
<dt><code>_PC_MAX_CANON</code></p>
<dd>The maximum length of a formatted input line, where <i>fd</i> or <i>path</i> must refer to a terminal. The corresponding macro is <code>_POSIX_MAX_CANON</code>.</p>
<dt><code>_PC_MAX_INPUT</code></p>
<dd>The maximum length of an input line, where <i>fd</i> or <i>path</i> must refer to a terminal. The corresponding macro is <code>_POSIX_MAX_INPUT</code>.</p>
<dt><code>_PC_NAME_MAX</code></p>
<dd>The maximum length of a filename in the directory <i>path</i> or <i>fd</i> that the process is allowed to create. The corresponding macro is <code>_POSIX_NAME_MAX</code>.</p>
<dt><code>_PC_PATH_MAX</code></p>
<dd>The maximum length of a relative pathname when <i>path</i> or <i>fd</i> is the current working directory. The corresponding macro is <code>_POSIX_PATH_MAX</code>.</p>
<dt><code>_PC_PIPE_BUF</code></p>
<dd>The maximum number of bytes that can be written atomically to a pipe of FIFO. For <code>fpathconf</code>(), <i>fd</i> should refer to a pipe or FIFO. For <code>fpathconf</code>(), <i>path</i> should refer to a FIFO or a directory; in the latter case, the returned value corresponds to FIFOs created in that directory. The corresponding macro is <code>_POSIX_PIPE_BUF</code>.</p>
<dt><code>_PC_CHOWN_RESTRICTED</code></p>
<dd>This returns a positive value if the use of <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2) and <code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2) for changing a file&#8217;s user ID is restricted to a process with appropriate privileges, and changing a file&#8217;s group ID to a value other than the process&#8217;s effective group ID or one of its supplementary group IDs is restricted to a process with appropriate privileges. According to POSIX.1, this variable shall always be defined with a value other than -1. The corresponding macro is <code>_POSIX_CHOWN_RESTRICTED</code>.</p>
<dd>If <i>fd</i> or <i>path</i> refers to a directory, then the return value applies to all files in that directory.</p>
<dt><code>_PC_NO_TRUNC</code></p>
<dd>This returns nonzero if accessing filenames longer than <code>_POSIX_NAME_MAX</code> generates an error. The corresponding macro is <code>_POSIX_NO_TRUNC</code>.</p>
<dt><code>_PC_VDISABLE</code></p>
<dd>This returns nonzero if special character processing can be disabled, where <i>fd</i> or <i>path</i> must refer to a terminal.</dl>
<h2>Return Value</h2>
<p>The return value of these functions is one of the following:</p>
<dl>
<dt>*</p>
<dd>On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error (for example, <code>EINVAL</code>, indicating that <i>name</i> is invalid).</p>
<dt>*</p>
<dd>If <i>name</i> corresponds to a maximum or minimum limit, and that limit is indeterminate, -1 is returned and <i>errno</i> is not changed. (To distinguish an indeterminate limit from an error, set <i>errno</i> to zero before the call, and then check whether <i>errno</i> is nonzero when -1 is returned.)</p>
<dt>*</p>
<dd>If <i>name</i> corresponds to an option, a positive value is returned if the option is supported, and -1 is returned if the option is not supported.</p>
<dt>*</p>
<dd>Otherwise, the current value of the option or limit is returned. This value will not be more restrictive than the corresponding value that was described to the application in <i>&lt;unistd.h&gt;</i> or <i>&lt;limits.h&gt;</i> when the application was compiled.</dl>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>(<code>pathconf</code>()) Search permission is denied for one of the directories in the path prefix of <i>path</i>.</p>
<dt><code>EBADF</code></p>
<dd>(<code>fpathconf</code>()) <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd><i>name</i> is invalid.</p>
<dt><code>EINVAL</code></p>
<dd>The implementation does not support an association of <i>name</i> with the specified file.</p>
<dt><code>ELOOP</code></p>
<dd>(<code>pathconf</code>()) Too many symbolic links were encountered while resolving <i>path</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd>(<code>pathconf</code>()) <i>path</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd>(<code>pathconf</code>()) A component of <i>path</i> does not exist, or <i>path</i> is an empty string.</p>
<dt><code>ENOTDIR</code></p>
<dd>(<code>pathconf</code>()) A component used as a directory in <i>path</i> is not in fact a directory.</dl>
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
<td> <code>fpathconf</code>(), <code>pathconf</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>Files with name lengths longer than the value returned for <i>name</i> equal to <code>_PC_NAME_MAX</code> may exist in the given directory. </p>
<p> Some returned values may be huge; they are not suitable for allocating memory.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-getconf/">getconf</a></code>(1), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2), <code><a href="/docs/linux/man/3-confstr/">confstr</a></code>(3), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
