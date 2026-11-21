---

title: "systemd-coredumpctl(1)"
name: "systemd-coredumpctl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-coredumpctl/"
description: "systemd-coredumpctl – Retrieve coredumps from the journal"
---

<dl>
<dt> <code>systemd-coredumpctl</code> [OPTIONS&#8230;] {COMMAND} [PID|COMM|EXE|MATCH&#8230;]</dt></dl>
<p> <code>systemd-coredumpctl</code></p>
<dd>may be used to retrieve coredumps from <code><a href="/docs/linux/man/8-systemd-journald/">systemd-journald</a></code>(8).</dd>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Print a short help text and exit.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print a short version string and exit.</dd></dl>
<p> <code>-F</code>, <code>&#8211;field=</code></p>
<dl>
<dt>
</dt><dd> Print all possible data values the specified field takes in matching coredump entries of the journal.</dd></dl>
<p> <code>-o</code>, <code>&#8211;output=FILE</code></p>
<dl>
<dt>
</dt><dd> Write the core to <code>FILE</code>.</dd></dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
</dt><dd> Do not pipe output of <code>list</code> into a pager.</dd></dl>
<p> <code>&#8211;no-legend</code></p>
<dl>
<dt>
</dt><dd> Do not print the column headers.</dd></dl>
<p> The following commands are understood: </p>
<p> <code>list</code></p>
<dl>
<dt>
</dt><dd> List coredumps captured in the journal matching specified characteristics.</dd></dl>
<p> <code>dump</code></p>
<dl>
<dt>
</dt><dd> Extract the last coredump matching specified characteristics. The coredump will be written on standard output, unless an output file is specified with <code>-o/&#8211;output</code>.</dd></dl>
<p> <code>gdb</code></p>
<dl>
<dt>
</dt><dd> Invoke the GNU debugger on the last coredump matching specified characteristics.</dd></dl>
<h2>MATCHING</h2>
<p> Match can be: </p>
<p> <i>PID</i></p>
<dl>
<dt>
</dt><dd> Process ID of the process that dumped core. An integer.</dd></dl>
<p> <i>COMM</i></p>
<dl>
<dt>
</dt><dd> Name of the executable (matches <code>COREDUMP_COMM=</code>). Must not contain slashes.</dd></dl>
<p> <i>EXE</i></p>
<dl>
<dt>
</dt><dd> Path to the executable (matches <code>COREDUMP_EXE=</code>). Must contain at least one slash.</dd></dl>
<p> <i>MATCH</i></p>
<dl>
<dt>
</dt><dd> General journalctl predicates (see <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1)). Must contain an equals sign.</dd></dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned; otherwise, a non-zero failure code is returned. Not finding any matching coredumps is treated as failure.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1) </p>
