---
title: "fsck-ext2(8)"
name: "fsck-ext2"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck-ext2/"
description: "e2fsck – check a Linux ext2/ext3/ext4 file system"
---

<p>e2fsck &#8211; check a Linux ext2/ext3/ext4 file system</p>
<h2>Synopsis</h2>
<p><code>e2fsck</code> [ <code>-pacnyrdfkvtDFV</code> ] [ <code>-b</code> <i>superblock</i> ] [ <code>-B</code> <i>blocksize</i> ] [ <code>-l</code>|<code>-L</code> <i>bad_blocks_file</i> ] [ <code>-C</code> <i>fd</i> ] [ <code>-j</code> <i>external-journal</i> ] [ <code>-E</code> <i>extended_options</i> ] [ <code>-z</code> <i>undo_file</i> ] <i>device</i></p>
<h2>Description</h2>
<p><code>e2fsck</code> is used to check the ext2/ext3/ext4 family of file systems. For ext3 and ext4 file systems that use a journal, if the system has been shut down uncleanly without any errors, normally, after replaying the committed transactions in the journal, the file system should be marked as clean. Hence, for file systems that use journaling, <code>e2fsck</code> will normally replay the journal and exit, unless its superblock indicates that further checking is required. </p>
<p> <i>device</i> is a block device (e.g., <i>/dev/sdc1</i>) or file containing the file system. </p>
<p> Note that in general it is not safe to run <code>e2fsck</code> on mounted file systems. The only exception is if the <code>-n</code> option is specified, and <code>-c</code>, <code>-l</code>, or <code>-L</code> options are <i>not</i> specified. However, even if it is safe to do so, the results printed by <code>e2fsck</code> are not valid if the file system is mounted. If <code>e2fsck</code> asks whether or not you should check a file system which is mounted, the only correct answer is &#8220;no&#8221;. Only experts who really know what they are doing should consider answering this question in any other way. </p>
<p> If <code>e2fsck</code> is run in interactive mode (meaning that none of <code>-y</code>, <code>-n</code>, or <code>-p</code> are specified), the program will ask the user to fix each problem found in the file system. A response of &#8216;y&#8217; will fix the error; &#8216;n&#8217; will leave the error unfixed; and &#8216;a&#8217; will fix the problem and all subsequent problems; pressing Enter will proceed with the default response, which is printed before the question mark. Pressing Control-C terminates e2fsck immediately.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>This option does the same thing as the <code>-p</code> option. It is provided for backwards compatibility only; it is suggested that people use <code>-p</code> option whenever possible.</p>
<dt><code>-b</code><i> superblock</i></p>
<dd>Instead of using the normal superblock, use an alternative superblock specified by <i>superblock</i>. This option is normally used when the primary superblock has been corrupted. The location of backup superblocks is dependent on the file system&#8217;s blocksize, the number of blocks per group, and features such as <code>sparse_super</code>.</p>
<dd>Additional backup superblocks can be determined by using the <code>mke2fs</code> program using the <code>-n</code> option to print out where the superblocks exist, supposing <code>mke2fs</code> is supplied with arguments that are consistent with the file system&#8217;s layout (e.g. blocksize, blocks per group, <code>sparse_super</code>, etc.).</p>
<dd>If an alternative superblock is specified and the file system is not opened read-only, e2fsck will make sure that the primary superblock is updated appropriately upon completion of the file system check.</p>
<dt><code>-B</code><i> blocksize</i></p>
<dd>Normally, <code>e2fsck</code> will search for the superblock at various different block sizes in an attempt to find the appropriate block size. This search can be fooled in some cases. This option forces <code>e2fsck</code> to only try locating the superblock at a particular blocksize. If the superblock is not found, <code>e2fsck</code> will terminate with a fatal error.</p>
<dt><code>-c</code></p>
<dd>This option causes <code>e2fsck</code> to use <code><a href="/docs/linux/man/8-badblocks/">badblocks</a></code>(8) program to do a read-only scan of the device in order to find any bad blocks. If any bad blocks are found, they are added to the bad block inode to prevent them from being allocated to a file or directory. If this option is specified twice, then the bad block scan will be done using a non-destructive read-write test.</p>
<dt><code>-C</code><i> fd</i></p>
<dd>This option causes <code>e2fsck</code> to write completion information to the specified file descriptor so that the progress of the file system check can be monitored. This option is typically used by programs which are running <code>e2fsck</code>. If the file descriptor number is negative, then absolute value of the file descriptor will be used, and the progress information will be suppressed initially. It can later be enabled by sending the <code>e2fsck</code> process a SIGUSR1 signal. If the file descriptor specified is 0, <code>e2fsck</code> will print a completion bar as it goes about its business. This requires that e2fsck is running on a video console or terminal.</p>
<dt><code>-d</code></p>
<dd>Print debugging output (useless unless you are debugging <code>e2fsck</code>).</p>
<dt><code>-D</code></p>
<dd>Optimize directories in file system. This option causes e2fsck to try to optimize all directories, either by re-indexing them if the file system supports directory indexing, or by sorting and compressing directories for smaller directories, or for file systems using traditional linear directories.</p>
<dd>Even without the <code>-D</code> option, <code>e2fsck</code> may sometimes optimize a few directories &#8212; for example, if directory indexing is enabled and a directory is not indexed and would benefit from being indexed, or if the index structures are corrupted and need to be rebuilt. The <code>-D</code> option forces all directories in the file system to be optimized. This can sometimes make them a little smaller and slightly faster to search, but in practice, you should rarely need to use this option.</p>
<dd>The <code>-D</code> option will detect directory entries with duplicate names in a single directory, which e2fsck normally does not enforce for performance reasons.</p>
<dt><code>-E</code><i> extended_options</i></p>
<dd>Set e2fsck extended options. Extended options are comma separated, and may take an argument using the equals (&#8216;=&#8217;) sign. The following options are supported:</p>
<dl>
<dd>
<dl>
<dt><code>ea_ver=</code><i>extended_attribute_version</i></p>
<dd>Set the version of the extended attribute blocks which <code>e2fsck</code> will require while checking the file system. The version number may be 1 or 2. The default extended attribute version format is 2.</p>
<dt><code>journal_only</code></p>
<dd>Only replay the journal if required, but do not perform any further checks or repairs.</p>
<dt><code>fragcheck</code></p>
<dd>During pass 1, print a detailed report of any discontiguous blocks for files in the file system.</p>
<dt><code>discard</code></p>
<dd>Attempt to discard free blocks and unused inode blocks after the full file system check (discarding blocks is useful on solid state devices and sparse / thin-provisioned storage). Note that discard is done in pass 5 AFTER the file system has been fully checked and only if it does not contain recognizable errors. However there might be cases where <code>e2fsck</code> does not fully recognize a problem and hence in this case this option may prevent you from further manual data recovery.</p>
<dt><code>nodiscard</code></p>
<dd>Do not attempt to discard free blocks and unused inode blocks. This option is exactly the opposite of discard option. This is set as default.</p>
<dt><code>no_optimize_extents</code></p>
<dd>Do not offer to optimize the extent tree by eliminating unnecessary width or depth. This can also be enabled in the options section of <code>/etc/e2fsck.conf</code>.</p>
<dt><code>optimize_extents</code></p>
<dd>Offer to optimize the extent tree by eliminating unnecessary width or depth. This is the default unless otherwise specified in <code>/etc/e2fsck.conf</code>.</p>
<dt><code>inode_count_fullmap</code></p>
<dd>Trade off using memory for speed when checking a file system with a large number of hard-linked files. The amount of memory required is proportional to the number of inodes in the file system. For large file systems, this can be gigabytes of memory. (For example, a 40TB file system with 2.8 billion inodes will consume an additional 5.7 GB memory if this optimization is enabled.) This optimization can also be enabled in the options section of <code>/etc/e2fsck.conf</code>.</p>
<dt><code>no_inode_count_fullmap</code></p>
<dd>Disable the <code>inode_count_fullmap</code> optimization. This is the default unless otherwise specified in <code>/etc/e2fsck.conf</code>.</p>
<dt><code>readahead_kb</code></p>
<dd>Use this many KiB of memory to pre-fetch metadata in the hopes of reducing e2fsck runtime. By default, this is set to the size of two block groups&#8217; inode tables (typically 4MiB on a regular ext4 file system); if this amount is more than 1/50th of total physical memory, readahead is disabled. Set this to zero to disable readahead entirely.</p>
<dt><code>bmap2extent</code></p>
<dd>Convert block-mapped files to extent-mapped files.</p>
<dt><code>fixes_only</code></p>
<dd>Only fix damaged metadata; do not optimize htree directories or compress extent trees. This option is incompatible with the -D and -E bmap2extent options.</p>
<dt><code>check_encoding</code></p>
<dd>Force verification of encoded filenames in case-insensitive directories. This is the default mode if the file system has the strict flag enabled.</p>
<dt><code>unshare_blocks</code></p>
<dd>If the file system has shared blocks, with the shared blocks read-only feature enabled, then this will unshare all shared blocks and unset the read-only feature bit. If there is not enough free space then the operation will fail. If the file system does not have the read-only feature bit, but has shared blocks anyway, then this option will have no effect. Note when using this option, if there is no free space to clone blocks, there is no prompt to delete files and instead the operation will fail.</p>
<dd>Note that unshare_blocks implies the &quot;-f&quot; option to ensure that all passes are run. Additionally, if &quot;-n&quot; is also specified, e2fsck will simulate trying to allocate enough space to deduplicate. If this fails, the exit code will be non-zero.</dl>
</dl>
<dt><code>-f</code></p>
<dd>Force checking even if the file system seems clean.</p>
<dt><code>-F</code></p>
<dd>Flush the file system device&#8217;s buffer caches before beginning. Only really useful for doing <code>e2fsck</code> time trials.</p>
<dt><code>-j</code><i> external-journal</i></p>
<dd>Set the pathname where the external-journal for this file system can be found.</p>
<dt><code>-k</code></p>
<dd>When combined with the <code>-c</code> option, any existing bad blocks in the bad blocks list are preserved, and any new bad blocks found by running <code><a href="/docs/linux/man/8-badblocks/">badblocks</a></code>(8) will be added to the existing bad blocks list.</p>
<dt><code>-l</code><i> filename</i></p>
<dd>Add the block numbers listed in the file specified by <i>filename</i> to the list of bad blocks. The format of this file is the same as the one generated by the <code><a href="/docs/linux/man/8-badblocks/">badblocks</a></code>(8) program. Note that the block numbers are based on the blocksize of the file system. Hence, <code><a href="/docs/linux/man/8-badblocks/">badblocks</a></code>(8) must be given the blocksize of the file system in order to obtain correct results. As a result, it is much simpler and safer to use the <code>-c</code> option to <code>e2fsck</code>, since it will assure that the correct parameters are passed to the <code>badblocks</code> program.</p>
<dt><code>-L</code><i> filename</i></p>
<dd>Set the bad blocks list to be the list of blocks specified by <i>filename</i>. (This option is the same as the <code>-l</code> option, except the bad blocks list is cleared before the blocks listed in the file are added to the bad blocks list.)</p>
<dt><code>-n</code></p>
<dd>Open the file system read-only, and assume an answer of `no&#8217; to all questions. Allows <code>e2fsck</code> to be used non-interactively. This option may not be specified at the same time as the <code>-p</code> or <code>-y</code> options.</p>
<dt><code>-p</code></p>
<dd>Automatically repair (&quot;preen&quot;) the file system. This option will cause <code>e2fsck</code> to automatically fix any file system problems that can be safely fixed without human intervention. If <code>e2fsck</code> discovers a problem which may require the system administrator to take additional corrective action, <code>e2fsck</code> will print a description of the problem and then exit with the value 4 logically or&#8217;ed into the exit code. (See the <code>EXIT CODE</code> section.) This option is normally used by the system&#8217;s boot scripts. It may not be specified at the same time as the <code>-n</code> or <code>-y</code> options.</p>
<dt><code>-r</code></p>
<dd>This option does nothing at all; it is provided only for backwards compatibility.</p>
<dt><code>-t</code></p>
<dd>Print timing statistics for <code>e2fsck</code>. If this option is used twice, additional timing statistics are printed on a pass by pass basis.</p>
<dt><code>-v</code></p>
<dd>Verbose mode.</p>
<dt><code>-V</code></p>
<dd>Print version information and exit.</p>
<dt><code>-y</code></p>
<dd>Assume an answer of `yes&#8217; to all questions; allows <code>e2fsck</code> to be used non-interactively. This option may not be specified at the same time as the <code>-n</code> or <code>-p</code> options.</p>
<dt><code>-z</code><i> undo_file</i></p>
<dd>Before overwriting a file system block, write the old contents of the block to an undo file. This undo file can be used with <a href="/docs/linux/man/8-e2undo/">e2undo</a>(8) to restore the old contents of the file system should something go wrong. If the empty string is passed as the undo_file argument, the undo file will be written to a file named e2fsck-<i>device</i>.e2undo in the directory specified via the <i>E2FSPROGS_UNDO_DIR</i> environment variable. </p>
<p> WARNING: The undo file cannot be used to recover from a power or system crash.</dl>
<h2>Exit Code</h2>
<p>The exit code returned by <code>e2fsck</code> is the sum of the following conditions:<br />
 0 &#8211; No errors<br />
 1 &#8211; File system errors corrected<br />
 2 &#8211; File system errors corrected, system should<br />
 &nbsp;<wbr>&nbsp;be rebooted<br />
 4 &#8211; File system errors left uncorrected<br />
 8 &#8211; Operational error<br />
 16 &#8211; Usage or syntax error<br />
 32 &#8211; E2fsck canceled by user request<br />
 128 &#8211; Shared library error</p>
<h2>Signals</h2>
<p>The following signals have the following effect when sent to <code>e2fsck</code>.</p>
<dl>
<dt><code>SIGUSR1</code></p>
<dd>This signal causes <code>e2fsck</code> to start displaying a completion bar or emitting progress information. (See discussion of the <code>-C</code> option.)</p>
<dt><code>SIGUSR2</code></p>
<dd>This signal causes <code>e2fsck</code> to stop displaying a completion bar or emitting progress information.</dl>
<h2>Reporting Bugs</h2>
<p>Almost any piece of software will have bugs. If you manage to find a file system which causes <code>e2fsck</code> to crash, or which <code>e2fsck</code> is unable to repair, please report it to the author. </p>
<p> Please include as much information as possible in your bug report. Ideally, include a complete transcript of the <code>e2fsck</code> run, so I can see exactly what error messages are displayed. (Make sure the messages printed by <code>e2fsck</code> are in English; if your system has been configured so that <code>e2fsck</code>&#8216;s messages have been translated into another language, please set the the <code>LC_ALL</code> environment variable to <code>C</code> so that the transcript of e2fsck&#8217;s output will be useful to me.) If you have a writable file system where the transcript can be stored, the <code><a href="/docs/linux/man/1-script/">script</a></code>(1) program is a handy way to save the output of <code>e2fsck</code> to a file. </p>
<p> It is also useful to send the output of <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8). If a specific inode or inodes seems to be giving <code>e2fsck</code> trouble, try running the <code><a href="/docs/linux/man/8-debugfs/">debugfs</a></code>(8) command and send the output of the <code><a href="//www.systutorials.com/docs/linux/man/1u-stat/">stat</a></code>(1u) command run on the relevant inode(s). If the inode is a directory, the <code>debugfs</code> <i>dump</i> command will allow you to extract the contents of the directory inode, which can sent to me after being first run through <code><a href="/docs/linux/man/1-uuencode/">uuencode</a></code>(1). The most useful data you can send to help reproduce the bug is a compressed raw image dump of the file system, generated using <code><a href="/docs/linux/man/8-e2image/">e2image</a></code>(8). See the <code><a href="/docs/linux/man/8-e2image/">e2image</a></code>(8) man page for more details. </p>
<p> Always include the full version string which <code>e2fsck</code> displays when it is run, so I know which version you are running.</p>
<h2>Environment</h2>
<dl>
<dt><code>E2FSCK_CONFIG</code></p>
<dd>Determines the location of the configuration file (see <code><a href="/docs/linux/man/5-e2fsck-conf/">e2fsck.conf</a></code>(5)).</dl>
<h2>Author</h2>
<p>This version of <code>e2fsck</code> was written by Theodore Ts&#8217;o &lt;tytso [at] mit.edu&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-e2fsck-conf/">e2fsck.conf</a></code>(5), <code><a href="/docs/linux/man/8-badblocks/">badblocks</a></code>(8), <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8), <code><a href="/docs/linux/man/8-debugfs/">debugfs</a></code>(8), <code><a href="/docs/linux/man/8-e2image/">e2image</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8) </p>
