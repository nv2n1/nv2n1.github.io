---
title: "sgdisk(8)"
name: "sgdisk"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sgdisk/"
description: "sgdisk – Command-line GUID partition table (GPT) manipulator for Linux and Unix"
---

<p>sgdisk &#8211; Command-line GUID partition table (GPT) manipulator for Linux and Unix</p>
<h2>Synopsis</h2>
<p><code>sgdisk </code> [ options ] <i>device</i> </p>
<h2>Description</h2>
<p>GPT fdisk is a text-mode menu-driven package for creation and manipulation of partition tables. It consists of two programs: the text-mode interactive <code>gdisk</code> and the command-line <code>sgdisk</code>. Either program will automatically convert an old-style Master Boot Record (MBR) partition table or BSD disklabel stored without an MBR carrier partition to the newer Globally Unique Identifier (GUID) Partition Table (GPT) format, or will load a GUID partition table. This man page documents the command-line <code>sgdisk</code> program. Some advanced data manipulation and recovery options require you to understand the distinctions between the main and backup data, as well as between the GPT headers and the partition tables. For information on MBR vs. GPT, as well as GPT terminology and structure, see the extended <code>gdisk</code> documentation at <i><a rel="nofollow" href="http://www.rodsbooks.com/gdisk/">http://www.rodsbooks.com/gdisk/</a></i> or consult Wikipedia. The <code>sgdisk</code> program employs a user interface that&#8217;s based entirely on the command line, making it suitable for use in scripts or by experts who want to make one or two quick changes to a disk. (The program may query the user when certain errors are encountered, though.) The program&#8217;s name is based on <code>sfdisk</code>, but the user options of the two programs are entirely different from one another. Ordinarily, <code>sgdisk</code> operates on disk device files, such as <i>/dev/sda</i> or <i>/dev/hda</i> under Linux, <i>/dev/disk0</i> under Mac OS X, or <i>/dev/ad0</i> or <i>/dev/da0</i> under FreeBSD. The program can also operate on disk image files, which can be either copies of whole disks (made with <code>dd</code>, for instance) or raw disk images used by emulators such as QEMU or VMWare. Note that only <i>raw</i> disk images are supported; <code>sgdisk</code> cannot work on compressed or other advanced disk image formats. The MBR partitioning system uses a combination of cylinder/head/sector (CHS) addressing and logical block addressing (LBA). The former is klunky and limiting. GPT drops CHS addressing and uses 64-bit LBA mode exclusively. Thus, GPT data structures, and therefore <code>sgdisk</code>, do not need to deal with CHS geometries and all the problems they create. For best results, you should use an OS-specific partition table program whenever possible. For example, you should make Mac OS X partitions with the Mac OS X Disk Utility program and Linux partitions with the Linux <code>gdisk</code>, <code>sgdisk</code>, or GNU Parted programs. Upon start, <code>sgdisk</code> attempts to identify the partition type in use on the disk. If it finds valid GPT data, <code>sgdisk</code> will use it. If <code>sgdisk</code> finds a valid MBR or BSD disklabel but no GPT data, it will attempt to convert the MBR or disklabel into GPT form. (BSD disklabels are likely to have unusable first and/or final partitions because they overlap with the GPT data structures, though.) GPT fdisk can identify, but not use data in, Apple Partition Map (APM) disks, which are used on 680&#215;0- and PowerPC-based Macintoshes. If you specify any option that results in changes to an MBR or BSD disklabel, <code>sgdisk</code> ignores those changes unless the <i>-g</i> (<i>&#8211;mbrtogpt</i>), <i>-z</i> (<i>&#8211;zap</i>), or <i>-Z</i> (<i>&#8211;zap-all</i>) option is used. If you use the <i>-g</i> option, <code>sgdisk</code> replaces the MBR or disklabel with a GPT. <i>This action is potentially dangerous!</i> Your system may become unbootable, and partition type codes may become corrupted if the disk uses unrecognized type codes. Boot problems are particularly likely if you&#8217;re multi-booting with any GPT-unaware OS. The MBR-to-GPT conversion will leave at least one gap in the partition numbering if the original MBR used logical partitions. These gaps are harmless, but you can eliminate them by using the <i>-s</i> (<i>&#8211;sort</i>) option, if you like. (Doing this may require you to update your <i>/etc/fstab</i> file.) When creating a fresh partition table, certain considerations may be in order:</p>
<dl>
<dt><code>*</code></p>
<dd>For data (non-boot) disks, and for boot disks used on BIOS-based computers with GRUB as the boot loader, partitions may be created in whatever order and in whatever sizes are desired.</p>
<dt><code>*</code></p>
<dd>Boot disks for EFI-based systems require an <i>EFI System Partition</i> (<code>gdisk</code> internal code 0xEF00) formatted as FAT-32. I recommended making this partition 550 MiB. (Smaller ESPs are common, but some EFIs have flaky FAT drivers that necessitate a larger partition for reliable operation.) Boot-related files are stored here. (Note that GNU Parted identifies such partitions as having the &quot;boot flag&quot; set.)</p>
<dt><code>*</code></p>
<dd>Some boot loaders for BIOS-based systems make use of a <i>BIOS Boot Partition</i> (<code>gdisk</code> internal code 0xEF02), in which the secondary boot loader is stored, possibly without the benefit of a filesystem. (GRUB2 may optionally use such a partition.) This partition can typically be quite small (roughly 32 to 200 KiB, although 1 MiB is more common in practice), but you should consult your boot loader documentation for details.</p>
<dt><code>*</code></p>
<dd>If Windows is to boot from a GPT disk, a partition of type <i>Microsoft Reserved</i> (<code>sgdisk</code> internal code 0x0C01) is recommended. This partition should be about 128 MiB in size. It ordinarily follows the EFI System Partition and immediately precedes the Windows data partitions. (Note that GNU Parted creates all FAT partitions as this type, which actually makes the partition unusable for normal file storage in both Windows and Mac OS X.)</p>
<dt><code>*</code></p>
<dd>Some OSes&#8217; GPT utilities create some blank space (typically 128 MiB) after each partition. The intent is to enable future disk utilities to use this space. Such free space is not required of GPT disks, but creating it may help in future disk maintenance. </p>
<h2>Options</h2>
<p>Some options take no arguments, others take one argument (typically a partition number), and others take compound arguments with colon delimitation. For instance, <i>-n</i> (<i>&#8211;new</i>) takes a partition number, a starting sector number, and an ending sector number, as in <code>sgdisk -n 2:2000:50000 /dev/sdc</code>, which creates a new partition, numbered 2, starting at sector 2000 an ending at sector 50,000, on <i>/dev/sdc</i>. </p>
<p> Unrelated options may be combined; however, some such combinations will be nonsense (such as deleting a partition and then changing its GUID type code). <code>sgdisk</code> interprets options in the order in which they&#8217;re entered, so effects can vary depending on order. For instance, <code>sgdisk -s -d 2</code> sorts the partition table entries and then deletes partition 2 from the newly-sorted list; but <code>sgdisk -d 2 -s</code> deletes the original partition 2 and then sorts the modified partition table. </p>
<p> Error checking and opportunities to correct mistakes in <code>sgdisk</code> are minimal. Although the program endeavors to keep the GPT data structures legal, it does not prompt for verification before performing its actions. Unless you require a command-line-driven program, you should use the interactive <code>gdisk</code> instead of <code>sgdisk</code>, since <code>gdisk</code> allows you to quit without saving your changes, should you make a mistake. </p>
<p> Although <code>sgdisk</code> is based on the same partition-manipulation code as <code>gdisk</code>, <code>sgdisk</code> implements fewer features than its interactive sibling. Options available in <code>sgdisk</code> are: </p>
<dl>
<dt><code>-a, &#8211;set-alignment=value</code></p>
<dd>Set the sector alignment multiple. GPT fdisk aligns the start of partitions to sectors that are multiples of this value, which defaults to 1 MiB (2048 on disks with 512-byte sectors) on freshly formatted disks. This alignment value is necessary to obtain optimum performance with Western Digital Advanced Format and similar drives with larger physical than logical sector sizes, with some types of RAID arrays, and with SSD devices. </p>
<dt><code>-A, &#8211;attributes=list|[partnum:show|or|nand|xor|=|set|clear|toggle|get[:bitnum|hexbitmask]]</code></p>
<dd>View or set partition attributes. Use <i>list</i> to see defined (known) attribute values. Omit the partition number (and even the device filename) when using this option. The others require a partition number. The <i>show</i> and <i>get</i> options show the current attribute settings (all attributes or for a particular bit, respectively). The <i>or</i>, <i>nand</i>, <i>xor</i>, <i>=</i>, <i>set</i>, <i>clear</i>, and <i>toggle</i> options enable you to change the attribute bit value. The <i>set</i>, <i>clear</i>, <i>toggle</i>, and <i>get</i> options work on a bit number; the others work on a hexadecimal bit mask. For example, type <code>sgdisk -A 4:set:2 /dev/sdc</code> to set the bit 2 attribute (legacy BIOS bootable) on partition 4 on <i>/dev/sdc</i>. </p>
<dt><code>-b, &#8211;backup=file</code></p>
<dd>Save partition data to a backup file. You can back up your current in-memory partition table to a disk file using this option. The resulting file is a binary file consisting of the protective MBR, the main GPT header, the backup GPT header, and one copy of the partition table, in that order. Note that the backup is of the current in-memory data structures, so if you launch the program, make changes, and then use this option, the backup will reflect your changes. If the GPT data structures are damaged, the backup may not accurately reflect the damaged state; instead, they will reflect GPT fdisk&#8217;s first-pass interpretation of the GPT. </p>
<dt><code>-B, &#8211;byte-swap-name=partnum</code></p>
<dd>Swap the byte order for the name of the specified partition. Some partitioning tools, including GPT fdisk 1.0.7 and earlier, can write the partition name in the wrong byte order on big-endian computers, such as the IBM s390 mainframes and PowerPC-based Macs. This feature corrects this problem. </p>
<dt><code>-c, &#8211;change-name=partnum:name</code></p>
<dd>Change the GPT name of a partition. This name is encoded as a UTF-16 string, but proper entry and display of anything beyond basic ASCII values requires suitable locale and font support. For the most part, Linux ignores the partition name, but it may be important in some OSes. If you want to set a name that includes a space, enclose it in quotation marks, as in <i>sgdisk -c 1:&quot;Sample Name&quot; /dev/sdb</i>. Note that the GPT name of a partition is distinct from the filesystem name, which is encoded in the filesystem&#8217;s data structures. </p>
<dt><code>-C, &#8211;recompute-chs</code></p>
<dd>Recompute CHS values in protective or hybrid MBR. This option can sometimes help if a disk utility, OS, or BIOS doesn&#8217;t like the CHS values used by the partitions in the protective or hybrid MBR. In particular, the GPT specification requires a CHS value of 0xFFFFFF for over-8GiB partitions, but this value is technically illegal by the usual standards. Some BIOSes hang if they encounter this value. This option will recompute a more normal CHS value &#8212; 0xFEFFFF for over-8GiB partitions, enabling these BIOSes to boot. </p>
<dt><code>-d, &#8211;delete=partnum</code></p>
<dd>Delete a partition. This action deletes the entry from the partition table but does not disturb the data within the sectors originally allocated to the partition on the disk. If a corresponding hybrid MBR partition exists, <code>gdisk</code> deletes it, as well, and expands any adjacent 0xEE (EFI GPT) MBR protective partition to fill the new free space. </p>
<dt><code>-D, &#8211;display-alignment</code></p>
<dd>Display current sector alignment value. Partitions will be created on multiples of the sector value reported by this option. You can change the alignment value with the -a option. </p>
<dt><code>-e, &#8211;move-second-header</code></p>
<dd>Move backup GPT data structures to the end of the disk. Use this option if you&#8217;ve added disks to a RAID array, thus creating a virtual disk with space that follows the backup GPT data structures. This command moves the backup GPT data structures to the end of the disk, where they belong. </p>
<dt><code>-E, &#8211;end-of-largest</code></p>
<dd>Displays the sector number of the end of the largest available block of sectors on the disk. A script may store this value and pass it back as part of <i>-n</i>&#8216;s option to create a partition. If no unallocated sectors are available, this function returns the value 0. </p>
<dt><code>-f, &#8211;first-in-largest</code></p>
<dd>Displays the sector number of the start of the largest available block of sectors on the disk. A script may store this value and pass it back as part of <i>-n</i>&#8216;s option to create a partition. If no unallocated sectors are available, this function returns the value 0. Note that this parameter is blind to partition alignment; when you actually create a partition, its start point might be changed from this value. </p>
<dt><code>-F, &#8211;first-aligned-in-largest</code></p>
<dd>Similar to <i>-f</i> (<i>&#8211;first-in-largest</i>), except returns the sector number with the current alignment correction applied. Use this function if you need to compute the actual partition start point rather than a theoretical start point or the actual start point if you set the alignment value to 1. </p>
<dt><code>-g, &#8211;mbrtogpt</code></p>
<dd>Convert an MBR or BSD disklabel disk to a GPT disk. As a safety measure, use of this option is required on MBR or BSD disklabel disks if you intend to save your changes, in order to prevent accidentally damaging such disks. </p>
<dt><code>-G, &#8211;randomize-guids</code></p>
<dd>Randomize the disk&#8217;s GUID and all partitions&#8217; unique GUIDs (but not their partition type code GUIDs). This function may be used after cloning a disk in order to render all GUIDs once again unique. </p>
<dt><code>-h, &#8211;hybrid</code></p>
<dd>Create a hybrid MBR. This option takes from one to three partition numbers, separated by colons, as arguments. You may optionally specify a final partition &quot;EE&quot; to indicate that the EFI GPT (type 0xEE) should be placed last in the table, otherwise it will be placed first, followed by the partition(s) you specify. Their type codes are based on the GPT fdisk type codes divided by 0x0100, which is usually correct for Windows partitions. If the active/bootable flag should be set, you must do so in another program, such as <code>fdisk</code>. The <code>gdisk</code> program offers additional hybrid MBR creation options. </p>
<dt><code>-i, &#8211;info=partnum</code></p>
<dd>Show detailed partition information. The summary information produced by the <i>-p</i> command necessarily omits many details, such as the partition&#8217;s unique GUID and the translation of <code>sgdisk</code>&#8216;s internal partition type code to a plain type name. The <i>-i</i> option displays this information for a single partition. </p>
<dt><code>-j, &#8211;adjust-main-table=sector</code></p>
<dd>Adjust the location of the main partition table. This value is normally 2, but it may need to be increased in some cases, such as when a system-on-chip (SoC) is hard-coded to read boot code from sector 2. I recommend against adjusting this value unless doing so is absolutely necessary. </p>
<dt><code>-l, &#8211;load-backup=file</code></p>
<dd>Load partition data from a backup file. This option is the reverse of the <i>-b</i> option. Note that restoring partition data from anything but the original disk is not recommended. This option will work even if the disk&#8217;s original partition table is bad; however, most other options on the same command line will be ignored. </p>
<dt><code>-L, &#8211;list-types</code></p>
<dd>Display a summary of partition types. GPT uses a GUID to identify partition types for particular OSes and purposes. For ease of data entry, <code>sgdisk</code> compresses these into two-byte (four-digit hexadecimal) values that are related to their equivalent MBR codes. Specifically, the MBR code is multiplied by hexadecimal 0x0100. For instance, the code for Linux swap space in MBR is 0x82, and it&#8217;s 0x8200 in <code>gdisk</code>. A one-to-one correspondence is impossible, though. Most notably, the codes for all varieties of FAT and NTFS partition correspond to a single GPT code (entered as 0x0700 in <code>sgdisk</code>). Some OSes use a single MBR code but employ many more codes in GPT. For these, <code>sgdisk</code> adds code numbers sequentially, such as 0xa500 for a FreeBSD disklabel, 0xa501 for FreeBSD boot, 0xa502 for FreeBSD swap, and so on. Note that these two-byte codes are unique to <code>gdisk</code> and <code>sgdisk</code>. This option does not require you to specify a valid disk device filename. </p>
<dt><code>-m, &#8211;gpttombr</code></p>
<dd>Convert disk from GPT to MBR form. This option takes from one to four partition numbers, separated by colons, as arguments. Their type codes are based on the GPT fdisk type codes divided by 0x0100. If the active/bootable flag should be set, you must do so in another program, such as <code>fdisk</code>. The <code>gdisk</code> program offers additional MBR conversion options. It is not possible to convert more than four partitions from GPT to MBR form or to convert partitions that start above the 2TiB mark or that are larger than 2TiB. </p>
<dt><code>-n, &#8211;new=partnum:start:end</code></p>
<dd>Create a new partition. You enter a partition number, starting sector, and an ending sector. Both start and end sectors can be specified in absolute terms as sector numbers or as positions measured in kibibytes (K), mebibytes (M), gibibytes (G), tebibytes (T), or pebibytes (P); for instance, <i></i><code>40M</code> specifies a position 40MiB from the start of the disk. You can specify locations relative to the start or end of the specified default range by preceding the number by a &#8216;+&#8217; or &#8216;-&#8216; symbol, as in <i></i><code>+2G</code> to specify a point 2GiB after the default start sector, or <i></i><code>-200M</code> to specify a point 200MiB before the last available sector. A start or end value of 0 specifies the default value, which is the start of the largest available block for the start sector and the end of the same block for the end sector. A partnum value of 0 causes the program to use the first available partition number. Subsequent uses of the <i>-A</i> (<i>&#8211;attributes</i>), <i>-c</i> (<i>&#8211;change-name</i>), <i>-t</i> (<i>&#8211;typecode</i>), and <i>-u</i> (<i>&#8211;partition-guid</i>) options may also use <i>0</i> to refer to the same partition. </p>
<dt><code>-N, &#8211;largest-new=num</code></p>
<dd>Create a new partition that fills the largest available block of space on the disk. You can use the <i>-a</i> (<i>&#8211;set-alignment</i>) option to adjust the alignment, if desired. A num value of 0 causes the program to use the first available partition number. </p>
<dt><code>-o, &#8211;clear</code></p>
<dd>Clear out all partition data. This includes GPT header data, all partition definitions, and the protective MBR. Note that this operation will, like most other operations, fail on a damaged disk. If you want to prepare a disk you know to be damaged for GPT use, you should first wipe it with -Z and then partition it normally. This option will work even if the disk&#8217;s original partition table is bad; however, most other options on the same command line will be ignored. </p>
<dt><code>-O, &#8211;print-mbr</code></p>
<dd>Display basic <i>MBR</i> partition summary data. This includes partition numbers, starting and ending sector numbers, partition sizes, MBR partition types codes, and partition names. This option is useful mainly for diagnosing partition table problems, particularly on disks with hybrid MBRs. </p>
<dt><code>-p, &#8211;print</code></p>
<dd>Display basic GPT partition summary data. This includes partition numbers, starting and ending sector numbers, partition sizes, <code>sgdisk</code>&#8216;s partition types codes, and partition names. For additional information, use the <i>-i</i> (<i>&#8211;info</i>) option. </p>
<dt><code>-P, &#8211;pretend</code></p>
<dd>Pretend to make specified changes. In-memory GPT data structures are altered according to other parameters, but changes are not written to disk. </p>
<dt><code>-r, &#8211;transpose</code></p>
<dd>Swap two partitions&#8217; entries in the partition table. One or both partitions may be empty, although swapping two empty partitions is pointless. For instance, if partitions 1-4 are defined, transposing 1 and 5 results in a table with partitions numbered from 2-5. Transposing partitions in this way has no effect on their disk space allocation; it only alters their order in the partition table. </p>
<dt><code>-R, &#8211;replicate=second_device_filename</code></p>
<dd>Replicate the main device&#8217;s partition table on the specified second device. Note that the replicated partition table is an exact copy, including all GUIDs; if the device should have its own unique GUIDs, you should use the -G option on the new disk. </p>
<dt><code>-s, &#8211;sort</code></p>
<dd>Sort partition entries. GPT partition numbers need not match the order of partitions on the disk. If you want them to match, you can use this option. Note that some partitioning utilities sort partitions whenever they make changes. Such changes will be reflected in your device filenames, so you may need to edit <i>/etc/fstab</i> if you use this option. </p>
<dt><code>-t, &#8211;typecode=partnum:{hexcode|GUID}</code></p>
<dd>Change a single partition&#8217;s type code. You enter the type code using either a two-byte hexadecimal number, as described earlier, or a fully-specified GUID value, such as EBD0A0A2-B9E5-4433-87C0-68B6B72699C7. </p>
<dt><code>-T, &#8211;transform-bsd=partnum</code></p>
<dd>Transform BSD partitions into GPT partitions. This option works on BSD disklabels held within GPT (or converted MBR) partitions. Converted partitions&#8217; type codes are likely to need manual adjustment. <code>sgdisk</code> will attempt to convert BSD disklabels stored on the main disk when launched, but this conversion is likely to produce first and/or last partitions that are unusable. The many BSD variants means that the probability of <code>sgdisk</code> being unable to convert a BSD disklabel is high compared to the likelihood of problems with an MBR conversion. </p>
<dt><code>-u, &#8211;partition-guid=partnum:guid</code></p>
<dd>Set the partition unique GUID for an individual partition. The GUID may be a complete GUID or &#8216;R&#8217; to set a random GUID. </p>
<dt><code>-U, &#8211;disk-guid=guid</code></p>
<dd>Set the GUID for the disk. The GUID may be a complete GUID or &#8216;R&#8217; to set a random GUID. </p>
<dt><code>&#8211;usage</code></p>
<dd>Print a brief summary of available options. </p>
<dt><code>-v, &#8211;verify</code></p>
<dd>Verify disk. This option checks for a variety of problems, such as incorrect CRCs and mismatched main and backup data. This option does not automatically correct most problems, though; for that, you must use options on the recovery &amp; transformation menu. If no problems are found, this command displays a summary of unallocated disk space. This option will work even if the disk&#8217;s original partition table is bad; however, most other options on the same command line will be ignored. </p>
<dt><code>-V, &#8211;version</code></p>
<dd>Display program version information. This option may be used without specifying a device filename. </p>
<dt><code>-z, &#8211;zap</code></p>
<dd>Zap (destroy) the GPT data structures and then exit. Use this option if you want to repartition a GPT disk using <code>fdisk</code> or some other GPT-unaware program. This option destroys only the GPT data structures; it leaves the MBR intact. This makes it useful for wiping out GPT data structures after a disk has been repartitioned for MBR using a GPT-unaware utility; however, there&#8217;s a risk that it will damage boot loaders or even the start of the first or end of the last MBR partition. If you use it on a valid GPT disk, the MBR will be left with an inappropriate EFI GPT (0xEE) partition definition, which you can delete using another utility. </p>
<dt><code>-Z, &#8211;zap-all</code></p>
<dd>Zap (destroy) the GPT and MBR data structures and then exit. This option works much like <i>-z</i>, but as it wipes the MBR as well as the GPT, it&#8217;s more suitable if you want to repartition a disk after using this option, and completely unsuitable if you&#8217;ve already repartitioned the disk. </p>
<dt><code>-?, &#8211;help</code></p>
<dd>Print a summary of options. </p>
</dl>
<h2>Return Values</h2>
<p><code>sgdisk</code> returns various values depending on its success or failure: </p>
<dl>
<dt><code>0</code></p>
<dd>Normal program execution </p>
<dt><code>1</code></p>
<dd>Too few arguments </p>
<dt><code>2</code></p>
<dd>An error occurred while reading the partition table </p>
<dt><code>3</code></p>
<dd>Non-GPT disk detected and no <i>-g</i> option, but operation requires a write action </p>
<dt><code>4</code></p>
<dd>An error prevented saving changes </p>
<dt><code>5</code></p>
<dd>An error occurred while reading standard input (should never occur with sgdisk, but may with gdisk) </p>
<dt><code>8</code></p>
<dd>Disk replication operation (-R) failed </p>
</dl>
<h2>Bugs</h2>
<p>Known bugs and limitations include:</p>
<dl>
<dt><code>*</code></p>
<dd>The program compiles correctly only on Linux, FreeBSD, and Mac OS X. Linux versions for x86-64 (64-bit), x86 (32-bit), and PowerPC (32-bit) have been tested, with the x86-64 version having seen the most testing.</p>
<dt><code>*</code></p>
<dd>The FreeBSD version of the program can&#8217;t write changes to the partition table to a disk when existing partitions on that disk are mounted. (The same problem exists with many other FreeBSD utilities, such as <code>gpt</code>, <code>fdisk</code>, and <code>dd</code>.) This limitation can be overcome by typing <code>sysctl kern.geom.debugflags=16</code> at a shell prompt.</p>
<dt><code>*</code></p>
<dd>The fields used to display the start and end sector numbers for partitions in the <i>-p</i> option are 14 characters wide. This translates to a limitation of about 45 PiB. On larger disks, the displayed columns will go out of alignment. </p>
<pre><code>*


The program can load only up to 128 partitions (4 primary partitions and
124 logical partitions) when converting from MBR format. This limit can
be raised by changing the #define MAX_MBR_PARTS line in the
basicmbr.h source code file and recompiling; however, such a change
will require using a larger-than-normal partition table. (The limit
of 128 partitions was chosen because that number equals the 128 partitions
supported by the most common partition table size.)</code></pre>
<dt><code>*</code></p>
<dd>Converting from MBR format sometimes fails because of insufficient space at the start or (more commonly) the end of the disk. Resizing the partition table (using the &#8216;s&#8217; option in the experts&#8217; menu) can sometimes overcome this problem; however, in extreme cases it may be necessary to resize a partition using GNU Parted or a similar tool prior to conversion with <code>gdisk</code>.</p>
<dt><code>*</code></p>
<dd>MBR conversions work only if the disk has correct LBA partition descriptors. These descriptors should be present on any disk over 8 GiB in size or on smaller disks partitioned with any but very ancient software.</p>
<dt><code>*</code></p>
<dd>BSD disklabel support can create first and/or last partitions that overlap with the GPT data structures. This can sometimes be compensated by adjusting the partition table size, but in extreme cases the affected partition(s) may need to be deleted.</p>
<dt><code>*</code></p>
<dd>Because of the highly variable nature of BSD disklabel structures, conversions from this form may be unreliable &#8212; partitions may be dropped, converted in a way that creates overlaps with other partitions, or converted with incorrect start or end values. Use this feature with caution!</p>
<dt><code>*</code></p>
<dd>Booting after converting an MBR or BSD disklabel disk is likely to be disrupted. Sometimes re-installing a boot loader will fix the problem, but other times you may need to switch boot loaders. Except on EFI-based platforms, Windows through at least Windows 7 RC doesn&#8217;t support booting from GPT disks. Creating a hybrid MBR (using the &#8216;h&#8217; option on the recovery &amp; transformation menu) or abandoning GPT in favor of MBR may be your only options in this case. </p>
<h2>Authors</h2>
<p>Primary author: Roderick W. Smith (rodsmith [at] rodsbooks.com) </p>
<p> Contributors: </p>
<p> * Yves Blusseau (1otnwmz02 [at] sneakemail.com) </p>
<p> * David Hubbard (david.c.hubbard [at] gmail.com) </p>
<p> * Justin Maggard (justin.maggard [at] netgear.com) </p>
<p> * Dwight Schauer (das [at] teegra.net) </p>
<p> * Florian Zumbiehl (florz [at] florz.de)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8), <code><a href="/docs/linux/man/8-cgdisk/">cgdisk</a></code>(8), <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-gdisk/">gdisk</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8), <code><a href="/docs/linux/man/8-fixparts/">fixparts</a></code>(8). <i><a rel="nofollow" href="http://en.wikipedia.org/wiki/GUID_Partition_Table">http://en.wikipedia.org/wiki/GUID_Partition_Table</a></i> <i><a rel="nofollow" href="http://developer.apple.com/technotes/tn2006/tn2166.html">http://developer.apple.com/technotes/tn2006/tn2166.html</a></i> <i><a rel="nofollow" href="http://www.rodsbooks.com/gdisk/">http://www.rodsbooks.com/gdisk/</a></i> </p>
<h2>Availability</h2>
<p>The <code>sgdisk</code> command is part of the <i>GPT fdisk</i> package and is available from Rod Smith.</p>
