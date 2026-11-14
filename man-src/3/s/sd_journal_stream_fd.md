---
title: "sd_journal_stream_fd(3)"
name: "sd_journal_stream_fd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_stream_fd/"
description: "sd_journal_stream_fd – Create log stream file descriptor to the journal"
---

<p>sd_journal_stream_fd &#8211; Create log stream file descriptor to the journal </p>
<h2>Synopsis</h2>
<pre>
#include &lt;systemd/sd-journal.h&gt;
</pre>
<dl COMPACT>
<dt> <code>int sd_journal_stream_fd(const char&nbsp;<wbr>*</code><i>identifier</i><code>, int&nbsp;<wbr></code><i>priority</i><code>, int&nbsp;<wbr></code><i>level_prefix</i><code>);</code></dl>
<h2>Description</h2>
<p> <code>sd_journal_stream_fd()</code></p>
<dd>may be used to create a log stream file descriptor. Log messages written to this file descriptor as simple newline-separated text strings are written to the journal. This file descriptor can be used internally by applications or be made standard output or standard error of other processes executed. </p>
<p> <code>sd_journal_stream_fd()</code> takes a short program identifier string as first argument, which will be written to the journal as _SYSLOG_IDENTIFIER= field for each log entry (see <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7) for more information). The second argument shall be the default priority level for all messages. The priority level is one of <code>LOG_EMERG</code>, <code>LOG_ALERT</code>, <code>LOG_CRIT</code>, <code>LOG_ERR</code>, <code>LOG_WARNING</code>, <code>LOG_NOTICE</code>, <code>LOG_INFO</code>, <code>LOG_DEBUG</code>, as defined in syslog.h, see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for details. The third argument is a boolean: if true kernel-style log level prefixes (such as <code>SD_WARNING</code>) are interpreted, see <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3) for more information. </p>
<p> It is recommended that applications log UTF-8 messages only with this API, but this is not enforced.</p>
<h2>Return Value</h2>
<p> The call returns a valid write-only file descriptor on success or a negative errno-style error code.</p>
<h2>Notes</h2>
<p> The <code>sd_journal_stream_fd()</code> interface is available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>Examples</h2>
<p> Creating a log stream suitable for <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3): </p>
<dl COMPACT>
<dt>
<dd>
<pre>
#include &lt;syslog.h&gt;
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;unistd.h&gt;
#include &lt;systemd/sd-journal.h&gt;
#include &lt;systemd/sd-daemon.h&gt;
int main(int argc, char *argv[]) {
  int fd;
  FILE *log;
  fd = sd_journal_stream_fd(&quot;test&quot;, LOG_INFO, 1);
  if (fd &lt; 0) {
    fprintf(stderr, &quot;Failed to create stream fd: %s
&quot;, strerror(-fd));
    return 1;
  }
  log = fdopen(fd, &quot;w&quot;);
  if (!log) {
    fprintf(stderr, &quot;Failed to create file object: %m
&quot;);
    close(fd);
    return 1;
  }
  fprintf(log, &quot;Hello World!
&quot;);
  fprintf(log, SD_WARNING &quot;This is a warning!
&quot;);
  fclose(log);
  return 0;
}
</pre>
</dl>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_print/">sd_journal_print</a></code>(3), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7)</p>
