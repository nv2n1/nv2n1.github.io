---
title: "try_to_writeback_inodes_sb_nr(9)"
name: "try_to_writeback_inodes_sb_nr"
section: "9"
letter: "t"
url: "/docs/linux/man/9-try_to_writeback_inodes_sb_nr/"
description: "try_to_writeback_inodes_sb_nr – try to start writeback if none underway"
---

<p>try_to_writeback_inodes_sb_nr &#8211; try to start writeback if none underway</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool try_to_writeback_inodes_sb_nr(struct super_block&nbsp;<wbr>*&nbsp;<wbr></code><i>sb</i><code>, unsigned long&nbsp;<wbr></code><i>nr</i><code>, enum wb_reason&nbsp;<wbr></code><i>reason</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>the superblock</dl>
<p> <i>nr</i></p>
<dl>
<dd>the number of pages to write</dl>
<p> <i>reason</i></p>
<dl>
<dd>the reason of writeback</dl>
<h2>Description</h2>
<p>Invoke writeback_inodes_sb_nr if no writeback is currently underway. Returns 1 if writeback was started, 0 if not.</p>
<h2>Copyright</h2>
