---
title: "e2undo(8)"
name: "e2undo"
section: "8"
letter: "e"
url: "/docs/linux/man/8-e2undo/"
description: "e2undo – Replay an undo log for an ext2/ext3/ext4 file system"
---

<p>e2undo &#8211; Replay an undo log for an ext2/ext3/ext4 file system</p>
<h2>Synopsis</h2>
<p><code>e2undo</code> [ <code>-f</code> ] [ <code>-h</code> ] [ <code>-n</code> ] [ <code>-o</code> <i>offset</i> ] [ <code>-v</code> ] [ <code>-z</code> <i>undo_file</i> ] <i>undo_log device</i></p>
<h2>Description</h2>
<p><code>e2undo</code> will replay the undo log <i>undo_log</i> for an ext2/ext3/ext4 file system found on <i>device</i>. This can be used to undo a failed operation by an e2fsprogs program.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Normally, <code>e2undo</code> will check the file system superblock to make sure the undo log matches with the file system on the device. If they do not match, <code>e2undo</code> will refuse to apply the undo log as a safety mechanism. The <code>-f</code> option disables this safety mechanism.</p>
<dt><code>-h</code></p>
<dd>Display a usage message.</p>
<dt><code>-n</code></p>
<dd>Dry-run; do not actually write blocks back to the file system.</p>
<dt><code>-o</code><i> offset</i></p>
<dd>Specify the file system&#8217;s <i>offset</i> (in bytes) from the beginning of the device or file.</p>
<dt><code>-v</code></p>
<dd>Report which block we&#8217;re currently replaying.</p>
<dt><code>-z</code><i> undo_file</i></p>
<dd>Before overwriting a file system block, write the old contents of the block to an undo file. This undo file can be used with <a href="/docs/linux/man/8-e2undo/">e2undo</a>(8) to restore the old contents of the file system should something go wrong. If the empty string is passed as the undo_file argument, the undo file will be written to a file named e2undo-<i>device</i>.e2undo in the directory specified via the <i>E2FSPROGS_UNDO_DIR</i> environment variable. </p>
<p> WARNING: The undo file cannot be used to recover from a power or system crash.</dl>
<h2>Author</h2>
<p><code>e2undo</code> was written by Aneesh Kumar K.V. (aneesh.kumar [at] linux.vnet.ibm.com)</p>
<h2>Availability</h2>
<p><code>e2undo</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8) </p>
