---
title: "sd_journal_get_cutoff_monotonic_usec(3)"
name: "sd_journal_get_cutoff_monotonic_usec"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_get_cutoff_monotonic_usec/"
description: "sd_journal_get_cutoff_realtime_usec, sd_journal_get_cutoff_monotonic_usec – Read cut-off timestamps from the current journal entry"
---

<p>sd_journal_get_cutoff_realtime_usec, sd_journal_get_cutoff_monotonic_usec &#8211; Read cut-off timestamps from the current journal entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_get_cutoff_realtime_usec(sd_journal *j, uint64_t *from, uint64_t *to);

int sd_journal_get_cutoff_monotonic_usec(sd_journal *j, sd_id128_t boot_id, uint64_t *from, uint64_t *to);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_get_cutoff_realtime_usec()</code></p>
<dd>retrieves the realtime (wallclock) timestamps of the first and last entries accessible in the journal. It takes three arguments: the journal context object <i>j</i> and two pointers <i>from</i> and <i>to</i> pointing at 64-bit unsigned integers to store the timestamps in. The timestamps are in microseconds since the epoch, i.e. <code>CLOCK_REALTIME</code>. Either one of the two timestamp arguments may be passed as <code>NULL</code> in case the timestamp is not needed, but not both. </p>
<p> <code>sd_journal_get_cutoff_monotonic_usec()</code> retrieves the monotonic timestamps of the first and last entries accessible in the journal. It takes three arguments: the journal context object <i>j</i>, a 128-bit identifier for the boot <i>boot_id</i>, and two pointers to 64-bit unsigned integers to store the timestamps, <i>from</i> and <i>to</i>. The timestamps are in microseconds since boot-up of the specific boot, i.e. <code>CLOCK_MONOTONIC</code>. Since the monotonic clock begins new with every reboot it only defines a well-defined point in time when used together with an identifier identifying the boot, see <code><a href="/docs/linux/man/3-sd_id128_get_boot/">sd_id128_get_boot</a></code>(3) for more information. The function will return the timestamps for the boot identified by the passed boot ID. Either one of the two timestamp arguments may be passed as <code>NULL</code> in case the timestamp is not needed, but not both.</p>
<h2>Return Value</h2>
<p><code>sd_journal_get_cutoff_realtime_usec()</code> and <code>sd_journal_get_cutoff_monotonic_usec()</code> return 1 on success, 0 if not suitable entries are in the journal or a negative errno-style error code. </p>
<p> Locations pointed to by parameters <i>from</i> and <i>to</i> will be set only if the return value is positive, and obviously, the parameters are non-null.</p>
<h2>Notes</h2>
<p>The <code>sd_journal_get_cutoff_realtime_usec()</code> and <code>sd_journal_get_cutoff_monotonic_usec()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_realtime_usec/">sd_journal_get_realtime_usec</a></code>(3), <code><a href="/docs/linux/man/3-sd_id128_get_boot/">sd_id128_get_boot</a></code>(3), <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) </p>
