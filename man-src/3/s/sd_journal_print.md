---
title: "sd_journal_print(3)"
name: "sd_journal_print"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_print/"
description: "sd_journal_print, sd_journal_printv, sd_journal_send, sd_journal_sendv, sd_journal_perror, SD_JOURNAL_SUPPRESS_LOCATION – Submit log entries to the journal"
---

<p>sd_journal_print, sd_journal_printv, sd_journal_send, sd_journal_sendv, sd_journal_perror, SD_JOURNAL_SUPPRESS_LOCATION &#8211; Submit log entries to the journal</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_print(int priority, const char *format, ...);

int sd_journal_printv(int priority, const char *format, va_list ap);

int sd_journal_send(const char *format, ...);

int sd_journal_sendv(const struct iovec *iov, int n);

int sd_journal_perror(const char *message);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_print()</code></p>
<dd>may be used to submit simple, plain text log entries to the system journal. The first argument is a priority value. This is followed by a format string and its parameters, similar to <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) or <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). The priority value is one of <code>LOG_EMERG</code>, <code>LOG_ALERT</code>, <code>LOG_CRIT</code>, <code>LOG_ERR</code>, <code>LOG_WARNING</code>, <code>LOG_NOTICE</code>, <code>LOG_INFO</code>, <code>LOG_DEBUG</code>, as defined in syslog.h, see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for details. It is recommended to use this call to submit log messages in the application locale or system locale and in UTF-8 format, but no such restrictions are enforced. <code>sd_journal_printv()</code> is similar to <code>sd_journal_print()</code> but takes a variable argument list encapsulated in an object of type <i>va_list</i> (see <code><a href="/docs/linux/man/3-stdarg/">stdarg</a></code>(3) for more information) instead of the format string. It is otherwise equivalent in behavior. <code>sd_journal_send()</code> may be used to submit structured log entries to the system journal. It takes a series of format strings, each immediately followed by their associated parameters, terminated by <code>NULL</code>. The strings passed should be of the format &quot;VARIABLE=value&quot;. The variable name must be in uppercase and consist only of characters, numbers and underscores, and may not begin with an underscore. (All assignments that do not follow this syntax will be ignored.) The value can be of any size and format. It is highly recommended to submit text strings formatted in the UTF-8 character encoding only, and submit binary fields only when formatting in UTF-8 strings is not sensible. A number of well known fields are defined, see <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7) for details, but additional application defined fields may be used. A variable may be assigned more than one value per entry. <code>sd_journal_sendv()</code> is similar to <code>sd_journal_send()</code> but takes an array of <i>struct iovec</i> (as defined in uio.h, see <code><a href="/docs/linux/man/3-readv/">readv</a></code>(3) for details) instead of the format string. Each structure should reference one field of the entry to submit. The second argument specifies the number of structures in the array. <code>sd_journal_sendv()</code> is particularly useful to submit binary objects to the journal where that is necessary. <code>sd_journal_perror()</code> is a similar to <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3) and writes a message to the journal that consists of the passed string, suffixed with &quot;: &quot; and a human readable representation of the current error code stored in <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3). If the message string is passed as <code>NULL</code> or empty string, only the error string representation will be written, prefixed with nothing. An additional journal field ERRNO= is included in the entry containing the numeric error code formatted as decimal string. The log priority used is <code>LOG_ERR</code> (3). Note that <code>sd_journal_send()</code> is a wrapper around <code>sd_journal_sendv()</code> to make it easier to use when only text strings shall be submitted. Also, the following two calls are mostly equivalent: </p>
<pre><code>sd_journal_print(LOG_INFO, &quot;Hello World, this is PID %lu!&quot;, (unsigned long) getpid());

sd_journal_send(&quot;MESSAGE=Hello World, this is PID %lu!&quot;, (unsigned long) getpid(),
&quot;PRIORITY=%i&quot;, LOG_INFO,
NULL);</code></pre>
<p> Note that these calls implicitly add fields for the source file, function name and code line where invoked. This is implemented with macros. If this is not desired, it can be turned off by defining SD_JOURNAL_SUPPRESS_LOCATION before including sd-journal.h. <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) and <code>sd_journal_print()</code> may largely be used interchangeably functionality-wise. However, note that log messages logged via the former take a different path to the journal server than the later, and hence global chronological ordering between the two streams cannot be guaranteed. Using <code>sd_journal_print()</code> has the benefit of logging source code line, filenames, and functions as metadata along all entries, and guaranteeing chronological ordering with structured log entries that are generated via <code>sd_journal_send()</code>. Using <code>syslog()</code> has the benefit of being more portable.</p>
<h2>Return Value</h2>
<p>The four calls return 0 on success or a negative errno-style error code. The <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3) variable itself is not altered. </p>
<p> If <code><a href="/docs/linux/man/8-systemd-journald/">systemd-journald</a></code>(8) is not running (the socket is not present), those functions do nothing, and also return 0.</p>
<h2>Async Signal Safety</h2>
<p><code>sd_journal_sendv()</code> is &quot;async signal safe&quot; in the meaning of <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). </p>
<p> <code>sd_journal_print</code>, <code>sd_journal_printv</code>, <code>sd_journal_send</code>, and <code>sd_journal_perror</code> are not async signal safe.</p>
<h2>Notes</h2>
<p>The <code>sd_journal_print()</code>, <code>sd_journal_printv()</code>, <code>sd_journal_send()</code> and <code>sd_journal_sendv()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_stream_fd/">sd_journal_stream_fd</a></code>(3), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) </p>
