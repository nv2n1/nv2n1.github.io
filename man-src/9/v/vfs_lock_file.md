---
title: "vfs_lock_file(9)"
name: "vfs_lock_file"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfs_lock_file/"
description: "vfs_lock_file – file byte range lock"
---

<p>vfs_lock_file &#8211; file byte range lock</p>
<h2>Synopsis</h2>
<pre><code>int vfs_lock_file(struct file *filp, unsigned int cmd, struct file_lock *fl, struct file_lock *conf);</code></pre>
<h2>Arguments</h2>
<p><i>filp</i></p>
<dl>
<dd>
<dd>The file to apply the lock to</dl>
<p> <i>cmd</i></p>
<dl>
<dd>type of locking operation (F_SETLK, F_GETLK, etc.)</dl>
<p> <i>fl</i></p>
<dl>
<dd>The lock to be applied</dl>
<p> <i>conf</i></p>
<dl>
<dd>Place to return a copy of the conflicting lock, if found.</dl>
<h2>Description</h2>
<p>A caller that doesn&#8217;t care about the conflicting lock may pass NULL as the final argument. </p>
<p> If the filesystem defines a private -&gt;<code>lock</code> method, then <i>conf</i> will be left unchanged; so a caller that cares should initialize it to some acceptable default. </p>
<p> To avoid blocking kernel daemons, such as lockd, that need to acquire POSIX locks, the -&gt;<code>lock</code> interface may return asynchronously, before the lock has been granted or denied by the underlying filesystem, if (and only if) lm_grant is set. Callers expecting -&gt;<code>lock</code> to return asynchronously will only use F_SETLK, not F_SETLKW; they will set FL_SLEEP if (and only if) the request is for a blocking lock. When -&gt;<code>lock</code> does return asynchronously, it must return FILE_LOCK_DEFERRED, and call -&gt;<code>lm_grant</code> when the lock request completes. If the request is for non-blocking lock the file system should return FILE_LOCK_DEFERRED then try to get the lock and call the callback routine with the result. If the request timed out the callback routine will return a nonzero return code and the file system should release the lock. The file system is also responsible to keep a corresponding posix lock when it grants a lock so the VFS can find out which locks are locally held and do the correct lock cleanup when required. The underlying filesystem must not drop the kernel lock or call -&gt;<code>lm_grant</code> before returning to the caller with a FILE_LOCK_DEFERRED return code.</p>
<h2>Copyright</h2>
