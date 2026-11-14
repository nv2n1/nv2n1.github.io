---
title: "acct(2)"
name: "acct"
section: "2"
letter: "a"
url: "/docs/linux/man/2-acct/"
description: "acct – switch process accounting on or off"
---

<h2 class="name">NAME</h2>
<p> acct &#8211; switch process accounting on or off </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int acct(const char *filename);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>acct</code>(): </p>
<pre><code>
Since glibc 2.21 : _DEFAULT_SOURCE
                       In glibc 2.19 and
                   2.20 : _DEFAULT_SOURCE ||
    (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE &amp; nbsp; &lt; &amp;nbsp; 500)
        Up to and including glibc 2.19 : _BSD_SOURCE
                                         ||
                                         (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE &amp; nbsp; &lt; &amp;nbsp; 500)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>acct</code>() system call enables or disables process accounting. If called with the name of an existing file as its argument, accounting is turned on, and records for each terminating process are appended to <i>filename</i> as it terminates. An argument of NULL causes accounting to be turned off.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Write permission is denied for the specified file, or search permission is denied for one of the directories in the path prefix of <i>filename</i> (see also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7)), or <i>filename</i> is not a regular file.</p>
<dt><code>EFAULT</code></p>
<dd> <i>filename</i> points outside your accessible address space.</p>
<dt><code>EIO</code></p>
<dd> Error writing to the file <i>filename</i>.</p>
<dt><code>EISDIR</code></p>
<dd> <i>filename</i> is a directory.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>filename</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>filename</i> was too long.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOENT</code></p>
<dd> The specified file does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>ENOSYS</code></p>
<dd> BSD process accounting has not been enabled when the operating system kernel was compiled. The kernel configuration parameter controlling this feature is <code>CONFIG_BSD_PROCESS_ACCT</code>.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>filename</i> is not in fact a directory.</p>
<dt><code>EPERM</code></p>
<dd> The calling process has insufficient privilege to enable process accounting. On Linux, the <code>CAP_SYS_PACCT</code> capability is required.</p>
<dt><code>EROFS</code></p>
<dd> <i>filename</i> refers to a file on a read-only filesystem.</p>
<dt><code>EUSERS</code></p>
<dd> There are no more free file structures or we ran out of memory.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD (but not POSIX).</p>
<h2>NOTES</h2>
<p> No accounting is produced for programs running when a system crash occurs. In particular, nonterminating processes are never accounted for. </p>
<p> The structure of the records written to the accounting file is described in <code><a href="/docs/linux/man/5-acct/">acct</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-acct/">acct</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
