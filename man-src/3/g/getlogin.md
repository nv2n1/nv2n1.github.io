---

title: "getlogin(3)"
name: "getlogin"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getlogin/"
description: "getlogin, getlogin_r, cuserid – get username"
---

<p> getlogin, getlogin_r, cuserid - get username </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>char *getlogin(void);</code> <br/>
 <code>int getlogin_r(char *</code><i>buf</i><code>, size_t </code><i>bufsize</i><code>);</code> </p>
<p> <code>#include &lt;stdio.h&gt;</code> </p>
<p> <code>char *cuserid(char *</code><i>string</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getlogin_r</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199506L </p>
<p> <code>cuserid</code>(): </p>
<pre><code>    Since glibc 2.24:
        (_XOPEN_SOURCE &amp;&amp; ! (_POSIX_C_SOURCE &gt;= 200112L)
        || _GNU_SOURCE
    Up to and including glibc 2.23:
        _XOPEN_SOURCE
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>getlogin</code>() returns a pointer to a string containing the name of the user logged in on the controlling terminal of the process, or a null pointer if this information cannot be determined. The string is statically allocated and might be overwritten on subsequent calls to this function or to <code>cuserid</code>(). </p>
<p> <code>getlogin_r</code>() returns this same username in the array <i>buf</i> of size <i>bufsize</i>. </p>
<p> <code>cuserid</code>() returns a pointer to a string containing a username associated with the effective user ID of the process. If <i>string</i> is not a null pointer, it should be an array that can hold at least <code>L_cuserid</code> characters; the string is returned in this array. Otherwise, a pointer to a string in a static area is returned. This string is statically allocated and might be overwritten on subsequent calls to this function or to <code>getlogin</code>(). </p>
<p> The macro <code>L_cuserid</code> is an integer constant that indicates how long an array you might need to store a username. <code>L_cuserid</code> is declared in <i>&lt;stdio.h&gt;</i>. </p>
<p> These functions let your program identify positively the user who is running (<code>cuserid</code>()) or the user who logged in this session (<code>getlogin</code>()). (These can differ when set-user-ID programs are involved.) </p>
<p> For most purposes, it is more useful to use the environment variable <code>LOGNAME</code> to find out who the user is. This is more flexible precisely because the user can set <code>LOGNAME</code> arbitrarily.  </p>
<h2>RETURN VALUE</h2>
<p> <code>getlogin</code>() returns a pointer to the username when successful, and NULL on failure, with <i>errno</i> set to indicate the cause of the error. <code>getlogin_r</code>() returns 0 when successful, and nonzero on failure.  </p>
<h2>ERRORS</h2>
<p> POSIX specifies: </p>
<dl>
<dt><code>EMFILE</code></dt>
<dd> <p> The per-process limit on the number of open file descriptors has been reached. </p>
 </dd>
<dt><code>ENFILE</code></dt>
<dd> <p> The system-wide limit on the total number of open files has been reached. </p>
 </dd>
<dt><code>ENXIO</code></dt>
<dd> <p> The calling process has no controlling terminal. </p>
 </dd>
<dt><code>ERANGE</code></dt>
<dd> <p> (getlogin_r) The length of the username, including the terminating null byte (&#8216;\0&#8217;), is larger than <i>bufsize</i>. </p>
 </dd></dl>
<p> Linux/glibc also has: </p>
<dl>
<dt><code>ENOENT</code></dt>
<dd> <p> There was no corresponding entry in the utmp-file. </p>
 </dd>
<dt><code>ENOMEM</code></dt>
<dd> <p> Insufficient memory to allocate passwd structure. </p>
 </dd>
<dt><code>ENOTTY</code></dt>
<dd> <p> Standard input didn&#8217;t refer to a terminal. (See BUGS.) </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/passwd</i></dt>
<dd> <p> password database file </p>
 </dd>
<dt><i>/var/run/utmp</i></dt>
<dd> <p> (traditionally <i>/etc/utmp</i>; some libc versions used <i>/var/adm/utmp</i>) </p>
 </dd></dl>
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
<td> <code>getlogin</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:getlogin race:utent  sig:ALRM timer locale 
</td>
</tr>
<tr VALIGN=top>
<td> <code>getlogin_r</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:utent sig:ALRM timer  locale 
</td>
</tr>
<tr VALIGN=top>
<td> <code>cuserid</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:cuserid/!string locale
</td>
</tr>
</table>
<p> In the above table, <i>utent</i> in <i>race:utent</i> signifies that if any of the functions <code><a href="/docs/linux/man/3-setutent/">setutent</a></code>(3), <code><a href="/docs/linux/man/3-getutent/">getutent</a></code>(3), or <code><a href="/docs/linux/man/3-endutent/">endutent</a></code>(3) are used in parallel in different threads of a program, then data races could occur. <code>getlogin</code>() and <code>getlogin_r</code>() call those functions, so we use race:utent to remind users.  </p>
<h2>CONFORMING TO</h2>
<p> <code>getlogin</code>() and <code>getlogin_r</code>(): POSIX.1-2001, POSIX.1-2008. </p>
<p> System V has a <code>cuserid</code>() function which uses the real user ID rather than the effective user ID. The <code>cuserid</code>() function was included in the 1988 version of POSIX, but removed from the 1990 version. It was present in SUSv2, but removed in POSIX.1-2001. </p>
<p> OpenBSD has <code>getlogin</code>() and <code>setlogin</code>(), and a username associated with a session, even if it has no controlling terminal.  </p>
<h2>BUGS</h2>
<p> Unfortunately, it is often rather easy to fool <code>getlogin</code>(). Sometimes it does not work at all, because some program messed up the utmp file. Often, it gives only the first 8 characters of the login name. The user currently logged in on the controlling terminal of our program need not be the user who started it. Avoid <code>getlogin</code>() for security-related purposes. </p>
<p> Note that glibc does not follow the POSIX specification and uses <i>stdin</i> instead of <i>/dev/tty</i>. A bug. (Other recent systems, like SunOS 5.8 and HP-UX 11.11 and FreeBSD 4.8 all return the login name also when <i>stdin</i> is redirected.) </p>
<p> Nobody knows precisely what <code>cuserid</code>() does; avoid it in portable programs. Or avoid it altogether: use <i>getpwuid(geteuid())</i> instead, if that is what you meant. <code>Do not use</code> <code>cuserid</code>().  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-logname/">logname</a></code>(1), <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2), <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
