---
title: "defrag-f2fs(8)"
name: "defrag-f2fs"
section: "8"
letter: "d"
url: "/docs/linux/man/8-defrag-f2fs/"
description: "defrag.f2fs – relocate blocks in a given area to the specified region"
---

<p>defrag.f2fs &#8211; relocate blocks in a given area to the specified region</p>
<h2>Synopsis</h2>
<p><code>defrag.f2fs</code> [ <code>-s</code> <i>start block address</i> ] [ <code>-l</code> <i>number of blocks</i> ] [ <code>-t</code> <i>target block address</i> ] [ <code>-i</code> <i>direction</i> ] [ <code>-d</code> <i>debugging-level</i> ] <i>device</i></p>
<h2>Description</h2>
<p><code>defrag.f2fs</code> is used to move specified number of blocks starting from a given block address to the target block address with a direction. <i>device</i> is the special file corresponding to the device (e.g. <i>/dev/sdXX</i>). </p>
<p> For example, # defrag.f2fs -s 0x4000 -l 0x100 -t 0x10000 -i /dev/sdb1 </p>
<p> This moves blocks between 0x4000 and 0x4100 to the left-hand area of 0x10000. </p>
<p> The exit code returned by <code>defrag.f2fs</code> is 0 on success and -1 on failure.</p>
<h2>Options</h2>
<dl>
<dt><code>-s</code><i> start block address</i></p>
<dd>Specify the starting block address.</p>
<dt><code>-l</code><i> number of blocks</i></p>
<dd>Specifiy the number of blocks to move.</p>
<dt><code>-t</code><i> target block address</i></p>
<dd>Specify the destination block address.</p>
<dt><code>-i</code><i> direction</i></p>
<dd>Set the direction to left. If it is not set, the direction becomes right by default.</p>
<dt><code>-d</code><i> debug-level</i></p>
<dd>Specify the level of debugging options. The default number is 0, which shows basic debugging messages.</p>
<dt></dl>
<h2>Author</h2>
<dd>This version of <code>defrag.f2fs</code> has been written by Jaegeuk Kim &lt;jaegeuk [at] kernel.org&gt;.</p>
<h2>Availability</h2>
<p><code>defrag.f2fs</code> is available from <a href="git://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git.">git://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-f2fs/">mkfs.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-dump-f2fs/">dump.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-fsck-f2fs/">fsck.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-resize-f2fs/">resize.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-sload-f2fs/">sload.f2fs</a>(8).</code> </p>
