---
title: "fgetpwent(3)"
name: "fgetpwent"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fgetpwent/"
description: "fgetpwent – get password file entry"
---

<h2 class="name">NAME</h2>
<p> fgetpwent &#8211; get password file entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;pwd.h&gt;
#include &lt;stdio.h&gt;
#include &lt;sys/types.h&gt;
struct passwd *fgetpwent(FILE *stream);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fgetpwent</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>fgetpwent</code>() function returns a pointer to a structure containing the broken out fields of a line in the file <i>stream</i>. The first time it is called it returns the first entry; thereafter, it returns successive entries. The file referred to by <i>stream</i> must have the same format as <i>/etc/passwd</i> (see <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5)). </p>
<p> The <i>passwd</i> structure is defined in <i>&lt;pwd.h&gt;</i> as follows: </p>
<p> struct passwd {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;username&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_passwd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user password&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;pw_uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;pw_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_gecos;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;real name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_dir;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;home directory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_shell;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;shell program&nbsp;*/ };</p>
<h2>RETURN VALUE</h2>
<p> The <code>fgetpwent</code>() function returns a pointer to a <i>passwd</i> structure, or NULL if there are no more entries or an error occurs. In the event of an error, <i>errno</i> is set to indicate the cause.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to allocate <i>passwd</i> structure.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/passwd</i></p>
<dd> password database file</dl>
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
<td> <code>fgetpwent</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:fgetpwent
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SVr4.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-endpwent/">endpwent</a></code>(3), <code><a href="/docs/linux/man/3-fgetpwent_r/">fgetpwent_r</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-getpw/">getpw</a></code>(3), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3), <code><a href="/docs/linux/man/3-putpwent/">putpwent</a></code>(3), <code><a href="/docs/linux/man/3-setpwent/">setpwent</a></code>(3), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
