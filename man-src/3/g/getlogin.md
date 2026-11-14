---
title: "getlogin(3)"
name: "getlogin"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getlogin/"
description: "getlogin, getlogin_r, cuserid – get username"
---

<h2 class="name">NAME</h2>
<p> getlogin, getlogin_r, cuserid &#8211; get username </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>char *getlogin(void);</code><br />
 <code>int getlogin_r(char *</code><i>buf</i><code>, size_t </code><i>bufsize</i><code>);</code> </p>
<p> <code>#include &lt;stdio.h&gt;</code> </p>
<p> <code>char *cuserid(char *</code><i>string</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getlogin_r</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199506L </p>
<p> <code>cuserid</code>(): </p>
<pre>
    Since glibc 2.24:
        (_XOPEN_SOURCE &amp;&amp; ! (_POSIX_C_SOURCE &gt;= 200112L)
        || _GNU_SOURCE
    Up to and including glibc 2.23:
        _XOPEN_SOURCE
</pre>
<h2>DESCRIPTION</h2>
<p> <code>getlogin</code>() returns a pointer to a string containing the name of the user logged in on the controlling terminal of the process, or a null pointer if this information cannot be determined. The string is statically allocated and might be overwritten on subsequent calls to this function or to <code>cuserid</code>(). </p>
<p> <code>getlogin_r</code>() returns this same username in the array <i>buf</i> of size <i>bufsize</i>. </p>
<p> <code>cuserid</code>() returns a pointer to a string containing a username associated with the effective user ID of the process. If <i>string</i> is not a null pointer, it should be an array that can hold at least <code>L_cuserid</code> characters; the string is returned in this array. Otherwise, a pointer to a string in a static area is returned. This string is statically allocated and might be overwritten on subsequent calls to this function or to <code>getlogin</code>(). </p>
<p> The macro <code>L_cuserid</code> is an integer constant that indicates how long an array you might need to store a username. <code>L_cuserid</code> is declared in <i>&lt;stdio.h&gt;</i>. </p>
<p> These functions let your program identify positively the user who is running (<code>cuserid</code>()) or the user who logged in this session (<code>getlogin</code>()). (These can differ when set-user-ID programs are involved.) </p>
<p> For most purposes, it is more useful to use the environment variable <code>LOGNAME</code> to find out who the user is. This is more flexible precisely because the user can set <code>LOGNAME</code> arbitrarily.</p>
<h2>RETURN VALUE</h2>
<p> <code>getlogin</code>() returns a pointer to the username when successful, and NULL on failure, with <i>errno</i> set to indicate the cause of the error. <code>getlogin_r</code>() returns 0 when successful, and nonzero on failure.</p>
<h2>ERRORS</h2>
<p> POSIX specifies:</p>
<dl>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENXIO</code></p>
<dd> The calling process has no controlling terminal.</p>
<dt><code>ERANGE</code></p>
<dd> (getlogin_r) The length of the username, including the terminating null byte (&#8216;
