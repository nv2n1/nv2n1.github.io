---
title: "mount(2)"
name: "mount"
section: "2"
letter: "m"
url: "/docs/linux/man/2-mount/"
description: "mount – mount filesystem"
---

<h2 class="name">NAME</h2>
<p> mount &#8211; mount filesystem </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/mount.h&gt;
int mount(const char *source, const char *target,
          const char *filesystemtype, unsigned long mountflags,
          const void *data);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mount</code>() attaches the filesystem specified by <i>source</i> (which is often a pathname referring to a device, but can also be the pathname of a directory or file, or a dummy string) to the location (a directory or file) specified by the pathname in <i>target</i>. </p>
<p> Appropriate privilege (Linux: the <code>CAP_SYS_ADMIN</code> capability) is required to mount filesystems. </p>
<p> Values for the <i>filesystemtype</i> argument supported by the kernel are listed in <i>/proc/filesystems</i> (e.g., &quot;btrfs&quot;, &quot;ext4&quot;, &quot;jfs&quot;, &quot;xfs&quot;, &quot;vfat&quot;, &quot;fuse&quot;, &quot;tmpfs&quot;, &quot;cgroup&quot;, &quot;proc&quot;, &quot;mqueue&quot;, &quot;nfs&quot;, &quot;cifs&quot;, &quot;iso9660&quot;). Further types may become available when the appropriate modules are loaded. </p>
<p> The <i>data</i> argument is interpreted by the different filesystems. Typically it is a string of comma-separated options understood by this filesystem. See <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) for details of the options available for each filesystem type. </p>
<p> A call to <code>mount</code>() performs one of a number of general types of operation, depending on the bits specified in <i>mountflags</i>. The choice of which operation to perform is determined by testing the bits set in <i>mountflags</i>, with the tests being conducted in the order listed here:</p>
<dl>
<dt>*</p>
<dd> Remount an existing mount: <i>mountflags</i> includes <code>MS_REMOUNT</code>.</p>
<dt>*</p>
<dd> Create a bind mount: <i>mountflags</i> includes <code>MS_BIND</code>.</p>
<dt>*</p>
<dd> Change the propagation type of an existing mount: <i>mountflags</i> includes one of <code>MS_SHARED</code>, <code>MS_PRIVATE</code>, <code>MS_SLAVE</code>, or <code>MS_UNBINDABLE</code>.</p>
<dt>*</p>
<dd> Move an existing mount to a new location: <i>mountflags</i> includes <code>MS_MOVE</code>.</p>
<dt>*</p>
<dd> Create a new mount: <i>mountflags</i> includes none of the above flags.</dl>
<p> Each of these operations is detailed later in this page. Further flags may be specified in <i>mountflags</i> to modify the behavior of <code>mount</code>(), as described below.</p>
<h3>Additional mount flags</h3>
<p> The list below describes the additional flags that can be specified in <i>mountflags</i>. Note that some operation types ignore some or all of these flags, as described later in this page.</p>
<dl>
<dt><code>MS_DIRSYNC</code> (since Linux 2.5.19)</p>
<dd> Make directory changes on this filesystem synchronous. (This property can be obtained for individual directories or subtrees using <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1).)</p>
<dt><code>MS_LAZYTIME</code> (since Linux 4.0)</p>
<dd> Reduce on-disk updates of inode timestamps (atime, mtime, ctime) by maintaining these changes only in memory. The on-disk timestamps are updated only when:</p>
<dl>
<dt>
<dd>
<dl>
<dt>(a)</p>
<dd> the inode needs to be updated for some change unrelated to file timestamps;</p>
<dt>(b)</p>
<dd> the application employs <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-syncfs/">syncfs</a></code>(2), or <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2);</p>
<dt>(c)</p>
<dd> an undeleted inode is evicted from memory; or</p>
<dt>(d)</p>
<dd> more than 24 hours have passed since the inode was written to disk.</dl>
</dl>
<dt>
<dd> This mount option significantly reduces writes needed to update the inode&#8217;s timestamps, especially mtime and atime. However, in the event of a system crash, the atime and mtime fields on disk might be out of date by up to 24 hours.</p>
<dt>
<dd> Examples of workloads where this option could be of significant benefit include frequent random writes to preallocated files, as well as cases where the <code>MS_STRICTATIME</code> mount option is also enabled. (The advantage of combining <code>MS_STRICTATIME</code> and <code>MS_LAZYTIME</code> is that <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) will return the correctly updated atime, but the atime updates will be flushed to disk only in the cases listed above.)</p>
<dt><code>MS_MANDLOCK</code></p>
<dd> Permit mandatory locking on files in this filesystem. (Mandatory locking must still be enabled on a per-file basis, as described in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).) Since Linux 4.5, this mount option requires the <code>CAP_SYS_ADMIN</code> capability and a kernel configured with the <code>CONFIG_MANDATORY_FILE_LOCKING</code> option.</p>
<dt><code>MS_NOATIME</code></p>
<dd> Do not update access times for (all types of) files on this filesystem.</p>
<dt><code>MS_NODEV</code></p>
<dd> Do not allow access to devices (special files) on this filesystem.</p>
<dt><code>MS_NODIRATIME</code></p>
<dd> Do not update access times for directories on this filesystem. This flag provides a subset of the functionality provided by <code>MS_NOATIME</code>; that is, <code>MS_NOATIME</code> implies <code>MS_NODIRATIME</code>.</p>
<dt><code>MS_NOEXEC</code></p>
<dd> Do not allow programs to be executed from this filesystem.</p>
<dt><code>MS_NOSUID</code></p>
<dd> Do not honor set-user-ID and set-group-ID bits or file capabilities when executing programs from this filesystem.</p>
<dt><code>MS_RDONLY</code></p>
<dd> Mount filesystem read-only.</p>
<dt><code>MS_REC</code> (since Linux 2.4.11)</p>
<dd> Used in conjunction with <code>MS_BIND</code> to create a recursive bind mount, and in conjunction with the propagation type flags to recursively change the propagation type of all of the mounts in a subtree. See below for further details.</p>
<dt><code>MS_RELATIME</code> (since Linux 2.6.20)</p>
<dd> When a file on this filesystem is accessed, update the file&#8217;s last access time (atime) only if the current value of atime is less than or equal to the file&#8217;s last modification time (mtime) or last status change time (ctime). This option is useful for programs, such as <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), that need to know when a file has been read since it was last modified. Since Linux 2.6.30, the kernel defaults to the behavior provided by this flag (unless <code>MS_NOATIME</code> was specified), and the <code>MS_STRICTATIME</code> flag is required to obtain traditional semantics. In addition, since Linux 2.6.30, the file&#8217;s last access time is always updated if it is more than 1 day old.</p>
<dt><code>MS_SILENT</code> (since Linux 2.6.17)</p>
<dd> Suppress the display of certain (<i>printk</i>()) warning messages in the kernel log. This flag supersedes the misnamed and obsolete <code>MS_VERBOSE</code> flag (available since Linux 2.4.12), which has the same meaning.</p>
<dt><code>MS_STRICTATIME</code> (since Linux 2.6.30)</p>
<dd> Always update the last access time (atime) when files on this filesystem are accessed. (This was the default behavior before Linux 2.6.30.) Specifying this flag overrides the effect of setting the <code>MS_NOATIME</code> and <code>MS_RELATIME</code> flags.</p>
<dt><code>MS_SYNCHRONOUS</code></p>
<dd> Make writes on this filesystem synchronous (as though the <code>O_SYNC</code> flag to <code><a href="/docs/linux/man/2-open/">open</a></code>(2) was specified for all file opens to this filesystem).</p>
<dt><code>MS_NOSYMFOLLOW</code> (since Linux 5.10)</p>
<dd> Do not follow symbolic links when resolving paths. Symbolic links can still be created, and <code><a href="/docs/linux/man/1-readlink/">readlink</a></code>(1), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/1-realpath/">realpath</a></code>(1), and <code><a href="/docs/linux/man/3-realpath/">realpath</a></code>(3) all still work properly.</dl>
<p> From Linux 2.4 onward, some of the above flags are settable on a per-mount basis, while others apply to the superblock of the mounted filesystem, meaning that all mounts of the same filesystem share those flags. (Previously, all of the flags were per-superblock.) </p>
<p> The per-mount-point flags are as follows:</p>
<dl>
<dt>*</p>
<dd> Since Linux 2.4: <code>MS_NODEV</code>, <code>MS_NOEXEC</code>, and <code>MS_NOSUID</code> flags are settable on a per-mount-point basis.</p>
<dt>*</p>
<dd> Additionally, since Linux 2.6.16: <code>MS_NOATIME</code> and <code>MS_NODIRATIME</code>.</p>
<dt>*</p>
<dd> Additionally, since Linux 2.6.20: <code>MS_RELATIME</code>.</dl>
<p> The following flags are per-superblock: <code>MS_DIRSYNC</code>, <code>MS_LAZYTIME</code>, <code>MS_MANDLOCK</code>, <code>MS_SILENT</code>, and <code>MS_SYNCHRONOUS</code>. The initial settings of these flags are determined on the first mount of the filesystem, and will be shared by all subsequent mounts of the same filesystem. Subsequently, the settings of the flags can be changed via a remount operation (see below). Such changes will be visible via all mount points associated with the filesystem. </p>
<p> Since Linux 2.6.16, <code>MS_RDONLY</code> can be set or cleared on a per-mount-point basis as well as on the underlying filesystem superblock. The mounted filesystem will be writable only if neither the filesystem nor the mountpoint are flagged as read-only.</p>
<h3>Remounting an existing mount</h3>
<p> An existing mount may be remounted by specifying <code>MS_REMOUNT</code> in <i>mountflags</i>. This allows you to change the <i>mountflags</i> and <i>data</i> of an existing mount without having to unmount and remount the filesystem. <i>target</i> should be the same value specified in the initial <code>mount</code>() call. </p>
<p> The <i>source</i> and <i>filesystemtype</i> arguments are ignored. </p>
<p> The <i>mountflags</i> and <i>data</i> arguments should match the values used in the original <code>mount</code>() call, except for those parameters that are being deliberately changed. </p>
<p> The following <i>mountflags</i> can be changed: <code>MS_LAZYTIME</code>, <code>MS_MANDLOCK</code>, <code>MS_NOATIME</code>, <code>MS_NODEV</code>, <code>MS_NODIRATIME</code>, <code>MS_NOEXEC</code>, <code>MS_NOSUID</code>, <code>MS_RELATIME</code>, <code>MS_RDONLY</code>, <code>MS_STRICTATIME</code> (whose effect is to clear the <code>MS_NOATIME</code> and <code>MS_RELATIME</code> flags), and <code>MS_SYNCHRONOUS</code>. Attempts to change the setting of the <code>MS_DIRSYNC</code> and <code>MS_SILENT</code> flags during a remount are silently ignored. Note that changes to per-superblock flags are visible via all mount points of the associated filesystem (because the per-superblock flags are shared by all mount points). </p>
<p> Since Linux 3.17, if none of <code>MS_NOATIME</code>, <code>MS_NODIRATIME</code>, <code>MS_RELATIME</code>, or <code>MS_STRICTATIME</code> is specified in <i>mountflags</i>, then the remount operation preserves the existing values of these flags (rather than defaulting to <code>MS_RELATIME</code>). </p>
<p> Since Linux 2.6.26, the <code>MS_REMOUNT</code> flag can be used with <code>MS_BIND</code> to modify only the per-mount-point flags. This is particularly useful for setting or clearing the &quot;read-only&quot; flag on a mount point without changing the underlying filesystem. Specifying <i>mountflags</i> as: </p>
<p> MS_REMOUNT | MS_BIND | MS_RDONLY </p>
<p> will make access through this mountpoint read-only, without affecting other mount points.</p>
<h3>Creating a bind mount</h3>
<p> If <i>mountflags</i> includes <code>MS_BIND</code> (available since Linux 2.4), then perform a bind mount. A bind mount makes a file or a directory subtree visible at another point within the single directory hierarchy. Bind mounts may cross filesystem boundaries and span <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) jails. </p>
<p> The <i>filesystemtype</i> and <i>data</i> arguments are ignored. </p>
<p> The remaining bits (other than <code>MS_REC</code>, described below) in the <i>mountflags</i> argument are also ignored. (The bind mount has the same mount options as the underlying mount point.) However, see the discussion of remounting above, for a method of making an existing bind mount read-only. </p>
<p> By default, when a directory is bind mounted, only that directory is mounted; if there are any submounts under the directory tree, they are not bind mounted. If the <code>MS_REC</code> flag is also specified, then a recursive bind mount operation is performed: all submounts under the <i>source</i> subtree (other than unbindable mounts) are also bind mounted at the corresponding location in the <i>target</i> subtree.</p>
<h3>Changing the propagation type of an existing mount</h3>
<p> If <i>mountflags</i> includes one of <code>MS_SHARED</code>, <code>MS_PRIVATE</code>, <code>MS_SLAVE</code>, or <code>MS_UNBINDABLE</code> (all available since Linux 2.6.15), then the propagation type of an existing mount is changed. If more than one of these flags is specified, an error results. </p>
<p> The only other flags that can be specified while changing the propagation type are <code>MS_REC</code> (described below) and <code>MS_SILENT</code> (which is ignored). </p>
<p> The <i>source</i>, <i>filesystemtype</i>, and <i>data</i> arguments are ignored. </p>
<p> The meanings of the propagation type flags are as follows:</p>
<dl>
<dt><code>MS_SHARED</code></p>
<dd> Make this mount point shared. Mount and unmount events immediately under this mount point will propagate to the other mount points that are members of this mount&#8217;s peer group. Propagation here means that the same mount or unmount will automatically occur under all of the other mount points in the peer group. Conversely, mount and unmount events that take place under peer mount points will propagate to this mount point.</p>
<dt><code>MS_PRIVATE</code></p>
<dd> Make this mount point private. Mount and unmount events do not propagate into or out of this mount point.</p>
<dt><code>MS_SLAVE</code></p>
<dd> If this is a shared mount point that is a member of a peer group that contains other members, convert it to a slave mount. If this is a shared mount point that is a member of a peer group that contains no other members, convert it to a private mount. Otherwise, the propagation type of the mount point is left unchanged.</p>
<dt>
<dd> When a mount point is a slave, mount and unmount events propagate into this mount point from the (master) shared peer group of which it was formerly a member. Mount and unmount events under this mount point do not propagate to any peer.</p>
<dt>
<dd> A mount point can be the slave of another peer group while at the same time sharing mount and unmount events with a peer group of which it is a member.</p>
<dt><code>MS_UNBINDABLE</code></p>
<dd> Make this mount unbindable. This is like a private mount, and in addition this mount can&#8217;t be bind mounted. When a recursive bind mount (<code>mount</code>() with the <code>MS_BIND</code> and <code>MS_REC</code> flags) is performed on a directory subtree, any unbindable mounts within the subtree are automatically pruned (i.e., not replicated) when replicating that subtree to produce the target subtree.</dl>
<p> By default, changing the propagation type affects only the <i>target</i> mount point. If the <code>MS_REC</code> flag is also specified in <i>mountflags</i>, then the propagation type of all mount points under <i>target</i> is also changed. </p>
<p> For further details regarding mount propagation types (including the default propagation type assigned to new mounts), see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7).</p>
<h3>Moving a mount</h3>
<p> If <i>mountflags</i> contains the flag <code>MS_MOVE</code> (available since Linux 2.4.18), then move a subtree: <i>source</i> specifies an existing mount point and <i>target</i> specifies the new location to which that mount point is to be relocated. The move is atomic: at no point is the subtree unmounted. </p>
<p> The remaining bits in the <i>mountflags</i> argument are ignored, as are the <i>filesystemtype</i> and <i>data</i> arguments.</p>
<h3>Creating a new mount point</h3>
<p> If none of <code>MS_REMOUNT</code>, <code>MS_BIND</code>, <code>MS_MOVE</code>, <code>MS_SHARED</code>, <code>MS_PRIVATE</code>, <code>MS_SLAVE</code>, or <code>MS_UNBINDABLE</code> is specified in <i>mountflags</i>, then <code>mount</code>() performs its default action: creating a new mount point. <i>source</i> specifies the source for the new mount point, and <i>target</i> specifies the directory at which to create the mount point. </p>
<p> The <i>filesystemtype</i> and <i>data</i> arguments are employed, and further bits may be specified in <i>mountflags</i> to modify the behavior of the call.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> The error values given below result from filesystem type independent errors. Each filesystem type may have its own special errors and its own special behavior. See the Linux kernel source code for details.</p>
<dl>
<dt><code>EACCES</code></p>
<dd> A component of a path was not searchable. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EACCES</code></p>
<dd> Mounting a read-only filesystem was attempted without giving the <code>MS_RDONLY</code> flag.</p>
<dt>
<dd> The filesystem may be read-only for various reasons, including: it resides on a read-only optical disk; it is resides on a device with a physical switch that has been set to mark the device read-only; the filesystem implementation was compiled with read-only support; or errors were detected when initially mounting the filesystem, so that it was marked read-only and can&#8217;t be remounted as read-write (until the errors are fixed).</p>
<dt>
<dd> Some filesystems instead return the error <code>EROFS</code> on an attempt to mount a read-only filesystem.</p>
<dt><code>EACCES</code></p>
<dd> The block device <i>source</i> is located on a filesystem mounted with the <code>MS_NODEV</code> option.</p>
<dt><code>EBUSY</code></p>
<dd> An attempt was made to stack a new mount directly on top of an existing mount point that was created in this mount namespace with the same <i>source</i> and <i>target</i>.</p>
<dt><code>EBUSY</code></p>
<dd> <i>source</i> cannot be remounted read-only, because it still holds files open for writing.</p>
<dt><code>EFAULT</code></p>
<dd> One of the pointer arguments points outside the user address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>source</i> had an invalid superblock.</p>
<dt><code>EINVAL</code></p>
<dd> A remount operation (<code>MS_REMOUNT</code>) was attempted, but <i>source</i> was not already mounted on <i>target</i>.</p>
<dt><code>EINVAL</code></p>
<dd> A move operation (<code>MS_MOVE</code>) was attempted, but the mount tree under <i>source</i> includes unbindable mounts and <i>target</i> is a mount point that has propagation type <code>MS_SHARED</code>.</p>
<dt><code>EINVAL</code></p>
<dd> A move operation (<code>MS_MOVE</code>) was attempted, but the parent mount of <i>source</i> mount has propagation type <code>MS_SHARED</code>.</p>
<dt><code>EINVAL</code></p>
<dd> A move operation (<code>MS_MOVE</code>) was attempted, but <i>source</i> was not a mount point, or was &#8216;/&#8217;.</p>
<dt><code>EINVAL</code></p>
<dd> A bind operation (<code>MS_BIND</code>) was requested where <i>source</i> referred a mount namespace magic link (i.e., a <i>/proc/[pid]/ns/mnt</i> magic link or a bind mount to such a link) and the propagation type of the parent mount of <i>target</i> was <code>MS_SHARED</code>, but propagation of the requested bind mount could lead to a circular dependency that might prevent the mount namespace from ever being freed.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mountflags</i> includes more than one of <code>MS_SHARED</code>, <code>MS_PRIVATE</code>, <code>MS_SLAVE</code>, or <code>MS_UNBINDABLE</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mountflags</i> includes <code>MS_SHARED</code>, <code>MS_PRIVATE</code>, <code>MS_SLAVE</code>, or <code>MS_UNBINDABLE</code> and also includes a flag other than <code>MS_REC</code> or <code>MS_SILENT</code>.</p>
<dt><code>EINVAL</code></p>
<dd> An attempt was made to bind mount an unbindable mount.</p>
<dt><code>EINVAL</code></p>
<dd> In an unprivileged mount namespace (i.e., a mount namespace owned by a user namespace that was created by an unprivileged user), a bind mount operation (<code>MS_BIND</code>) was attempted without specifying (<code>MS_REC</code>), which would have revealed the filesystem tree underneath one of the submounts of the directory being bound.</p>
<dt><code>ELOOP</code></p>
<dd> Too many links encountered during pathname resolution.</p>
<dt><code>ELOOP</code></p>
<dd> A move operation was attempted, and <i>target</i> is a descendant of <i>source</i>.</p>
<dt><code>EMFILE</code></p>
<dd> (In case no block device is required:) Table of dummy devices is full.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> A pathname was longer than <code>MAXPATHLEN</code>.</p>
<dt><code>ENODEV</code></p>
<dd> <i>filesystemtype</i> not configured in the kernel.</p>
<dt><code>ENOENT</code></p>
<dd> A pathname was empty or had a nonexistent component.</p>
<dt><code>ENOMEM</code></p>
<dd> The kernel could not allocate a free page to copy filenames or data into.</p>
<dt><code>ENOTBLK</code></p>
<dd> <i>source</i> is not a block device (and a device was required).</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>target</i>, or a prefix of <i>source</i>, is not a directory.</p>
<dt><code>ENXIO</code></p>
<dd> The major number of the block device <i>source</i> is out of range.</p>
<dt><code>EPERM</code></p>
<dd> The caller does not have the required privileges.</p>
<dt><code>EROFS</code></p>
<dd> Mounting a read-only filesystem was attempted without giving the <code>MS_RDONLY</code> flag. See <code>EACCES</code>, above.</dl>
<h2>VERSIONS</h2>
<p> The definitions of <code>MS_DIRSYNC</code>, <code>MS_MOVE</code>, <code>MS_PRIVATE</code>, <code>MS_REC</code>, <code>MS_RELATIME</code>, <code>MS_SHARED</code>, <code>MS_SLAVE</code>, <code>MS_STRICTATIME</code>, and <code>MS_UNBINDABLE</code> were added to glibc headers in version 2.12.</p>
<h2>CONFORMING TO</h2>
<p> This function is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> Since Linux 2.4 a single filesystem can be mounted at multiple mount points, and multiple mounts can be stacked on the same mount point. </p>
<p> The <i>mountflags</i> argument may have the magic number 0xC0ED (<code>MS_MGC_VAL</code>) in the top 16 bits. (All of the other flags discussed in DESCRIPTION occupy the low order 16 bits of <i>mountflags</i>.) Specifying <code>MS_MGC_VAL</code> was required in kernel versions prior to 2.4, but since Linux 2.4 is no longer required and is ignored if specified. </p>
<p> The original <code>MS_SYNC</code> flag was renamed <code>MS_SYNCHRONOUS</code> in 1.1.69 when a different <code>MS_SYNC</code> was added to <i>&lt;mman.h&gt;</i>. </p>
<p> Before Linux 2.4 an attempt to execute a set-user-ID or set-group-ID program on a filesystem mounted with <code>MS_NOSUID</code> would fail with <code>EPERM</code>. Since Linux 2.4 the set-user-ID and set-group-ID bits are just silently ignored in this case.</p>
<h3>Mount namespaces</h3>
<p> Starting with kernel 2.4.19, Linux provides mount namespaces. A mount namespace is the set of filesystem mounts that are visible to a process. Mount namespaces can be (and usually are) shared between multiple processes, and changes to the namespace (i.e., mounts and unmounts) by one process are visible to all other processes sharing the same namespace. (The pre-2.4.19 Linux situation can be considered as one in which a single namespace was shared by every process on the system.) </p>
<p> A child process created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) shares its parent&#8217;s mount namespace; the mount namespace is preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> A process can obtain a private mount namespace if: it was created using the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_NEWNS</code> flag, in which case its new namespace is initialized to be a <i>copy</i> of the namespace of the process that called <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2); or it calls <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) with the <code>CLONE_NEWNS</code> flag, which causes the caller&#8217;s mount namespace to obtain a private copy of the namespace that it was previously sharing with other processes, so that future mounts and unmounts by the caller are invisible to other processes (except child processes that the caller subsequently creates) and vice versa. </p>
<p> For further details on mount namespaces, see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7).</p>
<h3>Parental relationship between mount points</h3>
<p> Each mount point has a parent mount point. The overall parental relationship of all mount points defines the single directory hierarchy seen by the processes within a mount namespace. </p>
<p> The parent of a new mount point is defined when the mount point is created. In the usual case, the parent of a new mount is the mount point of the filesystem containing the directory or file at which the new mount is attached. In the case where a new mount is stacked on top of an existing mount, the parent of the new mount is the previous mount that was stacked at that location. </p>
<p> The parental relationship between mount points can be discovered via the <i>/proc/[pid]/mountinfo</i> file (see below).</p>
<h3>/proc/[pid]/mounts and /proc/[pid]/mountinfo</h3>
<p> The Linux-specific <i>/proc/[pid]/mounts</i> file exposes the list of mount points in the mount namespace of the process with the specified ID. The <i>/proc/[pid]/mountinfo</i> file exposes even more information about mount points, including the propagation type and mount ID information that makes it possible to discover the parental relationship between mount points. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) and <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7) for details of this file.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mountpoint/">mountpoint</a></code>(1), <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2), <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2), <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2), <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/8-findmnt/">findmnt</a></code>(8), <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
