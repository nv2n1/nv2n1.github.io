---
title: "xfs_admin(8)"
name: "xfs_admin"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_admin/"
description: "xfs_admin – change parameters of an XFS filesystem"
---

<p>xfs_admin &#8211; change parameters of an XFS filesystem</p>
<h2>Synopsis</h2>
<p><code>xfs_admin</code> [ <code>-eflpu</code> ] [ <code>-c 0</code>|<code>1</code> ] [ <code>-L</code> <i>label</i> ] [ <code>-U</code> <i>uuid</i> ] <i>device</i><br />
 <code>xfs_admin -V</code></p>
<h2>Description</h2>
<p><code>xfs_admin</code> uses the <code><a href="/docs/linux/man/8-xfs_db/">xfs_db</a></code>(8) command to modify various parameters of a filesystem. </p>
<p> Devices that are mounted cannot be modified. Administrators must unmount filesystems before <code>xfs_admin</code> or <code><a href="/docs/linux/man/8-xfs_db/">xfs_db</a></code>(8) can convert parameters. A number of parameters of a mounted filesystem can be examined and modified using the <code><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a></code>(8) command.</p>
<h2>Options</h2>
<dl>
<dt><code>-e</code></p>
<dd>Enables unwritten extent support on a filesystem that does not already have this enabled (for legacy filesystems, it can&#8217;t be disabled anymore at mkfs time).</p>
<dt><code>-f</code></p>
<dd>Specifies that the filesystem image to be processed is stored in a regular file at <i>device</i> (see the <code>mkfs.xfs -d</code> <i>file</i> option).</p>
<dt><code>-j</code></p>
<dd>Enables version 2 log format (journal format supporting larger log buffers).</p>
<dt><code>-l</code></p>
<dd>Print the current filesystem label.</p>
<dt><code>-p</code></p>
<dd>Enable 32bit project identifier support (PROJID32BIT feature).</p>
<dt><code>-u</code></p>
<dd>Print the current filesystem UUID (Universally Unique IDentifier).</p>
<dt><code>-c 0</code>|<code>1</code></p>
<dd>Enable (1) or disable (0) lazy-counters in the filesystem.</p>
<dd>Lazy-counters may not be disabled on Version 5 superblock filesystems (i.e. those with metadata CRCs enabled).</p>
<dd>This operation may take quite a bit of time on large filesystems as the entire filesystem needs to be scanned when this option is changed.</p>
<dd>With lazy-counters enabled, the superblock is not modified or logged on every change of the free-space and inode counters. Instead, enough information is kept in other parts of the filesystem to be able to maintain the counter values without needing to keep them in the superblock. This gives significant improvements in performance on some configurations and metadata intensive workloads.</p>
<dt><code>-L</code><i> label</i></p>
<dd>Set the filesystem label to <i>label</i>. XFS filesystem labels can be at most 12 characters long; if <i>label</i> is longer than 12 characters, <code>xfs_admin</code> will truncate it and print a warning message. The filesystem label can be cleared using the special &quot;<code>&#8212;</code>&quot; value for <i>label</i>.</p>
<dt><code>-U</code><i> uuid</i></p>
<dd>Set the UUID of the filesystem to <i>uuid</i>. A sample UUID looks like this: &quot;c1b9d5a2-f162-11cf-9ece-0020afc76f16&quot;. The <i>uuid</i> may also be <code>nil</code>, which will set the filesystem UUID to the null UUID. The <i>uuid</i> may also be <code>generate</code>, which will generate a new UUID for the filesystem. Note that on CRC-enabled filesystems, this will set an incompatible flag such that older kernels will not be able to mount the filesystem. To remove this incompatible flag, use <code>restore</code>, which will restore the original UUID and remove the incompatible feature flag as needed.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.</dl>
<p> The <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) manual entry describes how to mount a filesystem using its label or UUID, rather than its block special device name.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-xfs_db/">xfs_db</a></code>(8), <code><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a></code>(8), <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5). </p>
