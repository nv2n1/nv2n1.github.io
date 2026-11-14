---
title: "d_obtain_alias(9)"
name: "d_obtain_alias"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_obtain_alias/"
description: "d_obtain_alias – find or allocate a DISCONNECTED dentry for a given inode"
---

<p>d_obtain_alias &#8211; find or allocate a DISCONNECTED dentry for a given inode</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *d_obtain_alias(struct inode *inode);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode to allocate the dentry for</dl>
<h2>Description</h2>
<p>Obtain a dentry for an inode resulting from NFS filehandle conversion or similar open by handle operations. The returned dentry may be anonymous, or may have a full name (if the inode was already in the cache). </p>
<p> When called on a directory inode, we must ensure that the inode only ever has one dentry. If a dentry is found, that is returned instead of allocating a new one. </p>
<p> On successful return, the reference to the inode has been transferred to the dentry. In case of an error the reference on the inode is released. To make it easier to use in export operations a <code>NULL</code> or IS_ERR inode may be passed in and the error will be propagated to the return value, with a <code>NULL</code><i>inode</i> replaced by ERR_PTR(-ESTALE).</p>
<h2>Copyright</h2>
