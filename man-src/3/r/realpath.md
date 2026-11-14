---
title: "realpath(3)"
name: "realpath"
section: "3"
letter: "r"
url: "/docs/linux/man/3-realpath/"
description: "realpath – return the canonicalized absolute pathname"
---

<p>realpath &#8211; return the canonicalized absolute pathname</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;limits.h&gt;
#include &lt;stdlib.h&gt;

char *realpath(const char *path, char *resolved_path);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>realpath</code>():</p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>Description</h2>
<p><code>realpath</code>() expands all symbolic links and resolves references to <i>/./</i>, <i>/../</i> and extra &#8216;/&#8217; characters in the null-terminated string named by <i>path</i> to produce a canonicalized absolute pathname. The resulting pathname is stored as a null-terminated string, up to a maximum of <code>PATH_MAX</code> bytes, in the buffer pointed to by <i>resolved_path</i>. The resulting path will have no symbolic link, <i>/./</i> or <i>/../</i> components. </p>
<p> If <i>resolved_path</i> is specified as NULL, then <code>realpath</code>() uses <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) to allocate a buffer of up to <code>PATH_MAX</code> bytes to hold the resolved pathname, and returns a pointer to this buffer. The caller should deallocate this buffer using <code><a href="/docs/linux/man/3-free/">free</a></code>(3).</p>
<h2>Return Value</h2>
<p>If there is no error, <code>realpath</code>() returns a pointer to the <i>resolved_path</i>. </p>
<p> Otherwise, it returns NULL, the contents of the array <i>resolved_path</i> are undefined, and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>Read or search permission was denied for a component of the path prefix.</p>
<dt><code>EINVAL</code></p>
<dd><i>path</i> is NULL. (In glibc versions before 2.3, this error is also returned if <i>resolved_path</i> is NULL.)</p>
<dt><code>EIO</code></p>
<dd>An I/O error occurred while reading from the filesystem.</p>
<dt><code>ELOOP</code></p>
<dd>Too many symbolic links were encountered in translating the pathname.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd>A component of a pathname exceeded <code>NAME_MAX</code> characters, or an entire pathname exceeded <code>PATH_MAX</code> characters.</p>
<dt><code>ENOENT</code></p>
<dd>The named file does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd>Out of memory.</p>
<dt><code>ENOTDIR</code></p>
<dd>A component of the path prefix is not a directory.</dl>
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
<td> <code>realpath</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>4.4BSD, POSIX.1-2001. </p>
<p> POSIX.1-2001 says that the behavior if <i>resolved_path</i> is NULL is implementation-defined. POSIX.1-2008 specifies the behavior described in this page.</p>
<h2>Notes</h2>
<p>In 4.4BSD and Solaris, the limit on the pathname length is <code>MAXPATHLEN</code> (found in <i>&lt;sys/param.h&gt;</i>). SUSv2 prescribes <code>PATH_MAX</code> and <code>NAME_MAX</code>, as found in <i>&lt;limits.h&gt;</i> or provided by the <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3) function. A typical source fragment would be </p>
<pre><code>#ifdef PATH_MAX

path_max = PATH_MAX;
#else

path_max = pathconf(path, _PC_PATH_MAX);

if (path_max &lt;= 0)
    path_max = 4096;
#endif</code></pre>
<p> (But see the BUGS section.)</p>
<h3>GNU extensions</h3>
<p>If the call fails with either <code>EACCES</code> or <code>ENOENT</code> and <i>resolved_path</i> is not NULL, then the prefix of <i>path</i> that is not readable or does not exist is returned in <i>resolved_path</i>.</p>
<h2>Bugs</h2>
<p>The POSIX.1-2001 standard version of this function is broken by design, since it is impossible to determine a suitable size for the output buffer, <i>resolved_path</i>. According to POSIX.1-2001 a buffer of size <code>PATH_MAX</code> suffices, but <code>PATH_MAX</code> need not be a defined constant, and may have to be obtained using <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3). And asking <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3) does not really help, since, on the one hand POSIX warns that the result of <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3) may be huge and unsuitable for mallocing memory, and on the other hand <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3) may return -1 to signify that <code>PATH_MAX</code> is not bounded. The <i>resolved_path&nbsp;==&nbsp;NULL</i> feature, not standardized in POSIX.1-2001, but standardized in POSIX.1-2008, allows this design problem to be avoided.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-realpath/">realpath</a></code>(1), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/3-canonicalize_file_name/">canonicalize_file_name</a></code>(3), <code><a href="/docs/linux/man/3-getcwd/">getcwd</a></code>(3), <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
