---
title: "fsck-f2fs(8)"
name: "fsck-f2fs"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck-f2fs/"
description: "fsck.f2fs – check a Linux F2FS file system"
---

<p>fsck.f2fs &#8211; check a Linux F2FS file system</p>
<h2>Synopsis</h2>
<p><code>fsck.f2fs</code> [ <code>-a</code> <i>enable auto fix</i> ] [ <code>-f</code> <i>enable force fix</i> ] [ <code>-p</code> <i>enable preen mode</i> ] [ <code>-t</code> <i>show stored directory tree</i> ] [ <code>-d</code> <i>debugging-level</i> ] <i>device</i></p>
<h2>Description</h2>
<p><code>fsck.f2fs</code> is used to check an f2fs file system (usually in a disk partition). <i>device</i> is the special file corresponding to the device (e.g. <i>/dev/sdXX</i>). </p>
<p> The exit code returned by <code>fsck.f2fs</code> is 0 on success and -1 on failure.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code><i> enable auto fix</i></p>
<dd>Enable to run file system check only if a bug was reported by the F2FS kernel module. It is disabled by default.</p>
<dt><code>-f</code><i> enable force fix</i></p>
<dd>Enable to fix all the inconsistency in the partition.</p>
<dt><code>-p</code><i> enable preen mode</i></p>
<dd>Same as &quot;-a&quot; to support general fsck convention.</p>
<dt><code>-t</code><i> show stored directory tree</i></p>
<dd>Enable to show every directory entries in the partition.</p>
<dt><code>-d</code><i> debug-level</i></p>
<dd>Specify the level of debugging options. The default number is 0, which shows basic debugging messages.</p>
<dt></dl>
<h2>Author</h2>
<dd>Initial checking code was written by Byoung Geun Kim &lt;bgbg.kim [at] samsung.com&gt;. Jaegeuk Kim &lt;jaegeuk [at] kernel.org&gt; reworked most parts of the codes to support fixing any corrupted images.</p>
<h2>Availability</h2>
<p><code>fsck.f2fs</code> is available from <a href="git://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git.">git://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-f2fs/">mkfs.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-dump-f2fs/">dump.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-defrag-f2fs/">defrag.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-resize-f2fs/">resize.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-sload-f2fs/">sload.f2fs</a>(8).</code> </p>
