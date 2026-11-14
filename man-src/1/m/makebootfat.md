---
title: "makebootfat(1)"
name: "makebootfat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makebootfat/"
description: "makebootfat – Makebootfat Bootable FAT Disk Creation"
---

<h2>NAME</h2>
<p> makebootfat &#8211; Makebootfat Bootable FAT Disk Creation</p>
<h2>SYNOPSIS</h2>
<p> makebootfat [options] IMAGE </p>
<h2>DESCRIPTION</h2>
<p> This utility creates a bootable FAT filesystem and populates it with files and boot tools. </p>
<p> It is mainly designed to create bootable USB and Fixed disk for the AdvanceCD project. </p>
<p> The official site of AdvanceCD and makebootfat is: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://advancemame.sourceforge.net/">http://advancemame.sourceforge.net/</a> </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o, &#8211;output DEVICE</code></p>
<dd> Specify the output device. It must be the device where you want to setup the filesystem. You can use the special a&#8221;usba&#8221; value to automatically select the USB Mass Storage device connected at the system. This option is always required.</p>
<dt><code>-b, &#8211;boot FILE</code></p>
<dd>
<dt><code>-1, &#8211;boot-fat12 FILE</code></p>
<dd>
<dt><code>-2, &#8211;boot-fat16 FILE</code></p>
<dd>
<dt><code>-3, &#8211;boot-fat32 FILE</code></p>
<dd> Specify the FAT boot sector images to use. The -b option uses the same sector for all the FAT types. The other options can be used to specify a different sector for different FAT types. The FAT types for which a boot sector is not specified are not used. This option is always required.</p>
<dt><code>-m, &#8211;mbr FILE</code></p>
<dd> Specify the MBR sector image to use. If this option is specified a partition table is created on the disk. Otherwise the disk is filled without a partition table like a floppy disk.</p>
<dt><code>-F, &#8211;mbrfat</code></p>
<dd> Change the MBR image specified with the -m option to pretend to be a FAT filesystem starting from the first sector of the disk. This allows booting from USB-FDD (Floppy Disk Drive) also using a partition table generally required by USB-HDD (Hard Disk Drive). The MBR image specified with the -m option must have executable code positioned like a FAT boot sector. You can use the included &#8216;mbrfat.bin&#8217; file.</p>
<dt><code>-c, &#8211;copy FILE</code></p>
<dd> Copy the specified file in the root directory of the disk. The file is copied using the readonly attribute.</p>
<dt><code>-x, &#8211;exclude FILE</code></p>
<dd> Exclude the specified files and subdirectories in the IMAGE directory to copy. The path must be specified using the same format used in the IMAGE directory specification.</p>
<dt><code>-X, &#8211;syslinux2</code></p>
<dd> Enforce the syslinux 2.xx FAT limitations. Syslinux 2.xx doesn&#8217;t support FAT32 at all, and FAT16 with 64 and 128 sectors per cluster formats. This option excludes all the FAT formats not supported by syslinux. Please note that it limits the maximum size of filesystem to 1 GB.</p>
<dt><code>-Y, &#8211;syslinux3</code></p>
<dd> Enforce the syslinux 3.xx FAT support. Syslinux 3.00 supports all the FAT types and sizes but it requires a special customisation of the boot sector and of the file &#8216;ldlinux.sys&#8217;. This option does this customisation without the need to use the syslinux installer if the &#8216;ldlinux.sys&#8217; file is copied on disk with the -c option.</p>
<dt><code>-Z, &#8211;zip</code></p>
<dd> If possible force the ZIP-Disk compatibility. It sets a geometry of 32 sectors and 64 heads. It also uses the 4&#8217;th partition entry in the partition table. It&#8217;s required to boot also in USB-ZIP mode.</p>
<dt><code>-P, &#8211;partition</code></p>
<dd> Ensure to operate on a partition and not on a disk.</p>
<dt><code>-D, &#8211;disk</code></p>
<dd> Ensure to operate on a disk and not on a partition.</p>
<dt><code>-L, &#8211;label LABEL</code></p>
<dd> Set the FAT label. The label is a string of 11 chars.</p>
<dt><code>-O, &#8211;oem OEM</code></p>
<dd> Set the FAT OEM name. The OEM name is a string of 11 chars.</p>
<dt><code>-S, &#8211;serial SERIAL</code></p>
<dd> Set the FAT serial number. The serial number is a 32 bit unsigned integer.</p>
<dt><code>-E, &#8211;drive DRIVE</code></p>
<dd> Set the BIOS drive to setup in the FAT boot sector. Generally this value is ignored by boot sectors, with the exception of the FAT12 and FAT16 FreeDOS boot sectors that require the correct value or the value 255 to force auto detection.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Print some information on the device and on the filesystem created.</p>
<dt><code>-i, &#8211;interactive</code></p>
<dd> Show the errors in a message box. Only for Windows.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a short help.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print the version number.</p>
<dt><code>IMAGE</code></p>
<dd> Directory image to copy on the disk. All the files and subdirectories present in this directory are copied on the disk.</dl>
<h2>DISKS AND PARTITIONS NAMES</h2>
<p> In Linux disk devices are named /dev/hdX or /dev/sdX where X is a letter. Partition devices are named /dev/hdXN or /dev/sdXN where X is a letter and N a digit. </p>
<p> In Windows disk devices are named \.\PhysicalDriveN where N is a digit. Partition devices are named \.\X: where X is a letter, but sometimes \.\X: is a disk and not a partition, for example on floppies and on all the USB Mass Storage devices without a partition table.</p>
<h2>SYSLINUX</h2>
<p> To make a bootable FAT using syslinux you must use the -X option for syslinux version 2.xx or the -Y option for syslinux version 3.xx. You must also copy in the root directory of the disk the files:</p>
<dl>
<dt>
<dd>
<dl>
<dt> <i>ldlinux.sys</i></p>
<dd>The syslinux loader.</p>
<dt> <i>syslinux.cfg</i></p>
<dd>The syslinux configuration file.</p>
<dt> <i>linux</i></p>
<dd>The Linux kernel image (the file name may be different).</p>
<dt> <i>initrd.img</i></p>
<dd>The initrd filesystem (the file name may be different or missing).</dl>
</dl>
<p> You must also specify the &#8216;ldlinux.bss&#8217; boot sector with the -b option and possibily the &#8216;mbr.bin&#8217; MBR sector with the -m option. Both the sector images are present in the syslinux package. </p>
<p> For example: </p>
<dl>
<dt>
<dd> makebootfat -o usb \ </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-Y \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-b ldlinux.bss -m mbr.bin \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c ldlinux.sys -c syslinux.cfg \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c linux -c initrd.img \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>image</p>
</dl>
<h2>LOADLIN AND FREEDOS</h2>
<p> To make a bootable FAT using loadlin and FreeDOS you must copy in the root directory of the disk the files:</p>
<dl>
<dt>
<dd>
<dl>
<dt> <i>kernel.sys</i></p>
<dd>The FreeDOS kernel. Remember to use the a&#8221;32a&#8221; kernel version to support FAT32.</p>
<dt> <i>command.com</i></p>
<dd>The FreeDOS shell.</p>
<dt> <i>autoexec.bat</i></p>
<dd>Used to start loadlin.</p>
<dt> <i>loadlin.exe</i></p>
<dd>The loadlin executable.</p>
<dt> <i>linux</i></p>
<dd>The Linux kernel image (the file name may be different).</p>
<dt> <i>initrd.img</i></p>
<dd>The initrd filesystem (the file name may be different or missing).</dl>
</dl>
<p> You must also specify the FreeDOS boot sectors available on the FreeDOS &#8216;sys&#8217; source package with the -1, -2, -3 option. For the MBR you can use the sectors image available on the FreeDOS &#8216;fdisk&#8217; source package. </p>
<p> For example: </p>
<dl>
<dt>
<dd> makebootfat -o /dev/hda1 \ </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-E 255 \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-1 fat12com.bin -2 fat16com.bin -3 fat32lba.bin \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c kernel.sys -c command.com \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c autoexec.bat -c loadlin.exe \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c linux -c initrd.img \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>image</p>
</dl>
<h2>MULTI STANDARD USB BOOTING</h2>
<p> The BIOS USB boot support is generally differentiated in three categories: USB-HDD, USB-FDD and USB-ZIP. </p>
<p> The USB-HDD (Hard Disk Drive) standard is the preferred choice and it requires the presence of a partition table in the first sector of the disk. You can create this type of disk using the -m option. </p>
<p> The USB-FDD (Floppy Disk Drive) standard requires the presence of a filesystem starting from the first sector of the disk without a partition table. You can create this type of disk without using the -m option. </p>
<p> The USB-ZIP (ZIP Drive) standard requires the presence of a device with a very specific geometry. Specifically, it requires a geometry with 32 sectors and 64 heads. It also requires the presence of a partition table with only a bootable partition in the fourth entry. You can create this type of disk using the -m and -Z option. </p>
<p> Generally these standards are incompatible, but using the -m, -F and -Z options you can create a disk compatible with all of them. </p>
<p> To use the -F option, the MBR image specified must follow the constrains:</p>
<dl>
<dt>&bull;</p>
<dd> It must start with a standard FAT 3 bytes jump instruction.</p>
<dt>&bull;</p>
<dd> It must have the bytes from address 3 to 89 (included) unused.</dl>
<p> And example of such image is in the &#8216;mbrfat.bin&#8217; file. </p>
<p> For example to create a syslinux image: </p>
<dl>
<dt>
<dd> makebootfat -o usb \ </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-Y \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-Z \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-b ldlinux.bss -m mbrfat.bin -F \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c ldlinux.sys -c syslinux.cfg \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c linux -c initrd.img \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>image</p>
</dl>
<p> and for a FreeDOS and loadlin image: </p>
<dl>
<dt>
<dd> makebootfat -o usb \ </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-E 255 \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-Z \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-1 fat12com.bin -2 fat16com.bin -3 fat32chs.bin \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-m mbrfat.bin -F \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c kernel.sys -c command.com \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c autoexec.bat -c loadlin.exe \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c linux -c initrd.img \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>image</p>
</dl>
<p> Please note that FreeDos has some problems booting from USB. It works only on very few conditions.</p>
<h2>EXCLUSION</h2>
<p> To exclude some files or directories in the image copy, you can use the -x option using the same path specification which are you using for the image directory. </p>
<p> For example, if you need to exclude the &#8216;isolinux&#8217; and &#8216;syslinux&#8217; subdirectories from the &#8216;image&#8217; directory you can use the command: </p>
<dl>
<dt>
<dd> makebootfat &#8230; \ </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-x image/isolinux \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-x image/syslinux \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>image</p>
</dl>
<h2>COPYRIGHT</h2>
<p> This file is Copyright (C) 2004, 2005 Andrea Mazzoleni</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-syslinux/">syslinux</a>(1), <a href="/docs/linux/man/1-mkdosfs/">mkdosfs</a>(1), <a href="/docs/linux/man/1-dosfsck/">dosfsck</a>(1) </p>
<h2>Index</h2>
