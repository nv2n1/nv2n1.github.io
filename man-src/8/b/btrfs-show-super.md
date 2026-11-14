---
title: "btrfs-show-super(8)"
name: "btrfs-show-super"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-show-super/"
description: "btrfs-inspect-internal – query various internal information"
---

<p>btrfs-inspect-internal &#8211; query various internal information</p>
<h2>Synopsis</h2>
<p><code>btrfs inspect-internal</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p>This command group provides an interface to query internal information. The functionality ranges from a simple UI to an ioctl or a more complex query that assembles the result from several internal structures. The latter usually requires calls to privileged ioctls.</p>
<h2>Subcommand</h2>
<p><code>dump-super</code> [options] <i>&lt;device&gt;</i> [device&#8230;]</p>
<dl>
<dd>(replaces the standalone tool <code>btrfs-show-super</code>) </p>
<p> Show btrfs superblock information stored on given devices in textual form. By default the first superblock is printed, more details about all copies or additional backup data can be printed. </p>
<p> Besides verification of the filesystem signature, there are no other sanity checks. The superblock checksum status is reported, the device item and filesystem UUIDs are checked and reported. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 the meaning of option <i>-s</i> has changed in version 4.8 to be consistent with other tools to specify superblock copy rather the offset. The old way still works, but prints a warning. Please update your scripts to use <i>&#8211;bytenr</i> instead. The option <i>-i</i> has been deprecated. </p>
</dl>
<p> <code>Options</code> </p>
<p> -f|&#8211;full</p>
<dl>
<dd>print full superblock information, including the system chunk array and backup roots</dl>
<p> -a|&#8211;all</p>
<dl>
<dd>print information about all present superblock copies (cannot be used together with <i>-s</i> option)</dl>
<p> -i <i>&lt;super&gt;</i></p>
<dl>
<dd>(deprecated since 4.8, same behaviour as <i>&#8211;super</i>)</dl>
<p> &#8211;bytenr <i>&lt;bytenr&gt;</i></p>
<dl>
<dd>specify offset to a superblock in a non-standard location at <i>bytenr</i>, useful for debugging (disables the <i>-f</i> option) </p>
<p> If there are multiple options specified, only the last one applies.</dl>
<p> -F|&#8211;force</p>
<dl>
<dd>attempt to print the superblock even if a valid BTRFS signature is not found; the result may be completely wrong if the data does not resemble a superblock</dl>
<p> -s|&#8211;super <i>&lt;bytenr&gt;</i></p>
<dl>
<dd>(see compatibility note above) </p>
<p> specify which mirror to print, valid values are 0, 1 and 2 and the superblock must be present on the device with a valid signature, can be used together with <i>&#8211;force</i></dl>
</dl>
<p> <code>dump-tree</code> [options] <i>&lt;device&gt;</i></p>
<dl>
<dd>(replaces the standalone tool <code>btrfs-debug-tree</code>) </p>
<p> Dump tree structures from a given device in textual form, expand keys to human readable equivalents where possible. This is useful for analyzing filesystem state or inconsistencies and has a positive educational effect on understanding the internal filesystem structure. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 contains file names, consider that if you&#8217;re asked to send the dump for analysis. Does not contain file data. </p>
</dl>
<p> <code>Options</code> </p>
<p> -e|&#8211;extents</p>
<dl>
<dd>print only extent-related information: extent and device trees</dl>
<p> -d|&#8211;device</p>
<dl>
<dd>print only device-related information: tree root, chunk and device trees</dl>
<p> -r|&#8211;roots</p>
<dl>
<dd>print only short root node information, ie. the root tree keys</dl>
<p> -R|&#8211;backups</p>
<dl>
<dd>same as &#8211;roots plus print backup root info, ie. the backup root keys and the respective tree root block offset</dl>
<p> -u|&#8211;uuid</p>
<dl>
<dd>print only the uuid tree information, empty output if the tree does not exist</dl>
<p> -b <i>&lt;block_num&gt;</i></p>
<dl>
<dd>print info of the specified block only</dl>
<p> -t <i>&lt;tree_id&gt;</i></p>
<dl>
<dd>print only the tree with the specified ID, where the ID can be numerical or common name in a flexible human readable form </p>
<p> The tree id name recognition rules: </p>
<dl>
<dd>&bull; case does not matter</dl>
<dl>
<dd>&bull; the C source definition, eg. BTRFS_ROOT_TREE_OBJECTID</dl>
<dl>
<dd>&bull; short forms without BTRFS_ prefix, without _TREE and _OBJECTID suffix, eg. ROOT_TREE, ROOT</dl>
<dl>
<dd>&bull; convenience aliases, eg. DEVICE for the DEV tree, CHECKSUM for CSUM</dl>
<dl>
<dd>&bull; unrecognized ID is an error</dl>
</dl>
</dl>
<p> <code>inode-resolve</code> [-v] <i>&lt;ino&gt;</i> <i>&lt;path&gt;</i></p>
<dl>
<dd>(needs root privileges) </p>
<p> resolve paths to all files with given inode number <i>ino</i> in a given subvolume at <i>path</i>, ie. all hardlinks </p>
<p> <code>Options</code> </p>
<p> -v</p>
<dl>
<dd>verbose mode, print count of returned paths and ioctl() return value</dl>
</dl>
<p> <code>logical-resolve</code> [-Pv] [-s <i>&lt;bufsize&gt;</i>] <i>&lt;logical&gt;</i> <i>&lt;path&gt;</i></p>
<dl>
<dd>(needs root privileges) </p>
<p> resolve paths to all files at given <i>logical</i> address in the linear filesystem space </p>
<p> <code>Options</code> </p>
<p> -P</p>
<dl>
<dd>skip the path resolving and print the inodes instead</dl>
<p> -v</p>
<dl>
<dd>verbose mode, print count of returned paths and all ioctl() return values</dl>
<p> -s <i>&lt;bufsize&gt;</i></p>
<dl>
<dd>set internal buffer for storing the file names to <i>bufsize</i>, default is 4096, maximum 64k</dl>
</dl>
<p> <code>min-dev-size</code> [options] <i>&lt;path&gt;</i></p>
<dl>
<dd>(needs root privileges) </p>
<p> return the minimum size the device can be shrunk to, without performing any resize operation, this may be useful before executing the actual resize operation </p>
<p> <code>Options</code> </p>
<p> &#8211;id <i>&lt;id&gt;</i></p>
<dl>
<dd>specify the device <i>id</i> to query, default is 1 if this option is not used</dl>
</dl>
<p> <code>rootid</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>for a given file or directory, return the containing tree root id, but for a subvolume itself return its own tree id (ie. subvol id) </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The result is undefined for the so-called empty subvolumes (identified by inode number 2), but such a subvolume does not contain any files anyway </p>
</dl>
</dl>
<p> <code>subvolid-resolve</code> <i>&lt;subvolid&gt;</i> <i>&lt;path&gt;</i></p>
<dl>
<dd>(needs root privileges) </p>
<p> resolve the absolute path of the subvolume id <i>subvolid</i></dl>
<p> <code>tree-stats</code> [options] <i>&lt;device&gt;</i></p>
<dl>
<dd>(needs root privileges) </p>
<p> Print sizes and statistics of trees. </p>
<p> <code>Options</code> </p>
<p> -b</p>
<dl>
<dd>Print raw numbers in bytes.</dl>
</dl>
<h2>Exit Status</h2>
<p><code>btrfs inspect-internal</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) </p>
