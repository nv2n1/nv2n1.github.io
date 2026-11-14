---
title: "umount(8)"
name: "umount"
section: "8"
letter: "u"
url: "/docs/linux/man/8-umount/"
description: "umount – unmount filesystems"
---

<p>umount &#8211; unmount filesystems</p>
<h2>Synopsis</h2>
<p><code>umount</code> <code>-a</code> [<code>-dflnrv</code>] [<code>-t</code> <i>fstype</i>] [<code>-O</code> <i>option</i>&#8230;] </p>
<p> <code>umount</code> [<code>-dflnrv</code>] {<i>directory</i>|<i>device</i>} </p>
<p> <code>umount</code> <code>-h</code>|<code>-V</code></p>
<h2>Description</h2>
<p>The <code>umount</code> command detaches the mentioned filesystem(s) from the file hierarchy. A filesystem is specified by giving the directory where it has been mounted. Giving the special device on which the filesystem lives may also work, but is obsolete, mainly because it will fail in case this device was mounted on more than one directory. </p>
<p> Note that a filesystem cannot be unmounted when it is &#8216;busy&#8217; &#8211; for example, when there are open files on it, or when some process has its working directory there, or when a swap file on it is in use. The offending process could even be <code>umount</code> itself &#8211; it opens libc, and libc in its turn may open for example locale files. A lazy unmount avoids this problem, but it may introduce other issues. See <code>&#8211;lazy</code> description below.</p>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dd>All of the filesystems described in <i>/proc/self/mountinfo</i> (or in deprecated <i>/etc/mtab</i>) are unmounted, except the proc, devfs, devpts, sysfs, rpc_pipefs and nfsd filesystems. This list of the filesystems may be replaced by <code>&#8211;types</code> umount option.</dl>
<p> <code>-A</code>, <code>&#8211;all-targets</code></p>
<dl>
<dd>Unmount all mountpoints in the current mount namespace for the specified filesystem. The filesystem can be specified by one of the mountpoints or the device name (or UUID, etc.). When this option is used together with <code>&#8211;recursive</code>, then all nested mounts within the filesystem are recursively unmounted. This option is only supported on systems where <i>/etc/mtab</i> is a symlink to <i>/proc/mounts</i>.</dl>
<p> <code>-c</code>, <code>&#8211;no-canonicalize</code></p>
<dl>
<dd>Do not canonicalize paths. The paths canonicalization is based on <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) and <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2) system calls. These system calls may hang in some cases (for example on NFS if server is not available). The option has to be used with canonical path to the mount point. </p>
<p> This option is silently ignored by <code>umount</code> for non-root users. </p>
<p> For more details about this option see the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) man page. Note that <code>umount</code> does not pass this option to the <code>/sbin/umount.</code><i>type</i> helpers.</dl>
<p> <code>-d</code>, <code>&#8211;detach-loop</code></p>
<dl>
<dd>When the unmounted device was a loop device, also free this loop device. This option is unnecessary for devices initialized by <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), in this case &quot;autoclear&quot; functionality is enabled by default.</dl>
<p> <code>&#8211;fake</code></p>
<dl>
<dd>Causes everything to be done except for the actual system call or umount helper execution; this &#8216;fakes&#8217; unmounting the filesystem. It can be used to remove entries from the deprecated <i>/etc/mtab</i> that were unmounted earlier with the <code>-n</code> option.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>Force an unmount (in case of an unreachable NFS system). </p>
<p> Note that this option does not guarantee that umount command does not hang. It&#8217;s strongly recommended to use absolute paths without symlinks to avoid unwanted readlink and stat system calls on unreachable NFS in <code>umount</code>.</dl>
<p> <code>-i</code>, <code>&#8211;internal-only</code></p>
<dl>
<dd>Do not call the <code>/sbin/umount.</code><i>filesystem</i> helper even if it exists. By default such a helper program is called if it exists.</dl>
<p> <code>-l</code>, <code>&#8211;lazy</code></p>
<dl>
<dd>Lazy unmount. Detach the filesystem from the file hierarchy now, and clean up all references to this filesystem as soon as it is not busy anymore. </p>
<p> A system reboot would be expected in near future if you&#8217;re going to use this option for network filesystem or local filesystem with submounts. The recommended use-case for <code>umount -l</code> is to prevent hangs on shutdown due to an unreachable network share where a normal umount will hang due to a downed server or a network partition. Remounts of the share will not be possible.</dl>
<p> <code>-N</code>, <code>&#8211;namespace</code> <i>ns</i></p>
<dl>
<dd>Perform umount in the mount namespace specified by <i>ns</i>. <i>ns</i> is either PID of process running in that namespace or special file representing that namespace. </p>
<p> <code>umount</code> switches to the namespace when it reads <i>/etc/fstab</i>, writes <i>/etc/mtab</i> (or writes to <i>/run/mount</i>) and calls <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2) system call, otherwise it runs in the original namespace. It means that the target mount namespace does not have to contain any libraries or other requirements necessary to execute <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2) command. </p>
<p> See <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7) for more information.</dl>
<p> <code>-n</code>, <code>&#8211;no-mtab</code></p>
<dl>
<dd>Unmount without writing in <i>/etc/mtab</i>.</dl>
<p> <code>-O</code>, <code>&#8211;test-opts</code> <i>option</i>&#8230;</p>
<dl>
<dd>Unmount only the filesystems that have the specified option set in <i>/etc/fstab</i>. More than one option may be specified in a comma-separated list. Each option can be prefixed with <code>no</code> to indicate that no action should be taken for this option.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Suppress &quot;not mounted&quot; error messages.</dl>
<p> <code>-R</code>, <code>&#8211;recursive</code></p>
<dl>
<dd>Recursively unmount each specified directory. Recursion for each directory will stop if any unmount operation in the chain fails for any reason. The relationship between mountpoints is determined by <i>/proc/self/mountinfo</i> entries. The filesystem must be specified by mountpoint path; a recursive unmount by device name (or UUID) is unsupported. Since version 2.37 it umounts also all over-mounted filesystems (more filesystems on the same mountpoint).</dl>
<p> <code>-r</code>, <code>&#8211;read-only</code></p>
<dl>
<dd>When an unmount fails, try to remount the filesystem read-only.</dl>
<p> <code>-t</code>, <code>&#8211;types</code> <i>type</i>&#8230;</p>
<dl>
<dd>Indicate that the actions should only be taken on filesystems of the specified <i>type</i>. More than one type may be specified in a comma-separated list. The list of filesystem types can be prefixed with <code>no</code> to indicate that no action should be taken for all of the mentioned types. Note that <code>umount</code> reads information about mounted filesystems from kernel (<i>/proc/mounts</i>) and filesystem names may be different than filesystem names used in the <i>/etc/fstab</i> (e.g., &quot;nfs4&quot; vs. &quot;nfs&quot;).</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Verbose mode.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Non-Superuser Umounts</h2>
<p>Normally, only the superuser can umount filesystems. However, when <i>fstab</i> contains the <code>user</code> option on a line, anybody can umount the corresponding filesystem. For more details see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) man page. </p>
<p> Since version 2.34 the <code>umount</code> command can be used to perform umount operation also for fuse filesystems if kernel mount table contains user&#8217;s ID. In this case fstab <code>user=</code> mount option is not required. </p>
<p> Since version 2.35 <code>umount</code> command does not exit when user permissions are inadequate by internal libmount security rules. It drops suid permissions and continue as regular non-root user. This can be used to support use-cases where root permissions are not necessary (e.g., fuse filesystems, user namespaces, etc).</p>
<h2>Loop Device</h2>
<p>The <code>umount</code> command will automatically detach loop device previously initialized by <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command independently of <i>/etc/mtab</i>. </p>
<p> In this case the device is initialized with &quot;autoclear&quot; flag (see <code><a href="/docs/linux/man/8-losetup/">losetup</a></code>(8) output for more details), otherwise it&#8217;s necessary to use the option <code>&#8211;detach-loop</code> or call <code>losetup -d &lt;device&gt;</code>. The autoclear feature is supported since Linux 2.6.25.</p>
<h2>External Helpers</h2>
<p>The syntax of external unmount helpers is:</p>
<dl>
<dd><code>umount.</code><i>suffix</i> {<i>directory</i>|<i>device</i>} [<code>-flnrv</code>] [<code>-N</code> <i>namespace</i>] [<code>-t</code> <i>type</i>.<i>subtype</i>]
</dl>
<p> where <i>suffix</i> is the filesystem type (or the value from a <code>uhelper=</code> or <code>helper=</code> marker in the mtab file). The <code>-t</code> option can be used for filesystems that have subtype support. For example:</p>
<dl>
<dd><code>umount.fuse -t fuse.sshfs</code>
</dl>
<p> A <code>uhelper=</code><i>something</i> marker (unprivileged helper) can appear in the <i>/etc/mtab</i> file when ordinary users need to be able to unmount a mountpoint that is not defined in <i>/etc/fstab</i> (for example for a device that was mounted by <code><a href="/docs/linux/man/1-udisks/">udisks</a></code>(1)). </p>
<p> A <code>helper=</code><i>type</i> marker in the mtab file will redirect all unmount requests to the <code>/sbin/umount.</code><i>type</i> helper independently of UID. </p>
<p> Note that <i>/etc/mtab</i> is currently deprecated and <code>helper=</code> and other userspace mount options are maintained by libmount.</p>
<h2>Environment</h2>
<p>LIBMOUNT_FSTAB=&lt;path&gt;</p>
<dl>
<dd>overrides the default location of the fstab file (ignored for suid)</dl>
<p> LIBMOUNT_MTAB=&lt;path&gt;</p>
<dl>
<dd>overrides the default location of the mtab file (ignored for suid)</dl>
<p> LIBMOUNT_DEBUG=all</p>
<dl>
<dd>enables <code>libmount</code> debug output</dl>
<h2>Files</h2>
<p><i>/etc/mtab</i></p>
<dl>
<dd>table of mounted filesystems (deprecated and usually replaced by symlink to <i>/proc/mounts</i>)</dl>
<p> <i>/etc/fstab</i></p>
<dl>
<dd>table of known filesystems</dl>
<p> <i>/proc/self/mountinfo</i></p>
<dl>
<dd>table of mounted filesystems generated by kernel.</dl>
<h2>History</h2>
<p>A <code>umount</code> command appeared in Version 6 AT&amp;T UNIX.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-umount/">umount</a></code>(2), <code><a href="/docs/linux/man/8-losetup/">losetup</a></code>(8), <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>umount</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
