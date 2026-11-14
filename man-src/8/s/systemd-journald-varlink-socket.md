---
title: "systemd-journald-varlink-socket(8)"
name: "systemd-journald-varlink-socket"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-journald-varlink-socket/"
description: "systemd-journald.service, systemd-journald.socket, systemd-journald-dev-log.socket, systemd-journald-audit.socket, systemd-journald [at] .service, systemd-journald [at] .socket, systemd-journald-va..."
---

<p>systemd-journald.service, systemd-journald.socket, systemd-journald-dev-log.socket, systemd-journald-audit.socket, systemd-journald [at] .service, systemd-journald [at] .socket, systemd-journald-varlink [at] .socket, systemd-journald &#8211; Journal service</p>
<h2>Synopsis</h2>
<p>systemd-journald.service </p>
<p> systemd-journald.socket </p>
<p> systemd-journald-dev-log.socket </p>
<p> systemd-journald-audit.socket </p>
<p> systemd-journald [at] .service </p>
<p> systemd-journald [at] .socket </p>
<p> systemd-journald-varlink [at] .socket </p>
<p> /lib/systemd/systemd-journald</p>
<h2>Description</h2>
<p>systemd-journald is a system service that collects and stores logging data. It creates and maintains structured, indexed journals based on logging information that is received from a variety of sources: </p>
<dl>
<dd>&bull; Kernel log messages, via kmsg</dl>
<dl>
<dd>&bull; Simple system log messages, via the libc <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) call</dl>
<dl>
<dd>&bull; Structured system log messages via the native Journal API, see <code><a href="/docs/linux/man/3-sd_journal_print/">sd_journal_print</a></code>(3) and m[blue]<code>Native Journal Protocol</code>m[]<font SIZE="-2">[1]</font></dl>
<dl>
<dd>&bull; Standard output and standard error of service units. For further details see below.</dl>
<dl>
<dd>&bull; Audit records, originating from the kernel audit subsystem</dl>
<p> The daemon will implicitly collect numerous metadata fields for each log messages in a secure and unfakeable way. See <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7) for more information about the collected metadata. </p>
<p> Log data collected by the journal is primarily text-based but can also include binary data where necessary. Individual fields making up a log record stored in the journal may be up to 2^64-1 bytes in size. </p>
<p> The journal service stores log data either persistently below /var/log/journal or in a volatile way below /run/log/journal/ (in the latter case it is lost at reboot). By default, log data is stored persistently if /var/log/journal/ exists during boot, with an implicit fallback to volatile storage otherwise. Use <i>Storage=</i> in <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) to configure where log data is placed, independently of the existence of /var/log/journal/. </p>
<p> Note that journald will initially use volatile storage, until a call to <code>journalctl &#8211;flush</code> (or sending <code>SIGUSR1</code> to journald) will cause it to switch to persistent logging (under the conditions mentioned above). This is done automatically on boot via &quot;systemd-journal-flush.service&quot;. </p>
<p> On systems where /var/log/journal/ does not exist yet but where persistent logging is desired (and the default journald.conf is used), it is sufficient to create the directory, and ensure it has the correct access modes and ownership: </p>
<dl>
<dd>
<pre>mkdir -p /var/log/journal
systemd-tmpfiles --create --prefix /var/log/journal</pre>
</dl>
<p> See <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) for information about the configuration of this service.</p>
<h2>Stream Logging</h2>
<p>The systemd service manager invokes all service processes with standard output and standard error connected to the journal by default. This behaviour may be altered via the <i>StandardOutput=</i>/<i>StandardError=</i> unit file settings, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details. The journal converts the log byte stream received this way into individual log records, splitting the stream at newline (&quot;
&quot;, ASCII <code>10</code>) and <code>NUL</code> bytes. </p>
<p> If systemd-journald.service is stopped, the stream connections associated with all services are terminated. Further writes to those streams by the service will result in <code>EPIPE</code> errors. In order to react gracefully in this case it is recommended that programs logging to standard output/error ignore such errors. If the <code>SIGPIPE</code> UNIX signal handler is not blocked or turned off, such write attempts will also result in such process signals being generated, see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). To mitigate this issue, systemd service manager explicitly turns off the <code>SIGPIPE</code> signal for all invoked processes by default (this may be changed for each unit individually via the <i>IgnoreSIGPIPE=</i> option, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details). After the standard output/standard error streams have been terminated they may not be recovered until the services they are associated with are restarted. Note that during normal operation, systemd-journald.service stores copies of the file descriptors for those streams in the service manager. If systemd-journald.service is restarted using <code>systemctl restart</code> or equivalent operation instead of a pair of separate <code>systemctl stop</code> and <code>systemctl start</code> commands (or equivalent operations), these stream connections are not terminated and survive the restart. It is thus safe to restart systemd-journald.service, but stopping it is not recommended. </p>
<p> Note that the log record metadata for records transferred via such standard output/error streams reflect the metadata of the peer the stream was originally created for. If the stream connection is passed on to other processes (such as further child processes forked off the main service process), the log records will not reflect their metadata, but will continue to describe the original process. This is different from the other logging transports listed above, which are inherently record based and where the metadata is always associated with the individual record. </p>
<p> In addition to the implicit standard output/error logging of services, stream logging is also available via the <code><a href="/docs/linux/man/1-systemd-cat/">systemd-cat</a></code>(1) command line tool. </p>
<p> Currently, the number of parallel log streams systemd-journald will accept is limited to 4096. When this limit is reached further log streams may be established but will receive <code>EPIPE</code> right from the beginning.</p>
<h2>Journal Namespaces</h2>
<p>Journal &#8216;namespaces&#8217; are both a mechanism for logically isolating the log stream of projects consisting of one or more services from the rest of the system and a mechanism for improving performance. Multiple journal namespaces may exist simultaneously, each defining its own, independent log stream managed by its own instance of <code>systemd-journald</code>. Namespaces are independent of each other, both in the data store and in the IPC interface. By default only a single &#8216;default&#8217; namespace exists, managed by systemd-journald.service (and its associated socket units). Additional namespaces are created by starting an instance of the systemd-journald [at] .service service template. The instance name is the namespace identifier, which is a short string used for referencing the journal namespace. Service units may be assigned to a specific journal namespace through the <i>LogNamespace=</i> unit file setting, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details. The <code>&#8211;namespace=</code> switch of <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) may be used to view the log stream of a specific namespace. If the switch is not used the log stream of the default namespace is shown, i.e. log data from other namespaces is not visible. </p>
<p> Services associated with a specific log namespace may log via syslog, the native logging protocol of the journal and via stdout/stderr; the logging from all three transports is associated with the namespace. </p>
<p> By default only the default namespace will collect kernel and audit log messages. </p>
<p> The <code>systemd-journald</code> instance of the default namespace is configured through /etc/systemd/journald.conf (see below), while the other instances are configured through /etc/systemd/journald@<i>NAMESPACE</i>.conf. The journal log data for the default namespace is placed in /var/log/journal/<i>MACHINE_ID</i> (see below) while the data for the other namespaces is located in /var/log/journal/<i>MACHINE_ID</i>.<i>NAMESPACE</i>.</p>
<h2>Signals</h2>
<p>SIGUSR1</p>
<dl>
<dd>Request that journal data from /run/ is flushed to /var/ in order to make it persistent (if this is enabled). This must be used after /var/ is mounted, as otherwise log data from /run/ is never flushed to /var/ regardless of the configuration. Use the <code>journalctl &#8211;flush</code> command to request flushing of the journal files, and wait for the operation to complete. See <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) for details.</dl>
<p> SIGUSR2</p>
<dl>
<dd>Request immediate rotation of the journal files. Use the <code>journalctl &#8211;rotate</code> command to request journal file rotation, and wait for the operation to complete.</dl>
<p> SIGRTMIN+1</p>
<dl>
<dd>Request that all unwritten log data is written to disk. Use the <code>journalctl &#8211;sync</code> command to trigger journal synchronization, and wait for the operation to complete.</dl>
<h2>Kernel Command Line</h2>
<p>A few configuration parameters from journald.conf may be overridden on the kernel command line: </p>
<p> <i>systemd.journald.forward_to_syslog=</i>, <i>systemd.journald.forward_to_kmsg=</i>, <i>systemd.journald.forward_to_console=</i>, <i>systemd.journald.forward_to_wall=</i></p>
<dl>
<dd>Enables/disables forwarding of collected log messages to syslog, the kernel log buffer, the system console or wall. </p>
<p> See <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) for information about these settings.</dl>
<p> Note that these kernel command line options are only honoured by the default namespace, see above.</p>
<h2>Access Control</h2>
<p>Journal files are, by default, owned and readable by the &quot;systemd-journal&quot; system group but are not writable. Adding a user to this group thus enables them to read the journal files. </p>
<p> By default, each user, with a UID outside the range of system users, dynamic service users, and the nobody user, will get their own set of journal files in /var/log/journal/. See m[blue]<code>Users, Groups, UIDs and GIDs on systemd systems</code>m[]<font SIZE="-2">[2]</font> for more details about UID ranges. These journal files will not be owned by the user, however, in order to avoid that the user can write to them directly. Instead, file system ACLs are used to ensure the user gets read access only. </p>
<p> Additional users and groups may be granted access to journal files via file system access control lists (ACL). Distributions and administrators may choose to grant read access to all members of the &quot;wheel&quot; and &quot;adm&quot; system groups with a command such as the following: </p>
<dl>
<dd>
<pre># setfacl -Rnm g:wheel:rx,d:g:wheel:rx,g:adm:rx,d:g:adm:rx /var/log/journal/</pre>
</dl>
<p> Note that this command will update the ACLs both for existing journal files and for future journal files created in the /var/log/journal/ directory.</p>
<h2>Files</h2>
<p>/etc/systemd/journald.conf</p>
<dl>
<dd>Configure <code>systemd-journald</code> behavior. See <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5).</dl>
<p> /run/log/journal/<i>machine-id</i>/*.journal, /run/log/journal/<i>machine-id</i>/*.journal~, /var/log/journal/<i>machine-id</i>/*.journal, /var/log/journal/<i>machine-id</i>/*.journal~</p>
<dl>
<dd><code>systemd-journald</code> writes entries to files in /run/log/journal/<i>machine-id</i>/ or /var/log/journal/<i>machine-id</i>/ with the &quot;.journal&quot; suffix. If the daemon is stopped uncleanly, or if the files are found to be corrupted, they are renamed using the &quot;.journal~&quot; suffix, and <code>systemd-journald</code> starts writing to a new file. /run/ is used when /var/log/journal is not available, or when <code>Storage=volatile</code> is set in the <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) configuration file. </p>
<p> When systemd-journald ceases writing to a journal file, it will be renamed to &quot;<i>original-name</i>@<i>suffix.journal</i>&quot; (or &quot;<i>original-name</i>@<i>suffix.journal~</i>&quot;). Such files are &quot;archived&quot; and will not be written to any more. </p>
<p> In general, it is safe to read or copy any journal file (active or archived). <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and the functions in the <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3) library should be able to read all entries that have been fully written. </p>
<p> systemd-journald will automatically remove the oldest archived journal files to limit disk use. See <i>SystemMaxUse=</i> and related settings in <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5).</dl>
<p> /dev/kmsg, /dev/log, /run/systemd/journal/dev-log, /run/systemd/journal/socket, /run/systemd/journal/stdout</p>
<dl>
<dd>Sockets and other file node paths that <code>systemd-journald</code> will listen on and are visible in the file system. In addition to these, <code>systemd-journald</code> can listen for audit events using <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7).</dl>
<p> If journal namespacing is used these paths are slightly altered to include a namespace identifier, see above.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/8-systemd-coredump/">systemd-coredump</a></code>(8), <code><a href="/docs/linux/man/1-setfacl/">setfacl</a></code>(1), <code><a href="/docs/linux/man/3-sd_journal_print/">sd_journal_print</a></code>(3), <code>pydoc systemd.journal</code></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Native Journal Protocol</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/JOURNAL_NATIVE_PROTOCOL">https://systemd.io/JOURNAL_NATIVE_PROTOCOL</a></dl>
<dt> 2.</p>
<dd>Users, Groups, UIDs and GIDs on systemd systems</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/UIDS-GIDS">https://systemd.io/UIDS-GIDS</a></dl>
