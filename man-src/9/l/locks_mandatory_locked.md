---
title: "locks_mandatory_locked(9)"
name: "locks_mandatory_locked"
section: "9"
letter: "l"
url: "/docs/linux/man/9-locks_mandatory_locked/"
description: "locks_mandatory_locked – Check for an active lock"
---

<p>locks_mandatory_locked &#8211; Check for an active lock</p>
<h2>Synopsis</h2>
<pre><code>int locks_mandatory_locked(struct file *file);</code></pre>
<h2>Arguments</h2>
<p><i>file</i></p>
<dl>
<dd>
<dd>the file to check</dl>
<h2>Description</h2>
<p>Searches the inode&#8217;s list of locks to find any POSIX locks which conflict. This function is called from <code>locks_verify_locked</code> only.</p>
<h2>Copyright</h2>
