---
title: "pmount(1)"
name: "pmount"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmount/"
description: "pmount – mount arbitrary hotpluggable devices as normal user"
---

<h2 class="name">NAME</h2>
<p> pmount &#8211; mount arbitrary hotpluggable devices as normal user</p>
<h2>SYNOPSIS</h2>
<p> <code>pmount</code> [ <i>options</i> ] <i>device</i> </p>
<p> <code>pmount</code> [ <i>options</i> ] <i>device label</i> </p>
<p> <code>pmount &#8211;lock</code> [ <i>options</i> ] <i>device pid</i> </p>
<p> <code>pmount &#8211;unlock</code> [ <i>options</i> ] <i>device pid</i> </p>
<p> <code>pmount</code> </p>
<h2>DESCRIPTION</h2>
<p> pmount (&quot;policy mount&quot;) is a wrapper around the standard mount program which permits normal users to mount removable devices without a matching /etc/fstab entry. </p>
<p> pmount also supports encrypted devices which use dm-crypt and have LUKS metadata. If a LUKS-capable <code>cryptsetup</code> is installed, pmount will use it to decrypt the device first and mount the mapped unencrypted device instead. </p>
<p> <code>pmount</code> is invoked like this: </p>
<p> <code>pmount</code> <i>device </i> [ <i>label</i> ] </p>
<p> This will mount <i>device</i> to a directory below /media if policy is met (see below). If <i>label</i> is given, the mount point will be /media/label, otherwise it will be /media/device. </p>
<p> The device will be mounted with the following flags: async,atime,nodev,noexec,noauto,nosuid,user,rw </p>
<p> Some applications like CD burners modify a raw device which must not be mounted while the burning process is in progress. To prevent automatic mounting, pmount offers a locking mechanism: <code>pmount &#8211;lock </code> <i>device pid</i> will prevent the pmounting of <i>device</i> until it is unlocked again using <code>pmount &#8211;unlock </code> <i>device pid</i>. The process id <i>pid</i> assigns the lock to a particular process; this allows to lock a device by several processes. </p>
<p> During mount, the list of locks is cleaned, i. e. all locks whose associated process does not exist any more are removed. This prevents forgotten indefinite locks from crashed programs. </p>
<p> Running <code>pmount</code> without arguments prints the list of mounted removable devices, a bit in the fashion of <code>mount </code> (1). </p>
<p> Please note that you can use labels and uuids as described in <code>fstab</code> (5) for devices present in <i>/etc/fstab</i>. In this case, the device name need to match exactly the corresponding entry in <i>/etc/fstab</i>, including the <i>LABEL=</i> or <i>UUID=</i> part. </p>
<h2>POLICY</h2>
<p> The mount will succeed if all of the following conditions are met: </p>
<dl>
<dt>&bull;</p>
<dd> <i>device</i> is a block device in /dev/</p>
<dt>&bull;</p>
<dd> <i>device</i> is not in /etc/fstab (if it is, pmount executes <code> mount </code><i> device</i> as the calling user to handle this transparently). See below for more details.</p>
<dt>&bull;</p>
<dd> <i>device</i> is not already mounted according to /etc/mtab and /proc/mounts</p>
<dt>&bull;</p>
<dd> if the mount point already exists, there is no device already mounted at it and the directory is empty</p>
<dt>&bull;</p>
<dd> <i>device</i> is removable (USB, FireWire, or MMC device, or <code>/sys/block/</code><i>drive</i><code>/removable</code> is 1) or whitelisted in <code>/etc/pmount.allow</code>.</p>
<dt>&bull;</p>
<dd> <i>device</i> is not locked </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r, &#8211;read-only</code></p>
<dd> Force the device to be mounted read only. If neither -r nor -w is specified, the kernel will choose an appropriate default. </p>
<dt><code>-w, &#8211;read-write</code></p>
<dd> Force the device to be mounted read/write. If neither -r nor -w is specified, the kernel will choose an appropriate default. </p>
<dt><code>-s, &#8211;sync</code></p>
<dd> Mount the device with the <code>sync</code> option, i. e. without write caching. Default is <code>async</code> (write-back). With this option, write operations are much slower and due to the massive increase of updates of inode/FAT structures, flash devices may suffer heavily if you write large files. This option is intended to make it safe to just rip out USB drives without proper unmounting. </p>
<dt><code>-A, &#8211;noatime</code></p>
<dd> Mount the device with the <code>noatime</code> option. Default is <code>atime</code>. </p>
<dt><code>-e, &#8211;exec</code></p>
<dd> Mount the device with the <code>exec</code> option. Default is <code>noexec</code>. </p>
<dt><code>-t </code><i>filesystem</i>, <code>&#8211;type </code><i>filesystem</i></p>
<dd> Mount as specified file system type. The file system type is automatically determined if this option is not given. See at the bottom for a list of currently supported filesystems. </p>
<dt><code>-c </code><i>charset</i>, <code>&#8211;charset </code><i>charset</i></p>
<dd> Use given I/O character set (default: <code>utf8 </code> if called in an UTF-8 locale, otherwise mount default). This corresponds with the mount option <code>iocharset</code> (or <code>nls</code> for NTFS). This option is ignored for file systems that do not support setting the character set (see <code>mount</code> (8) for details). <code>Important note:</code> <code>pmount</code> will now mount VFAT filesystems with <i>iocharset=iso8859-1</i> as <i>iocharset=utf8</i> currently makes the filesystem case-sensitive (which is pretty bad&#8230;). </p>
<dt><code>-u </code><i>umask</i>, <code>&#8211;umask </code><i>umask</i></p>
<dd> Use specified umask instead of the default one. For UDF, the default is &#8216;000&#8217;, for VFAT and NTFS the default is &#8216;077&#8217;. This value is ignored for file systems which do not support setting an umask. Note that you can use a value of 077 to forbid anyone else to read/write the files, 027 to allow your group to read the files and 022 to allow anyone to read the files (but only you can write). </p>
<dt><code>&#8211;dmask </code><i>dmask</i></p>
<dd>
<dt><code>&#8211;fmask </code><i>fmask</i></p>
<dd> Some filesystems (essentially VFAT and HFS) supports separate <i>umasks</i> (see the <i>-u</i> option just above) for directories and files, to avoid the annoying effect of having all files executable. For these filesystems, you can specify separately the masks using these options. By default, <i>fmask</i> is <i>umask</i> without all executable permissions and <i>dmask</i> is <i>umask</i>. Most of the times, these settings should just do what you want, so there should be seldom any need for using directly the <i>&#8211;fmask</i> and <i>&#8211;dmask</i> options. </p>
<dt><code>-p</code><i>&nbsp;<wbr>file</i><code>&nbsp;<wbr>&#8211;passphrase</code><i>&nbsp;<wbr>file</i></p>
<dd> If the device is encrypted (dm-crypt with LUKS metadata), read the passphrase from specified <i>file</i> instead of prompting at the terminal. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a help message and exit successfully. </p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Enable verbose debug messages. </p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print the current version number and exit successfully. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pmount.allow</code></p>
<dd> List of devices (one device per line) which are additionally permitted for pmounting. Globs, such as <i>/dev/sda[123]</i> are permitted. See see <code>glob</code> (7) for a more complete syntax. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pumount/">pumount</a></code>(1), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) </p>
<h2>SUPPORTED FILESYSTEMS</h2>
<p> For now, <code>pmount</code> supports the following filesystems: <i>udf</i>, <i>iso9660</i>, <i>vfat</i>, <i>ntfs</i>, <i>hfsplus</i>, <i>hfs</i>, <i>ext3</i>, <i>ext2</i>, <i>ext4</i>, <i>reiserfs</i>, <i>reiser4</i>, <i>xfs</i>, <i>jfs </i> and <i>omfs</i>. They are tried sequentially in that exact order when the filesystem is not specified. </p>
<p> Additionally, <code>pmount</code> supports the filesystem types <i>ntfs-fuse</i> and <i>ntfs-3g</i> to mount NTFS volumes respectively with <code>ntfsmount</code> (1) or <code>ntfs-3g</code> (1). If the file <i>/sbin/mount.ntfs-3g</i> is found, then <code>pmount</code> will mount NTFS filestystems with type <i>ntfs-3g</i> rather than plain <i>ntfs</i>. To disable this behavior, just specify <i>-t ntfs</i> on the command-line, as this happens only for autodetection. </p>
<h2>MORE ABOUT FSTAB</h2>
<p> <code>pmount</code> now fully resolve all symlinks both in its input and in the <i>/etc/fstab</i> file, which means that if <i>/dev/cdrom</i> is a symlink to <i>/dev/hdc</i> and you try to mount <i>/dev/hdc</i> directly, <code>pmount</code> will delegate this to <code><a href="/docs/linux/man/1-mount/">mount</a></code>(1). This is a feature, and it contrasts with previous unclear behavior of <code>pmount</code> about symlinks in <i>/etc/fstab</i>. </p>
<h2>KNOWN ISSUES</h2>
<p> Though we believe <code>pmount</code> is pretty much free from security problems, there are quite a few glitches that probably will never be fixed. </p>
<dl>
<dt>&bull;</p>
<dd> <code>pmount</code> needs to try several different times to mount to get the filesystem right in the end; it is vital that <code>pmount</code> does know which precise filesystem to mount in order to give it the right options not to cause security holes. This is rather different from the behaviour of <code>mount</code> with the <i>-t auto</i> options, which can have a look at the device it is trying to mount and find out what its filesystem is. <code>pmount</code> will never try to open a device and look at it to find out which filesystem it is, as it might open quite a few security holes. Moreover, the order in which the filesystems are tried are what we could call the most commonly used filesystems on removable media. This order is unlikely to change as well. In particular, that means that when you mount an <i>ext3</i> filesystem using <code>pmount</code>, you might get a lot of fs-related kernel error messages. Sorry !</dl>
<p> <code>NOTE:</code> Starting from version <i>0.9.17</i>, <code>pmount</code> uses the same mechanism as <code>mount</code> (1) to autodetect the filesystem type, so this kind of problems should not happen anymore. </p>
<h2>AUTHOR</h2>
<p> <code>pmount </code> was originally developed by Martin Pitt &lt;martin.pitt [at] canonical.com&gt;. It is now maintained by Vincent Fourmond &lt;fourmond [at] debian.org&gt;. </p>
<h2>Index</h2>
