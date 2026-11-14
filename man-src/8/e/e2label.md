---
title: "e2label(8)"
name: "e2label"
section: "8"
letter: "e"
url: "/docs/linux/man/8-e2label/"
description: "e2label – Change the label on an ext2/ext3/ext4 file system"
---

<p>e2label &#8211; Change the label on an ext2/ext3/ext4 file system</p>
<h2>Synopsis</h2>
<p><code>e2label</code> <i>device</i> [ <i>volume-label</i> ]</p>
<h2>Description</h2>
<p><code>e2label</code> will display or change the volume label on the ext2, ext3, or ext4 file system located on <i>device.</i> If the optional argument <i>volume-label</i> is not present, <code>e2label</code> will simply display the current volume label. If the optional argument <i>volume-label</i> is present, then <code>e2label</code> will set the volume label to be <i>volume-label</i>. Ext2 volume labels can be at most 16 characters long; if <i>volume-label</i> is longer than 16 characters, <code>e2label</code> will truncate it and print a warning message. It is also possible to set the volume label using the <code>-L</code> option of <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8). </p>
<h2>Author</h2>
<p><code>e2label</code> was written by Theodore Ts&#8217;o (tytso [at] mit.edu).</p>
<h2>Availability</h2>
<p><code>e2label</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8) </p>
