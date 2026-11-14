---
title: "sd-journal(3)"
name: "sd-journal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd-journal/"
description: "sd-journal – APIs for submitting and querying log entries to and from the journal"
---

<p>sd-journal &#8211; APIs for submitting and querying log entries to and from the journal</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;





pkg-config --cflags --libs libsystemd</code></pre>
<h2>Description</h2>
<dd>sd-journal.h provides APIs to submit and query log entries. The APIs exposed act both as client for the <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8) journal service and as parser for the journal files on disk. </p>
<p> See <code><a href="/docs/linux/man/3-sd_journal_print/">sd_journal_print</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_stream_fd/">sd_journal_stream_fd</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_realtime_usec/">sd_journal_get_realtime_usec</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_add_match/">sd_journal_add_match</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_seek_head/">sd_journal_seek_head</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_cursor/">sd_journal_get_cursor</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_cutoff_realtime_usec/">sd_journal_get_cutoff_realtime_usec</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_cutoff_monotonic_usec/">sd_journal_get_cutoff_monotonic_usec</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_usage/">sd_journal_get_usage</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_catalog/">sd_journal_get_catalog</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_fd/">sd_journal_get_fd</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_has_runtime_files/">sd_journal_has_runtime_files</a></code>(3) and <code><a href="/docs/linux/man/3-sd_journal_has_persistent_files/">sd_journal_has_persistent_files</a></code>(3) for more information about the functions implemented. </p>
<p> Command line access for submitting entries to the journal is available with the <code><a href="/docs/linux/man/1-systemd-cat/">systemd-cat</a></code>(1) tool. Command line access for querying entries from the journal is available with the <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) tool.</p>
<h2>Notes</h2>
<p>These APIs are implemented as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd_journal_print/">sd_journal_print</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_stream_fd/">sd_journal_stream_fd</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_realtime_usec/">sd_journal_get_realtime_usec</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_add_match/">sd_journal_add_match</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_seek_head/">sd_journal_seek_head</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_cursor/">sd_journal_get_cursor</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_cutoff_realtime_usec/">sd_journal_get_cutoff_realtime_usec</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_cutoff_monotonic_usec/">sd_journal_get_cutoff_monotonic_usec</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_usage/">sd_journal_get_usage</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_fd/">sd_journal_get_fd</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_query_unique/">sd_journal_query_unique</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_catalog/">sd_journal_get_catalog</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_has_runtime_files/">sd_journal_has_runtime_files</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_has_persistent_files/">sd_journal_has_persistent_files</a></code>(3), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3), <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) </p>
