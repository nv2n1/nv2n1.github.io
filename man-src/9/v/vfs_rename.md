---
title: "vfs_rename(9)"
name: "vfs_rename"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfs_rename/"
description: "vfs_rename – rename a filesystem object"
---

<p>vfs_rename &#8211; rename a filesystem object</p>
<h2>Synopsis</h2>
<pre><code>int vfs_rename(struct inode *old_dir, struct dentry *old_dentry, struct inode *new_dir, struct dentry *new_dentry, struct inode **delegated_inode, unsigned int flags);</code></pre>
<h2>Arguments</h2>
<p><i>old_dir</i></p>
<dl>
<dd>
<dd>parent of source</dl>
<p> <i>old_dentry</i></p>
<dl>
<dd>source</dl>
<p> <i>new_dir</i></p>
<dl>
<dd>parent of destination</dl>
<p> <i>new_dentry</i></p>
<dl>
<dd>destination</dl>
<p> <i>delegated_inode</i></p>
<dl>
<dd>returns an inode needing a delegation break</dl>
<p> <i>flags</i></p>
<dl>
<dd>rename flags</dl>
<h2>Description</h2>
<p>The caller must hold multiple mutexes&#8211;see <code>lock_rename</code>). </p>
<p> If vfs_rename discovers a delegation in need of breaking at either the source or destination, it will return -EWOULDBLOCK and return a reference to the inode in delegated_inode. The caller should then break the delegation and retry. Because breaking a delegation may take a long time, the caller should drop all locks before doing so. </p>
<p> Alternatively, a caller may pass NULL for delegated_inode. This may be appropriate for callers that expect the underlying filesystem not to be NFS exported. </p>
<p> The worst of all namespace operations &#8211; renaming directory. &#8220;Perverted&#8221; doesn&#8217;t even start to describe it. Somebody in UCB had a heck of a trip&#8230; Problems: a) we can get into loop creation. b) race potential &#8211; two innocent renames can create a loop together. That&#8217;s where 4.4 screws up. Current fix: serialization on sb-&gt;s_vfs_rename_mutex. We might be more accurate, but that&#8217;s another story. c) we have to lock _four_ objects &#8211; parents and victim (if it exists), and source (if it is not a directory). And that &#8211; after we got -&gt;i_mutex on parents (until then we don&#8217;t know whether the target exists). Solution: try to be smart with locking order for inodes. We rely on the fact that tree topology may change only under -&gt;s_vfs_rename_mutex _and_ that parent of the object we move will be locked. Thus we can rank directories by the tree (ancestors first) and rank all non-directories after them. That works since everybody except rename does &#8220;lock parent, lookup, lock child&#8221; and rename is under -&gt;s_vfs_rename_mutex. HOWEVER, it relies on the assumption that any object with -&gt;<code>lookup</code> has no more than 1 dentry. If &#8220;hybrid&#8221; objects will ever appear, we&#8217;d better make sure that there&#8217;s no <a href="/docs/linux/man/2-link/">link</a>(2) for them. d) conversion from fhandle to dentry may come in the wrong moment &#8211; when we are removing the target. Solution: we will have to grab -&gt;i_mutex in the fhandle_to_dentry code. [FIXME &#8211; current nfsfh.c relies on -&gt;i_mutex on parents, which works but leads to some truly excessive locking].</p>
<h2>Copyright</h2>
