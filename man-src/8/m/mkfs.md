---
title: "mkfs(8)"
name: "mkfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs/"
description: "mkfs – build a Linux filesystem"
---

<p>mkfs &#8211; build a Linux filesystem</p>
<h2>Synopsis</h2>
<p><code>mkfs</code> [options] [<code>-t</code> <i>type</i>] [<i>fs-options</i>] <i>device</i> [<i>size</i>]</p>
<h2>Description</h2>
<p><code>This mkfs frontend is deprecated in favour of filesystem specific mkfs.&lt;type&gt; utils.</code> </p>
<p> <code>mkfs</code> is used to build a Linux filesystem on a device, usually a hard disk partition. The <i>device</i> argument is either the device name (e.g., <i>/dev/hda1</i>, <i>/dev/sdb2</i>), or a regular file that shall contain the filesystem. The <i>size</i> argument is the number of blocks to be used for the filesystem. </p>
<p> The exit status returned by <code>mkfs</code> is 0 on success and 1 on failure. </p>
<p> In actuality, <code>mkfs</code> is simply a front-end for the various filesystem builders (<code>mkfs.</code><i>fstype</i>) available under Linux. The filesystem-specific builder is searched for via your <code>PATH</code> environment setting only. Please see the filesystem-specific builder manual pages for further details.</p>
<h2>Options</h2>
<p><code>-t</code>, <code>&#8211;type</code> <i>type</i></p>
<dl>
<dd>Specify the <i>type</i> of filesystem to be built. If not specified, the default filesystem type (currently ext2) is used.</dl>
<p> <i>fs-options</i></p>
<dl>
<dd>Filesystem-specific options to be passed to the real filesystem builder.</dl>
<p> <code>-V</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Produce verbose output, including all filesystem-specific commands that are executed. Specifying this option more than once inhibits execution of any filesystem-specific commands. This is really only useful for testing.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit. (Option <code>-V</code> will display version information only when it is the only parameter, otherwise it will work as <code>&#8211;verbose</code>.)</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Bugs</h2>
<p>All generic options must precede and not be combined with filesystem-specific options. Some filesystem-specific programs do not automatically detect the device size and require the <i>size</i> parameter to be specified.</p>
<h2>Authors</h2>
<p>The manual page was shamelessly adapted from Remy Card&#8217;s version for the ext2 filesystem.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-fs/">fs</a></code>(5), <code><a href="/docs/linux/man/8-badblocks/">badblocks</a></code>(8), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-mkdosfs/">mkdosfs</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-bfs/">mkfs.bfs</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-ext2/">mkfs.ext2</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-ext3/">mkfs.ext3</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-ext4/">mkfs.ext4</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-minix/">mkfs.minix</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-msdos/">mkfs.msdos</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-vfat/">mkfs.vfat</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>mkfs</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
