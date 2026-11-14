---
title: "endutxent(3)"
name: "endutxent"
section: "3"
letter: "e"
url: "/docs/linux/man/3-endutxent/"
description: "getutent, getutid, getutline, pututline, setutent, endutent, utmpname – access utmp file entries"
---

<h2 class="name">NAME</h2>
<p> getutent, getutid, getutline, pututline, setutent, endutent, utmpname &#8211; access utmp file entries </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;utmp.h&gt;</code> </p>
<p> <code>struct utmp *getutent(void);</code><br />
 <code>struct utmp *getutid(const struct utmp *</code><i>ut</i><code>);</code><br />
 <code>struct utmp *getutline(const struct utmp *</code><i>ut</i><code>);</code> </p>
<p> <code>struct utmp *pututline(const struct utmp *</code><i>ut</i><code>);</code> </p>
<p> <code>void setutent(void);</code><br />
 <code>void endutent(void);</code> </p>
<p> <code>int utmpname(const char *</code><i>file</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> New applications should use the POSIX.1-specified &quot;utmpx&quot; versions of these functions; see CONFORMING TO. </p>
<p> <code>utmpname</code>() sets the name of the utmp-format file for the other utmp functions to access. If <code>utmpname</code>() is not used to set the filename before the other functions are used, they assume <code>_PATH_UTMP</code>, as defined in <i>&lt;paths.h&gt;</i>. </p>
<p> <code>setutent</code>() rewinds the file pointer to the beginning of the utmp file. It is generally a good idea to call it before any of the other functions. </p>
<p> <code>endutent</code>() closes the utmp file. It should be called when the user code is done accessing the file with the other functions. </p>
<p> <code>getutent</code>() reads a line from the current file position in the utmp file. It returns a pointer to a structure containing the fields of the line. The definition of this structure is shown in <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5). </p>
<p> <code>getutid</code>() searches forward from the current file position in the utmp file based upon <i>ut</i>. If <i>ut-&gt;ut_type</i> is one of <code>RUN_LVL</code>, <code>BOOT_TIME</code>, <code>NEW_TIME</code>, or <code>OLD_TIME</code>, <code>getutid</code>() will find the first entry whose <i>ut_type</i> field matches <i>ut-&gt;ut_type</i>. If <i>ut-&gt;ut_type</i> is one of <code>INIT_PROCESS</code>, <code>LOGIN_PROCESS</code>, <code>USER_PROCESS</code>, or <code>DEAD_PROCESS</code>, <code>getutid</code>() will find the first entry whose <i>ut_id</i> field matches <i>ut-&gt;ut_id</i>. </p>
<p> <code>getutline</code>() searches forward from the current file position in the utmp file. It scans entries whose <i>ut_type</i> is <code>USER_PROCESS</code> or <code>LOGIN_PROCESS</code> and returns the first one whose <i>ut_line</i> field matches <i>ut-&gt;ut_line</i>. </p>
<p> <code>pututline</code>() writes the <i>utmp</i> structure <i>ut</i> into the utmp file. It uses <code>getutid</code>() to search for the proper place in the file to insert the new entry. If it cannot find an appropriate slot for <i>ut</i>, <code>pututline</code>() will append the new entry to the end of the file.</p>
<h2>RETURN VALUE</h2>
<p> <code>getutent</code>(), <code>getutid</code>(), and <code>getutline</code>() return a pointer to a <i>struct utmp</i> on success, and NULL on failure (which includes the &quot;record not found&quot; case). This <i>struct utmp</i> is allocated in static storage, and may be overwritten by subsequent calls. </p>
<p> On success <code>pututline</code>() returns <i>ut</i>; on failure, it returns NULL. </p>
<p> <code>utmpname</code>() returns 0 if the new name was successfully stored, or -1 on failure. </p>
<p> In the event of an error, these functions <i>errno</i> set to indicate the cause.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>ESRCH</code></p>
<dd> Record not found.</dl>
<p> <code>setutent</code>(), <code>pututline</code>(), and the <code>getut*</code>() functions can also fail for the reasons described in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<h2>FILES</h2>
<dl>
<dt><i>/var/run/utmp</i></p>
<dd> database of currently logged-in users</p>
<dt><i>/var/log/wtmp</i></p>
<dd> database of past user logins</dl>
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
<td> <code>getutent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe init race:utent<br />
 race:utentbuf sig:ALRM timer
</td>
</tr>
<tr VALIGN=top>
<td> <code>getutid</code>(),<br />
 <code>getutline</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe init race:utent<br />
 sig:ALRM timer
</td>
</tr>
<tr VALIGN=top>
<td> <code>pututline</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:utent<br />
 sig:ALRM timer
</td>
</tr>
<tr VALIGN=top>
<td> <code>setutent</code>(),<br />
 <code>endutent</code>(),<br />
 <code>utmpname</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:utent
</td>
</tr>
</table>
<p> In the above table, <i>utent</i> in <i>race:utent</i> signifies that if any of the functions <code>setutent</code>(), <code>getutent</code>(), <code>getutid</code>(), <code>getutline</code>(), <code>pututline</code>(), <code>utmpname</code>(), or <code>endutent</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>CONFORMING TO</h2>
<p> XPG2, SVr4. </p>
<p> In XPG2 and SVID 2 the function <code>pututline</code>() is documented to return void, and that is what it does on many systems (AIX, HP-UX). HP-UX introduces a new function <code>_pututline</code>() with the prototype given above for <code>pututline</code>(). </p>
<p> All these functions are obsolete now on non-Linux systems. POSIX.1-2001 and POSIX.1-2008, following SUSv1, does not have any of these functions, but instead uses </p>
<dl>
<dt>
<dd> <code>#include &lt;utmpx.h&gt;</code> </p>
<p> <code>struct utmpx *getutxent(void);</code> <code>struct utmpx *getutxid(const struct utmpx *);</code> <code>struct utmpx *getutxline(const struct utmpx *);</code> <code>struct utmpx *pututxline(const struct utmpx *);</code> <code>void setutxent(void);</code> <code>void endutxent(void);</code></dl>
<p> These functions are provided by glibc, and perform the same task as their equivalents without the &quot;x&quot;, but use <i>struct utmpx</i>, defined on Linux to be the same as <i>struct utmp</i>. For completeness, glibc also provides <code>utmpxname</code>(), although this function is not specified by POSIX.1. </p>
<p> On some other systems, the <i>utmpx</i> structure is a superset of the <i>utmp</i> structure, with additional fields, and larger versions of the existing fields, and parallel files are maintained, often <i>/var/*/utmpx</i> and <i>/var/*/wtmpx</i>. </p>
<p> Linux glibc on the other hand does not use a parallel <i>utmpx</i> file since its <i>utmp</i> structure is already large enough. The &quot;x&quot; functions listed above are just aliases for their counterparts without the &quot;x&quot; (e.g., <code>getutxent</code>() is an alias for <code>getutent</code>()).</p>
<h2>NOTES</h2>
<h3>Glibc notes</h3>
<p> The above functions are not thread-safe. Glibc adds reentrant versions </p>
<pre><code>
#include &lt;utmp.h&gt;
int getutent_r(struct utmp *ubuf, struct utmp **ubufp);
int getutid_r(struct utmp *ut,
              struct utmp *ubuf, struct utmp **ubufp);
int getutline_r(struct utmp *ut,
                struct utmp *ubuf, struct utmp **ubufp);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getutent_r</code>(), <code>getutid_r</code>(), <code>getutline_r</code>(): </p>
<pre><code>
_GNU_SOURCE
|| /* since glibc 2.19: */ _DEFAULT_SOURCE || /* glibc &lt;= 2.19: */ _SVID_SOURCE || _BSD_SOURCE
</code></pre>
<p> These functions are GNU extensions, analogs of the functions of the same name without the _r suffix. The <i>ubuf</i> argument gives these functions a place to store their result. On success, they return 0, and a pointer to the result is written in <i>*ubufp</i>. On error, these functions return -1. There are no utmpx equivalents of the above functions. (POSIX.1 does not specify such functions.)</p>
<h2>EXAMPLES</h2>
<p> The following example adds and removes a utmp record, assuming it is run from within a pseudo terminal. For usage in a real application, you should check the return values of <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3) and <code><a href="/docs/linux/man/3-ttyname/">ttyname</a></code>(3). </p>
<p> #include &lt;string.h&gt; #include &lt;stdlib.h&gt; #include &lt;pwd.h&gt; #include &lt;unistd.h&gt; #include &lt;utmp.h&gt; #include &lt;time.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct utmp entry; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;system(&quot;echo before adding entry:;who&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;entry.ut_type&nbsp;=&nbsp;USER_PROCESS;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;entry.ut_pid&nbsp;=&nbsp;getpid();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strcpy(entry.ut_line, ttyname(STDIN_FILENO)&nbsp;+&nbsp;strlen(&quot;/dev/&quot;));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;only correct for ptys named&nbsp;/dev/tty[pqr][0-9a-z]&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strcpy(entry.ut_id, ttyname(STDIN_FILENO)&nbsp;+&nbsp;strlen(&quot;/dev/tty&quot;));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time(&amp;entry.ut_time);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strcpy(entry.ut_user, getpwuid(getuid())-&gt;pw_name);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(entry.ut_host, 0, UT_HOSTSIZE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;entry.ut_addr&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setutent();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pututline(&amp;entry); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;system(&quot;echo after adding entry:;who&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;entry.ut_type&nbsp;=&nbsp;DEAD_PROCESS;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(entry.ut_line, 0, UT_LINESIZE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;entry.ut_time&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(entry.ut_user, 0, UT_NAMESIZE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setutent();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pututline(&amp;entry); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;system(&quot;echo after removing entry:;who&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;endutent();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getutmp/">getutmp</a></code>(3), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
