---
title: "lease_get_mtime(9)"
name: "lease_get_mtime"
section: "9"
letter: "l"
url: "/docs/linux/man/9-lease_get_mtime/"
---

lease_get_mtime - get the last modified time of an inode

<h2>Synopsis</h2>

<pre><code>void lease_get_mtime(struct inode *inode, struct timespec *time);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>the inode</dl>
 

 <i>time</i>
<dl><dd>pointer to a timespec which will contain the last modified time</dl>

<h2>Description</h2>

This is to force NFS clients to flush their caches for files with exclusive leases. The justification is that if someone has an exclusive lease, then they could be modifying it.

<h2>Copyright</h2>


