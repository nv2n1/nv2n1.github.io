---
title: "gdisk(8)"
name: "gdisk"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gdisk/"
description: "gdisk – Interactive GUID partition table (GPT) manipulator"
---

<p>gdisk &#8211; Interactive GUID partition table (GPT) manipulator</p>
<h2>Synopsis</h2>
<p><code>gdisk </code> [ -l ] <i>device</i> </p>
<h2>Description</h2>
<p>GPT fdisk (aka <code>gdisk</code>) is a text-mode menu-driven program for creation and manipulation of partition tables. It will automatically convert an old-style Master Boot Record (MBR) partition table or BSD disklabel stored without an MBR carrier partition to the newer Globally Unique Identifier (GUID) Partition Table (GPT) format, or will load a GUID partition table. When used with the <i>-l</i> command-line option, the program displays the current partition table and then exits. GPT fdisk operates mainly on the GPT headers and partition tables; however, it can and will generate a fresh protective MBR, when required. (Any boot loader code in the protective MBR will not be disturbed.) If you&#8217;ve created an unusual protective MBR, such as a hybrid MBR created by <code>gptsync</code> or <code>gdisk</code>&#8216;s own hybrid MBR creation feature, this should not be disturbed by most ordinary actions. Some advanced data recovery options require you to understand the distinctions between the main and backup data, as well as between the GPT headers and the partition tables. For information on MBR vs. GPT, as well as GPT terminology and structure, see the extended <code>gdisk</code> documentation at <i><a rel="nofollow" href="http://www.rodsbooks.com/gdisk/">http://www.rodsbooks.com/gdisk/</a></i> or consult Wikipedia. The <code>gdisk</code> program employs a user interface similar to that of Linux&#8217;s <code>fdisk</code>, but <code>gdisk</code> modifies GPT partitions. It also has the capability of transforming MBR partitions or BSD disklabels into GPT partitions. Like the original <code>fdisk</code> program, <code>gdisk</code> does not modify disk structures until you explicitly write them to disk, so if you make a mistake, you can exit from the program with the &#8216;q&#8217; option to leave your partitions unmodified. Ordinarily, <code>gdisk</code> operates on disk device files, such as <i>/dev/sda</i> or <i>/dev/hda</i> under Linux, <i>/dev/disk0</i> under Mac OS X, or <i>/dev/ad0</i> or <i>/dev/da0</i> under FreeBSD. The program can also operate on disk image files, which can be either copies of whole disks (made with <code>dd</code>, for instance) or raw disk images used by emulators such as QEMU or VMWare. Note that only <i>raw</i> disk images are supported; <code>gdisk</code> cannot work on compressed or other advanced disk image formats. The MBR partitioning system uses a combination of cylinder/head/sector (CHS) addressing and logical block addressing (LBA). The former is klunky and limiting. GPT drops CHS addressing and uses 64-bit LBA mode exclusively. Thus, GPT data structures, and therefore <code>gdisk</code>, do not need to deal with CHS geometries and all the problems they create. Users of <code>fdisk</code> will note that <code>gdisk</code> lacks the options and limitations associated with CHS geometries. For best results, you should use an OS-specific partition table program whenever possible. For example, you should make Mac OS X partitions with the Mac OS X Disk Utility program and Linux partitions with the Linux <code>gdisk</code> or GNU Parted program. Upon start, <code>gdisk</code> attempts to identify the partition type in use on the disk. If it finds valid GPT data, <code>gdisk</code> will use it. If <code>gdisk</code> finds a valid MBR or BSD disklabel but no GPT data, it will attempt to convert the MBR or disklabel into GPT form. (BSD disklabels are likely to have unusable first and/or final partitions because they overlap with the GPT data structures, though.) GPT fdisk can identify, but not use data in, Apple Partition Map (APM) disks, which are used on 680&#215;0- and PowerPC-based Macintoshes. Upon exiting with the &#8216;w&#8217; option, <code>gdisk</code> replaces the MBR or disklabel with a GPT. <i>This action is potentially dangerous!</i> Your system may become unbootable, and partition type codes may become corrupted if the disk uses unrecognized type codes. Boot problems are particularly likely if you&#8217;re multi-booting with any GPT-unaware OS. If you mistakenly launch <code>gdisk</code> on an MBR disk, you can safely exit the program without making any changes by using the &#8216;q&#8217; option. The MBR-to-GPT conversion will leave at least one gap in the partition numbering if the original MBR used logical partitions. These gaps are harmless, but you can eliminate them by using the &#8216;s&#8217; option, if you like. (Doing this may require you to update your <i>/etc/fstab</i> file.) When creating a fresh partition table, certain considerations may be in order:</p>
<dl>
<dt><code>*</code></p>
<dd>For data (non-boot) disks, and for boot disks used on BIOS-based computers with GRUB as the boot loader, partitions may be created in whatever order and in whatever sizes are desired.</p>
<dt><code>*</code></p>
<dd>Boot disks for EFI-based systems require an <i>EFI System Partition</i> (<code>gdisk</code> internal code 0xEF00) formatted as FAT-32. I recommended making this partition 550 MiB. (Smaller ESPs are common, but some EFIs have flaky FAT drivers that necessitate a larger partition for reliable operation.) Boot-related files are stored here. (Note that GNU Parted identifies such partitions as having the &quot;boot flag&quot; set.)</p>
<dt><code>*</code></p>
<dd>Some boot loaders for BIOS-based systems make use of a <i>BIOS Boot Partition</i> (<code>gdisk</code> internal code 0xEF02), in which the secondary boot loader is stored, possibly without the benefit of a filesystem. (GRUB2 may optionally use such a partition.) This partition can typically be quite small (roughly 32 to 200 KiB, although 1 MiB is more common in practice), but you should consult your boot loader documentation for details.</p>
<dt><code>*</code></p>
<dd>If Windows is to boot from a GPT disk, a partition of type <i>Microsoft Reserved</i> (<code>gdisk</code> internal code 0x0C01) is recommended. This partition should be about 128 MiB in size. It ordinarily follows the EFI System Partition and immediately precedes the Windows data partitions. (Note that old versions of GNU Parted create all FAT partitions as this type, which actually makes the partition unusable for normal file storage in both Windows and Mac OS X.)</p>
<dt><code>*</code></p>
<dd>Some OSes&#8217; GPT utilities create some blank space (typically 128 MiB) after each partition. The intent is to enable future disk utilities to use this space. Such free space is not required of GPT disks, but creating it may help in future disk maintenance. You can use GPT fdisk&#8217;s relative partition positioning option (specifying the starting sector as &#8216;+128M&#8217;, for instance) to simplify creating such gaps. </p>
<h2>Options</h2>
<dl>
<dt><code>-l</code></p>
<dd>List the partition table for the specified device and then exits.</dl>
<p> Most interactions with <code>gdisk</code> occur with its interactive text-mode menus. Three menus exist: the main menu, the recovery &amp; transformation menu, and the experts&#8217; menu. The main menu provides the functions that are most likely to be useful for typical partitioning tasks, such as creating and deleting partitions, changing partition type codes, and so on. Specific functions are: </p>
<dl>
<dt><code>b</code></p>
<dd>Save partition data to a backup file. You can back up your current in-memory partition table to a disk file using this option. The resulting file is a binary file consisting of the protective MBR, the main GPT header, the backup GPT header, and one copy of the partition table, in that order. Note that the backup is of the current in-memory data structures, so if you launch the program, make changes, and then use this option, the backup will reflect your changes. Note also that the restore option is on the recovery &amp; transformation menu; the backup option is on the main menu to encourage its use. </p>
<dt><code>c</code></p>
<dd>Change the GPT name of a partition. This name is encoded as a UTF-16 string, but proper entry and display of anything beyond basic ASCII values requires suitable locale and font support. For the most part, Linux ignores the partition name, but it may be important in some OSes. GPT fdisk sets a default name based on the partition type code. Note that the GPT partition name is different from the filesystem name, which is encoded in the filesystem&#8217;s data structures. </p>
<dt><code>d</code></p>
<dd>Delete a partition. This action deletes the entry from the partition table but does not disturb the data within the sectors originally allocated to the partition on the disk. If a corresponding hybrid MBR partition exists, <code>gdisk</code> deletes it, as well, and expands any adjacent 0xEE (EFI GPT) MBR protective partition to fill the new free space. </p>
<dt><code>i</code></p>
<dd>Show detailed partition information. The summary information produced by the &#8216;p&#8217; command necessarily omits many details, such as the partition&#8217;s unique GUID and the translation of <code>gdisk</code>&#8216;s internal partition type code to a plain type name. The &#8216;i&#8217; option displays this information for a single partition. </p>
<dt><code>l</code></p>
<dd>Display a summary of partition types. GPT uses a GUID to identify partition types for particular OSes and purposes. For ease of data entry, <code>gdisk</code> compresses these into two-byte (four-digit hexadecimal) values that are related to their equivalent MBR codes. Specifically, the MBR code is multiplied by hexadecimal 0x0100. For instance, the code for Linux swap space in MBR is 0x82, and it&#8217;s 0x8200 in <code>gdisk</code>. A one-to-one correspondence is impossible, though. Most notably, the codes for all varieties of FAT and NTFS partition correspond to a single GPT code (entered as 0x0700 in <code>gdisk</code>). Some OSes use a single MBR code but employ many more codes in GPT. For these, <code>gdisk</code> adds code numbers sequentially, such as 0xa500 for a FreeBSD disklabel, 0xa501 for FreeBSD boot, 0xa502 for FreeBSD swap, and so on. Note that these two-byte codes are unique to <code>gdisk</code>. The type code list may optionally be filtered by a search string; for instance, entering <i></i><code>linux</code> shows only partition type codes with descriptions that include the string <i>Linux</i>. This search is performed case-insensitively. </p>
<dt><code>n</code></p>
<dd>Create a new partition. This command is modeled after the equivalent <code>fdisk</code> option, although some differences exist. You enter a partition number, starting sector, and an ending sector. Both start and end sectors can be specified in absolute terms as sector numbers or as positions measured in kibibytes (K), mebibytes (M), gibibytes (G), tebibytes (T), or pebibytes (P); for instance, <i></i><code>40M</code> specifies a position 40MiB from the start of the disk. You can specify locations relative to the start or end of the specified default range by preceding the number by a &#8216;+&#8217; or &#8216;-&#8216; symbol, as in <i></i><code>+2G</code> to specify a point 2GiB after the default start sector, or <i></i><code>-200M</code> to specify a point 200MiB before the last available sector. Pressing the Enter key with no input specifies the default value, which is the start of the largest available block for the start sector and the end of the same block for the end sector. </p>
<dt><code>o</code></p>
<dd>Clear out all partition data. This includes GPT header data, all partition definitions, and the protective MBR. The sector alignment is reset to the default (1 MiB, or 2048 sectors on a disk with 512-byte sectors). </p>
<dt><code>p</code></p>
<dd>Display basic partition summary data. This includes partition numbers, starting and ending sector numbers, partition sizes, <code>gdisk</code>&#8216;s partition types codes, and partition names. For additional information, use the &#8216;i&#8217; command. </p>
<dt><code>q</code></p>
<dd>Quit from the program <i>without saving your changes</i>. Use this option if you just wanted to view information or if you make a mistake and want to back out of all your changes. </p>
<dt><code>r</code></p>
<dd>Enter the recovery &amp; transformation menu. This menu includes emergency recovery options (to fix damaged GPT data structures) and options to transform to or from other partitioning systems, including creating hybrid MBRs. </p>
<dt><code>s</code></p>
<dd>Sort partition entries. GPT partition numbers need not match the order of partitions on the disk. If you want them to match, you can use this option. Note that some partitioning utilities sort partitions whenever they make changes. Such changes will be reflected in your device filenames, so you may need to edit <i>/etc/fstab</i> if you use this option. </p>
<dt><code>t</code></p>
<dd>Change a single partition&#8217;s type code. You enter the type code using a two-byte hexadecimal number, as described earlier. You may also enter a GUID directly, if you have one and <code>gdisk</code> doesn&#8217;t know it. </p>
<dt><code>v</code></p>
<dd>Verify disk. This option checks for a variety of problems, such as incorrect CRCs and mismatched main and backup data. This option does not automatically correct most problems, though; for that, you must use options on the recovery &amp; transformation menu. If no problems are found, this command displays a summary of unallocated disk space. </p>
<dt><code>w</code></p>
<dd>Write data. Use this command to save your changes. </p>
<dt><code>x</code></p>
<dd>Enter the experts&#8217; menu. Using this option provides access to features you can use to get into even more trouble than the main menu allows.</dl>
<dl>
<dt><code>?</code></p>
<dd>Print the menu. Type this command (or any other unrecognized command) to see a summary of available options. </p>
</dl>
<p> The second <code>gdisk</code> menu is the recovery &amp; transformation menu, which provides access to data recovery options and features related to the transformation of partitions between partitioning schemes (converting BSD disklabels into GPT partitions or creating hybrid MBRs, for instance). A few options on this menu duplicate functionality on the main menu, for the sake of convenience. The options on this menu are: </p>
<dl>
<dt><code>b</code></p>
<dd>Rebuild GPT header from backup. You can use the backup GPT header to rebuild the main GPT header with this option. It&#8217;s likely to be useful if your main GPT header was damaged or destroyed (say, by sloppy use of <code>dd</code>). </p>
<dt><code>c</code></p>
<dd>Load backup partition table. Ordinarily, <code>gdisk</code> uses only the main partition table (although the backup&#8217;s integrity is checked when you launch the program). If the main partition table has been damaged, you can use this option to load the backup from disk and use it instead. Note that this will almost certainly produce no or strange partition entries if you&#8217;ve just converted an MBR disk to GPT format, since there will be no backup partition table on disk. </p>
<dt><code>d</code></p>
<dd>Use main GPT header and rebuild the backup. This option is likely to be useful if the backup GPT header has been damaged or destroyed. </p>
<dt><code>e</code></p>
<dd>Load main partition table. This option reloads the main partition table from disk. It&#8217;s only likely to be useful if you&#8217;ve tried to use the backup partition table (via &#8216;c&#8217;) but it&#8217;s in worse shape then the main partition table. </p>
<dt><code>f</code></p>
<dd>Load MBR and build fresh GPT from it. Use this option if your GPT is corrupt or conflicts with the MBR and you want to use the MBR as the basis for a new set of GPT partitions. </p>
<dt><code>g</code></p>
<dd>Convert GPT into MBR and exit. This option converts as many partitions as possible into MBR form, destroys the GPT data structures, saves the new MBR, and exits. Use this option if you&#8217;ve tried GPT and find that MBR works better for you. Note that this function generates up to four primary MBR partitions or three primary partitions and as many logical partitions as can be generated. Each logical partition requires at least one unallocated block immediately before its first block. Therefore, it may be possible to convert a maximum of four partitions on disks with tightly-packed partitions; however, if free space was inserted between partitions when they were created, and if the disk is under 2 TiB in size, it should be possible to convert all the partitions to MBR form. See also the &#8216;h&#8217; option. </p>
<dt><code>h</code></p>
<dd>Create a hybrid MBR. This is an ugly workaround that enables GPT-unaware OSes, or those that can&#8217;t boot from a GPT disk, to access up to three of the partitions on the disk by creating MBR entries for them. Note that these hybrid MBR entries can easily go out of sync with the GPT entries, particularly when hybrid-unaware GPT utilities are used to edit the disk. Thus, you may need to re-create the hybrid MBR if you use such tools. Unlike the &#8216;g&#8217; option, this option does not support converting any partitions into MBR logical partitions. </p>
<dt><code>i</code></p>
<dd>Show detailed partition information. This option is identical to the &#8216;i&#8217; option on the main menu. </p>
<dt><code>l</code></p>
<dd>Load partition data from a backup file. This option is the reverse of the &#8216;b&#8217; option on the main menu. Note that restoring partition data from anything but the original disk is not recommended. </p>
<dt><code>m</code></p>
<dd>Return to the main menu. This option enables you to enter main-menu commands. </p>
<dt><code>o</code></p>
<dd>Print protective MBR data. You can see a summary of the protective MBR&#8217;s partitions with this option. This may enable you to spot glaring problems or help identify the partitions in a hybrid MBR. </p>
<dt><code>p</code></p>
<dd>Print the partition table. This option is identical to the &#8216;p&#8217; option in the main menu. </p>
<dt><code>q</code></p>
<dd>Quit without saving changes. This option is identical to the &#8216;q&#8217; option in the main menu. </p>
<dt><code>t</code></p>
<dd>Transform BSD partitions into GPT partitions. This option works on BSD disklabels held within GPT (or converted MBR) partitions. Converted partitions&#8217; type codes are likely to need manual adjustment. <code>gdisk</code> will attempt to convert BSD disklabels stored on the main disk when launched, but this conversion is likely to produce first and/or last partitions that are unusable. The many BSD variants means that the probability of <code>gdisk</code> being unable to convert a BSD disklabel is high compared to the likelihood of problems with an MBR conversion. </p>
<dt><code>v</code></p>
<dd>Verify disk. This option is identical to the &#8216;v&#8217; option in the main menu. </p>
<dt><code>w</code></p>
<dd>Write table to disk and exit. This option is identical to the &#8216;w&#8217; option in the main menu. </p>
<dt><code>x</code></p>
<dd>Enter the experts&#8217; menu. This option is identical to the &#8216;x&#8217; option in the main menu. </p>
<dt><code>?</code></p>
<dd>Print the menu. This option (or any unrecognized entry) displays a summary of the menu options. </p>
</dl>
<p> The third <code>gdisk</code> menu is the experts&#8217; menu. This menu provides advanced options that aren&#8217;t closely related to recovery or transformation between partitioning systems. Its options are: </p>
<dl>
<dt><code>a</code></p>
<dd>Set attributes. GPT provides a 64-bit attributes field that can be used to set features for each partition. <code>gdisk</code> supports four attributes: <i>system partition</i>, <i>read-only</i>, <i>hidden</i>, and <i>do not automount</i>. You can set other attributes, but their numbers aren&#8217;t translated into anything useful. In practice, most OSes seem to ignore these attributes. </p>
<dt><code>b</code></p>
<dd>Swap the byte order for the name of the specified partition. Some partitioning tools, including GPT fdisk 1.0.7 and earlier, can write the partition name in the wrong byte order on big-endian computers, such as the IBM s390 mainframes and PowerPC-based Macs. This feature corrects this problem. </p>
<dt><code>c</code></p>
<dd>Change partition GUID. You can enter a custom unique GUID for a partition using this option. (Note this refers to the GUID that uniquely identifies a partition, not to its type code, which you can change with the &#8216;t&#8217; main-menu option.) Ordinarily, <code>gdisk</code> assigns this number randomly; however, you might want to adjust the number manually if you&#8217;ve wound up with the same GUID on two partitions because of buggy GUID assignments (hopefully not in <code>gdisk</code>) or sheer incredible coincidence. </p>
<dt><code>d</code></p>
<dd>Display the sector alignment value. See the description of the &#8216;l&#8217; option for more details. </p>
<dt><code>e</code></p>
<dd>Move backup GPT data structures to the end of the disk. Use this command if you&#8217;ve added disks to a RAID array, thus creating a virtual disk with space that follows the backup GPT data structures. This command moves the backup GPT data structures to the end of the disk, where they belong. </p>
<dt><code>f</code></p>
<dd>Randomize the disk&#8217;s GUID and all partitions&#8217; unique GUIDs (but not their partition type code GUIDs). This function may be used after cloning a disk with another utility in order to render all GUIDs once again unique. </p>
<dt><code>g</code></p>
<dd>Change disk GUID. Each disk has a unique GUID code, which <code>gdisk</code> assigns randomly upon creation of the GPT data structures. You can generate a fresh random GUID or enter one manually with this option. </p>
<dt><code>h</code></p>
<dd>Recompute CHS values in protective or hybrid MBR. This option can sometimes help if a disk utility, OS, or BIOS doesn&#8217;t like the CHS values used by the partitions in the protective or hybrid MBR. In particular, the GPT specification requires a CHS value of 0xFFFFFF for over-8GiB partitions, but this value is technically illegal by the usual standards. Some BIOSes hang if they encounter this value. This option will recompute a more normal CHS value &#8212; 0xFEFFFF for over-8GiB partitions, enabling these BIOSes to boot. </p>
<dt><code>i</code></p>
<dd>Show detailed partition information. This option is identical to the &#8216;i&#8217; option on the main menu. </p>
<dt><code>j</code></p>
<dd>Adjust the location of the main partition table. This value is normally 2, but it may need to be increased in some cases, such as when a system-on-chip (SoC) is hard-coded to read boot code from sector 2. I recommend against adjusting this value unless doing so is absolutely necessary. </p>
<dt><code>l</code></p>
<dd>Change the sector alignment value. Disks with more logical sectors per physical sectors (such as modern Advanced Format drives), some RAID configurations, and many SSD devices, can suffer performance problems if partitions are not aligned properly for their internal data structures. On new disks, GPT fdisk attempts to align partitions on 1 MiB boundaries (2048-sectors on disks with 512-byte sectors) by default, which optimizes performance for all of these disk types. On pre-partitioned disks, GPT fdisk attempts to identify the alignment value used on that disk, but will set 8-sector alignment on disks larger than 300 GB even if lesser alignment values are detected. In either case, it can be changed by using this option. </p>
<dt><code>m</code></p>
<dd>Return to the main menu. This option enables you to enter main-menu commands. </p>
<dt><code>n</code></p>
<dd>Create a new protective MBR. Use this option if the current protective MBR is damaged in a way that <code>gdisk</code> doesn&#8217;t automatically detect and correct, or if you want to convert a hybrid MBR into a &quot;pure&quot; GPT with a conventional protective MBR. </p>
<dt><code>o</code></p>
<dd>Print protective MBR data. You can see a summary of the protective MBR&#8217;s partitions with this option. This may enable you to spot glaring problems or help identify the partitions in a hybrid MBR. </p>
<dt><code>p</code></p>
<dd>Print the partition table. This option is identical to the &#8216;p&#8217; option in the main menu. </p>
<dt><code>q</code></p>
<dd>Quit without saving changes. This option is identical to the &#8216;q&#8217; option in the main menu. </p>
<dt><code>r</code></p>
<dd>Enter the recovery &amp; transformations menu. This option is identical to the &#8216;r&#8217; option on the main menu. </p>
<dt><code>s</code></p>
<dd>Resize partition table. The default partition table size is 128 entries. Officially, sizes of less than 16KB (128 entries, given the normal entry size) are unsupported by the GPT specification; however, in practice they seem to work, and can sometimes be useful in converting MBR disks. Larger sizes also work fine. OSes may impose their own limits on the number of partitions, though. </p>
<dt><code>t</code></p>
<dd>Swap two partitions&#8217; entries in the partition table. One partition may be empty. For instance, if partitions 1-4 are defined, transposing 1 and 5 results in a table with partitions numbered from 2-5. Transposing partitions in this way has no effect on their disk space allocation; it only alters their order in the partition table. </p>
<dt><code>u</code></p>
<dd>Replicate the current device&#8217;s partition table on another device. You will be prompted to type the new device&#8217;s filename. After the write operation completes, you can continue editing the original device&#8217;s partition table. Note that the replicated partition table is an exact copy, including all GUIDs; if the device should have its own unique GUIDs, you should use the <code>f</code> option on the new disk. </p>
<dt><code>v</code></p>
<dd>Verify disk. This option is identical to the &#8216;v&#8217; option in the main menu. </p>
<dt><code>z</code></p>
<dd>Zap (destroy) the GPT data structures and exit. Use this option if you want to repartition a GPT disk using <code>fdisk</code> or some other GPT-unaware program. You&#8217;ll be given the choice of preserving the existing MBR, in case it&#8217;s a hybrid MBR with salvageable partitions or if you&#8217;ve already created new MBR partitions and want to erase the remnants of your GPT partitions. <i>If you&#8217;ve already created new MBR partitions, it&#8217;s conceivable that this option will damage the first and/or last MBR partitions!</i> Such an event is unlikely, but could occur if your new MBR partitions overlap the old GPT data structures. </p>
<dt><code>?</code></p>
<dd>Print the menu. This option (or any unrecognized entry) displays a summary of the menu options. </p>
</dl>
<p> In many cases, you can press the Enter key to select a default option when entering data. When only one option is possible, <code>gdisk</code> usually bypasses the prompt entirely.</p>
<h2>Bugs</h2>
<p>Known bugs and limitations include:</p>
<dl>
<dt><code>*</code></p>
<dd>The program compiles correctly only on Linux, FreeBSD, Mac OS X, and Windows. Linux versions for x86-64 (64-bit), x86 (32-bit), and PowerPC (32-bit) have been tested, with the x86-64 version having seen the most testing. Under FreeBSD, 32-bit (x86) and 64-bit (x86-64) versions have been tested. Only 32-bit versions for Mac OS X and Windows have been tested by the author, although I&#8217;ve heard of 64-bit versions being successfully compiled.</p>
<dt><code>*</code></p>
<dd>The FreeBSD version of the program can&#8217;t write changes to the partition table to a disk when existing partitions on that disk are mounted. (The same problem exists with many other FreeBSD utilities, such as <code>gpt</code>, <code>fdisk</code>, and <code>dd</code>.) This limitation can be overcome by typing <code>sysctl kern.geom.debugflags=16</code> at a shell prompt.</p>
<dt><code>*</code></p>
<dd>The fields used to display the start and end sector numbers for partitions in the &#8216;p&#8217; command are 14 characters wide. This translates to a limitation of about 45 PiB. On larger disks, the displayed columns will go out of alignment.</p>
<dt><code>*</code></p>
<dd>In the Windows version, only ASCII characters are supported in the partition name field. If an existing partition uses non-ASCII UTF-16 characters, they&#8217;re likely to be corrupted in the &#8216;i&#8217; and &#8216;p&#8217; menu options&#8217; displays; however, they should be preserved when loading and saving partitions. Binaries for Linux, FreeBSD, and OS X support full UTF-16 partition names. </p>
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
<dd>Booting after converting an MBR or BSD disklabel disk is likely to be disrupted. Sometimes re-installing a boot loader will fix the problem, but other times you may need to switch boot loaders. Except on EFI-based platforms, Windows through at least Windows 7 doesn&#8217;t support booting from GPT disks. Creating a hybrid MBR (using the &#8216;h&#8217; option on the recovery &amp; transformation menu) or abandoning GPT in favor of MBR may be your only options in this case. </p>
<h2>Authors</h2>
<p>Primary author: Roderick W. Smith (rodsmith [at] rodsbooks.com) </p>
<p> Contributors: </p>
<p> * Yves Blusseau (1otnwmz02 [at] sneakemail.com) </p>
<p> * David Hubbard (david.c.hubbard [at] gmail.com) </p>
<p> * Justin Maggard (justin.maggard [at] netgear.com) </p>
<p> * Dwight Schauer (das [at] teegra.net) </p>
<p> * Florian Zumbiehl (florz [at] florz.de)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8), <code><a href="/docs/linux/man/8-cgdisk/">cgdisk</a></code>(8), <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8), <code><a href="/docs/linux/man/8-sgdisk/">sgdisk</a></code>(8), <code><a href="/docs/linux/man/8-fixparts/">fixparts</a></code>(8). <i><a rel="nofollow" href="http://en.wikipedia.org/wiki/GUID_Partition_Table">http://en.wikipedia.org/wiki/GUID_Partition_Table</a></i> <i><a rel="nofollow" href="http://developer.apple.com/technotes/tn2006/tn2166.html">http://developer.apple.com/technotes/tn2006/tn2166.html</a></i> <i><a rel="nofollow" href="http://www.rodsbooks.com/gdisk/">http://www.rodsbooks.com/gdisk/</a></i> </p>
<h2>Availability</h2>
<p>The <code>gdisk</code> command is part of the <i>GPT fdisk</i> package and is available from Rod Smith.</p>
