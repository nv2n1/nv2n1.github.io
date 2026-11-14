---
title: "xfs_db(8)"
name: "xfs_db"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_db/"
description: "xfs_db – debug an XFS filesystem"
---

<p>xfs_db &#8211; debug an XFS filesystem</p>
<h2>Synopsis</h2>
<p><code>xfs_db</code> [ <code>-c</code> <i>cmd</i> ] &#8230; [ <code>-i</code>|<code>r</code>|<code>x</code>|<code>F</code> ] [ <code>-f</code> ] [ <code>-l</code> <i>logdev</i> ] [ <code>-p</code> <i>progname</i> ] <i>device</i><br />
 <code>xfs_db -V</code></p>
<h2>Description</h2>
<p><code>xfs_db</code> is used to examine an XFS filesystem. Under rare circumstances it can also be used to modify an XFS filesystem, but that task is normally left to <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8) or to scripts such as <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8) that run <code>xfs_db</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> cmd</i></p>
<dd><code>xfs_db</code> commands may be run interactively (the default) or as arguments on the command line. Multiple <code>-c</code> arguments may be given. The commands are run in the sequence given, then the program exits.</p>
<dt><code>-f</code></p>
<dd>Specifies that the filesystem image to be processed is stored in a regular file at <i>device</i> (see the <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) <code>-d</code> <i>file</i> option). This might happen if an image copy of a filesystem has been made into an ordinary file with <code><a href="/docs/linux/man/8-xfs_copy/">xfs_copy</a></code>(8).</p>
<dt><code>-F</code></p>
<dd>Specifies that we want to continue even if the superblock magic is not correct. For use in <code>xfs_metadump</code>.</p>
<dt><code>-i</code></p>
<dd>Allows execution on a mounted filesystem, provided it is mounted read-only. Useful for shell scripts which must only operate on filesystems in a guaranteed consistent state (either unmounted or mounted read-only). These semantics are slightly different to that of the <code>-r</code> option.</p>
<dt><code>-l</code><i> logdev</i></p>
<dd>Specifies the device where the filesystems external log resides. Only for those filesystems which use an external log. See the <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) <code>-l</code> option, and refer to <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5) for a detailed description of the XFS log.</p>
<dt><code>-p</code><i> progname</i></p>
<dd>Set the program name to <i>progname</i> for prompts and some error messages, the default value is <code>xfs_db</code>.</p>
<dt><code>-r</code></p>
<dd>Open <i>device</i> or <i>filename</i> read-only. This option is required if the filesystem is mounted. It is only necessary to omit this flag if a command that changes data (<code>write</code>, <code>blocktrash</code>, <code>crc</code>) is to be used.</p>
<dt><code>-x</code></p>
<dd>Specifies expert mode. This enables the (<code>write</code>, <code>blocktrash</code>, <code>crc</code> invalidate/revalidate) commands.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.</dl>
<h2>Concepts</h2>
<p><code>xfs_db</code> commands can be broken up into two classes. Most commands are for the navigation and display of data structures in the filesystem. Other commands are for scanning the filesystem in some way. </p>
<p> Commands which are used to navigate the filesystem structure take arguments which reflect the names of filesystem structure fields. There can be multiple field names separated by dots when the underlying structures are nested, as in C. The field names can be indexed (as an array index) if the underlying field is an array. The array indices can be specified as a range, two numbers separated by a dash. </p>
<p> <code>xfs_db</code> maintains a current address in the filesystem. The granularity of the address is a filesystem structure. This can be a filesystem block, an inode or quota (smaller than a filesystem block), or a directory block (could be larger than a filesystem block). There are a variety of commands to set the current address. Associated with the current address is the current data type, which is the structural type of this data. Commands which follow the structure of the filesystem always set the type as well as the address. Commands which examine pieces of an individual file (inode) need the current inode to be set, this is done with the <code>inode</code> command. </p>
<p> The current address/type information is actually maintained in a stack that can be explicitly manipulated with the <code>push</code>, <code>pop</code>, and <code>stack</code> commands. This allows for easy examination of a nested filesystem structure. Also, the last several locations visited are stored in a ring buffer which can be manipulated with the <code>forward</code>, <code>back</code>, and <code>ring</code> commands. </p>
<p> XFS filesystems are divided into a small number of allocation groups. <code>xfs_db</code> maintains a notion of the current allocation group which is manipulated by some commands. The initial allocation group is 0.</p>
<h2>Commands</h2>
<p>Many commands have extensive online help. Use the <code>help</code> command for more details on any command.</p>
<dl>
<dt><code>a</code></p>
<dd>See the <code>addr</code> command.</p>
<dt><code>ablock</code><i> filoff</i></p>
<dd>Set current address to the offset <i>filoff</i> (a filesystem block number) in the attribute area of the current inode.</p>
<dt><code>addr [</code><i>field-expression</i><code>]</code></p>
<dd>Set current address to the value of the <i>field-expression</i>. This is used to &quot;follow&quot; a reference in one structure to the object being referred to. If no argument is given, the current address is printed.</p>
<dt><code>agf [</code><i>agno</i><code>]</code></p>
<dd>Set current address to the AGF block for allocation group <i>agno</i>. If no argument is given, use the current allocation group.</p>
<dt><code>agfl [</code><i>agno</i><code>]</code></p>
<dd>Set current address to the AGFL block for allocation group <i>agno</i>. If no argument is given, use the current allocation group.</p>
<dt><code>agi [</code><i>agno</i><code>]</code></p>
<dd>Set current address to the AGI block for allocation group <i>agno</i>. If no argument is given, use the current allocation group.</p>
<dt><code>b</code></p>
<dd>See the <code>back</code> command.</p>
<dt><code>back</code></p>
<dd>Move to the previous location in the position ring.</p>
<dt><code>blockfree</code></p>
<dd>Free block usage information collected by the last execution of the <code>blockget</code> command. This must be done before another <code>blockget</code> command can be given, presumably with different arguments than the previous one.</p>
<dt><code>blockget [-npvs] [-b </code><i>bno</i><code>] &#8230; [-i </code><i>ino</i><code>] &#8230;</code></p>
<dd>Get block usage and check filesystem consistency. The information is saved for use by a subsequent <code>blockuse</code>, <code>ncheck</code>, or <code>blocktrash</code> command.</p>
<dl>
<dd>
<dl>
<dt><code>-b</code></p>
<dd>is used to specify filesystem block numbers about which verbose information should be printed.</p>
<dt><code>-i</code></p>
<dd>is used to specify inode numbers about which verbose information should be printed.</p>
<dt><code>-n</code></p>
<dd>is used to save pathnames for inodes visited, this is used to support the <code><a href="/docs/linux/man/8-xfs_ncheck/">xfs_ncheck</a></code>(8) command. It also means that pathnames will be printed for inodes that have problems. This option uses a lot of memory so is not enabled by default.</p>
<dt><code>-p</code></p>
<dd>causes error messages to be prefixed with the filesystem name being processed. This is useful if several copies of <code>xfs_db</code> are run in parallel.</p>
<dt><code>-s</code></p>
<dd>restricts output to severe errors only. This is useful if the output is too long otherwise.</p>
<dt><code>-v</code></p>
<dd>enables verbose output. Messages will be printed for every block and inode processed.</dl>
</dl>
<dt><code>blocktrash [-z] [-o </code><i>offset</i><code>] [-n </code><i>count</i><code>] [-x </code><i>min</i><code>] [-y </code><i>max</i><code>] [-s </code><i>seed</i><code>] [-0|1|2|3] [-t </code><i>type</i><code>] &#8230;</code></p>
<dd>Trash randomly selected filesystem metadata blocks. Trashing occurs to randomly selected bits in the chosen blocks. This command is available only in debugging versions of <code>xfs_db</code>. It is useful for testing <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8).</p>
<dl>
<dd>
<dl>
<dt><code>-0</code> | <code>-1</code> | <code>-2</code> | <code>-3</code></p>
<dd>These are used to set the operating mode for <code>blocktrash</code>. Only one can be used: <code>-0</code> changed bits are cleared; <code>-1</code> changed bits are set; <code>-2</code> changed bits are inverted; <code>-3</code> changed bits are randomized.</p>
<dt><code>-n</code></p>
<dd>supplies the <i>count</i> of block-trashings to perform (default 1).</p>
<dt><code>-o</code></p>
<dd>supplies the bit <i>offset</i> at which to start trashing the block. If the value is preceded by a &#8216;+&#8217;, the trashing will start at a randomly chosen offset that is larger than the value supplied. The default is to randomly choose an offset anywhere in the block.</p>
<dt><code>-s</code></p>
<dd>supplies a <i>seed</i> to the random processing.</p>
<dt><code>-t</code></p>
<dd>gives a <i>type</i> of blocks to be selected for trashing. Multiple <code>-t</code> options may be given. If no <code>-t</code> options are given then all metadata types can be trashed.</p>
<dt><code>-x</code></p>
<dd>sets the <i>minimum</i> size of bit range to be trashed. The default value is 1.</p>
<dt><code>-y</code></p>
<dd>sets the <i>maximum</i> size of bit range to be trashed. The default value is 1024.</p>
<dt><code>-z</code></p>
<dd>trashes the block at the top of the stack. It is not necessary to run <code>blockget</code> if this option is supplied.</dl>
</dl>
<dt><code>blockuse [-n] [-c </code><i>count</i><code>]</code></p>
<dd>Print usage for current filesystem block(s). For each block, the type and (if any) inode are printed.</p>
<dl>
<dd>
<dl>
<dt><code>-c</code></p>
<dd>specifies a <i>count</i> of blocks to process. The default value is 1 (the current block only).</p>
<dt><code>-n</code></p>
<dd>specifies that file names should be printed. The prior <code>blockget</code> command must have also specified the <code>-n</code> option.</dl>
</dl>
<dt><code>bmap [-a] [-d] [</code><i>block</i><code> [</code><i>len</i><code>]]</code></p>
<dd>Show the block map for the current inode. The map display can be restricted to an area of the file with the <i>block</i> and <i>len</i> arguments. If <i>block</i> is given and <i>len</i> is omitted then 1 is assumed for len.</p>
<dd>The <code>-a</code> and <code>-d</code> options are used to select the attribute or data area of the inode, if neither option is given then both areas are shown.</p>
<dt><code>check</code></p>
<dd>See the <code>blockget</code> command.</p>
<dt><code>convert </code><i>type number</i><code> [</code><i>type number</i><code>] &#8230; </code><i>type</i></p>
<dd>Convert from one address form to another. The known <i>type</i>s, with alternate names, are:</p>
<dl>
<dd>
<dl>
<dt> <code>agblock</code></p>
<dd>or <code>agbno</code> (filesystem block within an allocation group)</p>
<dt> <code>agino</code></p>
<dd>or <code>aginode</code> (inode number within an allocation group)</p>
<dt> <code>agnumber</code></p>
<dd>or <code>agno</code> (allocation group number)</p>
<dt> <code>bboff</code></p>
<dd>or <code>daddroff</code> (byte offset in a <code>daddr</code>)</p>
<dt> <code>blkoff</code></p>
<dd>or <code>fsboff or</code> <code>agboff</code> (byte offset in a <code>agblock</code> or <code>fsblock</code>)</p>
<dt> <code>byte</code></p>
<dd>or <code>fsbyte</code> (byte address in filesystem)</p>
<dt> <code>daddr</code></p>
<dd>or <code>bb</code> (disk address, 512-byte blocks)</p>
<dt> <code>fsblock</code></p>
<dd>or <code>fsb</code> or <code>fsbno</code> (filesystem block, see the <code>fsblock</code> command)</p>
<dt> <code>ino</code></p>
<dd>or <code>inode</code> (inode number)</p>
<dt> <code>inoidx</code></p>
<dd>or <code>offset</code> (index of inode in filesystem block)</p>
<dt> <code>inooff</code></p>
<dd>or <code>inodeoff</code> (byte offset in inode)</dl>
</dl>
<dd>Only conversions that &quot;make sense&quot; are allowed. The compound form (with more than three arguments) is useful for conversions such as <code>convert agno</code> <i>ag</i> <code>agbno</code> <i>agb</i> <code>fsblock</code>.</p>
<dt><code>crc [-i|-r|-v]</code></p>
<dd>Invalidates, revalidates, or validates the CRC (checksum) field of the current structure, if it has one. This command is available only on CRC-enabled filesystems. With no argument, validation is performed. Each command will display the resulting CRC value and state.</p>
<dl>
<dd>
<dl>
<dt><code>-i</code></p>
<dd>Invalidate the structure&#8217;s CRC value (incrementing it by one), and write it to disk.</p>
<dt><code>-r</code></p>
<dd>Recalculate the current structure&#8217;s correct CRC value, and write it to disk.</p>
<dt><code>-v</code></p>
<dd>Validate and display the current value and state of the structure&#8217;s CRC.</dl>
</dl>
<dt><code>daddr [</code><i>d</i><code>]</code></p>
<dd>Set current address to the daddr (512 byte block) given by <i>d</i>. If no value for <i>d</i> is given, the current address is printed, expressed as a daddr. The type is set to <code>data</code> (uninterpreted).</p>
<dt><code>dblock</code><i> filoff</i></p>
<dd>Set current address to the offset <i>filoff</i> (a filesystem block number) in the data area of the current inode.</p>
<dt><code>debug [</code><i>flagbits</i><code>]</code></p>
<dd>Set debug option bits. These are used for debugging <code>xfs_db</code>. If no value is given for <i>flagbits</i>, print the current debug option bits. These are for the use of the implementor.</p>
<dt><code>dquot [</code><i>-g</i><code>|</code><i>-p</i><code>|</code><i>-u</i><code>]</code><i> id</i></p>
<dd>Set current address to a group, project or user quota block for the given ID. Defaults to user quota.</p>
<dt><code>echo [</code><i>arg</i><code>] &#8230;</code></p>
<dd>Echo the arguments to the output.</p>
<dt><code>f</code></p>
<dd>See the <code>forward</code> command.</p>
<dt><code>forward</code></p>
<dd>Move forward to the next entry in the position ring.</p>
<dt><code>frag [-adflqRrv]</code></p>
<dd>Get file fragmentation data. This prints information about fragmentation of file data in the filesystem (as opposed to fragmentation of freespace, for which see the <code>freesp</code> command). Every file in the filesystem is examined to see how far from ideal its extent mappings are. A summary is printed giving the totals.</p>
<dl>
<dd>
<dl>
<dt><code>-v</code></p>
<dd>sets verbosity, every inode has information printed for it. The remaining options select which inodes and extents are examined. If no options are given then all are assumed set, otherwise just those given are enabled.</p>
<dt><code>-a</code></p>
<dd>enables processing of attribute data.</p>
<dt><code>-d</code></p>
<dd>enables processing of directory data.</p>
<dt><code>-f</code></p>
<dd>enables processing of regular file data.</p>
<dt><code>-l</code></p>
<dd>enables processing of symbolic link data.</p>
<dt><code>-q</code></p>
<dd>enables processing of quota file data.</p>
<dt><code>-R</code></p>
<dd>enables processing of realtime control file data.</p>
<dt><code>-r</code></p>
<dd>enables processing of realtime file data.</dl>
</dl>
<dt><code>freesp [-bcds] [-a </code><i>ag</i><code>] &#8230; [-e </code><i>i</i><code>] [-h </code><i>h1</i><code>] &#8230; [-m </code><i>m</i><code>]</code></p>
<dd>Summarize free space for the filesystem. The free blocks are examined and totalled, and displayed in the form of a histogram, with a count of extents in each range of free extent sizes.</p>
<dl>
<dd>
<dl>
<dt><code>-a</code></p>
<dd>adds <i>ag</i> to the list of allocation groups to be processed. If no <code>-a</code> options are given then all allocation groups are processed.</p>
<dt><code>-b</code></p>
<dd>specifies that the histogram buckets are binary-sized, with the starting sizes being the powers of 2.</p>
<dt><code>-c</code></p>
<dd>specifies that <code>freesp</code> will search the by-size (cnt) space Btree instead of the default by-block (bno) space Btree.</p>
<dt><code>-d</code></p>
<dd>specifies that every free extent will be displayed.</p>
<dt><code>-e</code></p>
<dd>specifies that the histogram buckets are equal-sized, with the size specified as <i>i</i>.</p>
<dt><code>-h</code></p>
<dd>specifies a starting block number for a histogram bucket as <i>h1</i>. Multiple <code>-h</code>&#8216;s are given to specify the complete set of buckets.</p>
<dt><code>-m</code></p>
<dd>specifies that the histogram starting block numbers are powers of <i>m</i>. This is the general case of <code>-b</code>.</p>
<dt><code>-s</code></p>
<dd>specifies that a final summary of total free extents, free blocks, and the average free extent size is printed.</dl>
</dl>
<dt><code>fsb</code></p>
<dd>See the <code>fsblock</code> command.</p>
<dt><code>fsblock [</code><i>fsb</i><code>]</code></p>
<dd>Set current address to the fsblock value given by <i>fsb</i>. If no value for <i>fsb</i> is given the current address is printed, expressed as an fsb. The type is set to <code>data</code> (uninterpreted). XFS filesystem block numbers are computed ((<i>agno</i> &lt;&lt; <i>agshift</i>) | <i>agblock</i>) where <i>agshift</i> depends on the size of an allocation group. Use the <code>convert</code> command to convert to and from this form. Block numbers given for file blocks (for instance from the <code>bmap</code> command) are in this form.</p>
<dt><code>fsmap [ </code><i>start</i><code> ] [ </code><i>end</i><code> ]</code></p>
<dd>Prints the mapping of disk blocks used by an XFS filesystem. The map lists each extent used by files, allocation group metadata, journalling logs, and static filesystem metadata, as well as any regions that are unused. All blocks, offsets, and lengths are specified in units of 512-byte blocks, no matter what the filesystem&#8217;s block size is. <code>The optional </code><i>start</i><code> and </code><i>end</i><code> arguments can be used to constrain</code> the output to a particular range of disk blocks.</p>
<dt><code>hash</code><i> string</i></p>
<dd>Prints the hash value of <i>string</i> using the hash function of the XFS directory and attribute implementation.</p>
<dt><code>help [</code><i>command</i><code>]</code></p>
<dd>Print help for one or all commands.</p>
<dt><code>inode [</code><i>inode#</i><code>]</code></p>
<dd>Set the current inode number. If no <i>inode#</i> is given, print the current inode number.</p>
<dt><code>label [</code><i>label</i><code>]</code></p>
<dd>Set the filesystem label. The filesystem label can be used by <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) instead of using a device special file. The maximum length of an XFS label is 12 characters &#8211; use of a longer <i>label</i> will result in truncation and a warning will be issued. If no <i>label</i> is given, the current filesystem label is printed.</p>
<dt><code>log [stop | start </code><i>filename</i><code>]</code></p>
<dd>Start logging output to <i>filename</i>, stop logging, or print the current logging status.</p>
<dt><code>metadump [-egow] </code><i>filename</i></p>
<dd>Dumps metadata to a file. See <code><a href="/docs/linux/man/8-xfs_metadump/">xfs_metadump</a></code>(8) for more information.</p>
<dt><code>ncheck [-s] [-i </code><i>ino</i><code>] &#8230;</code></p>
<dd>Print name-inode pairs. A <code>blockget -n</code> command must be run first to gather the information.</p>
<dl>
<dd>
<dl>
<dt><code>-i</code></p>
<dd>specifies an inode number to be printed. If no <code>-i</code> options are given then all inodes are printed.</p>
<dt><code>-s</code></p>
<dd>specifies that only setuid and setgid files are printed.</dl>
</dl>
<dt><code>p</code></p>
<dd>See the <code>print</code> command.</p>
<dt><code>pop</code></p>
<dd>Pop location from the stack.</p>
<dt><code>print [</code><i>field-expression</i><code>] &#8230;</code></p>
<dd>Print field values. If no argument is given, print all fields in the current structure.</p>
<dt><code>push [</code><i>command</i><code>]</code></p>
<dd>Push location to the stack. If <i>command</i> is supplied, set the current location to the results of <i>command</i> after pushing the old location.</p>
<dt><code>q</code></p>
<dd>See the <code>quit</code> command.</p>
<dt><code>quit</code></p>
<dd>Exit <code>xfs_db</code>.</p>
<dt><code>ring [</code><i>index</i><code>]</code></p>
<dd>Show position ring (if no <i>index</i> argument is given), or move to a specific entry in the position ring given by <i>index</i>.</p>
<dt><code>sb [</code><i>agno</i><code>]</code></p>
<dd>Set current address to SB header in allocation group <i>agno</i>. If no <i>agno</i> is given, use the current allocation group number.</p>
<dt><code>source </code><i>source-file</i></p>
<dd>Process commands from <i>source-file</i>. <code>source</code> commands can be nested.</p>
<dt><code>stack</code></p>
<dd>View the location stack.</p>
<dt><code>type [</code><i>type</i><code>]</code></p>
<dd>Set the current data type to <i>type</i>. If no argument is given, show the current data type. The possible data types are: <code>agf</code>, <code>agfl</code>, <code>agi</code>, <code>attr</code>, <code>bmapbta</code>, <code>bmapbtd</code>, <code>bnobt</code>, <code>cntbt</code>, <code>data</code>, <code>dir</code>, <code>dir2</code>, <code>dqblk</code>, <code>inobt</code>, <code>inode</code>, <code>log</code>, <code>refcntbt</code>, <code>rmapbt</code>, <code>rtbitmap</code>, <code>rtsummary</code>, <code>sb</code>, <code>symlink</code> and <code>text</code>. See the TYPES section below for more information on these data types.</p>
<dt><code>uuid [</code><i>uuid</i><code> | </code><i>generate</i><code> | </code><i>rewrite</i><code> | </code><i>restore</i><code>]</code></p>
<dd>Set the filesystem universally unique identifier (UUID). The filesystem UUID can be used by <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) instead of using a device special file. The <i>uuid</i> can be set directly to the desired UUID, or it can be automatically generated using the <code>generate</code> option. These options will both write the UUID into every copy of the superblock in the filesystem. On a CRC-enabled filesystem, this will set an incompatible superblock flag, and the filesystem will not be mountable with older kernels. This can be reverted with the <code>restore</code> option, which will copy the original UUID back into place and clear the incompatible flag as needed. <code>rewrite</code> copies the current UUID from the primary superblock to all secondary copies of the superblock. If no argument is given, the current filesystem UUID is printed.</p>
<dt><code>version [</code><i>feature</i><code> | </code><i>versionnum features2</i><code>]</code></p>
<dd>Enable selected features for a filesystem (certain features can be enabled on an unmounted filesystem, after <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) has created the filesystem). Support for unwritten extents can be enabled using the <code>extflg</code> option. Support for version 2 log format can be enabled using the <code>log2</code> option. Support for extended attributes can be enabled using the <code>attr1</code> or <code>attr2</code> option. Once enabled, extended attributes cannot be disabled, but the user may toggle between <code>attr1</code> and <code>attr2</code> at will (older kernels may not support the newer version).</p>
<dd>If no argument is given, the current version and feature bits are printed. With one argument, this command will write the updated version number into every copy of the superblock in the filesystem. If two arguments are given, they will be used as numeric values for the <i>versionnum</i> and <i>features2</i> bits respectively, and their string equivalent reported (but no modifications are made).</p>
<dt><code>write [-c] [</code><i>field value</i><code>] &#8230;</code></p>
<dd>Write a value to disk. Specific fields can be set in structures (struct mode), or a block can be set to data values (data mode), or a block can be set to string values (string mode, for symlink blocks). The operation happens immediately: there is no buffering.</p>
<dd>Struct mode is in effect when the current type is structural, i.e. not data. For struct mode, the syntax is &quot;<code>write</code> <i>field value</i>&quot;.</p>
<dd>Data mode is in effect when the current type is data. In this case the contents of the block can be shifted or rotated left or right, or filled with a sequence, a constant value, or a random value. In this mode <code>write</code> with no arguments gives more information on the allowed commands.</p>
<dl>
<dd>
<dl>
<dt><code>-c</code></p>
<dd>Skip write verifiers and CRC recalculation; allows invalid data to be written to disk.</dl>
</dl>
</dl>
<h2>Types</h2>
<p>This section gives the fields in each structure type and their meanings. Note that some types of block cover multiple actual structures, for instance directory blocks.</p>
<dl>
<dt><code>agf</code></p>
<dd>The AGF block is the header for block allocation information; it is in the second 512-byte block of each allocation group. The following fields are defined:</p>
<dl>
<dd>
<dl>
<dt><code>magicnum</code></p>
<dd>AGF block magic number, 0x58414746 (&#8216;XAGF&#8217;).</p>
<dt><code>versionnum</code></p>
<dd>version number, currently 1.</p>
<dt><code>seqno</code></p>
<dd>sequence number starting from 0.</p>
<dt><code>length</code></p>
<dd>size in filesystem blocks of the allocation group. All allocation groups except the last one of the filesystem have the superblock&#8217;s <code>agblocks</code> value here.</p>
<dt><code>bnoroot</code></p>
<dd>block number of the root of the Btree holding free space information sorted by block number.</p>
<dt><code>cntroot</code></p>
<dd>block number of the root of the Btree holding free space information sorted by block count.</p>
<dt><code>bnolevel</code></p>
<dd>number of levels in the by-block-number Btree.</p>
<dt><code>cntlevel</code></p>
<dd>number of levels in the by-block-count Btree.</p>
<dt><code>flfirst</code></p>
<dd>index into the AGFL block of the first active entry.</p>
<dt><code>fllast</code></p>
<dd>index into the AGFL block of the last active entry.</p>
<dt><code>flcount</code></p>
<dd>count of active entries in the AGFL block.</p>
<dt><code>freeblks</code></p>
<dd>count of blocks represented in the freespace Btrees.</p>
<dt><code>longest</code></p>
<dd>longest free space represented in the freespace Btrees.</p>
<dt><code>btreeblks</code></p>
<dd>number of blocks held in the AGF Btrees.</dl>
</dl>
<dt><code>agfl</code></p>
<dd>The AGFL block contains block numbers for use of the block allocator; it is in the fourth 512-byte block of each allocation group. Each entry in the active list is a block number within the allocation group that can be used for any purpose if space runs low. The AGF block fields <code>flfirst</code>, <code>fllast</code>, and <code>flcount</code> designate which entries are currently active. Entry space is allocated in a circular manner within the AGFL block. Fields defined:</p>
<dl>
<dd>
<dl>
<dt><code>bno</code></p>
<dd>array of all block numbers. Even those which are not active are printed.</dl>
</dl>
<dt><code>agi</code></p>
<dd>The AGI block is the header for inode allocation information; it is in the third 512-byte block of each allocation group. Fields defined:</p>
<dl>
<dd>
<dl>
<dt><code>magicnum</code></p>
<dd>AGI block magic number, 0x58414749 (&#8216;XAGI&#8217;).</p>
<dt><code>versionnum</code></p>
<dd>version number, currently 1.</p>
<dt><code>seqno</code></p>
<dd>sequence number starting from 0.</p>
<dt><code>length</code></p>
<dd>size in filesystem blocks of the allocation group.</p>
<dt><code>count</code></p>
<dd>count of inodes allocated.</p>
<dt><code>root</code></p>
<dd>block number of the root of the Btree holding inode allocation information.</p>
<dt><code>level</code></p>
<dd>number of levels in the inode allocation Btree.</p>
<dt><code>freecount</code></p>
<dd>count of allocated inodes that are not in use.</p>
<dt><code>newino</code></p>
<dd>last inode number allocated.</p>
<dt><code>dirino</code></p>
<dd>unused.</p>
<dt><code>unlinked</code></p>
<dd>an array of inode numbers within the allocation group. The entries in the AGI block are the heads of lists which run through the inode <code>next_unlinked</code> field. These inodes are to be unlinked the next time the filesystem is mounted.</dl>
</dl>
<dt><code>attr</code></p>
<dd>An attribute fork is organized as a Btree with the actual data embedded in the leaf blocks. The root of the Btree is found in block 0 of the fork. The index (sort order) of the Btree is the hash value of the attribute name. All the blocks contain a <code>blkinfo</code> structure at the beginning, see type <code>dir</code> for a description. Nonleaf blocks are identical in format to those for version 1 and version 2 directories, see type <code>dir</code> for a description. Leaf blocks can refer to &quot;local&quot; or &quot;remote&quot; attribute values. Local values are stored directly in the leaf block. Remote values are stored in an independent block in the attribute fork (with no structure). Leaf blocks contain the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>hdr</code></p>
<dd>header containing a <code>blkinfo</code> structure <code>info</code> (magic number 0xfbee), a <code>count</code> of active entries, <code>usedbytes</code> total bytes of names and values, the <code>firstused</code> byte in the name area, <code>holes</code> set if the block needs compaction, and array <code>freemap</code> as for <code>dir</code> leaf blocks.</p>
<dt><code>entries</code></p>
<dd>array of structures containing a <code>hashval</code>, <code>nameidx</code> (index into the block of the name), and flags <code>incomplete</code>, <code>root</code>, and <code>local</code>.</p>
<dt><code>nvlist</code></p>
<dd>array of structures describing the attribute names and values. Fields always present: <code>valuelen</code> (length of value in bytes), <code>namelen</code>, and <code>name</code>. Fields present for local values: <code>value</code> (value string). Fields present for remote values: <code>valueblk</code> (fork block number of containing the value).</dl>
</dl>
<dt><code>bmapbt</code></p>
<dd>Files with many extents in their data or attribute fork will have the extents described by the contents of a Btree for that fork, instead of being stored directly in the inode. Each bmap Btree starts with a root block contained within the inode. The other levels of the Btree are stored in filesystem blocks. The blocks are linked to sibling left and right blocks at each level, as well as by pointers from parent to child blocks. Each block contains the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>magic</code></p>
<dd>bmap Btree block magic number, 0x424d4150 (&#8216;BMAP&#8217;).</p>
<dt><code>level</code></p>
<dd>level of this block above the leaf level.</p>
<dt><code>numrecs</code></p>
<dd>number of records or keys in the block.</p>
<dt><code>leftsib</code></p>
<dd>left (logically lower) sibling block, 0 if none.</p>
<dt><code>rightsib</code></p>
<dd>right (logically higher) sibling block, 0 if none.</p>
<dt><code>recs</code></p>
<dd>[leaf blocks only] array of extent records. Each record contains <code>startoff</code>, <code>startblock</code>, <code>blockcount</code>, and <code>extentflag</code> (1 if the extent is unwritten).</p>
<dt><code>keys</code></p>
<dd>[non-leaf blocks only] array of key records. These are the first key value of each block in the level below this one. Each record contains <code>startoff</code>.</p>
<dt><code>ptrs</code></p>
<dd>[non-leaf blocks only] array of child block pointers. Each pointer is a filesystem block number to the next level in the Btree.</dl>
</dl>
<dt><code>bnobt</code></p>
<dd>There is one set of filesystem blocks forming the by-block-number allocation Btree for each allocation group. The root block of this Btree is designated by the <code>bnoroot</code> field in the corresponding AGF block. The blocks are linked to sibling left and right blocks at each level, as well as by pointers from parent to child blocks. Each block has the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>magic</code></p>
<dd>BNOBT block magic number, 0x41425442 (&#8216;ABTB&#8217;).</p>
<dt><code>level</code></p>
<dd>level number of this block, 0 is a leaf.</p>
<dt><code>numrecs</code></p>
<dd>number of data entries in the block.</p>
<dt><code>leftsib</code></p>
<dd>left (logically lower) sibling block, 0 if none.</p>
<dt><code>rightsib</code></p>
<dd>right (logically higher) sibling block, 0 if none.</p>
<dt><code>recs</code></p>
<dd>[leaf blocks only] array of freespace records. Each record contains <code>startblock</code> and <code>blockcount</code>.</p>
<dt><code>keys</code></p>
<dd>[non-leaf blocks only] array of key records. These are the first value of each block in the level below this one. Each record contains <code>startblock</code> and <code>blockcount</code>.</p>
<dt><code>ptrs</code></p>
<dd>[non-leaf blocks only] array of child block pointers. Each pointer is a block number within the allocation group to the next level in the Btree.</dl>
</dl>
<dt><code>cntbt</code></p>
<dd>There is one set of filesystem blocks forming the by-block-count allocation Btree for each allocation group. The root block of this Btree is designated by the <code>cntroot</code> field in the corresponding AGF block. The blocks are linked to sibling left and right blocks at each level, as well as by pointers from parent to child blocks. Each block has the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>magic</code></p>
<dd>CNTBT block magic number, 0x41425443 (&#8216;ABTC&#8217;).</p>
<dt><code>level</code></p>
<dd>level number of this block, 0 is a leaf.</p>
<dt><code>numrecs</code></p>
<dd>number of data entries in the block.</p>
<dt><code>leftsib</code></p>
<dd>left (logically lower) sibling block, 0 if none.</p>
<dt><code>rightsib</code></p>
<dd>right (logically higher) sibling block, 0 if none.</p>
<dt><code>recs</code></p>
<dd>[leaf blocks only] array of freespace records. Each record contains <code>startblock</code> and <code>blockcount</code>.</p>
<dt><code>keys</code></p>
<dd>[non-leaf blocks only] array of key records. These are the first value of each block in the level below this one. Each record contains <code>blockcount</code> and <code>startblock</code>.</p>
<dt><code>ptrs</code></p>
<dd>[non-leaf blocks only] array of child block pointers. Each pointer is a block number within the allocation group to the next level in the Btree.</dl>
</dl>
<dt><code>data</code></p>
<dd>User file blocks, and other blocks whose type is unknown, have this type for display purposes in <code>xfs_db</code>. The block data is displayed in hexadecimal format.</p>
<dt><code>dir</code></p>
<dd>A version 1 directory is organized as a Btree with the directory data embedded in the leaf blocks. The root of the Btree is found in block 0 of the file. The index (sort order) of the Btree is the hash value of the entry name. All the blocks contain a <code>blkinfo</code> structure at the beginning with the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>forw</code></p>
<dd>next sibling block.</p>
<dt><code>back</code></p>
<dd>previous sibling block.</p>
<dt><code>magic</code></p>
<dd>magic number for this block type.</dl>
</dl>
<dd>The non-leaf (node) blocks have the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>hdr</code></p>
<dd>header containing a <code>blkinfo</code> structure <code>info</code> (magic number 0xfebe), the <code>count</code> of active entries, and the <code>level</code> of this block above the leaves.</p>
<dt><code>btree</code></p>
<dd>array of entries containing <code>hashval</code> and <code>before</code> fields. The <code>before</code> value is a block number within the directory file to the child block, the <code>hashval</code> is the last hash value in that block.</dl>
</dl>
<dd>The leaf blocks have the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>hdr</code></p>
<dd>header containing a <code>blkinfo</code> structure <code>info</code> (magic number 0xfeeb), the <code>count</code> of active entries, <code>namebytes</code> (total name string bytes), <code>holes</code> flag (block needs compaction), and <code>freemap</code> (array of <code>base</code>, <code>size</code> entries for free regions).</p>
<dt><code>entries</code></p>
<dd>array of structures containing <code>hashval</code>, <code>nameidx</code> (byte index into the block of the name string), and <code>namelen</code>.</p>
<dt><code>namelist</code></p>
<dd>array of structures containing <code>inumber</code> and <code>name</code>.</dl>
</dl>
<dt><code>dir2</code></p>
<dd>A version 2 directory has four kinds of blocks. Data blocks start at offset 0 in the file. There are two kinds of data blocks: single-block directories have the leaf information embedded at the end of the block, data blocks in multi-block directories do not. Node and leaf blocks start at offset 32GiB (with either a single leaf block or the root node block). Freespace blocks start at offset 64GiB. The node and leaf blocks form a Btree, with references to the data in the data blocks. The freespace blocks form an index of longest free spaces within the data blocks.</p>
<dd>A single-block directory block contains the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>bhdr</code></p>
<dd>header containing <code>magic</code> number 0x58443242 (&#8216;XD2B&#8217;) and an array <code>bestfree</code> of the longest 3 free spaces in the block (<code>offset</code>, <code>length</code>).</p>
<dt><code>bu</code></p>
<dd>array of union structures. Each element is either an entry or a freespace. For entries, there are the following fields: <code>inumber</code>, <code>namelen</code>, <code>name</code>, and <code>tag</code>. For freespace, there are the following fields: <code>freetag</code> (0xffff), <code>length</code>, and <code>tag</code>. The <code>tag</code> value is the byte offset in the block of the start of the entry it is contained in.</p>
<dt><code>bleaf</code></p>
<dd>array of leaf entries containing <code>hashval</code> and <code>address</code>. The <code>address</code> is a 64-bit word offset into the file.</p>
<dt><code>btail</code></p>
<dd>tail structure containing the total <code>count</code> of leaf entries and <code>stale</code> count of unused leaf entries.</dl>
</dl>
<dd>A data block contains the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>dhdr</code></p>
<dd>header containing <code>magic</code> number 0x58443244 (&#8216;XD2D&#8217;) and an array <code>bestfree</code> of the longest 3 free spaces in the block (<code>offset</code>, <code>length</code>).</p>
<dt><code>du</code></p>
<dd>array of union structures as for <code>bu</code>.</dl>
</dl>
<dd>Leaf blocks have two possible forms. If the Btree consists of a single leaf then the freespace information is in the leaf block, otherwise it is in separate blocks and the root of the Btree is a node block. A leaf block contains the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>lhdr</code></p>
<dd>header containing a <code>blkinfo</code> structure <code>info</code> (magic number 0xd2f1 for the single leaf case, 0xd2ff for the true Btree case), the total <code>count</code> of leaf entries, and <code>stale</code> count of unused leaf entries.</p>
<dt><code>lents</code></p>
<dd>leaf entries, as for <code>bleaf</code>.</p>
<dt><code>lbests</code></p>
<dd>[single leaf only] array of values which represent the longest freespace in each data block in the directory.</p>
<dt><code>ltail</code></p>
<dd>[single leaf only] tail structure containing <code>bestcount</code> count of <code>lbests</code>.</dl>
</dl>
<dd>A node block is identical to that for types <code>attr</code> and <code>dir</code>. </p>
<p> A freespace block contains the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>fhdr</code></p>
<dd>header containing <code>magic</code> number 0x58443246 (&#8216;XD2F&#8217;), <code>firstdb</code> first data block number covered by this freespace block, <code>nvalid</code> number of valid entries, and <code>nused</code> number of entries representing real data blocks.</p>
<dt><code>fbests</code></p>
<dd>array of values as for <code>lbests</code>.</dl>
</dl>
<dt><code>dqblk</code></p>
<dd>The quota information is stored in files referred to by the superblock <code>uquotino</code> and <code>pquotino</code> fields. Each filesystem block in a quota file contains a constant number of quota entries. The quota entry size is currently 136 bytes, so with a 4KiB filesystem block size there are 30 quota entries per block. The <code>dquot</code> command is used to locate these entries in the filesystem. The file entries are indexed by the user or project identifier to determine the block and offset. Each quota entry has the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>magic</code></p>
<dd>magic number, 0x4451 (&#8216;DQ&#8217;).</p>
<dt><code>version</code></p>
<dd>version number, currently 1.</p>
<dt><code>flags</code></p>
<dd>flags, values include 0x01 for user quota, 0x02 for project quota.</p>
<dt><code>id</code></p>
<dd>user or project identifier.</p>
<dt><code>blk_hardlimit</code></p>
<dd>absolute limit on blocks in use.</p>
<dt><code>blk_softlimit</code></p>
<dd>preferred limit on blocks in use.</p>
<dt><code>ino_hardlimit</code></p>
<dd>absolute limit on inodes in use.</p>
<dt><code>ino_softlimit</code></p>
<dd>preferred limit on inodes in use.</p>
<dt><code>bcount</code></p>
<dd>blocks actually in use.</p>
<dt><code>icount</code></p>
<dd>inodes actually in use.</p>
<dt><code>itimer</code></p>
<dd>time when service will be refused if soft limit is violated for inodes.</p>
<dt><code>btimer</code></p>
<dd>time when service will be refused if soft limit is violated for blocks.</p>
<dt><code>iwarns</code></p>
<dd>number of warnings issued about inode limit violations.</p>
<dt><code>bwarns</code></p>
<dd>number of warnings issued about block limit violations.</p>
<dt><code>rtb_hardlimit</code></p>
<dd>absolute limit on realtime blocks in use.</p>
<dt><code>rtb_softlimit</code></p>
<dd>preferred limit on realtime blocks in use.</p>
<dt><code>rtbcount</code></p>
<dd>realtime blocks actually in use.</p>
<dt><code>rtbtimer</code></p>
<dd>time when service will be refused if soft limit is violated for realtime blocks.</p>
<dt><code>rtbwarns</code></p>
<dd>number of warnings issued about realtime block limit violations.</dl>
</dl>
<dt><code>inobt</code></p>
<dd>There is one set of filesystem blocks forming the inode allocation Btree for each allocation group. The root block of this Btree is designated by the <code>root</code> field in the corresponding AGI block. The blocks are linked to sibling left and right blocks at each level, as well as by pointers from parent to child blocks. Each block has the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>magic</code></p>
<dd>INOBT block magic number, 0x49414254 (&#8216;IABT&#8217;).</p>
<dt><code>level</code></p>
<dd>level number of this block, 0 is a leaf.</p>
<dt><code>numrecs</code></p>
<dd>number of data entries in the block.</p>
<dt><code>leftsib</code></p>
<dd>left (logically lower) sibling block, 0 if none.</p>
<dt><code>rightsib</code></p>
<dd>right (logically higher) sibling block, 0 if none.</p>
<dt><code>recs</code></p>
<dd>[leaf blocks only] array of inode records. Each record contains <code>startino</code> allocation-group relative inode number, <code>freecount</code> count of free inodes in this chunk, and <code>free</code> bitmap, LSB corresponds to inode 0.</p>
<dt><code>keys</code></p>
<dd>[non-leaf blocks only] array of key records. These are the first value of each block in the level below this one. Each record contains <code>startino</code>.</p>
<dt><code>ptrs</code></p>
<dd>[non-leaf blocks only] array of child block pointers. Each pointer is a block number within the allocation group to the next level in the Btree.</dl>
</dl>
<dt><code>inode</code></p>
<dd>Inodes are allocated in &quot;chunks&quot; of 64 inodes each. Usually a chunk is multiple filesystem blocks, although there are cases with large filesystem blocks where a chunk is less than one block. The inode Btree (see <code>inobt</code> above) refers to the inode numbers per allocation group. The inode numbers directly reflect the location of the inode block on disk. Use the <code>inode</code> command to point <code>xfs_db</code> to a specific inode. Each inode contains four regions: <code>core</code>, <code>next_unlinked</code>, <code>u</code>, and <code>a</code>. <code>core</code> contains the fixed information. <code>next_unlinked</code> is separated from the core due to journaling considerations, see type <code>agi</code> field <code>unlinked</code>. <code>u</code> is a union structure that is different in size and format depending on the type and representation of the file data (&quot;data fork&quot;). <code>a</code> is an optional union structure to describe attribute data, that is different in size, format, and location depending on the presence and representation of attribute data, and the size of the <code>u</code> data (&quot;attribute fork&quot;). <code>xfs_db</code> automatically selects the proper union members based on information in the inode.</p>
<dd>The following are fields in the inode core:</p>
<dl>
<dd>
<dl>
<dt><code>magic</code></p>
<dd>inode magic number, 0x494e (&#8216;IN&#8217;).</p>
<dt><code>mode</code></p>
<dd>mode and type of file, as described in <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), and <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2).</p>
<dt><code>version</code></p>
<dd>inode version, 1 or 2.</p>
<dt><code>format</code></p>
<dd>format of <code>u</code> union data (0: xfs_dev_t, 1: local file &#8211; in-inode directory or symlink, 2: extent list, 3: Btree root, 4: unique id [unused]).</p>
<dt><code>nlinkv1</code></p>
<dd>number of links to the file in a version 1 inode.</p>
<dt><code>nlinkv2</code></p>
<dd>number of links to the file in a version 2 inode.</p>
<dt><code>projid_lo</code></p>
<dd>owner&#8217;s project id (low word; version 2 inode only). <code>projid_hi</code> owner&#8217;s project id (high word; version 2 inode only).</p>
<dt><code>uid</code></p>
<dd>owner&#8217;s user id.</p>
<dt><code>gid</code></p>
<dd>owner&#8217;s group id.</p>
<dt><code>atime</code></p>
<dd>time last accessed (seconds and nanoseconds).</p>
<dt><code>mtime</code></p>
<dd>time last modified.</p>
<dt><code>ctime</code></p>
<dd>time created or inode last modified.</p>
<dt><code>size</code></p>
<dd>number of bytes in the file.</p>
<dt><code>nblocks</code></p>
<dd>total number of blocks in the file including indirect and attribute.</p>
<dt><code>extsize</code></p>
<dd>basic/minimum extent size for the file.</p>
<dt><code>nextents</code></p>
<dd>number of extents in the data fork.</p>
<dt><code>naextents</code></p>
<dd>number of extents in the attribute fork.</p>
<dt><code>forkoff</code></p>
<dd>attribute fork offset in the inode, in 64-bit words from the start of <code>u</code>.</p>
<dt><code>aformat</code></p>
<dd>format of <code>a</code> data (1: local attribute data, 2: extent list, 3: Btree root).</p>
<dt><code>dmevmask</code></p>
<dd>DMAPI event mask.</p>
<dt><code>dmstate</code></p>
<dd>DMAPI state information.</p>
<dt><code>newrtbm</code></p>
<dd>file is the realtime bitmap and is &quot;new&quot; format.</p>
<dt><code>prealloc</code></p>
<dd>file has preallocated data space after EOF.</p>
<dt><code>realtime</code></p>
<dd>file data is in the realtime subvolume.</p>
<dt><code>gen</code></p>
<dd>inode generation number.</dl>
</dl>
<dd>The following fields are in the <code>u</code> data fork union:</p>
<dl>
<dd>
<dl>
<dt><code>bmbt</code></p>
<dd>bmap Btree root. This looks like a <code>bmapbtd</code> block with redundant information removed.</p>
<dt><code>bmx</code></p>
<dd>array of extent descriptors.</p>
<dt><code>dev</code></p>
<dd>dev_t for the block or character device.</p>
<dt><code>sfdir</code></p>
<dd>shortform (in-inode) version 1 directory. This consists of a <code>hdr</code> containing the <code>parent</code> inode number and a <code>count</code> of active entries in the directory, followed by an array <code>list</code> of <code>hdr.count</code> entries. Each such entry contains <code>inumber</code>, <code>namelen</code>, and <code>name</code> string.</p>
<dt><code>sfdir2</code></p>
<dd>shortform (in-inode) version 2 directory. This consists of a <code>hdr</code> containing a <code>count</code> of active entries in the directory, an <code>i8count</code> of entries with inumbers that don&#8217;t fit in a 32-bit value, and the <code>parent</code> inode number, followed by an array <code>list</code> of <code>hdr.count</code> entries. Each such entry contains <code>namelen</code>, a saved <code>offset</code> used when the directory is converted to a larger form, a <code>name</code> string, and the <code>inumber</code>.</p>
<dt><code>symlink</code></p>
<dd>symbolic link string value.</dl>
</dl>
<dd>The following fields are in the <code>a</code> attribute fork union if it exists:</p>
<dl>
<dd>
<dl>
<dt><code>bmbt</code></p>
<dd>bmap Btree root, as above.</p>
<dt><code>bmx</code></p>
<dd>array of extent descriptors.</p>
<dt><code>sfattr</code></p>
<dd>shortform (in-inode) attribute values. This consists of a <code>hdr</code> containing a <code>totsize</code> (total size in bytes) and a <code>count</code> of active entries, followed by an array <code>list</code> of <code>hdr.count</code> entries. Each such entry contains <code>namelen</code>, <code>valuelen</code>, <code>root</code> flag, <code>name</code>, and <code>value</code>.</dl>
</dl>
<dt><code>log</code></p>
<dd>Log blocks contain the journal entries for XFS. It&#8217;s not useful to examine these with <code>xfs_db</code>, use <code><a href="/docs/linux/man/8-xfs_logprint/">xfs_logprint</a></code>(8) instead.</p>
<dt><code>refcntbt</code></p>
<dd>There is one set of filesystem blocks forming the reference count Btree for each allocation group. The root block of this Btree is designated by the <code>refcntroot</code> field in the corresponding AGF block. The blocks are linked to sibling left and right blocks at each level, as well as by pointers from parent to child blocks. Each block has the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>magic</code></p>
<dd>REFC block magic number, 0x52334643 (&#8216;R3FC&#8217;).</p>
<dt><code>level</code></p>
<dd>level number of this block, 0 is a leaf.</p>
<dt><code>numrecs</code></p>
<dd>number of data entries in the block.</p>
<dt><code>leftsib</code></p>
<dd>left (logically lower) sibling block, 0 if none.</p>
<dt><code>rightsib</code></p>
<dd>right (logically higher) sibling block, 0 if none.</p>
<dt><code>recs</code></p>
<dd>[leaf blocks only] array of reference count records. Each record contains <code>startblock</code>, <code>blockcount</code>, and <code>refcount</code>.</p>
<dt><code>keys</code></p>
<dd>[non-leaf blocks only] array of key records. These are the first value of each block in the level below this one. Each record contains <code>startblock</code>.</p>
<dt><code>ptrs</code></p>
<dd>[non-leaf blocks only] array of child block pointers. Each pointer is a block number within the allocation group to the next level in the Btree.</dl>
</dl>
<dt><code>rmapbt</code></p>
<dd>There is one set of filesystem blocks forming the reverse mapping Btree for each allocation group. The root block of this Btree is designated by the <code>rmaproot</code> field in the corresponding AGF block. The blocks are linked to sibling left and right blocks at each level, as well as by pointers from parent to child blocks. Each block has the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>magic</code></p>
<dd>RMAP block magic number, 0x524d4233 (&#8216;RMB3&#8217;).</p>
<dt><code>level</code></p>
<dd>level number of this block, 0 is a leaf.</p>
<dt><code>numrecs</code></p>
<dd>number of data entries in the block.</p>
<dt><code>leftsib</code></p>
<dd>left (logically lower) sibling block, 0 if none.</p>
<dt><code>rightsib</code></p>
<dd>right (logically higher) sibling block, 0 if none.</p>
<dt><code>recs</code></p>
<dd>[leaf blocks only] array of reference count records. Each record contains <code>startblock</code>, <code>blockcount</code>, <code>owner</code>, <code>offset</code>, <code>attr_fork</code>, <code>bmbt_block</code>, and <code>unwritten</code>.</p>
<dt><code>keys</code></p>
<dd>[non-leaf blocks only] array of double-key records. The first (&quot;low&quot;) key contains the first value of each block in the level below this one. The second (&quot;high&quot;) key contains the largest key that can be used to identify any record in the subtree. Each record contains <code>startblock</code>, <code>owner</code>, <code>offset</code>, <code>attr_fork</code>, and <code>bmbt_block</code>.</p>
<dt><code>ptrs</code></p>
<dd>[non-leaf blocks only] array of child block pointers. Each pointer is a block number within the allocation group to the next level in the Btree.</dl>
</dl>
<dt><code>rtbitmap</code></p>
<dd>If the filesystem has a realtime subvolume, then the <code>rbmino</code> field in the superblock refers to a file that contains the realtime bitmap. Each bit in the bitmap file controls the allocation of a single realtime extent (set == free). The bitmap is processed in 32-bit words, the LSB of a word is used for the first extent controlled by that bitmap word. The <code>atime</code> field of the realtime bitmap inode contains a counter that is used to control where the next new realtime file will start.</p>
<dt><code>rtsummary</code></p>
<dd>If the filesystem has a realtime subvolume, then the <code>rsumino</code> field in the superblock refers to a file that contains the realtime summary data. The summary file contains a two-dimensional array of 16-bit values. Each value counts the number of free extent runs (consecutive free realtime extents) of a given range of sizes that starts in a given bitmap block. The size ranges are binary buckets (low size in the bucket is a power of 2). There are as many size ranges as are necessary given the size of the realtime subvolume. The first dimension is the size range, the second dimension is the starting bitmap block number (adjacent entries are for the same size, adjacent bitmap blocks).</p>
<dt><code>sb</code></p>
<dd>There is one sb (superblock) structure per allocation group. It is the first disk block in the allocation group. Only the first one (block 0 of the filesystem) is actually used; the other blocks are redundant information for <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8) to use if the first superblock is damaged. Fields defined:</p>
<dl>
<dd>
<dl>
<dt><code>magicnum</code></p>
<dd>superblock magic number, 0x58465342 (&#8216;XFSB&#8217;).</p>
<dt><code>blocksize</code></p>
<dd>filesystem block size in bytes.</p>
<dt><code>dblocks</code></p>
<dd>number of filesystem blocks present in the data subvolume.</p>
<dt><code>rblocks</code></p>
<dd>number of filesystem blocks present in the realtime subvolume.</p>
<dt><code>rextents</code></p>
<dd>number of realtime extents that <code>rblocks</code> contain.</p>
<dt><code>uuid</code></p>
<dd>unique identifier of the filesystem.</p>
<dt><code>logstart</code></p>
<dd>starting filesystem block number of the log (journal). If this value is 0 the log is &quot;external&quot;.</p>
<dt><code>rootino</code></p>
<dd>root inode number.</p>
<dt><code>rbmino</code></p>
<dd>realtime bitmap inode number.</p>
<dt><code>rsumino</code></p>
<dd>realtime summary data inode number.</p>
<dt><code>rextsize</code></p>
<dd>realtime extent size in filesystem blocks.</p>
<dt><code>agblocks</code></p>
<dd>size of an allocation group in filesystem blocks.</p>
<dt><code>agcount</code></p>
<dd>number of allocation groups.</p>
<dt><code>rbmblocks</code></p>
<dd>number of realtime bitmap blocks.</p>
<dt><code>logblocks</code></p>
<dd>number of log blocks (filesystem blocks).</p>
<dt><code>versionnum</code></p>
<dd>filesystem version information. This value is currently 1, 2, 3, or 4 in the low 4 bits. If the low bits are 4 then the other bits have additional meanings. 1 is the original value. 2 means that attributes were used. 3 means that version 2 inodes (large link counts) were used. 4 is the bitmask version of the version number. In this case, the other bits are used as flags (0x0010: attributes were used, 0x0020: version 2 inodes were used, 0x0040: quotas were used, 0x0080: inode cluster alignment is in force, 0x0100: data stripe alignment is in force, 0x0200: the <code>shared_vn</code> field is used, 0x1000: unwritten extent tracking is on, 0x2000: version 2 directories are in use).</p>
<dt><code>sectsize</code></p>
<dd>sector size in bytes, currently always 512. This is the size of the superblock and the other header blocks.</p>
<dt><code>inodesize</code></p>
<dd>inode size in bytes.</p>
<dt><code>inopblock</code></p>
<dd>number of inodes per filesystem block.</p>
<dt><code>fname</code></p>
<dd>obsolete, filesystem name.</p>
<dt><code>fpack</code></p>
<dd>obsolete, filesystem pack name.</p>
<dt><code>blocklog</code></p>
<dd>log2 of <code>blocksize</code>.</p>
<dt><code>sectlog</code></p>
<dd>log2 of <code>sectsize</code>.</p>
<dt><code>inodelog</code></p>
<dd>log2 of <code>inodesize</code>.</p>
<dt><code>inopblog</code></p>
<dd>log2 of <code>inopblock</code>.</p>
<dt><code>agblklog</code></p>
<dd>log2 of <code>agblocks</code> (rounded up).</p>
<dt><code>rextslog</code></p>
<dd>log2 of <code>rextents</code>.</p>
<dt><code>inprogress</code></p>
<dd><code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) or <code><a href="/docs/linux/man/8-xfs_copy/">xfs_copy</a></code>(8) aborted before completing this filesystem.</p>
<dt><code>imax_pct</code></p>
<dd>maximum percentage of filesystem space used for inode blocks.</p>
<dt><code>icount</code></p>
<dd>number of allocated inodes.</p>
<dt><code>ifree</code></p>
<dd>number of allocated inodes that are not in use.</p>
<dt><code>fdblocks</code></p>
<dd>number of free data blocks.</p>
<dt><code>frextents</code></p>
<dd>number of free realtime extents.</p>
<dt><code>uquotino</code></p>
<dd>user quota inode number.</p>
<dt><code>pquotino</code></p>
<dd>project quota inode number; this is currently unused.</p>
<dt><code>qflags</code></p>
<dd>quota status flags (0x01: user quota accounting is on, 0x02: user quota limits are enforced, 0x04: quotacheck has been run on user quotas, 0x08: project quota accounting is on, 0x10: project quota limits are enforced, 0x20: quotacheck has been run on project quotas).</p>
<dt><code>flags</code></p>
<dd>random flags. 0x01: only read-only mounts are allowed.</p>
<dt><code>shared_vn</code></p>
<dd>shared version number (shared readonly filesystems).</p>
<dt><code>inoalignmt</code></p>
<dd>inode chunk alignment in filesystem blocks.</p>
<dt><code>unit</code></p>
<dd>stripe or RAID unit.</p>
<dt><code>width</code></p>
<dd>stripe or RAID width.</p>
<dt><code>dirblklog</code></p>
<dd>log2 of directory block size (filesystem blocks).</dl>
</dl>
<dt><code>symlink</code></p>
<dd>Symbolic link blocks are used only when the symbolic link value does not fit inside the inode. The block content is just the string value. Bytes past the logical end of the symbolic link value have arbitrary values.</p>
<dt><code>text</code></p>
<dd>User file blocks, and other blocks whose type is unknown, have this type for display purposes in <code>xfs_db</code>. The block data is displayed in two columns: Hexadecimal format and printable ASCII chars.</dl>
<h2>Diagnostics</h2>
<p>Many messages can come from the <code>check</code> (<code>blockget</code>) command. If the filesystem is completely corrupt, a core dump might be produced instead of the message</p>
<dl>
<dd><i>device</i> <code>is not a valid filesystem</code></dl>
<p> If the filesystem is very large (has many files) then <code>check</code> might run out of memory. In this case the message</p>
<dl>
<dd><code>out of memory</code></dl>
<p> is printed. </p>
<p> The following is a description of the most likely problems and the associated messages. Most of the diagnostics produced are only meaningful with an understanding of the structure of the filesystem.</p>
<dl>
<dt><code>agf_freeblks </code><i>n</i><code>, counted </code><i>m</i><code> in ag </code><i>a</i></p>
<dd>The freeblocks count in the allocation group header for allocation group <i>a</i> doesn&#8217;t match the number of blocks counted free.</p>
<dt><code>agf_longest </code><i>n</i><code>, counted </code><i>m</i><code> in ag </code><i>a</i></p>
<dd>The longest free extent in the allocation group header for allocation group <i>a</i> doesn&#8217;t match the longest free extent found in the allocation group.</p>
<dt><code>agi_count </code><i>n</i><code>, counted </code><i>m</i><code> in ag </code><i>a</i></p>
<dd>The allocated inode count in the allocation group header for allocation group <i>a</i> doesn&#8217;t match the number of inodes counted in the allocation group.</p>
<dt><code>agi_freecount </code><i>n</i><code>, counted </code><i>m</i><code> in ag </code><i>a</i></p>
<dd>The free inode count in the allocation group header for allocation group <i>a</i> doesn&#8217;t match the number of inodes counted free in the allocation group.</p>
<dt><code>block </code><i>a/b</i><code> expected inum 0 got </code><i>i</i></p>
<dd>The block number is specified as a pair (allocation group number, block in the allocation group). The block is used multiple times (shared), between multiple inodes. This message usually follows a message of the next type.</p>
<dt><code>block </code><i>a/b</i><code> expected type unknown got </code><i>y</i></p>
<dd>The block is used multiple times (shared).</p>
<dt><code>block </code><i>a/b</i><code> type unknown not expected</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/8-xfs_admin/">xfs_admin</a></code>(8), <code><a href="/docs/linux/man/8-xfs_copy/">xfs_copy</a></code>(8), <code><a href="/docs/linux/man/8-xfs_logprint/">xfs_logprint</a></code>(8), <code><a href="/docs/linux/man/8-xfs_metadump/">xfs_metadump</a></code>(8), <code><a href="/docs/linux/man/8-xfs_ncheck/">xfs_ncheck</a></code>(8), <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5). </p>
