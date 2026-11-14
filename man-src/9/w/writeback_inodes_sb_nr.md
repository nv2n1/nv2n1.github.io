---
title: "writeback_inodes_sb_nr(9)"
name: "writeback_inodes_sb_nr"
section: "9"
letter: "w"
url: "/docs/linux/man/9-writeback_inodes_sb_nr/"
---

writeback_inodes_sb_nr - writeback dirty inodes from given super_block

<h2>Synopsis</h2>

<pre><code>void writeback_inodes_sb_nr(struct super_block *sb, unsigned long nr, enum wb_reason reason);</code></pre>

<h2>Arguments</h2>

<i>sb</i>
<dl><dd><dd>the superblock</dl>
 

 <i>nr</i>
<dl><dd>the number of pages to write</dl>
 

 <i>reason</i>
<dl><dd>reason why some writeback work initiated</dl>

<h2>Description</h2>

Start writeback on some inodes on this super_block. No guarantees are made on how many (if any) will be written, and this function does not wait for IO completion of submitted IO.

<h2>Copyright</h2>


