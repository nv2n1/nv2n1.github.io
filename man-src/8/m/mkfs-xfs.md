---
title: "mkfs-xfs(8)"
name: "mkfs-xfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-xfs/"
description: "mkfs.xfs – construct an XFS filesystem"
---

<p>mkfs.xfs &#8211; construct an XFS filesystem</p>
<h2>Synopsis</h2>
<p><code>mkfs.xfs</code> [ <code>-b</code> <i>block_size</i> ] [ <code>-m</code> <i>global_metadata_options</i> ] [ <code>-d</code> <i>data_section_options</i> ] [ <code>-f</code> ] [ <code>-i</code> <i>inode_options</i> ] [ <code>-l</code> <i>log_section_options</i> ] [ <code>-n</code> <i>naming_options</i> ] [ <code>-p</code> <i>protofile</i> ] [ <code>-q</code> ] [ <code>-r</code> <i>realtime_section_options</i> ] [ <code>-s</code> <i>sector_size</i> ] [ <code>-L</code> <i>label</i> ] [ <code>-N</code> ] [ <code>-K</code> ] <i>device</i><br />
 <code>mkfs.xfs -V</code></p>
<h2>Description</h2>
<p><code>mkfs.xfs</code> constructs an XFS filesystem by writing on a special file using the values found in the arguments of the command line. It is invoked automatically by <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8) when it is given the <code>-t xfs</code> option. </p>
<p> In its simplest (and most commonly used form), the size of the filesystem is determined from the disk driver. As an example, to make a filesystem with an internal log on the first partition on the first SCSI disk, use:</p>
<dl>
<dd><code>mkfs.xfs /dev/sda1</code></dl>
<p> The metadata log can be placed on another device to reduce the number of disk seeks. To create a filesystem on the first partition on the first SCSI disk with a 10MiB log located on the first partition on the second SCSI disk, use:</p>
<dl>
<dd>
<dl>
<dt> <code>mkfs.xfs -l logdev=/dev/sdb1,size=10m /dev/sda1</code></dl>
</dl>
<dd>Each of the <i>option</i> elements in the argument list above can be given as multiple comma-separated suboptions if multiple suboptions apply to the same option. Equivalently, each main option can be given multiple times with different suboptions. For example, <code>-l internal,size=10m</code> and <code>-l internal -l size=10m</code> are equivalent. </p>
<p> In the descriptions below, sizes are given in sectors, bytes, blocks, kilobytes, megabytes, gigabytes, etc. Sizes are treated as hexadecimal if prefixed by 0x or 0X, octal if prefixed by 0, or decimal otherwise. The following lists possible multiplication suffixes:</p>
<dl>
<dd>
<dl>
<dt> <code>s</code>&nbsp;&#8211; multiply by sector size (default = 512, see <code>-s</code></p>
<dd>option below).</p>
<dt> <code>b</code>&nbsp;&#8211; multiply by filesystem block size (default = 4K, see <code>-b</code></p>
<dd>option below).</p>
<dt> <code>k</code>&nbsp;&#8211; multiply by one kilobyte (1,024 bytes).</p>
<dt> <code>m</code>&nbsp;&#8211; multiply by one megabyte (1,048,576 bytes).</p>
<dt> <code>g</code>&nbsp;&#8211; multiply by one gigabyte (1,073,741,824 bytes).</p>
<dt> <code>t</code>&nbsp;&#8211; multiply by one terabyte (1,099,511,627,776 bytes).</p>
<dt> <code>p</code>&nbsp;&#8211; multiply by one petabyte (1,024 terabytes).</p>
<dt> <code>e</code>&nbsp;&#8211; multiply by one exabyte (1,048,576 terabytes).</dl>
</dl>
<dd>When specifying parameters in units of sectors or filesystem blocks, the <code>-s</code> option or the <code>-b</code> option first needs to be added to the command line. Failure to specify the size of the units will result in illegal value errors when parameters are quantified in those units. </p>
<p> Many feature options allow an optional argument of 0 or 1, to explicitly disable or enable the functionality.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code><i> block_size_options</i></p>
<dd>This option specifies the fundamental block size of the filesystem. The valid <i>block_size_options</i> are: <code>log=</code><i>value</i> or <code>size=</code><i>value</i> and only one can be supplied. The block size is specified either as a base two logarithm value with <code>log=</code>, or in bytes with <code>size=</code>. The default value is 4096 bytes (4 KiB), the minimum is 512, and the maximum is 65536 (64 KiB).</p>
<dd>To specify any options on the command line in units of filesystem blocks, this option must be specified first so that the filesystem block size is applied consistently to all options.</p>
<dd>Although <code>mkfs.xfs</code> will accept any of these values and create a valid filesystem, XFS on Linux can only mount filesystems with pagesize or smaller blocks.</p>
<dt><code>-m</code><i> global_metadata_options</i></p>
<dd>These options specify metadata format options that either apply to the entire filesystem or aren&#8217;t easily characterised by a specific functionality group. The valid <i>global_metadata_options</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>crc=</code><i>value</i></p>
<dd>This is used to create a filesystem which maintains and checks CRC information in all metadata objects on disk. The value is either 0 to disable the feature, or 1 to enable the use of CRCs.</p>
<dd>CRCs enable enhanced error detection due to hardware issues, whilst the format changes also improves crash recovery algorithms and the ability of various tools to validate and repair metadata corruptions when they are found. The CRC algorithm used is CRC32c, so the overhead is dependent on CPU architecture as some CPUs have hardware acceleration of this algorithm. Typically the overhead of calculating and checking the CRCs is not noticeable in normal operation.</p>
<dd>By default, <code>mkfs.xfs</code> will enable metadata CRCs.</p>
<dt><code>finobt=</code><i>value</i></p>
<dd>This option enables the use of a separate free inode btree index in each allocation group. The value is either 0 to disable the feature, or 1 to create a free inode btree in each allocation group.</p>
<dd>The free inode btree mirrors the existing allocated inode btree index which indexes both used and free inodes. The free inode btree does not index used inodes, allowing faster, more consistent inode allocation performance as filesystems age.</p>
<dd>By default, <code>mkfs.xfs</code> will create free inode btrees for filesystems created with the (default) <code>-m crc=1</code> option set. When the option <code>-m crc=0</code> is used, the free inode btree feature is not supported and is disabled.</p>
<dt><code>uuid=</code><i>value</i></p>
<dd>Use the given value as the filesystem UUID for the newly created filesystem. The default is to generate a random UUID.</p>
<dt><code>rmapbt=</code><i>value</i></p>
<dd>This option enables the creation of a reverse-mapping btree index in each allocation group. The value is either 0 to disable the feature, or 1 to create the btree.</p>
<dd>The reverse mapping btree maps filesystem blocks to the owner of the filesystem block. Most of the mappings will be to an inode number and an offset, though there will also be mappings to filesystem metadata. This secondary metadata can be used to validate the primary metadata or to pinpoint exactly which data has been lost when a disk error occurs.</p>
<dd>By default, <code>mkfs.xfs</code> will not create reverse mapping btrees. This feature is only available for filesystems created with the (default) <code>-m crc=1</code> option set. When the option <code>-m crc=0</code> is used, the reverse mapping btree feature is not supported and is disabled.</p>
<dt><code>reflink=</code><i>value</i></p>
<dd>This option enables the use of a separate reference count btree index in each allocation group. The value is either 0 to disable the feature, or 1 to create a reference count btree in each allocation group.</p>
<dd>The reference count btree enables the sharing of physical extents between the data forks of different files, which is commonly known as &quot;reflink&quot;. Unlike traditional Unix filesystems which assume that every inode and logical block pair map to a unique physical block, a reflink-capable XFS filesystem removes the uniqueness requirement, allowing up to four billion arbitrary inode/logical block pairs to map to a physical block. If a program tries to write to a multiply-referenced block in a file, the write will be redirected to a new block, and that file&#8217;s logical-to-physical mapping will be changed to the new block (&quot;copy on write&quot;). This feature enables the creation of per-file snapshots and deduplication. It is only available for the data forks of regular files.</p>
<dd>By default, <code>mkfs.xfs</code> will not create reference count btrees and therefore will not enable the reflink feature. This feature is only available for filesystems created with the (default) <code>-m crc=1</code> option set. When the option <code>-m crc=0</code> is used, the reference count btree feature is not supported and reflink is disabled.</dl>
</dl>
<dt><code>-d</code><i> data_section_options</i></p>
<dd>These options specify the location, size, and other parameters of the data section of the filesystem. The valid <i>data_section_options</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>agcount=</code><i>value</i></p>
<dd>This is used to specify the number of allocation groups. The data section of the filesystem is divided into allocation groups to improve the performance of XFS. More allocation groups imply that more parallelism can be achieved when allocating blocks and inodes. The minimum allocation group size is 16 MiB; the maximum size is just under 1 TiB. The data section of the filesystem is divided into <i>value</i> allocation groups (default value is scaled automatically based on the underlying device size).</p>
<dt><code>agsize=</code><i>value</i></p>
<dd>This is an alternative to using the <code>agcount</code> suboption. The <i>value</i> is the desired size of the allocation group expressed in bytes (usually using the <code>m</code> or <code>g</code> suffixes). This value must be a multiple of the filesystem block size, and must be at least 16MiB, and no more than 1TiB, and may be automatically adjusted to properly align with the stripe geometry. The <code>agcount</code> and <code>agsize</code> suboptions are mutually exclusive.</p>
<dt><code>name=</code><i>value</i></p>
<dd>This can be used to specify the name of the special file containing the filesystem. In this case, the log section must be specified as <code>internal</code> (with a size, see the <code>-l</code> option below) and there can be no real-time section.</p>
<dt><code>file[=</code><i>value</i><code>]</code></p>
<dd>This is used to specify that the file given by the <code>name</code> suboption is a regular file. The <i>value</i> is either 0 or 1, with 1 signifying that the file is regular. This suboption is used only to make a filesystem image. If the <i>value</i> is omitted then 1 is assumed.</p>
<dt><code>size=</code><i>value</i></p>
<dd>This is used to specify the size of the data section. This suboption is required if <code>-d file[=1]</code> is given. Otherwise, it is only needed if the filesystem should occupy less space than the size of the special file.</p>
<dt><code>sunit=</code><i>value</i></p>
<dd>This is used to specify the stripe unit for a RAID device or a logical volume. The <i>value</i> has to be specified in 512-byte block units. Use the <code>su</code> suboption to specify the stripe unit size in bytes. This suboption ensures that data allocations will be stripe unit aligned when the current end of file is being extended and the file size is larger than 512KiB. Also inode allocations and the internal log will be stripe unit aligned.</p>
<dt><code>su=</code><i>value</i></p>
<dd>This is an alternative to using <code>sunit.</code> The <code>su</code> suboption is used to specify the stripe unit for a RAID device or a striped logical volume. The <i>value</i> has to be specified in bytes, (usually using the <code>m</code> or <code>g</code> suffixes). This <i>value</i> must be a multiple of the filesystem block size.</p>
<dt><code>swidth=</code><i>value</i></p>
<dd>This is used to specify the stripe width for a RAID device or a striped logical volume. The <i>value</i> has to be specified in 512-byte block units. Use the <code>sw</code> suboption to specify the stripe width size in bytes. This suboption is required if <code>-d sunit</code> has been specified and it has to be a multiple of the <code>-d sunit</code> suboption.</p>
<dt><code>sw=</code><i>value</i></p>
<dd>suboption is an alternative to using <code>swidth.</code> The <code>sw</code> suboption is used to specify the stripe width for a RAID device or striped logical volume. The <i>value</i> is expressed as a multiplier of the stripe unit, usually the same as the number of stripe members in the logical volume configuration, or data disks in a RAID device.</p>
<dd>When a filesystem is created on a logical volume device, <code>mkfs.xfs</code> will automatically query the logical volume for appropriate <code>sunit</code> and <code>swidth</code> values.</p>
<dt><code>noalign</code></p>
<dd>This option disables automatic geometry detection and creates the filesystem without stripe geometry alignment even if the underlying storage device provides this information.</dl>
</dl>
<dt><code>-f</code></p>
<dd>Force overwrite when an existing filesystem is detected on the device. By default, <code>mkfs.xfs</code> will not write to the device if it suspects that there is a filesystem or partition table on the device already.</p>
<dt><code>-i</code><i> inode_options</i></p>
<dd>This option specifies the inode size of the filesystem, and other inode allocation parameters. The XFS inode contains a fixed-size part and a variable-size part. The variable-size part, whose size is affected by this option, can contain: directory data, for small directories; attribute data, for small attribute sets; symbolic link data, for small symbolic links; the extent list for the file, for files with a small number of extents; and the root of a tree describing the location of extents for the file, for files with a large number of extents.</p>
<dd>The valid <i>inode_options</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>size=</code><i>value</i><code> | log=</code><i>value</i><code> | perblock=</code><i>value</i></p>
<dd>The inode size is specified either as a <i>value</i> in bytes with <code>size=</code>, a base two logarithm <i>value</i> with <code>log=</code>, or as the number fitting in a filesystem block with <code>perblock=</code>. The minimum (and default) <i>value</i> is 256 bytes without crc, 512 bytes with crc enabled. The maximum <i>value</i> is 2048 (2 KiB) subject to the restriction that the inode size cannot exceed one half of the filesystem block size.</p>
<dd>XFS uses 64-bit inode numbers internally; however, the number of significant bits in an inode number is affected by filesystem geometry. In practice, filesystem size and inode size are the predominant factors. The Linux kernel (on 32 bit hardware platforms) and most applications cannot currently handle inode numbers greater than 32 significant bits, so if no inode size is given on the command line, <code>mkfs.xfs</code> will attempt to choose a size such that inode numbers will be &lt; 32 bits. If an inode size is specified, or if a filesystem is sufficiently large, <code>mkfs.xfs</code> will warn if this will create inode numbers &gt; 32 significant bits.</p>
<dt><code>maxpct=</code><i>value</i></p>
<dd>This specifies the maximum percentage of space in the filesystem that can be allocated to inodes. The default <i>value</i> is 25% for filesystems under 1TB, 5% for filesystems under 50TB and 1% for filesystems over 50TB.</p>
<dd>In the default inode allocation mode, inode blocks are chosen such that inode numbers will not exceed 32 bits, which restricts the inode blocks to the lower portion of the filesystem. The data block allocator will avoid these low blocks to accommodate the specified maxpct, so a high value may result in a filesystem with nothing but inodes in a significant portion of the lower blocks of the filesystem. (This restriction is not present when the filesystem is mounted with the <i>inode64</i> option on 64-bit platforms).</p>
<dd>Setting the value to 0 means that essentially all of the filesystem can become inode blocks, subject to inode32 restrictions.</p>
<dd>This value can be modified with <i><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a>(8)</i>.</p>
<dt><code>align[=</code><i>value</i><code>]</code></p>
<dd>This is used to specify that inode allocation is or is not aligned. The <i>value</i> is either 0 or 1, with 1 signifying that inodes are allocated aligned. If the <i>value</i> is omitted, 1 is assumed. The default is that inodes are aligned. Aligned inode access is normally more efficient than unaligned access; alignment must be established at the time the filesystem is created, since inodes are allocated at that time. This option can be used to turn off inode alignment when the filesystem needs to be mountable by a version of IRIX that does not have the inode alignment feature (any release of IRIX before 6.2, and IRIX 6.2 without XFS patches).</p>
<dt><code>attr=</code><i>value</i></p>
<dd>This is used to specify the version of extended attribute inline allocation policy to be used. By default, this is 2, which uses an efficient algorithm for managing the available inline inode space between attribute and extent data.</p>
<dd>The previous version 1, which has fixed regions for attribute and extent data, is kept for backwards compatibility with kernels older than version 2.6.16.</p>
<dt><code>projid32bit[=</code><i>value</i><code>]</code></p>
<dd>This is used to enable 32bit quota project identifiers. The <i>value</i> is either 0 or 1, with 1 signifying that 32bit projid are to be enabled. If the value is omitted, 1 is assumed. (This default changed in release version 3.2.0.)</p>
<dt><code>sparse[=</code><i>value</i><code>]</code></p>
<dd>Enable sparse inode chunk allocation. The <i>value</i> is either 0 or 1, with 1 signifying that sparse allocation is enabled. If the value is omitted, 1 is assumed. Sparse inode allocation is disabled by default. This feature is only available for filesystems formatted with <code>-m crc=1.</code></p>
<dd>When enabled, sparse inode allocation allows the filesystem to allocate smaller than the standard 64-inode chunk when free space is severely limited. This feature is useful for filesystems that might fragment free space over time such that no free extents are large enough to accommodate a chunk of 64 inodes. Without this feature enabled, inode allocations can fail with out of space errors under severe fragmented free space conditions.</dl>
</dl>
<dt><code>-l</code><i> log_section_options</i></p>
<dd>These options specify the location, size, and other parameters of the log section of the filesystem. The valid <i>log_section_options</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>internal[=</code><i>value</i><code>]</code></p>
<dd>This is used to specify that the log section is a piece of the data section instead of being another device or logical volume. The <i>value</i> is either 0 or 1, with 1 signifying that the log is internal. If the <i>value</i> is omitted, 1 is assumed.</p>
<dt><code>logdev=</code><i>device</i></p>
<dd>This is used to specify that the log section should reside on the <i>device</i> separate from the data section. The <code>internal=1</code> and <code>logdev</code> options are mutually exclusive.</p>
<dt><code>size=</code><i>value</i></p>
<dd>This is used to specify the size of the log section.</p>
<dd>If the log is contained within the data section and <code>size</code> isn&#8217;t specified, <code>mkfs.xfs</code> will try to select a suitable log size depending on the size of the filesystem. The actual logsize depends on the filesystem block size and the directory block size.</p>
<dd>Otherwise, the <code>size</code> suboption is only needed if the log section of the filesystem should occupy less space than the size of the special file. The <i>value</i> is specified in bytes or blocks, with a <code>b</code> suffix meaning multiplication by the filesystem block size, as described above. The overriding minimum value for size is 512 blocks. With some combinations of filesystem block size, inode size, and directory block size, the minimum log size is larger than 512 blocks.</p>
<dt><code>version=</code><i>value</i></p>
<dd>This specifies the version of the log. The current default is 2, which allows for larger log buffer sizes, as well as supporting stripe-aligned log writes (see the sunit and su options, below).</p>
<dd>The previous version 1, which is limited to 32k log buffers and does not support stripe-aligned writes, is kept for backwards compatibility with very old 2.4 kernels.</p>
<dt><code>sunit=</code><i>value</i></p>
<dd>This specifies the alignment to be used for log writes. The <i>value</i> has to be specified in 512-byte block units. Use the <code>su</code> suboption to specify the log stripe unit size in bytes. Log writes will be aligned on this boundary, and rounded up to this boundary. This gives major improvements in performance on some configurations such as software RAID5 when the <code>sunit</code> is specified as the filesystem block size. The equivalent byte value must be a multiple of the filesystem block size. Version 2 logs are automatically selected if the log <code>sunit</code> suboption is specified.</p>
<dd>The <code>su</code> suboption is an alternative to using <code>sunit.</code></p>
<dt><code>su=</code><i>value</i></p>
<dd>This is used to specify the log stripe. The <i>value</i> has to be specified in bytes, (usually using the <code>s</code> or <code>b</code> suffixes). This value must be a multiple of the filesystem block size. Version 2 logs are automatically selected if the log <code>su</code> suboption is specified.</p>
<dt><code>lazy-count=</code><i>value</i></p>
<dd>This changes the method of logging various persistent counters in the superblock. Under metadata intensive workloads, these counters are updated and logged frequently enough that the superblock updates become a serialization point in the filesystem. The <i>value</i> can be either 0 or 1.</p>
<dd>With <code>lazy-count=1</code>, the superblock is not modified or logged on every change of the persistent counters. Instead, enough information is kept in other parts of the filesystem to be able to maintain the persistent counter values without needed to keep them in the superblock. This gives significant improvements in performance on some configurations. The default <i>value</i> is 1 (on) so you must specify <code>lazy-count=0</code> if you want to disable this feature for older kernels which don&#8217;t support it.</dl>
</dl>
<dt><code>-n</code><i> naming_options</i></p>
<dd>These options specify the version and size parameters for the naming (directory) area of the filesystem. The valid <i>naming_options</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>size=</code><i>value</i><code> | log=</code><i>value</i></p>
<dd>The block size is specified either as a <i>value</i> in bytes with <code>size=</code>, or as a base two logarithm <i>value</i> with <code>log=</code>. The block size must be a power of 2 and cannot be less than the filesystem block size. The default size <i>value</i> for version 2 directories is 4096 bytes (4 KiB), unless the filesystem block size is larger than 4096, in which case the default <i>value</i> is the filesystem block size. For version 1 directories the block size is the same as the filesystem block size.</p>
<dt><code>version=</code><i>value</i></p>
<dd>The naming (directory) version <i>value</i> can be either 2 or &#8216;ci&#8217;, defaulting to 2 if unspecified. With version 2 directories, the directory block size can be any power of 2 size from the filesystem block size up to 65536.</p>
<dd>The <code>version=ci</code> option enables ASCII only case-insensitive filename lookup and version 2 directories. Filenames are case-preserving, that is, the names are stored in directories using the case they were created with.</p>
<dd>Note: Version 1 directories are not supported.</p>
<dt><code>ftype=</code><i>value</i></p>
<dd>This feature allows the inode type to be stored in the directory structure so that the <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) and <code><a href="/docs/linux/man/2-getdents/">getdents</a></code>(2) do not need to look up the inode to determine the inode type. </p>
<p> The <i>value</i> is either 0 or 1, with 1 signifying that filetype information will be stored in the directory structure. The default value is 1. </p>
<p> When CRCs are enabled (the default), the ftype functionality is always enabled, and cannot be turned off.</p>
<dd></dl>
</dl>
<dt><code>-p</code><i> protofile</i></p>
<dd>If the optional <code>-p</code><i> protofile</i> argument is given, <code>mkfs.xfs</code> uses <i>protofile</i> as a prototype file and takes its directions from that file. The blocks and inodes specifiers in the <i>protofile</i> are provided for backwards compatibility, but are otherwise unused. The syntax of the protofile is defined by a number of tokens separated by spaces or newlines. Note that the line numbers are not part of the syntax but are meant to help you in the following discussion of the file contents. </p>
<pre>1 /stand/<i>diskboot</i>
2 4872 110
3 d--777 3 1
4 usr d--777 3 1
5 sh ---755 3 1 /bin/sh
6 ken d--755 6 1
7 $
8 b0 b--644 3 1 0 0
9 c0 c--644 3 1 0 0
10 fifo p--644 3 1
11 slink l--644 3 1 /a/symbolic/link
12 : This is a comment line
13 $
14 $</pre>
<dd>Line 1 is a dummy string. (It was formerly the bootfilename.) It is present for backward compatibility; boot blocks are not used on SGI systems.</p>
<dd>Note that some string of characters must be present as the first line of the proto file to cause it to be parsed correctly; the value of this string is immaterial since it is ignored.</p>
<dd>Line 2 contains two numeric values (formerly the numbers of blocks and inodes). These are also merely for backward compatibility: two numeric values must appear at this point for the proto file to be correctly parsed, but their values are immaterial since they are ignored.</p>
<dd>The lines 3 through 11 specify the files and directories you want to include in this filesystem. Line 3 defines the root directory. Other directories and files that you want in the filesystem are indicated by lines 4 through 6 and lines 8 through 10. Line 11 contains symbolic link syntax.</p>
<dd>Notice the dollar sign (<code>$</code>) syntax on line 7. This syntax directs the <code>mkfs.xfs</code> command to terminate the branch of the filesystem it is currently on and then continue from the directory specified by the next line, in this case line 8. It must be the last character on a line. The colon on line 12 introduces a comment; all characters up until the following newline are ignored. Note that this means you cannot have a file in a prototype file whose name contains a colon. The <code>$</code> on lines 13 and 14 end the process, since no additional specifications follow.</p>
<dd>File specifications provide the following:</p>
<dd>&nbsp;<wbr>&nbsp;*&nbsp;file mode </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;user ID </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;group ID </p>
<p>&nbsp;<wbr>&nbsp;*&nbsp;the file&#8217;s beginning contents</dl>
<dl>
<dd>A 6-character string defines the mode for a file. The first character of this string defines the file type. The character range for this first character is <code>-bcdpl.</code> A file may be a regular file, a block special file, a character special file, directory files, named pipes (first-in, first out files), and symbolic links. The second character of the mode string is used to specify setuserID mode, in which case it is <code>u</code>. If setuserID mode is not specified, the second character is <code>&#8211;</code>. The third character of the mode string is used to specify the setgroupID mode, in which case it is <code>g</code>. If setgroupID mode is not specified, the third character is <code>&#8211;</code>. The remaining characters of the mode string are a three digit octal number. This octal number defines the owner, group, and other read, write, and execute permissions for the file, respectively. For more information on file permissions, see the <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) command.</p>
<dd>Following the mode character string are two decimal number tokens that specify the user and group IDs of the file&#8217;s owner.</p>
<dd>In a regular file, the next token specifies the pathname from which the contents and size of the file are copied. In a block or character special file, the next token are two decimal numbers that specify the major and minor device numbers. When a file is a symbolic link, the next token specifies the contents of the link. </p>
<p> When the file is a directory, the <code>mkfs.xfs</code> command creates the entries <code>dot</code> (.) and <code>dot-dot</code> (..) and then reads the list of names and file specifications in a recursive manner for all of the entries in the directory. A scan of the protofile is always terminated with the dollar ( <code>$</code> ) token.</p>
<dt><code>-q</code></p>
<dd>Quiet option. Normally <code>mkfs.xfs</code> prints the parameters of the filesystem to be constructed; the <code>-q</code> flag suppresses this.</p>
<dt><code>-r</code><i> realtime_section_options</i></p>
<dd>These options specify the location, size, and other parameters of the real-time section of the filesystem. The valid <i>realtime_section_options</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>rtdev=</code><i>device</i></p>
<dd>This is used to specify the <i>device</i> which should contain the real-time section of the filesystem. The suboption value is the name of a block device.</p>
<dt><code>extsize=</code><i>value</i></p>
<dd>This is used to specify the size of the blocks in the real-time section of the filesystem. This <i>value</i> must be a multiple of the filesystem block size. The minimum allowed size is the filesystem block size or 4 KiB (whichever is larger); the default size is the stripe width for striped volumes or 64 KiB for non-striped volumes; the maximum allowed size is 1 GiB. The real-time extent size should be carefully chosen to match the parameters of the physical media used.</p>
<dt><code>size=</code><i>value</i></p>
<dd>This is used to specify the size of the real-time section. This suboption is only needed if the real-time section of the filesystem should occupy less space than the size of the partition or logical volume containing the section.</p>
<dt><code>noalign</code></p>
<dd>This option disables stripe size detection, enforcing a realtime device with no stripe geometry.</dl>
</dl>
<dt><code>-s</code><i> sector_size</i></p>
<dd>This option specifies the fundamental sector size of the filesystem. The <i>sector_size</i> is specified either as a value in bytes with <code>size=</code><i>value</i> or as a base two logarithm value with <code>log=</code><i>value.</i> The default <i>sector_size</i> is 512 bytes. The minimum value for sector size is 512; the maximum is 32768 (32 KiB). The <i>sector_size</i> must be a power of 2 size and cannot be made larger than the filesystem block size.</p>
<dd>To specify any options on the command line in units of sectors, this option must be specified first so that the sector size is applied consistently to all options.</p>
<dt><code>-L</code><i> label</i></p>
<dd>Set the filesystem <i>label</i>. XFS filesystem labels can be at most 12 characters long; if <i>label</i> is longer than 12 characters, <code>mkfs.xfs</code> will not proceed with creating the filesystem. Refer to the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) and <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8) manual entries for additional information.</p>
<dt><code>-N</code></p>
<dd>Causes the file system parameters to be printed out without really creating the file system.</p>
<dt><code>-K</code></p>
<dd>Do not attempt to discard blocks at mkfs time.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-xfs_info/">xfs_info</a></code>(8), <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8).</p>
<h2>Bugs</h2>
<p>With a prototype file, it is not possible to specify hard links. </p>
