---
title: "fs(5)"
name: "fs"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fs/"
description: "filesystems – Linux filesystem types: ext, ext2, ext3, ext4, hpfs, iso9660, JFS, minix, msdos, ncpfs nfs, ntfs, proc, Reiserfs, smb, sysv, umsdos, vfat, XFS, xiafs"
---

<p>filesystems &#8211; Linux filesystem types: ext, ext2, ext3, ext4, hpfs, iso9660, JFS, minix, msdos, ncpfs nfs, ntfs, proc, Reiserfs, smb, sysv, umsdos, vfat, XFS, xiafs</p>
<h2>Description</h2>
<p>When, as is customary, the <code>proc</code> filesystem is mounted on <i>/proc</i>, you can find in the file <i>/proc/filesystems</i> which filesystems your kernel currently supports; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for more details. There is also a legacy <code><a href="/docs/linux/man/2-sysfs/">sysfs</a></code>(2) system call (whose availability is controlled by the <code>CONFIG_SYSFS_SYSCALL</code> kernel build configuration option since Linux 3.15) that enables enumeration of the currently available filesystem types regardless of <i>/proc</i> availability and/or sanity. </p>
<p> If you need a currently unsupported filesystem, insert the corresponding kernel module or recompile the kernel. </p>
<p> In order to use a filesystem, you have to <i>mount</i> it; see <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) and <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
<p> The following list provides a short description of the available or historically available filesystems in the Linux kernel. See the kernel documentation for a comprehensive description of all options and limitations.</p>
<dl>
<dt><code>ext</code></p>
<dd>is an elaborate extension of the <code>minix</code> filesystem. It has been completely superseded by the second version of the extended filesystem (<code>ext2</code>) and has been removed from the kernel (in 2.1.21).</p>
<dt><code>ext2</code></p>
<dd>is the high performance disk filesystem used by Linux for fixed disks as well as removable media. The second extended filesystem was designed as an extension of the extended filesystem (<code>ext</code>). See <code><a href="/docs/linux/man/5-ext2/">ext2</a></code>(5).</p>
<dt><code>ext3</code></p>
<dd>is a journaling version of the <code>ext2</code> filesystem. It is easy to switch back and forth between <code>ext2</code> and <code>ext3</code>. See <code><a href="/docs/linux/man/5-ext3/">ext3</a></code>(5).</p>
<dt><code>ext4</code></p>
<dd>is a set of upgrades to <code>ext3</code> including substantial performance and reliability enhancements, plus large increases in volume, file, and directory size limits. See <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5).</p>
<dt><code>hpfs</code></p>
<dd>is the High Performance Filesystem, used in OS/2. This filesystem is read-only under Linux due to the lack of available documentation.</p>
<dt><code>iso9660</code></p>
<dd>is a CD-ROM filesystem type conforming to the ISO 9660 standard.</p>
<dl>
<dd>
<dl>
<dt><code>High Sierra</code></p>
<dd>Linux supports High Sierra, the precursor to the ISO 9660 standard for CD-ROM filesystems. It is automatically recognized within the <code>iso9660</code> filesystem support under Linux.</p>
<dt><code>Rock Ridge</code></p>
<dd>Linux also supports the System Use Sharing Protocol records specified by the Rock Ridge Interchange Protocol. They are used to further describe the files in the <code>iso9660</code> filesystem to a UNIX host, and provide information such as long filenames, UID/GID, POSIX permissions, and devices. It is automatically recognized within the <code>iso9660</code> filesystem support under Linux.</dl>
</dl>
<dt><code>JFS</code></p>
<dd>is a journaling filesystem, developed by IBM, that was integrated into Linux in kernel 2.4.24.</p>
<dt><code>minix</code></p>
<dd>is the filesystem used in the Minix operating system, the first to run under Linux. It has a number of shortcomings, including a 64 MB partition size limit, short filenames, and a single timestamp. It remains useful for floppies and RAM disks.</p>
<dt><code>msdos</code></p>
<dd>is the filesystem used by DOS, Windows, and some OS/2 computers. <code>msdos</code> filenames can be no longer than 8 characters, followed by an optional period and 3 character extension.</p>
<dt><code>ncpfs</code></p>
<dd>is a network filesystem that supports the NCP protocol, used by Novell NetWare. It was was removed from the kernel in 4.17.</p>
<dd>To use <code>ncpfs</code>, you need special programs, which can be found at</p>
<dt><code>nfs</code></p>
<dd>is the network filesystem used to access disks located on remote computers.</p>
<dt><code>ntfs</code></p>
<dd>is the filesystem native to Microsoft Windows NT, supporting features like ACLs, journaling, encryption, and so on.</p>
<dt><code>proc</code></p>
<dd>is a pseudo filesystem which is used as an interface to kernel data structures rather than reading and interpreting <i>/dev/kmem</i>. In particular, its files do not take disk space. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt><code>Reiserfs</code></p>
<dd>is a journaling filesystem, designed by Hans Reiser, that was integrated into Linux in kernel 2.4.1.</p>
<dt><code>smb</code></p>
<dd>is a network filesystem that supports the SMB protocol, used by Windows for Workgroups, Windows NT, and Lan Manager. See</p>
<dt><code>sysv</code></p>
<dd>is an implementation of the System V/Coherent filesystem for Linux. It implements all of Xenix FS, System V/386 FS, and Coherent FS.</p>
<dt><code>umsdos</code></p>
<dd>is an extended DOS filesystem used by Linux. It adds capability for long filenames, UID/GID, POSIX permissions, and special files (devices, named pipes, etc.) under the DOS filesystem, without sacrificing compatibility with DOS.</p>
<dt><code>tmpfs</code></p>
<dd>is a filesystem whose contents reside in virtual memory. Since the files on such filesystems typically reside in RAM, file access is extremely fast. See <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5).</p>
<dt><code>vfat</code></p>
<dd>is an extended FAT filesystem used by Microsoft Windows95 and Windows NT. <code>vfat</code> adds the capability to use long filenames under the MSDOS filesystem.</p>
<dt><code>XFS</code></p>
<dd>is a journaling filesystem, developed by SGI, that was integrated into Linux in kernel 2.4.20.</p>
<dt><code>xiafs</code></p>
<dd>was designed and implemented to be a stable, safe filesystem by extending the Minix filesystem code. It provides the basic most requested features without undue complexity. The <code>xiafs</code> filesystem is no longer actively developed or maintained. It was removed from the kernel in 2.1.21.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-fuse/">fuse</a></code>(4), <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5), <code><a href="/docs/linux/man/5-ext2/">ext2</a></code>(5), <code><a href="/docs/linux/man/5-ext3/">ext3</a></code>(5), <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/5-sysfs/">sysfs</a></code>(5), <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
