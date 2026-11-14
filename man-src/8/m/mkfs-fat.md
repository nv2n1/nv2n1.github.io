---
title: "mkfs-fat(8)"
name: "mkfs-fat"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-fat/"
description: "mkfs.fat – create an MS-DOS FAT filesystem"
---

<p>mkfs.fat &#8211; create an MS-DOS FAT filesystem</p>
<h2>Synopsis</h2>
<p><code>mkfs.fat</code> [<i>OPTIONS</i>] <i>DEVICE</i> [<i>BLOCK-COUNT</i>]</p>
<h2>Description</h2>
<p><code>mkfs.fat</code> is used to create a FAT filesystem on a device or in an image file. <i>DEVICE</i> is the special file corresponding to the device (e.g. /dev/sdXX) or the image file (which does not need to exist when the option <code>-C</code> is given). <i>BLOCK-COUNT</i> is the number of blocks on the device and size of one block is always 1024 bytes, independently of the sector size or the cluster size. Therefore <i>BLOCK-COUNT</i> specifies size of filesystem in KiB unit and not in the number of sectors (like for all other <code>mkfs.fat</code> options). If omitted, <code>mkfs.fat</code> automatically chooses a filesystem size to fill the available space. </p>
<p> Two different variants of the FAT filesystem are supported. Standard is the FAT12, FAT16 and FAT32 filesystems as defined by Microsoft and widely used on hard disks and removable media like USB sticks and SD cards. The other is the legacy Atari variant used on Atari ST. </p>
<p> In Atari mode, if not directed otherwise by the user, <code>mkfs.fat</code> will always use 2 sectors per cluster, since GEMDOS doesn&#8217;t like other values very much. It will also obey the maximum number of sectors GEMDOS can handle. Larger filesystems are managed by raising the logical sector size. An Atari-compatible serial number for the filesystem is generated, and a 12 bit FAT is used only for filesystems that have one of the usual floppy sizes (720k, 1.2M, 1.44M, 2.88M), a 16 bit FAT otherwise. This can be overridden with the <code>-F</code> option. Some PC-specific boot sector fields aren&#8217;t written, and a boot message (option <code>-m</code>) is ignored.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Normally, for any filesystem except very small ones, <code>mkfs.fat</code> will align all the data structures to cluster size, to make sure that as long as the partition is properly aligned, so will all the data structures in the filesystem. This option disables alignment; this may provide a handful of additional clusters of storage at the expense of a significant performance degradation on RAIDs, flash media or large-sector hard disks.</p>
<dt><code>-A</code></p>
<dd>Select using the Atari variation of the FAT filesystem if that isn&#8217;t active already, otherwise select standard FAT filesystem. This is selected by default if <code>mkfs.fat</code> is run on 68k Atari Linux.</p>
<dt><code>-b</code> <i>SECTOR-OF-BACKUP</i></p>
<dd>Selects the location of the backup boot sector for FAT32. Default depends on number of reserved sectors, but usually is sector 6. If there is a free space available after the backup boot sector then backup of the FAT32 info sector is put after the backup boot sector, usually at sector 7. The backup must be within the range of reserved sectors. Value 0 completely disables creating of backup boot and info FAT32 sectors.</p>
<dt><code>-c</p>
<dd>Check the device for bad blocks before creating the filesystem.</p>
<dt>-C</code></p>
<dd>Create the file given as <i>DEVICE</i> on the command line, and write the to-be-created filesystem to it. This can be used to create the new filesystem in a file instead of on a real device, and to avoid using <code>dd</code> in advance to create a file of appropriate size. With this option, the <i>BLOCK-COUNT</i> must be given, because otherwise the intended size of the filesystem wouldn&#8217;t be known. The file created is a sparse file, which actually only contains the meta-data areas (boot sector, FATs, and root directory). The data portions won&#8217;t be stored on the disk, but the file nevertheless will have the correct size. The resulting file can be copied later to a floppy disk or other device, or mounted through a loop device.</p>
<dt><code>-D</code> <i>DRIVE-NUMBER</i></p>
<dd>Specify the BIOS drive number to be stored in the FAT boot sector. For hard disks and removable medias it is usually 0x80-0xFF (0x80 is first hard disk C:, 0x81 is second hard disk D:, &#8230;), for floppy devices or partitions to be used for floppy emulation it is 0x00-0x7F (0x00 is first floppy A:, 0x01 is second floppy B:).</p>
<dt><code>-f</code> <i>NUMBER-OF-FATS</i></p>
<dd>Specify the number of file allocation tables in the filesystem. The default is 2.</p>
<dt><code>-F</code> <i>FAT-SIZE</i></p>
<dd>Specifies the type of file allocation tables used (12, 16 or 32 bit). If nothing is specified, <code>mkfs.fat</code> will automatically select between 12, 16 and 32 bit, whatever fits better for the filesystem size.</p>
<dt><code>-g</code> <i>HEADS</i>/<i>SECTORS-PER-TRACK</i></p>
<dd>Specify <i>HEADS</i> and <i>SECTORS-PER-TRACK</i> numbers which represents disk geometry of <i>DEVICE</i>. Both numbers are stored into the FAT boot sector. Number <i>SECTORS-PER-TRACK</i> is used also for aligning the total count of FAT sectors. By default disk geometry is read from <i>DEVICE</i> itself. If it is not available then <i>LBA-Assist Translation</i> and translation table from the <i>SD Card Part 2 File System Specification</i> based on total number of disk sectors is used.</p>
<dt><code>-h</code> <i>NUMBER-OF-HIDDEN-SECTORS</i></p>
<dd>Specify the number of so-called <i>hidden sectors</i>, as stored in the FAT boot sector: this number represents the beginning sector of the partition containing the file system. Normally this is an offset (in sectors) relative to the start of the disk, although for MBR logical volumes contained in an extended partition of type 0x05 (a non-LBA extended partition), a quirk in the MS-DOS implementation of FAT requires it to be relative to the partition&#8217;s immediate containing Extended Boot Record. Boot code and other software handling FAT volumes may also rely on this field being set up correctly; most modern FAT implementations will ignore it. By default, if the <i>DEVICE</i> is a partition block device, <code>mkfs.fat</code> uses the partition offset relative to disk start. Otherwise, <code>mkfs.fat</code> assumes zero. Use this option to override this behaviour.</p>
<dt><code>-i</code> <i>VOLUME-ID</i></p>
<dd>Sets the volume ID of the newly created filesystem; <i>VOLUME-ID</i> is a 32-bit hexadecimal number (for example, 2e24ec82). The default is a number which depends on the filesystem creation time.</p>
<dt><code>-I</code></p>
<dd>Ignore and disable safety checks. By default <code>mkfs.fat</code> refuses to create a filesystem on a device with partitions or virtual mapping. <code>mkfs.fat</code> will complain and tell you that it refuses to work. This is different when using MO disks. One doesn&#8217;t always need partitions on MO disks. The filesystem can go directly to the whole disk. Under other OSes this is known as the <i>superfloppy</i> format. This switch will force <code>mkfs.fat</code> to work properly.</p>
<dt><code>-l</code> <i>FILENAME</i></p>
<dd>Read the bad blocks list from <i>FILENAME</i>.</p>
<dt><code>-m</code> <i>MESSAGE-FILE</i></p>
<dd>Sets the message the user receives on attempts to boot this filesystem without having properly installed an operating system. The message file must not exceed 418 bytes once line feeds have been converted to carriage return-line feed combinations, and tabs have been expanded. If the filename is a hyphen (-), the text is taken from standard input.</p>
<dt><code>-M</code> <i>FAT-MEDIA-TYPE</i></p>
<dd>Specify the media type to be stored in the FAT boot sector. This value is usually 0xF8 for hard disks and is 0xF0 or a value from 0xF9 to 0xFF for floppies or partitions to be used for floppy emulation.</p>
<dt><code>&#8211;mbr</code>[=<i>y</i>|<i>yes</i>|<i>n</i>|<i>no</i>|<i>a</i>|<i>auto</i>]</p>
<dd>Fill (fake) MBR table with disk signature one partition which starts at sector 0 (includes MBR itself) and spans whole disk device. It is needed only for non-removable disks used on Microsoft Windows systems and only when formatting whole unpartitioned disk. Location of the disk signature and partition table overlaps with the end of the first FAT sector (boot code location), therefore there is no additional space usage. Default is <i>auto</i> mode in which <code>mkfs.fat</code> put MBR table only for non-removable disks when formatting whole unpartitioned disk.</p>
<dt><code>-n</code> <i>VOLUME-NAME</i></p>
<dd>Sets the volume name (label) of the filesystem. The volume name can be up to 11 characters long. Supplying an empty string, a string consisting only of white space or the string &quot;NO NAME&quot; as <i>VOLUME-NAME</i> has the same effect as not giving the <code>-n</code> option. The default is no label.</p>
<dt><code>&#8211;codepage</code>=<i>PAGE</i></p>
<dd>Use DOS codepage <i>PAGE</i> to encode label. By default codepage 850 is used.</p>
<dt><code>-r</code> <i>ROOT-DIR-ENTRIES</i></p>
<dd>Select the minimal number of entries available in the root directory. The default is 112 or 224 for floppies and 512 for hard disks. Note that this is minimal number and it may be increased by <code>mkfs.fat</code> due to alignment of structures. See also <code>mkfs.fat</code> option <code>-a</code>.</p>
<dt><code>-R</code> <i>NUMBER-OF-RESERVED-SECTORS</i></p>
<dd>Select the minimal number of reserved sectors. With FAT32 format at least 2 reserved sectors are needed, the default is 32. Otherwise the default is 1 (only the boot sector). Note that this is minimal number and it may be increased by <code>mkfs.fat</code> due to alignment of structures. See also <code>mkfs.fat</code> option <code>-a</code>.</p>
<dt><code>-s</code> <i>SECTORS-PER-CLUSTER</i></p>
<dd>Specify the number of disk sectors per cluster. Must be a power of 2, i.e. 1, 2, 4, 8, &#8230; 128.</p>
<dt><code>-S</code> <i>LOGICAL-SECTOR-SIZE</i></p>
<dd>Specify the number of bytes per logical sector. Must be a power of 2 and greater than or equal to 512, i.e. 512, 1024, 2048, 4096, 8192, 16384, or 32768. Values larger than 4096 are not conforming to the FAT file system specification and may not work everywhere.</p>
<dt><code>-v</code></p>
<dd>Verbose execution.</p>
<dt><code>&#8211;offset</code> <i>SECTOR</i></p>
<dd>Write the filesystem at a specific sector into the device file. This is useful for creating a filesystem in a partitioned disk image without having to set up a loop device.</p>
<dt><code>&#8211;variant</code> <i>TYPE</i></p>
<dd>Create a filesystem of variant <i>TYPE</i>. Acceptable values are <i>standard</i> and <i>atari</i> (in any combination of upper/lower case). See above under DESCRIPTION for the differences.</p>
<dt><code>&#8211;help</code></p>
<dd>Display option summary and exit.</p>
<dt><code>&#8211;invariant</code></p>
<dd>Use constants for normally randomly generated or time based data such as volume ID and creation time. Multiple runs of <code>mkfs.fat</code> on the same device create identical results with this option. Its main purpose is testing <code>mkfs.fat</code>.</dl>
<h2>Bugs</h2>
<p><code>mkfs.fat</code> can not create boot-able filesystems. This isn&#8217;t as easy as you might think at first glance for various reasons and has been discussed a lot already. <code>mkfs.fat</code> simply will not support it ;)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fatlabel/">fatlabel</a></code>(8), <code><a href="/docs/linux/man/8-fsck-fat/">fsck.fat</a></code>(8)</p>
<h2>Homepage</h2>
<p>The home for the <code>dosfstools</code> project is its GitHub project page</p>
<h2>Authors</h2>
<p><code>dosfstools</code> were written by Werner Almesberger Roman Hodek and others. Current maintainers are Andreas Bombe and Pali Rohár</p>
