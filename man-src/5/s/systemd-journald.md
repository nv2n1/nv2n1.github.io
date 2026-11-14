---
title: "systemd-journald(5)"
name: "systemd-journald"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-journald/"
description: "systemd-journald.conf – Journal service configuration file"
---

<p>systemd-journald.conf &#8211; Journal service configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/systemd-journald.conf</p>
<h2>Description</h2>
<p>This files configures various parameters of the systemd journal service <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8).</p>
<h2>Options</h2>
<p>All options are configured in the [Journal] section: </p>
<p> <i>Compress=</i></p>
<dl>
<dd>Takes a boolean value. If enabled (the default) data objects that shall be stored in the journal and are larger than a certain threshold are compressed with the XZ compression algorithm before they are written to the file system.</dl>
<p> <i>RateLimitInterval=</i>, <i>RateLimitBurst=</i></p>
<dl>
<dd>Configures the rate limiting that is applied to all messages generated on the system. If in the time interval defined by <i>RateLimitInterval=</i> more messages than specified in <i>RateLimitBurst=</i> are logged by a service all further messages within the interval are dropped, until the interval is over. A message about the number of dropped messages is generated. This rate limiting is applied per-service, so that two services which log do not interfere with each other&#8217;s limit. Defaults to 100 messages in 10s. The time specification for <i>RateLimitInterval=</i> may be specified in the following units: s, min, h, ms, us. To turn off any kind of rate limiting, set either value to 0.</dl>
<p> <i>SystemMaxUse=</i>, <i>SystemKeepFree=</i>, <i>SystemMaxFileSize=</i>, <i>SystemMinFileSize=</i>, <i>RuntimeMaxUse=</i>, <i>RuntimeKeepFree=</i>, <i>RuntimeMaxFileSize=</i>, <i>RuntimeMinFileSize=</i></p>
<dl>
<dd>Enforce size limits on the journal files stored. The options prefixed with System apply to the journal files when stored on a persistent file system, more specifically /var/log/journal. The options prefixed with Runtime apply to the journal files when stored on a volatile in-memory file system, more specifically /run/log/journal. The former is used only when /var is mounted, writable and the directory /var/log/journal exists. Otherwise only the latter applies. Note that this means that during early boot and if the administrator disabled persistent logging only the latter options apply, while the former apply if persistent logging is enabled and the system is fully booted up. <i>SystemMaxUse=</i> and <i>RuntimeMaxUse=</i> control how much disk space the journal may use up at maximum. Defaults to 10% of the size of the respective file system. <i>SystemKeepFree=</i> and <i>RuntimeKeepFree=</i> control how much disk space the journal shall always leave free for other uses if less than the disk space configured in <i>SystemMaxUse=</i> and <i>RuntimeMaxUse=</i> is available. Defaults to 5% of the size of the respective file system. <i>SystemMaxFileSize=</i> and <i>RuntimeMaxFileSize=</i> control how large individual journal files may grow at maximum. This influences the granularity in which disk space is made available through rotation, i.e. deletion of historic data. Defaults to one eigth of the values configured with <i>SystemMaxUse=</i> and <i>RuntimeMaxUse=</i>, so that usually seven rotated journal files are kept as history. <i>SystemMinFileSize=</i> and <i>RuntimeMinFileSize=</i> control how large individual journal files grow at minimum. Defaults to 64K. Specify values in bytes or use K, M, G, T, P, E as units for the specified sizes. Note that size limits are enforced synchronously to journal files as they are extended, and need no explicit rotation step triggered by time.</dl>
<p> <i>ForwardToSyslog=</i>, <i>ForwardToKMsg=</i>, <i>ForwardToConsole=</i></p>
<dl>
<dd>Control whether log messages received by the journal daemon shall be forwarded to a traditional syslog daemon, to the kernel log buffer (kmsg), or to the system console. These options take boolean arguments. If forwarding to syslog is enabled but no syslog daemon is running the respective option has no effect. By default only forwarding to syslog is enabled. These settings may be overridden at boot time with the kernel command line options systemd_journald.forward_to_syslog=, systemd_journald.forward_to_kmsg= and systemd_journald.forward_to_console=. If forwarding to the kernel log buffer and <i>ImportKernel=</i> is enabled at the same time care is taken to avoid logging loops. It is safe to use these options in combination.</dl>
<p> <i>MaxLevelStore=</i>, <i>MaxLevelSyslog=</i>, <i>MaxLevelKMsg=</i>, <i>MaxLevelConsole=</i></p>
<dl>
<dd>Controls the maximum log level of messages that are stored on disk, forwarded to syslog, kmsg or the console (if that is enabled, see above). As argument, takes one of emerg, alert, crit, err, warning, notice, info, debug or integer values in the range of 0..7 (corresponding to the same levels). Messages equal or below the log level specified are stored/forwarded, messages above are dropped. Defaults to debug for <i>MaxLevelStore=</i> and <i>MaxLevelSyslog=</i>, to ensure that the all messages are written to disk and forwarded to syslog. Defaults to notice for <i>MaxLevelKMsg=</i> and info for <i>MaxLevelConsole=</i>.</dl>
<p> <i>TTYPath=</i></p>
<dl>
<dd>Change the console TTY to use if <i>ForwardToConsole=yes</i> is used. Defaults to /dev/console.</dl>
<p> <i>ImportKernel=</i></p>
<dl>
<dd>Controls whether kernel log messages shall be stored in the journal. Takes a boolean argument and defaults to enabled. Note that currently only one userspace service can read kernel messages at a time, which means that kernel log message reading might get corrupted if it is enabled in more than one service, for example in both the journal and a traditional syslog service.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/5-systemd-conf/">systemd.conf</a></code>(5)</p>
<h2>Author</h2>
<p><code>Lennart Poettering</code> &lt;lennart [at] poettering.net&gt;</p>
<dl>
<dd>Developer</dl>
