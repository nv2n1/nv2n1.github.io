---
title: "journalctl(1)"
name: "journalctl"
section: "1"
letter: "j"
url: "/docs/linux/man/1-journalctl/"
description: "journalctl – Query the systemd journal"
---

<h2 class="name">NAME</h2>
<p> journalctl &#8211; Query the systemd journal </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>journalctl</code> [OPTIONS&#8230;] [MATCHES&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>journalctl</code></p>
<dd>may be used to query the contents of the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) journal as written by <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8). </p>
<p> If called without parameters, it will show the full contents of the journal, starting with the oldest entry collected. </p>
<p> If one or more match arguments are passed, the output is filtered accordingly. A match is in the format &quot;FIELD=VALUE&quot;, e.g. &quot;_SYSTEMD_UNIT=httpd.service&quot;, referring to the components of a structured journal entry. See <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7) for a list of well-known fields. If multiple matches are specified matching different fields, the log entries are filtered by both, i.e. the resulting output will show only entries matching all the specified matches of this kind. If two matches apply to the same field, then they are automatically matched as alternatives, i.e. the resulting output will show entries matching any of the specified matches for the same field. Finally, the character &quot;+&quot; may appear as a separate word between other terms on the command line. This causes all matches before and after to be combined in a disjunction (i.e. logical OR). </p>
<p> It is also possible to filter the entries by specifying an absolute file path as an argument. The file path may be a file or a symbolic link and the file must exist at the time of the query. If a file path refers to an executable binary, an &quot;_EXE=&quot; match for the canonicalized binary path is added to the query. If a file path refers to an executable script, a &quot;_COMM=&quot; match for the script name is added to the query. If a file path refers to a device node, &quot;_KERNEL_DEVICE=&quot; matches for the kernel name of the device and for each of its ancestor devices is added to the query. Symbolic links are dereferenced, kernel names are synthesized, and parent devices are identified from the environment at the time of the query. In general, a device node is the best proxy for an actual device, as log entries do not usually contain fields that identify an actual device. For the resulting log entries to be correct for the actual device, the relevant parts of the environment at the time the entry was logged, in particular the actual device corresponding to the device node, must have been the same as those at the time of the query. Because device nodes generally change their corresponding devices across reboots, specifying a device node path causes the resulting entries to be restricted to those from the current boot. </p>
<p> Additional constraints may be added using options <code>&#8211;boot</code>, <code>&#8211;unit=</code>, etc., to further limit what entries will be shown (logical AND). </p>
<p> Output is interleaved from all accessible journal files, whether they are rotated or currently being written, and regardless of whether they belong to the system itself or are accessible user journals. The <code>&#8211;header</code> option can be used to identify which files <i>are</i> being shown. </p>
<p> The set of journal files which will be used can be modified using the <code>&#8211;user</code>, <code>&#8211;system</code>, <code>&#8211;directory</code>, and <code>&#8211;file</code> options, see below. </p>
<p> All users are granted access to their private per-user journals. However, by default, only root and users who are members of a few special groups are granted access to the system journal and the journals of other users. Members of the groups &quot;systemd-journal&quot;, &quot;adm&quot;, and &quot;wheel&quot; can read all journal files. Note that the two latter groups traditionally have additional privileges specified by the distribution. Members of the &quot;wheel&quot; group can often perform administrative tasks. </p>
<p> The output is paged through <code>less</code> by default, and long lines are &quot;truncated&quot; to screen width. The hidden part can be viewed by using the left-arrow and right-arrow keys. Paging can be disabled; see the <code>&#8211;no-pager</code> option and the &quot;Environment&quot; section below. </p>
<p> When outputting to a tty, lines are colored according to priority: lines of level ERROR and higher are colored red; lines of level NOTICE and higher are highlighted; lines of level DEBUG are colored lighter grey; other lines are displayed normally.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;no-full</code>, <code>&#8211;full</code>, <code>-l</code></p>
<dl>
<dt>
<dd> Ellipsize fields when they do not fit in available columns. The default is to show full fields, allowing them to wrap or be truncated by the pager, if one is used. </p>
<p> The old options <code>-l</code>/<code>&#8211;full</code> are not useful anymore, except to undo <code>&#8211;no-full</code>.</dl>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Show all fields in full, even if they include unprintable characters or are very long. By default, fields with unprintable characters are abbreviated as &quot;blob data&quot;. (Note that the pager may escape unprintable characters again.)</dl>
<p> <code>-f</code>, <code>&#8211;follow</code></p>
<dl>
<dt>
<dd> Show only the most recent journal entries, and continuously print new entries as they are appended to the journal.</dl>
<p> <code>-e</code>, <code>&#8211;pager-end</code></p>
<dl>
<dt>
<dd> Immediately jump to the end of the journal inside the implied pager tool. This implies <code>-n1000</code> to guarantee that the pager will not buffer logs of unbounded size. This may be overridden with an explicit <code>-n</code> with some other numeric value, while <code>-nall</code> will disable this cap. Note that this option is only supported for the <code><a href="/docs/linux/man/1-less/">less</a></code>(1) pager.</dl>
<p> <code>-n</code>, <code>&#8211;lines=</code></p>
<dl>
<dt>
<dd> Show the most recent journal events and limit the number of events shown. If <code>&#8211;follow</code> is used, this option is implied. The argument is a positive integer or &quot;all&quot; to disable line limiting. The default value is 10 if no argument is given.</dl>
<p> <code>&#8211;no-tail</code></p>
<dl>
<dt>
<dd> Show all stored output lines, even in follow mode. Undoes the effect of <code>&#8211;lines=</code>.</dl>
<p> <code>-r</code>, <code>&#8211;reverse</code></p>
<dl>
<dt>
<dd> Reverse output so that the newest entries are displayed first.</dl>
<p> <code>-o</code>, <code>&#8211;output=</code></p>
<dl>
<dt>
<dd> Controls the formatting of the journal entries that are shown. Takes one of the following options: </p>
<p> <code>short</code></p>
<dl>
<dt>
<dd> is the default and generates an output that is mostly identical to the formatting of classic syslog files, showing one line per journal entry.</dl>
<p> <code>short-full</code></p>
<dl>
<dt>
<dd> is very similar, but shows timestamps in the format the <code>&#8211;since=</code> and <code>&#8211;until=</code> options accept. Unlike the timestamp information shown in <code>short</code> output mode this mode includes weekday, year and timezone information in the output, and is locale-independent.</dl>
<p> <code>short-iso</code></p>
<dl>
<dt>
<dd> is very similar, but shows ISO 8601 wallclock timestamps.</dl>
<p> <code>short-iso-precise</code></p>
<dl>
<dt>
<dd> as for <code>short-iso</code> but includes full microsecond precision.</dl>
<p> <code>short-precise</code></p>
<dl>
<dt>
<dd> is very similar, but shows classic syslog timestamps with full microsecond precision.</dl>
<p> <code>short-monotonic</code></p>
<dl>
<dt>
<dd> is very similar, but shows monotonic timestamps instead of wallclock timestamps.</dl>
<p> <code>short-unix</code></p>
<dl>
<dt>
<dd> is very similar, but shows seconds passed since January 1st 1970 UTC instead of wallclock timestamps (&quot;UNIX time&quot;). The time is shown with microsecond accuracy.</dl>
<p> <code>verbose</code></p>
<dl>
<dt>
<dd> shows the full-structured entry items with all fields.</dl>
<p> <code>export</code></p>
<dl>
<dt>
<dd> serializes the journal into a binary (but mostly text-based) stream suitable for backups and network transfer (see m[blue]<code>Journal Export Format</code>m[]<font SIZE="-2">[1]</font> for more information). To import the binary stream back into native journald format use <code><a href="/docs/linux/man/8-systemd-journal-remote/">systemd-journal-remote</a></code>(8).</dl>
<p> <code>json</code></p>
<dl>
<dt>
<dd> formats entries as JSON objects, separated by newline characters (see m[blue]<code>Journal JSON Format</code>m[]<font SIZE="-2">[2]</font> for more information). Field values are generally encoded as JSON strings, with three exceptions: </p>
<dl>
<dt>
<dd> 1. Fields larger than 4096 bytes are encoded as <code>null</code> values. (This may be turned off by passing <code>&#8211;all</code>, but be aware that this may allocate overly long JSON objects.)</dl>
<dl>
<dt>
<dd> 2. Journal entries permit non-unique fields within the same log entry. JSON does not allow non-unique fields within objects. Due to this, if a non-unique field is encountered a JSON array is used as field value, listing all field values as elements.</dl>
<dl>
<dt>
<dd> 3. Fields containing non-printable or non-UTF8 bytes are encoded as arrays containing the raw bytes individually formatted as unsigned numbers.</dl>
<p> Note that this encoding is reversible (with the exception of the size limit).</dl>
<p> <code>json-pretty</code></p>
<dl>
<dt>
<dd> formats entries as JSON data structures, but formats them in multiple lines in order to make them more readable by humans.</dl>
<p> <code>json-sse</code></p>
<dl>
<dt>
<dd> formats entries as JSON data structures, but wraps them in a format suitable for m[blue]<code>Server-Sent Events</code>m[]<font SIZE="-2">[3]</font>.</dl>
<p> <code>json-seq</code></p>
<dl>
<dt>
<dd> formats entries as JSON data structures, but prefixes them with an ASCII Record Separator character (0x1E) and suffixes them with an ASCII Line Feed character (0x0A), in accordance with m[blue]<code>JavaScript Object Notation (JSON) Text Sequences</code>m[]<font SIZE="-2">[4]</font> (&quot;application/json-seq&quot;).</dl>
<p> <code>cat</code></p>
<dl>
<dt>
<dd> generates a very terse output, only showing the actual message of each journal entry with no metadata, not even a timestamp. If combined with the <code>&#8211;output-fields=</code> option will output the listed fields for each log record, instead of the message.</dl>
<p> <code>with-unit</code></p>
<dl>
<dt>
<dd> similar to short-full, but prefixes the unit and user unit names instead of the traditional syslog identifier. Useful when using templated instances, as it will include the arguments in the unit names.</dl>
</dl>
<p> <code>&#8211;output-fields=</code></p>
<dl>
<dt>
<dd> A comma separated list of the fields which should be included in the output. This has an effect only for the output modes which would normally show all fields (<code>verbose</code>, <code>export</code>, <code>json</code>, <code>json-pretty</code>, <code>json-sse</code> and <code>json-seq</code>), as well as on <code>cat</code>. For the former, the &quot;__CURSOR&quot;, &quot;__REALTIME_TIMESTAMP&quot;, &quot;__MONOTONIC_TIMESTAMP&quot;, and &quot;_BOOT_ID&quot; fields are always printed.</dl>
<p> <code>&#8211;utc</code></p>
<dl>
<dt>
<dd> Express time in Coordinated Universal Time (UTC).</dl>
<p> <code>&#8211;no-hostname</code></p>
<dl>
<dt>
<dd> Don&#8217;t show the hostname field of log messages originating from the local host. This switch has an effect only on the <code>short</code> family of output modes (see above). </p>
<p> Note: this option does not remove occurrences of the hostname from log entries themselves, so it does not prevent the hostname from being visible in the logs.</dl>
<p> <code>-x</code>, <code>&#8211;catalog</code></p>
<dl>
<dt>
<dd> Augment log lines with explanation texts from the message catalog. This will add explanatory help texts to log messages in the output where this is available. These short help texts will explain the context of an error or log event, possible solutions, as well as pointers to support forums, developer documentation, and any other relevant manuals. Note that help texts are not available for all messages, but only for selected ones. For more information on the message catalog, please refer to the m[blue]<code>Message Catalog Developer Documentation</code>m[]<font SIZE="-2">[5]</font>. </p>
<p> Note: when attaching <code>journalctl</code> output to bug reports, please do <i>not</i> use <code>-x</code>.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Suppresses all informational messages (i.e. &quot;&#8211; Journal begins at &#8230;&quot;, &quot;&#8211; Reboot &#8211;&quot;), any warning messages regarding inaccessible system journals when run as a normal user.</dl>
<p> <code>-m</code>, <code>&#8211;merge</code></p>
<dl>
<dt>
<dd> Show entries interleaved from all available journals, including remote ones.</dl>
<p> <code>-b </code><code>[[</code><i>ID</i>][<i>&plusmn;offset</i>]|<code>all</code>], <code>&#8211;boot</code><code>[=[</code><i>ID</i>][<i>&plusmn;offset</i>]|<code>all</code>]</p>
<dl>
<dt>
<dd> Show messages from a specific boot. This will add a match for &quot;_BOOT_ID=&quot;. </p>
<p> The argument may be empty, in which case logs for the current boot will be shown. </p>
<p> If the boot ID is omitted, a positive <i>offset</i> will look up the boots starting from the beginning of the journal, and an equal-or-less-than zero <i>offset</i> will look up boots starting from the end of the journal. Thus, <code>1</code> means the first boot found in the journal in chronological order, <code>2</code> the second and so on; while <code>-0</code> is the last boot, <code>-1</code> the boot before last, and so on. An empty <i>offset</i> is equivalent to specifying <code>-0</code>, except when the current boot is not the last boot (e.g. because <code>&#8211;directory</code> was specified to look at logs from a different machine). </p>
<p> If the 32-character <i>ID</i> is specified, it may optionally be followed by <i>offset</i> which identifies the boot relative to the one given by boot <i>ID</i>. Negative values mean earlier boots and positive values mean later boots. If <i>offset</i> is not specified, a value of zero is assumed, and the logs for the boot given by <i>ID</i> are shown. </p>
<p> The special argument <code>all</code> can be used to negate the effect of an earlier use of <code>-b</code>.</dl>
<p> <code>&#8211;list-boots</code></p>
<dl>
<dt>
<dd> Show a tabular list of boot numbers (relative to the current boot), their IDs, and the timestamps of the first and last message pertaining to the boot.</dl>
<p> <code>-k</code>, <code>&#8211;dmesg</code></p>
<dl>
<dt>
<dd> Show only kernel messages. This implies <code>-b</code> and adds the match &quot;_TRANSPORT=kernel&quot;.</dl>
<p> <code>-t</code>, <code>&#8211;identifier=</code><i>SYSLOG_IDENTIFIER</i></p>
<dl>
<dt>
<dd> Show messages for the specified syslog identifier <i>SYSLOG_IDENTIFIER</i>. </p>
<p> This parameter can be specified multiple times.</dl>
<p> <code>-u</code>, <code>&#8211;unit=</code><i>UNIT</i><code>|</code><i>PATTERN</i></p>
<dl>
<dt>
<dd> Show messages for the specified systemd unit <i>UNIT</i> (such as a service unit), or for any of the units matched by <i>PATTERN</i>. If a pattern is specified, a list of unit names found in the journal is compared with the specified pattern and all that match are used. For each unit name, a match is added for messages from the unit (&quot;_SYSTEMD_UNIT=<i>UNIT</i>&quot;), along with additional matches for messages from systemd and messages about coredumps for the specified unit. A match is also added for &quot;_SYSTEMD_SLICE=<i>UNIT</i>&quot;, such that if the provided <i>UNIT</i> is a <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5) unit, all logs of children of the slice will be shown. </p>
<p> This parameter can be specified multiple times.</dl>
<p> <code>&#8211;user-unit=</code></p>
<dl>
<dt>
<dd> Show messages for the specified user session unit. This will add a match for messages from the unit (&quot;_SYSTEMD_USER_UNIT=&quot; and &quot;_UID=&quot;) and additional matches for messages from session systemd and messages about coredumps for the specified unit. A match is also added for &quot;_SYSTEMD_USER_SLICE=<i>UNIT</i>&quot;, such that if the provided <i>UNIT</i> is a <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5) unit, all logs of children of the unit will be shown. </p>
<p> This parameter can be specified multiple times.</dl>
<p> <code>-p</code>, <code>&#8211;priority=</code></p>
<dl>
<dt>
<dd> Filter output by message priorities or priority ranges. Takes either a single numeric or textual log level (i.e. between 0/&quot;emerg&quot; and 7/&quot;debug&quot;), or a range of numeric/text log levels in the form FROM..TO. The log levels are the usual syslog log levels as documented in <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), i.e. &quot;emerg&quot;&nbsp;(0), &quot;alert&quot;&nbsp;(1), &quot;crit&quot;&nbsp;(2), &quot;err&quot;&nbsp;(3), &quot;warning&quot;&nbsp;(4), &quot;notice&quot;&nbsp;(5), &quot;info&quot;&nbsp;(6), &quot;debug&quot;&nbsp;(7). If a single log level is specified, all messages with this log level or a lower (hence more important) log level are shown. If a range is specified, all messages within the range are shown, including both the start and the end value of the range. This will add &quot;PRIORITY=&quot; matches for the specified priorities.</dl>
<p> <code>&#8211;facility=</code></p>
<dl>
<dt>
<dd> Filter output by syslog facility. Takes a comma-separated list of numbers or facility names. The names are the usual syslog facilities as documented in <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). <code>&#8211;facility=help</code> may be used to display a list of known facility names and exit.</dl>
<p> <code>-g</code>, <code>&#8211;grep=</code></p>
<dl>
<dt>
<dd> Filter output to entries where the <i>MESSAGE=</i> field matches the specified regular expression. PERL-compatible regular expressions are used, see <code><a href="/docs/linux/man/3-pcre2pattern/">pcre2pattern</a></code>(3) for a detailed description of the syntax. </p>
<p> If the pattern is all lowercase, matching is case insensitive. Otherwise, matching is case sensitive. This can be overridden with the <code>&#8211;case-sensitive</code> option, see below.</dl>
<p> <code>&#8211;case-sensitive</code><code>[=BOOLEAN]</code></p>
<dl>
<dt>
<dd> Make pattern matching case sensitive or case insensitive.</dl>
<p> <code>-c</code>, <code>&#8211;cursor=</code></p>
<dl>
<dt>
<dd> Start showing entries from the location in the journal specified by the passed cursor.</dl>
<p> <code>&#8211;cursor-file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> If <i>FILE</i> exists and contains a cursor, start showing entries <i>after</i> this location. Otherwise the show entries according the other given options. At the end, write the cursor of the last entry to <i>FILE</i>. Use this option to continually read the journal by sequentially calling <code>journalctl</code>.</dl>
<p> <code>&#8211;after-cursor=</code></p>
<dl>
<dt>
<dd> Start showing entries from the location in the journal <i>after</i> the location specified by the passed cursor. The cursor is shown when the <code>&#8211;show-cursor</code> option is used.</dl>
<p> <code>&#8211;show-cursor</code></p>
<dl>
<dt>
<dd> The cursor is shown after the last entry after two dashes: </p>
<dl>
<dt>
<dd>
<pre>
-- cursor: s=0639...
</pre>
</dl>
<p> The format of the cursor is private and subject to change.</dl>
<p> <code>-S</code>, <code>&#8211;since=</code>, <code>-U</code>, <code>&#8211;until=</code></p>
<dl>
<dt>
<dd> Start showing entries on or newer than the specified date, or on or older than the specified date, respectively. Date specifications should be of the format &quot;2012-10-30 18:17:16&quot;. If the time part is omitted, &quot;00:00:00&quot; is assumed. If only the seconds component is omitted, &quot;:00&quot; is assumed. If the date component is omitted, the current day is assumed. Alternatively the strings &quot;yesterday&quot;, &quot;today&quot;, &quot;tomorrow&quot; are understood, which refer to 00:00:00 of the day before the current day, the current day, or the day after the current day, respectively. &quot;now&quot; refers to the current time. Finally, relative times may be specified, prefixed with &quot;-&quot; or &quot;+&quot;, referring to times before or after the current time, respectively. For complete time and date specification, see <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7). Note that <code>&#8211;output=short-full</code> prints timestamps that follow precisely this format.</dl>
<p> <code>-F</code>, <code>&#8211;field=</code></p>
<dl>
<dt>
<dd> Print all possible data values the specified field can take in all entries of the journal.</dl>
<p> <code>-N</code>, <code>&#8211;fields</code></p>
<dl>
<dt>
<dd> Print all field names currently used in all entries of the journal.</dl>
<p> <code>&#8211;system</code>, <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Show messages from system services and the kernel (with <code>&#8211;system</code>). Show messages from service of current user (with <code>&#8211;user</code>). If neither is specified, show all messages that the user can see.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Show messages from a running, local container. Specify a container name to connect to.</dl>
<p> <code>-D </code><i>DIR</i>, <code>&#8211;directory=</code><i>DIR</i></p>
<dl>
<dt>
<dd> Takes a directory path as argument. If specified, journalctl will operate on the specified journal directory <i>DIR</i> instead of the default runtime and system journal paths.</dl>
<p> <code>&#8211;file=</code><i>GLOB</i></p>
<dl>
<dt>
<dd> Takes a file glob as an argument. If specified, journalctl will operate on the specified journal files matching <i>GLOB</i> instead of the default runtime and system journal paths. May be specified multiple times, in which case files will be suitably interleaved.</dl>
<p> <code>&#8211;root=</code><i>ROOT</i></p>
<dl>
<dt>
<dd> Takes a directory path as an argument. If specified, <code>journalctl</code> will operate on journal directories and catalog file hierarchy underneath the specified directory instead of the root directory (e.g. <code>&#8211;update-catalog</code> will create <i>ROOT</i>/var/lib/systemd/catalog/database, and journal files under <i>ROOT</i>/run/journal/ or <i>ROOT</i>/var/log/journal/ will be displayed).</dl>
<p> <code>&#8211;image=</code><i>IMAGE</i></p>
<dl>
<dt>
<dd> Takes a path to a disk image file or block device node. If specified, <code>journalctl</code> will operate on the file system in the indicated disk image. This is similar to <code>&#8211;root=</code> but operates on file systems stored in disk images or block devices, thus providing an easy way to extract log data from disk images. The disk image should either contain just a file system or a set of file systems within a GPT partition table, following the m[blue]<code>Discoverable Partitions Specification</code>m[]<font SIZE="-2">[6]</font>. For further information on supported disk images, see <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1)&#8217;s switch of the same name.</dl>
<p> <code>&#8211;namespace=</code><i>NAMESPACE</i></p>
<dl>
<dt>
<dd> Takes a journal namespace identifier string as argument. If not specified the data collected by the default namespace is shown. If specified shows the log data of the specified namespace instead. If the namespace is specified as &quot;*&quot; data from all namespaces is shown, interleaved. If the namespace identifier is prefixed with &quot;+&quot; data from the specified namespace and the default namespace is shown, interleaved, but no other. For details about journal namespaces see <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8).</dl>
<p> <code>&#8211;header</code></p>
<dl>
<dt>
<dd> Instead of showing journal contents, show internal header information of the journal fields accessed. </p>
<p> This option is particularly useful when trying to identify out-of-order journal entries, as happens for example when the machine is booted with the wrong system time.</dl>
<p> <code>&#8211;disk-usage</code></p>
<dl>
<dt>
<dd> Shows the current disk usage of all journal files. This shows the sum of the disk usage of all archived and active journal files.</dl>
<p> <code>&#8211;vacuum-size=</code>, <code>&#8211;vacuum-time=</code>, <code>&#8211;vacuum-files=</code></p>
<dl>
<dt>
<dd> Removes the oldest archived journal files until the disk space they use falls below the specified size (specified with the usual &quot;K&quot;, &quot;M&quot;, &quot;G&quot; and &quot;T&quot; suffixes), or all archived journal files contain no data older than the specified timespan (specified with the usual &quot;s&quot;, &quot;m&quot;, &quot;h&quot;, &quot;days&quot;, &quot;months&quot;, &quot;weeks&quot; and &quot;years&quot; suffixes), or no more than the specified number of separate journal files remain. Note that running <code>&#8211;vacuum-size=</code> has only an indirect effect on the output shown by <code>&#8211;disk-usage</code>, as the latter includes active journal files, while the vacuuming operation only operates on archived journal files. Similarly, <code>&#8211;vacuum-files=</code> might not actually reduce the number of journal files to below the specified number, as it will not remove active journal files. </p>
<p> <code>&#8211;vacuum-size=</code>, <code>&#8211;vacuum-time=</code> and <code>&#8211;vacuum-files=</code> may be combined in a single invocation to enforce any combination of a size, a time and a number of files limit on the archived journal files. Specifying any of these three parameters as zero is equivalent to not enforcing the specific limit, and is thus redundant. </p>
<p> These three switches may also be combined with <code>&#8211;rotate</code> into one command. If so, all active files are rotated first, and the requested vacuuming operation is executed right after. The rotation has the effect that all currently active files are archived (and potentially new, empty journal files opened as replacement), and hence the vacuuming operation has the greatest effect as it can take all log data written so far into account.</dl>
<p> <code>&#8211;list-catalog </code><code>[</code><i>128-bit-ID&#8230;</i>]</p>
<dl>
<dt>
<dd> List the contents of the message catalog as a table of message IDs, plus their short description strings. </p>
<p> If any <i>128-bit-ID</i>s are specified, only those entries are shown.</dl>
<p> <code>&#8211;dump-catalog </code><code>[</code><i>128-bit-ID&#8230;</i>]</p>
<dl>
<dt>
<dd> Show the contents of the message catalog, with entries separated by a line consisting of two dashes and the ID (the format is the same as .catalog files). </p>
<p> If any <i>128-bit-ID</i>s are specified, only those entries are shown.</dl>
<p> <code>&#8211;update-catalog</code></p>
<dl>
<dt>
<dd> Update the message catalog index. This command needs to be executed each time new catalog files are installed, removed, or updated to rebuild the binary catalog index.</dl>
<p> <code>&#8211;setup-keys</code></p>
<dl>
<dt>
<dd> Instead of showing journal contents, generate a new key pair for Forward Secure Sealing (FSS). This will generate a sealing key and a verification key. The sealing key is stored in the journal data directory and shall remain on the host. The verification key should be stored externally. Refer to the <code>Seal=</code> option in <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) for information on Forward Secure Sealing and for a link to a refereed scholarly paper detailing the cryptographic theory it is based on.</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> When <code>&#8211;setup-keys</code> is passed and Forward Secure Sealing (FSS) has already been configured, recreate FSS keys.</dl>
<p> <code>&#8211;interval=</code></p>
<dl>
<dt>
<dd> Specifies the change interval for the sealing key when generating an FSS key pair with <code>&#8211;setup-keys</code>. Shorter intervals increase CPU consumption but shorten the time range of undetectable journal alterations. Defaults to 15min.</dl>
<p> <code>&#8211;verify</code></p>
<dl>
<dt>
<dd> Check the journal file for internal consistency. If the file has been generated with FSS enabled and the FSS verification key has been specified with <code>&#8211;verify-key=</code>, authenticity of the journal file is verified.</dl>
<p> <code>&#8211;verify-key=</code></p>
<dl>
<dt>
<dd> Specifies the FSS verification key to use for the <code>&#8211;verify</code> operation.</dl>
<p> <code>&#8211;sync</code></p>
<dl>
<dt>
<dd> Asks the journal daemon to write all yet unwritten journal data to the backing file system and synchronize all journals. This call does not return until the synchronization operation is complete. This command guarantees that any log messages written before its invocation are safely stored on disk at the time it returns.</dl>
<p> <code>&#8211;flush</code></p>
<dl>
<dt>
<dd> Asks the journal daemon to flush any log data stored in /run/log/journal/ into /var/log/journal/, if persistent storage is enabled. This call does not return until the operation is complete. Note that this call is idempotent: the data is only flushed from /run/log/journal/ into /var/log/journal/ once during system runtime (but see <code>&#8211;relinquish-var</code> below), and this command exits cleanly without executing any operation if this has already happened. This command effectively guarantees that all data is flushed to /var/log/journal/ at the time it returns.</dl>
<p> <code>&#8211;relinquish-var</code></p>
<dl>
<dt>
<dd> Asks the journal daemon for the reverse operation to <code>&#8211;flush</code>: if requested the daemon will write further log data to /run/log/journal/ and stops writing to /var/log/journal/. A subsequent call to <code>&#8211;flush</code> causes the log output to switch back to /var/log/journal/, see above.</dl>
<p> <code>&#8211;smart-relinquish-var</code></p>
<dl>
<dt>
<dd> Similar to <code>&#8211;relinquish-var</code> but executes no operation if the root file system and /var/lib/journal/ reside on the same mount point. This operation is used during system shutdown in order to make the journal daemon stop writing data to /var/log/journal/ in case that directory is located on a mount point that needs to be unmounted.</dl>
<p> <code>&#8211;rotate</code></p>
<dl>
<dt>
<dd> Asks the journal daemon to rotate journal files. This call does not return until the rotation operation is complete. Journal file rotation has the effect that all currently active journal files are marked as archived and renamed, so that they are never written to in future. New (empty) journal files are then created in their place. This operation may be combined with <code>&#8211;vacuum-size=</code>, <code>&#8211;vacuum-time=</code> and <code>&#8211;vacuum-file=</code> into a single command, see above.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned; otherwise, a non-zero failure code is returned.</p>
<h2>ENVIRONMENT</h2>
<p> <i>$SYSTEMD_LOG_LEVEL</i></p>
<dl>
<dt>
<dd> The maximum log level of emitted messages (messages with a higher log level, i.e. less important ones, will be suppressed). Either one of (in order of decreasing importance) <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code>, or an integer in the range 0&#8230;7. See <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for more information.</dl>
<p> <i>$SYSTEMD_LOG_COLOR</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages written to the tty will be colored according to priority. </p>
<p> This setting is only useful when messages are written directly to the terminal, because <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and other tools that display logs will color messages based on the log level on their own.</dl>
<p> <i>$SYSTEMD_LOG_TIME</i></p>
<dl>
<dt>
<dd> A boolean. If true, console log messages will be prefixed with a timestamp. </p>
<p> This setting is only useful when messages are written directly to the terminal or a file, because <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and other tools that display logs will attach timestamps based on the entry metadata on their own.</dl>
<p> <i>$SYSTEMD_LOG_LOCATION</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages will be prefixed with a filename and line number in the source code where the message originates. </p>
<p> Note that the log location is often attached as metadata to journal entries anyway. Including it directly in the message text can nevertheless be convenient when debugging programs.</dl>
<p> <i>$SYSTEMD_LOG_TID</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages will be prefixed with the current numerical thread ID (TID). </p>
<p> Note that the this information is attached as metadata to journal entries anyway. Including it directly in the message text can nevertheless be convenient when debugging programs.</dl>
<p> <i>$SYSTEMD_LOG_TARGET</i></p>
<dl>
<dt>
<dd> The destination for log messages. One of <code>console</code> (log to the attached tty), <code>console-prefixed</code> (log to the attached tty but with prefixes encoding the log level and &quot;facility&quot;, see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code>kmsg</code> (log to the kernel circular log buffer), <code>journal</code> (log to the journal), <code>journal-or-kmsg</code> (log to the journal if available, and to kmsg otherwise), <code>auto</code> (determine the appropriate log target automatically, the default), <code>null</code> (disable log output).</dl>
<p> <i>$SYSTEMD_PAGER</i></p>
<dl>
<dt>
<dd> Pager to use when <code>&#8211;no-pager</code> is not given; overrides <i>$PAGER</i>. If neither <i>$SYSTEMD_PAGER</i> nor <i>$PAGER</i> are set, a set of well-known pager implementations are tried in turn, including <code><a href="/docs/linux/man/1-less/">less</a></code>(1) and <code><a href="/docs/linux/man/1-more/">more</a></code>(1), until one is found. If no pager implementation is discovered no pager is invoked. Setting this environment variable to an empty string or the value &quot;cat&quot; is equivalent to passing <code>&#8211;no-pager</code>.</dl>
<p> <i>$SYSTEMD_LESS</i></p>
<dl>
<dt>
<dd> Override the options passed to <code>less</code> (by default &quot;FRSXMK&quot;). </p>
<p> Users might want to change two options in particular: </p>
<p> <code>K</code></p>
<dl>
<dt>
<dd> This option instructs the pager to exit immediately when Ctrl+C is pressed. To allow <code>less</code> to handle Ctrl+C itself to switch back to the pager command prompt, unset this option. </p>
<p> If the value of <i>$SYSTEMD_LESS</i> does not include &quot;K&quot;, and the pager that is invoked is <code>less</code>, Ctrl+C will be ignored by the executable, and needs to be handled by the pager.</dl>
<p> <code>X</code></p>
<dl>
<dt>
<dd> This option instructs the pager to not send termcap initialization and deinitialization strings to the terminal. It is set by default to allow command output to remain visible in the terminal even after the pager exits. Nevertheless, this prevents some pager functionality from working, in particular paged output cannot be scrolled with the mouse.</dl>
<p> See <code><a href="/docs/linux/man/1-less/">less</a></code>(1) for more discussion.</dl>
<p> <i>$SYSTEMD_LESSCHARSET</i></p>
<dl>
<dt>
<dd> Override the charset passed to <code>less</code> (by default &quot;utf-8&quot;, if the invoking terminal is determined to be UTF-8 compatible).</dl>
<p> <i>$SYSTEMD_PAGERSECURE</i></p>
<dl>
<dt>
<dd> Takes a boolean argument. When true, the &quot;secure&quot; mode of the pager is enabled; if false, disabled. If <i>$SYSTEMD_PAGERSECURE</i> is not set at all, secure mode is enabled if the effective UID is not the same as the owner of the login session, see <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2) and <code><a href="/docs/linux/man/3-sd_pid_get_owner_uid/">sd_pid_get_owner_uid</a></code>(3). In secure mode, <code>LESSSECURE=1</code> will be set when invoking the pager, and the pager shall disable commands that open or create new files or start new subprocesses. When <i>$SYSTEMD_PAGERSECURE</i> is not set at all, pagers which are not known to implement secure mode will not be used. (Currently only <code><a href="/docs/linux/man/1-less/">less</a></code>(1) implements secure mode.) </p>
<p> Note: when commands are invoked with elevated privileges, for example under <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) or <code><a href="/docs/linux/man/1-pkexec/">pkexec</a></code>(1), care must be taken to ensure that unintended interactive features are not enabled. &quot;Secure&quot; mode for the pager may be enabled automatically as describe above. Setting <i>SYSTEMD_PAGERSECURE=0</i> or not removing it from the inherited environment allows the user to invoke arbitrary commands. Note that if the <i>$SYSTEMD_PAGER</i> or <i>$PAGER</i> variables are to be honoured, <i>$SYSTEMD_PAGERSECURE</i> must be set too. It might be reasonable to completely disable the pager using <code>&#8211;no-pager</code> instead.</dl>
<p> <i>$SYSTEMD_COLORS</i></p>
<dl>
<dt>
<dd> Takes a boolean argument. When true, <code>systemd</code> and related utilities will use colors in their output, otherwise the output will be monochrome. Additionally, the variable can take one of the following special values: &quot;16&quot;, &quot;256&quot; to restrict the use of colors to the base 16 or 256 ANSI colors, respectively. This can be specified to override the automatic decision based on <i>$TERM</i> and what the console is connected to.</dl>
<p> <i>$SYSTEMD_URLIFY</i></p>
<dl>
<dt>
<dd> The value must be a boolean. Controls whether clickable links should be generated in the output for terminal emulators supporting this. This can be specified to override the decision that <code>systemd</code> makes based on <i>$TERM</i> and other conditions.</dl>
<h2>EXAMPLES</h2>
<p> Without arguments, all collected logs are shown unfiltered: </p>
<dl>
<dt>
<dd>
<pre>
journalctl
</pre>
</dl>
<p> With one match specified, all entries with a field matching the expression are shown: </p>
<dl>
<dt>
<dd>
<pre>
journalctl _SYSTEMD_UNIT=avahi-daemon.service
journalctl _SYSTEMD_CGROUP=/user.slice/user-42.slice/session-c1.scope
</pre>
</dl>
<p> If two different fields are matched, only entries matching both expressions at the same time are shown: </p>
<dl>
<dt>
<dd>
<pre>
journalctl _SYSTEMD_UNIT=avahi-daemon.service _PID=28097
</pre>
</dl>
<p> If two matches refer to the same field, all entries matching either expression are shown: </p>
<dl>
<dt>
<dd>
<pre>
journalctl _SYSTEMD_UNIT=avahi-daemon.service _SYSTEMD_UNIT=dbus.service
</pre>
</dl>
<p> If the separator &quot;+&quot; is used, two expressions may be combined in a logical OR. The following will show all messages from the Avahi service process with the PID 28097 plus all messages from the D-Bus service (from any of its processes): </p>
<dl>
<dt>
<dd>
<pre>
journalctl _SYSTEMD_UNIT=avahi-daemon.service _PID=28097 + _SYSTEMD_UNIT=dbus.service
</pre>
</dl>
<p> To show all fields emitted <i>by</i> a unit and <i>about</i> the unit, option <code>-u</code>/<code>&#8211;unit=</code> should be used. <code>journalctl -u </code><i>name</i> expands to a complex filter similar to </p>
<dl>
<dt>
<dd>
<pre>
_SYSTEMD_UNIT=<i>name</i>.service
  + UNIT=<i>name</i>.service _PID=1
  + OBJECT_SYSTEMD_UNIT=<i>name</i>.service _UID=0
  + COREDUMP_UNIT=<i>name</i>.service _UID=0 MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1
    
</pre>
</dl>
<p> (see <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7) for an explanation of those patterns). </p>
<p> Show all logs generated by the D-Bus executable: </p>
<dl>
<dt>
<dd>
<pre>
journalctl /usr/bin/dbus-daemon
</pre>
</dl>
<p> Show all kernel logs from previous boot: </p>
<dl>
<dt>
<dd>
<pre>
journalctl -k -b -1
</pre>
</dl>
<p> Show a live log display from a system service apache.service: </p>
<dl>
<dt>
<dd>
<pre>
journalctl -f -u apache
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/1-coredumpctl/">coredumpctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5), <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7), <code><a href="/docs/linux/man/8-systemd-journal-remote-service/">systemd-journal-remote.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-journal-upload-service/">systemd-journal-upload.service</a></code>(8)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Journal Export Format</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/JOURNAL_EXPORT_FORMATS#journal-export-format">https://systemd.io/JOURNAL_EXPORT_FORMATS#journal-export-format</a></dl>
<dt> 2.</p>
<dd> Journal JSON Format</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/JOURNAL_EXPORT_FORMATS#journal-json-format">https://systemd.io/JOURNAL_EXPORT_FORMATS#journal-json-format</a></dl>
<dt> 3.</p>
<dd> Server-Sent Events</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://developer.mozilla.org/en-US/docs/Server-sent_events/Using_server-sent_events">https://developer.mozilla.org/en-US/docs/Server-sent_events/Using_server-sent_events</a></dl>
<dt> 4.</p>
<dd> JavaScript Object Notation (JSON) Text Sequences</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://tools.ietf.org/html/rfc7464">https://tools.ietf.org/html/rfc7464</a></dl>
<dt> 5.</p>
<dd> Message Catalog Developer Documentation</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/catalog">https://www.freedesktop.org/wiki/Software/systemd/catalog</a></dl>
<dt> 6.</p>
<dd> Discoverable Partitions Specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/DISCOVERABLE_PARTITIONS">https://systemd.io/DISCOVERABLE_PARTITIONS</a></dl>
</dl>
<h2>Index</h2>
