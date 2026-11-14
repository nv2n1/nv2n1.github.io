---
title: "sd_journal_suppress_location(3)"
name: "sd_journal_suppress_location"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_suppress_location/"
---

sd_journal_print, sd_journal_printv, sd_journal_send, sd_journal_sendv, sd_journal_perror, SD_JOURNAL_SUPPRESS_LOCATION - Submit log entries to the journal 

<h2>Synopsis</h2><pre>#include &lt;systemd/sd-journal.h&gt;</pre><dl COMPACT><dt> <b>int sd_journal_print(int&nbsp;<wbr></b><i>priority</i><b>, const char&nbsp;<wbr>*</b><i>format</i><b>, ...);</b>
<dt> <b>int sd_journal_printv(int&nbsp;<wbr></b><i>priority</i><b>, const char&nbsp;<wbr>*</b><i>format</i><b>, va_list&nbsp;<wbr></b><i>ap</i><b>);</b>
<dt> <b>int sd_journal_send(const char&nbsp;<wbr>*</b><i>format</i><b>, ...);</b>
<dt> <b>int sd_journal_sendv(const struct iovec&nbsp;<wbr>*</b><i>iov</i><b>, int&nbsp;<wbr></b><i>n</i><b>);</b>
<dt> <b>int sd_journal_perror(const char&nbsp;<wbr>*</b><i>message</i><b>);</b></dl><h2>Description</h2><b>sd_journal_print()</b>
<dd>may be used to submit simple, plain text log entries to the system journal. The first argument is a priority value. This is followed by a format string and its parameters, similar to <b><a HREF="/docs/linux/man/3-printf/">printf</a></b>(3) or <b><a HREF="/docs/linux/man/3-syslog/">syslog</a></b>(3). The priority value is one of <b>LOG_EMERG</b>, <b>LOG_ALERT</b>, <b>LOG_CRIT</b>, <b>LOG_ERR</b>, <b>LOG_WARNING</b>, <b>LOG_NOTICE</b>, <b>LOG_INFO</b>, <b>LOG_DEBUG</b>, as defined in syslog.h, see <b><a HREF="/docs/linux/man/3-syslog/">syslog</a></b>(3) for details. It is recommended to use this call to submit log messages in the application locale or system locale and in UTF-8 format, but no such restrictions are enforced. 

 <b>sd_journal_printv()</b> is similar to <b>sd_journal_print()</b> but takes a variable argument list encapsulated in an object of type <i>va_list</i> (see <b><a HREF="/docs/linux/man/3-stdarg/">stdarg</a></b>(3) for more information) instead of the format string. It is otherwise equivalent in behavior. 

 <b>sd_journal_send()</b> may be used to submit structured log entries to the system journal. It takes a series of format strings, each immediately followed by their associated parameters, terminated by <b>NULL</b>. The strings passed should be of the format &quot;VARIABLE=value&quot;. The variable name must be in uppercase and consist only of characters, numbers and underscores, and may not begin with an underscore. (All assignments that do not follow this syntax will be ignored.) The value can be of any size and format. It is highly recommended to submit text strings formatted in the UTF-8 character encoding only, and submit binary fields only when formatting in UTF-8 strings is not sensible. A number of well known fields are defined, see <b><a HREF="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></b>(7) for details, but additional application defined fields may be used. A variable may be assigned more than one value per entry. 

 <b>sd_journal_sendv()</b> is similar to <b>sd_journal_send()</b> but takes an array of <i>struct iovec</i> (as defined in uio.h, see <b><a HREF="/docs/linux/man/3-readv/">readv</a></b>(3) for details) instead of the format string. Each structure should reference one field of the entry to submit. The second argument specifies the number of structures in the array. <b>sd_journal_sendv()</b> is particularly useful to submit binary objects to the journal where that is necessary. 

 <b>sd_journal_perror()</b> is a similar to <b><a HREF="/docs/linux/man/3-perror/">perror</a></b>(3) and writes a message to the journal that consists of the passed string, suffixed with &quot;: &quot; and a human readable representation of the current error code stored in <b><a HREF="/docs/linux/man/3-errno/">errno</a></b>(3). If the message string is passed as <b>NULL</b> or empty string, only the error string representation will be written, prefixed with nothing. An additional journal field ERRNO= is included in the entry containing the numeric error code formatted as decimal string. The log priority used is <b>LOG_ERR</b> (3). 

 Note that <b>sd_journal_send()</b> is a wrapper around <b>sd_journal_sendv()</b> to make it easier to use when only text strings shall be submitted. Also, the following two calls are mostly equivalent: 

<dl COMPACT><dd><pre>sd_journal_print(LOG_INFO, &quot;Hello World, this is PID %lu!&quot;, (unsigned long) getpid());
sd_journal_send(&quot;MESSAGE=Hello World, this is PID %lu!&quot;, (unsigned long) getpid(),
 &quot;PRIORITY=%i&quot;, LOG_INFO,
 NULL);</pre></dl>
 

 Note that these calls implicitly add fields for the source file, function name and code line where invoked. This is implemented with macros. If this is not desired, it can be turned off by defining SD_JOURNAL_SUPPRESS_LOCATION before including sd-journal.h. 

 <b><a HREF="/docs/linux/man/3-syslog/">syslog</a></b>(3) and <b>sd_journal_print()</b> may largely be used interchangeably functionality-wise. However, note that log messages logged via the former take a different path to the journal server than the later, and hence global chronological ordering between the two streams cannot be guaranteed. Using <b>sd_journal_print()</b> has the benefit of logging source code line, filenames, and functions as metadata along all entries, and guaranteeing chronological ordering with structured log entries that are generated via <b>sd_journal_send()</b>. Using <b>syslog()</b> has the benefit of being more portable.
<h2>Return Value</h2>The four calls return 0 on success or a negative errno-style error code. The <b><a HREF="/docs/linux/man/3-errno/">errno</a></b>(3) variable itself is not altered. 

 If <b><a HREF="/docs/linux/man/8-systemd-journald/">systemd-journald</a></b>(8) is not running (the socket is not present), those functions do nothing, and also return 0.
<h2>Async Signal Safety</h2><b>sd_journal_sendv()</b> is &quot;async signal safe&quot; in the meaning of <b><a HREF="/docs/linux/man/7-signal/">signal</a></b>(7). 

 <b>sd_journal_print</b>, <b>sd_journal_printv</b>, <b>sd_journal_send</b>, and <b>sd_journal_perror</b> are not async signal safe.
<h2>Notes</h2>The <b>sd_journal_print()</b>, <b>sd_journal_printv()</b>, <b>sd_journal_send()</b> and <b>sd_journal_sendv()</b> interfaces are available as a shared library, which can be compiled and linked to with the <b>libsystemd</b>&nbsp;<wbr><b><a HREF="/docs/linux/man/1-pkg-config/">pkg-config</a></b>(1) file.
<h2>See Also</h2><b><a HREF="/docs/linux/man/1-systemd/">systemd</a></b>(1), <b><a HREF="/docs/linux/man/3-sd-journal/">sd-journal</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_stream_fd/">sd_journal_stream_fd</a></b>(3), <b><a HREF="/docs/linux/man/3-syslog/">syslog</a></b>(3), <b><a HREF="/docs/linux/man/3-perror/">perror</a></b>(3), <b><a HREF="/docs/linux/man/3-errno/">errno</a></b>(3), <b><a HREF="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></b>(7), <b><a HREF="/docs/linux/man/7-signal/">signal</a></b>(7), <b><a HREF="/docs/linux/man/7-socket/">socket</a></b>(7)
