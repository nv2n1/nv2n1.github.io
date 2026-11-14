---
title: "xfs_copy(8)"
name: "xfs_copy"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_copy/"
description: "xfs_copy – copy the contents of an XFS filesystem"
---

<p>xfs_copy &#8211; copy the contents of an XFS filesystem</p>
<h2>Synopsis</h2>
<p><code>xfs_copy</code> [ <code>-bd</code> ] [ <code>-L</code> <i>log</i> ] <i>source target1</i> [ <i>target2</i> &#8230; ]<br />
 <code>xfs_copy -V</code></p>
<h2>Description</h2>
<p><code>xfs_copy</code> copies an XFS filesystem to one or more targets in parallel (see <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5)). The first (<i>source</i>) argument must be the pathname of the device or file containing the XFS filesystem. The remaining arguments specify one or more <i>target</i> devices or file names. If the pathnames specify devices, a copy of the source XFS filesystem is created on each device. The <i>target</i> can also be the name of a regular file, in which case an image of the source XFS filesystem is created in that file. If the file does not exist, <code>xfs_copy</code> creates the file. The length of the resulting file is equal to the size of the source filesystem. However, if the file is created on an XFS filesystem, the file consumes roughly the amount of space actually used in the source filesystem by the filesystem and the XFS log. The space saving is because <code>xfs_copy</code> seeks over free blocks instead of copying them and the XFS filesystem supports sparse files efficiently. </p>
<p> <code>xfs_copy</code> should only be used to copy unmounted filesystems, read-only mounted filesystems, or frozen filesystems (see <code><a href="/docs/linux/man/8-xfs_freeze/">xfs_freeze</a></code>(8)). Otherwise, the generated filesystem(s) would be inconsistent or corrupt. </p>
<p> <code>xfs_copy</code> does not alter the source filesystem in any way. Each new (target) filesystem is identical to the original filesystem except that new filesystems each have a new unique filesystem identifier (UUID). Therefore, if both the old and new filesystems will be used as separate distinct filesystems, <code>xfs_copy</code> or <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8)/<code><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></code>(8) should be used to generate the new filesystem(s) instead of <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1) or other programs that do block-by-block disk copying. </p>
<p> <code>xfs_copy</code> uses synchronous writes to ensure that write errors are detected. </p>
<p> <code>xfs_copy</code> uses <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7) to perform simultaneous parallel writes. <code>xfs_copy</code> creates one additional thread for each target to be written. All threads die if <code>xfs_copy</code> terminates or aborts.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Create a duplicate (true clone) filesystem. This should be done only if the new filesystem will be used as a replacement for the original filesystem (such as in the case of disk replacement).</p>
<dt><code>-b</code></p>
<dd>The buffered option can be used to ensure direct IO is not attempted to any of the target files. This is useful when the filesystem holding the target file does not support direct IO.</p>
<dt><code>-L</code><i> log</i></p>
<dd>Specifies the location of the <i>log</i> if the default location of <i>/var/tmp/xfs_copy.log.XXXXXX</i> is not desired.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.</dl>
<h2>Diagnostics</h2>
<p><code>xfs_copy</code> reports errors to both <code>stderr</code> and in more detailed form to a generated log file whose name is of the form <i>/var/tmp/xfs_copy.log.XXXXXX</i> or a log file specified by the <code>-L</code> option. If <code>xfs_copy</code> detects a write error on a target, the copy of that one target is aborted and an error message is issued to both stderr and the log file, but the rest of the copies continue. When <code>xfs_copy</code> terminates, all aborted targets are reported to both <code>stderr</code> and the log file. </p>
<p> If all targets abort or if there is an error reading the source filesystem, <code>xfs_copy</code> immediately aborts. </p>
<p> <code>xfs_copy</code> returns an exit code of 0 if all targets are successfully copied and an exit code of 1 if any target fails.</p>
<h2>Notes</h2>
<p>When moving filesystems from one disk to another, if the original filesystem is significantly smaller than the new filesystem, and will be made larger, we recommend that <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) and <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8)/<code><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></code>(8) be used instead of using <code>xfs_copy</code> and <code><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a></code>(8). The filesystem layout resulting from using <code>xfs_copy</code>/<code>xfs_growfs</code> is almost always worse than the result of using <code>mkfs.xfs</code>/<code>xfsdump</code>/<code>xfsrestore</code> but in the case of small filesystems, the differences can have a significant performance impact. This is due to the way <code><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a></code>(8) works, and not due to any shortcoming in <code>xfs_copy</code> itself.</p>
<h2>Caveats</h2>
<p><code>xfs_copy</code> does not copy XFS filesystems that have a real-time section or XFS filesystems with external logs. In both cases, <code>xfs_copy</code> aborts with an error message.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8), <code><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></code>(8), <code><a href="/docs/linux/man/8-xfs_freeze/">xfs_freeze</a></code>(8), <code><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a></code>(8), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5). </p>
