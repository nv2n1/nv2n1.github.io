---
title: "endgrent(3)"
name: "endgrent"
section: "3"
letter: "e"
url: "/docs/linux/man/3-endgrent/"
description: "getgrent, setgrent, endgrent – get group file entry"
---

<h2 class="name">NAME</h2>
<p> getgrent, setgrent, endgrent &#8211; get group file entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;grp.h&gt;
#include &lt;sys/types.h&gt;
struct group *getgrent(void);
void setgrent(void);
void endgrent(void);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>setgrent</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>getgrent</code>(), <code>endgrent</code>():</p>
<dl>
<dt>
<dd> Since glibc 2.22:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
 Glibc 2.21 and earlier<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>getgrent</code>() function returns a pointer to a structure containing the broken-out fields of a record in the group database (e.g., the local group file <i>/etc/group</i>, NIS, and LDAP). The first time <code>getgrent</code>() is called, it returns the first entry; thereafter, it returns successive entries. </p>
<p> The <code>setgrent</code>() function rewinds to the beginning of the group database, to allow repeated scans. </p>
<p> The <code>endgrent</code>() function is used to close the group database after all processing has been performed. </p>
<p> The <i>group</i> structure is defined in <i>&lt;grp.h&gt;</i> as follows: </p>
<p> struct group {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*gr_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*gr_passwd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group password&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;gr_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;**gr_mem;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;NULL-terminated array of pointers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to names of group members&nbsp;*/ }; </p>
<p> For more information about the fields of this structure, see <code><a href="/docs/linux/man/5-group/">group</a></code>(5).</p>
<h2>RETURN VALUE</h2>
<p> The <code>getgrent</code>() function returns a pointer to a <i>group</i> structure, or NULL if there are no more entries or an error occurs. </p>
<p> Upon error, <i>errno</i> may be set. If one wants to check <i>errno</i> after the call, it should be set to zero before the call. </p>
<p> The return value may point to a static area, and may be overwritten by subsequent calls to <code>getgrent</code>(), <code><a href="/docs/linux/man/3-getgrgid/">getgrgid</a></code>(3), or <code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a></code>(3). (Do not pass the returned pointer to <code><a href="/docs/linux/man/3-free/">free</a></code>(3).)</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The service was temporarily unavailable; try again later. For NSS backends in glibc this indicates a temporary error talking to the backend. The error may correct itself, retrying later is suggested.</p>
<dt><code>EINTR</code></p>
<dd> A signal was caught; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EIO</code></p>
<dd> I/O error.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt>
<dd> <code>ENOENT</code> A necessary input file cannot be found. For NSS backends in glibc this indicates the backend is not correctly configured.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to allocate <i>group</i> structure.</p>
<dt><code>ERANGE</code></p>
<dd> Insufficient buffer space supplied.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/group</i></p>
<dd> local group database file</dl>
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
<td> <code>getgrent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:grent<br />
 race:grentbuf locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>setgrent</code>(), <code>endgrent</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:grent locale
</td>
</tr>
</table>
<p> In the above table, <i>grent</i> in <i>race:grent</i> signifies that if any of the functions <code>setgrent</code>(), <code>getgrent</code>(), or <code>endgrent</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fgetgrent/">fgetgrent</a></code>(3), <code><a href="/docs/linux/man/3-getgrent_r/">getgrent_r</a></code>(3), <code><a href="/docs/linux/man/3-getgrgid/">getgrgid</a></code>(3), <code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a></code>(3), <code><a href="/docs/linux/man/3-getgrouplist/">getgrouplist</a></code>(3), <code><a href="/docs/linux/man/3-putgrent/">putgrent</a></code>(3), <code><a href="/docs/linux/man/5-group/">group</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
