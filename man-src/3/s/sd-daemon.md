---
title: "sd-daemon(3)"
name: "sd-daemon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd-daemon/"
description: "sd-daemon, SD_EMERG, SD_ALERT, SD_CRIT, SD_ERR, SD_WARNING, SD_NOTICE, SD_INFO, SD_DEBUG – APIs for new-style daemons"
---

<p>sd-daemon, SD_EMERG, SD_ALERT, SD_CRIT, SD_ERR, SD_WARNING, SD_NOTICE, SD_INFO, SD_DEBUG &#8211; APIs for new-style daemons</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-daemon.h&gt;





pkg-config --cflags --libs libsystemd</code></pre>
<h2>Description</h2>
<dd>sd-daemon.h provide APIs for new-style daemons, as implemented by the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) init system. See <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3), <code><a href="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></code>(3), <code><a href="/docs/linux/man/3-sd_watchdog_enabled/">sd_watchdog_enabled</a></code>(3) for more information about the functions implemented. In addition to these functions, a couple of logging prefixes are defined as macros: fprintf(stderr, SD_NOTICE &quot;Hello World!
&quot;); These prefixes are intended to be used in conjunction with stderr-based logging as implemented by systemd. If a systemd service definition file is configured with <i>StandardError=journal</i>, <i>StandardError=syslog</i> or <i>StandardError=kmsg</i>, these prefixes can be used to encode a log level in lines printed. This is similar to the kernel <code>printk()</code>-style logging. See <code><a href="/docs/linux/man/2-klogctl/">klogctl</a></code>(2) for more information. The log levels are identical to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3)&#8217;s log level system. To use these prefixes simply prefix every line with one of these strings. A line that is not prefixed will be logged at the default log level SD_INFO. <code>Example 1. Hello World</code> A daemon may log with the log level NOTICE by issuing this call: </p>
<pre><code>fprintf(stderr, SD_NOTICE &quot;Hello World!
&quot;);</code></pre>
<h2>Notes</h2>
<p>These APIs are implemented as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3), <code><a href="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></code>(3), <code><a href="/docs/linux/man/3-sd_watchdog_enabled/">sd_watchdog_enabled</a></code>(3), <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/3-sd-readahead/">sd-readahead</a></code>(3), <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) </p>
