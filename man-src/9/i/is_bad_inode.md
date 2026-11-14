---
title: "is_bad_inode(9)"
name: "is_bad_inode"
section: "9"
letter: "i"
url: "/docs/linux/man/9-is_bad_inode/"
description: "is_bad_inode – is an inode errored"
---

<p>is_bad_inode &#8211; is an inode errored</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool is_bad_inode(struct inode&nbsp;<wbr>*&nbsp;<wbr></code><i>inode</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode to test</dl>
<h2>Description</h2>
<p>Returns true if the inode in question has been marked as bad.</p>
<h2>Copyright</h2>
