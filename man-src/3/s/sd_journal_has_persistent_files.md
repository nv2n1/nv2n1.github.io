---
title: "sd_journal_has_persistent_files(3)"
name: "sd_journal_has_persistent_files"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_has_persistent_files/"
description: "sd_journal_has_runtime_files, sd_journal_has_persistent_files – Query availability of runtime or persistent journal files."
---

<p>sd_journal_has_runtime_files, sd_journal_has_persistent_files &#8211; Query availability of runtime or persistent journal files.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_has_runtime_files(sd_journal *j);

int sd_journal_has_persistent_files(sd_journal *j);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_has_runtime_files()</code></p>
<dd>returns a positive value if runtime journal files (present in /run/systemd/journal/) have been found. Otherwise returns 0. </p>
<p> <code>sd_journal_has_persistent_files()</code> returns a positive value if persistent journal files (present in /var/log/journal/) have been found. Otherwise returns 0.</p>
<h2>Return Value</h2>
<p>Both <code>sd_journal_has_runtime_files()</code> and <code>sd_journal_has_persistent_files()</code> return -EINVAL if their argument is NULL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3) </p>
