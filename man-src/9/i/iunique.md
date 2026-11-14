---
title: "iunique(9)"
name: "iunique"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iunique/"
description: "iunique – get a unique inode number"
---

<p>iunique &#8211; get a unique inode number</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ino_t iunique(struct super_block&nbsp;<wbr>*&nbsp;<wbr></code><i>sb</i><code>, ino_t&nbsp;<wbr></code><i>max_reserved</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>superblock</dl>
<p> <i>max_reserved</i></p>
<dl>
<dd>highest reserved inode number</dl>
<h2>Description</h2>
<p>Obtain an inode number that is unique on the system for a given superblock. This is used by file systems that have no natural permanent inode numbering system. An inode number is returned that is higher than the reserved limit but unique. </p>
<p> BUGS: With a large number of inodes live on the file system this function currently becomes quite slow.</p>
<h2>Copyright</h2>
