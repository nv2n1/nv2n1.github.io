---
title: "freeze_super(9)"
name: "freeze_super"
section: "9"
letter: "f"
url: "/docs/linux/man/9-freeze_super/"
description: "freeze_super – lock the filesystem and force it into a consistent state"
---

<p>freeze_super &#8211; lock the filesystem and force it into a consistent state</p>
<h2>Synopsis</h2>
<pre><code>int freeze_super(struct super_block *sb);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>the super to lock</dl>
<h2>Description</h2>
<p>Syncs the super to make sure the filesystem is consistent and calls the fs&#8217;s freeze_fs. Subsequent calls to this without first thawing the fs will return -EBUSY. </p>
<p> During this function, sb-&gt;s_writers.frozen goes through these values: </p>
<p> SB_UNFROZEN: File system is normal, all writes progress as usual. </p>
<p> SB_FREEZE_WRITE: The file system is in the process of being frozen. New writes should be blocked, though page faults are still allowed. We wait for all writes to complete and then proceed to the next stage. </p>
<p> SB_FREEZE_PAGEFAULT: Freezing continues. Now also page faults are blocked but internal fs threads can still modify the filesystem (although they should not dirty new pages or inodes), writeback can run etc. After waiting for all running page faults we sync the filesystem which will clean all dirty pages and inodes (no new dirty pages or inodes can be created when sync is running). </p>
<p> SB_FREEZE_FS: The file system is frozen. Now all internal sources of fs modification are blocked (e.g. XFS preallocation truncation on inode reclaim). This is usually implemented by blocking new transactions for filesystems that have them and need this additional guard. After all internal writers are finished we call -&gt;<code>freeze_fs</code> to finish filesystem freezing. Then we transition to SB_FREEZE_COMPLETE state. This state is mostly auxiliary for filesystems to verify they do not modify frozen fs. </p>
<p> sb-&gt;s_writers.frozen is protected by sb-&gt;s_umount.</p>
<h2>Copyright</h2>
