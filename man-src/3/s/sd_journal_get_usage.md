---
title: "sd_journal_get_usage(3)"
name: "sd_journal_get_usage"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_get_usage/"
description: "sd_journal_get_usage – Journal disk usage"
---

<p>sd_journal_get_usage &#8211; Journal disk usage</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_get_usage(sd_journal *j, uint64_t *bytes);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_get_usage()</code></p>
<dd>determines the total disk space currently used by journal files (in bytes). If <code>SD_JOURNAL_LOCAL_ONLY</code> was passed when opening the journal, this value will only reflect the size of journal files of the local host, otherwise of all hosts.</p>
<h2>Return Value</h2>
<p><code>sd_journal_get_usage()</code> returns 0 on success or a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_journal_get_usage()</code> interface is available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), </p>
