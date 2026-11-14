---
title: "inode_permission(9)"
name: "inode_permission"
section: "9"
letter: "i"
url: "/docs/linux/man/9-inode_permission/"
description: "inode_permission – Check for access rights to a given inode"
---

<p>inode_permission &#8211; Check for access rights to a given inode</p>
<h2>Synopsis</h2>
<pre><code>int inode_permission(struct inode *inode, int mask);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>Inode to check permission on</dl>
<p> <i>mask</i></p>
<dl>
<dd>Right to check for (<code>MAY_READ</code>, <code>MAY_WRITE</code>, <code>MAY_EXEC</code>)</dl>
<h2>Description</h2>
<p>Check for read/write/execute permissions on an inode. We use fs[ug]id for this, letting us set arbitrary permissions for filesystem access without changing the &#8220;normal&#8221; UIDs which are used for other things. </p>
<p> When checking for MAY_APPEND, MAY_WRITE must also be set in <i>mask</i>.</p>
<h2>Copyright</h2>
