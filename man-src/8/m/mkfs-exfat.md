---
title: "mkfs-exfat(8)"
name: "mkfs-exfat"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-exfat/"
description: "mkexfatfs – create an exFAT file system"
---

<p><code>mkexfatfs</code> &#8211; create an exFAT file system</p>
<h2>Synopsis</h2>
<p><code>mkexfatfs</code> [ <code>-i</code> <i>volume-id</i> ] [ <code>-n</code> <i>volume-name</i> ] [ <code>-p</code> <i>partition-first-sector</i> ] [ <code>-s</code> <i>sectors-per-cluster</i> ] [ <code>-V</code> ] <i>device</i> </p>
<h2>Description</h2>
<p><code>mkexfatfs</code> creates an exFAT file system on a block device. <i>device</i> is a special file corresponding to the partition on the device. Note that if this is an MBR partition then the file system type should be set to 0x07 (NTFS/exFAT) otherwise other operating systems may refuse to mount the file system. </p>
<h2>Options</h2>
<p>Command line options available:</p>
<dl>
<dt><code>-i</code><i> volume-id</i></p>
<dd>A 32-bit hexadecimal number. By default a value based on current time is set.</p>
<dt><code>-n</code><i> volume-name</i></p>
<dd>Volume name (label), up to 15 characters. By default no label is set.</p>
<dt><code>-p</code><i> partition-first-sector</i></p>
<dd>First sector of the partition starting from the beginning of the whole disk. exFAT super block has a field for this value but in fact it&#8217;s optional and does not affect anything. Default is 0.</p>
<dt><code>-s</code><i> sectors-per-cluster</i></p>
<dd>Number of physical sectors per cluster (cluster is an allocation unit in exFAT). Must be a power of 2, i.e. 1, 2, 4, 8, etc. Cluster size can not exceed 32 MB. Default cluster sizes are: 4 KB if volume size is less than 256 MB, 32 KB if volume size is from 256 MB to 32 GB, 128 KB if volume size is 32 GB or larger.</p>
<dt><code>-V</code></p>
<dd>Print version and copyright. </p>
</dl>
<h2>Exit Codes</h2>
<p>Zero is returned on successful creation. Any other code means an error.</p>
<h2>Author</h2>
<p>Andrew Nayenko</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8),<code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) </p>
