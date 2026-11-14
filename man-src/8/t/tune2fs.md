---
title: "tune2fs(8)"
name: "tune2fs"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tune2fs/"
description: "tune2fs – adjust tunable file system parameters on ext2/ext3/ext4 file systems"
---

<p>tune2fs &#8211; adjust tunable file system parameters on ext2/ext3/ext4 file systems</p>
<h2>Synopsis</h2>
<p><code>tune2fs</code> [ <code>-l</code> ] [ <code>-c</code> <i>max-mount-counts</i> ] [ <code>-e</code> <i>errors-behavior</i> ] [ <code>-f</code> ] [ <code>-i</code> <i>interval-between-checks</i> ] [ <code>-I</code> <i>new_inode_size</i> ] [ <code>-j</code> ] [ <code>-J</code> <i>journal-options</i> ] [ <code>-m</code> <i>reserved-blocks-percentage</i> ] [ <code>-o</code> [^]mount-options<i>[,&#8230;]</i> ] [ <code>-r</code> <i>reserved-blocks-count</i> ] [ <code>-u</code> <i>user</i> ] [ <code>-g</code> <i>group</i> ] [ <code>-C</code> <i>mount-count</i> ] [ <code>-E</code> <i>extended-options</i> ] [ <code>-L</code> <i>volume-label</i> ] [ <code>-M</code> <i>last-mounted-directory</i> ] [ <code>-O</code> [^]<i>feature</i>[,&#8230;] ] [ <code>-Q</code> <i>quota-options</i> ] [ <code>-T</code> <i>time-last-checked</i> ] [ <code>-U</code> <i>UUID</i> ] [ <code>-z</code> <i>undo_file</i> ] device</p>
<h2>Description</h2>
<p><code>tune2fs</code> allows the system administrator to adjust various tunable file system parameters on Linux ext2, ext3, or ext4 file systems. The current values of these options can be displayed by using the <code>-l</code> option to <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8) program, or by using the <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8) program. </p>
<p> The <i>device</i> specifier can either be a filename (i.e., /dev/sda1), or a LABEL or UUID specifier: &quot;<code>LABEL=</code><i>volume-label</i>&quot; or &quot;<code>UUID=</code><i>uuid</i>&quot;. (i.e., LABEL=home or UUID=e40486c6-84d5-4f2f-b99c-032281799c9d).</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> max-mount-counts</i></p>
<dd>Adjust the number of mounts after which the file system will be checked by <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8). If <i>max-mount-counts</i> is the string &quot;random&quot;, tune2fs will use a random value between 20 and 40. If <i>max-mount-counts</i> is 0 or -1, the number of times the file system is mounted will be disregarded by <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) and the kernel. </p>
<p> Staggering the mount-counts at which file systems are forcibly checked will avoid all file systems being checked at one time when using journaled file systems. </p>
<p> Mount-count-dependent checking is disabled by default to avoid unanticipated long reboots while e2fsck does its work. If you are concerned about file system corruptions caused by potential hardware problems of kernel bugs, a better solution than mount-count-dependent checking is to use the <code><a href="/docs/linux/man/8-e2scrub/">e2scrub</a></code>(8) program. This does require placing the file system on an LVM volume, however.</p>
<dt><code>-C</code><i> mount-count</i></p>
<dd>Set the number of times the file system has been mounted. If set to a greater value than the max-mount-counts parameter set by the <code>-c</code> option, <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) will check the file system at the next reboot.</p>
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
<dd>Set extended options for the file system. Extended options are comma separated, and may take an argument using the equals (&#8216;=&#8217;) sign. The following extended options are supported:</p>
<dl>
<dd>
<dl>
<dt><code>clear_mmp</code></p>
<dd>Reset the MMP block (if any) back to the clean state. Use only if absolutely certain the device is not currently mounted or being fscked, or major file system corruption can result. Needs &#8216;-f&#8217;.</p>
<dt><code>mmp_update_interval=</code><i>interval</i></p>
<dd>Adjust the initial MMP update interval to <i>interval</i> seconds. Specifying an <i>interval</i> of 0 means to use the default interval. The specified interval must be less than 300 seconds. Requires that the <code>mmp</code> feature be enabled.</p>
<dt><code>stride=</code><i>stride-size</i></p>
<dd>Configure the file system for a RAID array with <i>stride-size</i> file system blocks. This is the number of blocks read or written to disk before moving to next disk. This mostly affects placement of file system metadata like bitmaps at <code><a href="/docs/linux/man/2-mke2fs/">mke2fs</a></code>(2) time to avoid placing them on a single disk, which can hurt the performance. It may also be used by block allocator.</p>
<dt><code>stripe_width=</code><i>stripe-width</i></p>
<dd>Configure the file system for a RAID array with <i>stripe-width</i> file system blocks per stripe. This is typically be stride-size * N, where N is the number of data disks in the RAID (e.g. RAID 5 N+1, RAID 6 N+2). This allows the block allocator to prevent read-modify-write of the parity in a RAID stripe if possible when the data is written.</p>
<dt><code>hash_alg=</code><i>hash-alg</i></p>
<dd>Set the default hash algorithm used for file systems with hashed b-tree directories. Valid algorithms accepted are: <i>legacy</i>, <i>half_md4</i>, and <i>tea</i>.</p>
<dt><code>encoding=</code><i>encoding-name</i></p>
<dd>Enable the <i>casefold</i> feature in the super block and set <i>encoding-name</i> as the encoding to be used. If <i>encoding-name</i> is not specified, utf8 is used. The encoding cannot be altered if casefold was previously enabled.</p>
<dt><code>encoding_flags=</code><i>encoding-flags</i></p>
<dd>Define parameters for file name character encoding operations. If a flag is not changed using this parameter, its default value is used. <i>encoding-flags</i> should be a comma-separated lists of flags to be enabled. The flags cannot be altered if casefold was previously enabled. </p>
<p> The only flag that can be set right now is <i>strict</i> which means that invalid strings should be rejected by the file system. In the default configuration, the <i>strict</i> flag is disabled.</p>
<dt><code>mount_opts=</code><i>mount_option_string</i></p>
<dd>Set a set of default mount options which will be used when the file system is mounted. Unlike the bitmask-based default mount options which can be specified with the <code>-o</code> option, <i>mount_option_string</i> is an arbitrary string with a maximum length of 63 bytes, which is stored in the superblock.</p>
<dd>The ext4 file system driver will first apply the bitmask-based default options, and then parse the <i>mount_option_string</i>, before parsing the mount options passed from the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) program.</p>
<dd>This superblock setting is only honored in 2.6.35+ kernels; and not at all by the ext2 and ext3 file system drivers.</p>
<dt><code>force_fsck</code></p>
<dd>Set a flag in the file system superblock indicating that errors have been found. This will force fsck to run at the next mount.</p>
<dt><code>test_fs</code></p>
<dd>Set a flag in the file system superblock indicating that it may be mounted using experimental kernel code, such as the ext4dev file system.</p>
<dt><code>^test_fs</code></p>
<dd>Clear the test_fs flag, indicating the file system should only be mounted using production-level file system code.</dl>
</dl>
<dt><code>-f</code></p>
<dd>Force the tune2fs operation to complete even in the face of errors. This option is useful when removing the <code>has_journal</code> file system feature from a file system which has an external journal (or is corrupted such that it appears to have an external journal), but that external journal is not available. If the file system appears to require journal replay, the <code>-f</code> flag must be specified twice to proceed. </p>
<p> <code>WARNING:</code> Removing an external journal from a file system which was not cleanly unmounted without first replaying the external journal can result in severe data loss and file system corruption.</p>
<dt><code>-g</code><i> group</i></p>
<dd>Set the group which can use the reserved file system blocks. The <i>group</i> parameter can be a numerical gid or a group name. If a group name is given, it is converted to a numerical gid before it is stored in the superblock.</p>
<dt><code>-i </code><i>interval-between-checks</i>[<code>d</code>|<code>m</code>|<code>w</code>]</p>
<dd>Adjust the maximal time between two file system checks. No suffix or <code>d</code> will interpret the number <i>interval-between-checks</i> as days, <code>m</code> as months, and <code>w</code> as weeks. A value of zero will disable the time-dependent checking. </p>
<p> There are pros and cons to disabling these periodic checks; see the discussion under the <code>-c</code> (mount-count-dependent check) option for details.</p>
<dt><code>-I</code></p>
<dd>Change the inode size used by the file system. This requires rewriting the inode table, so it requires that the file system is checked for consistency first using <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8). This operation can also take a while and the file system can be corrupted and data lost if it is interrupted while in the middle of converting the file system. Backing up the file system before changing inode size is recommended.</p>
<dd>File systems with an inode size of 128 bytes do not support timestamps beyond January 19, 2038. Inodes which are 256 bytes or larger will support extended timestamps, project id&#8217;s, and the ability to store some extended attributes in the inode table for improved performance.</p>
<dt><code>-j</code></p>
<dd>Add an ext3 journal to the file system. If the <code>-J</code> option is not specified, the default journal parameters will be used to create an appropriately sized journal (given the size of the file system) stored within the file system. Note that you must be using a kernel which has ext3 support in order to actually make use of the journal.</p>
<dd>If this option is used to create a journal on a mounted file system, an immutable file, <code>.journal</code>, will be created in the top-level directory of the file system, as it is the only safe way to create the journal inode while the file system is mounted. While the ext3 journal is visible, it is not safe to delete it, or modify it while the file system is mounted; for this reason the file is marked immutable. While checking unmounted file systems, <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) will automatically move <code>.journal</code> files to the invisible, reserved journal inode. For all file systems except for the root file system, this should happen automatically and naturally during the next reboot cycle. Since the root file system is mounted read-only, <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) must be run from a rescue floppy in order to effect this transition.</p>
<dd>On some distributions, such as Debian, if an initial ramdisk is used, the initrd scripts will automatically convert an ext2 root file system to ext3 if the <code>/etc/fstab</code> file specifies the ext3 file system for the root file system in order to avoid requiring the use of a rescue floppy to add an ext3 journal to the root file system.</p>
<dt><code>-J</code> journal-options</p>
<dd>Override the default ext3 journal parameters. Journal options are comma separated, and may take an argument using the equals (&#8216;=&#8217;) sign. The following journal options are supported:</p>
<dl>
<dd>
<dl>
<dt><code>size=</code><i>journal-size</i></p>
<dd>Create a journal stored in the file system of size <i>journal-size</i> megabytes. The size of the journal must be at least 1024 file system blocks (i.e., 1MB if using 1k blocks, 4MB if using 4k blocks, etc.) and may be no more than 10,240,000 file system blocks. There must be enough free space in the file system to create a journal of that size.</p>
<dt><code>fast_commit_size=</code><i>fast-commit-size</i></p>
<dd>Create an additional fast commit journal area of size <i>fast-commit-size</i> kilobytes. This option is only valid if <code>fast_commit</code> feature is enabled on the file system. If this option is not specified and if <code>fast_commit</code> feature is turned on, fast commit area size defaults to <i>journal-size</i> / 64 megabytes. The total size of the journal with <code>fast_commit</code> feature set is <i>journal-size</i> + ( <i>fast-commit-size</i> * 1024) megabytes. The total journal size may be no more than 10,240,000 file system blocks or half the total file system size (whichever is smaller).</p>
<dt><code>location</code><i>=journal-location</i></p>
<dd>Specify the location of the journal. The argument <i>journal-location</i> can either be specified as a block number, or if the number has a units suffix (e.g., &#8216;M&#8217;, &#8216;G&#8217;, etc.) interpret it as the offset from the beginning of the file system.</p>
<dt><code>device=</code><i>external-journal</i></p>
<dd>Attach the file system to the journal block device located on <i>external-journal</i>. The external journal must have been already created using the command</p>
<dd><code>mke2fs -O journal_dev</code> <i>external-journal</i></p>
<dd>Note that <i>external-journal</i> must be formatted with the same block size as file systems which will be using it. In addition, while there is support for attaching multiple file systems to a single external journal, the Linux kernel and <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) do not currently support shared external journals yet.</p>
<dd>Instead of specifying a device name directly, <i>external-journal</i> can also be specified by either <code>LABEL=</code><i>label</i> or <code>UUID=</code><i>UUID</i> to locate the external journal by either the volume label or UUID stored in the ext2 superblock at the start of the journal. Use <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8) to display a journal device&#8217;s volume label and UUID. See also the <code>-L</code> option of <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8).</dl>
</dl>
<dd>Only one of the <code>size</code> or <code>device</code> options can be given for a file system.</p>
<dt><code>-l</code></p>
<dd>List the contents of the file system superblock, including the current values of the parameters that can be set via this program.</p>
<dt><code>-L</code><i> volume-label</i></p>
<dd>Set the volume label of the file system. Ext2 file system labels can be at most 16 characters long; if <i>volume-label</i> is longer than 16 characters, <code>tune2fs</code> will truncate it and print a warning. The volume label can be used by <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), and <code>/etc/<a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) (and possibly others) by specifying <code>LABEL=</code><i>volume-label</i> instead of a block special device name like <code>/dev/hda5</code>.</p>
<dt><code>-m</code><i> reserved-blocks-percentage</i></p>
<dd>Set the percentage of the file system which may only be allocated by privileged processes. Reserving some number of file system blocks for use by privileged processes is done to avoid file system fragmentation, and to allow system daemons, such as <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8), to continue to function correctly after non-privileged processes are prevented from writing to the file system. Normally, the default percentage of reserved blocks is 5%.</p>
<dt><code>-M</code><i> last-mounted-directory</i></p>
<dd>Set the last-mounted directory for the file system.</p>
<dt><code>-o</code> [^]<i>mount-option</i>[,&#8230;]</p>
<dd>Set or clear the indicated default mount options in the file system. Default mount options can be overridden by mount options specified either in <code>/etc/<a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) or on the command line arguments to <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). Older kernels may not support this feature; in particular, kernels which predate 2.4.20 will almost certainly ignore the default mount options field in the superblock.</p>
<dd>More than one mount option can be cleared or set by separating features with commas. Mount options prefixed with a caret character (&#8216;^&#8217;) will be cleared in the file system&#8217;s superblock; mount options without a prefix character or prefixed with a plus character (&#8216;+&#8217;) will be added to the file system.</p>
<dd>The following mount options can be set or cleared using <code>tune2fs</code>:</p>
<dl>
<dd>
<dl>
<dt><code>debug</code></p>
<dd>Enable debugging code for this file system.</p>
<dt><code>bsdgroups</code></p>
<dd>Emulate BSD behavior when creating new files: they will take the group-id of the directory in which they were created. The standard System V behavior is the default, where newly created files take on the fsgid of the current process, unless the directory has the setgid bit set, in which case it takes the gid from the parent directory, and also gets the setgid bit set if it is a directory itself.</p>
<dt><code>user_xattr</code></p>
<dd>Enable user-specified extended attributes.</p>
<dt><code>acl</code></p>
<dd>Enable Posix Access Control Lists.</p>
<dt><code>uid16</code></p>
<dd>Disables 32-bit UIDs and GIDs. This is for interoperability with older kernels which only store and expect 16-bit values.</p>
<dt><code>journal_data</code></p>
<dd>When the file system is mounted with journaling enabled, all data (not just metadata) is committed into the journal prior to being written into the main file system.</p>
<dt><code>journal_data_ordered</code></p>
<dd>When the file system is mounted with journaling enabled, all data is forced directly out to the main file system prior to its metadata being committed to the journal.</p>
<dt><code>journal_data_writeback</code></p>
<dd>When the file system is mounted with journaling enabled, data may be written into the main file system after its metadata has been committed to the journal. This may increase throughput, however, it may allow old data to appear in files after a crash and journal recovery.</p>
<dt><code>nobarrier</code></p>
<dd>The file system will be mounted with barrier operations in the journal disabled. (This option is currently only supported by the ext4 file system driver in 2.6.35+ kernels.)</p>
<dt><code>block_validity</code></p>
<dd>The file system will be mounted with the block_validity option enabled, which causes extra checks to be performed after reading or writing from the file system. This prevents corrupted metadata blocks from causing file system damage by overwriting parts of the inode table or block group descriptors. This comes at the cost of increased memory and CPU overhead, so it is enabled only for debugging purposes. (This option is currently only supported by the ext4 file system driver in 2.6.35+ kernels.)</p>
<dt><code>discard</code></p>
<dd>The file system will be mounted with the discard mount option. This will cause the file system driver to attempt to use the trim/discard feature of some storage devices (such as SSD&#8217;s and thin-provisioned drives available in some enterprise storage arrays) to inform the storage device that blocks belonging to deleted files can be reused for other purposes. (This option is currently only supported by the ext4 file system driver in 2.6.35+ kernels.)</p>
<dt><code>nodelalloc</code></p>
<dd>The file system will be mounted with the nodelalloc mount option. This will disable the delayed allocation feature. (This option is currently only supported by the ext4 file system driver in 2.6.35+ kernels.)</dl>
</dl>
<dt><code>-O</code> [^]<i>feature</i>[,&#8230;]</p>
<dd>Set or clear the indicated file system features (options) in the file system. More than one file system feature can be cleared or set by separating features with commas. File System features prefixed with a caret character (&#8216;^&#8217;) will be cleared in the file system&#8217;s superblock; file system features without a prefix character or prefixed with a plus character (&#8216;+&#8217;) will be added to the file system. For a detailed description of the file system features, please see the man page <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5).</p>
<dd>The following file system features can be set or cleared using <code>tune2fs</code>:</p>
<dl>
<dd>
<dl>
<dt><code>64bit</code></p>
<dd>Enable the file system to be larger than 2^32 blocks.</p>
<dt><code>casefold</code></p>
<dd>Enable support for file system level casefolding. <code>Tune2fs</code> currently only supports setting this file system feature.</p>
<dt><code>dir_index</code></p>
<dd>Use hashed b-trees to speed up lookups for large directories.</p>
<dt><code>dir_nlink</code></p>
<dd>Allow more than 65000 subdirectories per directory.</p>
<dt><code>ea_inode</code></p>
<dd>Allow the value of each extended attribute to be placed in the data blocks of a separate inode if necessary, increasing the limit on the size and number of extended attributes per file. <code>Tune2fs</code> currently only supports setting this file system feature.</p>
<dt><code>encrypt</code></p>
<dd>Enable support for file system level encryption. <code>Tune2fs</code> currently only supports setting this file system feature.</p>
<dt><code>extent</code></p>
<dd>Enable the use of extent trees to store the location of data blocks in inodes. <code>Tune2fs</code> currently only supports setting this file system feature.</p>
<dt><code>extra_isize</code></p>
<dd>Enable the extended inode fields used by ext4.</p>
<dt><code>filetype</code></p>
<dd>Store file type information in directory entries.</p>
<dt><code>flex_bg</code></p>
<dd>Allow bitmaps and inode tables for a block group to be placed anywhere on the storage media. <code>Tune2fs</code> will not reorganize the location of the inode tables and allocation bitmaps, as <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) will do when it creates a freshly formatted file system with <code>flex_bg</code> enabled.</p>
<dt><code>has_journal</code></p>
<dd>Use a journal to ensure file system consistency even across unclean shutdowns. Setting the file system feature is equivalent to using the <code>-j</code> option.</p>
<dt>
<dt><code>fast_commit</code></p>
<dd>
<dd>Enable fast commit journaling feature to improve fsync latency.</p>
<dt><code>large_dir</code></p>
<dd>Increase the limit on the number of files per directory. <code>Tune2fs</code> currently only supports setting this file system feature.</p>
<dt><code>huge_file</code></p>
<dd>Support files larger than 2 terabytes in size.</p>
<dt><code>large_file</code></p>
<dd>File System can contain files that are greater than 2GB.</p>
<dt><code>metadata_csum</code></p>
<dd>Store a checksum to protect the contents in each metadata block.</p>
<dt><code>metadata_csum_seed</code></p>
<dd>Allow the file system to store the metadata checksum seed in the superblock, enabling the administrator to change the UUID of a file system using the <code>metadata_csum</code> feature while it is mounted.</p>
<dt><code>mmp</code></p>
<dd>Enable or disable multiple mount protection (MMP) feature.</p>
<dt><code>project</code></p>
<dd>Enable project ID tracking. This is used for project quota tracking.</p>
<dt><code>quota</code></p>
<dd>Enable internal file system quota inodes.</p>
<dt><code>read-only</code></p>
<dd>Force the kernel to mount the file system read-only.</p>
<dt><code>resize_inode</code></p>
<dd>Reserve space so the block group descriptor table may grow in the future. <code>Tune2fs</code> only supports clearing this file system feature.</p>
<dt><code>sparse_super</code></p>
<dd>Limit the number of backup superblocks to save space on large file systems. <code>Tune2fs</code> currently only supports setting this file system feature.</p>
<dt><code>stable_inodes</code></p>
<dd>Prevent the file system from being shrunk or having its UUID changed, in order to allow the use of specialized encryption settings that make use of the inode numbers and UUID. <code>Tune2fs</code> currently only supports setting this file system feature.</p>
<dt><code>uninit_bg</code></p>
<dd>Allow the kernel to initialize bitmaps and inode tables lazily, and to keep a high watermark for the unused inodes in a file system, to reduce <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) time. The first e2fsck run after enabling this feature will take the full time, but subsequent e2fsck runs will take only a fraction of the original time, depending on how full the file system is.</p>
<dt><code>verity</code></p>
<dd>Enable support for verity protected files. <code>Tune2fs</code> currently only supports setting this file system feature.</dl>
</dl>
<dd>After setting or clearing <code>sparse_super</code>, <code>uninit_bg</code>, <code>filetype</code>, or <code>resize_inode</code> file system features, the file system may require being checked using <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) to return the file system to a consistent state. <code>Tune2fs</code> will print a message requesting that the system administrator run <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) if necessary. After setting the <code>dir_index</code> feature, <code>e2fsck -D</code> can be run to convert existing directories to the hashed B-tree format. Enabling certain file system features may prevent the file system from being mounted by kernels which do not support those features. In particular, the <code>uninit_bg</code> and <code>flex_bg</code> features are only supported by the ext4 file system.</p>
<dt><code>-r</code><i> reserved-blocks-count</i></p>
<dd>Set the number of reserved file system blocks.</p>
<dt><code>-Q</code><i> quota-options</i></p>
<dd>Sets &#8216;quota&#8217; feature on the superblock and works on the quota files for the given quota type. Quota options could be one or more of the following:</p>
<dl>
<dd>
<dl>
<dt><code>[^]usrquota</code></p>
<dd>Sets/clears user quota inode in the superblock.</p>
<dt><code>[^]grpquota</code></p>
<dd>Sets/clears group quota inode in the superblock.</p>
<dt><code>[^]prjquota</code></p>
<dd>Sets/clears project quota inode in the superblock.</dl>
</dl>
<dt><code>-T</code><i> time-last-checked</i></p>
<dd>Set the time the file system was last checked using <code>e2fsck</code>. The time is interpreted using the current (local) timezone. This can be useful in scripts which use a Logical Volume Manager to make a consistent snapshot of a file system, and then check the file system during off hours to make sure it hasn&#8217;t been corrupted due to hardware problems, etc. If the file system was clean, then this option can be used to set the last checked time on the original file system. The format of <i>time-last-checked</i> is the international date format, with an optional time specifier, i.e. YYYYMMDD[HH[MM[SS]]]. The keyword <code>now</code> is also accepted, in which case the last checked time will be set to the current time.</p>
<dt><code>-u</code><i> user</i></p>
<dd>Set the user who can use the reserved file system blocks. <i>user</i> can be a numerical uid or a user name. If a user name is given, it is converted to a numerical uid before it is stored in the superblock.</p>
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
<dd>The UUID may be used by <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), and <code>/etc/<a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) (and possibly others) by specifying <code>UUID=</code><i>uuid</i> instead of a block special device name like <code>/dev/hda1</code>.</p>
<dd>See <code><a href="/docs/linux/man/8-uuidgen/">uuidgen</a></code>(8) for more information. If the system does not have a good random number generator such as <i>/dev/random</i> or <i>/dev/urandom</i>, <code>tune2fs</code> will automatically use a time-based UUID instead of a randomly-generated UUID.</p>
<dt><code>-z</code><i> undo_file</i></p>
<dd>Before overwriting a file system block, write the old contents of the block to an undo file. This undo file can be used with <a href="/docs/linux/man/8-e2undo/">e2undo</a>(8) to restore the old contents of the file system should something go wrong. If the empty string is passed as the undo_file argument, the undo file will be written to a file named tune2fs-<i>device</i>.e2undo in the directory specified via the <i>E2FSPROGS_UNDO_DIR</i> environment variable. </p>
<p> WARNING: The undo file cannot be used to recover from a power or system crash.</dl>
<h2>Bugs</h2>
<p>We haven&#8217;t found any bugs yet. That doesn&#8217;t mean there aren&#8217;t any&#8230;</p>
<h2>Author</h2>
<p><code>tune2fs</code> was written by Remy Card &lt;Remy.Card [at] linux.org&gt;. It is currently being maintained by Theodore Ts&#8217;o &lt;tytso [at] alum.mit.edu&gt;. <code>tune2fs</code> uses the ext2fs library written by Theodore Ts&#8217;o &lt;tytso [at] mit.edu&gt;. This manual page was written by Christian Kuhtz &lt;chk [at] data-hh.Hanse.DE&gt;. Time-dependent checking was added by Uwe Ohse &lt;uwe [at] tirka.gun.de&gt;.</p>
<h2>Availability</h2>
<p><code>tune2fs</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-debugfs/">debugfs</a></code>(8), <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8), <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5) </p>
