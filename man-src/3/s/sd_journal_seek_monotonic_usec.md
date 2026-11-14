---
title: "sd_journal_seek_monotonic_usec(3)"
name: "sd_journal_seek_monotonic_usec"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_seek_monotonic_usec/"
description: "sd_journal_seek_head, sd_journal_seek_tail, sd_journal_seek_monotonic_usec, sd_journal_seek_realtime_usec, sd_journal_seek_cursor – Seek to a position in the journal"
---

<p>sd_journal_seek_head, sd_journal_seek_tail, sd_journal_seek_monotonic_usec, sd_journal_seek_realtime_usec, sd_journal_seek_cursor &#8211; Seek to a position in the journal </p>
<h2>Synopsis</h2>
<pre>
#include &lt;systemd/sd-journal.h&gt;
</pre>
<dl COMPACT>
<dt> <code>int sd_journal_seek_head(sd_journal&nbsp;<wbr>*</code><i>j</i><code>);</code></p>
<dt> <code>int sd_journal_seek_tail(sd_journal&nbsp;<wbr>*</code><i>j</i><code>);</code></p>
<dt> <code>int sd_journal_seek_monotonic_usec(sd_journal&nbsp;<wbr>*</code><i>j</i><code>, sd_id128_t&nbsp;<wbr></code><i>boot_id</i><code>, uint64_t&nbsp;<wbr></code><i>usec</i><code>);</code></p>
<dt> <code>int sd_journal_seek_realtime_usec(sd_journal&nbsp;<wbr>*</code><i>j</i><code>, uint64_t&nbsp;<wbr></code><i>usec</i><code>);</code></p>
<dt> <code>int sd_journal_seek_cursor(sd_journal&nbsp;<wbr>*</code><i>j</i><code>, const char&nbsp;<wbr>*</code><i>cursor</i><code>);</code></dl>
<h2>Description</h2>
<p> <code>sd_journal_seek_head()</code></p>
<dd>seeks to the beginning of the journal, i.e. the oldest available entry. </p>
<p> Similarly, <code>sd_journal_seek_tail()</code> may be used to seek to the end of the journal, i.e. the most recent available entry. </p>
<p> <code>sd_journal_seek_monotonic_usec()</code> seeks to the entry with the specified monotonic timestamp, i.e. <code>CLOCK_MONOTONIC</code>. Since monotonic time restarts on every reboot a boot ID needs to be specified as well. </p>
<p> <code>sd_journal_seek_realtime_usec()</code> seeks to the entry with the specified realtime (wallclock) timestamp, i.e. <code>CLOCK_REALTIME</code>. Note that the realtime clock is not necessarily monotonic. If a realtime timestamp is ambiguous, it is not defined which position is sought to. </p>
<p> <code>sd_journal_seek_cursor()</code> seeks to the entry located at the specified cursor string. For details on cursors, see <code><a href="/docs/linux/man/3-sd_journal_get_cursor/">sd_journal_get_cursor</a></code>(3). If no entry matching the specified cursor is found the call will seek to the next closest entry (in terms of time) instead. To verify whether the newly selected entry actually matches the cursor, use <code><a href="/docs/linux/man/3-sd_journal_test_cursor/">sd_journal_test_cursor</a></code>(3). </p>
<p> Note that these calls do not actually make any entry the new current entry, this needs to be done in a separate step with a subsequent <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3) invocation (or a similar call). Only then, entry data may be retrieved via <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3). If no entry exists that matches exactly the specified seek address, the next closest is sought to. If <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3) is used, the closest following entry will be sought to, if <code><a href="/docs/linux/man/3-sd_journal_previous/">sd_journal_previous</a></code>(3) is used the closest preceding entry is sought to.</p>
<h2>Return Value</h2>
<p> The functions return 0 on success or a negative errno-style error code.</p>
<h2>Notes</h2>
<p> The <code>sd_journal_seek_head()</code>, <code>sd_journal_seek_tail()</code>, <code>sd_journal_seek_monotonic_usec()</code>, <code>sd_journal_seek_realtime_usec()</code>, and <code>sd_journal_seek_cursor()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_cursor/">sd_journal_get_cursor</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_realtime_usec/">sd_journal_get_realtime_usec</a></code>(3)</p>
