---
title: "debugfs_use_file_finish(9)"
name: "debugfs_use_file_finish"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_use_file_finish/"
description: "debugfs_use_file_finish – mark the end of file data access"
---

<p>debugfs_use_file_finish &#8211; mark the end of file data access</p>
<h2>Synopsis</h2>
<pre><code>void debugfs_use_file_finish(int srcu_idx);</code></pre>
<h2>Arguments</h2>
<p><i>srcu_idx</i></p>
<dl>
<dd>
<dd>the SRCU index &#8220;created&#8221; by a former call to <code>debugfs_use_file_start</code>.</dl>
<h2>Description</h2>
<p>Allow any ongoing concurrent call into <code>debugfs_remove</code> or <code>debugfs_remove_recursive</code> blocked by a former call to <code>debugfs_use_file_start</code> to proceed and return to its caller.</p>
<h2>Copyright</h2>
