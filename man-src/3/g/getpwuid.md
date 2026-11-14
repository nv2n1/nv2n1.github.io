---
title: "getpwuid(3)"
name: "getpwuid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getpwuid/"
description: "getpwnam, getpwnam_r, getpwuid, getpwuid_r – get password file entry"
---

<h2 class="name">NAME</h2>
<p> getpwnam, getpwnam_r, getpwuid, getpwuid_r &#8211; get password file entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;pwd.h&gt;
#include &lt;sys/types.h&gt;
struct passwd *getpwnam(const char *name);
struct passwd *getpwuid(uid_t uid);
int getpwnam_r(const char *name, struct passwd *pwd,
               char *buf, size_t buflen, struct passwd **result);
int getpwuid_r(uid_t uid, struct passwd *pwd,
               char *buf, size_t buflen, struct passwd **result);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getpwnam_r</code>(), <code>getpwuid_r</code>():</p>
<dl>
<dt>
<dd> _POSIX_C_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>getpwnam</code>() function returns a pointer to a structure containing the broken-out fields of the record in the password database (e.g., the local password file <i>/etc/passwd</i>, NIS, and LDAP) that matches the username <i>name</i>. </p>
<p> The <code>getpwuid</code>() function returns a pointer to a structure containing the broken-out fields of the record in the password database that matches the user ID <i>uid</i>. </p>
<p> The <i>passwd</i> structure is defined in <i>&lt;pwd.h&gt;</i> as follows: </p>
<p> struct passwd {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;username&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_passwd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user password&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;pw_uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;pw_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_gecos;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_dir;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;home directory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_shell;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;shell program&nbsp;*/ }; </p>
<p> See <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5) for more information about these fields. </p>
<p> The <code>getpwnam_r</code>() and <code>getpwuid_r</code>() functions obtain the same information as <code>getpwnam</code>() and <code>getpwuid</code>(), but store the retrieved <i>passwd</i> structure in the space pointed to by <i>pwd</i>. The string fields pointed to by the members of the <i>passwd</i> structure are stored in the buffer <i>buf</i> of size <i>buflen</i>. A pointer to the result (in case of success) or NULL (in case no entry was found or an error occurred) is stored in <i>*result</i>. </p>
<p> The call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sysconf(_SC_GETPW_R_SIZE_MAX) </p>
<p> returns either -1, without changing <i>errno</i>, or an initial suggested size for <i>buf</i>. (If this size is too small, the call fails with <code>ERANGE</code>, in which case the caller can retry with a larger buffer.)</p>
<h2>RETURN VALUE</h2>
<p> The <code>getpwnam</code>() and <code>getpwuid</code>() functions return a pointer to a <i>passwd</i> structure, or NULL if the matching entry is not found or an error occurs. If an error occurs, <i>errno</i> is set appropriately. If one wants to check <i>errno</i> after the call, it should be set to zero before the call. </p>
<p> The return value may point to a static area, and may be overwritten by subsequent calls to <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code>getpwnam</code>(), or <code>getpwuid</code>(). (Do not pass the returned pointer to <code><a href="/docs/linux/man/3-free/">free</a></code>(3).) </p>
<p> On success, <code>getpwnam_r</code>() and <code>getpwuid_r</code>() return zero, and set <i>*result</i> to <i>pwd</i>. If no matching password record was found, these functions return 0 and store NULL in <i>*result</i>. In case of error, an error number is returned, and NULL is stored in <i>*result</i>.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>0</code> or <code>ENOENT</code> or <code>ESRCH</code> or <code>EBADF</code> or <code>EPERM</code> or &#8230;</p>
<dd> The given <i>name</i> or <i>uid</i> was not found.</p>
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
<h2>NOTE</h2>
<p> The user password database mostly refers to <i>/etc/passwd</i>. However, with recent systems it also refers to network wide databases using NIS, LDAP and other local files as configured in <i>/etc/nsswitch.conf</i>.</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/passwd</i></p>
<dd> local password database file</p>
<dt><i>/etc/nsswitch.conf</i></p>
<dd> System Databases and Name Service Switch configuration file</dl>
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
<td> <code>getpwnam</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:pwnam locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getpwuid</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:pwuid locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getpwnam_r</code>(),<br />
 <code>getpwuid_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. The <i>pw_gecos</i> field is not specified in POSIX, but is present on most implementations.</p>
<h2>NOTES</h2>
<p> The formulation given above under &quot;RETURN VALUE&quot; is from POSIX.1-2001. It does not call &quot;not found&quot; an error, and hence does not specify what value <i>errno</i> might have in this situation. But that makes it impossible to recognize errors. One might argue that according to POSIX <i>errno</i> should be left unchanged if an entry is not found. Experiments on various UNIX-like systems show that lots of different values occur in this situation: 0, ENOENT, EBADF, ESRCH, EWOULDBLOCK, EPERM, and probably others. </p>
<p> The <i>pw_dir</i> field contains the name of the initial working directory of the user. Login programs use the value of this field to initialize the <code>HOME</code> environment variable for the login shell. An application that wants to determine its user&#8217;s home directory should inspect the value of <code>HOME</code> (rather than the value <i>getpwuid(getuid())-&gt;pw_dir</i>) since this allows the user to modify their notion of &quot;the home directory&quot; during a login session. To determine the (initial) home directory of another user, it is necessary to use <i>getpwnam(username)-&gt;pw_dir</i> or similar.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>getpwnam_r</code>() to find the full username and user ID for the username supplied as a command-line argument. </p>
<p> #include &lt;pwd.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;errno.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct passwd pwd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct passwd&nbsp;*result;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*buf;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t bufsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int s; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s username
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bufsize&nbsp;=&nbsp;sysconf(_SC_GETPW_R_SIZE_MAX);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(bufsize&nbsp;==&nbsp;-1)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Value was indeterminate&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bufsize&nbsp;=&nbsp;16384;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Should be more than enough&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf&nbsp;=&nbsp;malloc(bufsize);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(buf&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;malloc&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;getpwnam_r(argv[1],&nbsp;&amp;pwd, buf, bufsize,&nbsp;&amp;result);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(result&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;==&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Not found
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno&nbsp;=&nbsp;s;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;getpwnam_r&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Name:&nbsp;%s;&nbsp;UID:&nbsp;%jd
&quot;, pwd.pw_gecos,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;pwd.pw_uid);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-endpwent/">endpwent</a></code>(3), <code><a href="/docs/linux/man/3-fgetpwent/">fgetpwent</a></code>(3), <code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a></code>(3), <code><a href="/docs/linux/man/3-getpw/">getpw</a></code>(3), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/3-getspnam/">getspnam</a></code>(3), <code><a href="/docs/linux/man/3-putpwent/">putpwent</a></code>(3), <code><a href="/docs/linux/man/3-setpwent/">setpwent</a></code>(3), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
