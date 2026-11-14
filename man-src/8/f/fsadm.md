---
title: "fsadm(8)"
name: "fsadm"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsadm/"
description: "fsadm — utility to resize or check filesystem on a device"
---

<p>fsadm &#8212; utility to resize or check filesystem on a device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>fsadm</code> [<i>options</i>] <code>check</code> <i>device</i></p>
<dt> <code>fsadm</code> [<i>options</i>] <code>resize</code> <i>device</i> [<i>new_size</i>]</dl>
<h2>Description</h2>
<dd>fsadm utility checks or resizes the filesystem on a device. It tries to use the same API for <code>ext2</code>, <code>ext3</code>, <code>ext4</code>, <code>ReiserFS</code> and <code>XFS</code> filesystem.</p>
<h2>Options</h2>
<dl>
<dt> <code>-e</code>|<code>&#8211;ext-offline</code></p>
<dd>
<dd>Unmount ext2/ext3/ext4 filesystem before doing resize.</p>
<dt> <code>-f</code>|<code>&#8211;force</code></p>
<dd>
<dd>Bypass some sanity checks.</p>
<dt> <code>-h</code>|<code>&#8211;help</code></p>
<dd>
<dd>Display the help text.</p>
<dt> <code>-n</code>|<code>&#8211;dry-run</code></p>
<dd>
<dd>Print commands without running them.</p>
<dt> <code>-v</code>|<code>&#8211;verbose</code></p>
<dd>
<dd>Be more verbose.</p>
<dt> <code>-y</code>|<code>&#8211;yes</code></p>
<dd>
<dd>Answer &quot;yes&quot; at any prompts.</p>
<dt> <code>-c</code>|<code>&#8211;cryptresize</code></p>
<dd>
<dd>Resize dm-crypt mapping together with filesystem detected on the device. The dm-crypt device must be recognizable by <a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8).</p>
<dt> <i>new_size</i>[<code>B</code>|<code>K</code>|<code>M</code>|<code>G</code>|<code>T</code>|<code>P</code>|<code>E</code>]</p>
<dd>
<dd>Absolute number of filesystem blocks to be in the filesystem, or an absolute size using a suffix (in powers of 1024). If new_size is not supplied, the whole device is used.</dl>
<h2>Diagnostics</h2>
<p>On successful completion, the status code is 0. A status code of 2 indicates the operation was interrupted by the user. A status code of 3 indicates the requested check operation could not be performed because the filesystem is mounted and does not support an online <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8). A status code of 1 is used for other failures.</p>
<h2>Examples</h2>
<p>Resize the filesystem on logical volume <i>/dev/vg/test</i> to 1000 megabytes. If <i>/dev/vg/test</i> contains ext2/ext3/ext4 filesystem it will be unmounted prior the resize. All [y/n] questions will be answered &#8216;y&#8217;. </p>
<p> <code>fsadm -e -y resize /dev/vg/test 1000M</code></p>
<h2>Environment Variables</h2>
<dl>
<dt><code>TMPDIR </code></p>
<dd>The temporary directory name for mount points. Defaults to &quot;<i>/tmp</i>&quot;.</p>
<dt><code>DM_DEV_DIR</code></p>
<dd>The device directory name. Defaults to &quot;<i>/dev</i>&quot; and must be an absolute path. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8), <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8), <code><a href="/docs/linux/man/8-resize2fs/">resize2fs</a></code>(8), <code><a href="/docs/linux/man/8-reiserfstune/">reiserfstune</a></code>(8), <code><a href="/docs/linux/man/8-resize_reiserfs/">resize_reiserfs</a></code>(8), <code><a href="/docs/linux/man/8-xfs_info/">xfs_info</a></code>(8), <code><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a></code>(8), <code><a href="/docs/linux/man/8-xfs_check/">xfs_check</a></code>(8), <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8) </p>
