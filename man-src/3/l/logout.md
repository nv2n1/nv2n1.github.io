---
title: "logout(3)"
name: "logout"
section: "3"
letter: "l"
url: "/docs/linux/man/3-logout/"
description: "login, logout – write utmp and wtmp entries"
---

<h2 class="name">NAME</h2>
<p> login, logout &#8211; write utmp and wtmp entries </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;utmp.h&gt;</code> </p>
<p> <code>void login(const struct utmp *</code><i>ut</i><code>);</code> </p>
<p> <code>int logout(const char *</code><i>ut_line</i><code>);</code> </p>
<p> Link with <i>-lutil</i>.</p>
<h2>DESCRIPTION</h2>
<p> The utmp file records who is currently using the system. The wtmp file records all logins and logouts. See <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5). </p>
<p> The function <code>login</code>() takes the supplied <i>struct utmp</i>, <i>ut</i>, and writes it to both the utmp and the wtmp file. </p>
<p> The function <code>logout</code>() clears the entry in the utmp file again.</p>
<h3>GNU details</h3>
<p> More precisely, <code>login</code>() takes the argument <i>ut</i> struct, fills the field <i>ut-&gt;ut_type</i> (if there is such a field) with the value <code>USER_PROCESS</code>, and fills the field <i>ut-&gt;ut_pid</i> (if there is such a field) with the process ID of the calling process. Then it tries to fill the field <i>ut-&gt;ut_line</i>. It takes the first of <i>stdin</i>, <i>stdout</i>, <i>stderr</i> that is a terminal, and stores the corresponding pathname minus a possible leading <i>/dev/</i> into this field, and then writes the struct to the utmp file. On the other hand, if no terminal name was found, this field is filled with &quot;???&quot; and the struct is not written to the utmp file. After this, the struct is written to the wtmp file. </p>
<p> The <code>logout</code>() function searches the utmp file for an entry matching the <i>ut_line</i> argument. If a record is found, it is updated by zeroing out the <i>ut_name</i> and <i>ut_host</i> fields, updating the <i>ut_tv</i> timestamp field and setting <i>ut_type</i> (if there is such a field) to <code>DEAD_PROCESS</code>.</p>
<h2>RETURN VALUE</h2>
<p> The <code>logout</code>() function returns 1 if the entry was successfully written to the database, or 0 if an error occurred.</p>
<h2>FILES</h2>
<dl>
<dt><i>/var/run/utmp</i></p>
<dd> user accounting database, configured through <code>_PATH_UTMP</code> in <i>&lt;paths.h&gt;</i></p>
<dt><i>/var/log/wtmp</i></p>
<dd> user accounting log file, configured through <code>_PATH_WTMP</code> in <i>&lt;paths.h&gt;</i></dl>
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
<td> <code>login</code>(),<br />
 <code>logout</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:utent<br />
 sig:ALRM timer
</td>
</tr>
</table>
<p> In the above table, <i>utent</i> in <i>race:utent</i> signifies that if any of the functions <code><a href="/docs/linux/man/3-setutent/">setutent</a></code>(3), <code><a href="/docs/linux/man/3-getutent/">getutent</a></code>(3), or <code><a href="/docs/linux/man/3-endutent/">endutent</a></code>(3) are used in parallel in different threads of a program, then data races could occur. <code>login</code>() and <code>logout</code>() calls those functions, so we use race:utent to remind users.</p>
<h2>CONFORMING TO</h2>
<p> Not in POSIX.1. Present on the BSDs.</p>
<h2>NOTES</h2>
<p> Note that the member <i>ut_user</i> of <i>struct utmp</i> is called <i>ut_name</i> in BSD. Therefore, <i>ut_name</i> is defined as an alias for <i>ut_user</i> in <i>&lt;utmp.h&gt;</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getutent/">getutent</a></code>(3), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
