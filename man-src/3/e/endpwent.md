---
title: "endpwent(3)"
name: "endpwent"
section: "3"
letter: "e"
url: "/docs/linux/man/3-endpwent/"
description: "getpwent, setpwent, endpwent – get password file entry"
---

<h2 class="name">NAME</h2>
<p> getpwent, setpwent, endpwent &#8211; get password file entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;pwd.h&gt;
#include &lt;sys/types.h&gt;
struct passwd *getpwent(void);
void setpwent(void);
void endpwent(void);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getpwent</code>(), <code>setpwent</code>(), <code>endpwent</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>getpwent</code>() function returns a pointer to a structure containing the broken-out fields of a record from the password database (e.g., the local password file <i>/etc/passwd</i>, NIS, and LDAP). The first time <code>getpwent</code>() is called, it returns the first entry; thereafter, it returns successive entries. </p>
<p> The <code>setpwent</code>() function rewinds to the beginning of the password database. </p>
<p> The <code>endpwent</code>() function is used to close the password database after all processing has been performed. </p>
<p> The <i>passwd</i> structure is defined in <i>&lt;pwd.h&gt;</i> as follows: </p>
<p> struct passwd {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;username&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_passwd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user password&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;pw_uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;pw_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_gecos;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_dir;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;home directory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_shell;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;shell program&nbsp;*/ }; </p>
<p> When <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5) passwords are enabled (which is default on many GNU/Linux installations) the content of <i>pw_passwd</i> is usually not very useful. In such a case most passwords are stored in a separate file. </p>
<p> The variable <i>pw_shell</i> may be empty, in which case the system will execute the default shell (<code>/bin/sh</code>) for the user. </p>
<p> For more information about the fields of this structure, see <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5).</p>
<h2>RETURN VALUE</h2>
<p> The <code>getpwent</code>() function returns a pointer to a <i>passwd</i> structure, or NULL if there are no more entries or an error occurred. If an error occurs, <i>errno</i> is set appropriately. If one wants to check <i>errno</i> after the call, it should be set to zero before the call. </p>
<p> The return value may point to a static area, and may be overwritten by subsequent calls to <code>getpwent</code>(), <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), or <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3). (Do not pass the returned pointer to <code><a href="/docs/linux/man/3-free/">free</a></code>(3).)</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINTR</code></p>
<dd> A signal was caught; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EIO</code></p>
<dd> I/O error.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to allocate <i>passwd</i> structure.</p>
<dt><code>ERANGE</code></p>
<dd> Insufficient buffer space supplied.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/passwd</i></p>
<dd> local password database file</dl>
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
<td> <code>getpwent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:pwent<br />
 race:pwentbuf locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>setpwent</code>(),<br />
 <code>endpwent</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:pwent locale
</td>
</tr>
</table>
<p> In the above table, <i>pwent</i> in <i>race:pwent</i> signifies that if any of the functions <code>setpwent</code>(), <code>getpwent</code>(), or <code>endpwent</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. The <i>pw_gecos</i> field is not specified in POSIX, but is present on most implementations.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fgetpwent/">fgetpwent</a></code>(3), <code><a href="/docs/linux/man/3-getpw/">getpw</a></code>(3), <code><a href="/docs/linux/man/3-getpwent_r/">getpwent_r</a></code>(3), <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3), <code><a href="/docs/linux/man/3-putpwent/">putpwent</a></code>(3), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
