---
title: "alphasort(3)"
name: "alphasort"
section: "3"
letter: "a"
url: "/docs/linux/man/3-alphasort/"
description: "scandir, scandirat, alphasort, versionsort – scan a directory for matching entries"
---

<h2 class="name">NAME</h2>
<p> scandir, scandirat, alphasort, versionsort &#8211; scan a directory for matching entries </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;dirent.h&gt;
int scandir(const char *dirp, struct dirent ***namelist,
            int (*filter)(const struct dirent *),
            int (*compar)(const struct dirent **, const struct dirent **));

int alphasort(const struct dirent **a, const struct dirent **b);
int versionsort(const struct dirent **a, const struct dirent **b);
#include &lt;dirent.h&gt;
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
int scandirat(int dirfd, const char *dirp,
              struct dirent ***namelist,
              int (*filter)(const struct dirent *),
              int (*compar)(const struct dirent **, const struct dirent **));
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>scandir</code>(), <code>alphasort</code>(): </p>
<dl>
<dt>
<dd> /* Since glibc 2.10: */ _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>versionsort</code>(): _GNU_SOURCE </p>
<p> <code>scandirat</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>scandir</code>() function scans the directory <i>dirp</i>, calling <i>filter</i>() on each directory entry. Entries for which <i>filter</i>() returns nonzero are stored in strings allocated via <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), sorted using <code><a href="/docs/linux/man/3-qsort/">qsort</a></code>(3) with the comparison function <i>compar</i>(), and collected in array <i>namelist</i> which is allocated via <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). If <i>filter</i> is NULL, all entries are selected. </p>
<p> The <code>alphasort</code>() and <code>versionsort</code>() functions can be used as the comparison function <i>compar</i>(). The former sorts directory entries using <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), the latter using <code><a href="/docs/linux/man/3-strverscmp/">strverscmp</a></code>(3) on the strings <i>(*a)-&gt;d_name</i> and <i>(*b)-&gt;d_name</i>.</p>
<h3>scandirat()</h3>
<p> The <code>scandirat</code>() function operates in exactly the same way as <code>scandir</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>dirp</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>scandir</code>() for a relative pathname). </p>
<p> If <i>dirp</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>dirp</i> is interpreted relative to the current working directory of the calling process (like <code>scandir</code>()). </p>
<p> If <i>dirp</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>scandirat</code>().</p>
<h2>RETURN VALUE</h2>
<p> The <code>scandir</code>() function returns the number of directory entries selected. On error, -1 is returned, with <i>errno</i> set to indicate the cause of the error. </p>
<p> The <code>alphasort</code>() and <code>versionsort</code>() functions return an integer less than, equal to, or greater than zero if the first argument is considered to be respectively less than, equal to, or greater than the second.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOENT</code></p>
<dd> The path in <i>dirp</i> does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to complete the operation.</p>
<dt><code>ENOTDIR</code></p>
<dd> The path in <i>dirp</i> is not a directory.</dl>
<p> The following additional errors can occur for <code>scandirat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>dirp</i> is a relative path and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>versionsort</code>() was added to glibc in version 2.1. </p>
<p> <code>scandirat</code>() was added to glibc in version 2.15.</p>
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
<td> <code>scandir</code>(), <code>scandirat</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>alphasort</code>(), <code>versionsort</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>alphasort</code>(), <code>scandir</code>(): 4.3BSD, POSIX.1-2008. </p>
<p> <code>versionsort</code>() and <code>scandirat</code>() are GNU extensions.</p>
<h2>NOTES</h2>
<p> Since glibc 2.1, <code>alphasort</code>() calls <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3); earlier it used <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3). </p>
<p> Before glibc 2.10, the two arguments of <code>alphasort</code>() and <code>versionsort</code>() were typed as <i>const void&nbsp;*</i>. When <code>alphasort</code>() was standardized in POSIX.1-2008, the argument type was specified as the type-safe <i>const struct dirent&nbsp;**,</i> and glibc 2.10 changed the definition of <code>alphasort</code>() (and the nonstandard <code>versionsort</code>()) to match the standard.</p>
<h2>EXAMPLES</h2>
<p> The program below prints a list of the files in the current directory in reverse order.</p>
<h3>Program source</h3>
<p> #define _DEFAULT_SOURCE #include &lt;dirent.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct dirent&nbsp;**namelist;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int n; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n&nbsp;=&nbsp;scandir(&quot;.&quot;,&nbsp;&amp;namelist, NULL, alphasort);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(n&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;scandir&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(n&#8211;)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s
&quot;, namelist[n]-&gt;d_name);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(namelist[n]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(namelist); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-closedir/">closedir</a></code>(3), <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3), <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), <code><a href="/docs/linux/man/3-rewinddir/">rewinddir</a></code>(3), <code><a href="/docs/linux/man/3-seekdir/">seekdir</a></code>(3), <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-strverscmp/">strverscmp</a></code>(3), <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
