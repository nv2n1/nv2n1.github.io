---
title: "mkfs-hfsplus(8)"
name: "mkfs-hfsplus"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-hfsplus/"
description: "mkfs.hfsplus – construct a new HFS Plus file system"
---

<p><code>mkfs.hfsplus</code> &#8211; construct a new HFS Plus file system</p>
<h2>Synopsis</h2>
<p><code>mkfs.hfsplus</code> [-<code>N</code> ] [-<code>U </code><i>uid</i> ] [-<code>G </code><i>gid</i> ] [-<code>M </code><i>mask</i> ] [-<code>P</code> ] [-<code>s</code> ] [-<code>b </code><i>block-size</i> ] [-<code>c </code><i>clump-size-list</i> ] [-<code>i </code><i>first-cnid</i> ] [-<code>J </code><i>[journal-size]</i> ] [-<code>n </code><i>node-size-list</i> ] [-<code>v </code><i>volume-name</i> ] <i>special</i><br />
<code>mkfs.hfsplus</code> &#8211;<code>N </code><i>partition-size</i> [-<code>U </code><i>uid</i> ] [-<code>G </code><i>gid</i> ] [-<code>M </code><i>mask</i> ] [-<code>P</code> ] [-<code>h | w</code> ] [-<code>s</code> ] [-<code>b </code><i>block-size</i> ] [-<code>c </code><i>clump-size-list</i> ] [-<code>i </code><i>first-cnid</i> ] [-<code>J </code><i>[journal-size]</i> ] [-<code>n </code><i>node-size-list</i> ] [-<code>v </code><i>volume-name</i> ]</p>
<h2>Description</h2>
<p><code>mkfs.hfsplus</code> builds an HFS Plus file system on the specified special device. Before running <code>mkfs.hfsplus</code> the disk should be partitioned using the <i>Disk Utility</i> application or <a href="/docs/linux/man/8-pdisk/">pdisk</a>(8). The file system default parameters are calculated based on the size of the disk partition. Typically the defaults are reasonable, however <code>mkfs.hfsplus</code> has several options to allow the defaults to be selectively overridden. The options are as follows:</p>
<dl>
<dt><code>-N </code><i>[partition-size]</i></p>
<dd>Causes the file system parameters to be printed out without really creating the file system. If the argument following the &#8211;<code>N</code> starts with a decimal digit, it is assumed to be a partition size. The paritition size may be given in decimal, octal (with leading `0&#8242;), or hexadecimal (with leading `0x&#8217;). The partition size argument can be specified in 512-byte blocks (with a `b&#8217; suffix), petabytes (`p&#8217; suffix), terabytes (`t&#8217; suffix), gigabytes (`g&#8217; suffix), megabytes (`m&#8217; suffix), or kilobytes (`k&#8217; suffix). All suffixes indicate binary, not decimal, multipliers (e.g., `1k&#8217; is 1024 bytes). If no suffix is specified, the value is assumed to be in bytes; if an illegal suffix is specified, it results in a size of 0 bytes. If the partition size is given, then no special device argument shall be provided. If no partition size is given, then the size of the given special device is used instead, and the special device will not be written to.</p>
<dt><code>-U </code><i>uid</i></p>
<dd>Set the owner of the file system&#8217;s root directory to uid</p>
<dt><code>-G </code><i>gid</i></p>
<dd>Set the group of the file system&#8217;s root directory to gid</p>
<dt><code>-M </code><i>mask</i></p>
<dd>Specify the octal access permissions mask for the file system&#8217;s root directory.</p>
<dt><code>-P</code></p>
<dd>Set kHFSContentProtectionBit in the volume&#8217;s attributes, which will cause the volume to be mounted with the &quot;protect&quot; option if the kernel supports it.</p>
<dt><code>-s</code></p>
<dd>Creates a case-sensitive HFS Plus filesystem. By default a case-insensitive filesystem is created. Case-sensitive HFS Plus file systems require a Mac OS X version of 10.3 (Darwin 7.0) or later.</p>
<dt><code>-b </code><i>block-size</i></p>
<dd>The allocation block size of the file system. The default value is 4096.</p>
<dt><code>-c </code><i>clump-size-list</i></p>
<dd>This specifies the <i>clump</i> and/or <i>initial</i> sizes, in allocation blocks, for the various metadata files. <i>Clump</i> sizes are specified with the &#8211;<code>c</code> option followed by a comma separated list of the form arg=blocks. Example: -c c=5000,e=500</p>
<dl>
<dt><i>a=blocks</i></p>
<dd>Set the attribute file clump size.</p>
<dt><i>b=blocks</i></p>
<dd>Set the allocation bitmap file clump size.</p>
<dt><i>c=blocks</i></p>
<dd>Set the catalog file clump size.</p>
<dt><i>d=blocks</i></p>
<dd>Set the data fork clump size.</p>
<dt><i>e=blocks</i></p>
<dd>Set the extent overflow file clump size.</p>
<dt><i>r=blocks</i></p>
<dd>Set the resource fork clump size.</dl>
<dt><code>-i </code><i>first-cnid</i></p>
<dd>This specifies the initial catalog node ID for user files and directories. The default value is 16.</p>
<dt><code>-J </code><i>[journal-size]</i></p>
<dd>Creates a journaled HFS+ volume. The default journal size varies, based on the size of the volume. Appending an &#8216;M&#8217; to the journal size implies megabytes (i.e. 64M is 64 megabytes). The maximum journal size is 1024 megabytes.</p>
<dt><code>-n </code><i>node-size-list</i></p>
<dd>This specifies the b-tree <i>node</i> sizes, in bytes, for the various b-tree files. <i>Node</i> sizes are specified with the &#8211;<code>n</code> option followed by a comma separated list of the form arg=bytes. The <i>node</i> size must be a power of two and no larger than 32768 bytes. Example: -n c=8192,e=4096</p>
<dl>
<dt><i>a=bytes</i></p>
<dd>Set the attribute b-tree node size.</p>
<dt><i>c=bytes</i></p>
<dd>Set the catalog b-tree node size.</p>
<dt><i>e=bytes</i></p>
<dd>Set the extent overflow b-tree node size.</dl>
<dt><code>-v </code><i>volume-name</i></p>
<dd>Volume name (file system name) in ascii or UTF-8 format.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mount/">mount</a>(8), <a href="/docs/linux/man/8-pdisk/">pdisk</a>(8)</p>
<h2>History</h2>
<p>The <code>mkfs.hfsplus</code> command appeared in Mac OS X Server 1.0 . As of Mac OS X 10.6, this utility no longer generates HFS standard file systems.</p>
