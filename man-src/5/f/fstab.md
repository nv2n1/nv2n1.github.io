---
title: "fstab(5)"
name: "fstab"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fstab/"
description: "fstab – static information about the filesystems"
---

<p>fstab &#8211; static information about the filesystems</p>
<h2>Synopsis</h2>
<p><i>/etc/fstab</i></p>
<h2>Description</h2>
<p>The file <code>fstab</code> contains descriptive information about the filesystems the system can mount. <code>fstab</code> is only read by programs, and not written; it is the duty of the system administrator to properly create and maintain this file. The order of records in <code>fstab</code> is important because <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), and <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) sequentially iterate through <code>fstab</code> doing their thing. </p>
<p> Each filesystem is described on a separate line. Fields on each line are separated by tabs or spaces. Lines starting with &#8216;#&#8217; are comments. Blank lines are ignored. </p>
<p> The following is a typical example of an <code>fstab</code> entry: </p>
<dl>
<dd>
<pre>LABEL=t-home2 /home ext4 defaults,auto_da_alloc 0 2</pre>
</dl>
<h3>The first field (<i>fs_spec</i>).</h3>
<p>This field describes the block special device, remote filesystem or filesystem image for loop device to be mounted or swap file or swap partition to be enabled. </p>
<p> For ordinary mounts, it will hold (a link to) a block special device node (as created by <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2)) for the device to be mounted, like <i>/dev/cdrom</i> or <i>/dev/sdb7</i>. For NFS mounts, this field is <i>&lt;host&gt;:&lt;dir&gt;</i>, e.g., <i>knuth.aeb.nl:/</i>. For filesystems with no storage, any string can be used, and will show up in <code><a href="/docs/linux/man/1-df/">df</a></code>(1) output, for example. Typical usage is <i>proc</i> for <code>procfs</code>; <i>mem</i>, <i>none</i>, or <i>tmpfs</i> for <code>tmpfs</code>. Other special filesystems, like <code>udev</code> and <code>sysfs</code>, are typically not listed in <code>fstab</code>. </p>
<p> LABEL=&lt;label&gt; or UUID=&lt;uuid&gt; may be given instead of a device name. This is the recommended method, as device names are often a coincidence of hardware detection order, and can change when other disks are added or removed. For example, &#8216;LABEL=Boot&#8217; or &#8216;UUID=3e6be9de-8139-11d1-9106-a43f08d823a6&#8217;. (Use a filesystem-specific tool like <code><a href="/docs/linux/man/8-e2label/">e2label</a></code>(8), <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8), or <code><a href="/docs/linux/man/8-fatlabel/">fatlabel</a></code>(8) to set LABELs on filesystems). </p>
<p> It&#8217;s also possible to use <code>PARTUUID=</code> and <code>PARTLABEL=</code>. These partitions identifiers are supported for example for GUID Partition Table (GPT). </p>
<p> See <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8) or <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8) for more details about device identifiers. </p>
<p> Note that <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) uses UUIDs as strings. The string representation of the UUID should be based on lower case characters. But when specifying the volume ID of FAT or NTFS file systems upper case characters are used (e.g UUID=&quot;A40D-85E7&quot; or UUID=&quot;61DB7756DB7779B3&quot;).</p>
<h3>The second field (<i>fs_file</i>).</h3>
<p>This field describes the mount point (target) for the filesystem. For swap partitions, this field should be specified as `none&#8217;. If the name of the mount point contains spaces or tabs these can be escaped as ` &#8242; and &#8216;	&#8217; respectively.</p>
<h3>The third field (<i>fs_vfstype</i>).</h3>
<p>This field describes the type of the filesystem. Linux supports many filesystem types: ext4, xfs, btrfs, f2fs, vfat, ntfs, hfsplus, tmpfs, sysfs, proc, iso9660, udf, squashfs, nfs, cifs, and many more. For more details, see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
<p> An entry <i>swap</i> denotes a file or partition to be used for swapping, cf. <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8). An entry <i>none</i> is useful for bind or move mounts. </p>
<p> More than one type may be specified in a comma-separated list. </p>
<p> <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) and <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) support filesystem <i>subtypes</i>. The subtype is defined by &#8216;.subtype&#8217; suffix. For example &#8216;fuse.sshfs&#8217;. It&#8217;s recommended to use subtype notation rather than add any prefix to the first fstab field (for example &#8216;sshfs#example.com&#8217; is deprecated).</p>
<h3>The fourth field (<i>fs_mntops</i>).</h3>
<p>This field describes the mount options associated with the filesystem. </p>
<p> It is formatted as a comma-separated list of options. It contains at least the type of mount (<code>ro</code> or <code>rw</code>), plus any additional options appropriate to the filesystem type (including performance-tuning options). For details, see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) or <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8). </p>
<p> Basic filesystem-independent options are: </p>
<p> <code>defaults</code></p>
<dl>
<dd>use default options: rw, suid, dev, exec, auto, nouser, and async.</dl>
<p> <code>noauto</code></p>
<dl>
<dd>do not mount when <code>mount -a</code> is given (e.g., at boot time)</dl>
<p> <code>user</code></p>
<dl>
<dd>allow a user to mount</dl>
<p> <code>owner</code></p>
<dl>
<dd>allow device owner to mount</dl>
<p> <code>comment</code></p>
<dl>
<dd>or <code>x-&lt;name&gt;</code> for use by fstab-maintaining programs</dl>
<p> <code>nofail</code></p>
<dl>
<dd>do not report errors for this device if it does not exist.</dl>
<h3>The fifth field (<i>fs_freq</i>).</h3>
<p>This field is used by <code><a href="/docs/linux/man/8-dump/">dump</a></code>(8) to determine which filesystems need to be dumped. Defaults to zero (don&#8217;t dump) if not present.</p>
<h3>The sixth field (<i>fs_passno</i>).</h3>
<p>This field is used by <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8) to determine the order in which filesystem checks are done at boot time. The root filesystem should be specified with a <i>fs_passno</i> of 1. Other filesystems should have a <i>fs_passno</i> of 2. Filesystems within a drive will be checked sequentially, but filesystems on different drives will be checked at the same time to utilize parallelism available in the hardware. Defaults to zero (don&#8217;t check the filesystem) if not present.</p>
<h2>Files</h2>
<p><i>/etc/fstab</i>, <i>&lt;fstab.h&gt;</i></p>
<h2>Notes</h2>
<p>The proper way to read records from <code>fstab</code> is to use the routines <code><a href="/docs/linux/man/3-getmntent/">getmntent</a></code>(3) or <code>libmount</code>. </p>
<p> The keyword <code>ignore</code> as a filesystem type (3rd field) is no longer supported by the pure libmount based mount utility (since util-linux v2.22).</p>
<h2>History</h2>
<p>The ancestor of this <code>fstab</code> file format appeared in 4.0BSD.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getmntent/">getmntent</a></code>(3), <code><a href="/docs/linux/man/5-fs/">fs</a></code>(5), <code><a href="/docs/linux/man/8-findmnt/">findmnt</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p><code>fstab</code> is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
