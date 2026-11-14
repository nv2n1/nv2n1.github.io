---
title: "vsyslog(3)"
name: "vsyslog"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vsyslog/"
description: "closelog, openlog, syslog, vsyslog – send messages to the system logger"
---

<p>closelog, openlog, syslog, vsyslog &#8211; send messages to the system logger</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;syslog.h&gt;
void openlog(const char *ident, int option, int facility);

void syslog(int priority, const char *format, ...);

void closelog(void);
void vsyslog(int priority, const char *format, va_list ap);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>vsyslog</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<h3>openlog()</h3>
<p><code>openlog</code>() opens a connection to the system logger for a program. </p>
<p> The string pointed to by <i>ident</i> is prepended to every message, and is typically set to the program name. If <i>ident</i> is NULL, the program name is used. (POSIX.1-2008 does not specify the behavior when <i>ident</i> is NULL.) </p>
<p> The <i>option</i> argument specifies flags which control the operation of <code>openlog</code>() and subsequent calls to <code>syslog</code>(). The <i>facility</i> argument establishes a default to be used if none is specified in subsequent calls to <code>syslog</code>(). The values that may be specified for <i>option</i> and <i>facility</i> are described below. </p>
<p> The use of <code>openlog</code>() is optional; it will automatically be called by <code>syslog</code>() if necessary, in which case <i>ident</i> will default to NULL.</p>
<h3>syslog() and vsyslog()</h3>
<p><code>syslog</code>() generates a log message, which will be distributed by <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). </p>
<p> The <i>priority</i> argument is formed by ORing together a <i>facility</i> value and a <i>level</i> value (described below). If no <i>facility</i> value is ORed into <i>priority</i>, then the default value set by <code>openlog</code>() is used, or, if there was no preceding <code>openlog</code>() call, a default of <code>LOG_USER</code> is employed. </p>
<p> The remaining arguments are a <i>format</i>, as in <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), and any arguments required by the <i>format</i>, except that the two-character sequence <code>%m</code> will be replaced by the error message string <i>strerror</i>(<i>errno</i>). The format string need not include a terminating newline character. </p>
<p> The function <code>vsyslog</code>() performs the same task as <code>syslog</code>() with the difference that it takes a set of arguments which have been obtained using the <code><a href="/docs/linux/man/3-stdarg/">stdarg</a></code>(3) variable argument list macros.</p>
<h3>closelog()</h3>
<p><code>closelog</code>() closes the file descriptor being used to write to the system logger. The use of <code>closelog</code>() is optional.</p>
<h3>Values for <i>option</i></h3>
<p>The <i>option</i> argument to <code>openlog</code>() is a bit mask constructed by ORing together any of the following values:</p>
<dl>
<dt><code>LOG_CONS</code></p>
<dd>Write directly to the system console if there is an error while sending to the system logger.</p>
<dt><code>LOG_NDELAY</code></p>
<dd>Open the connection immediately (normally, the connection is opened when the first message is logged). This may be useful, for example, if a subsequent <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) would make the pathname used internally by the logging facility unreachable.</p>
<dt><code>LOG_NOWAIT</code></p>
<dd>Don&#8217;t wait for child processes that may have been created while logging the message. (The GNU C library does not create a child process, so this option has no effect on Linux.)</p>
<dt><code>LOG_ODELAY</code></p>
<dd>The converse of <code>LOG_NDELAY</code>; opening of the connection is delayed until <code>syslog</code>() is called. (This is the default, and need not be specified.)</p>
<dt><code>LOG_PERROR</code></p>
<dd>(Not in POSIX.1-2001 or POSIX.1-2008.) Also log the message to <i>stderr</i>.</p>
<dt><code>LOG_PID</code></p>
<dd>Include the caller&#8217;s PID with each message.</dl>
<h3>Values for <i>facility</i></h3>
<p>The <i>facility</i> argument is used to specify what type of program is logging the message. This lets the configuration file specify that messages from different facilities will be handled differently.</p>
<dl>
<dt><code>LOG_AUTH</code></p>
<dd>security/authorization messages</p>
<dt><code>LOG_AUTHPRIV</code></p>
<dd>security/authorization messages (private)</p>
<dt><code>LOG_CRON</code></p>
<dd>clock daemon (<code>cron</code> and <code>at</code>)</p>
<dt><code>LOG_DAEMON</code></p>
<dd>system daemons without separate facility value</p>
<dt><code>LOG_FTP</code></p>
<dd>ftp daemon</p>
<dt><code>LOG_KERN</code></p>
<dd>kernel messages (these can&#8217;t be generated from user processes)</p>
<dt><code>LOG_LOCAL0</code> through <code>LOG_LOCAL7</code></p>
<dd>reserved for local use</p>
<dt><code>LOG_LPR</code></p>
<dd>line printer subsystem</p>
<dt><code>LOG_MAIL</code></p>
<dd>mail subsystem</p>
<dt><code>LOG_NEWS</code></p>
<dd>USENET news subsystem</p>
<dt><code>LOG_SYSLOG</code></p>
<dd>messages generated internally by <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8)</p>
<dt><code>LOG_USER</code> (default)</p>
<dd>generic user-level messages</p>
<dt><code>LOG_UUCP</code></p>
<dd>UUCP subsystem</dl>
<h3>Values for <i>level</i></h3>
<p>This determines the importance of the message. The levels are, in order of decreasing importance:</p>
<dl>
<dt><code>LOG_EMERG</code></p>
<dd>system is unusable</p>
<dt><code>LOG_ALERT</code></p>
<dd>action must be taken immediately</p>
<dt><code>LOG_CRIT</code></p>
<dd>critical conditions</p>
<dt><code>LOG_ERR</code></p>
<dd>error conditions</p>
<dt><code>LOG_WARNING</code></p>
<dd>warning conditions</p>
<dt><code>LOG_NOTICE</code></p>
<dd>normal, but significant, condition</p>
<dt><code>LOG_INFO</code></p>
<dd>informational message</p>
<dt><code>LOG_DEBUG</code></p>
<dd>debug-level message</dl>
<p> The function <code><a href="/docs/linux/man/3-setlogmask/">setlogmask</a></code>(3) can be used to restrict logging to specified levels only.</p>
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
<td> <code>openlog</code>(), <code>closelog</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>syslog</code>(), <code>vsyslog</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>The functions <code>openlog</code>(), <code>closelog</code>(), and <code>syslog</code>() (but not <code>vsyslog</code>()) are specified in SUSv2, POSIX.1-2001, and POSIX.1-2008. </p>
<p> POSIX.1-2001 specifies only the <code>LOG_USER</code> and <code>LOG_LOCAL*</code> values for <i>facility</i>. However, with the exception of <code>LOG_AUTHPRIV</code> and <code>LOG_FTP</code>, the other <i>facility</i> values appear on most UNIX systems. </p>
<p> The <code>LOG_PERROR</code> value for <i>option</i> is not specified by POSIX.1-2001 or POSIX.1-2008, but is available in most versions of UNIX.</p>
<h2>Notes</h2>
<p>The argument <i>ident</i> in the call of <code>openlog</code>() is probably stored as-is. Thus, if the string it points to is changed, <code>syslog</code>() may start prepending the changed string, and if the string it points to ceases to exist, the results are undefined. Most portable is to use a string constant. </p>
<p> Never pass a string with user-supplied data as a format, use the following instead: </p>
<p> syslog(priority, &quot;%s&quot;, string);</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1), <code><a href="/docs/linux/man/3-setlogmask/">setlogmask</a></code>(3), <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5), <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
