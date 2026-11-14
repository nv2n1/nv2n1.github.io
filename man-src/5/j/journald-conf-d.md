---
title: "journald-conf-d(5)"
name: "journald-conf-d"
section: "5"
letter: "j"
url: "/docs/linux/man/5-journald-conf-d/"
description: "journald.conf, journald.conf.d, journald [at] .conf – Journal service configuration files"
---

<p>journald.conf, journald.conf.d, journald [at] .conf &#8211; Journal service configuration files</p>
<h2>Synopsis</h2>
<p>/etc/systemd/journald.conf </p>
<p> /etc/systemd/journald.conf.d/*.conf </p>
<p> /run/systemd/journald.conf.d/*.conf </p>
<p> /usr/lib/systemd/journald.conf.d/*.conf </p>
<p> /etc/systemd/journald@<i>NAMESPACE</i>.conf </p>
<p> /etc/systemd/journald@<i>NAMESPACE</i>.conf.d/*.conf </p>
<p> /run/systemd/journald@<i>NAMESPACE</i>.conf.d/*.conf </p>
<p> /usr/lib/systemd/journald@<i>NAMESPACE</i>.conf.d/*.conf</p>
<h2>Description</h2>
<p>These files configure various parameters of the systemd journal service, <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8). See <code><a href="/docs/linux/man/7-systemd-syntax/">systemd.syntax</a></code>(7) for a general description of the syntax. </p>
<p> The <code>systemd-journald</code> instance managing the default namespace is configured by /etc/systemd/journald.conf and associated drop-ins. Instances managing other namespaces read /etc/systemd/journald@<i>NAMESPACE</i>.conf and associated drop-ins with the namespace identifier filled in. This allows each namespace to carry a distinct configuration. See <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8) for details about journal namespaces.</p>
<h2>Configuration Directories And Precedence</h2>
<p>The default configuration is set during compilation, so configuration is only needed when it is necessary to deviate from those defaults. Initially, the main configuration file in /etc/systemd/ contains commented out entries showing the defaults as a guide to the administrator. Local overrides can be created by editing this file or by creating drop-ins, as described below. Using drop-ins for local configuration is recommended over modifications to the main configuration file. </p>
<p> In addition to the &quot;main&quot; configuration file, drop-in configuration snippets are read from /usr/lib/systemd/*.conf.d/, /usr/local/lib/systemd/*.conf.d/, and /etc/systemd/*.conf.d/. Those drop-ins have higher precedence and override the main configuration file. Files in the *.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of in which of the subdirectories they reside. When multiple files specify the same option, for options which accept just a single value, the entry in the file sorted last takes precedence, and for options which accept a list of values, entries are collected as they occur in the sorted files. </p>
<p> When packages need to customize the configuration, they can install drop-ins under /usr/. Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. Drop-ins have to be used to override package drop-ins, since the main configuration file has lower precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file.</p>
<h2>Options</h2>
<p>All options are configured in the [Journal] section: </p>
<p> <i>Storage=</i></p>
<dl>
<dd>Controls where to store journal data. One of &quot;volatile&quot;, &quot;persistent&quot;, &quot;auto&quot; and &quot;none&quot;. If &quot;volatile&quot;, journal log data will be stored only in memory, i.e. below the /run/log/journal hierarchy (which is created if needed). If &quot;persistent&quot;, data will be stored preferably on disk, i.e. below the /var/log/journal hierarchy (which is created if needed), with a fallback to /run/log/journal (which is created if needed), during early boot and if the disk is not writable. &quot;auto&quot; behaves like &quot;persistent&quot; if the /var/log/journal directory exists, and &quot;volatile&quot; otherwise (the existence of the directory controls the storage mode). &quot;none&quot; turns off all storage, all log data received will be dropped (but forwarding to other targets, such as the console, the kernel log buffer, or a syslog socket will still work). Defaults to &quot;auto&quot; in the default journal namespace, and &quot;persistent&quot; in all others. </p>
<p> Note that journald will initially use volatile storage, until a call to <code>journalctl &#8211;flush</code> (or sending <code>SIGUSR1</code> to journald) will cause it to switch to persistent logging (under the conditions mentioned above). This is done automatically on boot via &quot;systemd-journal-flush.service&quot;. </p>
<p> Note that when this option is changed to &quot;volatile&quot;, existing persistent data is not removed. In the other direction, <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) with the <code>&#8211;flush</code> option may be used to move volatile data to persistent storage.</dl>
<p> <i>Compress=</i></p>
<dl>
<dd>Can take a boolean value. If enabled (the default), data objects that shall be stored in the journal and are larger than the default threshold of 512 bytes are compressed before they are written to the file system. It can also be set to a number of bytes to specify the compression threshold directly. Suffixes like K, M, and G can be used to specify larger units.</dl>
<p> <i>Seal=</i></p>
<dl>
<dd>Takes a boolean value. If enabled (the default), and a sealing key is available (as created by <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1)&#8217;s <code>&#8211;setup-keys</code> command), Forward Secure Sealing (FSS) for all persistent journal files is enabled. FSS is based on m[blue]<code>Seekable Sequential Key Generators</code>m[]<font SIZE="-2">[1]</font> by G. A. Marson and B. Poettering (doi:10.1007/978-3-642-40203-6_7) and may be used to protect journal files from unnoticed alteration.</dl>
<p> <i>SplitMode=</i></p>
<dl>
<dd>Controls whether to split up journal files per user, either &quot;uid&quot; or &quot;none&quot;. Split journal files are primarily useful for access control: on UNIX/Linux access control is managed per file, and the journal daemon will assign users read access to their journal files. If &quot;uid&quot;, all regular users (with UID outside the range of system users, dynamic service users, and the nobody user) will each get their own journal files, and system users will log to the system journal. See m[blue]<code>Users, Groups, UIDs and GIDs on systemd systems</code>m[]<font SIZE="-2">[2]</font> for more details about UID ranges. If &quot;none&quot;, journal files are not split up by user and all messages are instead stored in the single system journal. In this mode unprivileged users generally do not have access to their own log data. Note that splitting up journal files by user is only available for journals stored persistently. If journals are stored on volatile storage (see <i>Storage=</i> above), only a single journal file is used. Defaults to &quot;uid&quot;.</dl>
<p> <i>RateLimitIntervalSec=</i>, <i>RateLimitBurst=</i></p>
<dl>
<dd>Configures the rate limiting that is applied to all messages generated on the system. If, in the time interval defined by <i>RateLimitIntervalSec=</i>, more messages than specified in <i>RateLimitBurst=</i> are logged by a service, all further messages within the interval are dropped until the interval is over. A message about the number of dropped messages is generated. This rate limiting is applied per-service, so that two services which log do not interfere with each other&#8217;s limits. Defaults to 10000 messages in 30s. The time specification for <i>RateLimitIntervalSec=</i> may be specified in the following units: &quot;s&quot;, &quot;min&quot;, &quot;h&quot;, &quot;ms&quot;, &quot;us&quot;. To turn off any kind of rate limiting, set either value to 0. </p>
<p> Note that the effective rate limit is multiplied by a factor derived from the available free disk space for the journal. Currently, this factor is calculated using the base 2 logarithm. </p>
<p> <code>Table 1. Example </code><i>RateLimitBurst=</i> rate modifications by the available disk space </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Available Disk Space </code></td>
<td><code> Burst Multiplier </code>
</td>
</tr>
<tr VALIGN=top>
<td> &lt;= 1MB </td>
<td> 1
</td>
</tr>
<tr VALIGN=top>
<td> &lt;= 16MB </td>
<td> 2
</td>
</tr>
<tr VALIGN=top>
<td> &lt;= 256MB </td>
<td> 3
</td>
</tr>
<tr VALIGN=top>
<td> &lt;= 4GB </td>
<td> 4
</td>
</tr>
<tr VALIGN=top>
<td> &lt;= 64GB </td>
<td> 5
</td>
</tr>
<tr VALIGN=top>
<td> &lt;= 1TB </td>
<td> 6
</td>
</tr>
</table>
<p> If a service provides rate limits for itself through <i>LogRateLimitIntervalSec=</i> and/or <i>LogRateLimitBurst=</i> in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), those values will override the settings specified here.</dl>
<p> <i>SystemMaxUse=</i>, <i>SystemKeepFree=</i>, <i>SystemMaxFileSize=</i>, <i>SystemMaxFiles=</i>, <i>RuntimeMaxUse=</i>, <i>RuntimeKeepFree=</i>, <i>RuntimeMaxFileSize=</i>, <i>RuntimeMaxFiles=</i></p>
<dl>
<dd>Enforce size limits on the journal files stored. The options prefixed with &quot;System&quot; apply to the journal files when stored on a persistent file system, more specifically /var/log/journal. The options prefixed with &quot;Runtime&quot; apply to the journal files when stored on a volatile in-memory file system, more specifically /run/log/journal. The former is used only when /var/ is mounted, writable, and the directory /var/log/journal exists. Otherwise, only the latter applies. Note that this means that during early boot and if the administrator disabled persistent logging, only the latter options apply, while the former apply if persistent logging is enabled and the system is fully booted up. <code>journalctl</code> and <code>systemd-journald</code> ignore all files with names not ending with &quot;.journal&quot; or &quot;.journal~&quot;, so only such files, located in the appropriate directories, are taken into account when calculating current disk usage. </p>
<p> <i>SystemMaxUse=</i> and <i>RuntimeMaxUse=</i> control how much disk space the journal may use up at most. <i>SystemKeepFree=</i> and <i>RuntimeKeepFree=</i> control how much disk space systemd-journald shall leave free for other uses. <code>systemd-journald</code> will respect both limits and use the smaller of the two values. </p>
<p> The first pair defaults to 10% and the second to 15% of the size of the respective file system, but each value is capped to 4G. If the file system is nearly full and either <i>SystemKeepFree=</i> or <i>RuntimeKeepFree=</i> are violated when systemd-journald is started, the limit will be raised to the percentage that is actually free. This means that if there was enough free space before and journal files were created, and subsequently something else causes the file system to fill up, journald will stop using more space, but it will not be removing existing files to reduce the footprint again, either. Also note that only archived files are deleted to reduce the space occupied by journal files. This means that, in effect, there might still be more space used than <i>SystemMaxUse=</i> or <i>RuntimeMaxUse=</i> limit after a vacuuming operation is complete. </p>
<p> <i>SystemMaxFileSize=</i> and <i>RuntimeMaxFileSize=</i> control how large individual journal files may grow at most. This influences the granularity in which disk space is made available through rotation, i.e. deletion of historic data. Defaults to one eighth of the values configured with <i>SystemMaxUse=</i> and <i>RuntimeMaxUse=</i>, so that usually seven rotated journal files are kept as history. </p>
<p> Specify values in bytes or use K, M, G, T, P, E as units for the specified sizes (equal to 1024, 1024&sup2;, &#8230; bytes). Note that size limits are enforced synchronously when journal files are extended, and no explicit rotation step triggered by time is needed. </p>
<p> <i>SystemMaxFiles=</i> and <i>RuntimeMaxFiles=</i> control how many individual journal files to keep at most. Note that only archived files are deleted to reduce the number of files until this limit is reached; active files will stay around. This means that, in effect, there might still be more journal files around in total than this limit after a vacuuming operation is complete. This setting defaults to 100.</dl>
<p> <i>MaxFileSec=</i></p>
<dl>
<dd>The maximum time to store entries in a single journal file before rotating to the next one. Normally, time-based rotation should not be required as size-based rotation with options such as <i>SystemMaxFileSize=</i> should be sufficient to ensure that journal files do not grow without bounds. However, to ensure that not too much data is lost at once when old journal files are deleted, it might make sense to change this value from the default of one month. Set to 0 to turn off this feature. This setting takes time values which may be suffixed with the units &quot;year&quot;, &quot;month&quot;, &quot;week&quot;, &quot;day&quot;, &quot;h&quot; or &quot;m&quot; to override the default time unit of seconds.</dl>
<p> <i>MaxRetentionSec=</i></p>
<dl>
<dd>The maximum time to store journal entries. This controls whether journal files containing entries older than the specified time span are deleted. Normally, time-based deletion of old journal files should not be required as size-based deletion with options such as <i>SystemMaxUse=</i> should be sufficient to ensure that journal files do not grow without bounds. However, to enforce data retention policies, it might make sense to change this value from the default of 0 (which turns off this feature). This setting also takes time values which may be suffixed with the units &quot;year&quot;, &quot;month&quot;, &quot;week&quot;, &quot;day&quot;, &quot;h&quot; or &quot; m&quot; to override the default time unit of seconds.</dl>
<p> <i>SyncIntervalSec=</i></p>
<dl>
<dd>The timeout before synchronizing journal files to disk. After syncing, journal files are placed in the OFFLINE state. Note that syncing is unconditionally done immediately after a log message of priority CRIT, ALERT or EMERG has been logged. This setting hence applies only to messages of the levels ERR, WARNING, NOTICE, INFO, DEBUG. The default timeout is 5 minutes.</dl>
<p> <i>ForwardToSyslog=</i>, <i>ForwardToKMsg=</i>, <i>ForwardToConsole=</i>, <i>ForwardToWall=</i></p>
<dl>
<dd>Control whether log messages received by the journal daemon shall be forwarded to a traditional syslog daemon, to the kernel log buffer (kmsg), to the system console, or sent as wall messages to all logged-in users. These options take boolean arguments. If forwarding to syslog is enabled but nothing reads messages from the socket, forwarding to syslog has no effect. By default, only forwarding to syslog and wall is enabled. These settings may be overridden at boot time with the kernel command line options &quot;systemd.journald.forward_to_syslog&quot;, &quot;systemd.journald.forward_to_kmsg&quot;, &quot;systemd.journald.forward_to_console&quot;, and &quot;systemd.journald.forward_to_wall&quot;. If the option name is specified without &quot;=&quot; and the following argument, true is assumed. Otherwise, the argument is parsed as a boolean. </p>
<p> When forwarding to the console, the TTY to log to can be changed with <i>TTYPath=</i>, described below. </p>
<p> When forwarding to the kernel log buffer (kmsg), make sure to select a suitably large size for the log buffer, for example by adding &quot;log_buf_len=8M&quot; to the kernel command line. <code>systemd</code> will automatically disable kernel&#8217;s rate-limiting applied to userspace processes (equivalent to setting &quot;printk.devkmsg=on&quot;).</dl>
<p> <i>MaxLevelStore=</i>, <i>MaxLevelSyslog=</i>, <i>MaxLevelKMsg=</i>, <i>MaxLevelConsole=</i>, <i>MaxLevelWall=</i></p>
<dl>
<dd>Controls the maximum log level of messages that are stored in the journal, forwarded to syslog, kmsg, the console or wall (if that is enabled, see above). As argument, takes one of &quot;emerg&quot;, &quot;alert&quot;, &quot;crit&quot;, &quot;err&quot;, &quot;warning&quot;, &quot;notice&quot;, &quot;info&quot;, &quot;debug&quot;, or integer values in the range of 0-7 (corresponding to the same levels). Messages equal or below the log level specified are stored/forwarded, messages above are dropped. Defaults to &quot;debug&quot; for <i>MaxLevelStore=</i> and <i>MaxLevelSyslog=</i>, to ensure that the all messages are stored in the journal and forwarded to syslog. Defaults to &quot;notice&quot; for <i>MaxLevelKMsg=</i>, &quot;info&quot; for <i>MaxLevelConsole=</i>, and &quot;emerg&quot; for <i>MaxLevelWall=</i>. These settings may be overridden at boot time with the kernel command line options &quot;systemd.journald.max_level_store=&quot;, &quot;systemd.journald.max_level_syslog=&quot;, &quot;systemd.journald.max_level_kmsg=&quot;, &quot;systemd.journald.max_level_console=&quot;, &quot;systemd.journald.max_level_wall=&quot;.</dl>
<p> <i>ReadKMsg=</i></p>
<dl>
<dd>Takes a boolean value. If enabled <code>systemd-journal</code> processes /dev/kmsg messages generated by the kernel. In the default journal namespace this option is enabled by default, it is disabled in all others.</dl>
<p> <i>Audit=</i></p>
<dl>
<dd>Takes a boolean value. If enabled <code>systemd-journal</code> will turn on kernel auditing on start-up. If disabled it will turn it off. If unset it will neither enable nor disable it, leaving the previous state unchanged. Note that this option does not control whether <code>systemd-journald</code> collects generated audit records, it just controls whether it tells the kernel to generate them. This means if another tool turns on auditing even if <code>systemd-journald</code> left it off, it will still collect the generated messages. Defaults to off.</dl>
<p> <i>TTYPath=</i></p>
<dl>
<dd>Change the console TTY to use if <i>ForwardToConsole=yes</i> is used. Defaults to /dev/console.</dl>
<p> <i>LineMax=</i></p>
<dl>
<dd>The maximum line length to permit when converting stream logs into record logs. When a systemd unit&#8217;s standard output/error are connected to the journal via a stream socket, the data read is split into individual log records at newline (&quot;
&quot;, ASCII 10) and <code>NUL</code> characters. If no such delimiter is read for the specified number of bytes a hard log record boundary is artificially inserted, breaking up overly long lines into multiple log records. Selecting overly large values increases the possible memory usage of the Journal daemon for each stream client, as in the worst case the journal daemon needs to buffer the specified number of bytes in memory before it can flush a new log record to disk. Also note that permitting overly large line maximum line lengths affects compatibility with traditional log protocols as log records might not fit anymore into a single <code>AF_UNIX</code> or <code>AF_INET</code> datagram. Takes a size in bytes. If the value is suffixed with K, M, G or T, the specified size is parsed as Kilobytes, Megabytes, Gigabytes, or Terabytes (with the base 1024), respectively. Defaults to 48K, which is relatively large but still small enough so that log records likely fit into network datagrams along with extra room for metadata. Note that values below 79 are not accepted and will be bumped to 79.</dl>
<h2>Forwarding To Traditional Syslog Daemons</h2>
<p>Journal events can be transferred to a different logging daemon in two different ways. With the first method, messages are immediately forwarded to a socket (/run/systemd/journal/syslog), where the traditional syslog daemon can read them. This method is controlled by the <i>ForwardToSyslog=</i> option. With a second method, a syslog daemon behaves like a normal journal client, and reads messages from the journal files, similarly to <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1). With this, messages do not have to be read immediately, which allows a logging daemon which is only started late in boot to access all messages since the start of the system. In addition, full structured meta-data is available to it. This method of course is available only if the messages are stored in a journal file at all. So it will not work if <i>Storage=none</i> is set. It should be noted that usually the <i>second</i> method is used by syslog daemons, so the <i>Storage=</i> option, and not the <i>ForwardToSyslog=</i> option, is relevant for them.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Seekable Sequential Key Generators</p>
<dl>
<dd><a rel="nofollow" href="https://eprint.iacr.org/2013/397">https://eprint.iacr.org/2013/397</a></dl>
<dt> 2.</p>
<dd>Users, Groups, UIDs and GIDs on systemd systems</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/UIDS-GIDS">https://systemd.io/UIDS-GIDS</a></dl>
