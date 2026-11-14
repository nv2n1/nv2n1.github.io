---
title: "btrfs-convert(8)"
name: "btrfs-convert"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-convert/"
description: "btrfs-convert – convert from ext2/3/4 or reiserfs filesystem to btrfs in-place"
---

<p>btrfs-convert &#8211; convert from ext2/3/4 or reiserfs filesystem to btrfs in-place</p>
<h2>Synopsis</h2>
<p><code>btrfs-convert</code> [options] <i>&lt;device&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs-convert</code> is used to convert existing source filesystem image to a btrfs filesystem in-place. The original filesystem image is accessible in subvolume named like <i>ext2_saved</i> as file <i>image</i>. Supported filesystems:</p>
<dl>
<dd>&bull; ext2, ext3, ext4 &#8212; original feature, always built in</dl>
<dl>
<dd>&bull; reiserfs &#8212; since version 4.13, optionally built, requires libreiserfscore 3.6.27</dl>
<p> The list of supported source filesystem by a given binary is listed at the end of help (option <i>&#8211;help</i>).</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 If you are going to perform rollback to the original filesystem, you should not execute <code>btrfs balance</code> command on the converted filesystem. This will change the extent layout and make <code>btrfs-convert</code> unable to rollback.  The conversion utilizes free space of the original filesystem. The exact estimate of the required space cannot be foretold. The final btrfs metadata might occupy several gigabytes on a hundreds-gigabyte filesystem. If the ability to rollback is no longer important, the it is recommended to perform a few more steps to transition the btrfs filesystem to a more compact layout. This is because the conversion inherits the original data blocks&#8217; fragmentation, and also because the metadata blocks are bound to the original free space layout. Due to different constraints, it is only possible to convert filesystems that have a supported data block size (ie. the same that would be valid for <i>mkfs.btrfs</i>). This is typically the system page size (4KiB on x86_64 machines).</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The source filesystem should be clean, you are encouraged to run the <i>fsck</i> tool if you&#8217;re not sure.  <code>REMOVE THE ORIGINAL FILESYSTEM METADATA</code> By removing the subvolume named like <i>ext2_saved</i> or <i>reiserfs_saved</i>, all metadata of the original filesystem will be removed:</p>
<dl>
<dd>
<pre># btrfs subvolume delete /mnt/ext2_saved</pre>
</dl>
<p> At this point it is not possible to do a rollback. The filesystem is usable but may be impacted by the fragmentation inherited from the original filesystem. <code>MAKE FILE DATA MORE CONTIGUOUS</code> An optional but recommended step is to run defragmentation on the entire filesystem. This will attempt to make file extents more contiguous.</p>
<dl>
<dd>
<pre># btrfs filesystem defrag -v -r -f -t 32M /mnt/btrfs</pre>
</dl>
<p> Verbose recursive defragmentation (<i>-v</i>, <i>-r</i>), flush data per-file (<i>-f</i>) with target extent size 32MiB (<i>-t</i>). <code>ATTEMPT TO MAKE BTRFS METADATA MORE COMPACT</code> Optional but recommended step. The metadata block groups after conversion may be smaller than the default size (256MiB or 1GiB). Running a balance will attempt to merge the block groups. This depends on the free space layout (and fragmentation) and may fail due to lack of enough work space. This is a soft error leaving the filesystem usable but the block group layout may remain unchanged. Note that balance operation takes a lot of time, please see also <code><a href="/docs/linux/man/8-btrfs-balance/">btrfs-balance</a></code>(8).</p>
<dl>
<dd>
<pre># btrfs balance start -m /mnt/btrfs</pre>
</dl>
<h2>Options</h2>
<p>&#8211;csum <i>&lt;type&gt;</i>, &#8211;checksum <i>&lt;type&gt;</i></p>
<dl>
<dd>Specify the checksum algorithm. Default is <i>crc32c</i>. Valid values are <i>crc32c</i>, <i>xxhash</i>, <i>sha256</i> or <i>blake2</i>. To mount such filesystem kernel must support the checksums as well.</dl>
<p> -d|&#8211;no-datasum</p>
<dl>
<dd>disable data checksum calculations and set the NODATASUM file flag, this can speed up the conversion</dl>
<p> -i|&#8211;no-xattr</p>
<dl>
<dd>ignore xattrs and ACLs of files</dl>
<p> -n|&#8211;no-inline</p>
<dl>
<dd>disable inlining of small files to metadata blocks, this will decrease the metadata consumption and may help to convert a filesystem with low free space</dl>
<p> -N|&#8211;nodesize <i>&lt;SIZE&gt;</i></p>
<dl>
<dd>set filesystem nodesize, the tree block size in which btrfs stores its metadata. The default value is 16KB (16384) or the page size, whichever is bigger. Must be a multiple of the sectorsize, but not larger than 65536. See <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) for more details.</dl>
<p> -r|&#8211;rollback</p>
<dl>
<dd>rollback to the original ext2/3/4 filesystem if possible</dl>
<p> -l|&#8211;label <i>&lt;LABEL&gt;</i></p>
<dl>
<dd>set filesystem label during conversion</dl>
<p> -L|&#8211;copy-label</p>
<dl>
<dd>use label from the converted filesystem</dl>
<p> -O|&#8211;features <i>&lt;feature1&gt;</i>[,<i>&lt;feature2&gt;</i>&#8230;]</p>
<dl>
<dd>A list of filesystem features enabled the at time of conversion. Not all features are supported by old kernels. To disable a feature, prefix it with <i>^</i>. Description of the features is in section <i>FILESYSTEM FEATURES</i> of <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8). </p>
<p> To see all available features that btrfs-convert supports run: </p>
<p> <code>btrfs-convert -O list-all</code></dl>
<p> -p|&#8211;progress</p>
<dl>
<dd>show progress of conversion (a heartbeat indicator and number of inodes processed), on by default</dl>
<p> &#8211;no-progress</p>
<dl>
<dd>disable progress and show only the main phases of conversion</dl>
<h2>Exit Status</h2>
<p><code>btrfs-convert</code> will return 0 if no error happened. If any problems happened, 1 will be returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) </p>
