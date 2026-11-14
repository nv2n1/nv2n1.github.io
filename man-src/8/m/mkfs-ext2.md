---
title: "mkfs-ext2(8)"
name: "mkfs-ext2"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-ext2/"
description: "mke2fs – create an ext2/ext3/ext4 file system"
---

<p>mke2fs &#8211; create an ext2/ext3/ext4 file system</p>
<h2>Synopsis</h2>
<p><code>mke2fs</code> [ <code>-c</code> | <code>-l</code> <i>filename</i> ] [ <code>-b</code> <i>block-size</i> ] [ <code>-C</code> <i>cluster-size</i> ] [ <code>-d</code> <i>root-directory</i> ] [ <code>-D</code> ] [ <code>-g</code> <i>blocks-per-group</i> ] [ <code>-G</code> <i>number-of-groups</i> ] [ <code>-i</code> <i>bytes-per-inode</i> ] [ <code>-I</code> <i>inode-size</i> ] [ <code>-j</code> ] [ <code>-J</code> <i>journal-options</i> ] [ <code>-N</code> <i>number-of-inodes</i> ] [ <code>-n</code> ] [ <code>-m</code> <i>reserved-blocks-percentage</i> ] [ <code>-o</code> <i>creator-os</i> ] [ <code>-O</code> [^]<i>feature</i>[,&#8230;] ] [ <code>-q</code> ] [ <code>-r</code> <i>fs-revision-level</i> ] [ <code>-E</code> <i>extended-options</i> ] [ <code>-v</code> ] [ <code>-F</code> ] [ <code>-L</code> <i>volume-label</i> ] [ <code>-M</code> <i>last-mounted-directory</i> ] [ <code>-S</code> ] [ <code>-t</code> <i>fs-type</i> ] [ <code>-T</code> <i>usage-type</i> ] [ <code>-U</code> <i>UUID</i> ] [ <code>-V</code> ] [ <code>-e</code> <i>errors-behavior</i> ] [ <code>-z</code> <i>undo_file</i> ] <i>device</i> [ <i>fs-size</i> ] </p>
<p> <code>mke2fs -O journal_dev</code> [ <code>-b</code> <i>block-size</i> ] [ <code>-L</code> <i>volume-label</i> ] [ <code>-n</code> ] [ <code>-q</code> ] [ <code>-v</code> ] <i>external-journal</i> [ <i>fs-size</i> ]</p>
<h2>Description</h2>
<p><code>mke2fs</code> is used to create an ext2, ext3, or ext4 file system, usually in a disk partition (or file) named by <i>device</i>. </p>
<p> The file system size is specified by <i>fs-size</i>. If <i>fs-size</i> does not have a suffix, it is interpreted as power-of-two kilobytes, unless the <code>-b</code> <i>blocksize</i> option is specified, in which case <i>fs-size</i> is interpreted as the number of <i>blocksize</i> blocks. If the fs-size is suffixed by &#8216;k&#8217;, &#8216;m&#8217;, &#8216;g&#8217;, &#8216;t&#8217; (either upper-case or lower-case), then it is interpreted in power-of-two kilobytes, megabytes, gigabytes, terabytes, etc. If <i>fs-size</i> is omitted, <code>mke2fs</code> will create the file system based on the device size. </p>
<p> If <code>mke2fs</code> is run as <code>mkfs.XXX</code> (i.e., <code>mkfs.ext2</code>, <code>mkfs.ext3</code>, or <code>mkfs.ext4</code>) the option <code>-t</code> <i>XXX</i> is implied; so <code>mkfs.ext3</code> will create a file system for use with ext3, <code>mkfs.ext4</code> will create a file system for use with ext4, and so on. </p>
<p> The defaults of the parameters for the newly created file system, if not overridden by the options listed below, are controlled by the <code>/etc/mke2fs.conf</code> configuration file. See the <code><a href="/docs/linux/man/5-mke2fs-conf/">mke2fs.conf</a></code>(5) manual page for more details.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code><i> block-size</i></p>
<dd>Specify the size of blocks in bytes. Valid block-size values are powers of two from 1024 up to 65536 (however note that the kernel is able to mount only file systems with block-size smaller or equal to the system page size &#8211; 4k on x86 systems, up to 64k on ppc64 or aarch64 depending on kernel configuration). If omitted, block-size is heuristically determined by the file system size and the expected usage of the file system (see the <code>-T</code> option). In most common cases, the default block size is 4k. If <i>block-size</i> is preceded by a negative sign (&#8216;-&#8216;), then <code>mke2fs</code> will use heuristics to determine the appropriate block size, with the constraint that the block size will be at least <i>block-size</i> bytes. This is useful for certain hardware devices which require that the blocksize be a multiple of 2k.</p>
<dt><code>-c</code></p>
<dd>Check the device for bad blocks before creating the file system. If this option is specified twice, then a slower read-write test is used instead of a fast read-only test.</p>
<dt><code>-C cluster-size</code></p>
<dd>Specify the size of cluster in bytes for file systems using the bigalloc feature. Valid cluster-size values are from 2048 to 256M bytes per cluster. This can only be specified if the bigalloc feature is enabled. (See the <code>ext4 (5)</code> man page for more details about bigalloc.) The default cluster size if bigalloc is enabled is 16 times the block size.</p>
<dt><code>-d</code><i> root-directory</i></p>
<dd>Copy the contents of the given directory into the root directory of the file system.</p>
<dt><code>-D</code></p>
<dd>Use direct I/O when writing to the disk. This avoids mke2fs dirtying a lot of buffer cache memory, which may impact other applications running on a busy server. This option will cause mke2fs to run much more slowly, however, so there is a tradeoff to using direct I/O.</p>
<dt><code>-e</code><i> error-behavior</i></p>
<dd>Change the behavior of the kernel code when errors are detected. In all cases, a file system error will cause <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) to check the file system on the next boot. <i>error-behavior</i> can be one of the following:</p>
<dl>
<dd>
<dl>
<dt><code>continue</code></p>
<dd>Continue normal execution.</p>
<dt><code>remount-ro</code></p>
<dd>Remount file system read-only.</p>
<dt><code>panic</code></p>
<dd>Cause a kernel panic.</dl>
</dl>
<dt><code>-E</code><i> extended-options</i></p>
<dd>Set extended options for the file system. Extended options are comma separated, and may take an argument using the equals (&#8216;=&#8217;) sign. The <code>-E</code> option used to be <code>-R</code> in earlier versions of <code>mke2fs</code>. The <code>-R</code> option is still accepted for backwards compatibility, but is deprecated. The following extended options are supported:</p>
<dl>
<dd>
<dl>
<dt><code>encoding=</code><i>encoding-name</i></p>
<dd>Enable the <i>casefold</i> feature in the super block and set <i>encoding-name</i> as the encoding to be used. If <i>encoding-name</i> is not specified, the encoding defined in <code><a href="/docs/linux/man/5-mke2fs-conf/">mke2fs.conf</a></code>(5) is used.</p>
<dt><code>encoding_flags=</code><i>encoding-flags</i></p>
<dd>Define parameters for file name character encoding operations. If a flag is not changed using this parameter, its default value is used. <i>encoding-flags</i> should be a comma-separated lists of flags to be enabled. To disable a flag, add it to the list with the prefix &quot;no&quot;. </p>
<p> The only flag that can be set right now is <i>strict</i> which means that invalid strings should be rejected by the file system. In the default configuration, the <i>strict</i> flag is disabled.</p>
<dt><code>mmp_update_interval=</code><i>interval</i></p>
<dd>Adjust the initial MMP update interval to <i>interval</i> seconds. Specifying an <i>interval</i> of 0 means to use the default interval. The specified interval must be less than 300 seconds. Requires that the <code>mmp</code> feature be enabled.</p>
<dt><code>stride=</code><i>stride-size</i></p>
<dd>Configure the file system for a RAID array with <i>stride-size</i> file system blocks. This is the number of blocks read or written to disk before moving to the next disk, which is sometimes referred to as the <i>chunk size.</i> This mostly affects placement of file system metadata like bitmaps at <code>mke2fs</code> time to avoid placing them on a single disk, which can hurt performance. It may also be used by the block allocator.</p>
<dt><code>stripe_width=</code><i>stripe-width</i></p>
<dd>Configure the file system for a RAID array with <i>stripe-width</i> file system blocks per stripe. This is typically stride-size * N, where N is the number of data-bearing disks in the RAID (e.g. for RAID 5 there is one parity disk, so N will be the number of disks in the array minus 1). This allows the block allocator to prevent read-modify-write of the parity in a RAID stripe if possible when the data is written.</p>
<dt><code>offset=</code><i>offset</i></p>
<dd>Create the file system at an offset from the beginning of the device or file. This can be useful when creating disk images for virtual machines.</p>
<dt><code>resize=</code><i>max-online-resize</i></p>
<dd>Reserve enough space so that the block group descriptor table can grow to support a file system that has <i>max-online-resize</i> blocks.</p>
<dt><code>lazy_itable_init</code>[<code>= </code><i>&lt;0 to disable, 1 to enable&gt;</i>]</p>
<dd>If enabled and the uninit_bg feature is enabled, the inode table will not be fully initialized by <code>mke2fs</code>. This speeds up file system initialization noticeably, but it requires the kernel to finish initializing the file system in the background when the file system is first mounted. If the option value is omitted, it defaults to 1 to enable lazy inode table zeroing.</p>
<dt><code>lazy_journal_init</code>[<code>= </code><i>&lt;0 to disable, 1 to enable&gt;</i>]</p>
<dd>If enabled, the journal inode will not be fully zeroed out by <code>mke2fs</code>. This speeds up file system initialization noticeably, but carries some small risk if the system crashes before the journal has been overwritten entirely one time. If the option value is omitted, it defaults to 1 to enable lazy journal inode zeroing.</p>
<dt><code>no_copy_xattrs</code></p>
<dd>Normally <code>mke2fs</code> will copy the extended attributes of the files in the directory hierarchy specified via the (optional) <code>-d</code> option. This will disable the copy and leaves the files in the newly created file system without any extended attributes.</p>
<dt><code>num_backup_sb=</code><i>&lt;0|1|2&gt;</i></p>
<dd>If the <code>sparse_super2</code> file system feature is enabled this option controls whether there will be 0, 1, or 2 backup superblocks created in the file system.</p>
<dt><code>packed_meta_blocks</code>[<code>= </code><i>&lt;0 to disable, 1 to enable&gt;</i>]</p>
<dd>Place the allocation bitmaps and the inode table at the beginning of the disk. This option requires that the flex_bg file system feature to be enabled in order for it to have effect, and will also create the journal at the beginning of the file system. This option is useful for flash devices that use SLC flash at the beginning of the disk. It also maximizes the range of contiguous data blocks, which can be useful for certain specialized use cases, such as supported Shingled Drives.</p>
<dt><code>root_owner</code><i>[=uid:gid]</i></p>
<dd>Specify the numeric user and group ID of the root directory. If no UID:GID is specified, use the user and group ID of the user running <code>mke2fs</code>. In <code>mke2fs</code> 1.42 and earlier the UID and GID of the root directory were set by default to the UID and GID of the user running the mke2fs command. The <code>root_owner=</code> option allows explicitly specifying these values, and avoid side-effects for users that do not expect the contents of the file system to change based on the user running <code>mke2fs</code>.</p>
<dt><code>test_fs</code></p>
<dd>Set a flag in the file system superblock indicating that it may be mounted using experimental kernel code, such as the ext4dev file system.</p>
<dt><code>discard</code></p>
<dd>Attempt to discard blocks at mkfs time (discarding blocks initially is useful on solid state devices and sparse / thin-provisioned storage). When the device advertises that discard also zeroes data (any subsequent read after the discard and before write returns zero), then mark all not-yet-zeroed inode tables as zeroed. This significantly speeds up file system initialization. This is set as default.</p>
<dt><code>nodiscard</code></p>
<dd>Do not attempt to discard blocks at mkfs time.</p>
<dt><code>quotatype</code></p>
<dd>Specify the which quota types (usrquota, grpquota, prjquota) which should be enabled in the created file system. The argument of this extended option should be a colon separated list. This option has effect only if the <code>quota</code> feature is set. The default quota types to be initialized if this option is not specified is both user and group quotas. If the project feature is enabled that project quotas will be initialized as well.</dl>
</dl>
<dt><code>-F</code></p>
<dd>Force <code>mke2fs</code> to create a file system, even if the specified device is not a partition on a block special device, or if other parameters do not make sense. In order to force <code>mke2fs</code> to create a file system even if the file system appears to be in use or is mounted (a truly dangerous thing to do), this option must be specified twice.</p>
<dt><code>-g</code><i> blocks-per-group</i></p>
<dd>Specify the number of blocks in a block group. There is generally no reason for the user to ever set this parameter, as the default is optimal for the file system. (For administrators who are creating file systems on RAID arrays, it is preferable to use the <i>stride</i> RAID parameter as part of the <code>-E</code> option rather than manipulating the number of blocks per group.) This option is generally used by developers who are developing test cases.</p>
<dd>If the bigalloc feature is enabled, the <code>-g</code> option will specify the number of clusters in a block group.</p>
<dt><code>-G</code><i> number-of-groups</i></p>
<dd>Specify the number of block groups that will be packed together to create a larger virtual block group (or &quot;flex_bg group&quot;) in an ext4 file system. This improves meta-data locality and performance on meta-data heavy workloads. The number of groups must be a power of 2 and may only be specified if the <code>flex_bg</code> file system feature is enabled.</p>
<dt><code>-i</code><i> bytes-per-inode</i></p>
<dd>Specify the bytes/inode ratio. <code>mke2fs</code> creates an inode for every <i>bytes-per-inode</i> bytes of space on the disk. The larger the <i>bytes-per-inode</i> ratio, the fewer inodes will be created. This value generally shouldn&#8217;t be smaller than the blocksize of the file system, since in that case more inodes would be made than can ever be used. Be warned that it is not possible to change this ratio on a file system after it is created, so be careful deciding the correct value for this parameter. Note that resizing a file system changes the number of inodes to maintain this ratio.</p>
<dt><code>-I</code><i> inode-size</i></p>
<dd>Specify the size of each inode in bytes. The <i>inode-size</i> value must be a power of 2 larger or equal to 128. The larger the <i>inode-size</i> the more space the inode table will consume, and this reduces the usable space in the file system and can also negatively impact performance. It is not possible to change this value after the file system is created.</p>
<dd>File systems with an inode size of 128 bytes do not support timestamps beyond January 19, 2038. Inodes which are 256 bytes or larger will support extended timestamps, project id&#8217;s, and the ability to store some extended attributes in the inode table for improved performance.</p>
<dd>The default inode size is controlled by the <code><a href="/docs/linux/man/5-mke2fs-conf/">mke2fs.conf</a></code>(5) file. In the <code>mke2fs.conf</code> file shipped with e2fsprogs, the default inode size is 256 bytes for most file systems, except for small file systems where the inode size will be 128 bytes.</p>
<dt><code>-j</code></p>
<dd>Create the file system with an ext3 journal. If the <code>-J</code> option is not specified, the default journal parameters will be used to create an appropriately sized journal (given the size of the file system) stored within the file system. Note that you must be using a kernel which has ext3 support in order to actually make use of the journal.</p>
<dt><code>-J</code><i> journal-options</i></p>
<dd>Create the ext3 journal using options specified on the command-line. Journal options are comma separated, and may take an argument using the equals (&#8216;=&#8217;) sign. The following journal options are supported:</p>
<dl>
<dd>
<dl>
<dt><code>size=</code><i>journal-size</i></p>
<dd>Create an internal journal (i.e., stored inside the file system) of size <i>journal-size</i> megabytes. The size of the journal must be at least 1024 file system blocks (i.e., 1MB if using 1k blocks, 4MB if using 4k blocks, etc.) and may be no more than 10,240,000 file system blocks or half the total file system size (whichever is smaller)</p>
<dt><code>fast_commit_size=</code><i>fast-commit-size</i></p>
<dd>Create an additional fast commit journal area of size <i>fast-commit-size</i> kilobytes. This option is only valid if <code>fast_commit</code> feature is enabled on the file system. If this option is not specified and if <code>fast_commit</code> feature is turned on, fast commit area size defaults to <i>journal-size</i> / 64 megabytes. The total size of the journal with <code>fast_commit</code> feature set is <i>journal-size</i> + ( <i>fast-commit-size</i> * 1024) megabytes. The total journal size may be no more than 10,240,000 file system blocks or half the total file system size (whichever is smaller).</p>
<dt><code>location</code><i>=journal-location</i></p>
<dd>Specify the location of the journal. The argument <i>journal-location</i> can either be specified as a block number, or if the number has a units suffix (e.g., &#8216;M&#8217;, &#8216;G&#8217;, etc.) interpret it as the offset from the beginning of the file system.</p>
<dt><code>device=</code><i>external-journal</i></p>
<dd>Attach the file system to the journal block device located on <i>external-journal</i>. The external journal must already have been created using the command</p>
<dd><code>mke2fs -O journal_dev</code> <i>external-journal</i></p>
<dd>Note that <i>external-journal</i> must have been created with the same block size as the new file system. In addition, while there is support for attaching multiple file systems to a single external journal, the Linux kernel and <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) do not currently support shared external journals yet.</p>
<dd>Instead of specifying a device name directly, <i>external-journal</i> can also be specified by either <code>LABEL=</code><i>label</i> or <code>UUID=</code><i>UUID</i> to locate the external journal by either the volume label or UUID stored in the ext2 superblock at the start of the journal. Use <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8) to display a journal device&#8217;s volume label and UUID. See also the <code>-L</code> option of <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8).</dl>
</dl>
<dd>Only one of the <code>size</code> or <code>device</code> options can be given for a file system.</p>
<dt><code>-l</code><i> filename</i></p>
<dd>Read the bad blocks list from <i>filename</i>. Note that the block numbers in the bad block list must be generated using the same block size as used by <code>mke2fs</code>. As a result, the <code>-c</code> option to <code>mke2fs</code> is a much simpler and less error-prone method of checking a disk for bad blocks before formatting it, as <code>mke2fs</code> will automatically pass the correct parameters to the <code>badblocks</code> program.</p>
<dt><code>-L</code><i> new-volume-label</i></p>
<dd>Set the volume label for the file system to <i>new-volume-label</i>. The maximum length of the volume label is 16 bytes.</p>
<dt><code>-m</code><i> reserved-blocks-percentage</i></p>
<dd>Specify the percentage of the file system blocks reserved for the super-user. This avoids fragmentation, and allows root-owned daemons, such as <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8), to continue to function correctly after non-privileged processes are prevented from writing to the file system. The default percentage is 5%.</p>
<dt><code>-M</code><i> last-mounted-directory</i></p>
<dd>Set the last mounted directory for the file system. This might be useful for the sake of utilities that key off of the last mounted directory to determine where the file system should be mounted.</p>
<dt><code>-n</code></p>
<dd>Causes <code>mke2fs</code> to not actually create a file system, but display what it would do if it were to create a file system. This can be used to determine the location of the backup superblocks for a particular file system, so long as the <code>mke2fs</code> parameters that were passed when the file system was originally created are used again. (With the <code>-n</code> option added, of course!)</p>
<dt><code>-N</code><i> number-of-inodes</i></p>
<dd>Overrides the default calculation of the number of inodes that should be reserved for the file system (which is based on the number of blocks and the <i>bytes-per-inode</i> ratio). This allows the user to specify the number of desired inodes directly.</p>
<dt><code>-o</code><i> creator-os</i></p>
<dd>Overrides the default value of the &quot;creator operating system&quot; field of the file system. The creator field is set by default to the name of the OS the <code>mke2fs</code> executable was compiled for.</p>
<dt><code>-O </code>[^]<i>feature</i>[,&#8230;]</p>
<dd>Create a file system with the given features (file system options), overriding the default file system options. The features that are enabled by default are specified by the <i>base_features</i> relation, either in the <i>[defaults]</i> section in the <code>/etc/mke2fs.conf</code> configuration file, or in the <i>[fs_types]</i> subsections for the usage types as specified by the <code>-T</code> option, further modified by the <i>features</i> relation found in the <i>[fs_types]</i> subsections for the file system and usage types. See the <code><a href="/docs/linux/man/5-mke2fs-conf/">mke2fs.conf</a></code>(5) manual page for more details. The file system type-specific configuration setting found in the <i>[fs_types]</i> section will override the global default found in <i>[defaults]</i>. </p>
<p> The file system feature set will be further edited using either the feature set specified by this option, or if this option is not given, by the <i>default_features</i> relation for the file system type being created, or in the <i>[defaults]</i> section of the configuration file. </p>
<p> The file system feature set is comprised of a list of features, separated by commas, that are to be enabled. To disable a feature, simply prefix the feature name with a caret (&#8216;^&#8217;) character. Features with dependencies will not be removed successfully. The pseudo-file system feature &quot;none&quot; will clear all file system features.</p>
<dt>For more information about the features which can be set, please see</p>
<dd>the manual page <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5).</p>
<dt><code>-q</code></p>
<dd>Quiet execution. Useful if <code>mke2fs</code> is run in a script.</p>
<dt><code>-r</code><i> revision</i></p>
<dd>Set the file system revision for the new file system. Note that 1.2 kernels only support revision 0 file systems. The default is to create revision 1 file systems.</p>
<dt><code>-S</code></p>
<dd>Write superblock and group descriptors only. This is an extreme measure to be taken only in the very unlikely case that all of the superblock and backup superblocks are corrupted, and a last-ditch recovery method is desired by experienced users. It causes <code>mke2fs</code> to reinitialize the superblock and group descriptors, while not touching the inode table and the block and inode bitmaps. The <code>e2fsck</code> program should be run immediately after this option is used, and there is no guarantee that any data will be salvageable. Due to the wide variety of possible options to <code>mke2fs</code> that affect the on-disk layout, it is critical to specify exactly the same format options, such as blocksize, fs-type, feature flags, and other tunables when using this option, or the file system will be further corrupted. In some cases, such as file systems that have been resized, or have had features enabled after format time, it is impossible to overwrite all of the superblocks correctly, and at least some file system corruption will occur. It is best to run this on a full copy of the file system so other options can be tried if this doesn&#8217;t work.</p>
<dt><code>-t</code><i> fs-type</i></p>
<dd>Specify the file system type (i.e., ext2, ext3, ext4, etc.) that is to be created. If this option is not specified, <code>mke2fs</code> will pick a default either via how the command was run (for example, using a name of the form mkfs.ext2, mkfs.ext3, etc.) or via a default as defined by the <code>/etc/mke2fs.conf</code> file. This option controls which file system options are used by default, based on the <code>fstypes</code> configuration stanza in <code>/etc/mke2fs.conf</code>. </p>
<p> If the <code>-O</code> option is used to explicitly add or remove file system options that should be set in the newly created file system, the resulting file system may not be supported by the requested <i>fs-type</i>. (e.g., &quot;<code>mke2fs -t ext3 -O extent /dev/sdXX</code>&quot; will create a file system that is not supported by the ext3 implementation as found in the Linux kernel; and &quot;<code>mke2fs -t ext3 -O ^has_journal /dev/hdXX</code>&quot; will create a file system that does not have a journal and hence will not be supported by the ext3 file system code in the Linux kernel.)</p>
<dt><code>-T</code><i> usage-type[,&#8230;]</i></p>
<dd>Specify how the file system is going to be used, so that <code>mke2fs</code> can choose optimal file system parameters for that use. The usage types that are supported are defined in the configuration file <code>/etc/mke2fs.conf</code>. The user may specify one or more usage types using a comma separated list. </p>
<p> If this option is is not specified, <code>mke2fs</code> will pick a single default usage type based on the size of the file system to be created. If the file system size is less than 3 megabytes, <code>mke2fs</code> will use the file system type <i>floppy</i>. If the file system size is greater than or equal to 3 but less than 512 megabytes, <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) will use the file system type <i>small</i>. If the file system size is greater than or equal to 4 terabytes but less than 16 terabytes, <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) will use the file system type <i>big</i>. If the file system size is greater than or equal to 16 terabytes, <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) will use the file system type <i>huge</i>. Otherwise, <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) will use the default file system type <i>default</i>.</p>
<dt><code>-U</code><i> UUID</i></p>
<dd>Set the universally unique identifier (UUID) of the file system to <i>UUID</i>. The format of the UUID is a series of hex digits separated by hyphens, like this: &quot;c1b9d5a2-f162-11cf-9ece-0020afc76f16&quot;. The <i>UUID</i> parameter may also be one of the following:</p>
<dl>
<dd>
<dl>
<dt><i>clear</i></p>
<dd>clear the file system UUID</p>
<dt><i>random</i></p>
<dd>generate a new randomly-generated UUID</p>
<dt><i>time</i></p>
<dd>generate a new time-based UUID</dl>
</dl>
<dt><code>-v</code></p>
<dd>Verbose execution.</p>
<dt><code>-V</code></p>
<dd>Print the version number of <code>mke2fs</code> and exit.</p>
<dt><code>-z</code><i> undo_file</i></p>
<dd>Before overwriting a file system block, write the old contents of the block to an undo file. This undo file can be used with <a href="/docs/linux/man/8-e2undo/">e2undo</a>(8) to restore the old contents of the file system should something go wrong. If the empty string is passed as the undo_file argument, the undo file will be written to a file named mke2fs-<i>device</i>.e2undo in the directory specified via the <i>E2FSPROGS_UNDO_DIR</i> environment variable or the <i>undo_dir</i> directive in the configuration file. </p>
<p> WARNING: The undo file cannot be used to recover from a power or system crash.</dl>
<h2>Environment</h2>
<dl>
<dt><code>MKE2FS_SYNC</code></p>
<dd>If set to non-zero integer value, its value is used to determine how often <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2) is called during inode table initialization.</p>
<dt><code>MKE2FS_CONFIG</code></p>
<dd>Determines the location of the configuration file (see <code><a href="/docs/linux/man/5-mke2fs-conf/">mke2fs.conf</a></code>(5)).</p>
<dt><code>MKE2FS_FIRST_META_BG</code></p>
<dd>If set to non-zero integer value, its value is used to determine first meta block group. This is mostly for debugging purposes.</p>
<dt><code>MKE2FS_DEVICE_SECTSIZE</code></p>
<dd>If set to non-zero integer value, its value is used to determine logical sector size of the <i>device</i>.</p>
<dt><code>MKE2FS_DEVICE_PHYS_SECTSIZE</code></p>
<dd>If set to non-zero integer value, its value is used to determine physical sector size of the <i>device</i>.</p>
<dt><code>MKE2FS_SKIP_CHECK_MSG</code></p>
<dd>If set, do not show the message of file system automatic check caused by mount count or check interval.</dl>
<h2>Author</h2>
<p>This version of <code>mke2fs</code> has been written by Theodore Ts&#8217;o &lt;tytso [at] mit.edu&gt;.</p>
<h2>Availability</h2>
<p><code>mke2fs</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-mke2fs-conf/">mke2fs.conf</a></code>(5), <code><a href="/docs/linux/man/8-badblocks/">badblocks</a></code>(8), <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8), <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8), <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5) </p>
