---
title: "sfdisk(8)"
name: "sfdisk"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sfdisk/"
description: "sfdisk – display or manipulate a disk partition table"
---

<p>sfdisk &#8211; display or manipulate a disk partition table</p>
<h2>Synopsis</h2>
<p><code>sfdisk</code> [options] <i>device</i> [<code>-N</code> <i>partition-number</i>] </p>
<p> <code>sfdisk</code> [options] <i>command</i></p>
<h2>Description</h2>
<p><code>sfdisk</code> is a script-oriented tool for partitioning any block device. It runs in interactive mode if executed on a terminal (stdin refers to a terminal). </p>
<p> Since version 2.26 <code>sfdisk</code> supports MBR (DOS), GPT, SUN and SGI disk labels, but no longer provides any functionality for CHS (Cylinder-Head-Sector) addressing. CHS has never been important for Linux, and this addressing concept does not make any sense for new devices. </p>
<p> <code>sfdisk</code> protects the first disk sector when create a new disk label. The option <code>&#8211;wipe always</code> disables this protection. Note that <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) and <code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8) completely erase this area by default. </p>
<p> <code>sfdisk</code> (since version 2.26) <code>aligns the start and end of partitions</code> to block-device I/O limits when relative sizes are specified, when the default values are used or when multiplicative suffixes (e.g., MiB) are used for sizes. It is possible that partition size will be optimized (reduced or enlarged) due to alignment if the start offset is specified exactly in sectors and partition size relative or by multiplicative suffixes. </p>
<p> The recommended way is not to specify start offsets at all and specify partition size in MiB, GiB (or so). In this case <code>sfdisk</code> aligns all partitions to block-device I/O limits (or when I/O limits are too small then to megabyte boundary to keep disk layout portable). If this default behaviour is unwanted (usually for very small partitions) then specify offsets and sizes in sectors. In this case <code>sfdisk</code> entirely follows specified numbers without any optimization. </p>
<p> <code>sfdisk</code> does not create the standard system partitions for SGI and SUN disk labels like <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) does. It is necessary to explicitly create all partitions including whole-disk system partitions. </p>
<p> <code>sfdisk</code> uses <code>BLKRRPART</code> (reread partition table) ioctl to make sure that the device is not used by system or other tools (see also <code>&#8211;no-reread</code>). It&#8217;s possible that this feature or another <code>sfdisk</code> activity races with <code>udevd</code>. The recommended way how to avoid possible collisions is to use <code>&#8211;lock</code> option. The exclusive lock will cause udevd to skip the event handling on the device. </p>
<p> The <code>sfdisk</code> prompt is only a hint for users and a displayed partition number does not mean that the same partition table entry will be created (if <code>-N</code> not specified), especially for tables with gaps.</p>
<h2>Commands</h2>
<p>The commands are mutually exclusive. </p>
<p> [<code>-N</code> <i>partition-number</i>] <i>device</i></p>
<dl>
<dd>The default <code>sfdisk</code> command is to read the specification for the desired partitioning of <i>device</i> from standard input, and then create a partition table according to the specification. See below for the description of the input format. If standard input is a terminal, then <code>sfdisk</code> starts an interactive session. </p>
<p> If the option <code>-N</code> is specified, then the changes are applied to the partition addressed by <i>partition-number</i>. The unspecified fields of the partition are not modified. </p>
<p> Note that it&#8217;s possible to address an unused partition with <code>-N</code>. For example, an MBR always contains 4 partitions, but the number of used partitions may be smaller. In this case <code>sfdisk</code> follows the default values from the partition table and does not use built-in defaults for the unused partition given with <code>-N</code>. See also <code>&#8211;append</code>.</dl>
<p> <code>-A</code>, <code>&#8211;activate</code> <i>device</i> [<i>partition-number</i>&#8230;]</p>
<dl>
<dd>Switch on the bootable flag for the specified partitions and switch off the bootable flag on all unspecified partitions. The special placeholder &#8216;-&#8216; may be used instead of the partition numbers to switch off the bootable flag on all partitions. </p>
<p> The activation command is supported for MBR and PMBR only. If a GPT label is detected, then <code>sfdisk</code> prints warning and automatically enters PMBR. </p>
<p> If no <i>partition-number</i> is specified, then list the partitions with an enabled flag.</dl>
<p> <code>&#8211;delete</code> <i>device</i> [<i>partition-number</i>&#8230;]</p>
<dl>
<dd>Delete all or the specified partitions.</dl>
<p> <code>-d</code>, <code>&#8211;dump</code> <i>device</i></p>
<dl>
<dd>Dump the partitions of a device in a format that is usable as input to <code>sfdisk</code>. See the section <code>BACKING UP THE PARTITION TABLE</code>.</dl>
<p> <code>-g</code>, <code>&#8211;show-geometry</code> [<i>device</i>&#8230;]</p>
<dl>
<dd>List the geometry of all or the specified devices. For backward compatibility the deprecated option <code>&#8211;show-pt-geometry</code> have the same meaning as this one.</dl>
<p> <code>-J</code>, <code>&#8211;json</code> <i>device</i></p>
<dl>
<dd>Dump the partitions of a device in JSON format. Note that <code>sfdisk</code> is not able to use JSON as input format.</dl>
<p> <code>-l</code>, <code>&#8211;list</code> [<i>device</i>&#8230;]</p>
<dl>
<dd>List the partitions of all or the specified devices. This command can be used together with <code>&#8211;verify</code>.</dl>
<p> <code>-F</code>, <code>&#8211;list-free</code> [<i>device</i>&#8230;]</p>
<dl>
<dd>List the free unpartitioned areas on all or the specified devices.</dl>
<p> <code>&#8211;part-attrs</code> <i>device partition-number</i> [<i>attributes</i>]</p>
<dl>
<dd>Change the GPT partition attribute bits. If <i>attributes</i> is not specified, then print the current partition settings. The <i>attributes</i> argument is a comma- or space-delimited list of bits numbers or bit names. For example, the string &quot;RequiredPartition,50,51&quot; sets three bits. The currently supported attribute bits are: </p>
<p> <code>Bit 0 (RequiredPartition)</code></p>
<dl>
<dd>If this bit is set, the partition is required for the platform to function. The creator of the partition indicates that deletion or modification of the contents can result in loss of platform features or failure for the platform to boot or operate. The system cannot function normally if this partition is removed, and it should be considered part of the hardware of the system.</dl>
<p> <code>Bit 1 (NoBlockIOProtocol)</code></p>
<dl>
<dd>EFI firmware should ignore the content of the partition and not try to read from it.</dl>
<p> <code>Bit 2 (LegacyBIOSBootable)</code></p>
<dl>
<dd>The partition may be bootable by legacy BIOS firmware.</dl>
<p> <code>Bits 3-47</code></p>
<dl>
<dd>Undefined and must be zero. Reserved for expansion by future versions of the UEFI specification.</dl>
<p> <code>Bits 48-63</code></p>
<dl>
<dd>Reserved for GUID specific use. The use of these bits will vary depending on the partition type. For example Microsoft uses bit 60 to indicate read-only, 61 for shadow copy of another partition, 62 for hidden partitions and 63 to disable automount.</dl>
</dl>
<p> <code>&#8211;part-label</code> <i>device partition-number</i> [<i>label</i>]</p>
<dl>
<dd>Change the GPT partition name (label). If <i>label</i> is not specified, then print the current partition label.</dl>
<p> <code>&#8211;part-type</code> <i>device partition-number</i> [<i>type</i>]</p>
<dl>
<dd>Change the partition type. If <i>type</i> is not specified, then print the current partition type. </p>
<p> The <i>type</i> argument is hexadecimal for MBR, GUID for GPT, type alias (e.g. &quot;linux&quot;) or type shortcut (e.g. &#8216;L&#8217;). For backward compatibility the options <code>-c</code> and <code>&#8211;id</code> have the same meaning as this one.</dl>
<p> <code>&#8211;part-uuid</code> <i>device partition-number</i> [<i>uuid</i>]</p>
<dl>
<dd>Change the GPT partition UUID. If <i>uuid</i> is not specified, then print the current partition UUID.</dl>
<p> <code>&#8211;disk-id</code> <i>device</i> [<i>id</i>]</p>
<dl>
<dd>Change the disk identifier. If <i>id</i> is not specified, then print the current identifier. The identifier is UUID for GPT or unsigned integer for MBR.</dl>
<p> <code>-r</code>, <code>&#8211;reorder</code> <i>device</i></p>
<dl>
<dd>Renumber the partitions, ordering them by their start offset.</dl>
<p> <code>-s</code>, <code>&#8211;show-size</code> [<i>device</i>&#8230;]</p>
<dl>
<dd>List the sizes of all or the specified devices in units of 1024 byte size. This command is DEPRECATED in favour of <code><a href="/docs/linux/man/8-blockdev/">blockdev</a></code>(8).</dl>
<p> <code>-T</code>, <code>&#8211;list-types</code></p>
<dl>
<dd>Print all supported types for the current disk label or the label specified by <code>&#8211;label</code>.</dl>
<p> <code>-V</code>, <code>&#8211;verify</code> [<i>device</i>&#8230;]</p>
<dl>
<dd>Test whether the partition table and partitions seem correct.</dl>
<p> <code>&#8211;relocate</code> <i>oper</i> <i>device</i></p>
<dl>
<dd>Relocate partition table header. This command is currently supported for GPT header only. The argument <i>oper</i> can be: </p>
<p> <code>gpt-bak-std</code></p>
<dl>
<dd>Move GPT backup header to the standard location at the end of the device.</dl>
<p> <code>gpt-bak-mini</code></p>
<dl>
<dd>Move GPT backup header behind the last partition. Note that UEFI standard requires the backup header at the end of the device and partitioning tools can automatically relocate the header to follow the standard.</dl>
</dl>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;append</code></p>
<dl>
<dd>Don&#8217;t create a new partition table, but only append the specified partitions. </p>
<p> Note that unused partition maybe be re-used in this case although it is not the last partition in the partition table. See also <code>-N</code> to specify entry in the partition table.</dl>
<p> <code>-b</code>, <code>&#8211;backup</code></p>
<dl>
<dd>Back up the current partition table sectors before starting the partitioning. The default backup file name is <i>~/sfdisk-&lt;device&gt;-&lt;offset&gt;.bak</i>; to use another name see option <code>-O</code>, <code>&#8211;backup-file</code>.</dl>
<p> <code>&#8211;color</code>[<code>=</code><i>when</i>]</p>
<dl>
<dd>Colorize the output. The optional argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. If the <i>when</i> argument is omitted, it defaults to <code>auto</code>. The colors can be disabled; for the current built-in default see the <code>&#8211;help</code> output. See also the <code>COLORS</code> section.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>Disable all consistency checking.</dl>
<p> <code>&#8211;Linux</code></p>
<dl>
<dd>Deprecated and ignored option. Partitioning that is compatible with Linux (and other modern operating systems) is the default.</dl>
<p> <code>&#8211;lock</code>[=<i>mode</i>]</p>
<dl>
<dd>Use exclusive BSD lock for device or file it operates. The optional argument <i>mode</i> can be <code>yes</code>, <code>no</code> (or 1 and 0) or <code>nonblock</code>. If the <i>mode</i> argument is omitted, it defaults to <code>&quot;yes&quot;</code>. This option overwrites environment variable <code>$LOCK_BLOCK_DEVICE</code>. The default is not to use any lock at all, but it&#8217;s recommended to avoid collisions with udevd or other tools.</dl>
<p> <code>-n</code>, <code>&#8211;no-act</code></p>
<dl>
<dd>Do everything except writing to the device.</dl>
<p> <code>&#8211;no-reread</code></p>
<dl>
<dd>Do not check through the re-read-partition-table ioctl whether the device is in use.</dl>
<p> <code>&#8211;no-tell-kernel</code></p>
<dl>
<dd>Don&#8217;t tell the kernel about partition changes. This option is recommended together with <code>&#8211;no-reread</code> to modify a partition on used disk. The modified partition should not be used (e.g., mounted).</dl>
<p> <code>-O</code>, <code>&#8211;backup-file</code> <i>path</i></p>
<dl>
<dd>Override the default backup file name. Note that the device name and offset are always appended to the file name.</dl>
<p> <code>&#8211;move-data</code>[<code>=</code><i>path</i>]</p>
<dl>
<dd>Move data after partition relocation, for example when moving the beginning of a partition to another place on the disk. The size of the partition has to remain the same, the new and old location may overlap. This option requires option <code>-N</code> in order to be processed on one specific partition only. </p>
<p> The optional <i>path</i> specifies log file name. The log file contains information about all read/write operations on the partition data. The word &quot;@default&quot; as a <i>path</i> forces sfdisk to use <i>~/sfdisk-&lt;devname&gt;.move</i> for the log. The log is optional since v2.35. </p>
<p> Note that this operation is risky and not atomic. <code>Don&#8217;t forget to backup your data!</code> </p>
<p> See also <code>&#8211;move-use-fsync</code>. </p>
<p> In the example below, the first command creates a 100MiB free area before the first partition and moves the data it contains (e.g., a filesystem), the next command creates a new partition from the free space (at offset 2048), and the last command reorders partitions to match disk order (the original sdc1 will become sdc2). </p>
<p> <code>echo &#8216;+100M,&#8217; | sfdisk &#8211;move-data /dev/sdc -N 1</code> <code>echo &#8216;2048,&#8217; | sfdisk /dev/sdc &#8211;append</code> <code>sfdisk /dev/sdc &#8211;reorder</code></dl>
<p> <code>&#8211;move-use-fsync</code></p>
<dl>
<dd>Use the <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) system call after each write when moving data to a new location by <code>&#8211;move-data</code>.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Specify which output columns to print. Use <code>&#8211;help</code> to get a list of all supported columns. </p>
<p> The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i> (e.g., <code>-o +UUID</code>).</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Suppress extra info messages.</dl>
<p> <code>-u</code>, <code>&#8211;unit S</code></p>
<dl>
<dd>Deprecated option. Only the sector unit is supported. This option is not supported when using the <code>&#8211;show-size</code> command.</dl>
<p> <code>-X</code>, <code>&#8211;label</code> <i>type</i></p>
<dl>
<dd>Specify the disk label type (e.g., <code>dos</code>, <code>gpt</code>, &#8230;). If this option is not given, then <code>sfdisk</code> defaults to the existing label, but if there is no label on the device yet, then the type defaults to <code>dos</code>. The default or the current label may be overwritten by the &quot;label: &lt;name&gt;&quot; script header line. The option <code>&#8211;label</code> does not force <code>sfdisk</code> to create empty disk label (see the <code>EMPTY DISK LABEL</code> section below).</dl>
<p> <code>-Y</code>, <code>&#8211;label-nested</code> <i>type</i></p>
<dl>
<dd>Force editing of a nested disk label. The primary disk label has to exist already. This option allows editing for example a hybrid/protective MBR on devices with GPT.</dl>
<p> <code>-w</code>, <code>&#8211;wipe</code> <i>when</i></p>
<dl>
<dd>Wipe filesystem, RAID and partition-table signatures from the device, in order to avoid possible collisions. The argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. When this option is not given, the default is <code>auto</code>, in which case signatures are wiped only when in interactive mode; except the old partition-table signatures which are always wiped before create a new partition-table if the argument <i>when</i> is not <code>never</code>. The <code>auto</code> mode also does not wipe the first sector (boot sector), it is necessary to use the <code>always</code> mode to wipe this area. In all cases detected signatures are reported by warning messages before a new partition table is created. See also the <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8) command.</dl>
<p> <code>-W</code>, <code>&#8211;wipe-partitions</code> <i>when</i></p>
<dl>
<dd>Wipe filesystem, RAID and partition-table signatures from a newly created partitions, in order to avoid possible collisions. The argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. When this option is not given, the default is <code>auto</code>, in which case signatures are wiped only when in interactive mode and after confirmation by user. In all cases detected signatures are reported by warning messages after a new partition is created. See also <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8) command.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Input Formats</h2>
<p><code>sfdisk</code> supports two input formats and generic header lines.</p>
<h3>Header lines</h3>
<p>The optional header lines specify generic information that apply to the partition table. The header-line format is: </p>
<p> <code>&lt;name&gt;: &lt;value&gt;</code> </p>
<p> The currently recognized headers are: </p>
<p> <code>unit</code></p>
<dl>
<dd>Specify the partitioning unit. The only supported unit is <code>sectors</code>.</dl>
<p> <code>label</code></p>
<dl>
<dd>Specify the partition table type. For example <code>dos</code> or <code>gpt</code>.</dl>
<p> <code>label-id</code></p>
<dl>
<dd>Specify the partition table identifier. It should be a hexadecimal number (with a 0x prefix) for MBR and a UUID for GPT.</dl>
<p> <code>first-lba</code></p>
<dl>
<dd>Specify the first usable sector for GPT partitions.</dl>
<p> <code>last-lba</code></p>
<dl>
<dd>Specify the last usable sector for GPT partitions.</dl>
<p> <code>table-length</code></p>
<dl>
<dd>Specify the maximal number of GPT partitions.</dl>
<p> <code>grain</code></p>
<dl>
<dd>Specify minimal size in bytes used to calculate partitions alignment. The default is 1MiB and it&#8217;s strongly recommended to use the default. Do not modify this variable if you&#8217;re not sure.</dl>
<p> <code>sector-size</code></p>
<dl>
<dd>Specify sector size. This header is informative only and it is not used when sfdisk creates a new partition table, in this case the real device specific value is always used and sector size from the dump is ignored.</dl>
<p> Note that it is only possible to use header lines before the first partition is specified in the input.</p>
<h3>Unnamed-fields format</h3>
<dl>
<dd><i>start size type bootable</i>
</dl>
<p> where each line fills one partition descriptor. </p>
<p> Fields are separated by whitespace, comma or semicolon possibly followed by whitespace; initial and trailing whitespace is ignored. Numbers can be octal, decimal or hexadecimal; decimal is the default. When a field is absent, empty or specified as &#8216;-&#8216; a default value is used. But when the <code>-N</code> option (change a single partition) is given, the default for each field is its previous value. </p>
<p> The default value of <i>start</i> is the first non-assigned sector aligned according to device I/O limits. The default start offset for the first partition is 1 MiB. The offset may be followed by the multiplicative suffixes (KiB, MiB, GiB, TiB, PiB, EiB, ZiB and YiB) then the number is interpreted as offset in bytes. </p>
<p> The default value of <i>size</i> indicates &quot;as much as possible&quot;; i.e., until the next partition or end-of-device. A numerical argument is by default interpreted as a number of sectors, however if the size is followed by one of the multiplicative suffixes (KiB, MiB, GiB, TiB, PiB, EiB, ZiB and YiB) then the number is interpreted as the size of the partition in bytes and it is then aligned according to the device I/O limits. A &#8216;+&#8217; can be used instead of a number to enlarge the partition as much as possible. Note &#8216;+&#8217; is equivalent to the default behaviour for a new partition; existing partitions will be resized as required. </p>
<p> The partition <i>type</i> is given in hex for MBR (DOS) where 0x prefix is optional; a GUID string for GPT; a shortcut or an alias. It&#8217;s recommended to use two letters for MBR hex codes to avoid collision between deprecated shortcut &#8216;E&#8217; and &#8216;0E&#8217; MBR hex code. For backward compatibility <code>sfdisk</code> tries to interpret <i>type</i> as a shortcut as a first possibility in partitioning scripts although on other places (e.g. <code>&#8211;part-type</code> command) it tries shortcuts as the last possibility. </p>
<p> Since v2.36 libfdisk supports partition type aliases as extension to shortcuts. The alias is a simple human readable word (e.g. &quot;linux&quot;). </p>
<p> Since v2.37 libfdisk supports partition type names on input, ignoring the case of the characters and all non-alphanumeric and non-digit characters in the name (e.g. &quot;Linux /usr x86&quot; is the same as &quot;linux usr-x86&quot;). </p>
<p> Supported shortcuts and aliases: </p>
<p> <code>L &#8211; alias &#8216;linux&#8217;</code></p>
<dl>
<dd>Linux; means 83 for MBR and 0FC63DAF-8483-4772-8E79-3D69D8477DE4 for GPT.</dl>
<p> <code>S &#8211; alias &#8216;swap&#8217;</code></p>
<dl>
<dd>swap area; means 82 for MBR and 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F for GPT</dl>
<p> <code>Ex &#8211; alias &#8216;extended&#8217;</code></p>
<dl>
<dd>MBR extended partition; means 05 for MBR. The original shortcut &#8216;E&#8217; is deprecated due to collision with 0x0E MBR partition type.</dl>
<p> <code>H &#8211; alias &#8216;home&#8217;</code></p>
<dl>
<dd>home partition; means 933AC7E1-2EB4-4F13-B844-0E14E2AEF915 for GPT</dl>
<p> <code>U &#8211; alias &#8216;uefi&#8217;</code></p>
<dl>
<dd>EFI System partition, means EF for MBR and C12A7328-F81F-11D2-BA4B-00A0C93EC93B for GPT</dl>
<p> <code>R &#8211; alias &#8216;raid&#8217;</code></p>
<dl>
<dd>Linux RAID; means FD for MBR and A19D880F-05FC-4D3B-A006-743F0F84911E for GPT</dl>
<p> <code>V &#8211; alias &#8216;lvm&#8217;</code></p>
<dl>
<dd>LVM; means 8E for MBR and E6D6D379-F507-44C2-A23C-238F2A3DF928 for GPT</dl>
<p> The default <i>type</i> value is <i>linux</i>. </p>
<p> The shortcut &#8216;X&#8217; for Linux extended partition (85) is deprecated in favour of &#8216;Ex&#8217;. </p>
<p> <i>bootable</i> is specified as [<code>*</code>|<code>&#8211;</code>], with as default not-bootable. The value of this field is irrelevant for Linux &#8211; when Linux runs it has been booted already &#8211; but it might play a role for certain boot loaders and for other operating systems.</p>
<h3>Named-fields format</h3>
<p>This format is more readable, robust, extensible and allows specifying additional information (e.g., a UUID). It is recommended to use this format to keep your scripts more readable.</p>
<dl>
<dd>[<i>device</i> <code>:</code>] <i>name</i>[<code>=</code><i>value</i>], &#8230;
</dl>
<p> The <i>device</i> field is optional. <code>sfdisk</code> extracts the partition number from the device name. It allows specifying the partitions in random order. This functionality is mostly used by <code>&#8211;dump</code>. Don&#8217;t use it if you are not sure. </p>
<p> The <i>value</i> can be between quotation marks (e.g., name=&quot;This is partition name&quot;). The currently supported fields are: </p>
<p> <code>start=</code><i>number</i></p>
<dl>
<dd>The first non-assigned sector aligned according to device I/O limits. The default start offset for the first partition is 1 MiB. The offset may be followed by the multiplicative suffixes (KiB, MiB, GiB, TiB, PiB, EiB, ZiB and YiB) then the number is interpreted as offset in bytes.</dl>
<p> <code>size=</code><i>number</i></p>
<dl>
<dd>Specify the partition size in sectors. The number may be followed by the multiplicative suffixes (KiB, MiB, GiB, TiB, PiB, EiB, ZiB and YiB), then it&#8217;s interpreted as size in bytes and the size is aligned according to device I/O limits.</dl>
<p> <code>bootable</code></p>
<dl>
<dd>Mark the partition as bootable.</dl>
<p> <code>attrs=</code><i>string</i></p>
<dl>
<dd>Partition attributes, usually GPT partition attribute bits. See <code>&#8211;part-attrs</code> for more details about the GPT-bits string format.</dl>
<p> <code>uuid=</code><i>string</i></p>
<dl>
<dd>GPT partition UUID.</dl>
<p> <code>name=</code><i>string</i></p>
<dl>
<dd>GPT partition name.</dl>
<p> <code>type=</code><i>code</i></p>
<dl>
<dd>A hexadecimal number (without 0x) for an MBR partition, a GUID for a GPT partition, a shortcut as for unnamed-fields format or a type name (e.g. type=&quot;Linux /usr (x86)&quot;). See above the section about the unnamed-fields format for more details. For backward compatibility the <code>Id=</code> field has the same meaning.</dl>
<h2>Empty Disk Label</h2>
<p><code>sfdisk</code> does not create partition table without partitions by default. The lines with partitions are expected in the script by default. The empty partition table has to be explicitly requested by &quot;label: &lt;name&gt;&quot; script header line without any partitions lines. For example:</p>
<dl>
<dd><code>echo &#8216;label: gpt&#8217; | sfdisk /dev/sdb</code>
</dl>
<p> creates empty GPT partition table. Note that the <code>&#8211;append</code> disables this feature.</p>
<h2>Backing Up The Partition Table</h2>
<p>It is recommended to save the layout of your devices. <code>sfdisk</code> supports two ways. </p>
<p> Use the <code>&#8211;dump</code> option to save a description of the device layout to a text file. The dump format is suitable for later <code>sfdisk</code> input. For example:</p>
<dl>
<dd><code>sfdisk &#8211;dump /dev/sda &gt; sda.dump</code>
</dl>
<p> This can later be restored by:</p>
<dl>
<dd><code>sfdisk /dev/sda &lt; sda.dump</code>
</dl>
<p> If you want to do a full (binary) backup of all sectors where the partition table is stored, then use the <code>&#8211;backup</code> option. It writes the sectors to <i>~/sfdisk-&lt;device&gt;-&lt;offset&gt;.bak</i> files. The default name of the backup file can be changed with the <code>&#8211;backup-file</code> option. The backup files contain only raw data from the <i>device</i>. Note that the same concept of backup files is used by <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8). For example:</p>
<dl>
<dd><code>sfdisk &#8211;backup /dev/sda</code>
</dl>
<p> The GPT header can later be restored by:</p>
<dl>
<dd>dd if=~/sfdisk-sda-0x00000200.bak of=/dev/sda \ seek=$0x00000200 bs=1 conv=notrunc
</dl>
<p> Note that <code>sfdisk</code> since version 2.26 no longer provides the <code>-I</code> option to restore sectors. <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1) provides all necessary functionality.</p>
<h2>Colors</h2>
<p>Implicit coloring can be disabled by an empty file <i>/etc/terminal-colors.d/sfdisk.disable</i>. </p>
<p> See <code><a href="/docs/linux/man/5-terminal-colors-d/">terminal-colors.d</a></code>(5) for more details about colorization configuration. The logical color names supported by <code>sfdisk</code> are: </p>
<p> <code>header</code></p>
<dl>
<dd>The header of the output tables.</dl>
<p> <code>warn</code></p>
<dl>
<dd>The warning messages.</dl>
<p> <code>welcome</code></p>
<dl>
<dd>The welcome message.</dl>
<h2>Environment</h2>
<p>SFDISK_DEBUG=all</p>
<dl>
<dd>enables <code>sfdisk</code> debug output.</dl>
<p> LIBFDISK_DEBUG=all</p>
<dl>
<dd>enables libfdisk debug output.</dl>
<p> LIBBLKID_DEBUG=all</p>
<dl>
<dd>enables libblkid debug output.</dl>
<p> LIBSMARTCOLS_DEBUG=all</p>
<dl>
<dd>enables libsmartcols debug output.</dl>
<p> LOCK_BLOCK_DEVICE=&lt;mode&gt;</p>
<dl>
<dd>use exclusive BSD lock. The mode is &quot;1&quot; or &quot;0&quot;. See <code>&#8211;lock</code> for more details.</dl>
<h2>Notes</h2>
<p>Since version 2.26 <code>sfdisk</code> no longer provides the <code>-R</code> or <code>&#8211;re-read</code> option to force the kernel to reread the partition table. Use <code>blockdev &#8211;rereadpt</code> instead. </p>
<p> Since version 2.26 <code>sfdisk</code> does not provide the <code>&#8211;DOS</code>, <code>&#8211;IBM</code>, <code>&#8211;DOS-extended</code>, <code>&#8211;unhide</code>, <code>&#8211;show-extended</code>, <code>&#8211;cylinders</code>, <code>&#8211;heads</code>, <code>&#8211;sectors</code>, <code>&#8211;inside-outer</code>, <code>&#8211;not-inside-outer</code> options.</p>
<h2>Authors</h2>
<p>The current <code>sfdisk</code> implementation is based on the original <code>sfdisk</code> from Andries E. Brouwer.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8), <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-partprobe/">partprobe</a></code>(8), <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>sfdisk</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
