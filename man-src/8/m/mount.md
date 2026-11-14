---
title: "mount(8)"
name: "mount"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount/"
description: "mount – mount a filesystem"
---

<p>mount &#8211; mount a filesystem</p>
<h2>Synopsis</h2>
<p><code>mount</code> [<code>-h</code>|<code>-V</code>] </p>
<p> <code>mount</code> [<code>-l</code>] [<code>-t</code> <i>fstype</i>] </p>
<p> <code>mount</code> <code>-a</code> [<code>-fFnrsvw</code>] [<code>-t</code> <i>fstype</i>] [<code>-O</code> <i>optlist</i>] </p>
<p> <code>mount</code> [<code>-fnrsvw</code>] [<code>-o</code> <i>options</i>] <i>device</i>|<i>mountpoint</i> </p>
<p> <code>mount</code> [<code>-fnrsvw</code>] [<code>-t</code> <i>fstype</i>] [<code>-o</code> <i>options</i>] <i>device mountpoint</i> </p>
<p> <code>mount</code> <code>&#8211;bind</code>|<code>&#8211;rbind</code>|<code>&#8211;move</code> <i>olddir newdir</i> </p>
<p> <code>mount</code> <code>&#8211;make</code>-[<code>shared</code>|<code>slave</code>|<code>private</code>|<code>unbindable</code>|<code>rshared</code>|<code>rslave</code>|<code>rprivate</code>|<code>runbindable</code>] <i>mountpoint</i></p>
<h2>Description</h2>
<p>All files accessible in a Unix system are arranged in one big tree, the file hierarchy, rooted at <i>/</i>. These files can be spread out over several devices. The <code>mount</code> command serves to attach the filesystem found on some device to the big file tree. Conversely, the <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) command will detach it again. The filesystem is used to control how data is stored on the device or provided in a virtual way by network or other services. </p>
<p> The standard form of the <code>mount</code> command is:</p>
<dl>
<dd><code>mount -t</code> <i>type device dir</i>
</dl>
<p> This tells the kernel to attach the filesystem found on <i>device</i> (which is of type <i>type</i>) at the directory <i>dir</i>. The option <code>-t</code> <i>type</i> is optional. The <code>mount</code> command is usually able to detect a filesystem. The root permissions are necessary to mount a filesystem by default. See section &quot;Non-superuser mounts&quot; below for more details. The previous contents (if any) and owner and mode of <i>dir</i> become invisible, and as long as this filesystem remains mounted, the pathname <i>dir</i> refers to the root of the filesystem on <i>device</i>. </p>
<p> If only the directory or the device is given, for example:</p>
<dl>
<dd><code>mount /dir</code>
</dl>
<p> then <code>mount</code> looks for a mountpoint (and if not found then for a device) in the <i>/etc/fstab</i> file. It&#8217;s possible to use the <code>&#8211;target</code> or <code>&#8211;source</code> options to avoid ambiguous interpretation of the given argument. For example:</p>
<dl>
<dd><code>mount &#8211;target /mountpoint</code>
</dl>
<p> The same filesystem may be mounted more than once, and in some cases (e.g., network filesystems) the same filesystem may be mounted on the same mountpoint multiple times. The <code>mount</code> command does not implement any policy to control this behavior. All behavior is controlled by the kernel and it is usually specific to the filesystem driver. The exception is <code>&#8211;all</code>, in this case already mounted filesystems are ignored (see <code>&#8211;all</code> below for more details).</p>
<h3>Listing the mounts</h3>
<p>The listing mode is maintained for backward compatibility only. </p>
<p> For more robust and customizable output use <code><a href="/docs/linux/man/8-findmnt/">findmnt</a></code>(8), <code>especially in your scripts</code>. Note that control characters in the mountpoint name are replaced with &#8216;?&#8217;. </p>
<p> The following command lists all mounted filesystems (of type <i>type</i>):</p>
<dl>
<dd><code>mount</code> [<code>-l</code>] [<code>-t</code> <i>type</i>]
</dl>
<p> The option <code>-l</code> adds labels to this listing. See below.</p>
<h3>Indicating the device and filesystem</h3>
<p>Most devices are indicated by a filename (of a block special device), like <i>/dev/sda1</i>, but there are other possibilities. For example, in the case of an NFS mount, <i>device</i> may look like <i>knuth.cwi.nl:/dir</i>. </p>
<p> The device names of disk partitions are unstable; hardware reconfiguration, and adding or removing a device can cause changes in names. This is the reason why it&#8217;s strongly recommended to use filesystem or partition identifiers like UUID or LABEL. Currently supported identifiers (tags): </p>
<p> LABEL=<i>label</i></p>
<dl>
<dd>Human readable filesystem identifier. See also <code>-L</code>.</dl>
<p> UUID=<i>uuid</i></p>
<dl>
<dd>Filesystem universally unique identifier. The format of the UUID is usually a series of hex digits separated by hyphens. See also <code>-U</code>. </p>
<p> Note that <code>mount</code> uses UUIDs as strings. The UUIDs from the command line or from <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) are not converted to internal binary representation. The string representation of the UUID should be based on lower case characters.</dl>
<p> PARTLABEL=<i>label</i></p>
<dl>
<dd>Human readable partition identifier. This identifier is independent on filesystem and does not change by mkfs or mkswap operations It&#8217;s supported for example for GUID Partition Tables (GPT).</dl>
<p> PARTUUID=<i>uuid</i></p>
<dl>
<dd>Partition universally unique identifier. This identifier is independent on filesystem and does not change by mkfs or mkswap operations It&#8217;s supported for example for GUID Partition Tables (GPT).</dl>
<p> ID=<i>id</i></p>
<dl>
<dd>Hardware block device ID as generated by udevd. This identifier is usually based on WWN (unique storage identifier) and assigned by the hardware manufacturer. See <code>ls /dev/disk/by-id</code> for more details, this directory and running udevd is required. This identifier is not recommended for generic use as the identifier is not strictly defined and it depends on udev, udev rules and hardware.</dl>
<p> The command <code>lsblk &#8211;fs</code> provides an overview of filesystems, LABELs and UUIDs on available block devices. The command <code>blkid -p &lt;device&gt;</code> provides details about a filesystem on the specified device. </p>
<p> Don&#8217;t forget that there is no guarantee that UUIDs and labels are really unique, especially if you move, share or copy the device. Use <code>lsblk -o +UUID,PARTUUID</code> to verify that the UUIDs are really unique in your system. </p>
<p> The recommended setup is to use tags (e.g. <code>UUID</code>=<i>uuid</i>) rather than <i>/dev/disk/by-{label,uuid,id,partuuid,partlabel}</i> udev symlinks in the <i>/etc/fstab</i> file. Tags are more readable, robust and portable. The <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command internally uses udev symlinks, so the use of symlinks in <i>/etc/fstab</i> has no advantage over tags. For more details see <code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3). </p>
<p> The <i>proc</i> filesystem is not associated with a special device, and when mounting it, an arbitrary keyword &#8211; for example, <i>proc</i> &#8211; can be used instead of a device specification. (The customary choice <i>none</i> is less fortunate: the error message &#8216;none already mounted&#8217; from <code>mount</code> can be confusing.)</p>
<h3>The files /etc/fstab, /etc/mtab and /proc/mounts</h3>
<p>The file <i>/etc/fstab</i> (see <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5)), may contain lines describing what devices are usually mounted where, using which options. The default location of the <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) file can be overridden with the <code>&#8211;fstab</code> <i>path</i> command-line option (see below for more details). </p>
<p> The command</p>
<dl>
<dd><code>mount -a</code> [<code>-t</code> <i>type</i>] [<code>-O</code> <i>optlist</i>]
</dl>
<p> (usually given in a bootscript) causes all filesystems mentioned in <i>fstab</i> (of the proper type and/or having or not having the proper options) to be mounted as indicated, except for those whose line contains the <code>noauto</code> keyword. Adding the <code>-F</code> option will make <code>mount</code> fork, so that the filesystems are mounted in parallel. </p>
<p> When mounting a filesystem mentioned in <i>fstab</i> or <i>mtab</i>, it suffices to specify on the command line only the device, or only the mount point. </p>
<p> The programs <code>mount</code> and <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) traditionally maintained a list of currently mounted filesystems in the file <i>/etc/mtab</i>. The support for regular classic <i>/etc/mtab</i> is completely disabled at compile time by default, because on current Linux systems it is better to make <i>/etc/mtab</i> a symlink to <i>/proc/mounts</i> instead. The regular <i>mtab</i> file maintained in userspace cannot reliably work with namespaces, containers and other advanced Linux features. If the regular <i>mtab</i> support is enabled, then it&#8217;s possible to use the file as well as the symlink. </p>
<p> If no arguments are given to <code>mount</code>, the list of mounted filesystems is printed. </p>
<p> If you want to override mount options from <i>/etc/fstab</i>, you have to use the <code>-o</code> option:</p>
<dl>
<dd><code>mount</code> <i>device</i>*<code>*</code>|<i>dir</i> <code>-o</code> <i>options</i>
</dl>
<p> and then the mount options from the command line will be appended to the list of options from <i>/etc/fstab</i>. This default behaviour can be changed using the <code>&#8211;options-mode</code> command-line option. The usual behavior is that the last option wins if there are conflicting ones. </p>
<p> The <code>mount</code> program does not read the <i>/etc/fstab</i> file if both <i>device</i> (or LABEL, UUID, ID, PARTUUID or PARTLABEL) and <i>dir</i> are specified. For example, to mount device <code>foo</code> at <code>/dir</code>:</p>
<dl>
<dd><code>mount /dev/foo /dir</code>
</dl>
<p> This default behaviour can be changed by using the <code>&#8211;options-source-force</code> command-line option to always read configuration from <i>fstab</i>. For non-root users <code>mount</code> always reads the <i>fstab</i> configuration.</p>
<h3>Non-superuser mounts</h3>
<p>Normally, only the superuser can mount filesystems. However, when <i>fstab</i> contains the <code>user</code> option on a line, anybody can mount the corresponding filesystem. </p>
<p> Thus, given a line</p>
<dl>
<dd><code>/dev/cdrom /cd iso9660 ro,user,noauto,unhide</code>
</dl>
<p> any user can mount the iso9660 filesystem found on an inserted CDROM using the command:</p>
<dl>
<dd><code>mount /cd</code>
</dl>
<p> Note that <code>mount</code> is very strict about non-root users and all paths specified on command line are verified before <i>fstab</i> is parsed or a helper program is executed. It&#8217;s strongly recommended to use a valid mountpoint to specify filesystem, otherwise <code>mount</code> may fail. For example it&#8217;s a bad idea to use NFS or CIFS source on command line. </p>
<p> Since util-linux 2.35, <code>mount</code> does not exit when user permissions are inadequate according to libmount&#8217;s internal security rules. Instead, it drops suid permissions and continues as regular non-root user. This behavior supports use-cases where root permissions are not necessary (e.g., fuse filesystems, user namespaces, etc). </p>
<p> For more details, see <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5). Only the user that mounted a filesystem can unmount it again. If any user should be able to unmount it, then use <code>users</code> instead of <code>user</code> in the <i>fstab</i> line. The <code>owner</code> option is similar to the <code>user</code> option, with the restriction that the user must be the owner of the special file. This may be useful e.g. for <i>/dev/fd</i> if a login script makes the console user owner of this device. The <code>group</code> option is similar, with the restriction that the user must be a member of the group of the special file.</p>
<h3>Bind mount operation</h3>
<p>Remount part of the file hierarchy somewhere else. The call is:</p>
<dl>
<dd><code>mount &#8211;bind</code> <i>olddir newdir</i>
</dl>
<p> or by using this <i>fstab</i> entry:</p>
<dl>
<dd><code>/</code><i>olddir</i> <code>/</code><i>newdir</i> <code>none bind</code>
</dl>
<p> After this call the same contents are accessible in two places. </p>
<p> It is important to understand that &quot;bind&quot; does not create any second-class or special node in the kernel VFS. The &quot;bind&quot; is just another operation to attach a filesystem. There is nowhere stored information that the filesystem has been attached by a &quot;bind&quot; operation. The <i>olddir</i> and <i>newdir</i> are independent and the <i>olddir</i> may be unmounted. </p>
<p> One can also remount a single file (on a single file). It&#8217;s also possible to use a bind mount to create a mountpoint from a regular directory, for example:</p>
<dl>
<dd><code>mount &#8211;bind foo foo</code>
</dl>
<p> The bind mount call attaches only (part of) a single filesystem, not possible submounts. The entire file hierarchy including submounts can be attached a second place by using:</p>
<dl>
<dd><code>mount &#8211;rbind</code> <i>olddir newdir</i>
</dl>
<p> Note that the filesystem mount options maintained by the kernel will remain the same as those on the original mount point. The userspace mount options (e.g., _netdev) will not be copied by <code>mount</code> and it&#8217;s necessary to explicitly specify the options on the <code>mount</code> command line. </p>
<p> Since util-linux 2.27 <code>mount</code> permits changing the mount options by passing the relevant options along with <code>&#8211;bind</code>. For example:</p>
<dl>
<dd><code>mount -o bind,ro foo foo</code>
</dl>
<p> This feature is not supported by the Linux kernel; it is implemented in userspace by an additional <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) remounting system call. This solution is not atomic. </p>
<p> The alternative (classic) way to create a read-only bind mount is to use the remount operation, for example:</p>
<dl>
<dd><code>mount &#8211;bind</code> <i>olddir newdir</i> <code>mount -o remount,bind,ro</code> <i>olddir newdir</i>
</dl>
<p> Note that a read-only bind will create a read-only mountpoint (VFS entry), but the original filesystem superblock will still be writable, meaning that the <i>olddir</i> will be writable, but the <i>newdir</i> will be read-only. </p>
<p> It&#8217;s also possible to change nosuid, nodev, noexec, noatime, nodiratime and relatime VFS entry flags via a &quot;remount,bind&quot; operation. The other flags (for example filesystem-specific flags) are silently ignored. It&#8217;s impossible to change mount options recursively (for example with <code>-o rbind,ro</code>). </p>
<p> Since util-linux 2.31, <code>mount</code> ignores the <code>bind</code> flag from <i>/etc/fstab</i> on a <code>remount</code> operation (if &quot;-o remount&quot; is specified on command line). This is necessary to fully control mount options on remount by command line. In previous versions the bind flag has been always applied and it was impossible to re-define mount options without interaction with the bind semantic. This <code>mount</code> behavior does not affect situations when &quot;remount,bind&quot; is specified in the <i>/etc/fstab</i> file.</p>
<h3>The move operation</h3>
<p>Move a <code>mounted tree</code> to another place (atomically). The call is:</p>
<dl>
<dd><code>mount &#8211;move</code> <i>olddir newdir</i>
</dl>
<p> This will cause the contents which previously appeared under <i>olddir</i> to now be accessible under <i>newdir</i>. The physical location of the files is not changed. Note that <i>olddir</i> has to be a mountpoint. </p>
<p> Note also that moving a mount residing under a shared mount is invalid and unsupported. Use <code>findmnt -o TARGET,PROPAGATION</code> to see the current propagation flags.</p>
<h3>Shared subtree operations</h3>
<p>Since Linux 2.6.15 it is possible to mark a mount and its submounts as shared, private, slave or unbindable. A shared mount provides the ability to create mirrors of that mount such that mounts and unmounts within any of the mirrors propagate to the other mirror. A slave mount receives propagation from its master, but not vice versa. A private mount carries no propagation abilities. An unbindable mount is a private mount which cannot be cloned through a bind operation. The detailed semantics are documented in <i>Documentation/filesystems/sharedsubtree.txt</i> file in the kernel source tree; see also <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7). </p>
<p> Supported operations are: </p>
<dl>
<dd>
<pre>mount --make-shared mountpoint
mount --make-slave mountpoint
mount --make-private mountpoint
mount --make-unbindable mountpoint</pre>
</dl>
<p> The following commands allow one to recursively change the type of all the mounts under a given mountpoint. </p>
<dl>
<dd>
<pre>mount --make-rshared mountpoint
mount --make-rslave mountpoint
mount --make-rprivate mountpoint
mount --make-runbindable mountpoint</pre>
</dl>
<p> <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) <code>does not read</code> <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) when a <code>&#8211;make-</code>* operation is requested. All necessary information has to be specified on the command line. </p>
<p> Note that the Linux kernel does not allow changing multiple propagation flags with a single <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) system call, and the flags cannot be mixed with other mount options and operations. </p>
<p> Since util-linux 2.23 the <code>mount</code> command can be used to do more propagation (topology) changes by one <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) call and do it also together with other mount operations. The propagation flags are applied by additional <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) system calls when the preceding mount operations were successful. Note that this use case is not atomic. It is possible to specify the propagation flags in <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) as mount options (<code>private</code>, <code>slave</code>, <code>shared</code>, <code>unbindable</code>, <code>rprivate</code>, <code>rslave</code>, <code>rshared</code>, <code>runbindable</code>). </p>
<p> For example: </p>
<dl>
<dd>
<pre>mount --make-private --make-unbindable /dev/sda1 /foo</pre>
</dl>
<p> is the same as: </p>
<dl>
<dd>
<pre>mount /dev/sda1 /foo
mount --make-private /foo
mount --make-unbindable /foo</pre>
</dl>
<h2>Command-Line Options</h2>
<p>The full set of mount options used by an invocation of <code>mount</code> is determined by first extracting the mount options for the filesystem from the <i>fstab</i> table, then applying any options specified by the <code>-o</code> argument, and finally applying a <code>-r</code> or <code>-w</code> option, when present. </p>
<p> The <code>mount</code> command does not pass all command-line options to the <code>/sbin/mount.</code><i>suffix</i> mount helpers. The interface between <code>mount</code> and the mount helpers is described below in the section <code>EXTERNAL HELPERS</code>. </p>
<p> Command-line options available for the <code>mount</code> command are: </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dd>Mount all filesystems (of the given types) mentioned in <i>fstab</i> (except for those whose line contains the <code>noauto</code> keyword). The filesystems are mounted following their order in <i>fstab</i>. The <code>mount</code> command compares filesystem source, target (and fs root for bind mount or btrfs) to detect already mounted filesystems. The kernel table with already mounted filesystems is cached during <code>mount &#8211;all</code>. This means that all duplicated <i>fstab</i> entries will be mounted. </p>
<p> The option <code>&#8211;all</code> is possible to use for remount operation too. In this case all filters (<code>-t</code> and <code>-O</code>) are applied to the table of already mounted filesystems. </p>
<p> Since version 2.35 is possible to use the command line option <code>-o</code> to alter mount options from <i>fstab</i> (see also <code>&#8211;options-mode</code>). </p>
<p> Note that it is a bad practice to use <code>mount -a</code> for <i>fstab</i> checking. The recommended solution is <code>findmnt &#8211;verify</code>.</dl>
<p> <code>-B</code>, <code>&#8211;bind</code></p>
<dl>
<dd>Remount a subtree somewhere else (so that its contents are available in both places). See above, under <code>Bind mounts</code>.</dl>
<p> <code>-c</code>, <code>&#8211;no-canonicalize</code></p>
<dl>
<dd>Don&#8217;t canonicalize paths. The <code>mount</code> command canonicalizes all paths (from the command line or <i>fstab</i>) by default. This option can be used together with the <code>-f</code> flag for already canonicalized absolute paths. The option is designed for mount helpers which call <code>mount -i</code>. It is strongly recommended to not use this command-line option for normal mount operations. </p>
<p> Note that <code>mount</code> does not pass this option to the <code>/sbin/mount.</code><i>type</i> helpers.</dl>
<p> <code>-F</code>, <code>&#8211;fork</code></p>
<dl>
<dd>(Used in conjunction with <code>-a</code>.) Fork off a new incarnation of <code>mount</code> for each device. This will do the mounts on different devices or different NFS servers in parallel. This has the advantage that it is faster; also NFS timeouts proceed in parallel. A disadvantage is that the order of the mount operations is undefined. Thus, you cannot use this option if you want to mount both <i>/usr</i> and <i>/usr/spool</i>.</dl>
<p> <code>-f, &#8211;fake</code></p>
<dl>
<dd>Causes everything to be done except for the actual system call; if it&#8217;s not obvious, this &quot;fakes&quot; mounting the filesystem. This option is useful in conjunction with the <code>-v</code> flag to determine what the <code>mount</code> command is trying to do. It can also be used to add entries for devices that were mounted earlier with the <code>-n</code> option. The <code>-f</code> option checks for an existing record in <i>/etc/mtab</i> and fails when the record already exists (with a regular non-fake mount, this check is done by the kernel).</dl>
<p> <code>-i, &#8211;internal-only</code></p>
<dl>
<dd>Don&#8217;t call the <code>/sbin/mount.</code><i>filesystem</i> helper even if it exists.</dl>
<p> <code>-L</code>, <code>&#8211;label</code> <i>label</i></p>
<dl>
<dd>Mount the partition that has the specified <i>label</i>.</dl>
<p> <code>-l</code>, <code>&#8211;show-labels</code></p>
<dl>
<dd>Add the labels in the mount output. <code>mount</code> must have permission to read the disk device (e.g. be set-user-ID root) for this to work. One can set such a label for ext2, ext3 or ext4 using the <code><a href="/docs/linux/man/8-e2label/">e2label</a></code>(8) utility, or for XFS using <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8), or for reiserfs using <code><a href="/docs/linux/man/8-reiserfstune/">reiserfstune</a></code>(8).</dl>
<p> <code>-M</code>, <code>&#8211;move</code></p>
<dl>
<dd>Move a subtree to some other place. See above, the subsection <code>The move operation</code>.</dl>
<p> <code>-n</code>, <code>&#8211;no-mtab</code></p>
<dl>
<dd>Mount without writing in <i>/etc/mtab</i>. This is necessary for example when <i>/etc</i> is on a read-only filesystem.</dl>
<p> <code>-N</code>, <code>&#8211;namespace</code> <i>ns</i></p>
<dl>
<dd>Perform the mount operation in the mount namespace specified by <i>ns</i>. <i>ns</i> is either PID of process running in that namespace or special file representing that namespace. </p>
<p> <code>mount</code> switches to the mount namespace when it reads <i>/etc/fstab</i>, writes <i>/etc/mtab: (or writes to _/run/mount</i>) and calls the <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) system call, otherwise it runs in the original mount namespace. This means that the target namespace does not have to contain any libraries or other requirements necessary to execute the <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) call. </p>
<p> See <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7) for more information.</dl>
<p> <code>-O</code>, <code>&#8211;test-opts</code> <i>opts</i></p>
<dl>
<dd>Limit the set of filesystems to which the <code>-a</code> option applies. In this regard it is like the <code>-t</code> option except that <code>-O</code> is useless without <code>-a</code>. For example, the command </p>
<p> <code>mount -a -O no_netdev</code> </p>
<p> mounts all filesystems except those which have the option <i>netdev</i> specified in the options field in the <i>/etc/fstab</i> file. </p>
<p> It is different from <code>-t</code> in that each option is matched exactly; a leading <code>no</code> at the beginning of one option does not negate the rest. </p>
<p> The <code>-t</code> and <code>-O</code> options are cumulative in effect; that is, the command </p>
<p> <code>mount -a -t ext2 -O _netdev</code> </p>
<p> mounts all ext2 filesystems with the _netdev option, not all filesystems that are either ext2 or have the _netdev option specified.</dl>
<p> <code>-o</code>, <code>&#8211;options</code> <i>opts</i></p>
<dl>
<dd>Use the specified mount options. The <i>opts</i> argument is a comma-separated list. For example: </p>
<p> <code>mount LABEL=mydisk -o noatime,nodev,nosuid</code> </p>
<p> For more details, see the <code>FILESYSTEM-INDEPENDENT MOUNT OPTIONS</code> and <code>FILESYSTEM-SPECIFIC MOUNT OPTIONS</code> sections.</dl>
<p> <code>&#8211;options-mode</code> <i>mode</i></p>
<dl>
<dd>Controls how to combine options from <i>fstab</i>/<i>mtab</i> with options from the command line. <i>mode</i> can be one of <code>ignore</code>, <code>append</code>, <code>prepend</code> or <code>replace</code>. For example, <code>append</code> means that options from <i>fstab</i> are appended to options from the command line. The default value is <code>prepend</code> &#8212; it means command line options are evaluated after <i>fstab</i> options. Note that the last option wins if there are conflicting ones.</dl>
<p> <code>&#8211;options-source</code> <i>source</i></p>
<dl>
<dd>Source of default options. <i>source</i> is a comma-separated list of <code>fstab</code>, <code>mtab</code> and <code>disable</code>. <code>disable</code> disables <code>fstab</code> and <code>mtab</code> and disables <code>&#8211;options-source-force</code>. The default value is <code>fstab,mtab</code>.</dl>
<p> <code>&#8211;options-source-force</code></p>
<dl>
<dd>Use options from <i>fstab</i>/<i>mtab</i> even if both <i>device</i> and <i>dir</i> are specified.</dl>
<p> <code>-R</code>, <code>&#8211;rbind</code></p>
<dl>
<dd>Remount a subtree and all possible submounts somewhere else (so that its contents are available in both places). See above, the subsection <code>Bind mounts</code>.</dl>
<p> <code>-r</code>, <code>&#8211;read-only</code></p>
<dl>
<dd>Mount the filesystem read-only. A synonym is <code>-o ro</code>. </p>
<p> Note that, depending on the filesystem type, state and kernel behavior, the system may still write to the device. For example, ext3 and ext4 will replay the journal if the filesystem is dirty. To prevent this kind of write access, you may want to mount an ext3 or ext4 filesystem with the <code>ro,noload</code> mount options or set the block device itself to read-only mode, see the <code><a href="/docs/linux/man/8-blockdev/">blockdev</a></code>(8) command.</dl>
<p> <code>-s</code></p>
<dl>
<dd>Tolerate sloppy mount options rather than failing. This will ignore mount options not supported by a filesystem type. Not all filesystems support this option. Currently it&#8217;s supported by the <code>mount.nfs</code> mount helper only.</dl>
<p> <code>&#8211;source</code> <i>device</i></p>
<dl>
<dd>If only one argument for the <code>mount</code> command is given, then the argument might be interpreted as the target (mountpoint) or source (device). This option allows you to explicitly define that the argument is the mount source.</dl>
<p> <code>&#8211;target</code> <i>directory</i></p>
<dl>
<dd>If only one argument for the mount command is given, then the argument might be interpreted as the target (mountpoint) or source (device). This option allows you to explicitly define that the argument is the mount target.</dl>
<p> <code>&#8211;target-prefix</code> <i>directory</i></p>
<dl>
<dd>Prepend the specified directory to all mount targets. This option can be used to follow <i>fstab</i>, but mount operations are done in another place, for example: </p>
<p> <code>mount &#8211;all &#8211;target-prefix /chroot -o X-mount.mkdir</code> </p>
<p> mounts all from system <i>fstab</i> to <i>/chroot</i>, all missing mountpoint are created (due to X-mount.mkdir). See also <code>&#8211;fstab</code> to use an alternative <i>fstab</i>.</dl>
<p> <code>-T</code>, <code>&#8211;fstab</code> <i>path</i></p>
<dl>
<dd>Specifies an alternative <i>fstab</i> file. If <i>path</i> is a directory, then the files in the directory are sorted by <code><a href="/docs/linux/man/3-strverscmp/">strverscmp</a></code>(3); files that start with &quot;.&quot; or without an <i>.fstab</i> extension are ignored. The option can be specified more than once. This option is mostly designed for initramfs or chroot scripts where additional configuration is specified beyond standard system configuration. </p>
<p> Note that <code>mount</code> does not pass the option <code>&#8211;fstab</code> to the <code>/sbin/mount.</code><i>type</i> helpers, meaning that the alternative <i>fstab</i> files will be invisible for the helpers. This is no problem for normal mounts, but user (non-root) mounts always require <i>fstab</i> to verify the user&#8217;s rights.</dl>
<p> <code>-t</code>, <code>&#8211;types</code> <i>fstype</i></p>
<dl>
<dd>The argument following the <code>-t</code> is used to indicate the filesystem type. The filesystem types which are currently supported depend on the running kernel. See <i>/proc/filesystems</i> and <i>/lib/modules/$(uname -r)/kernel/fs</i> for a complete list of the filesystems. The most common are ext2, ext3, ext4, xfs, btrfs, vfat, sysfs, proc, nfs and cifs. </p>
<p> The programs <code>mount</code> and <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) support filesystem subtypes. The subtype is defined by a &#8216;.subtype&#8217; suffix. For example &#8216;fuse.sshfs&#8217;. It&#8217;s recommended to use subtype notation rather than add any prefix to the mount source (for example &#8216;sshfs#example.com&#8217; is deprecated). </p>
<p> If no <code>-t</code> option is given, or if the <code>auto</code> type is specified, <code>mount</code> will try to guess the desired type. <code>mount</code> uses the <code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3) library for guessing the filesystem type; if that does not turn up anything that looks familiar, <code>mount</code> will try to read the file <i>/etc/filesystems</i>, or, if that does not exist, <i>/proc/filesystems</i>. All of the filesystem types listed there will be tried, except for those that are labeled &quot;nodev&quot; (e.g. <i>devpts</i>, <i>proc</i> and <i>nfs</i>). If <i>/etc/filesystems</i> ends in a line with a single *, mount will read <i>/proc/filesystems</i> afterwards. While trying, all filesystem types will be mounted with the mount option <code>silent</code>. </p>
<p> The <code>auto</code> type may be useful for user-mounted floppies. Creating a file <i>/etc/filesystems</i> can be useful to change the probe order (e.g., to try vfat before msdos or ext3 before ext2) or if you use a kernel module autoloader. </p>
<p> More than one type may be specified in a comma-separated list, for the <code>-t</code> option as well as in an <i>/etc/fstab</i> entry. The list of filesystem types for the <code>-t</code> option can be prefixed with <code>no</code> to specify the filesystem types on which no action should be taken. The prefix <code>no</code> has no effect when specified in an <i>/etc/fstab</i> entry. </p>
<p> The prefix <code>no</code> can be meaningful with the <code>-a</code> option. For example, the command </p>
<p> <code>mount -a -t nomsdos,smbfs</code> </p>
<p> mounts all filesystems except those of type <i>msdos</i> and <i>smbfs</i>. </p>
<p> For most types all the <code>mount</code> program has to do is issue a simple <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) system call, and no detailed knowledge of the filesystem type is required. For a few types however (like nfs, nfs4, cifs, smbfs, ncpfs) an ad hoc code is necessary. The nfs, nfs4, cifs, smbfs, and ncpfs filesystems have a separate mount program. In order to make it possible to treat all types in a uniform way, <code>mount</code> will execute the program <code>/sbin/mount.</code><i>type</i> (if that exists) when called with type <i>type</i>. Since different versions of the <code>smbmount</code> program have different calling conventions, <code>/sbin/mount.smbfs</code> may have to be a shell script that sets up the desired call.</dl>
<p> <code>-U</code>, <code>&#8211;uuid</code> <i>uuid</i></p>
<dl>
<dd>Mount the partition that has the specified <i>uuid</i>.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Verbose mode.</dl>
<p> <code>-w</code>, <code>&#8211;rw</code>, <code>&#8211;read-write</code></p>
<dl>
<dd>Mount the filesystem read/write. Read-write is the kernel default and the <code>mount</code> default is to try read-only if the previous mount syscall with read-write flags on write-protected devices of filesystems failed. </p>
<p> A synonym is <code>-o rw</code>. </p>
<p> Note that specifying <code>-w</code> on the command line forces <code>mount</code> to never try read-only mount on write-protected devices or already mounted read-only filesystems.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Filesystem-Independent Mount Options</h2>
<p>Some of these options are only useful when they appear in the <i>/etc/fstab</i> file. </p>
<p> Some of these options could be enabled or disabled by default in the system kernel. To check the current setting see the options in <i>/proc/mounts</i>. Note that filesystems also have per-filesystem specific default mount options (see for example <code>tune2fs -l</code> output for ext_N_ filesystems). </p>
<p> The following options apply to any filesystem that is being mounted (but not every filesystem actually honors them &#8211; e.g., the <code>sync</code> option today has an effect only for ext2, ext3, ext4, fat, vfat, ufs and xfs): </p>
<p> <code>async</code></p>
<dl>
<dd>All I/O to the filesystem should be done asynchronously. (See also the <code>sync</code> option.)</dl>
<p> <code>atime</code></p>
<dl>
<dd>Do not use the <code>noatime</code> feature, so the inode access time is controlled by kernel defaults. See also the descriptions of the <code>relatime</code> and <code>strictatime</code> mount options.</dl>
<p> <code>noatime</code></p>
<dl>
<dd>Do not update inode access times on this filesystem (e.g. for faster access on the news spool to speed up news servers). This works for all inode types (directories too), so it implies <code>nodiratime</code>.</dl>
<p> <code>auto</code></p>
<dl>
<dd>Can be mounted with the <code>-a</code> option.</dl>
<p> <code>noauto</code></p>
<dl>
<dd>Can only be mounted explicitly (i.e., the <code>-a</code> option will not cause the filesystem to be mounted).</dl>
<p> <code>context=</code><i>context</i>, <code>fscontext=</code><i>context</i>, <code>defcontext=</code><i>context</i>, and <code>rootcontext=</code><i>context</i></p>
<dl>
<dd>The <code>context=</code> option is useful when mounting filesystems that do not support extended attributes, such as a floppy or hard disk formatted with VFAT, or systems that are not normally running under SELinux, such as an ext3 or ext4 formatted disk from a non-SELinux workstation. You can also use <code>context=</code> on filesystems you do not trust, such as a floppy. It also helps in compatibility with xattr-supporting filesystems on earlier 2.4.&lt;x&gt; kernel versions. Even where xattrs are supported, you can save time not having to label every file by assigning the entire disk one security context. </p>
<p> A commonly used option for removable media is <code>context=&quot;system_u:object_r:removable_t</code>. </p>
<p> The <code>fscontext=</code> option works for all filesystems, regardless of their xattr support. The fscontext option sets the overarching filesystem label to a specific security context. This filesystem label is separate from the individual labels on the files. It represents the entire filesystem for certain kinds of permission checks, such as during mount or file creation. Individual file labels are still obtained from the xattrs on the files themselves. The context option actually sets the aggregate context that fscontext provides, in addition to supplying the same label for individual files. </p>
<p> You can set the default security context for unlabeled files using <code>defcontext=</code> option. This overrides the value set for unlabeled files in the policy and requires a filesystem that supports xattr labeling. </p>
<p> The <code>rootcontext=</code> option allows you to explicitly label the root inode of a FS being mounted before that FS or inode becomes visible to userspace. This was found to be useful for things like stateless Linux. </p>
<p> Note that the kernel rejects any remount request that includes the context option, <code>even</code> when unchanged from the current context. </p>
<p> <code>Warning: the</code> <i>context</i> <code>value might contain commas</code>, in which case the value has to be properly quoted, otherwise <code>mount</code> will interpret the comma as a separator between mount options. Don&#8217;t forget that the shell strips off quotes and thus <code>double quoting is required</code>. For example:</dl>
<dl>
<dd>mount -t tmpfs none /mnt -o \ &#8216;context=&quot;system_u:object_r:tmp_t:s0:c127,c456&quot;,noexec&#8217;
</dl>
<p> For more details, see <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8). </p>
<p> <code>defaults</code></p>
<dl>
<dd>Use the default options: <code>rw</code>, <code>suid</code>, <code>dev</code>, <code>exec</code>, <code>auto</code>, <code>nouser</code>, and <code>async</code>. </p>
<p> Note that the real set of all default mount options depends on the kernel and filesystem type. See the beginning of this section for more details.</dl>
<p> <code>dev</code></p>
<dl>
<dd>Interpret character or block special devices on the filesystem.</dl>
<p> <code>nodev</code></p>
<dl>
<dd>Do not interpret character or block special devices on the filesystem.</dl>
<p> <code>diratime</code></p>
<dl>
<dd>Update directory inode access times on this filesystem. This is the default. (This option is ignored when <code>noatime</code> is set.)</dl>
<p> <code>nodiratime</code></p>
<dl>
<dd>Do not update directory inode access times on this filesystem. (This option is implied when <code>noatime</code> is set.)</dl>
<p> <code>dirsync</code></p>
<dl>
<dd>All directory updates within the filesystem should be done synchronously. This affects the following system calls: <code><a href="/docs/linux/man/2-creat/">creat</a></code>(2), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2) and <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2).</dl>
<p> <code>exec</code></p>
<dl>
<dd>Permit execution of binaries.</dl>
<p> <code>noexec</code></p>
<dl>
<dd>Do not permit direct execution of any binaries on the mounted filesystem.</dl>
<p> <code>group</code></p>
<dl>
<dd>Allow an ordinary user to mount the filesystem if one of that user&#8217;s groups matches the group of the device. This option implies the options <code>nosuid</code> and <code>nodev</code> (unless overridden by subsequent options, as in the option line <code>group,dev,suid</code>).</dl>
<p> <code>iversion</code></p>
<dl>
<dd>Every time the inode is modified, the i_version field will be incremented.</dl>
<p> <code>noiversion</code></p>
<dl>
<dd>Do not increment the i_version inode field.</dl>
<p> <code>mand</code></p>
<dl>
<dd>Allow mandatory locks on this filesystem. See <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</dl>
<p> <code>nomand</code></p>
<dl>
<dd>Do not allow mandatory locks on this filesystem.</dl>
<p> <code>_netdev</code></p>
<dl>
<dd>The filesystem resides on a device that requires network access (used to prevent the system from attempting to mount these filesystems until the network has been enabled on the system).</dl>
<p> <code>nofail</code></p>
<dl>
<dd>Do not report errors for this device if it does not exist.</dl>
<p> <code>relatime</code></p>
<dl>
<dd>Update inode access times relative to modify or change time. Access time is only updated if the previous access time was earlier than the current modify or change time. (Similar to <code>noatime</code>, but it doesn&#8217;t break <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1) or other applications that need to know if a file has been read since the last time it was modified.) </p>
<p> Since Linux 2.6.30, the kernel defaults to the behavior provided by this option (unless <code>noatime</code> was specified), and the <code>strictatime</code> option is required to obtain traditional semantics. In addition, since Linux 2.6.30, the file&#8217;s last access time is always updated if it is more than 1 day old.</dl>
<p> <code>norelatime</code></p>
<dl>
<dd>Do not use the <code>relatime</code> feature. See also the <code>strictatime</code> mount option.</dl>
<p> <code>strictatime</code></p>
<dl>
<dd>Allows to explicitly request full atime updates. This makes it possible for the kernel to default to <code>relatime</code> or <code>noatime</code> but still allow userspace to override it. For more details about the default system mount options see <i>/proc/mounts</i>.</dl>
<p> <code>nostrictatime</code></p>
<dl>
<dd>Use the kernel&#8217;s default behavior for inode access time updates.</dl>
<p> <code>lazytime</code></p>
<dl>
<dd>Only update times (atime, mtime, ctime) on the in-memory version of the file inode. </p>
<p> This mount option significantly reduces writes to the inode table for workloads that perform frequent random writes to preallocated files. </p>
<p> The on-disk timestamps are updated only when: </p>
<dl>
<dd>&bull; the inode needs to be updated for some change unrelated to file timestamps</dl>
<dl>
<dd>&bull; the application employs <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-syncfs/">syncfs</a></code>(2), or <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2)</dl>
<dl>
<dd>&bull; an undeleted inode is evicted from memory</dl>
<dl>
<dd>&bull; more than 24 hours have passed since the inode was written to disk.</dl>
</dl>
<p> <code>nolazytime</code></p>
<dl>
<dd>Do not use the lazytime feature.</dl>
<p> <code>suid</code></p>
<dl>
<dd>Honor set-user-ID and set-group-ID bits or file capabilities when executing programs from this filesystem.</dl>
<p> <code>nosuid</code></p>
<dl>
<dd>Do not honor set-user-ID and set-group-ID bits or file capabilities when executing programs from this filesystem. In addition, SELinux domain transitions require permission nosuid_transition, which in turn needs also policy capability nnp_nosuid_transition.</dl>
<p> <code>silent</code></p>
<dl>
<dd>Turn on the silent flag.</dl>
<p> <code>loud</code></p>
<dl>
<dd>Turn off the silent flag.</dl>
<p> <code>owner</code></p>
<dl>
<dd>Allow an ordinary user to mount the filesystem if that user is the owner of the device. This option implies the options <code>nosuid</code> and <code>nodev</code> (unless overridden by subsequent options, as in the option line <code>owner,dev,suid</code>).</dl>
<p> <code>remount</code></p>
<dl>
<dd>Attempt to remount an already-mounted filesystem. This is commonly used to change the mount flags for a filesystem, especially to make a readonly filesystem writable. It does not change device or mount point. </p>
<p> The remount operation together with the <code>bind</code> flag has special semantics. See above, the subsection <code>Bind mounts</code>. </p>
<p> The remount functionality follows the standard way the <code>mount</code> command works with options from <i>fstab</i>. This means that <code>mount</code> does not read <i>fstab</i> (or <i>mtab</i>) only when both <i>device</i> and <i>dir</i> are specified. </p>
<p> <code>mount -o remount,rw /dev/foo /dir</code> </p>
<p> After this call all old mount options are replaced and arbitrary stuff from <i>fstab</i> (or <i>mtab</i>) is ignored, except the loop= option which is internally generated and maintained by the mount command. </p>
<p> <code>mount -o remount,rw /dir</code> </p>
<p> After this call, mount reads <i>fstab</i> and merges these options with the options from the command line (<code>-o</code>). If no mountpoint is found in <i>fstab</i>, then a remount with unspecified source is allowed. </p>
<p> <code>mount</code> allows the use of <code>&#8211;all</code> to remount all already mounted filesystems which match a specified filter (<code>-O</code> and <code>-t</code>). For example: </p>
<p> <code>mount &#8211;all -o remount,ro -t vfat</code> </p>
<p> remounts all already mounted vfat filesystems in read-only mode. Each of the filesystems is remounted by <code>mount -o remount,ro /dir</code> semantic. This means the <code>mount</code> command reads <i>fstab</i> or <i>mtab</i> and merges these options with the options from the command line.</dl>
<p> <code>ro</code></p>
<dl>
<dd>Mount the filesystem read-only.</dl>
<p> <code>rw</code></p>
<dl>
<dd>Mount the filesystem read-write.</dl>
<p> <code>sync</code></p>
<dl>
<dd>All I/O to the filesystem should be done synchronously. In the case of media with a limited number of write cycles (e.g. some flash drives), <code>sync</code> may cause life-cycle shortening.</dl>
<p> <code>user</code></p>
<dl>
<dd>Allow an ordinary user to mount the filesystem. The name of the mounting user is written to the <i>mtab</i> file (or to the private libmount file in <i>/run/mount</i> on systems without a regular <i>mtab</i>) so that this same user can unmount the filesystem again. This option implies the options <code>noexec</code>, <code>nosuid</code>, and <code>nodev</code> (unless overridden by subsequent options, as in the option line <code>user,exec,dev,suid</code>).</dl>
<p> <code>nouser</code></p>
<dl>
<dd>Forbid an ordinary user to mount the filesystem. This is the default; it does not imply any other options.</dl>
<p> <code>users</code></p>
<dl>
<dd>Allow any user to mount and to unmount the filesystem, even when some other ordinary user mounted it. This option implies the options <code>noexec</code>, <code>nosuid</code>, and <code>nodev</code> (unless overridden by subsequent options, as in the option line <code>users,exec,dev,suid</code>).</dl>
<p> <code>X-</code>*</p>
<dl>
<dd>All options prefixed with &quot;X-&quot; are interpreted as comments or as userspace application-specific options. These options are not stored in user space (e.g., <i>mtab</i> file), nor sent to the mount.<i>type</i> helpers nor to the <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) system call. The suggested format is <code>X-</code><i>appname</i>.<i>option</i>.</dl>
<p> <code>x-</code>*</p>
<dl>
<dd>The same as <code>X-</code>* options, but stored permanently in user space. This means the options are also available for <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) or other operations. Note that maintaining mount options in user space is tricky, because it&#8217;s necessary use libmount-based tools and there is no guarantee that the options will be always available (for example after a move mount operation or in unshared namespace). </p>
<p> Note that before util-linux v2.30 the x-* options have not been maintained by libmount and stored in user space (functionality was the same as for X-* now), but due to the growing number of use-cases (in initrd, systemd etc.) the functionality has been extended to keep existing <i>fstab</i> configurations usable without a change.</dl>
<p> <code>X-mount.mkdir</code>[=<i>mode</i>]</p>
<dl>
<dd>Allow to make a target directory (mountpoint) if it does not exit yet. The optional argument <i>mode</i> specifies the filesystem access mode used for <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2) in octal notation. The default mode is 0755. This functionality is supported only for root users or when mount executed without suid permissions. The option is also supported as x-mount.mkdir, this notation is deprecated since v2.30.</dl>
<p> <code>nosymfollow</code></p>
<dl>
<dd>Do not follow symlinks when resolving paths. Symlinks can still be created, and <code><a href="/docs/linux/man/1-readlink/">readlink</a></code>(1), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/1-realpath/">realpath</a></code>(1), and <code><a href="/docs/linux/man/3-realpath/">realpath</a></code>(3) all still work properly.</dl>
<h2>Filesystem-Specific Mount Options</h2>
<p>This section lists options that are specific to particular filesystems. Where possible, you should first consult filesystem-specific manual pages for details. Some of those pages are listed in the following table. </p>
<table BORDER>
<tr VALIGN=top>
<td>
<p> <code>Filesystem(s)</code> </td>
<td>
<p> <code>Manual page</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> btrfs </td>
<td>
<p> <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> cifs </td>
<td>
<p> <code><a href="/docs/linux/man/8-mount-cifs/">mount.cifs</a></code>(8)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ext2, ext3, ext4 </td>
<td>
<p> <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> fuse </td>
<td>
<p> <code><a href="/docs/linux/man/8-fuse/">fuse</a></code>(8)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nfs </td>
<td>
<p> <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> tmpfs </td>
<td>
<p> <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> xfs </td>
<td>
<p> <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5)
</td>
</tr>
</table>
<p> Note that some of the pages listed above might be available only after you install the respective userland tools. </p>
<p> The following options apply only to certain filesystems. We sort them by filesystem. All options follow the <code>-o</code> flag. </p>
<p> What options are supported depends a bit on the running kernel. Further information may be available in filesystem-specific files in the kernel source subdirectory <i>Documentation/filesystems</i>.</p>
<h3>Mount options for adfs</h3>
<p><code>uid=</code><i>value</i> and <code>gid=</code><i>value</i></p>
<dl>
<dd>Set the owner and group of the files in the filesystem (default: uid=gid=0).</dl>
<p> <code>ownmask=</code><i>value</i> and <code>othmask=</code><i>value</i></p>
<dl>
<dd>Set the permission mask for ADFS &#8216;owner&#8217; permissions and &#8216;other&#8217; permissions, respectively (default: 0700 and 0077, respectively). See also <i>/usr/src/linux/Documentation/filesystems/adfs.rst</i>.</dl>
<h3>Mount options for affs</h3>
<p><code>uid=</code><i>value</i> and <code>gid=</code><i>value</i></p>
<dl>
<dd>Set the owner and group of the root of the filesystem (default: uid=gid=0, but with option <code>uid</code> or <code>gid</code> without specified value, the UID and GID of the current process are taken).</dl>
<p> <code>setuid=</code><i>value</i> and <code>setgid=</code><i>value</i></p>
<dl>
<dd>Set the owner and group of all files.</dl>
<p> <code>mode=</code><i>value</i></p>
<dl>
<dd>Set the mode of all files to <i>value</i> &amp; 0777 disregarding the original permissions. Add search permission to directories that have read permission. The value is given in octal.</dl>
<p> <code>protect</code></p>
<dl>
<dd>Do not allow any changes to the protection bits on the filesystem.</dl>
<p> <code>usemp</code></p>
<dl>
<dd>Set UID and GID of the root of the filesystem to the UID and GID of the mount point upon the first sync or umount, and then clear this option. Strange&#8230;</dl>
<p> <code>verbose</code></p>
<dl>
<dd>Print an informational message for each successful mount.</dl>
<p> <code>prefix=</code><i>string</i></p>
<dl>
<dd>Prefix used before volume name, when following a link.</dl>
<p> <code>volume=</code><i>string</i></p>
<dl>
<dd>Prefix (of length at most 30) used before &#8216;/&#8217; when following a symbolic link.</dl>
<p> <code>reserved=</code><i>value</i></p>
<dl>
<dd>(Default: 2.) Number of unused blocks at the start of the device.</dl>
<p> <code>root=</code><i>value</i></p>
<dl>
<dd>Give explicitly the location of the root block.</dl>
<p> <code>bs=</code><i>value</i></p>
<dl>
<dd>Give blocksize. Allowed values are 512, 1024, 2048, 4096.</dl>
<p> <code>grpquota</code>|<code>noquota</code>|<code>quota</code>|<code>usrquota</code></p>
<dl>
<dd>These options are accepted but ignored. (However, quota utilities may react to such strings in <i>/etc/fstab</i>.)</dl>
<h3>Mount options for debugfs</h3>
<p>The debugfs filesystem is a pseudo filesystem, traditionally mounted on <i>/sys/kernel/debug</i>. As of kernel version 3.4, debugfs has the following options: </p>
<p> <code>uid=</code><i>n</i><code>, gid=</code><i>n</i></p>
<dl>
<dd>Set the owner and group of the mountpoint.</dl>
<p> <code>mode=</code><i>value</i></p>
<dl>
<dd>Sets the mode of the mountpoint.</dl>
<h3>Mount options for devpts</h3>
<p>The devpts filesystem is a pseudo filesystem, traditionally mounted on <i>/dev/pts</i>. In order to acquire a pseudo terminal, a process opens <i>/dev/ptmx</i>; the number of the pseudo terminal is then made available to the process and the pseudo terminal slave can be accessed as <i>/dev/pts/</i>&lt;number&gt;. </p>
<p> <code>uid=</code><i>value</i> and <code>gid=</code><i>value</i></p>
<dl>
<dd>This sets the owner or the group of newly created pseudo terminals to the specified values. When nothing is specified, they will be set to the UID and GID of the creating process. For example, if there is a tty group with GID 5, then <code>gid=5</code> will cause newly created pseudo terminals to belong to the tty group.</dl>
<p> <code>mode=</code><i>value</i></p>
<dl>
<dd>Set the mode of newly created pseudo terminals to the specified value. The default is 0600. A value of <code>mode=620</code> and <code>gid=5</code> makes &quot;mesg y&quot; the default on newly created pseudo terminals.</dl>
<p> <code>newinstance</code></p>
<dl>
<dd>Create a private instance of the devpts filesystem, such that indices of pseudo terminals allocated in this new instance are independent of indices created in other instances of devpts. </p>
<p> All mounts of devpts without this <code>newinstance</code> option share the same set of pseudo terminal indices (i.e., legacy mode). Each mount of devpts with the <code>newinstance</code> option has a private set of pseudo terminal indices. </p>
<p> This option is mainly used to support containers in the Linux kernel. It is implemented in Linux kernel versions starting with 2.6.29. Further, this mount option is valid only if <code>CONFIG_DEVPTS_MULTIPLE_INSTANCES</code> is enabled in the kernel configuration. </p>
<p> To use this option effectively, <i>/dev/ptmx</i> must be a symbolic link to <i>pts/ptmx</i>. See <i>Documentation/filesystems/devpts.txt</i> in the Linux kernel source tree for details.</dl>
<p> <code>ptmxmode=</code><i>value</i></p>
<dl>
<dd>Set the mode for the new <i>ptmx</i> device node in the devpts filesystem. </p>
<p> With the support for multiple instances of devpts (see <code>newinstance</code> option above), each instance has a private <i>ptmx</i> node in the root of the devpts filesystem (typically <i>/dev/pts/ptmx</i>). </p>
<p> For compatibility with older versions of the kernel, the default mode of the new <i>ptmx</i> node is 0000. <code>ptmxmode=</code><i>value</i> specifies a more useful mode for the <i>ptmx</i> node and is highly recommended when the <code>newinstance</code> option is specified. </p>
<p> This option is only implemented in Linux kernel versions starting with 2.6.29. Further, this option is valid only if <code>CONFIG_DEVPTS_MULTIPLE_INSTANCES</code> is enabled in the kernel configuration.</dl>
<h3>Mount options for fat</h3>
<p>(Note: <i>fat</i> is not a separate filesystem, but a common part of the <i>msdos</i>, <i>umsdos</i> and <i>vfat</i> filesystems.) </p>
<p> <code>blocksize=</code>{<code>512</code>|<code>1024</code>|<code>2048</code>}</p>
<dl>
<dd>Set blocksize (default 512). This option is obsolete.</dl>
<p> <code>uid=</code><i>value</i> and <code>gid=</code><i>value</i></p>
<dl>
<dd>Set the owner and group of all files. (Default: the UID and GID of the current process.)</dl>
<p> <code>umask=</code><i>value</i></p>
<dl>
<dd>Set the umask (the bitmask of the permissions that are <code>not</code> present). The default is the umask of the current process. The value is given in octal.</dl>
<p> <code>dmask=</code><i>value</i></p>
<dl>
<dd>Set the umask applied to directories only. The default is the umask of the current process. The value is given in octal.</dl>
<p> <code>fmask=</code><i>value</i></p>
<dl>
<dd>Set the umask applied to regular files only. The default is the umask of the current process. The value is given in octal.</dl>
<p> <code>allow_utime=</code><i>value</i></p>
<dl>
<dd>This option controls the permission check of mtime/atime. </p>
<p> <code>20</code></p>
<dl>
<dd>If current process is in group of file&#8217;s group ID, you can change timestamp.</dl>
<p> <code>2</code></p>
<dl>
<dd>Other users can change timestamp.</dl>
</dl>
<p> The default is set from &#8216;dmask&#8217; option. (If the directory is writable, <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2) is also allowed. I.e. ~dmask &amp; 022) </p>
<p> Normally <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2) checks that the current process is owner of the file, or that it has the <code>CAP_FOWNER</code> capability. But FAT filesystems don&#8217;t have UID/GID on disk, so the normal check is too inflexible. With this option you can relax it. </p>
<p> <code>check=</code><i>value</i></p>
<dl>
<dd>Three different levels of pickiness can be chosen: </p>
<p> <code>r</code>[<code>elaxed</code>]</p>
<dl>
<dd>Upper and lower case are accepted and equivalent, long name parts are truncated (e.g. <i>verylongname.foobar</i> becomes <i>verylong.foo</i>), leading and embedded spaces are accepted in each name part (name and extension).</dl>
<p> <code>n</code>[<code>ormal</code>]</p>
<dl>
<dd>Like &quot;relaxed&quot;, but many special characters (*, ?, &lt;, spaces, etc.) are rejected. This is the default.</dl>
<p> <code>s</code>[<code>trict</code>]</p>
<dl>
<dd>Like &quot;normal&quot;, but names that contain long parts or special characters that are sometimes used on Linux but are not accepted by MS-DOS (+, =, etc.) are rejected.</dl>
</dl>
<p> <code>codepage=</code><i>value</i></p>
<dl>
<dd>Sets the codepage for converting to shortname characters on FAT and VFAT filesystems. By default, codepage 437 is used.</dl>
<p> <code>conv=</code><i>mode</i></p>
<dl>
<dd>This option is obsolete and may fail or be ignored.</dl>
<p> <code>cvf_format=</code><i>module</i></p>
<dl>
<dd>Forces the driver to use the CVF (Compressed Volume File) module cvf__module_ instead of auto-detection. If the kernel supports kmod, the cvf_format=xxx option also controls on-demand CVF module loading. This option is obsolete.</dl>
<p> <code>cvf_option=</code><i>option</i></p>
<dl>
<dd>Option passed to the CVF module. This option is obsolete.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Turn on the <i>debug</i> flag. A version string and a list of filesystem parameters will be printed (these data are also printed if the parameters appear to be inconsistent).</dl>
<p> <code>discard</code></p>
<dl>
<dd>If set, causes discard/TRIM commands to be issued to the block device when blocks are freed. This is useful for SSD devices and sparse/thinly-provisioned LUNs.</dl>
<p> <code>dos1xfloppy</code></p>
<dl>
<dd>If set, use a fallback default BIOS Parameter Block configuration, determined by backing device size. These static parameters match defaults assumed by DOS 1.x for 160 kiB, 180 kiB, 320 kiB, and 360 kiB floppies and floppy images.</dl>
<p> <code>errors=</code>{<code>panic</code>|<code>continue</code>|<code>remount-ro</code>}</p>
<dl>
<dd>Specify FAT behavior on critical errors: panic, continue without doing anything, or remount the partition in read-only mode (default behavior).</dl>
<p> <code>fat=</code>{<code>12</code>|<code>16</code>|<code>32</code>}</p>
<dl>
<dd>Specify a 12, 16 or 32 bit fat. This overrides the automatic FAT type detection routine. Use with caution!</dl>
<p> <code>iocharset=</code><i>value</i></p>
<dl>
<dd>Character set to use for converting between 8 bit characters and 16 bit Unicode characters. The default is iso8859-1. Long filenames are stored on disk in Unicode format.</dl>
<p> <code>nfs=</code>{<code>stale_rw</code>|<code>nostale_ro</code>}</p>
<dl>
<dd>Enable this only if you want to export the FAT filesystem over NFS. </p>
<p> <code>stale_rw</code>: This option maintains an index (cache) of directory inodes which is used by the nfs-related code to improve look-ups. Full file operations (read/write) over NFS are supported but with cache eviction at NFS server, this could result in spurious <code>ESTALE</code> errors. </p>
<p> <code>nostale_ro</code>: This option bases the inode number and file handle on the on-disk location of a file in the FAT directory entry. This ensures that <code>ESTALE</code> will not be returned after a file is evicted from the inode cache. However, it means that operations such as rename, create and unlink could cause file handles that previously pointed at one file to point at a different file, potentially causing data corruption. For this reason, this option also mounts the filesystem readonly. </p>
<p> To maintain backward compatibility, <code>-o nfs</code> is also accepted, defaulting to <code>stale_rw</code>.</dl>
<p> <code>tz=UTC</code></p>
<dl>
<dd>This option disables the conversion of timestamps between local time (as used by Windows on FAT) and UTC (which Linux uses internally). This is particularly useful when mounting devices (like digital cameras) that are set to UTC in order to avoid the pitfalls of local time.</dl>
<p> <code>time_offset=</code><i>minutes</i></p>
<dl>
<dd>Set offset for conversion of timestamps from local time used by FAT to UTC. I.e., <i>minutes</i> will be subtracted from each timestamp to convert it to UTC used internally by Linux. This is useful when the time zone set in the kernel via <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2) is not the time zone used by the filesystem. Note that this option still does not provide correct time stamps in all cases in presence of DST &#8211; time stamps in a different DST setting will be off by one hour.</dl>
<p> <code>quiet</code></p>
<dl>
<dd>Turn on the <i>quiet</i> flag. Attempts to chown or chmod files do not return errors, although they fail. Use with caution!</dl>
<p> <code>rodir</code></p>
<dl>
<dd>FAT has the <code>ATTR_RO</code> (read-only) attribute. On Windows, the <code>ATTR_RO</code> of the directory will just be ignored, and is used only by applications as a flag (e.g. it&#8217;s set for the customized folder). </p>
<p> If you want to use <code>ATTR_RO</code> as read-only flag even for the directory, set this option.</dl>
<p> <code>showexec</code></p>
<dl>
<dd>If set, the execute permission bits of the file will be allowed only if the extension part of the name is .EXE, .COM, or .BAT. Not set by default.</dl>
<p> <code>sys_immutable</code></p>
<dl>
<dd>If set, <code>ATTR_SYS</code> attribute on FAT is handled as <code>IMMUTABLE</code> flag on Linux. Not set by default.</dl>
<p> <code>flush</code></p>
<dl>
<dd>If set, the filesystem will try to flush to disk more early than normal. Not set by default.</dl>
<p> <code>usefree</code></p>
<dl>
<dd>Use the &quot;free clusters&quot; value stored on <code>FSINFO</code>. It&#8217;ll be used to determine number of free clusters without scanning disk. But it&#8217;s not used by default, because recent Windows don&#8217;t update it correctly in some case. If you are sure the &quot;free clusters&quot; on <code>FSINFO</code> is correct, by this option you can avoid scanning disk.</dl>
<p> <code>dots</code>, <code>nodots</code>, <code>dotsOK=</code>[<code>yes</code>|<code>no</code>]</p>
<dl>
<dd>Various misguided attempts to force Unix or DOS conventions onto a FAT filesystem.</dl>
<h3>Mount options for hfs</h3>
<p><code>creator=</code><i>cccc</i><code>, type=</code><i>cccc</i></p>
<dl>
<dd>Set the creator/type values as shown by the MacOS finder used for creating new files. Default values: &#8216;????&#8217;.</dl>
<p> <code>uid=</code><i>n</i><code>, gid=</code><i>n</i></p>
<dl>
<dd>Set the owner and group of all files. (Default: the UID and GID of the current process.)</dl>
<p> <code>dir_umask=</code><i>n</i><code>, file_umask=</code><i>n</i><code>, umask=</code><i>n</i></p>
<dl>
<dd>Set the umask used for all directories, all regular files, or all files and directories. Defaults to the umask of the current process.</dl>
<p> <code>session=</code><i>n</i></p>
<dl>
<dd>Select the CDROM session to mount. Defaults to leaving that decision to the CDROM driver. This option will fail with anything but a CDROM as underlying device.</dl>
<p> <code>part=</code><i>n</i></p>
<dl>
<dd>Select partition number n from the device. Only makes sense for CDROMs. Defaults to not parsing the partition table at all.</dl>
<p> <code>quiet</code></p>
<dl>
<dd>Don&#8217;t complain about invalid mount options.</dl>
<h3>Mount options for hpfs</h3>
<p><code>uid=</code><i>value</i> and <code>gid=</code><i>value</i></p>
<dl>
<dd>Set the owner and group of all files. (Default: the UID and GID of the current process.)</dl>
<p> <code>umask=</code><i>value</i></p>
<dl>
<dd>Set the umask (the bitmask of the permissions that are <code>not</code> present). The default is the umask of the current process. The value is given in octal.</dl>
<p> <code>case=</code>{<code>lower</code>|<code>asis</code>}</p>
<dl>
<dd>Convert all files names to lower case, or leave them. (Default: <code>case=lower</code>.)</dl>
<p> <code>conv=</code><i>mode</i></p>
<dl>
<dd>This option is obsolete and may fail or being ignored.</dl>
<p> <code>nocheck</code></p>
<dl>
<dd>Do not abort mounting when certain consistency checks fail.</dl>
<h3>Mount options for iso9660</h3>
<p>ISO 9660 is a standard describing a filesystem structure to be used on CD-ROMs. (This filesystem type is also seen on some DVDs. See also the <i>udf</i> filesystem.) </p>
<p> Normal <i>iso9660</i> filenames appear in an 8.3 format (i.e., DOS-like restrictions on filename length), and in addition all characters are in upper case. Also there is no field for file ownership, protection, number of links, provision for block/character devices, etc. </p>
<p> Rock Ridge is an extension to iso9660 that provides all of these UNIX-like features. Basically there are extensions to each directory record that supply all of the additional information, and when Rock Ridge is in use, the filesystem is indistinguishable from a normal UNIX filesystem (except that it is read-only, of course). </p>
<p> <code>norock</code></p>
<dl>
<dd>Disable the use of Rock Ridge extensions, even if available. Cf. <code>map</code>.</dl>
<p> <code>nojoliet</code></p>
<dl>
<dd>Disable the use of Microsoft Joliet extensions, even if available. Cf. <code>map</code>.</dl>
<p> <code>check=</code>{<code>r</code>[<code>elaxed</code>]|<code>s</code>[<code>trict</code>]}</p>
<dl>
<dd>With <code>check=relaxed</code>, a filename is first converted to lower case before doing the lookup. This is probably only meaningful together with <code>norock</code> and <code>map=normal</code>. (Default: <code>check=strict</code>.)</dl>
<p> <code>uid=</code><i>value</i> and <code>gid=</code><i>value</i></p>
<dl>
<dd>Give all files in the filesystem the indicated user or group id, possibly overriding the information found in the Rock Ridge extensions. (Default: <code>uid=0,gid=0</code>.)</dl>
<p> <code>map=</code>{<code>n</code>[<code>ormal</code>]|<code>o</code>[<code>ff</code>]|<code>a</code>[<code>corn</code>]}</p>
<dl>
<dd>For non-Rock Ridge volumes, normal name translation maps upper to lower case ASCII, drops a trailing &#8216;;1&#8217;, and converts &#8216;;&#8217; to &#8216;.&#8217;. With <code>map=off</code> no name translation is done. See <code>norock</code>. (Default: <code>map=normal</code>.) <code>map=acorn</code> is like <code>map=normal</code> but also apply Acorn extensions if present.</dl>
<p> <code>mode=</code><i>value</i></p>
<dl>
<dd>For non-Rock Ridge volumes, give all files the indicated mode. (Default: read and execute permission for everybody.) Octal mode values require a leading 0.</dl>
<p> <code>unhide</code></p>
<dl>
<dd>Also show hidden and associated files. (If the ordinary files and the associated or hidden files have the same filenames, this may make the ordinary files inaccessible.)</dl>
<p> <code>block=</code>{<code>512</code>|<code>1024</code>|<code>2048</code>}</p>
<dl>
<dd>Set the block size to the indicated value. (Default: <code>block=1024</code>.)</dl>
<p> <code>conv=</code><i>mode</i></p>
<dl>
<dd>This option is obsolete and may fail or being ignored.</dl>
<p> <code>cruft</code></p>
<dl>
<dd>If the high byte of the file length contains other garbage, set this mount option to ignore the high order bits of the file length. This implies that a file cannot be larger than 16 MB.</dl>
<p> <code>session=</code><i>x</i></p>
<dl>
<dd>Select number of session on a multisession CD.</dl>
<p> <code>sbsector=</code><i>xxx</i></p>
<dl>
<dd>Session begins from sector xxx.</dl>
<p> The following options are the same as for vfat and specifying them only makes sense when using discs encoded using Microsoft&#8217;s Joliet extensions. </p>
<p> <code>iocharset=</code><i>value</i></p>
<dl>
<dd>Character set to use for converting 16 bit Unicode characters on CD to 8 bit characters. The default is iso8859-1.</dl>
<p> <code>utf8</code></p>
<dl>
<dd>Convert 16 bit Unicode characters on CD to UTF-8.</dl>
<h3>Mount options for jfs</h3>
<p><code>iocharset=</code><i>name</i></p>
<dl>
<dd>Character set to use for converting from Unicode to ASCII. The default is to do no conversion. Use <code>iocharset=utf8</code> for UTF8 translations. This requires <code>CONFIG_NLS_UTF8</code> to be set in the kernel <i>.config</i> file.</dl>
<p> <code>resize=</code><i>value</i></p>
<dl>
<dd>Resize the volume to <i>value</i> blocks. JFS only supports growing a volume, not shrinking it. This option is only valid during a remount, when the volume is mounted read-write. The <code>resize</code> keyword with no value will grow the volume to the full size of the partition.</dl>
<p> <code>nointegrity</code></p>
<dl>
<dd>Do not write to the journal. The primary use of this option is to allow for higher performance when restoring a volume from backup media. The integrity of the volume is not guaranteed if the system abnormally ends.</dl>
<p> <code>integrity</code></p>
<dl>
<dd>Default. Commit metadata changes to the journal. Use this option to remount a volume where the <code>nointegrity</code> option was previously specified in order to restore normal behavior.</dl>
<p> <code>errors=</code>{<code>continue</code>|<code>remount-ro</code>|<code>panic</code>}</p>
<dl>
<dd>Define the behavior when an error is encountered. (Either ignore errors and just mark the filesystem erroneous and continue, or remount the filesystem read-only, or panic and halt the system.)</dl>
<p> <code>noquota</code>|<code>quota</code>|<code>usrquota</code>|<code>grpquota</code></p>
<dl>
<dd>These options are accepted but ignored.</dl>
<h3>Mount options for msdos</h3>
<p>See mount options for fat. If the <i>msdos</i> filesystem detects an inconsistency, it reports an error and sets the file system read-only. The filesystem can be made writable again by remounting it.</p>
<h3>Mount options for ncpfs</h3>
<p>Just like <i>nfs</i>, the <i>ncpfs</i> implementation expects a binary argument (a <i>struct ncp_mount_data</i>) to the mount system call. This argument is constructed by <code><a href="/docs/linux/man/8-ncpmount/">ncpmount</a></code>(8) and the current version of <code>mount</code> (2.12) does not know anything about ncpfs.</p>
<h3>Mount options for ntfs</h3>
<p><code>iocharset=</code><i>name</i></p>
<dl>
<dd>Character set to use when returning file names. Unlike VFAT, NTFS suppresses names that contain nonconvertible characters. Deprecated.</dl>
<p> <code>nls=</code><i>name</i></p>
<dl>
<dd>New name for the option earlier called <i>iocharset</i>.</dl>
<p> <code>utf8</code></p>
<dl>
<dd>Use UTF-8 for converting file names.</dl>
<p> <code>uni_xlate=</code>{<code>0</code>|<code>1</code>|<code>2</code>}</p>
<dl>
<dd>For 0 (or &#8216;no&#8217; or &#8216;false&#8217;), do not use escape sequences for unknown Unicode characters. For 1 (or &#8216;yes&#8217; or &#8216;true&#8217;) or 2, use vfat-style 4-byte escape sequences starting with &quot;:&quot;. Here 2 gives a little-endian encoding and 1 a byteswapped bigendian encoding.</dl>
<p> <code>posix=[0|1]</code></p>
<dl>
<dd>If enabled (posix=1), the filesystem distinguishes between upper and lower case. The 8.3 alias names are presented as hard links instead of being suppressed. This option is obsolete.</dl>
<p> <code>uid=</code><i>value</i>, <code>gid=</code><i>value</i> and <code>umask=</code><i>value</i></p>
<dl>
<dd>Set the file permission on the filesystem. The umask value is given in octal. By default, the files are owned by root and not readable by somebody else.</dl>
<h3>Mount options for overlay</h3>
<p>Since Linux 3.18 the overlay pseudo filesystem implements a union mount for other filesystems. </p>
<p> An overlay filesystem combines two filesystems &#8211; an <code>upper</code> filesystem and a <code>lower</code> filesystem. When a name exists in both filesystems, the object in the upper filesystem is visible while the object in the lower filesystem is either hidden or, in the case of directories, merged with the upper object. </p>
<p> The lower filesystem can be any filesystem supported by Linux and does not need to be writable. The lower filesystem can even be another overlayfs. The upper filesystem will normally be writable and if it is it must support the creation of trusted.* extended attributes, and must provide a valid d_type in readdir responses, so NFS is not suitable. </p>
<p> A read-only overlay of two read-only filesystems may use any filesystem type. The options <code>lowerdir</code> and <code>upperdir</code> are combined into a merged directory by using:</p>
<dl>
<dd>
<dl>
<dd>
<pre>mount -t overlay overlay \
 -olowerdir=/lower,upperdir=/upper,workdir=/work /merged</pre>
</dl>
</dl>
<p> <code>lowerdir=</code><i>directory</i></p>
<dl>
<dd>Any filesystem, does not need to be on a writable filesystem.</dl>
<p> <code>upperdir=</code><i>directory</i></p>
<dl>
<dd>The upperdir is normally on a writable filesystem.</dl>
<p> <code>workdir=</code><i>directory</i></p>
<dl>
<dd>The workdir needs to be an empty directory on the same filesystem as upperdir.</dl>
<p> <code>userxattr</code></p>
<dl>
<dd>Use the &quot;<code>user.overlay.</code>&quot; xattr namespace instead of &quot;<code>trusted.overlay.</code>&quot;. This is useful for unprivileged mounting of overlayfs.</dl>
<p> <code>redirect_dir=</code>{<code>on</code>|<code>off</code>|<code>follow</code>|<code>nofollow</code>}</p>
<dl>
<dd>If the <i>redirect_dir</i> feature is enabled, then the directory will be copied up (but not the contents). Then the &quot;{<code>trusted</code>|<code>user</code>}.overlay.redirect&quot; extended attribute is set to the path of the original location from the root of the overlay. Finally the directory is moved to the new location. </p>
<p> <code>on</code></p>
<dl>
<dd>Redirects are enabled.</dl>
<p> <code>off</code></p>
<dl>
<dd>Redirects are not created and only followed if &quot;redirect_always_follow&quot; feature is enabled in the kernel/module config.</dl>
<p> <code>follow</code></p>
<dl>
<dd>Redirects are not created, but followed.</dl>
<p> <code>nofollow</code></p>
<dl>
<dd>Redirects are not created and not followed (equivalent to &quot;redirect_dir=off&quot; if &quot;redirect_always_follow&quot; feature is not enabled).</dl>
</dl>
<p> <code>index=</code>{<code>on</code>|<code>off</code>}</p>
<dl>
<dd>Inode index. If this feature is disabled and a file with multiple hard links is copied up, then this will &quot;break&quot; the link. Changes will not be propagated to other names referring to the same inode.</dl>
<p> <code>uuid=</code>{<code>on</code>|<code>off</code>}</p>
<dl>
<dd>Can be used to replace UUID of the underlying filesystem in file handles with null, and effectively disable UUID checks. This can be useful in case the underlying disk is copied and the UUID of this copy is changed. This is only applicable if all lower/upper/work directories are on the same filesystem, otherwise it will fallback to normal behaviour.</dl>
<p> <code>nfs_export=</code>{<code>on</code>|<code>off</code>}</p>
<dl>
<dd>When the underlying filesystems supports NFS export and the &quot;nfs_export&quot; feature is enabled, an overlay filesystem may be exported to NFS. </p>
<p> With the “nfs_export” feature, on copy_up of any lower object, an index entry is created under the index directory. The index entry name is the hexadecimal representation of the copy up origin file handle. For a non-directory object, the index entry is a hard link to the upper inode. For a directory object, the index entry has an extended attribute &quot;{<code>trusted</code>|<code>user</code>}.overlay.upper&quot; with an encoded file handle of the upper directory inode. </p>
<p> When encoding a file handle from an overlay filesystem object, the following rules apply</p>
<dl>
<dd>
<dl>
<dd>&bull; For a non-upper object, encode a lower file handle from lower inode</dl>
<dl>
<dd>&bull; For an indexed object, encode a lower file handle from copy_up origin</dl>
<dl>
<dd>&bull; For a pure-upper object and for an existing non-indexed upper object, encode an upper file handle from upper inode</dl>
</dl>
<p> The encoded overlay file handle includes</p>
<dl>
<dd>
<dl>
<dd>&bull; Header including path type information (e.g. lower/upper)</dl>
<dl>
<dd>&bull; UUID of the underlying filesystem</dl>
<dl>
<dd>&bull; Underlying filesystem encoding of underlying inode</dl>
</dl>
<p> This encoding format is identical to the encoding format file handles that are stored in extended attribute &quot;{<code>trusted</code>|<code>user</code>}.overlay.origin&quot;. When decoding an overlay file handle, the following steps are followed</p>
<dl>
<dd>
<dl>
<dd>&bull; Find underlying layer by UUID and path type information.</dl>
<dl>
<dd>&bull; Decode the underlying filesystem file handle to underlying dentry.</dl>
<dl>
<dd>&bull; For a lower file handle, lookup the handle in index directory by name.</dl>
<dl>
<dd>&bull; If a whiteout is found in index, return ESTALE. This represents an overlay object that was deleted after its file handle was encoded.</dl>
<dl>
<dd>&bull; For a non-directory, instantiate a disconnected overlay dentry from the decoded underlying dentry, the path type and index inode, if found.</dl>
<dl>
<dd>&bull; For a directory, use the connected underlying decoded dentry, path type and index, to lookup a connected overlay dentry.</dl>
</dl>
<p> Decoding a non-directory file handle may return a disconnected dentry. copy_up of that disconnected dentry will create an upper index entry with no upper alias. </p>
<p> When overlay filesystem has multiple lower layers, a middle layer directory may have a &quot;redirect&quot; to lower directory. Because middle layer &quot;redirects&quot; are not indexed, a lower file handle that was encoded from the &quot;redirect&quot; origin directory, cannot be used to find the middle or upper layer directory. Similarly, a lower file handle that was encoded from a descendant of the &quot;redirect&quot; origin directory, cannot be used to reconstruct a connected overlay path. To mitigate the cases of directories that cannot be decoded from a lower file handle, these directories are copied up on encode and encoded as an upper file handle. On an overlay filesystem with no upper layer this mitigation cannot be used NFS export in this setup requires turning off redirect follow (e.g. &quot;<i>redirect_dir=nofollow</i>&quot;). </p>
<p> The overlay filesystem does not support non-directory connectable file handles, so exporting with the <i>subtree_check</i> exportfs configuration will cause failures to lookup files over NFS. </p>
<p> When the NFS export feature is enabled, all directory index entries are verified on mount time to check that upper file handles are not stale. This verification may cause significant overhead in some cases. </p>
<p> Note: the mount options <i>index=off,nfs_export=on</i> are conflicting for a read-write mount and will result in an error.</dl>
<p> <code>xinfo=</code>{<code>on</code>|<code>off</code>|<code>auto</code>}</p>
<dl>
<dd>The &quot;xino&quot; feature composes a unique object identifier from the real object st_ino and an underlying fsid index. The &quot;xino&quot; feature uses the high inode number bits for fsid, because the underlying filesystems rarely use the high inode number bits. In case the underlying inode number does overflow into the high xino bits, overlay filesystem will fall back to the non xino behavior for that inode. </p>
<p> For a detailed description of the effect of this option please refer to <i></i> &lt;<a rel="nofollow" href="https://www.kernel.org/doc/html/latest/filesystems/overlayfs.html?highlight=overlayfs">https://www.kernel.org/doc/html/latest/filesystems/overlayfs.html?highlight=overlayfs</a>&gt;</dl>
<p> <code>metacopy=</code>{<code>on</code>|<code>off</code>}</p>
<dl>
<dd>When metadata only copy up feature is enabled, overlayfs will only copy up metadata (as opposed to whole file), when a metadata specific operation like chown/chmod is performed. Full file will be copied up later when file is opened for WRITE operation. </p>
<p> In other words, this is delayed data copy up operation and data is copied up when there is a need to actually modify data.</dl>
<p> <code>volatile</code></p>
<dl>
<dd>Volatile mounts are not guaranteed to survive a crash. It is strongly recommended that volatile mounts are only used if data written to the overlay can be recreated without significant effort. </p>
<p> The advantage of mounting with the &quot;volatile&quot; option is that all forms of sync calls to the upper filesystem are omitted. </p>
<p> In order to avoid a giving a false sense of safety, the syncfs (and fsync) semantics of volatile mounts are slightly different than that of the rest of VFS. If any writeback error occurs on the upperdir’s filesystem after a volatile mount takes place, all sync functions will return an error. Once this condition is reached, the filesystem will not recover, and every subsequent sync call will return an error, even if the upperdir has not experience a new error since the last sync call. </p>
<p> When overlay is mounted with &quot;volatile&quot; option, the directory &quot;$workdir/work/incompat/volatile&quot; is created. During next mount, overlay checks for this directory and refuses to mount if present. This is a strong indicator that user should throw away upper and work directories and create fresh one. In very limited cases where the user knows that the system has not crashed and contents of upperdir are intact, The &quot;volatile&quot; directory can be removed.</dl>
<h3>Mount options for reiserfs</h3>
<p>Reiserfs is a journaling filesystem. </p>
<p> <code>conv</code></p>
<dl>
<dd>Instructs version 3.6 reiserfs software to mount a version 3.5 filesystem, using the 3.6 format for newly created objects. This filesystem will no longer be compatible with reiserfs 3.5 tools.</dl>
<p> <code>hash=</code>{<code>rupasov</code>|<code>tea</code>|<code>r5</code>|<code>detect</code>}</p>
<dl>
<dd>Choose which hash function reiserfs will use to find files within directories. </p>
<p> <code>rupasov</code></p>
<dl>
<dd>A hash invented by Yury Yu. Rupasov. It is fast and preserves locality, mapping lexicographically close file names to close hash values. This option should not be used, as it causes a high probability of hash collisions.</dl>
<p> <code>tea</code></p>
<dl>
<dd>A Davis-Meyer function implemented by Jeremy Fitzhardinge. It uses hash permuting bits in the name. It gets high randomness and, therefore, low probability of hash collisions at some CPU cost. This may be used if <code>EHASHCOLLISION</code> errors are experienced with the r5 hash.</dl>
<p> <code>r5</code></p>
<dl>
<dd>A modified version of the rupasov hash. It is used by default and is the best choice unless the filesystem has huge directories and unusual file-name patterns.</dl>
<p> <code>detect</code></p>
<dl>
<dd>Instructs <code>mount</code> to detect which hash function is in use by examining the filesystem being mounted, and to write this information into the reiserfs superblock. This is only useful on the first mount of an old format filesystem.</dl>
</dl>
<p> <code>hashed_relocation</code></p>
<dl>
<dd>Tunes the block allocator. This may provide performance improvements in some situations.</dl>
<p> <code>no_unhashed_relocation</code></p>
<dl>
<dd>Tunes the block allocator. This may provide performance improvements in some situations.</dl>
<p> <code>noborder</code></p>
<dl>
<dd>Disable the border allocator algorithm invented by Yury Yu. Rupasov. This may provide performance improvements in some situations.</dl>
<p> <code>nolog</code></p>
<dl>
<dd>Disable journaling. This will provide slight performance improvements in some situations at the cost of losing reiserfs&#8217;s fast recovery from crashes. Even with this option turned on, reiserfs still performs all journaling operations, save for actual writes into its journaling area. Implementation of <i>nolog</i> is a work in progress.</dl>
<p> <code>notail</code></p>
<dl>
<dd>By default, reiserfs stores small files and &#8216;file tails&#8217; directly into its tree. This confuses some utilities such as <code><a href="/docs/linux/man/8-lilo/">lilo</a></code>(8). This option is used to disable packing of files into the tree.</dl>
<p> <code>replayonly</code></p>
<dl>
<dd>Replay the transactions which are in the journal, but do not actually mount the filesystem. Mainly used by <i>reiserfsck</i>.</dl>
<p> <code>resize=</code><i>number</i></p>
<dl>
<dd>A remount option which permits online expansion of reiserfs partitions. Instructs reiserfs to assume that the device has <i>number</i> blocks. This option is designed for use with devices which are under logical volume management (LVM). There is a special <i>resizer</i> utility which can be obtained from <i> <i></i> &lt;<a href="ftp://ftp.namesys.com/pub/reiserfsprogs">ftp://ftp.namesys.com/pub/reiserfsprogs</a>&gt;</i>.</dl>
<p> <code>user_xattr</code></p>
<dl>
<dd>Enable Extended User Attributes. See the <code><a href="/docs/linux/man/1-attr/">attr</a></code>(1) manual page.</dl>
<p> <code>acl</code></p>
<dl>
<dd>Enable POSIX Access Control Lists. See the <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5) manual page.</dl>
<p> <code>barrier=none</code> / <code>barrier=flush</code></p>
<dl>
<dd>This disables / enables the use of write barriers in the journaling code. <code>barrier=none</code> disables, <code>barrier=flush</code> enables (default). This also requires an IO stack which can support barriers, and if reiserfs gets an error on a barrier write, it will disable barriers again with a warning. Write barriers enforce proper on-disk ordering of journal commits, making volatile disk write caches safe to use, at some performance penalty. If your disks are battery-backed in one way or another, disabling barriers may safely improve performance.</dl>
<h3>Mount options for ubifs</h3>
<p>UBIFS is a flash filesystem which works on top of UBI volumes. Note that <code>atime</code> is not supported and is always turned off. </p>
<p> The device name may be specified as</p>
<dl>
<dd><code>ubiX_Y</code></p>
<dl>
<dd>UBI device number <code>X</code>, volume number <code>Y</code></dl>
<p> <code>ubiY</code></p>
<dl>
<dd>UBI device number <code>0</code>, volume number <code>Y</code></dl>
<p> <code>ubiX:NAME</code></p>
<dl>
<dd>UBI device number <code>X</code>, volume with name <code>NAME</code></dl>
<p> <code>ubi:NAME</code></p>
<dl>
<dd>UBI device number <code>0</code>, volume with name <code>NAME</code></dl>
</dl>
<p> Alternative <code>!</code> separator may be used instead of <code>:</code>. </p>
<p> The following mount options are available: </p>
<p> <code>bulk_read</code></p>
<dl>
<dd>Enable bulk-read. VFS read-ahead is disabled because it slows down the filesystem. Bulk-Read is an internal optimization. Some flashes may read faster if the data are read at one go, rather than at several read requests. For example, OneNAND can do &quot;read-while-load&quot; if it reads more than one NAND page.</dl>
<p> <code>no_bulk_read</code></p>
<dl>
<dd>Do not bulk-read. This is the default.</dl>
<p> <code>chk_data_crc</code></p>
<dl>
<dd>Check data CRC-32 checksums. This is the default.</dl>
<p> <code>no_chk_data_crc</code></p>
<dl>
<dd>Do not check data CRC-32 checksums. With this option, the filesystem does not check CRC-32 checksum for data, but it does check it for the internal indexing information. This option only affects reading, not writing. CRC-32 is always calculated when writing the data.</dl>
<p> <code>compr=</code>{<code>none</code>|<code>lzo</code>|<code>zlib</code>}</p>
<dl>
<dd>Select the default compressor which is used when new files are written. It is still possible to read compressed files if mounted with the <code>none</code> option.</dl>
<h3>Mount options for udf</h3>
<p>UDF is the &quot;Universal Disk Format&quot; filesystem defined by OSTA, the Optical Storage Technology Association, and is often used for DVD-ROM, frequently in the form of a hybrid UDF/ISO-9660 filesystem. It is, however, perfectly usable by itself on disk drives, flash drives and other block devices. See also <i>iso9660</i>. </p>
<p> <code>uid=</code></p>
<dl>
<dd>Make all files in the filesystem belong to the given user. uid=forget can be specified independently of (or usually in addition to) uid=&lt;user&gt; and results in UDF not storing uids to the media. In fact the recorded uid is the 32-bit overflow uid -1 as defined by the UDF standard. The value is given as either &lt;user&gt; which is a valid user name or the corresponding decimal user id, or the special string &quot;forget&quot;.</dl>
<p> <code>gid=</code></p>
<dl>
<dd>Make all files in the filesystem belong to the given group. gid=forget can be specified independently of (or usually in addition to) gid=&lt;group&gt; and results in UDF not storing gids to the media. In fact the recorded gid is the 32-bit overflow gid -1 as defined by the UDF standard. The value is given as either &lt;group&gt; which is a valid group name or the corresponding decimal group id, or the special string &quot;forget&quot;.</dl>
<p> <code>umask=</code></p>
<dl>
<dd>Mask out the given permissions from all inodes read from the filesystem. The value is given in octal.</dl>
<p> <code>mode=</code></p>
<dl>
<dd>If <code>mode=</code> is set the permissions of all non-directory inodes read from the filesystem will be set to the given mode. The value is given in octal.</dl>
<p> <code>dmode=</code></p>
<dl>
<dd>If <code>dmode=</code> is set the permissions of all directory inodes read from the filesystem will be set to the given dmode. The value is given in octal.</dl>
<p> <code>bs=</code></p>
<dl>
<dd>Set the block size. Default value prior to kernel version 2.6.30 was 2048. Since 2.6.30 and prior to 4.11 it was logical device block size with fallback to 2048. Since 4.11 it is logical block size with fallback to any valid block size between logical device block size and 4096. </p>
<p> For other details see the <code><a href="/docs/linux/man/8-mkudffs/">mkudffs</a></code>(8) 2.0+ manpage, sections <code>COMPATIBILITY</code> and <code>BLOCK SIZE</code>.</dl>
<p> <code>unhide</code></p>
<dl>
<dd>Show otherwise hidden files.</dl>
<p> <code>undelete</code></p>
<dl>
<dd>Show deleted files in lists.</dl>
<p> <code>adinicb</code></p>
<dl>
<dd>Embed data in the inode. (default)</dl>
<p> <code>noadinicb</code></p>
<dl>
<dd>Don&#8217;t embed data in the inode.</dl>
<p> <code>shortad</code></p>
<dl>
<dd>Use short UDF address descriptors.</dl>
<p> <code>longad</code></p>
<dl>
<dd>Use long UDF address descriptors. (default)</dl>
<p> <code>nostrict</code></p>
<dl>
<dd>Unset strict conformance.</dl>
<p> <code>iocharset=</code></p>
<dl>
<dd>Set the NLS character set. This requires kernel compiled with <code>CONFIG_UDF_NLS</code> option.</dl>
<p> <code>utf8</code></p>
<dl>
<dd>Set the UTF-8 character set.</dl>
<h3>Mount options for debugging and disaster recovery</h3>
<p><code>novrs</code></p>
<dl>
<dd>Ignore the Volume Recognition Sequence and attempt to mount anyway.</dl>
<p> <code>session=</code></p>
<dl>
<dd>Select the session number for multi-session recorded optical media. (default= last session)</dl>
<p> <code>anchor=</code></p>
<dl>
<dd>Override standard anchor location. (default= 256)</dl>
<p> <code>lastblock=</code></p>
<dl>
<dd>Set the last block of the filesystem.</dl>
<h3>Unused historical mount options that may be encountered and should be removed</h3>
<p><code>uid=ignore</code></p>
<dl>
<dd>Ignored, use uid=&lt;user&gt; instead.</dl>
<p> <code>gid=ignore</code></p>
<dl>
<dd>Ignored, use gid=&lt;group&gt; instead.</dl>
<p> <code>volume=</code></p>
<dl>
<dd>Unimplemented and ignored.</dl>
<p> <code>partition=</code></p>
<dl>
<dd>Unimplemented and ignored.</dl>
<p> <code>fileset=</code></p>
<dl>
<dd>Unimplemented and ignored.</dl>
<p> <code>rootdir=</code></p>
<dl>
<dd>Unimplemented and ignored.</dl>
<h3>Mount options for ufs</h3>
<p><code>ufstype=</code><i>value</i></p>
<dl>
<dd>UFS is a filesystem widely used in different operating systems. The problem are differences among implementations. Features of some implementations are undocumented, so its hard to recognize the type of ufs automatically. That&#8217;s why the user must specify the type of ufs by mount option. Possible values are: </p>
<p> <code>old</code></p>
<dl>
<dd>Old format of ufs, this is the default, read only. (Don&#8217;t forget to give the <code>-r</code> option.)</dl>
<p> <code>44bsd</code></p>
<dl>
<dd>For filesystems created by a BSD-like system (NetBSD, FreeBSD, OpenBSD).</dl>
<p> <code>ufs2</code></p>
<dl>
<dd>Used in FreeBSD 5.x supported as read-write.</dl>
<p> <code>5xbsd</code></p>
<dl>
<dd>Synonym for ufs2.</dl>
<p> <code>sun</code></p>
<dl>
<dd>For filesystems created by SunOS or Solaris on Sparc.</dl>
<p> <code>sunx86</code></p>
<dl>
<dd>For filesystems created by Solaris on x86.</dl>
<p> <code>hp</code></p>
<dl>
<dd>For filesystems created by HP-UX, read-only.</dl>
<p> <code>nextstep</code></p>
<dl>
<dd>For filesystems created by NeXTStep (on NeXT station) (currently read only).</dl>
<p> <code>nextstep-cd</code></p>
<dl>
<dd>For NextStep CDROMs (block_size == 2048), read-only.</dl>
<p> <code>openstep</code></p>
<dl>
<dd>For filesystems created by OpenStep (currently read only). The same filesystem type is also used by Mac OS X.</dl>
</dl>
<p> <code>onerror=</code><i>value</i></p>
<dl>
<dd>Set behavior on error: </p>
<p> <code>panic</code></p>
<dl>
<dd>If an error is encountered, cause a kernel panic.</dl>
<p> [<code>lock</code>|<code>umount</code>|<code>repair</code>]</p>
<dl>
<dd>These mount options don&#8217;t do anything at present; when an error is encountered only a console message is printed.</dl>
</dl>
<h3>Mount options for umsdos</h3>
<p>See mount options for msdos. The <code>dotsOK</code> option is explicitly killed by <i>umsdos</i>.</p>
<h3>Mount options for vfat</h3>
<p>First of all, the mount options for <i>fat</i> are recognized. The <code>dotsOK</code> option is explicitly killed by <i>vfat</i>. Furthermore, there are </p>
<p> <code>uni_xlate</code></p>
<dl>
<dd>Translate unhandled Unicode characters to special escaped sequences. This lets you backup and restore filenames that are created with any Unicode characters. Without this option, a &#8216;?&#8217; is used when no translation is possible. The escape character is &#8216;:&#8217; because it is otherwise invalid on the vfat filesystem. The escape sequence that gets used, where u is the Unicode character, is: &#8216;:&#8217;, (u &amp; 0x3f), ((u&gt;&gt;6) &amp; 0x3f), (u&gt;&gt;12).</dl>
<p> <code>posix</code></p>
<dl>
<dd>Allow two files with names that only differ in case. This option is obsolete.</dl>
<p> <code>nonumtail</code></p>
<dl>
<dd>First try to make a short name without sequence number, before trying <i>name~num.ext</i>.</dl>
<p> <code>utf8</code></p>
<dl>
<dd>UTF8 is the filesystem safe 8-bit encoding of Unicode that is used by the console. It can be enabled for the filesystem with this option or disabled with utf8=0, utf8=no or utf8=false. If <i>uni_xlate</i> gets set, UTF8 gets disabled.</dl>
<p> <code>shortname=</code><i>mode</i></p>
<dl>
<dd>Defines the behavior for creation and display of filenames which fit into 8.3 characters. If a long name for a file exists, it will always be the preferred one for display. There are four <i>mode</i>s: </p>
<p> <code>lower</code></p>
<dl>
<dd>Force the short name to lower case upon display; store a long name when the short name is not all upper case.</dl>
<p> <code>win95</code></p>
<dl>
<dd>Force the short name to upper case upon display; store a long name when the short name is not all upper case.</dl>
<p> <code>winnt</code></p>
<dl>
<dd>Display the short name as is; store a long name when the short name is not all lower case or all upper case.</dl>
<p> <code>mixed</code></p>
<dl>
<dd>Display the short name as is; store a long name when the short name is not all upper case. This mode is the default since Linux 2.6.32.</dl>
</dl>
<h3>Mount options for usbfs</h3>
<p><code>devuid=</code><i>uid</i> and <code>devgid=</code><i>gid</i> and <code>devmode=</code><i>mode</i></p>
<dl>
<dd>Set the owner and group and mode of the device files in the usbfs filesystem (default: uid=gid=0, mode=0644). The mode is given in octal.</dl>
<p> <code>busuid=</code><i>uid</i> and <code>busgid=</code><i>gid</i> and <code>busmode=</code><i>mode</i></p>
<dl>
<dd>Set the owner and group and mode of the bus directories in the usbfs filesystem (default: uid=gid=0, mode=0555). The mode is given in octal.</dl>
<p> <code>listuid=</code><i>uid</i> and <code>listgid=</code><i>gid</i> and <code>listmode=</code><i>mode</i></p>
<dl>
<dd>Set the owner and group and mode of the file <i>devices</i> (default: uid=gid=0, mode=0444). The mode is given in octal.</dl>
<h2>Dm-Verity Support (Experimental)</h2>
<p>The device-mapper verity target provides read-only transparent integrity checking of block devices using kernel crypto API. The <code>mount</code> command can open the dm-verity device and do the integrity verification before on the device filesystem is mounted. Requires libcryptsetup with in libmount (optionally via <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3)). If libcryptsetup supports extracting the root hash of an already mounted device, existing devices will be automatically reused in case of a match. Mount options for dm-verity: </p>
<p> <code>verity.hashdevice=</code><i>path</i></p>
<dl>
<dd>Path to the hash tree device associated with the source volume to pass to dm-verity.</dl>
<p> <code>verity.roothash=</code><i>hex</i></p>
<dl>
<dd>Hex-encoded hash of the root of <i>verity.hashdevice</i>. Mutually exclusive with <i>verity.roothashfile.</i></dl>
<p> <code>verity.roothashfile=</code><i>path</i></p>
<dl>
<dd>Path to file containing the hex-encoded hash of the root of <i>verity.hashdevice.</i> Mutually exclusive with <i>verity.roothash.</i></dl>
<p> <code>verity.hashoffset=</code><i>offset</i></p>
<dl>
<dd>If the hash tree device is embedded in the source volume, <i>offset</i> (default: 0) is used by dm-verity to get to the tree.</dl>
<p> <code>verity.fecdevice=</code><i>path</i></p>
<dl>
<dd>Path to the Forward Error Correction (FEC) device associated with the source volume to pass to dm-verity. Optional. Requires kernel built with <code>CONFIG_DM_VERITY_FEC</code>.</dl>
<p> <code>verity.fecoffset=</code><i>offset</i></p>
<dl>
<dd>If the FEC device is embedded in the source volume, <i>offset</i> (default: 0) is used by dm-verity to get to the FEC area. Optional.</dl>
<p> <code>verity.fecroots=</code><i>value</i></p>
<dl>
<dd>Parity bytes for FEC (default: 2). Optional.</dl>
<p> <code>verity.roothashsig=</code><i>path</i></p>
<dl>
<dd>Path to <code>pkcs7</code>(1ssl) signature of root hash hex string. Requires crypt_activate_by_signed_key() from cryptsetup and kernel built with <code>CONFIG_DM_VERITY_VERIFY_ROOTHASH_SIG</code>. For device reuse, signatures have to be either used by all mounts of a device or by none. Optional.</dl>
<p> Supported since util-linux v2.35. </p>
<p> For example commands: </p>
<dl>
<dd>
<pre>mksquashfs /etc /tmp/etc.squashfs
dd if=/dev/zero of=/tmp/etc.hash bs=1M count=10
veritysetup format /tmp/etc.squashfs /tmp/etc.hash
openssl smime -sign -in &lt;hash&gt; -nocerts -inkey private.key \
-signer private.crt -noattr -binary -outform der -out /tmp/etc.roothash.p7s
mount -o verity.hashdevice=/tmp/etc.hash,verity.roothash=&lt;hash&gt;,\
verity.roothashsig=/tmp/etc.roothash.p7s /tmp/etc.squashfs /mnt</pre>
</dl>
<p> create squashfs image from <i>/etc</i> directory, verity hash device and mount verified filesystem image to <i>/mnt</i>. The kernel will verify that the root hash is signed by a key from the kernel keyring if roothashsig is used.</p>
<h2>Loop-Device Support</h2>
<p>One further possible type is a mount via the loop device. For example, the command</p>
<dl>
<dd><code>mount /tmp/disk.img /mnt -t vfat -o loop=/dev/loop3</code>
</dl>
<p> will set up the loop device <i>/dev/loop3</i> to correspond to the file <i>/tmp/disk.img</i>, and then mount this device on <i>/mnt</i>. </p>
<p> If no explicit loop device is mentioned (but just an option &#8216;<code>-o loop</code>&#8216; is given), then <code>mount</code> will try to find some unused loop device and use that, for example</p>
<dl>
<dd><code>mount /tmp/disk.img /mnt -o loop</code>
</dl>
<p> The <code>mount</code> command <code>automatically</code> creates a loop device from a regular file if a filesystem type is not specified or the filesystem is known for libblkid, for example:</p>
<dl>
<dd><code>mount /tmp/disk.img /mnt</code> </p>
<p> <code>mount -t ext4 /tmp/disk.img /mnt</code>
</dl>
<p> This type of mount knows about three options, namely <code>loop</code>, <code>offset</code> and <code>sizelimit</code>, that are really options to <code><a href="/docs/linux/man/8-losetup/">losetup</a></code>(8). (These options can be used in addition to those specific to the filesystem type.) </p>
<p> Since Linux 2.6.25 auto-destruction of loop devices is supported, meaning that any loop device allocated by <code>mount</code> will be freed by <code>umount</code> independently of <i>/etc/mtab</i>. </p>
<p> You can also free a loop device by hand, using <code>losetup -d</code> or <code>umount -d</code>. </p>
<p> Since util-linux v2.29, <code>mount</code> re-uses the loop device rather than initializing a new device if the same backing file is already used for some loop device with the same offset and sizelimit. This is necessary to avoid a filesystem corruption.</p>
<h2>Exit Status</h2>
<p><code>mount</code> has the following exit status values (the bits can be ORed): </p>
<p> <code>0</code></p>
<dl>
<dd>success</dl>
<p> <code>1</code></p>
<dl>
<dd>incorrect invocation or permissions</dl>
<p> <code>2</code></p>
<dl>
<dd>system error (out of memory, cannot fork, no more loop devices)</dl>
<p> <code>4</code></p>
<dl>
<dd>internal <code>mount</code> bug</dl>
<p> <code>8</code></p>
<dl>
<dd>user interrupt</dl>
<p> <code>16</code></p>
<dl>
<dd>problems writing or locking <i>/etc/mtab</i></dl>
<p> <code>32</code></p>
<dl>
<dd>mount failure</dl>
<p> <code>64</code></p>
<dl>
<dd>some mount succeeded </p>
<p> The command <code>mount -a</code> returns 0 (all succeeded), 32 (all failed), or 64 (some failed, some succeeded).</dl>
<h2>External Helpers</h2>
<p>The syntax of external mount helpers is: </p>
<p> <code>/sbin/mount.</code><i>suffix</i> <i>spec dir</i> [<code>-sfnv</code>] [<code>-N</code> <i>namespace</i>] [<code>-o</code> <i>options</i>] [<code>-t</code> <i>type</i><code>.</code><i>subtype</i>] </p>
<p> where the <i>suffix</i> is the filesystem type and the <code>-sfnvoN</code> options have the same meaning as the normal mount options. The <code>-t</code> option is used for filesystems with subtypes support (for example <code>/sbin/mount.fuse -t fuse.sshfs</code>). </p>
<p> The command <code>mount</code> does not pass the mount options <code>unbindable</code>, <code>runbindable</code>, <code>private</code>, <code>rprivate</code>, <code>slave</code>, <code>rslave</code>, <code>shared</code>, <code>rshared</code>, <code>auto</code>, <code>noauto</code>, <code>comment</code>, <code>x-</code>*, <code>loop</code>, <code>offset</code> and <code>sizelimit</code> to the mount.&lt;suffix&gt; helpers. All other options are used in a comma-separated list as an argument to the <code>-o</code> option.</p>
<h2>Environment</h2>
<p>LIBMOUNT_FSTAB=&lt;path&gt;</p>
<dl>
<dd>overrides the default location of the <i>fstab</i> file (ignored for suid)</dl>
<p> LIBMOUNT_MTAB=&lt;path&gt;</p>
<dl>
<dd>overrides the default location of the <i>mtab</i> file (ignored for suid)</dl>
<p> LIBMOUNT_DEBUG=all</p>
<dl>
<dd>enables libmount debug output</dl>
<p> LIBBLKID_DEBUG=all</p>
<dl>
<dd>enables libblkid debug output</dl>
<p> LOOPDEV_DEBUG=all</p>
<dl>
<dd>enables loop device setup debug output</dl>
<h2>Files</h2>
<p>See also &quot;<code>The files /etc/fstab, /etc/mtab and /proc/mounts</code>&quot; section above. </p>
<p> <i>/etc/fstab</i></p>
<dl>
<dd>filesystem table</dl>
<p> <i>/run/mount</i></p>
<dl>
<dd>libmount private runtime directory</dl>
<p> <i>/etc/mtab</i></p>
<dl>
<dd>table of mounted filesystems or symlink to <i>/proc/mounts</i></dl>
<p> <i>/etc/mtab~</i></p>
<dl>
<dd>lock file (unused on systems with <i>mtab</i> symlink)</dl>
<p> <i>/etc/mtab.tmp</i></p>
<dl>
<dd>temporary file (unused on systems with <i>mtab</i> symlink)</dl>
<p> <i>/etc/filesystems</i></p>
<dl>
<dd>a list of filesystem types to try</dl>
<h2>History</h2>
<p>A <code>mount</code> command existed in Version 5 AT&amp;T UNIX.</p>
<h2>Bugs</h2>
<p>It is possible for a corrupted filesystem to cause a crash. </p>
<p> Some Linux filesystems don&#8217;t support <code>-o sync</code> and <code>-o dirsync</code> (the ext2, ext3, ext4, fat and vfat filesystems <i>do</i> support synchronous updates (a la BSD) when mounted with the <code>sync</code> option). </p>
<p> The <code>-o remount</code> may not be able to change mount parameters (all <i>ext2fs</i>-specific parameters, except <code>sb</code>, are changeable with a remount, for example, but you can&#8217;t change <code>gid</code> or <code>umask</code> for the <i>fatfs</i>). </p>
<p> It is possible that the files <i>/etc/mtab</i> and <i>/proc/mounts</i> don&#8217;t match on systems with a regular <i>mtab</i> file. The first file is based only on the <code>mount</code> command options, but the content of the second file also depends on the kernel and others settings (e.g. on a remote NFS server &#8212; in certain cases the <code>mount</code> command may report unreliable information about an NFS mount point and the <i>/proc/mount</i> file usually contains more reliable information.) This is another reason to replace the <i>mtab</i> file with a symlink to the <i>/proc/mounts</i> file. </p>
<p> Checking files on NFS filesystems referenced by file descriptors (i.e. the <code>fcntl</code> and <code>ioctl</code> families of functions) may lead to inconsistent results due to the lack of a consistency check in the kernel even if the <code>noac</code> mount option is used. </p>
<p> The <code>loop</code> option with the <code>offset</code> or <code>sizelimit</code> options used may fail when using older kernels if the <code>mount</code> command can&#8217;t confirm that the size of the block device has been configured as requested. This situation can be worked around by using the <code><a href="/docs/linux/man/8-losetup/">losetup</a></code>(8) command manually before calling <code>mount</code> with the configured loop device.</p>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2), <code><a href="/docs/linux/man/5-filesystems/">filesystems</a></code>(5), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7), <code><a href="/docs/linux/man/8-e2label/">e2label</a></code>(8), <code><a href="/docs/linux/man/8-findmnt/">findmnt</a></code>(8), <code><a href="/docs/linux/man/8-losetup/">losetup</a></code>(8), <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-mountd/">mountd</a></code>(8), <code><a href="/docs/linux/man/8-nfsd/">nfsd</a></code>(8), <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8), <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>mount</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
