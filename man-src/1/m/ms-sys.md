---
title: "ms-sys(1)"
name: "ms-sys"
section: "1"
letter: "m"
url: "/docs/linux/man/1-ms-sys/"
description: "ms-sys – write Microsoft boot block"
---

<h2 class="name">NAME</h2>
<p> ms-sys &#8211; write Microsoft boot block </p>
<h2>SYNOPSIS</h2>
<p> <code>ms-sys</code> [options] [device]</p>
<h2>DESCRIPTION</h2>
<p> <code>ms-sys</code> is for writing Microsoft compatible boot records.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-1, &#8211;fat12</code></p>
<dd> Write a FAT12 floppy boot record to device.</p>
<dt><code>-2, &#8211;fat32nt</code></p>
<dd> Write a FAT32 partition NT boot record to device.</p>
<dt><code>-3, &#8211;fat32</code></p>
<dd> Write a FAT32 partition DOS (Win9x) boot record to device.</p>
<dt><code>-4, &#8211;fat32free</code></p>
<dd> Write a FAT32 partition FreeDOS boot record to device.</p>
<dt><code>-5, &#8211;fat16free</code></p>
<dd> Write a FAT16 partition FreeDOS boot record to device.</p>
<dt><code>-6, &#8211;fat16</code></p>
<dd> Write a FAT16 partition DOS (Win9x) boot record to device.</p>
<dt><code>-n, &#8211;ntfs</code></p>
<dd> Write a NTFS partition Windows 7 boot record to device. This functionality should be considered experimental and probably is of no practical use.</p>
<dt><code>-l, &#8211;wipelabel</code></p>
<dd> Reset partition disk label in boot record.</p>
<dt><code>-p, &#8211;partition</code></p>
<dd> Write partition info (hidden sectors, heads and drive id) to boot record. This might be needed on some partitions depending on which program was used to create the file system.</p>
<dt><code>-H &lt;n&gt;, &#8211;heads &lt;n&gt;</code></p>
<dd> Set number of heads written with -p switch.</p>
<dt><code>-7, &#8211;mbr7</code></p>
<dd> Write a Windows 7 master boot record to device. Does not change Windows Disk Signature (bytes 01b8-01bd). This MBR will boot certain partition types beyond cylinder 1024 using LBA addressing.</p>
<dt><code>-i, &#8211;mbrvista</code></p>
<dd> Write a Windows Vista master boot record to device. Does not change Windows Disk Signature (bytes 01b8-01bd). This MBR will boot certain partition types beyond cylinder 1024 using LBA addressing.</p>
<dt><code>-m, &#8211;mbr</code></p>
<dd> Write a Windows 2000/XP/2003 master boot record to device. Does not change Windows Disk Signature (bytes 01b8-01bd). This MBR will boot certain partition types beyond cylinder 1024 using LBA addressing.</p>
<dt><code>-9, &#8211;mbr95b</code></p>
<dd> Write a Windows 95B/98/98SE/ME master boot record to device. Does not change Windows Disk Signature (bytes 01b8-01bd) or boot drive and time (bytes 00da-00df). This MBR will boot FAT-LBA partition types 0c and 0e beyond cylinder 1024 using LBA addressing.</p>
<dt><code>-d, &#8211;mbrdos</code></p>
<dd> Write a DOS/Windows NT master boot record to device. Does not change Windows Disk Signature (bytes 01b8-01bd). This MBR will not boot beyond cylinder 1024 as it does not support LBA addressing.</p>
<dt><code>-s, &#8211;mbrsyslinux</code></p>
<dd> Write a public domain syslinux master boot record to device. Does not change Windows Disk Signature (bytes 01b8-01bd). This MBR will boot any partition types beyond cylinder 1024 using LBA addressing.</p>
<dt><code>-z, &#8211;mbrzero</code></p>
<dd> Write an empty (zeroed, non-bootable) master boot record to device. Zeroes all bytes except the partition map and signature (bytes 01be-01ff). Similar to the empty DOS partition table that fdisk creates.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> Force writing of boot record.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show program version.</p>
<dt><code>-w, &#8211;write</code></p>
<dd> Write automatically selected boot record to device.</dl>
<p> If ms-sys is started without any options a simple diagnosis will be done on the given device. </p>
<h2>EXAMPLES</h2>
<p> Please note that Windows ME is not useful for making standalone bootable floppies. However, Win9x and DOS works fine with the first two examples. </p>
<p> <code>Creating a 1.68 MB bootable floppy</code></p>
<dl>
<dt>This example assumes that you have your windows installation mounted at /dosc and also have mtools and fdformat installed.</p>
<dd></dl>
<p> fdformat /dev/fd0u1680<br />
 mformat a:<br />
 ms-sys -w /dev/fd0<br />
 mcopy /dosc/io.sys a:<br />
 mcopy /dosc/msdos.sys a:<br />
 mcopy /dosc/command.com a: </p>
<p> <code>Creating a bootable 2.8 MB floppy image to use with an el-torito bootable CD</code> </p>
<p> dd if=/dev/zero of=floppy288.img bs=1024 count=2880<br />
 /sbin/mkdosfs floppy288.img<br />
 ms-sys -1 -f floppy288.img<br />
 su<br />
 mount -o loop floppy288.img /mnt<br />
 cp msdos.sys /mnt/<br />
 cp io.sys /mnt/<br />
 cp command.com /mnt/<br />
 (it might also be a good idea to add a config.sys and autoexec.bat with CDROM support)<br />
 umount /mnt<br />
 exit<br />
 cp floppy288.img cd-files/boot.img<br />
 mkisofs -b boot.img -c boot.cat -o cdimage.iso cd-files<br />
 (burn the file cdimage.iso to a CD with cdrecord or another program) </p>
<p> <code>restoring a backup of Win9x or Win ME to a fresh hard disk</code> </p>
<p> Step 1, use GNU parted to create your FAT32 partition and file system: </p>
<p> parted (then create partition and file system) </p>
<p> Step 2, write the MBR: </p>
<p> ms-sys -w /dev/hda </p>
<p> Step 3, write the FAT32 partition boot record: </p>
<p> ms-sys -w /dev/hda1 </p>
<p> Step 4, mount your new filesystem: </p>
<p> mount /dev/hda1 /mnt </p>
<p> Step 5, read your backup </p>
<p> cd /mnt; tar -xzvf /path/to/my_windows_backup_file.tgz </p>
<h2>ENVIRONMENT</h2>
<p> The variables LANG and LC_ALL have the usual meaning, however there are not many translations available. </p>
<h2>BUGS</h2>
<p> There have been reports about unbootable FAT32 partitions created with &quot;mformat -F c:&quot;. The problem has also been reported on partitions formatted with mkdosfs and mkfs.vfat. One workaround is to use gnu parted to create the partition instead. Since version 1.1.3 ms-sys has the switch -p which is supposed to fix this problem. Unfortunately, when using ms-sys with Linux kernel 2.6 nor the -p switch or gnu parted might work. A simple workaround is to use ms-sys with Linux kernel 2.4. Another possible workaround is to manually set the number of heads with the switch -H. If the system has been booted by LILO, the correct number of heads can be given by &quot;lilo -T geom&quot;. </p>
<p> The writing of NTFS partition boot records in ms-sys probably has no practical use. For Windows 7 it has been reported that doing &quot;sysprep&quot; before making an image of an NTFS partition will make the partition restored from the image bootable.</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by G&uuml;rkan Seng&uuml;n and since edited by Henrik Carlqvist. The program ms-sys is mostly written by Henrik Carlqvist, the file CONTRIBUTORS in the source archive contains a complete list of contributors.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mformat/">mformat</a>(1) <a href="/docs/linux/man/8-fdformat/">fdformat</a>(8) <a href="/docs/linux/man/8-mkdosfs/">mkdosfs</a>(8) <a href="/docs/linux/man/8-mkisofs/">mkisofs</a>(8) <a href="/docs/linux/man/8-parted/">parted</a>(8) </p>
<h2>Index</h2>
