---
title: "sd_emerg(3)"
name: "sd_emerg"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_emerg/"
description: "sd-daemon, SD_EMERG, SD_ALERT, SD_CRIT, SD_ERR, SD_WARNING, SD_NOTICE, SD_INFO, SD_DEBUG – APIs for new-style daemons"
---

<p>sd-daemon, SD_EMERG, SD_ALERT, SD_CRIT, SD_ERR, SD_WARNING, SD_NOTICE, SD_INFO, SD_DEBUG &#8211; APIs for new-style daemons </p>
<h2>Synopsis</h2>
<pre>
#include &lt;systemd/sd-daemon.h&gt;
</pre>
<dl COMPACT>
<dt> <code>pkg-config &#8211;cflags &#8211;libs libsystemd</code></dl>
<h2>Description</h2>
<dd>sd-daemon.h provide APIs for new-style daemons, as implemented by the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) init system. </p>
<p> See <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3), <code><a href="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></code>(3), <code><a href="/docs/linux/man/3-sd_watchdog_enabled/">sd_watchdog_enabled</a></code>(3) for more information about the functions implemented. In addition to these functions, a couple of logging prefixes are defined as macros: </p>
<dl COMPACT>
<dt>
<dd>
<pre>
#define SD_EMERG   &quot;&lt;0&gt;&quot;  /* system is unusable */
#define SD_ALERT   &quot;&lt;1&gt;&quot;  /* action must be taken immediately */
#define SD_CRIT    &quot;&lt;2&gt;&quot;  /* critical conditions */
#define SD_ERR     &quot;&lt;3&gt;&quot;  /* error conditions */
#define SD_WARNING &quot;&lt;4&gt;&quot;  /* warning conditions */
#define SD_NOTICE  &quot;&lt;5&gt;&quot;  /* normal but significant condition */
#define SD_INFO    &quot;&lt;6&gt;&quot;  /* informational */
#define SD_DEBUG   &quot;&lt;7&gt;&quot;  /* debug-level messages */
</pre>
</dl>
<p> These prefixes are intended to be used in conjunction with stderr-based logging as implemented by systemd. If a systemd service definition file is configured with <i>StandardError=journal</i>, <i>StandardError=syslog</i> or <i>StandardError=kmsg</i>, these prefixes can be used to encode a log level in lines printed. This is similar to the kernel <code>printk()</code>-style logging. See <code><a href="/docs/linux/man/2-klogctl/">klogctl</a></code>(2) for more information. </p>
<p> The log levels are identical to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3)&#8217;s log level system. To use these prefixes simply prefix every line with one of these strings. A line that is not prefixed will be logged at the default log level SD_INFO. </p>
<p> <code>Example 1. Hello World</code> </p>
<p> A daemon may log with the log level NOTICE by issuing this call: </p>
<dl COMPACT>
<dt>
<dd>
<pre>
fprintf(stderr, SD_NOTICE &quot;Hello World!
&quot;);
</pre>
</dl>
<h2>Notes</h2>
<p> These APIs are implemented as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3), <code><a href="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></code>(3), <code><a href="/docs/linux/man/3-sd_watchdog_enabled/">sd_watchdog_enabled</a></code>(3), <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/3-sd-readahead/">sd-readahead</a></code>(3), <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1)</p>
