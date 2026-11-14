---
title: "try_to_writeback_inodes_sb(9)"
name: "try_to_writeback_inodes_sb"
section: "9"
letter: "t"
url: "/docs/linux/man/9-try_to_writeback_inodes_sb/"
description: "try_to_writeback_inodes_sb – try to start writeback if none underway"
---

<p>try_to_writeback_inodes_sb &#8211; try to start writeback if none underway</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool try_to_writeback_inodes_sb(struct super_block&nbsp;<wbr>*&nbsp;<wbr></code><i>sb</i><code>, enum wb_reason&nbsp;<wbr></code><i>reason</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>the superblock</dl>
<p> <i>reason</i></p>
<dl>
<dd>reason why some writeback work was initiated</dl>
<h2>Description</h2>
<p>Implement by <code>try_to_writeback_inodes_sb_nr</code> Returns 1 if writeback was started, 0 if not.</p>
<h2>Copyright</h2>
