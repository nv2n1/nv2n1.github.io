---
title: "disktype(1)"
name: "disktype"
section: "1"
letter: "d"
url: "/docs/linux/man/1-disktype/"
description: "disktype – disk format detector"
---

<h2 class="name">NAME</h2>
<p> <code>disktype</code> &#8211; disk format detector </p>
<h2>SYNOPSIS</h2>
<p> <i>file&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The purpose of is to detect the content format of a disk or disk image. It knows about common file systems, partition tables, and boot codes.</p>
<h2>USAGE</h2>
<p> can be run with any number of regular files or device special files as arguments. They will be analyzed in the order given, and the results printed to standard output. There are no switches in this version. Note that running disktype on device files like your hard disk will likely require root rights. </p>
<p> See the online documentation at &lt;<a rel="nofollow" href="http://disktype.sourceforge.net/doc/">http://disktype.sourceforge.net/doc/</a>&gt; for some example command lines.</p>
<h2>RECOGNIZED FORMATS</h2>
<p> The following formats are recognized by this version of</p>
<dl>
<dt><code>File systems:</code></p>
<dd> FAT12/FAT16/FAT32, NTFS, HPFS, MFS, HFS, HFS Plus, ISO9660, ext2/ext3, Minix, ReiserFS, Reiser4, Linux romfs, Linux cramfs, Linux squashfs, UFS (some variations), SysV FS (some variations), JFS, XFS, Amiga FS/FFS, BeOS BFS, QNX4 FS, UDF, 3DO CD-ROM file system, Veritas VxFS, Xbox DVD file system.</p>
<dt><code>Partitioning:</code></p>
<dd> DOS/PC style, Apple, Amiga &quot;Rigid Disk&quot;, ATARI ST (AHDI3), BSD disklabel, Linux RAID physical disks, Linux LVM1 physical volumes, Linux LVM2 physical volumes, Solaris x86 disklabel (vtoc), Solaris SPARC disklabel.</p>
<dt><code>Other structures:</code></p>
<dd> Debian split floppy header, Linux swap.</p>
<dt><code>Disk images:</code></p>
<dd> Raw CD image (.bin), Virtual PC hard disk image, Apple UDIF disk image (limited).</p>
<dt><code>Boot codes:</code></p>
<dd> LILO, GRUB, SYSLINUX, ISOLINUX, Linux kernel, FreeBSD loader, Sega Dreamcast (?).</p>
<dt><code>Compression formats:</code></p>
<dd> gzip, compress, bzip2.</p>
<dt><code>Archive formats:</code></p>
<dd> tar, cpio, bar, dump/restore.</dl>
<p> Compressed files (gzip, compress, bzip2 formats) will also have their contents analyzed using transparent decompression. The appropriate compression program must be installed on the system, i.e. <a href="/docs/linux/man/1-gzip/">gzip</a>(1) for the gzip and compress formats, <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1) for the bzip2 format. </p>
<p> Disk images in general will also have their contents analyzed using the proper mapping, with the exception of the Apple UDIF format. </p>
<p> See the online documentation at &lt;<a rel="nofollow" href="http://disktype.sourceforge.net/doc/">http://disktype.sourceforge.net/doc/</a>&gt; for more details on the supported formats and their quirks.</p>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="http://disktype.sourceforge.net/">http://disktype.sourceforge.net/</a></p>
<h2>AUTHOR</h2>
<p> Christoph Pfisterer &lt;chrisp [at] users.sourceforge.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-file/">file</a>(1), <a href="/docs/linux/man/8-gpart/">gpart</a>(8) </p>
<h2>Index</h2>
