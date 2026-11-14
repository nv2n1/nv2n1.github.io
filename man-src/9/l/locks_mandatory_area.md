---
title: "locks_mandatory_area(9)"
name: "locks_mandatory_area"
section: "9"
letter: "l"
url: "/docs/linux/man/9-locks_mandatory_area/"
description: "locks_mandatory_area – Check for a conflicting lock"
---

<p>locks_mandatory_area &#8211; Check for a conflicting lock</p>
<h2>Synopsis</h2>
<pre><code>int locks_mandatory_area(struct inode *inode, struct file *filp, loff_t start, loff_t end, unsigned char type);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>the file to check</dl>
<p> <i>filp</i></p>
<dl>
<dd>how the file was opened (if it was)</dl>
<p> <i>start</i></p>
<dl>
<dd>first byte in the file to check</dl>
<p> <i>end</i></p>
<dl>
<dd>lastbyte in the file to check</dl>
<p> <i>type</i></p>
<dl>
<dd><code>F_WRLCK</code> for a write lock, else <code>F_RDLCK</code></dl>
<h2>Description</h2>
<p>Searches the inode&#8217;s list of locks to find any POSIX locks which conflict.</p>
<h2>Copyright</h2>
