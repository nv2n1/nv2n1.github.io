---
title: "btrfs-check(8)"
name: "btrfs-check"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-check/"
description: "btrfs-check – check or repair a btrfs filesystem"
---

<p>btrfs-check &#8211; check or repair a btrfs filesystem</p>
<h2>Synopsis</h2>
<p><code>btrfs check</code> [options] <i>&lt;device&gt;</i></p>
<h2>Description</h2>
<p>The filesystem checker is used to verify structural integrity of a filesystem and attempt to repair it if requested. It is recommended to unmount the filesystem prior to running the check, but it is possible to start checking a mounted filesystem (see <i>&#8211;force</i>). By default, <code>btrfs check</code> will not modify the device but you can reaffirm that by the option <i>&#8211;readonly</i>. <code>btrfsck</code> is an alias of <code>btrfs check</code> command and is now deprecated.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Do not use <i>&#8211;repair</i> unless you are advised to do so by a developer or an experienced user, and then only after having accepted that no <i>fsck</i> successfully repair all types of filesystem corruption. Eg. some other software or hardware bugs can fatally damage a volume.  The structural integrity check verifies if internal filesystem objects or data structures satisfy the constraints, point to the right objects or are correctly connected together. There are several cross checks that can detect wrong reference counts of shared extents, backreferences, missing extents of inodes, directory and inode connectivity etc. The amount of memory required can be high, depending on the size of the filesystem, similarly the run time. Check the modes that can also affect that.</p>
<h2>Safe Or Advisory Options</h2>
<p>-b|&#8211;backup</p>
<dl>
<dd>use the first valid set of backup roots stored in the superblock </p>
<p> This can be combined with <i>&#8211;super</i> if some of the superblocks are damaged.</dl>
<p> &#8211;check-data-csum</p>
<dl>
<dd>verify checksums of data blocks </p>
<p> This expects that the filesystem is otherwise OK, and is basically and offline <i>scrub</i> but does not repair data from spare copies.</dl>
<p> &#8211;chunk-root <i>&lt;bytenr&gt;</i></p>
<dl>
<dd>use the given offset <i>bytenr</i> for the chunk tree root</dl>
<p> -E|&#8211;subvol-extents <i>&lt;subvolid&gt;</i></p>
<dl>
<dd>show extent state for the given subvolume</dl>
<p> -p|&#8211;progress</p>
<dl>
<dd>indicate progress at various checking phases</dl>
<p> -Q|&#8211;qgroup-report</p>
<dl>
<dd>verify qgroup accounting and compare against filesystem accounting</dl>
<p> -r|&#8211;tree-root <i>&lt;bytenr&gt;</i></p>
<dl>
<dd>use the given offset <i>bytenr</i> for the tree root</dl>
<p> &#8211;readonly</p>
<dl>
<dd>(default) run in read-only mode, this option exists to calm potential panic when users are going to run the checker</dl>
<p> -s|&#8211;super <i>&lt;superblock&gt;</i></p>
<dl>
<dd>use &#8216;superblock&#8217;th superblock copy, valid values are 0, 1 or 2 if the respective superblock offset is within the device size </p>
<p> This can be used to use a different starting point if some of the primary superblock is damaged.</dl>
<p> &#8211;clear-space-cache v1|v2</p>
<dl>
<dd>completely wipe all free space cache of given type </p>
<p> For free space cache <i>v1</i>, the <i>clear_cache</i> kernel mount option only rebuilds the free space cache for block groups that are modified while the filesystem is mounted with that option. Thus, using this option with <i>v1</i> makes it possible to actually clear the entire free space cache. </p>
<p> For free space cache <i>v2</i>, the <i>clear_cache</i> kernel mount option destroys the entire free space cache. This option, with <i>v2</i> provides an alternative method of clearing the free space cache that doesn&#8217;t require mounting the filesystem.</dl>
<h2>Dangerous Options</h2>
<p>&#8211;repair</p>
<dl>
<dd>enable the repair mode and attempt to fix problems where possible </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 there&#8217;s a warning and 10 second delay when this option is run without <i>&#8211;force</i> to give users a chance to think twice before running repair, the warnings in documentation have shown to be insufficient </p>
</dl>
</dl>
<p> &#8211;init-csum-tree</p>
<dl>
<dd>create a new checksum tree and recalculate checksums in all files </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Do not blindly use this option to fix checksum mismatch problems. </p>
</dl>
</dl>
<p> &#8211;init-extent-tree</p>
<dl>
<dd>build the extent tree from scratch </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Do not use unless you know what you&#8217;re doing. </p>
</dl>
</dl>
<p> &#8211;mode <i>&lt;MODE&gt;</i></p>
<dl>
<dd>select mode of operation regarding memory and IO </p>
<p> The <i>MODE</i> can be one of: </p>
<p> <i>original</i></p>
<dl>
<dd>The metadata are read into memory and verified, thus the requirements are high on large filesystems and can even lead to out-of-memory conditions. The possible workaround is to export the block device over network to a machine with enough memory.</dl>
<p> <i>lowmem</i></p>
<dl>
<dd>This mode is supposed to address the high memory consumption at the cost of increased IO when it needs to re-read blocks. This may increase run time. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 <i>lowmem</i> mode does not work with <i>&#8211;repair</i> yet, and is still considered experimental. </p>
</dl>
</dl>
</dl>
<p> &#8211;force</p>
<dl>
<dd>allow work on a mounted filesystem. Note that this should work fine on a quiescent or read-only mounted filesystem but may crash if the device is changed externally, eg. by the kernel module. Repair without mount checks is not supported right now. </p>
<p> This option also skips the delay and warning in the repair mode (see <i>&#8211;repair</i>).</dl>
<h2>Exit Status</h2>
<p><code>btrfs check</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-scrub/">btrfs-scrub</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-rescue/">btrfs-rescue</a></code>(8) </p>
