---
title: "putpwent(3)"
name: "putpwent"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putpwent/"
description: "putpwent – write a password file entry"
---

<p>putpwent &#8211; write a password file entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pwd.h&gt;
#include &lt;stdio.h&gt;
#include &lt;sys/types.h&gt;

int putpwent(const struct passwd *p, FILE *stream);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>putpwent</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>The <code>putpwent</code>() function writes a password entry from the structure <i>p</i> in the file associated with <i>stream</i>. The <i>passwd</i> structure is defined in <i>&lt;pwd.h&gt;</i> as follows: </p>
<pre><code>struct passwd {
    char *pw_name;   /* username */
    char *pw_passwd; /* user password */
    uid_t pw_uid;    /* user ID */
    gid_t pw_gid;    /* group ID */
    char *pw_gecos;  /* real name */
    char *pw_dir;    /* home directory */
    char *pw_shell;  /* shell program */
};</code></pre>
<h2>Return Value</h2>
<p>The <code>putpwent</code>() function returns 0 on success, or -1 if an error occurs. In the event of an error, <i>errno</i> is set to indicate the cause.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>Invalid (NULL) argument given.</dl>
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
<td> <code>putpwent</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>SVr4.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-endpwent/">endpwent</a></code>(3), <code><a href="/docs/linux/man/3-fgetpwent/">fgetpwent</a></code>(3), <code><a href="/docs/linux/man/3-getpw/">getpw</a></code>(3), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3), <code><a href="/docs/linux/man/3-setpwent/">setpwent</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
