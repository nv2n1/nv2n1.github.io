---
title: "systemd-journalctl(1)"
name: "systemd-journalctl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-journalctl/"
description: "journalctl, systemd-journalctl – Query the systemd journal"
---

<h2 class="name">NAME</h2>
<p> journalctl, systemd-journalctl &#8211; Query the systemd journal </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>journalctl </code><code>[OPTIONS&#8230;]</code><code>[MATCH]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>journalctl</code></p>
<dd>may be used to query the contents of the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) journal as written by <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8). </p>
<p> If called without parameter will show the full contents of the journal, starting with the oldest entry collected. </p>
<p> If a match argument is passed the output is filtered accordingly. A match is in the format FIELD=VALUE, e.g. _SYSTEMD_UNIT=httpd.service. See <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7) for a list of well-known fields. </p>
<p> Output is interleaved from all accessible journal files, whether they are rotated or currently being written, and regardless whether they belong to the system itself or are accessible user journals. </p>
<p> All users are granted access to their private per-user journals. However, by default only root and users who are members of the adm group get access to the system journal and the journals of other users.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;help</code>, <code>-h</code></p>
<dl>
<dt>
<dd> Prints a short help text and exits.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints a short version string and exits.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<p> <code>&#8211;all</code>, <code>-a</code></p>
<dl>
<dt>
<dd> Show all fields in full, even if they include unprintable characters or are very long.</dl>
<p> <code>&#8211;follow</code>, <code>-f</code></p>
<dl>
<dt>
<dd> Show only most recent journal entries, and continously print new entries as they are appended to the journal.</dl>
<p> <code>&#8211;lines=</code>, <code>-n</code></p>
<dl>
<dt>
<dd> Controls the number of journal lines to show, counting from the most recent ones. Takes a positive integer argument. In follow mode defaults to 10, otherwise is unset thus not limiting how many lines are shown.</dl>
<p> <code>&#8211;no-tail</code></p>
<dl>
<dt>
<dd> Show all stored output lines, even in follow mode. Undoes the effect of <code>&#8211;lines=</code>.</dl>
<p> <code>&#8211;output=</code>, <code>-o</code></p>
<dl>
<dt>
<dd> Controls the formatting of the journal entries that are shown. Takes one of short, short-monotonic, verbose, export, json, cat. short is the default and generates an output that is mostly identical to the formatting of classic syslog log files, showing one line per journal entry. short-monotonic is very similar but shows monotonic timestamps instead of wallclock timestamps. verbose shows the full structered entry items with all fiels. export serializes the journal into a binary (but mostly text-based) stream suitable for backups and network transfer. json formats entries as JSON data structures. cat generates a very terse output only showing the actual message of each journal entry with no meta data, not even a timestamp.</dl>
<p> <code>&#8211;quiet</code>, <code>-q</code></p>
<dl>
<dt>
<dd> Suppresses any warning message regarding inaccessable system journals when run as normal user.</dl>
<p> <code>&#8211;local</code>, <code>-l</code></p>
<dl>
<dt>
<dd> Show only locally generated messages.</dl>
<p> <code>&#8211;new-id128</code></p>
<dl>
<dt>
<dd> Instead of showing journal contents generate a new 128 bit ID suitable for identifying messages. This is intended for usage by developers who need a new identifier for a new message they introduce and want to make recognizable. Will print the new ID in three different formats which can be copied into source code or similar.</dl>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>ENVIRONMENT</h2>
<p> <i>$SYSTEMD_PAGER</i></p>
<dl>
<dt>
<dd> Pager to use when <code>&#8211;no-pager</code> is not given; overrides <i>$PAGER</i>. Setting this to an empty string or the value cat is equivalent to passing <code>&#8211;no-pager</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/5-systemd-journald-conf/">systemd-journald.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> <code>Lennart Poettering</code> &lt;lennart [at] poettering.net&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<h2>Index</h2>
