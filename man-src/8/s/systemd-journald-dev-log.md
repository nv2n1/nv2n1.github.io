---
title: "systemd-journald-dev-log(8)"
name: "systemd-journald-dev-log"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-journald-dev-log/"
description: "systemd-journald.service, systemd-journald.socket, systemd-journald-dev-log.socket, systemd-journald – Journal service"
---

<p>systemd-journald.service, systemd-journald.socket, systemd-journald-dev-log.socket, systemd-journald &#8211; Journal service</p>
<h2>Synopsis</h2>
<p>systemd-journald.service </p>
<p> systemd-journald.socket </p>
<p> systemd-journald-dev-log.socket </p>
<p> /usr/lib/systemd/systemd-journald</p>
<h2>Description</h2>
<p>systemd-journald is a system service that collects and stores logging data. It creates and maintains structured, indexed journals based on logging information that is received from the kernel, from user processes via the libc <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) call, from standard input and standard error of system services or via its native API. It will implicitly collect numerous metadata fields for each log messages in a secure and unfakeable way. See <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7) for more information about the collected metadata. </p>
<p> Log data collected by the journal is primarily text-based but can also include binary data where necessary. All objects stored in the journal can be up to 2^64-1 bytes in size. </p>
<p> By default, the journal stores log data in /run/log/journal/. Since /run/ is volatile, log data is lost at reboot. To make the data persistent, it is sufficient to create /var/log/journal/ where systemd-journald will then store the data. </p>
<p> systemd-journald will forward all received log messages to the <code>AF_UNIX</code><code>SOCK_DGRAM</code> socket /run/systemd/journal/syslog, if it exists, which may be used by Unix syslog daemons to process the data further. </p>
<p> See <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) for information about the configuration of this service.</p>
<h2>Signals</h2>
<p>SIGUSR1</p>
<dl>
<dd>Request that journal data from /run/ is flushed to /var/ in order to make it persistent (if this is enabled). This must be used after /var/ is mounted, as otherwise log data from /run is never flushed to /var regardless of the configuration.</dl>
<p> SIGUSR2</p>
<dl>
<dd>Request immediate rotation of the journal files.</dl>
<h2>Kernel Command Line</h2>
<p>A few configuration parameters from journald.conf may be overridden on the kernel command line: </p>
<p> <i>systemd.journald.forward_to_syslog=</i>, <i>systemd.journald.forward_to_kmsg=</i>, <i>systemd.journald.forward_to_console=</i>, <i>systemd.journald.forward_to_wall=</i></p>
<dl>
<dd>Enables/disables forwarding of collected log messages to syslog, the kernel log buffer, the system console or wall. </p>
<p> See <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) for information about these settings.</dl>
<h2>Access Control</h2>
<p>Journal files are, by default, owned and readable by the &quot;systemd-journal&quot; system group but are not writable. Adding a user to this group thus enables her/him to read the journal files. </p>
<p> By default, each logged in user will get her/his own set of journal files in /var/log/journal/. These files will not be owned by the user, however, in order to avoid that the user can write to them directly. Instead, file system ACLs are used to ensure the user gets read access only. </p>
<p> Additional users and groups may be granted access to journal files via file system access control lists (ACL). Distributions and administrators may choose to grant read access to all members of the &quot;wheel&quot; and &quot;adm&quot; system groups with a command such as the following: </p>
<dl>
<dd>
<pre># setfacl -Rnm g:wheel:rx,d:g:wheel:rx,g:adm:rx,d:g:adm:rx /var/log/journal/</pre>
</dl>
<p> Note that this command will update the ACLs both for existing journal files and for future journal files created in the /var/log/journal/ directory.</p>
<h2>Files</h2>
<p>/etc/systemd/journald.conf</p>
<dl>
<dd>Configure <code>systemd-journald</code> behaviour. See <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5).</dl>
<p> /run/log/journal/<i>machine-id</i>/*.journal, /run/log/journal/<i>machine-id</i>/*.journal~, /var/log/journal/<i>machine-id</i>/*.journal, /var/log/journal/<i>machine-id</i>/*.journal~</p>
<dl>
<dd><code>systemd-journald</code> writes entries to files in /run/log/journal/<i>machine-id</i>/ or /var/log/journal/<i>machine-id</i>/ with the &quot;.journal&quot; suffix. If the daemon is stopped uncleanly, or if the files are found to be corrupted, they are renamed using the &quot;.journal~&quot; suffix, and <code>systemd-journald</code> starts writing to a new file. /run is used when /var/log/journal is not available, or when <code>Storage=volatile</code> is set in the <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) configuration file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/8-systemd-coredump/">systemd-coredump</a></code>(8), <code><a href="/docs/linux/man/1-setfacl/">setfacl</a></code>(1), <code>pydoc systemd.journal</code>. </p>
