---

title: "acct(2)"
name: "acct"
section: "2"
letter: "a"
url: "/docs/linux/man/2-acct/"
description: "acct – switch process accounting on or off"
---

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
<p> The <code>acct</code>() system call enables or disables process accounting. If called with the name of an existing file as its argument, accounting is turned on, and records for each terminating process are appended to <i>filename</i> as it terminates. An argument of NULL causes accounting to be turned off.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></dt>
<dd> Write permission is denied for the specified file, or search permission is denied for one of the directories in the path prefix of <i>filename</i> (see also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7)), or <i>filename</i> is not a regular file.</dd>
<dt><code>EFAULT</code></dt>
<dd> <i>filename</i> points outside your accessible address space.</dd>
<dt><code>EIO</code></dt>
<dd> Error writing to the file <i>filename</i>.</dd>
<dt><code>EISDIR</code></dt>
<dd> <i>filename</i> is a directory.</dd>
<dt><code>ELOOP</code></dt>
<dd> Too many symbolic links were encountered in resolving <i>filename</i>.</dd>
<dt><code>ENAMETOOLONG</code></dt>
<dd> <i>filename</i> was too long.</dd>
<dt><code>ENFILE</code></dt>
<dd> The system-wide limit on the total number of open files has been reached.</dd>
<dt><code>ENOENT</code></dt>
<dd> The specified file does not exist.</dd>
<dt><code>ENOMEM</code></dt>
<dd> Out of memory.</dd>
<dt><code>ENOSYS</code></dt>
<dd> BSD process accounting has not been enabled when the operating system kernel was compiled. The kernel configuration parameter controlling this feature is <code>CONFIG_BSD_PROCESS_ACCT</code>.</dd>
<dt><code>ENOTDIR</code></dt>
<dd> A component used as a directory in <i>filename</i> is not in fact a directory.</dd>
<dt><code>EPERM</code></dt>
<dd> The calling process has insufficient privilege to enable process accounting. On Linux, the <code>CAP_SYS_PACCT</code> capability is required.</dd>
<dt><code>EROFS</code></dt>
<dd> <i>filename</i> refers to a file on a read-only filesystem.</dd>
<dt><code>EUSERS</code></dt>
<dd> There are no more free file structures or we ran out of memory.</dd></dl>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD (but not POSIX).</p>
<h2>NOTES</h2>
<p> No accounting is produced for programs running when a system crash occurs. In particular, nonterminating processes are never accounted for. </p>
<p> The structure of the records written to the accounting file is described in <code><a href="/docs/linux/man/5-acct/">acct</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-acct/">acct</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
