---
title: "bmap(9)"
name: "bmap"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bmap/"
description: "bmap – find a block number in a file"
---

<p>bmap &#8211; find a block number in a file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sector_t bmap(struct inode&nbsp;<wbr>*&nbsp;<wbr></code><i>inode</i><code>, sector_t&nbsp;<wbr></code><i>block</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode of file</dl>
<p> <i>block</i></p>
<dl>
<dd>block to find</dl>
<h2>Description</h2>
<p>Returns the block number on the device holding the inode that is the disk block number for the block of the file requested. That is, asked for block 4 of inode 1 the function will return the disk block relative to the disk start that holds that block of the file.</p>
<h2>Copyright</h2>
