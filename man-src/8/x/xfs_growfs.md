---
title: "xfs_growfs(8)"
name: "xfs_growfs"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_growfs/"
description: "xfs_growfs, xfs_info – expand an XFS filesystem"
---

<p>xfs_growfs, xfs_info &#8211; expand an XFS filesystem</p>
<h2>Synopsis</h2>
<p><code>xfs_growfs</code> [ <code>-dilnrx</code> ] [ <code>-D</code> <i>size</i> ] [ <code>-e</code> <i>rtextsize</i> ] [ <code>-L</code> <i>size</i> ] [ <code>-m</code> <i>maxpct</i> ] [ <code>-t</code> <i>mtab</i> ] [ <code>-R</code> <i>size</i> ] <i>mount-point</i><br />
 <code>xfs_growfs -V</code> </p>
<p> <code>xfs_info</code> [ <code>-t</code> <i>mtab</i> ] <i>mount-point</i><br />
 <code>xfs_info -V</code></p>
<h2>Description</h2>
<p><code>xfs_growfs</code> expands an existing XFS filesystem (see <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5)). The <i>mount-point</i> argument is the pathname of the directory where the filesystem is mounted. The filesystem must be mounted to be grown (see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)). The existing contents of the filesystem are undisturbed, and the added space becomes available for additional file storage. </p>
<p> <code>xfs_info</code> is equivalent to invoking <code>xfs_growfs</code> with the <code>-n</code> option (see discussion below).</p>
<h2>Options</h2>
<dl>
<dt><code>-d | -D </code><i>size</i></p>
<dd>Specifies that the data section of the filesystem should be grown. If the <code>-D</code> <i>size</i> option is given, the data section is grown to that <i>size</i>, otherwise the data section is grown to the largest size possible with the <code>-d</code> option. The size is expressed in filesystem blocks.</p>
<dt><code>-e</code></p>
<dd>Allows the real-time extent size to be specified. In <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) this is specified with <code>-r extsize=</code><i>nnnn</i>.</p>
<dt><code>-i</code></p>
<dd>The new log is an internal log (inside the data section). <code>[NOTE: This option is not implemented]</code></p>
<dt><code>-l | -L </code><i>size</i></p>
<dd>Specifies that the log section of the filesystem should be grown, shrunk, or moved. If the <code>-L</code> <i>size</i> option is given, the log section is changed to be that <i>size</i>, if possible. The size is expressed in filesystem blocks. The size of an internal log must be smaller than the size of an allocation group (this value is printed at <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8) time). If neither <code>-i</code> nor <code>-x</code> is given with <code>-l</code>, the log continues to be internal or external as it was before. <code>[NOTE: These options are not implemented]</code></p>
<dt><code>-m</code></p>
<dd>Specify a new value for the maximum percentage of space in the filesystem that can be allocated as inodes. In <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) this is specified with <code>-i maxpct=</code><i>nn</i>.</p>
<dt><code>-n</code></p>
<dd>Specifies that no change to the filesystem is to be made. The filesystem geometry is printed, and argument checking is performed, but no growth occurs. <code>See output examples below.</code></p>
<dt><code>-r | -R </code><i>size</i></p>
<dd>Specifies that the real-time section of the filesystem should be grown. If the <code>-R</code> <i>size</i> option is given, the real-time section is grown to that size, otherwise the real-time section is grown to the largest size possible with the <code>-r</code> option. The size is expressed in filesystem blocks. The filesystem does not need to have contained a real-time section before the <code>xfs_growfs</code> operation.</p>
<dt><code>-t</code></p>
<dd>Specifies an alternate mount table file (default is <i>/proc/mounts</i> if it exists, else <i>/etc/mtab</i>). This is used when working with filesystems mounted without writing to <i>/etc/mtab</i> file &#8211; refer to <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) for further details.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits. The <i>mount-point</i> argument is not required with <code>-V</code>.</dl>
<p> <code>xfs_growfs</code> is most often used in conjunction with logical volumes (see <code><a href="/docs/linux/man/4-md/">md</a></code>(4) and <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) on Linux). However, it can also be used on a regular disk partition, for example if a partition has been enlarged while retaining the same starting block.</p>
<h2>Practical Use</h2>
<p>Filesystems normally occupy all of the space on the device where they reside. In order to grow a filesystem, it is necessary to provide added space for it to occupy. Therefore there must be at least one spare new disk partition available. Adding the space is often done through the use of a logical volume manager.</p>
<h2>Examples</h2>
<p>Understanding xfs_info output. </p>
<p> Suppose one has the following &quot;xfs_info /dev/sda&quot; output: </p>
<dl>
<dd>
<pre>meta-data=/dev/sda isize=256 agcount=32, agsize=16777184 blks
 = sectsz=512 attr=2
data = bsize=4096 blocks=536869888, imaxpct=5
 = sunit=32 swidth=128 blks
naming =version 2 bsize=4096
log =internal bsize=4096 blocks=32768, version=2
 = sectsz=512 sunit=32 blks, lazy-count=1
realtime =none extsz=524288 blocks=0, rtextents=0</pre>
</dl>
<p> Here, the data section of the output indicates &quot;bsize=4096&quot;, meaning the data block size for this filesystem is 4096 bytes. This section also shows &quot;sunit=32 swidth=128 blks&quot;, which means the stripe unit is 32*4096 bytes = 128 kibibytes and the stripe width is 128*4096 bytes = 512 kibibytes. A single stripe of this filesystem therefore consists of four stripe units (128 blocks / 32 blocks per unit).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/4-md/">md</a></code>(4), <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
