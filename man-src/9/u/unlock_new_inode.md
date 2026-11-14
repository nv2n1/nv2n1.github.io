---
title: "unlock_new_inode(9)"
name: "unlock_new_inode"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unlock_new_inode/"
---

unlock_new_inode - clear the I_NEW state and wake up any waiters

<h2>Synopsis</h2>

<pre><code>void unlock_new_inode(struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>new inode to unlock</dl>

<h2>Description</h2>

Called when the inode is fully initialised to clear the new state of the inode and wake up anyone waiting for the inode to finish initialisation.

<h2>Copyright</h2>


