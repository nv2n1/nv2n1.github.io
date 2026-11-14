---
title: "sb_start_write(9)"
name: "sb_start_write"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sb_start_write/"
description: "sb_start_write – get write access to a superblock"
---

<p>sb_start_write &#8211; get write access to a superblock</p>
<h2>Synopsis</h2>
<pre><code>void sb_start_write(struct super_block *sb);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>the super we write to</dl>
<h2>Description</h2>
<p>When a process wants to write data or metadata to a file system (i.e. dirty a page or an inode), it should embed the operation in a <code>sb_start_write</code> &#8211; <code>sb_end_write</code> pair to get exclusion against file system freezing. This function increments number of writers preventing freezing. If the file system is already frozen, the function waits until the file system is thawed. </p>
<p> Since freeze protection behaves as a lock, users have to preserve ordering of freeze protection and other filesystem locks. Generally, freeze protection should be the outermost lock. In particular, we have: </p>
<p> sb_start_write -&gt; i_mutex (write path, truncate, directory ops, &#8230;) -&gt; s_umount (freeze_super, thaw_super)</p>
<h2>Copyright</h2>
