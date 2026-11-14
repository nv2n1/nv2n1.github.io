---
title: "xfs_check(8)"
name: "xfs_check"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_check/"
description: "xfs_check – check XFS filesystem consistency"
---

<p>xfs_check &#8211; check XFS filesystem consistency</p>
<h2>Synopsis</h2>
<p><code>xfs_check</code> [ <code>-i</code> <i>ino</i> ] &#8230; [ <code>-b</code> <i>bno</i> ] &#8230; [ <code>-f</code> ] [ <code>-s</code> ] [ <code>-v</code> ] [ <code>-l</code> <i>logdev</i> ] <i>device</i></p>
<h2>Description</h2>
<p><code>xfs_check</code> checks whether an XFS filesystem is consistent. It is normally run only when there is reason to believe that the filesystem has a consistency problem. The filesystem to be checked is specified by the <i>device</i> argument, which should be the disk or volume device for the filesystem. Filesystems stored in files can also be checked, using the <code>-f</code> flag. The filesystem should normally be unmounted or read-only during the execution of <code>xfs_check</code>. Otherwise, spurious problems are reported. </p>
<p> Note that using <code>xfs_check</code> is NOT recommended. Please use <code>xfs_repair</code> <code>-n</code> instead, for better scalability and speed.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Specifies that the filesystem image to be processed is stored in a regular file at <i>device</i> (see the <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) <code>-d</code> <i>file</i> option). This might happen if an image copy of a filesystem has been made into an ordinary file.</p>
<dt><code>-l</code><i> logdev</i></p>
<dd>Specifies the device where the filesystem&#8217;s external log resides. Only for those filesystems which use an external log. See the <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) <code>-l</code> option, and refer to <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5) for a detailed description of the XFS log.</p>
<dt><code>-s</code></p>
<dd>Specifies that only serious errors should be reported. Serious errors are those that make it impossible to find major data structures in the filesystem. This option can be used to cut down the amount of output when there is a serious problem, when the output might make it difficult to see what the real problem is.</p>
<dt><code>-v</code></p>
<dd>Specifies verbose output; it is impossibly long for a reasonably-sized filesystem. This option is intended for internal use only.</p>
<dt><code>-i</code><i> ino</i></p>
<dd>Specifies verbose behavior for the specified inode <i>ino</i>. For instance, it can be used to locate all the blocks associated with a given inode.</p>
<dt><code>-b</code><i> bno</i></p>
<dd>Specifies verbose behavior for the specific filesystem block at <i>bno</i>. For instance, it can be used to determine what a specific block is used for. The block number is a &quot;file system block number&quot;. Conversion between disk addresses (i.e. addresses reported by <code><a href="/docs/linux/man/8-xfs_bmap/">xfs_bmap</a></code>(8)) and file system blocks may be accomplished using <code><a href="/docs/linux/man/8-xfs_db/">xfs_db</a></code>(8)&#8217;s <code>convert</code> command.</dl>
<p> Any output that is produced when <code>xfs_check</code> is not run in verbose mode indicates that the filesystem has an inconsistency. The filesystem can be repaired using either <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8) to fix the filesystem in place, or by using <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8) and <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) to dump the filesystem, make a new filesystem, then use <code><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></code>(8) to restore the data onto the new filesystem. Note that xfsdump may fail on a corrupt filesystem. However, if the filesystem is mountable, xfsdump can be used to try and save important data before repairing the filesystem with xfs_repair. If the filesystem is not mountable though, xfs_repair is the only viable option.</p>
<h2>Diagnostics</h2>
<p>If the filesystem is completely corrupt, a core dump might be produced instead of the message</p>
<dl>
<dd><i>device</i> <code>is not a valid filesystem</code></dl>
<p> If the filesystem is very large (has many files) then <code>xfs_check</code> might run out of memory. In this case the message</p>
<dl>
<dd><code>out of memory</code></dl>
<p> is printed. </p>
<p> The following is a description of the most likely problems and the associated messages. Most of the diagnostics produced are only meaningful with an understanding of the structure of the filesystem.</p>
<dl>
<dt><code>agf_freeblks </code><i>n</i><code>, counted </code><i>m</i><code> in ag </code><i>a</i></p>
<dd>The freeblocks count in the allocation group header for allocation group <i>a</i> doesn&#8217;t match the number of blocks counted free.</p>
<dt><code>agf_longest </code><i>n</i><code>, counted </code><i>m</i><code> in ag </code><i>a</i></p>
<dd>The longest free extent in the allocation group header for allocation group <i>a</i> doesn&#8217;t match the longest free extent found in the allocation group.</p>
<dt><code>agi_count </code><i>n</i><code>, counted </code><i>m</i><code> in ag </code><i>a</i></p>
<dd>The allocated inode count in the allocation group header for allocation group <i>a</i> doesn&#8217;t match the number of inodes counted in the allocation group.</p>
<dt><code>agi_freecount </code><i>n</i><code>, counted </code><i>m</i><code> in ag </code><i>a</i></p>
<dd>The free inode count in the allocation group header for allocation group <i>a</i> doesn&#8217;t match the number of inodes counted free in the allocation group.</p>
<dt><code>block </code><i>a/b</i><code> expected inum 0 got </code><i>i</i></p>
<dd>The block number is specified as a pair (allocation group number, block in the allocation group). The block is used multiple times (shared), between multiple inodes. This message usually follows a message of the next type.</p>
<dt><code>block </code><i>a/b</i><code> expected type unknown got </code><i>y</i></p>
<dd>The block is used multiple times (shared).</p>
<dt><code>block </code><i>a/b</i><code> type unknown not expected</code></p>
<dd>The block is unaccounted for (not in the freelist and not in use).</p>
<dt><code>link count mismatch for inode </code><i>nnn</i><code> (name </code><i>xxx</i><code>), nlink </code><i>m</i><code>, counted </code><i>n</i></p>
<dd>The inode has a bad link count (number of references in directories).</p>
<dt><code>rtblock </code><i>b</i><code> expected inum 0 got </code><i>i</i></p>
<dd>The block is used multiple times (shared), between multiple inodes. This message usually follows a message of the next type.</p>
<dt><code>rtblock </code><i>b</i><code> expected type unknown got </code><i>y</i></p>
<dd>The real-time block is used multiple times (shared).</p>
<dt><code>rtblock </code><i>b</i><code> type unknown not expected</code></p>
<dd>The real-time block is unaccounted for (not in the freelist and not in use).</p>
<dt><code>sb_fdblocks </code><i>n</i><code>, counted </code><i>m</i></p>
<dd>The number of free data blocks recorded in the superblock doesn&#8217;t match the number counted free in the filesystem.</p>
<dt><code>sb_frextents </code><i>n</i><code>, counted </code><i>m</i></p>
<dd>The number of free real-time extents recorded in the superblock doesn&#8217;t match the number counted free in the filesystem.</p>
<dt><code>sb_icount </code><i>n</i><code>, counted </code><i>m</i></p>
<dd>The number of allocated inodes recorded in the superblock doesn&#8217;t match the number allocated in the filesystem.</p>
<dt><code>sb_ifree </code><i>n</i><code>, counted </code><i>m</i></p>
<dd>The number of free inodes recorded in the superblock doesn&#8217;t match the number free in the filesystem.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8), <code><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></code>(8), <code><a href="/docs/linux/man/8-xfs_ncheck/">xfs_ncheck</a></code>(8), <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5). </p>
