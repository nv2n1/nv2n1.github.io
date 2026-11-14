---
title: "journald(5)"
name: "journald"
section: "5"
letter: "j"
url: "/docs/linux/man/5-journald/"
description: "journald.conf – Journal service configuration file"
---

<p>journald.conf &#8211; Journal service configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/journald.conf</p>
<h2>Description</h2>
<p>This file configures various parameters of the systemd journal service, <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8).</p>
<h2>Options</h2>
<p>All options are configured in the &quot;[Journal]&quot; section: </p>
<p> <i>Storage=</i></p>
<dl>
<dd>Controls where to store journal data. One of &quot;volatile&quot;, &quot;persistent&quot;, &quot;auto&quot; and &quot;none&quot;. If &quot;volatile&quot;, journal log data will be stored only in memory, i.e. below the /run/log/journal hierarchy (which is created if needed). If &quot;persistent&quot;, data will be stored preferably on disk, i.e. below the /var/log/journal hierarchy (which is created if needed), with a fallback to /run/log/journal (which is created if needed), during early boot and if the disk is not writable. &quot;auto&quot; is similar to &quot;persistent&quot; but the directory /var/log/journal is not created if needed, so that its existence controls where log data goes. &quot;none&quot; turns off all storage, all log data received will be dropped. Forwarding to other targets, such as the console, the kernel log buffer or a syslog daemon will still work however. Defaults to &quot;auto&quot;.</dl>
<p> <i>Compress=</i></p>
<dl>
<dd>Takes a boolean value. If enabled (the default), data objects that shall be stored in the journal and are larger than a certain threshold are compressed with the XZ compression algorithm before they are written to the file system.</dl>
<p> <i>Seal=</i></p>
<dl>
<dd>Takes a boolean value. If enabled (the default), and a sealing key is available (as created by <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1)&#8217;s <code>&#8211;setup-keys</code> command), Forward Secure Sealing (FSS) for all persistent journal files is enabled. FSS is based on m[blue]<code>Seekable Sequential Key Generators</code>m[]<font SIZE="-2">[1]</font> by G. A. Marson and B. Poettering (doi:10.1007/978-3-642-40203-6_7) and may be used to protect journal files from unnoticed alteration.</dl>
<p> <i>SplitMode=</i></p>
<dl>
<dd>Controls whether to split up journal files per user. One of &quot;uid&quot;, &quot;login&quot; and &quot;none&quot;. If &quot;uid&quot;, all users will get each their own journal files regardless of whether they possess a login session or not, however system users will log into the system journal. If &quot;login&quot;, actually logged-in users will get each their own journal files, but users without login session and system users will log into the system journal. If &quot;none&quot;, journal files are not split up by user and all messages are instead stored in the single system journal. Note that splitting up journal files by user is only available for journals stored persistently. If journals are stored on volatile storage (see above), only a single journal file for all user IDs is kept. Defaults to &quot;uid&quot;.</dl>
<p> <i>RateLimitInterval=</i>, <i>RateLimitBurst=</i></p>
<dl>
<dd>Configures the rate limiting that is applied to all messages generated on the system. If, in the time interval defined by <i>RateLimitInterval=</i>, more messages than specified in <i>RateLimitBurst=</i> are logged by a service, all further messages within the interval are dropped until the interval is over. A message about the number of dropped messages is generated. This rate limiting is applied per-service, so that two services which log do not interfere with each other&#8217;s limits. Defaults to 1000 messages in 30s. The time specification for <i>RateLimitInterval=</i> may be specified in the following units: &quot;s&quot;, &quot;min&quot;, &quot;h&quot;, &quot;ms&quot;, &quot;us&quot;. To turn off any kind of rate limiting, set either value to 0.</dl>
<p> <i>SystemMaxUse=</i>, <i>SystemKeepFree=</i>, <i>SystemMaxFileSize=</i>, <i>RuntimeMaxUse=</i>, <i>RuntimeKeepFree=</i>, <i>RuntimeMaxFileSize=</i></p>
<dl>
<dd>Enforce size limits on the journal files stored. The options prefixed with &quot;System&quot; apply to the journal files when stored on a persistent file system, more specifically /var/log/journal. The options prefixed with &quot;Runtime&quot; apply to the journal files when stored on a volatile in-memory file system, more specifically /run/log/journal. The former is used only when /var is mounted, writable, and the directory /var/log/journal exists. Otherwise, only the latter applies. Note that this means that during early boot and if the administrator disabled persistent logging, only the latter options apply, while the former apply if persistent logging is enabled and the system is fully booted up. <code>journalctl</code> and <code>systemd-journald</code> ignore all files with names not ending with &quot;.journal&quot; or &quot;.journal~&quot;, so only such files, located in the appropriate directories, are taken into account when calculating current disk usage. </p>
<p> <i>SystemMaxUse=</i> and <i>RuntimeMaxUse=</i> control how much disk space the journal may use up at maximum. <i>SystemKeepFree=</i> and <i>RuntimeKeepFree=</i> control how much disk space systemd-journald shall leave free for other uses. <code>systemd-journald</code> will respect both limits and use the smaller of the two values. </p>
<p> The first pair defaults to 10% and the second to 15% of the size of the respective file system. If the file system is nearly full and either <i>SystemKeepFree=</i> or <i>RuntimeKeepFree=</i> is violated when systemd-journald is started, the value will be raised to percentage that is actually free. This means that if there was enough free space before and journal files were created, and subsequently something else causes the file system to fill up, journald will stop using more space, but it will not be removing existing files to go reduce footprint either. </p>
<p> <i>SystemMaxFileSize=</i> and <i>RuntimeMaxFileSize=</i> control how large individual journal files may grow at maximum. This influences the granularity in which disk space is made available through rotation, i.e. deletion of historic data. Defaults to one eighth of the values configured with <i>SystemMaxUse=</i> and <i>RuntimeMaxUse=</i>, so that usually seven rotated journal files are kept as history. Specify values in bytes or use K, M, G, T, P, E as units for the specified sizes (equal to 1024, 1024&sup2;,&#8230; bytes). Note that size limits are enforced synchronously when journal files are extended, and no explicit rotation step triggered by time is needed.</dl>
<p> <i>MaxFileSec=</i></p>
<dl>
<dd>The maximum time to store entries in a single journal file before rotating to the next one. Normally, time-based rotation should not be required as size-based rotation with options such as <i>SystemMaxFileSize=</i> should be sufficient to ensure that journal files do not grow without bounds. However, to ensure that not too much data is lost at once when old journal files are deleted, it might make sense to change this value from the default of one month. Set to 0 to turn off this feature. This setting takes time values which may be suffixed with the units &quot;year&quot;, &quot;month&quot;, &quot;week&quot;, &quot;day&quot;, &quot;h&quot; or &quot;m&quot; to override the default time unit of seconds.</dl>
<p> <i>MaxRetentionSec=</i></p>
<dl>
<dd>The maximum time to store journal entries. This controls whether journal files containing entries older then the specified time span are deleted. Normally, time-based deletion of old journal files should not be required as size-based deletion with options such as <i>SystemMaxUse=</i> should be sufficient to ensure that journal files do not grow without bounds. However, to enforce data retention policies, it might make sense to change this value from the default of 0 (which turns off this feature). This setting also takes time values which may be suffixed with the units &quot;year&quot;, &quot;month&quot;, &quot;week&quot;, &quot;day&quot;, &quot;h&quot; or &quot; m&quot; to override the default time unit of seconds.</dl>
<p> <i>SyncIntervalSec=</i></p>
<dl>
<dd>The timeout before synchronizing journal files to disk. After syncing, journal files are placed in the OFFLINE state. Note that syncing is unconditionally done immediately after a log message of priority CRIT, ALERT or EMERG has been logged. This setting hence applies only to messages of the levels ERR, WARNING, NOTICE, INFO, DEBUG. The default timeout is 5 minutes.</dl>
<p> <i>ForwardToSyslog=</i>, <i>ForwardToKMsg=</i>, <i>ForwardToConsole=</i>, <i>ForwardToWall=</i></p>
<dl>
<dd>Control whether log messages received by the journal daemon shall be forwarded to a traditional syslog daemon, to the kernel log buffer (kmsg), to the system console, or sent as wall messages to all logged-in users. These options take boolean arguments. If forwarding to syslog is enabled but no syslog daemon is running, the respective option has no effect. By default, only forwarding wall is enabled. These settings may be overridden at boot time with the kernel command line options &quot;systemd.journald.forward_to_syslog=&quot;, &quot;systemd.journald.forward_to_kmsg=&quot;, &quot;systemd.journald.forward_to_console=&quot; and &quot;systemd.journald.forward_to_wall=&quot;. When forwarding to the console, the TTY to log to can be changed with <i>TTYPath=</i>, described below.</dl>
<p> <i>MaxLevelStore=</i>, <i>MaxLevelSyslog=</i>, <i>MaxLevelKMsg=</i>, <i>MaxLevelConsole=</i>, <i>MaxLevelWall=</i></p>
<dl>
<dd>Controls the maximum log level of messages that are stored on disk, forwarded to syslog, kmsg, the console or wall (if that is enabled, see above). As argument, takes one of &quot;emerg&quot;, &quot;alert&quot;, &quot;crit&quot;, &quot;err&quot;, &quot;warning&quot;, &quot;notice&quot;, &quot;info&quot;, &quot;debug&quot; or integer values in the range of 0..7 (corresponding to the same levels). Messages equal or below the log level specified are stored/forwarded, messages above are dropped. Defaults to &quot;debug&quot; for <i>MaxLevelStore=</i> and <i>MaxLevelSyslog=</i>, to ensure that the all messages are written to disk and forwarded to syslog. Defaults to &quot;notice&quot; for <i>MaxLevelKMsg=</i>, &quot;info&quot; for <i>MaxLevelConsole=</i> and &quot;emerg&quot; for <i>MaxLevelWall=</i>.</dl>
<p> <i>TTYPath=</i></p>
<dl>
<dd>Change the console TTY to use if <i>ForwardToConsole=yes</i> is used. Defaults to /dev/console.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Seekable Sequential Key Generators</p>
<dl>
<dd><a rel="nofollow" href="https://eprint.iacr.org/2013/397">https://eprint.iacr.org/2013/397</a></dl>
