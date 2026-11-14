---
title: "fsck-msdos(8)"
name: "fsck-msdos"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck-msdos/"
description: "fsck.fat – check and repair MS-DOS FAT filesystems"
---

<p>fsck.fat &#8211; check and repair MS-DOS FAT filesystems</p>
<h2>Synopsis</h2>
<p><code>fsck.fat</code> [<i>OPTIONS</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p><code>fsck.fat</code> verifies the consistency of MS-DOS filesystems and optionally tries to repair them. </p>
<p> The following filesystem problems can be corrected (in this order):</p>
<dl>
<dt>&bull;</p>
<dd>FAT contains invalid cluster numbers. Cluster is changed to EOF.</p>
<dt>&bull;</p>
<dd>File&#8217;s cluster chain contains a loop. The loop is broken.</p>
<dt>&bull;</p>
<dd>Bad clusters (read errors). The clusters are marked bad and they are removed from files owning them. This check is optional.</p>
<dt>&bull;</p>
<dd>Directories with a large number of bad entries (probably corrupt). The directory can be deleted.</p>
<dt>&bull;</p>
<dd>Files . and .. are non-directories. They can be deleted or renamed.</p>
<dt>&bull;</p>
<dd>Directories . and .. in root directory. They are deleted.</p>
<dt>&bull;</p>
<dd>Bad filenames. They can be renamed.</p>
<dt>&bull;</p>
<dd>Duplicate directory entries. They can be deleted or renamed.</p>
<dt>&bull;</p>
<dd>Directories with non-zero size field. Size is set to zero.</p>
<dt>&bull;</p>
<dd>Directory . does not point to parent directory. The start pointer is adjusted.</p>
<dt>&bull;</p>
<dd>Directory .. does not point to parent of parent directory. The start pointer is adjusted.</p>
<dt>&bull;</p>
<dd>. and .. are not the two first entries in a non-root directory. The entries are created, moving occupied slots if necessary.</p>
<dt>&bull;</p>
<dd>Start cluster number of a file is invalid. The file is truncated.</p>
<dt>&bull;</p>
<dd>File contains bad or free clusters. The file is truncated.</p>
<dt>&bull;</p>
<dd>File&#8217;s cluster chain is longer than indicated by the size fields. The file is truncated.</p>
<dt>&bull;</p>
<dd>Two or more files share the same cluster(s). All but one of the files are truncated. If the file being truncated is a directory file that has already been read, the filesystem check is restarted after truncation.</p>
<dt>&bull;</p>
<dd>File&#8217;s cluster chain is shorter than indicated by the size fields. The file is truncated.</p>
<dt>&bull;</p>
<dd>Volume label in root directory or label in boot sector is invalid. Invalid labels are removed.</p>
<dt>&bull;</p>
<dd>Volume label in root directory and label in boot sector are different. Volume label from root directory is copied to boot sector.</p>
<dt>&bull;</p>
<dd>Clusters are marked as used but are not owned by a file. They are marked as free.</dl>
<p> Additionally, the following problems are detected, but not repaired:</p>
<dl>
<dt>&bull;</p>
<dd>Invalid parameters in boot sector</dl>
<p> When <code>fsck.fat</code> checks a filesystem, it accumulates all changes in memory and performs them only after all checks are complete. This can be disabled with the <code>-w</code> option. </p>
<p> Two different variants of the FAT filesystem are supported. Standard is the FAT12, FAT16 and FAT32 filesystems as defined by Microsoft and widely used on hard disks and removable media like USB sticks and SD cards. The other is the legacy Atari variant used on Atari ST. </p>
<p> There are some minor differences in Atari format: Some boot sector fields are interpreted slightly different, and the special FAT entries for end-of-file and bad cluster can be different. Under MS-DOS 0xfff8 is used for EOF and Atari employs 0xffff by default, but both systems recognize all values from 0xfff8-0xffff as end-of-file. MS-DOS uses only 0xfff7 for bad clusters, where on Atari values 0xfff0-0xfff7 are for this purpose (but the standard value is still 0xfff7).</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Automatically repair the filesystem. No user intervention is necessary. Whenever there is more than one method to solve a problem, the least destructive approach is used.</p>
<dt><code>-A</code></p>
<dd>Select using the Atari variation of the FAT filesystem if that isn&#8217;t active already, otherwise select standard FAT filesystem. This is selected by default if <code>mkfs.fat</code> is run on 68k Atari Linux.</p>
<dt><code>-b</code></p>
<dd>Make read-only boot sector check.</p>
<dt><code>-c</code> <i>PAGE</i></p>
<dd>Use DOS codepage <i>PAGE</i> to decode short file names. By default codepage 850 is used.</p>
<dt><code>-d</code> <i>PATH</i></p>
<dd>Delete the specified file. If more than one file with that name exist, the first one is deleted. This option can be given more than once.</p>
<dt><code>-f</code></p>
<dd>Salvage unused cluster chains to files. By default, unused clusters are added to the free disk space except in auto mode (<code>-a</code>).</p>
<dt><code>-F</code> <i>NUM</i></p>
<dd>Specify FAT table <i>NUM</i> for filesystem access. By default value <i>0</i> is assumed and then the first uncorrupted FAT table is chosen. Uncorrupted means that FAT table has valid first cluster. If default value <i>0</i> is used and all FAT tables are corrupted then <code>fsck.fat</code> gives up and does not try to repair FAT filesystem. If non-zero <i>NUM</i> value is specified then <code>fsck.fat</code> uses FAT table <i>NUM</i> for repairing FAT filesystem. If FAT table <i>NUM</i> has corrupted first cluster then <code>fsck.fat</code> will repair it. In any case, if FAT filesystem has more FAT tables then repaired content of chosen FAT table is copied to other FAT tables. To repair corrupted first cluster it is required to call <code>fsck.fat</code> with non-zero <i>NUM</i> value.</p>
<dt><code>-l</code></p>
<dd>List path names of files being processed.</p>
<dt><code>-n</code></p>
<dd>No-operation mode: non-interactively check for errors, but don&#8217;t write anything to the filesystem.</p>
<dt><code>-p</code></p>
<dd>Same as <code>-a</code>, for compatibility with other *fsck.</p>
<dt><code>-r</code></p>
<dd>Interactively repair the filesystem. The user is asked for advice whenever there is more than one approach to fix an inconsistency. This is the default mode and the option is only retained for backwards compatibility.</p>
<dt><code>-S</code></p>
<dd>Consider short (8.3) file names with spaces in the middle to be invalid, like previous versions of this program did. While such file names are not forbidden by the FAT specification, and were never treated as errors by Microsoft file system checking tools, many DOS programs are unable to handle files with such names. Using this option can make them accessible to these programs.</p>
<dd>Short file names which <i>start</i> with a space are considered invalid regardless of this option&#8217;s setting.</p>
<dd>Previous versions of this program exceptionally treated <i>EA DATA. SF</i> and <i>WP ROOT. SF</i> as valid short names; using this option does not preserve that exception.</p>
<dt><code>-t</code></p>
<dd>Mark unreadable clusters as bad.</p>
<dt><code>-u</code> <i>PATH</i></p>
<dd>Try to undelete the specified file. <code>fsck.fat</code> tries to allocate a chain of contiguous unallocated clusters beginning with the start cluster of the undeleted file. This option can be given more than once.</p>
<dt><code>-U</code></p>
<dd>Consider lowercase volume and boot label as invalid and allow only uppercase characters. Such labels are forbidden by the FAT specification, but they are widely used by Linux tools. Moreover MS-DOS and Windows systems do not have problems to read them. Therefore volume and boot labels with lowercase characters are by default permitted.</p>
<dt><code>-v</code></p>
<dd>Verbose mode. Generates slightly more output.</p>
<dt><code>-V</code></p>
<dd>Perform a verification pass. The filesystem check is repeated after the first run. The second pass should never report any fixable errors. It may take considerably longer than the first pass, because the first pass may have generated long list of modifications that have to be scanned for each disk read.</p>
<dt><code>&#8211;variant</code> <i>TYPE</i></p>
<dd>Create a filesystem of variant <i>TYPE</i>. Acceptable values are <i>standard</i> and <i>atari</i> (in any combination of upper/lower case). See above under DESCRIPTION for the differences.</p>
<dt><code>-w</code></p>
<dd>Write changes to disk immediately.</p>
<dt><code>-y</code></p>
<dd>Same as <code>-a</code> (automatically repair filesystem) for compatibility with other fsck tools.</p>
<dt><code>&#8211;help</code></p>
<dd>Display help message describing usage and options then exit.</dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd>No recoverable errors have been detected.</p>
<dt>1</p>
<dd>Recoverable errors have been detected or <code>fsck.fat</code> has discovered an internal inconsistency.</p>
<dt>2</p>
<dd>Usage error. <code>fsck.fat</code> did not access the filesystem.</dl>
<h2>Files</h2>
<dl>
<dt><i>fsck0000.rec</i>, <i>fsck0001.rec</i>, &#8230;</p>
<dd>When recovering from a corrupted filesystem, <code>fsck.fat</code> dumps recovered data into files named <i>fsckNNNN.rec</i> in the top level directory of the filesystem.</dl>
<h2>Bugs</h2>
<dl>
<dt>&bull;</p>
<dd>Does not remove entirely empty directories.</p>
<dt>&bull;</p>
<dd>Should give more diagnostic messages.</p>
<dt>&bull;</p>
<dd>Undeleting files should use a more sophisticated algorithm.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fatlabel/">fatlabel</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-fat/">mkfs.fat</a></code>(8)</p>
<h2>Homepage</h2>
<p>The home for the <code>dosfstools</code> project is its GitHub project page</p>
<h2>Authors</h2>
<p><code>dosfstools</code> were written by Werner Almesberger Roman Hodek and others. Current maintainers are Andreas Bombe and Pali Rohár</p>
