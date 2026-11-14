---
title: "inode_owner_or_capable(9)"
name: "inode_owner_or_capable"
section: "9"
letter: "i"
url: "/docs/linux/man/9-inode_owner_or_capable/"
description: "inode_owner_or_capable – check current task permissions to inode"
---

<p>inode_owner_or_capable &#8211; check current task permissions to inode</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool inode_owner_or_capable(const struct inode&nbsp;<wbr>*&nbsp;<wbr></code><i>inode</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode being checked</dl>
<h2>Description</h2>
<p>Return true if current either has CAP_FOWNER in a namespace with the inode owner uid mapped, or owns the file.</p>
<h2>Copyright</h2>
