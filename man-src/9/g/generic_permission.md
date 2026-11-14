---
title: "generic_permission(9)"
name: "generic_permission"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_permission/"
description: "generic_permission – check for access rights on a Posix-like filesystem"
---

<p>generic_permission &#8211; check for access rights on a Posix-like filesystem</p>
<h2>Synopsis</h2>
<pre><code>int generic_permission(struct inode *inode, int mask);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode to check access rights for</dl>
<p> <i>mask</i></p>
<dl>
<dd>right to check for (<code>MAY_READ</code>, <code>MAY_WRITE</code>, <code>MAY_EXEC</code>, &#8230;)</dl>
<h2>Description</h2>
<p>Used to check for read/write/execute permissions on a file. We use &#8220;fsuid&#8221; for this, letting us set arbitrary permissions for filesystem access without changing the &#8220;normal&#8221; uids which are used for other things. </p>
<p> generic_permission is rcu-walk aware. It returns -ECHILD in case an rcu-walk request cannot be satisfied (eg. requires blocking or too much complexity). It would then be called again in ref-walk mode.</p>
<h2>Copyright</h2>
