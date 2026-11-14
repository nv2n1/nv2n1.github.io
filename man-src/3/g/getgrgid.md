---
title: "getgrgid(3)"
name: "getgrgid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getgrgid/"
description: "getgrnam, getgrnam_r, getgrgid, getgrgid_r – get group file entry"
---

<h2 class="name">NAME</h2>
<p> getgrnam, getgrnam_r, getgrgid, getgrgid_r &#8211; get group file entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;grp.h&gt;
#include &lt;sys/types.h&gt;
struct group *getgrnam(const char *name);
struct group *getgrgid(gid_t gid);
int getgrnam_r(const char *name, struct group *grp,
               char *buf, size_t buflen, struct group **result);
int getgrgid_r(gid_t gid, struct group *grp,
               char *buf, size_t buflen, struct group **result);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getgrnam_r</code>(), <code>getgrgid_r</code>():</p>
<dl>
<dt>
<dd> _POSIX_C_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>getgrnam</code>() function returns a pointer to a structure containing the broken-out fields of the record in the group database (e.g., the local group file <i>/etc/group</i>, NIS, and LDAP) that matches the group name <i>name</i>. </p>
<p> The <code>getgrgid</code>() function returns a pointer to a structure containing the broken-out fields of the record in the group database that matches the group ID <i>gid</i>. </p>
<p> The <i>group</i> structure is defined in <i>&lt;grp.h&gt;</i> as follows: </p>
<p> struct group {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*gr_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*gr_passwd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group password&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;gr_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;**gr_mem;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;NULL-terminated array of pointers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to names of group members&nbsp;*/ }; </p>
<p> For more information about the fields of this structure, see <code><a href="/docs/linux/man/5-group/">group</a></code>(5). </p>
<p> The <code>getgrnam_r</code>() and <code>getgrgid_r</code>() functions obtain the same information as <code>getgrnam</code>() and <code>getgrgid</code>(), but store the retrieved <i>group</i> structure in the space pointed to by <i>grp</i>. The string fields pointed to by the members of the <i>group</i> structure are stored in the buffer <i>buf</i> of size <i>buflen</i>. A pointer to the result (in case of success) or NULL (in case no entry was found or an error occurred) is stored in <i>*result</i>. </p>
<p> The call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sysconf(_SC_GETGR_R_SIZE_MAX) </p>
<p> returns either -1, without changing <i>errno</i>, or an initial suggested size for <i>buf</i>. (If this size is too small, the call fails with <code>ERANGE</code>, in which case the caller can retry with a larger buffer.)</p>
<h2>RETURN VALUE</h2>
<p> The <code>getgrnam</code>() and <code>getgrgid</code>() functions return a pointer to a <i>group</i> structure, or NULL if the matching entry is not found or an error occurs. If an error occurs, <i>errno</i> is set appropriately. If one wants to check <i>errno</i> after the call, it should be set to zero before the call. </p>
<p> The return value may point to a static area, and may be overwritten by subsequent calls to <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code>getgrgid</code>(), or <code>getgrnam</code>(). (Do not pass the returned pointer to <code><a href="/docs/linux/man/3-free/">free</a></code>(3).) </p>
<p> On success, <code>getgrnam_r</code>() and <code>getgrgid_r</code>() return zero, and set <i>*result</i> to <i>grp</i>. If no matching group record was found, these functions return 0 and store NULL in <i>*result</i>. In case of error, an error number is returned, and NULL is stored in <i>*result</i>.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>0</code> or <code>ENOENT</code> or <code>ESRCH</code> or <code>EBADF</code> or <code>EPERM</code> or &#8230;</p>
<dd> The given <i>name</i> or <i>gid</i> was not found.</p>
<dt><code>EINTR</code></p>
<dd> A signal was caught; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EIO</code></p>
<dd> I/O error.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
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
<td> <code>getgrnam</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:grnam locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getgrgid</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:grgid locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getgrnam_r</code>(),<br />
 <code>getgrgid_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> The formulation given above under &quot;RETURN VALUE&quot; is from POSIX.1. It does not call &quot;not found&quot; an error, hence does not specify what value <i>errno</i> might have in this situation. But that makes it impossible to recognize errors. One might argue that according to POSIX <i>errno</i> should be left unchanged if an entry is not found. Experiments on various UNIX-like systems show that lots of different values occur in this situation: 0, ENOENT, EBADF, ESRCH, EWOULDBLOCK, EPERM, and probably others.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-endgrent/">endgrent</a></code>(3), <code><a href="/docs/linux/man/3-fgetgrent/">fgetgrent</a></code>(3), <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), <code><a href="/docs/linux/man/3-setgrent/">setgrent</a></code>(3), <code><a href="/docs/linux/man/5-group/">group</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
