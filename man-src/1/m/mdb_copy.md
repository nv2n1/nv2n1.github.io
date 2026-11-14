---
title: "mdb_copy(1)"
name: "mdb_copy"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb_copy/"
description: "mdb_copy – LMDB environment copy tool"
---

<h2 class="name">NAME</h2>
<p> mdb_copy &#8211; LMDB environment copy tool </p>
<h2>SYNOPSIS</h2>
<p> <code>mdb_copy</code> [<code>-V</code>] [<code>-c</code>] [<code>-n</code>] <code>srcpath</code> [<code>dstpath</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>mdb_copy</code> utility copies an LMDB environment. The environment can be copied regardless of whether it is currently in use. No lockfile is created, since it gets recreated at need. </p>
<p> If <i>dstpath</i> is specified it must be the path of an empty directory for storing the backup. Otherwise, the backup will be written to stdout. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> Write the library version number to the standard output, and exit.</p>
<dt><code>-c</code></p>
<dd> Compact while copying. Only current data pages will be copied; freed or unused pages will be omitted from the copy. This option will slow down the backup process as it is more CPU-intensive.</p>
<dt><code>-n</code></p>
<dd> Open LDMB environment(s) which do not use subdirectories. </p>
</dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>CAVEATS</h2>
<p> This utility can trigger significant file size growth if run in parallel with write transactions, because pages which they free during copying cannot be reused until the copy is done.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mdb_stat/">mdb_stat</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Howard Chu of Symas Corporation &lt;<a rel="nofollow" href="http://www.symas.com">http://www.symas.com</a>&gt; </p>
<h2>Index</h2>
