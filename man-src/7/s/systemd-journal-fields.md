---
title: "systemd-journal-fields(7)"
name: "systemd-journal-fields"
section: "7"
letter: "s"
url: "/docs/linux/man/7-systemd-journal-fields/"
description: "systemd.journal-fields – Special journal fields"
---

<p>systemd.journal-fields &#8211; Special journal fields</p>
<h2>Description</h2>
<p>Entries in the journal (as written by <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8)) resemble a UNIX process environment block in syntax but with fields that may include binary data. Primarily, fields are formatted UTF-8 text strings, and binary encoding is used only where formatting as UTF-8 text strings makes little sense. New fields may freely be defined by applications, but a few fields have special meanings. All fields with special meanings are optional. In some cases, fields may appear more than once per entry.</p>
<h2>User Journal Fields</h2>
<p>User fields are fields that are directly passed from clients and stored in the journal. </p>
<p> <i>MESSAGE=</i></p>
<dl>
<dd>The human-readable message string for this entry. This is supposed to be the primary text shown to the user. It is usually not translated (but might be in some cases), and is not supposed to be parsed for metadata.</dl>
<p> <i>MESSAGE_ID=</i></p>
<dl>
<dd>A 128-bit message identifier ID for recognizing certain message types, if this is desirable. This should contain a 128-bit ID formatted as a lower-case hexadecimal string, without any separating dashes or suchlike. This is recommended to be a UUID-compatible ID, but this is not enforced, and formatted differently. Developers can generate a new ID for this purpose with <code>systemd-id128 new</code>.</dl>
<p> <i>PRIORITY=</i></p>
<dl>
<dd>A priority value between 0 (&quot;emerg&quot;) and 7 (&quot;debug&quot;) formatted as a decimal string. This field is compatible with syslog&#8217;s priority concept.</dl>
<p> <i>CODE_FILE=</i>, <i>CODE_LINE=</i>, <i>CODE_FUNC=</i></p>
<dl>
<dd>The code location generating this message, if known. Contains the source filename, the line number and the function name.</dl>
<p> <i>ERRNO=</i></p>
<dl>
<dd>The low-level Unix error number causing this entry, if any. Contains the numeric value of <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3) formatted as a decimal string.</dl>
<p> <i>INVOCATION_ID=</i>, <i>USER_INVOCATION_ID=</i></p>
<dl>
<dd>A randomized, unique 128-bit ID identifying each runtime cycle of the unit. This is different from <i>_SYSTEMD_INVOCATION_ID</i> in that it is only used for messages coming from systemd code (e.g. logs from the system/user manager or from forked processes performing systemd-related setup).</dl>
<p> <i>SYSLOG_FACILITY=</i>, <i>SYSLOG_IDENTIFIER=</i>, <i>SYSLOG_PID=</i>, <i>SYSLOG_TIMESTAMP=</i></p>
<dl>
<dd>Syslog compatibility fields containing the facility (formatted as decimal string), the identifier string (i.e. &quot;tag&quot;), the client PID, and the timestamp as specified in the original datagram. (Note that the tag is usually derived from glibc&#8217;s <i>program_invocation_short_name</i> variable, see <code><a href="/docs/linux/man/3-program_invocation_short_name/">program_invocation_short_name</a></code>(3).) </p>
<p> Note that the journal service does not validate the values of any structured journal fields whose name is not prefixed with an underscore, and this includes any syslog related fields such as these. Hence, applications that supply a facility, PID, or log level are expected to do so properly formatted, i.e. as numeric integers formatted as decimal strings.</dl>
<p> <i>SYSLOG_RAW=</i></p>
<dl>
<dd>The original contents of the syslog line as received in the syslog datagram. This field is only included if the <i>MESSAGE=</i> field was modified compared to the original payload or the timestamp could not be located properly and is not included in <i>SYSLOG_TIMESTAMP=</i>. Message truncation occurs when when the message contains leading or trailing whitespace (trailing and leading whitespace is stripped), or it contains an embedded <code>NUL</code> byte (the <code>NUL</code> byte and anything after it is not included). Thus, the original syslog line is either stored as <i>SYSLOG_RAW=</i> or it can be recreated based on the stored priority and facility, timestamp, identifier, and the message payload in <i>MESSAGE=</i>.</dl>
<p> <i>DOCUMENTATION=</i></p>
<dl>
<dd>A documentation URL with further information about the topic of the log message. Tools such as <code>journalctl</code> will include a hyperlink to an URL specified this way in their output. Should be an &quot;http://&quot;, &quot;https://&quot;, &quot;file:/&quot;, &quot;man:&quot; or &quot;info:&quot; URL.</dl>
<p> <i>TID=</i></p>
<dl>
<dd>The numeric thread ID (TID) the log message originates from.</dl>
<p> <i>UNIT=</i>, <i>USER_UNIT=</i></p>
<dl>
<dd>The name of a unit. Used by the system and user managers when logging about specific units. </p>
<p> When <code>&#8211;unit=</code><i>name</i> or <code>&#8211;user-unit=</code><i>name</i> are used with <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), a match pattern that includes &quot;UNIT=<i>name</i>.service&quot; or &quot;USER_UNIT=<i>name</i>.service&quot; will be generated.</dl>
<h2>Trusted Journal Fields</h2>
<p>Fields prefixed with an underscore are trusted fields, i.e. fields that are implicitly added by the journal and cannot be altered by client code. </p>
<p> <i>_PID=</i>, <i>_UID=</i>, <i>_GID=</i></p>
<dl>
<dd>The process, user, and group ID of the process the journal entry originates from formatted as a decimal string. Note that entries obtained via &quot;stdout&quot; or &quot;stderr&quot; of forked processes will contain credentials valid for a parent process (that initiated the connection to <code>systemd-journald</code>).</dl>
<p> <i>_COMM=</i>, <i>_EXE=</i>, <i>_CMDLINE=</i></p>
<dl>
<dd>The name, the executable path, and the command line of the process the journal entry originates from.</dl>
<p> <i>_CAP_EFFECTIVE=</i></p>
<dl>
<dd>The effective <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) of the process the journal entry originates from.</dl>
<p> <i>_AUDIT_SESSION=</i>, <i>_AUDIT_LOGINUID=</i></p>
<dl>
<dd>The session and login UID of the process the journal entry originates from, as maintained by the kernel audit subsystem.</dl>
<p> <i>_SYSTEMD_CGROUP=</i>, <i>_SYSTEMD_SLICE=</i>, <i>_SYSTEMD_UNIT=</i>, <i>_SYSTEMD_USER_UNIT=</i>, <i>_SYSTEMD_USER_SLICE=</i>, <i>_SYSTEMD_SESSION=</i>, <i>_SYSTEMD_OWNER_UID=</i></p>
<dl>
<dd>The control group path in the systemd hierarchy, the systemd slice unit name, the systemd unit name, the unit name in the systemd user manager (if any), the systemd session ID (if any), and the owner UID of the systemd user unit or systemd session (if any) of the process the journal entry originates from.</dl>
<p> <i>_SELINUX_CONTEXT=</i></p>
<dl>
<dd>The SELinux security context (label) of the process the journal entry originates from.</dl>
<p> <i>_SOURCE_REALTIME_TIMESTAMP=</i></p>
<dl>
<dd>The earliest trusted timestamp of the message, if any is known that is different from the reception time of the journal. This is the time in microseconds since the epoch UTC, formatted as a decimal string.</dl>
<p> <i>_BOOT_ID=</i></p>
<dl>
<dd>The kernel boot ID for the boot the message was generated in, formatted as a 128-bit hexadecimal string.</dl>
<p> <i>_MACHINE_ID=</i></p>
<dl>
<dd>The machine ID of the originating host, as available in <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5).</dl>
<p> <i>_SYSTEMD_INVOCATION_ID=</i></p>
<dl>
<dd>The invocation ID for the runtime cycle of the unit the message was generated in, as available to processes of the unit in <i>$INVOCATION_ID</i> (see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5)).</dl>
<p> <i>_HOSTNAME=</i></p>
<dl>
<dd>The name of the originating host.</dl>
<p> <i>_TRANSPORT=</i></p>
<dl>
<dd>How the entry was received by the journal service. Valid transports are: </p>
<p> <code>audit</code></p>
<dl>
<dd>for those read from the kernel audit subsystem</dl>
<p> <code>driver</code></p>
<dl>
<dd>for internally generated messages</dl>
<p> <code>syslog</code></p>
<dl>
<dd>for those received via the local syslog socket with the syslog protocol</dl>
<p> <code>journal</code></p>
<dl>
<dd>for those received via the native journal protocol</dl>
<p> <code>stdout</code></p>
<dl>
<dd>for those read from a service&#8217;s standard output or error output</dl>
<p> <code>kernel</code></p>
<dl>
<dd>for those read from the kernel</dl>
</dl>
<p> <i>_STREAM_ID=</i></p>
<dl>
<dd>Only applies to &quot;_TRANSPORT=stdout&quot; records: specifies a randomized 128bit ID assigned to the stream connection when it was first created. This ID is useful to reconstruct individual log streams from the log records: all log records carrying the same stream ID originate from the same stream.</dl>
<p> <i>_LINE_BREAK=</i></p>
<dl>
<dd>Only applies to &quot;_TRANSPORT=stdout&quot; records: indicates that the log message in the standard output/error stream was not terminated with a normal newline character (&quot;
&quot;, i.e. ASCII 10). Specifically, when set this field is one of <code>nul</code> (in case the line was terminated by a <code>NUL</code> byte), <code>line-max</code> (in case the maximum log line length was reached, as configured with <i>LineMax=</i> in <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5)), <code>eof</code> (if this was the last log record of a stream and the stream ended without a final newline character), or <code>pid-change</code> (if the process which generated the log output changed in the middle of a line). Note that this record is not generated when a normal newline character was used for marking the log line end.</dl>
<p> <i>_NAMESPACE=</i></p>
<dl>
<dd>If this file was written by a <code>systemd-journald</code> instance managing a journal namespace that is not the default, this field contains the namespace identifier. See <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8) for details about journal namespaces.</dl>
<h2>Kernel Journal Fields</h2>
<p>Kernel fields are fields that are used by messages originating in the kernel and stored in the journal. </p>
<p> <i>_KERNEL_DEVICE=</i></p>
<dl>
<dd>The kernel device name. If the entry is associated to a block device, contains the major and minor numbers of the device node, separated by &quot;:&quot; and prefixed by &quot;b&quot;. Similarly for character devices, but prefixed by &quot;c&quot;. For network devices, this is the interface index prefixed by &quot;n&quot;. For all other devices, this is the subsystem name prefixed by &quot;+&quot;, followed by &quot;:&quot;, followed by the kernel device name.</dl>
<p> <i>_KERNEL_SUBSYSTEM=</i></p>
<dl>
<dd>The kernel subsystem name.</dl>
<p> <i>_UDEV_SYSNAME=</i></p>
<dl>
<dd>The kernel device name as it shows up in the device tree below /sys/.</dl>
<p> <i>_UDEV_DEVNODE=</i></p>
<dl>
<dd>The device node path of this device in /dev/.</dl>
<p> <i>_UDEV_DEVLINK=</i></p>
<dl>
<dd>Additional symlink names pointing to the device node in /dev/. This field is frequently set more than once per entry.</dl>
<h2>Fields To Log On Behalf Of A Different Program</h2>
<p>Fields in this section are used by programs to specify that they are logging on behalf of another program or unit. </p>
<p> Fields used by the <code>systemd-coredump</code> coredump kernel helper: </p>
<p> <i>COREDUMP_UNIT=</i>, <i>COREDUMP_USER_UNIT=</i></p>
<dl>
<dd>Used to annotate messages containing coredumps from system and session units. See <code><a href="/docs/linux/man/1-coredumpctl/">coredumpctl</a></code>(1).</dl>
<p> Privileged programs (currently UID 0) may attach <i>OBJECT_PID=</i> to a message. This will instruct <code>systemd-journald</code> to attach additional fields on behalf of the caller: </p>
<p> <i>OBJECT_PID=</i><i>PID</i></p>
<dl>
<dd>PID of the program that this message pertains to.</dl>
<p> <i>OBJECT_UID=</i>, <i>OBJECT_GID=</i>, <i>OBJECT_COMM=</i>, <i>OBJECT_EXE=</i>, <i>OBJECT_CMDLINE=</i>, <i>OBJECT_AUDIT_SESSION=</i>, <i>OBJECT_AUDIT_LOGINUID=</i>, <i>OBJECT_SYSTEMD_CGROUP=</i>, <i>OBJECT_SYSTEMD_SESSION=</i>, <i>OBJECT_SYSTEMD_OWNER_UID=</i>, <i>OBJECT_SYSTEMD_UNIT=</i>, <i>OBJECT_SYSTEMD_USER_UNIT=</i></p>
<dl>
<dd>These are additional fields added automatically by <code>systemd-journald</code>. Their meaning is the same as <i>_UID=</i>, <i>_GID=</i>, <i>_COMM=</i>, <i>_EXE=</i>, <i>_CMDLINE=</i>, <i>_AUDIT_SESSION=</i>, <i>_AUDIT_LOGINUID=</i>, <i>_SYSTEMD_CGROUP=</i>, <i>_SYSTEMD_SESSION=</i>, <i>_SYSTEMD_UNIT=</i>, <i>_SYSTEMD_USER_UNIT=</i>, and <i>_SYSTEMD_OWNER_UID=</i> as described above, except that the process identified by <i>PID</i> is described, instead of the process which logged the message.</dl>
<h2>Address Fields</h2>
<p>During serialization into external formats, such as the m[blue]<code>Journal Export Format</code>m[]<font SIZE="-2">[1]</font> or the m[blue]<code>Journal JSON Format</code>m[]<font SIZE="-2">[2]</font>, the addresses of journal entries are serialized into fields prefixed with double underscores. Note that these are not proper fields when stored in the journal but for addressing metadata of entries. They cannot be written as part of structured log entries via calls such as <code><a href="/docs/linux/man/3-sd_journal_send/">sd_journal_send</a></code>(3). They may also not be used as matches for <code><a href="/docs/linux/man/3-sd_journal_add_match/">sd_journal_add_match</a></code>(3). </p>
<p> <i>__CURSOR=</i></p>
<dl>
<dd>The cursor for the entry. A cursor is an opaque text string that uniquely describes the position of an entry in the journal and is portable across machines, platforms and journal files.</dl>
<p> <i>__REALTIME_TIMESTAMP=</i></p>
<dl>
<dd>The wallclock time (<code>CLOCK_REALTIME</code>) at the point in time the entry was received by the journal, in microseconds since the epoch UTC, formatted as a decimal string. This has different properties from &quot;_SOURCE_REALTIME_TIMESTAMP=&quot;, as it is usually a bit later but more likely to be monotonic.</dl>
<p> <i>__MONOTONIC_TIMESTAMP=</i></p>
<dl>
<dd>The monotonic time (<code>CLOCK_MONOTONIC</code>) at the point in time the entry was received by the journal in microseconds, formatted as a decimal string. To be useful as an address for the entry, this should be combined with the boot ID in &quot;_BOOT_ID=&quot;.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/1-coredumpctl/">coredumpctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Journal Export Format</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/JOURNAL_EXPORT_FORMATS#journal-export-format">https://systemd.io/JOURNAL_EXPORT_FORMATS#journal-export-format</a></dl>
<dt> 2.</p>
<dd>Journal JSON Format</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/JOURNAL_EXPORT_FORMATS#journal-json-format">https://systemd.io/JOURNAL_EXPORT_FORMATS#journal-json-format</a></dl>
