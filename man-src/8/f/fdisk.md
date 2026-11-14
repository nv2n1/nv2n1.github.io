---
title: "fdisk(8)"
name: "fdisk"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fdisk/"
description: "fdisk – manipulate disk partition table"
---

<p>fdisk &#8211; manipulate disk partition table</p>
<h2>Synopsis</h2>
<p><code>fdisk</code> [options] <i>device</i> </p>
<p> <code>fdisk</code> <code>-l</code> [<i>device</i>&#8230;]</p>
<h2>Description</h2>
<p><code>fdisk</code> is a dialog-driven program for creation and manipulation of partition tables. It understands GPT, MBR, Sun, SGI and BSD partition tables. </p>
<p> Block devices can be divided into one or more logical disks called <i>partitions</i>. This division is recorded in the <i>partition table</i>, usually found in sector 0 of the disk. (In the BSD world one talks about `disk slices&#8217; and a `disklabel&#8217;.) </p>
<p> All partitioning is driven by device I/O limits (the topology) by default. <code>fdisk</code> is able to optimize the disk layout for a 4K-sector size and use an alignment offset on modern devices for MBR and GPT. It is always a good idea to follow <code>fdisk</code>&#8216;s defaults as the default values (e.g., first and last partition sectors) and partition sizes specified by the +/-&lt;size&gt;{M,G,&#8230;} notation are always aligned according to the device properties. </p>
<p> CHS (Cylinder-Head-Sector) addressing is deprecated and not used by default. Please, do not follow old articles and recommendations with <code>fdisk -S &lt;n&gt; -H &lt;n&gt;</code> advices for SSD or 4K-sector devices. </p>
<p> Note that <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8) provides a rich interface for scripts to print disk layouts, <code>fdisk</code> is mostly designed for humans. Backward compatibility in the output of <code>fdisk</code> is not guaranteed. The input (the commands) should always be backward compatible.</p>
<h2>Options</h2>
<p><code>-b</code>, <code>&#8211;sector-size</code> <i>sectorsize</i></p>
<dl>
<dd>Specify the sector size of the disk. Valid values are 512, 1024, 2048, and 4096. (Recent kernels know the sector size. Use this option only on old kernels or to override the kernel&#8217;s ideas.) Since util-linux-2.17, <code>fdisk</code> differentiates between logical and physical sector size. This option changes both sector sizes to <i>sectorsize</i>.</dl>
<p> <code>-B</code>, <code>&#8211;protect-boot</code></p>
<dl>
<dd>Don&#8217;t erase the beginning of the first disk sector when creating a new disk label. This feature is supported for GPT and MBR.</dl>
<p> <code>-c</code>, <code>&#8211;compatibility</code>[=<i>mode</i>]</p>
<dl>
<dd>Specify the compatibility mode, &#8216;dos&#8217; or &#8216;nondos&#8217;. The default is non-DOS mode. For backward compatibility, it is possible to use the option without the <i>mode</i> argument &#8212; then the default is used. Note that the optional <i>mode</i> argument cannot be separated from the <code>-c</code> option by a space, the correct form is for example <code>-c</code>=<i>dos</i>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display a help text and exit.</dl>
<p> <code>-L</code>, <code>&#8211;color</code>[=<i>when</i>]</p>
<dl>
<dd>Colorize the output. The optional argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. If the <i>when</i> argument is omitted, it defaults to <code>auto</code>. The colors can be disabled; for the current built-in default see the <code>&#8211;help</code> output. See also the <code>COLORS</code> section.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dd>List the partition tables for the specified devices and then exit. </p>
<p> If no devices are given, the devices mentioned in <i>/proc/partitions</i> (if this file exists) are used. Devices are always listed in the order in which they are specified on the command-line, or by the kernel listed in <i>/proc/partitions</i>.</dl>
<p> <code>-x</code>, <code>&#8211;list-details</code></p>
<dl>
<dd>Like <code>&#8211;list</code>, but provides more details.</dl>
<p> <code>&#8211;lock</code>[=<i>mode</i>]</p>
<dl>
<dd>Use exclusive BSD lock for device or file it operates. The optional argument <i>mode</i> can be <code>yes</code>, <code>no</code> (or 1 and 0) or <code>nonblock</code>. If the <i>mode</i> argument is omitted, it defaults to <code>&quot;yes&quot;</code>. This option overwrites environment variable <code>$LOCK_BLOCK_DEVICE</code>. The default is not to use any lock at all, but it&#8217;s recommended to avoid collisions with udevd or other tools.</dl>
<p> <code>-n</code>, <code>&#8211;noauto-pt</code></p>
<dl>
<dd>Don&#8217;t automatically create a default partition table on empty device. The partition table has to be explicitly created by user (by command like &#8216;o&#8217;, &#8216;g&#8217;, etc.).</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Specify which output columns to print. Use <code>&#8211;help</code> to get a list of all supported columns. </p>
<p> The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i> (e.g., <code>-o +UUID</code>).</dl>
<p> <code>-s</code>, <code>&#8211;getsz</code></p>
<dl>
<dd>Print the size in 512-byte sectors of each given block device. This option is DEPRECATED in favour of <code><a href="/docs/linux/man/8-blockdev/">blockdev</a></code>(8).</dl>
<p> <code>-t</code>, <code>&#8211;type</code> <i>type</i></p>
<dl>
<dd>Enable support only for disklabels of the specified <i>type</i>, and disable support for all other types.</dl>
<p> <code>-u</code>, <code>&#8211;units</code>[=<i>unit</i>]</p>
<dl>
<dd>When listing partition tables, show sizes in &#8216;sectors&#8217; or in &#8216;cylinders&#8217;. The default is to show sizes in sectors. For backward compatibility, it is possible to use the option without the <i>unit</i> argument &#8212; then the default is used. Note that the optional <i>unit</i> argument cannot be separated from the <code>-u</code> option by a space, the correct form is for example &#8216;*-u=*<i>cylinders</i>&#8216;.</dl>
<p> <code>-C</code>, <code>&#8211;cylinders</code> <i>number</i></p>
<dl>
<dd>Specify the number of cylinders of the disk. I have no idea why anybody would want to do so.</dl>
<p> <code>-H</code>, <code>&#8211;heads</code> <i>number</i></p>
<dl>
<dd>Specify the number of heads of the disk. (Not the physical number, of course, but the number used for partition tables.) Reasonable values are 255 and 16.</dl>
<p> <code>-S</code>, <code>&#8211;sectors</code> <i>number</i></p>
<dl>
<dd>Specify the number of sectors per track of the disk. (Not the physical number, of course, but the number used for partition tables.) A reasonable value is 63.</dl>
<p> <code>-w</code>, <code>&#8211;wipe</code> <i>when</i></p>
<dl>
<dd>Wipe filesystem, RAID and partition-table signatures from the device, in order to avoid possible collisions. The argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. When this option is not given, the default is <code>auto</code>, in which case signatures are wiped only when in interactive mode. In all cases detected signatures are reported by warning messages before a new partition table is created. See also <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8) command.</dl>
<p> <code>-W</code>, <code>&#8211;wipe-partitions</code> <i>when</i></p>
<dl>
<dd>Wipe filesystem, RAID and partition-table signatures from a newly created partitions, in order to avoid possible collisions. The argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. When this option is not given, the default is <code>auto</code>, in which case signatures are wiped only when in interactive mode and after confirmation by user. In all cases detected signatures are reported by warning messages before a new partition is created. See also <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8) command.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<h2>Devices</h2>
<p>The <i>device</i> is usually <i>/dev/sda</i>, <i>/dev/sdb</i> or so. A device name refers to the entire disk. Old systems without libata (a library used inside the Linux kernel to support ATA host controllers and devices) make a difference between IDE and SCSI disks. In such cases the device name will be <i>/dev/hd*</i> (IDE) or <i>/dev/sd*</i> (SCSI). </p>
<p> The <i>partition</i> is a device name followed by a partition number. For example, <i>/dev/sda1</i> is the first partition on the first hard disk in the system. See also Linux kernel documentation (the <i>Documentation/admin-guide/devices.txt</i> file).</p>
<h2>Sizes</h2>
<p>The &quot;last sector&quot; dialog accepts partition size specified by number of sectors or by +/-&lt;size&gt;{K,B,M,G,&#8230;} notation. </p>
<p> If the size is prefixed by &#8216;+&#8217; then it is interpreted as relative to the partition first sector. If the size is prefixed by &#8216;-&#8216; then it is interpreted as relative to the high limit (last available sector for the partition). </p>
<p> In the case the size is specified in bytes than the number may be followed by the multiplicative suffixes KiB=1024, MiB=1024*1024, and so on for GiB, TiB, PiB, EiB, ZiB and YiB. The &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;. </p>
<p> The relative sizes are always aligned according to device I/O limits. The +/-&lt;size&gt;{K,B,M,G,&#8230;} notation is recommended. </p>
<p> For backward compatibility fdisk also accepts the suffixes KB=1000, MB=1000*1000, and so on for GB, TB, PB, EB, ZB and YB. These 10^N suffixes are deprecated.</p>
<h2>Script Files</h2>
<p><code>fdisk</code> allows reading (by &#8216;I&#8217; command) <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8) compatible script files. The script is applied to in-memory partition table, and then it is possible to modify the partition table before you write it to the device. </p>
<p> And vice-versa it is possible to write the current in-memory disk layout to the script file by command &#8216;O&#8217;. </p>
<p> The script files are compatible between <code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8), <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8), <code>fdisk</code> and other libfdisk applications. For more details see <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8).</p>
<h2>Disk Labels</h2>
<p><code>GPT (GUID Partition Table)</code></p>
<dl>
<dd>GPT is modern standard for the layout of the partition table. GPT uses 64-bit logical block addresses, checksums, UUIDs and names for partitions and an unlimited number of partitions (although the number of partitions is usually restricted to 128 in many partitioning tools). </p>
<p> Note that the first sector is still reserved for a <code>protective MBR</code> in the GPT specification. It prevents MBR-only partitioning tools from mis-recognizing and overwriting GPT disks. </p>
<p> GPT is always a better choice than MBR, especially on modern hardware with a UEFI boot loader.</dl>
<p> <code>DOS-type (MBR)</code></p>
<dl>
<dd>A DOS-type partition table can describe an unlimited number of partitions. In sector 0 there is room for the description of 4 partitions (called `primary&#8217;). One of these may be an extended partition; this is a box holding logical partitions, with descriptors found in a linked list of sectors, each preceding the corresponding logical partitions. The four primary partitions, present or not, get numbers 1-4. Logical partitions are numbered starting from 5. </p>
<p> In a DOS-type partition table the starting offset and the size of each partition is stored in two ways: as an absolute number of sectors (given in 32 bits), and as a <code>Cylinders/Heads/Sectors</code> triple (given in 10+8+6 bits). The former is OK &#8212; with 512-byte sectors this will work up to 2 TB. The latter has two problems. First, these C/H/S fields can be filled only when the number of heads and the number of sectors per track are known. And second, even if we know what these numbers should be, the 24 bits that are available do not suffice. DOS uses C/H/S only, Windows uses both, Linux never uses C/H/S. The <code>C/H/S addressing is deprecated</code> and may be unsupported in some later <code>fdisk</code> version. </p>
<p> <code>Please, read the DOS-mode section if you want DOS-compatible partitions.</code> <code>fdisk</code> does not care about cylinder boundaries by default.</dl>
<p> <code>BSD/Sun-type</code></p>
<dl>
<dd>A BSD/Sun disklabel can describe 8 partitions, the third of which should be a `whole disk&#8217; partition. Do not start a partition that actually uses its first sector (like a swap partition) at cylinder 0, since that will destroy the disklabel. Note that a <code>BSD label</code> is usually nested within a DOS partition.</dl>
<p> <code>IRIX/SGI-type</code></p>
<dl>
<dd>An IRIX/SGI disklabel can describe 16 partitions, the eleventh of which should be an entire `volume&#8217; partition, while the ninth should be labeled `volume header&#8217;. The volume header will also cover the partition table, i.e., it starts at block zero and extends by default over five cylinders. The remaining space in the volume header may be used by header directory entries. No partitions may overlap with the volume header. Also do not change its type or make some filesystem on it, since you will lose the partition table. Use this type of label only when working with Linux on IRIX/SGI machines or IRIX/SGI disks under Linux. </p>
<p> A sync() and an ioctl(BLKRRPART) (rereading the partition table from disk) are performed before exiting when the partition table has been updated.</dl>
<h2>Dos Mode And Dos 6.X Warning</h2>
<p><code>Note that all this is deprecated. You don&#8217;t have to care about things like</code> <code>geometry and cylinders on modern operating systems. If you really want</code> <code>DOS-compatible partitioning then you have to enable DOS mode and cylinder</code> <code>units by using the &#8216;-c=dos -u=cylinders&#8217; fdisk command-line options.</code> </p>
<p> The DOS 6.x FORMAT command looks for some information in the first sector of the data area of the partition, and treats this information as more reliable than the information in the partition table. DOS FORMAT expects DOS FDISK to clear the first 512 bytes of the data area of a partition whenever a size change occurs. DOS FORMAT will look at this extra information even if the /U flag is given &#8212; we consider this a bug in DOS FORMAT and DOS FDISK. </p>
<p> The bottom line is that if you use <code>fdisk</code> or <code>cfdisk</code> to change the size of a DOS partition table entry, then you must also use <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1) to <code>zero the first 512 bytes</code> of that partition before using DOS FORMAT to format the partition. For example, if you were using <code>fdisk</code> to make a DOS partition table entry for <i>/dev/sda1</i>, then (after exiting <code>fdisk</code> and rebooting Linux so that the partition table information is valid) you would use the command <code>dd if=/dev/zero of=/dev/sda1 bs=512 count=1</code> to zero the first 512 bytes of the partition. </p>
<p> <code>fdisk</code> usually obtains the disk geometry automatically. This is not necessarily the physical disk geometry (indeed, modern disks do not really have anything like a physical geometry, certainly not something that can be described in the simplistic Cylinders/Heads/Sectors form), but it is the disk geometry that MS-DOS uses for the partition table. </p>
<p> Usually all goes well by default, and there are no problems if Linux is the only system on the disk. However, if the disk has to be shared with other operating systems, it is often a good idea to let an <code>fdisk</code> from another operating system make at least one partition. When Linux boots it looks at the partition table, and tries to deduce what (fake) geometry is required for good cooperation with other systems. </p>
<p> Whenever a partition table is printed out in DOS mode, a consistency check is performed on the partition table entries. This check verifies that the physical and logical start and end points are identical, and that each partition starts and ends on a cylinder boundary (except for the first partition). </p>
<p> Some versions of MS-DOS create a first partition which does not begin on a cylinder boundary, but on sector 2 of the first cylinder. Partitions beginning in cylinder 1 cannot begin on a cylinder boundary, but this is unlikely to cause difficulty unless you have OS/2 on your machine. </p>
<p> For best results, you should always use an OS-specific partition table program. For example, you should make DOS partitions with the DOS FDISK program and Linux partitions with the Linux <code>fdisk</code> or Linux <code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8) programs.</p>
<h2>Colors</h2>
<p>Implicit coloring can be disabled by an empty file <i>/etc/terminal-colors.d/fdisk.disable</i>. </p>
<p> See <code><a href="/docs/linux/man/5-terminal-colors-d/">terminal-colors.d</a></code>(5) for more details about colorization configuration. The logical color names supported by <code>fdisk</code> are: </p>
<p> <code>header</code></p>
<dl>
<dd>The header of the output tables.</dl>
<p> <code>help-title</code></p>
<dl>
<dd>The help section titles.</dl>
<p> <code>warn</code></p>
<dl>
<dd>The warning messages.</dl>
<p> <code>welcome</code></p>
<dl>
<dd>The welcome message.</dl>
<h2>Environment</h2>
<p><code>FDISK_DEBUG</code>=all</p>
<dl>
<dd>enables fdisk debug output.</dl>
<p> <code>LIBFDISK_DEBUG</code>=all</p>
<dl>
<dd>enables libfdisk debug output.</dl>
<p> <code>LIBBLKID_DEBUG</code>=all</p>
<dl>
<dd>enables libblkid debug output.</dl>
<p> <code>LIBSMARTCOLS_DEBUG</code>=all</p>
<dl>
<dd>enables libsmartcols debug output.</dl>
<p> <code>LIBSMARTCOLS_DEBUG_PADDING</code>=on</p>
<dl>
<dd>use visible padding characters.</dl>
<p> <code>LOCK_BLOCK_DEVICE</code>=&lt;mode&gt;</p>
<dl>
<dd>use exclusive BSD lock. The mode is &quot;1&quot; or &quot;0&quot;. See <code>&#8211;lock</code> for more details.</dl>
<h2>Authors</h2>
<p>The original version was written by Andries E. Brouwer, A. V. Le Blanc and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8), <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>fdisk</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
