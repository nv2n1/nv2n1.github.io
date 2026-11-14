---
title: "sd_journal_get_realtime_usec(3)"
name: "sd_journal_get_realtime_usec"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_get_realtime_usec/"
description: "sd_journal_get_realtime_usec, sd_journal_get_monotonic_usec – Read timestamps from the current journal entry"
---

<p>sd_journal_get_realtime_usec, sd_journal_get_monotonic_usec &#8211; Read timestamps from the current journal entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_get_realtime_usec(sd_journal *j, uint64_t *usec);

int sd_journal_get_monotonic_usec(sd_journal *j, uint64_t *usec, sd_id128_t *boot_id);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_get_realtime_usec()</code></p>
<dd>gets the realtime (wallclock) timestamp of the current journal entry. It takes two arguments: the journal context object and a pointer to a 64-bit unsigned integer to store the timestamp in. The timestamp is in microseconds since the epoch, i.e. <code>CLOCK_REALTIME</code>. </p>
<p> <code>sd_journal_get_monotonic_usec()</code> gets the monotonic timestamp of the current journal entry. It takes three arguments: the journal context object, a pointer to a 64-bit unsigned integer to store the timestamp in, as well as a 128-bit ID buffer to store the boot ID of the monotonic timestamp. The timestamp is in microseconds since boot-up of the specific boot, i.e. <code>CLOCK_MONOTONIC</code>. Since the monotonic clock begins new with every reboot, it only defines a well-defined point in time when used together with an identifier identifying the boot. See <code><a href="/docs/linux/man/3-sd_id128_get_boot/">sd_id128_get_boot</a></code>(3) for more information. If the boot ID parameter is passed <code>NULL</code>, the function will fail if the monotonic timestamp of the current entry is not of the current system boot. </p>
<p> Note that these functions will not work before <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3) (or related call) has been called at least once, in order to position the read pointer at a valid entry.</p>
<h2>Return Value</h2>
<p><code>sd_journal_get_realtime_usec()</code> and <code>sd_journal_get_monotonic_usec()</code> returns 0 on success or a negative errno-style error code. If the boot ID parameter was passed <code>NULL</code> and the monotonic timestamp of the current journal entry is not of the current system boot, <code>-ESTALE</code> is returned by <code>sd_journal_get_monotonic_usec()</code>.</p>
<h2>Notes</h2>
<p>The <code>sd_journal_get_realtime_usec()</code> and <code>sd_journal_get_monotonic_usec()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3), <code><a href="/docs/linux/man/3-sd_id128_get_boot/">sd_id128_get_boot</a></code>(3), <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/3-sd_journal_get_cutoff_realtime_usec/">sd_journal_get_cutoff_realtime_usec</a></code>(3) </p>
