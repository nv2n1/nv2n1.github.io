---
title: "lde(8)"
name: "lde"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lde/"
description: "lde – a curses based file system viewer/editor for Linux"
---

<p>lde &#8211; a curses based file system viewer/editor for Linux</p>
<h2>Synopsis</h2>
<p><code>lde</code> [options] device</p>
<h2>Description</h2>
<p><code>lde</code> supports the three most popular file systems under Linux at the time of its inception: ext2fs, minix, and xiafs. It also has minimal support for msdos FAT file systems and a nofs system in which case <code>lde </code> will function as a binary editor. <code>lde</code> will attempt to automatically detect the file system present on the device or file when it is started, if it does not recognize the file system present on the device, it will default to nofs. <code>lde</code> allows you to view and edit disk blocks in hex or ASCII mode, view a block that contains directory entries in a readable fashion, and view and edit formatted inodes. <code>lde</code> is a great help when recovering deleted files (see doc/UNERASE included with the <code>lde</code> distribution for more info). The device parameter is a required option for <code>lde.</code> If omitted, it will print a warning and refuse to start. The default mode for <code>lde</code> is to use a curses interface; this can be overriden by some of the options listed below. </p>
<h2>Options</h2>
<dl>
<dt><code>-a, &#8211;all</code></p>
<dd>Indicates that searches should be performed on the entire disk. If <code>-a</code> is not specified, only data zones which are marked not in use will be searched.</p>
<dt><code>&#8211;append</code></p>
<dd>Always append data to existing recovery file. If file does not exist, create new file.</p>
<dt><code>-b (&#8211;block) block_number</code></p>
<dd>Format a single block as hex and dump it to standard output. Specify <code>-N</code> to dump more than one block.</p>
<dt><code>-B block_number</code></p>
<dd>Format all blocks after specifed block_number as hex and dump to standard output. You can use <code>-N</code> to specify the number of blocks to display.</p>
<dt><code>&#8211;blanked-indirects</code></p>
<dd>Linux &lt;= 2.0.33 blanks all the indirect blocks when truncating an inode. The inode still knows where the 1x/2x/3x indirect blocks are, but they&#8217;re full of zeros. This was a quick hack that works to restore small (&gt;12k &lt;~500k) unfragmented files. It can be toggled via the flags menu in the curses interface.</p>
<dt><code>-d block_number</code></p>
<dd>Dump a block&#8217;s data to standard out as unformatted binary data, ( like <code>cat</code> and faster than <code>dd</code> ). Specify <code>-N</code> to dump more than one block.</p>
<dt><code>-D block_number</code></p>
<dd>Dump all blocks after block_number to standard out as unformatted binary data. You can use <code>-N</code> to specify the number of blocks to dump.</p>
<dt><code>-f, &#8211;file recovery_file_name</code></p>
<dd>Signal lde that we want to recover an inode to a file and specify its name. You should specify the inode number to be recovered with the <code>-i</code> option.</p>
<dt><code>-g, &#8211;grep</code></p>
<dd>This option was designed to work with grep output. Grep a file for lost data, pipe it through awk to yield just byte offsets where the desired string lies. <code>lde</code> will then find the block corresponding to the desired offset and try to find an inode which references this block. A sample script is included with the <code>lde</code> distribution (crash_recovery/grep-inode).</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Display extended help.</p>
<dt><code>-i (&#8211;inode) inode_number</code></p>
<dd>Format and dump a single inode to standard output. Specify <code>-N</code> to dump more than one inode.</p>
<dt><code>-I inode_number</code></p>
<dd>Format and dump all inodes after inode_number to standard output. You can use <code>-N</code> to specify the number of inodes to display.</p>
<dt><code>&#8211;indirects</code></p>
<dd>Search the filesystem for blocks that looks like indirect blocks.</p>
<dt><code>&#8211;ilookup</code></p>
<dd>When searching, if we find a match, activate this flag to lookup the inode which contains the matched block. It might be easier and faster to do this with paper and use lde to interactively lookup only the blocks which have a high probability of being the one you want. <code>&#8211;ilookup</code> can also be used if the <code>-B</code> or <code>-b</code> option is specified to try to find an inode reference for the specifed blocks. When using <code>-B</code> you may want to specify <code>-N</code> also.</p>
<dt><code>&#8211;logtofile</code></p>
<dd>Debugging option. All of lde&#8217;s messages will be dumped to /tmp/ldeerrors.</p>
<dt><code>-L &#8211;length</code></p>
<dd>Sets search string length (when using <code>-T</code> with a filename).</p>
<dt><code>-N &#8211;limit</code></p>
<dd>Sets the number of blocks to display when using inode or block dumps. If unspecified, default is to the end of the filesystem ( <code>-I</code> <code>-B</code> <code>-D</code> ) or a single block ( <code>-i</code> <code>-b</code> <code>-d</code> ). </p>
<p> <code>-N</code> can also be used to specify a block to begin/resume searching at. If unspecified in this usage, it defaults to the first data zone.</p>
<dt><code>-O &#8211;offset</code></p>
<dd>Sets search string offset (when using <code>-T</code> with a filename). The first byte in the template file is 0. When searching for matches, the block will be examined starting at this offset.</p>
<dt><code>-p, -r, &#8211;paranoid, &#8211;safe, &#8211;read-only</code></p>
<dd>Open the device read only. Once set, this cannot be toggled from within the program.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Turn off bell.</p>
<dt><code>&#8211;recoverable</code></p>
<dd>When searching, check that any inodes found contain a deleted file that may be recovered. <code>&#8211;ilookup</code> must also be activated for this option to have any effect. If no blocks are marked used by another inode, &quot;recovery possible&quot; will be printed. If blocks are used by another file &quot;recovery NOT possible&quot; will be printed to the screen. You may still be able to get some data back even when it reports that recovery is not possible. To get an idea of how many blocks are in use, you will have to check its recoverablilty from lde via its curses interface (see Recover mode below).</p>
<dl>
<dd>If <code>&#8211;recoverable</code> is used with <code>-I 1</code> , it will check all the deleted inodes to see if they can be recovered. The deletion time of the inode will be printed to the screen if it is recoverable.</dl>
<dt><code>-s (&#8211;bs or &#8211;blocksize) block_size</code></p>
<dd>Override blocksize which lde has detected. The blocksize may have been read from the information (superblock) stored on the disk or is what lde would consider the default blocksize for that type of filesystem (generally 1024 bytes). With this option, you can force lde to use a different blocksize.</p>
<dt><code>&#8211;superscan</code></p>
<dd>Try to find ext2 signature on device. Supersedes functionaly previously provided by <code>find_ext2_fs</code>.</p>
<dt><code>-S string</code></p>
<dd>Search disk for data (of questionable usefulness). This was more for searching for a specific type of file (which is now easier with <code>-T</code> ) rather than file data. To search for data or strings, use the &#8211;grep option. If you insist on using <code>-S</code> which might be prudent occasionally, The offset of the string must be specified with <code>-O</code> , and each block will only be inspected at that offset. If <code>-O</code> is not specified, then 0 is assumed and the string must lie at the start of a block. You can also specify the block to begin/resume searching from with <code>-N</code> which defaults to the first data zone.</p>
<dt><code>-t fstype</code></p>
<dd>Override the auto-detect. fstype = {no, minix, xiafs, ext2fs, msdos}</p>
<dt><code>-T type</code></p>
<dd>Search disk for data. This will search the start of each block for numbers found in /etc/magic for certain types of files, currently supported types are {gz, tgz, script}.</p>
<dl>
<dd><code>Note:</code> type tgz only finds tar files that were created with gnu tar using its cfz options. Use gz to find tar files that were compressed after creation (or through a pipe?). </p>
<p> If you specify a filename after the <code>-T</code> option, it will read in the first block of the file and search the filesystem for something which matches it exactly. This may be useful for finding deleted copies of files (i.e. you&#8217;ve found version 1.0, but deleted version 1.5 and now want to recover it) or with the <code>-L</code> and <code>-O</code> options, you can pick off a few bytes and search for magic numbers in a certain file type. When using the filename option, you really should specify <code>-L</code> and <code>-O</code> or they will default to BLOCKSIZE and 0. You can also specify the block to begin/resume searching from with <code>-N</code> which defaults to the first data zone.</dl>
<dt><code>-V, &#8211;version</code></p>
<dd>Display version information.</p>
<dt><code>-w, &#8211;write</code></p>
<dd>Allow writes to the disk. </p>
</dl>
<h2>Curses Interface</h2>
<p>The <code>lde</code> main screen displays the file system&#8217;s superblock in the workspace window. The header window will be the same for all modes and indicates the program name and version, the device, the current selected inode, and the current selected block. There are also nine digits (and some extra characters shifted-12456 on an American keyboard, sorry I skip &#8216;#&#8217; which is reserved for another function) &quot;0123456789!@$%^&quot; which indicate the status of a bogus inode which can be used for file recovery. A digit means the inode block entry has not been filled yet, a minus sign indicates that it has been filled. </p>
<p> While displaying the superblock, you can use the following keys which are valid in most modes:</p>
<dl>
<dd>
<dl>
<dt><code>b</code></p>
<dd>to enter block mode</p>
<dt><code>d</code></p>
<dd>display the directory contents of the current inode or block</p>
<dt><code>f</code></p>
<dd>menu of runtime flags</p>
<dt><code>i </code></p>
<dd>to enter inode mode</p>
<dt><code>r</code></p>
<dd>to enter recover mode</p>
<dt><code>s</code></p>
<dd>return to super block mode ( only valid from other modes )</p>
<dt><code>q</code></p>
<dd>to quit</p>
<dt><code>v</code></p>
<dd>view the error/warning log</p>
<dt><code>^L</code></p>
<dd>to repaint the screen</p>
<dt><code>^O</code></p>
<dd>display menu of valid choices ( also <code>F2</code> )</p>
<dt><code>F1</code></p>
<dd>display help screen ( also <code>M-h</code> or <code>?</code> )</dl>
</dl>
<p> I have tried to implement cursor motion modes similar to both vi and emacs (M = meta key, ^ = control key, ESC is recognized as the meta key, M-ESC is recognized occasionally as ESC &#8212; to exit menus). </p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>vi<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> emacs</p>
<p>&nbsp;<wbr>UP<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>k<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>^P</p>
<p> DOWN<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>j<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> ^N</p>
<p> LEFT<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>h<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> ^B</p>
<p> RIGHT<tt>&nbsp;<wbr>&nbsp;<wbr></tt>l<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> ^F</p>
<p> PG_UP<tt>&nbsp;<wbr>&nbsp;<wbr></tt>^U<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> M-v</p>
<p> PG_DN<tt>&nbsp;<wbr>&nbsp;<wbr></tt>^D<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> ^V
</dl>
<dl>
<dd><code>Inode mode:</code> </p>
<p> Once in inode mode, the current inode will be displayed in the workspace window. </p>
<dl>
<dd>
<dl>
<dt><code>PG_DOWN</code></p>
<dd>Make next inode the current inode.</p>
<dt><code>PG_UP</code></p>
<dd>Make previous inode the current inode.</p>
<dt><code>arrows</code></p>
<dd>Move cursor to different fields of inode. Up and left go back one field, down or right will go to the next field.</p>
<dt><code>0123456789!@#$%^</code></p>
<dd>Add corresponding block entry from this inode to the recovery list.</p>
<dt><code>B</code></p>
<dd>Switch to block mode, examining block under cursor.</p>
<dt><code>b</code></p>
<dd>Switch to block mode, examining current block (displayed in status line).</p>
<dt><code>c</code></p>
<dd>Copy inode to inode copy buffer.</p>
<dt><code>e</code></p>
<dd>Edit inode information. Use the cursor to select the field you want to edit, then hit <code>RET ^M ^J</code> or <code>e</code> and a line will pop up at the bottom of the screen, enter the new value here. Entering a blank line will leave the value unchanged. </p>
<p> Dates can be entered in any format other than the one displayed on the screen. The year must be kept near the month and day. Use formats like &quot;24SEP96 10:00:01&quot; or &quot;10:00:01 Sep 24, 1996&quot;. &quot;12/24/96&quot; will probably default to the American interpretation MM/DD/YY. I did not write the date parser, so I don&#8217;t want to hear any complaints about it.</p>
<dt><code>p</code></p>
<dd>Paste inode from inode copy buffer.</p>
<dt><code>r</code></p>
<dd>Switch to recover mode.</p>
<dt><code>R</code></p>
<dd>Switch to recover mode, copy current inode block information into recovery inode.</p>
<dt><code>#</code></p>
<dd>This will prompt the user to enter a number and it will then make that the current inode. The number may be entered as hexadecimal (leading &#8216;x&#8217;, &#8216;0x&#8217;, or &#8216;$&#8217;), octal (leading &#8221;), or decimal.</p>
<dt><code>M-b</code></p>
<dd>View inode in its raw block format.</dl>
</dl>
<p> <code>Block Mode:</code> </p>
<p> In block mode, the current block will be displayed in hexadecimal and ASCII. The numbers along the left hand side of the screen are hexadecimal offsets from the beginning of the block. As much of the block as possible will be displayed. If the block is marked unused, the central row of &#8216;:&#8217; will spell out NOT USED. </p>
<dl>
<dd>
<dl>
<dt><code>PG_DOWN</code></p>
<dd>Display next chunk of this block.</p>
<dt><code>PG_UP</code></p>
<dd>Display previous chunk of this block.</p>
<dt><code>+</code></p>
<dd>Make next block the current block.</p>
<dt><code>&#8211;</code></p>
<dd>Make previous block the current block.</p>
<dt><code>arrow</code></p>
<dd>Move cursor.</p>
<dt><code>b</code></p>
<dd>View block under cursor. <code>lde</code> will interpret the byte under the cursor as the start of a block pointer (as if it were part of an indirect block). This will be a two byte pointer for the minix file system, four bytes for ext2fs and xiafs.</p>
<dt><code>B</code></p>
<dd>Interpret blocks under cursor as a block pointer and make it the current block.</p>
<dt><code>c</code></p>
<dd>Copy block to copy buffer.</p>
<dt><code>d</code></p>
<dd>Dump block as a directory (see directory popup description below).</p>
<dt><code>e</code></p>
<dd>Edit the data in hex or ascii mode. <code>TAB</code> ( <i>^I</i>) switches between hex and ascii editing. While in hex edit, the keys <code>A-F</code> and <code>0123456789</code> will not perform their lde functions, but are used to enter new data. In ascii edit, most keys (chars 32-126) are used to enter new data. Characters outside this range must be entered in hex mode, they will be displayed on the ASCII display as a period. </p>
<p> Editing will exit on write block ( <code>^W</code> ) or a command which goes to another block or leaves block mode. To discard your changes and re-read the block use <code>^A </code> or view another block and come back. You will always be prompted [Yes/Discard changes/Continue edit] before a write occurs. Select <code>y</code> to save the block to disk, <code>d</code> to discard your changes and re-read the data from disk, or <code>c</code> if you made a mistake and want to go back and make some more changes before saving this block. </p>
<p> It is probably a good idea to <i>unmount the file system before you do any writes to it</i>. My guess is that bad things will happen if you try to write the inode/block tables while someone else is using the filesystem.</p>
<dt><code>I</code></p>
<dd>View inode under cursor. <code>lde</code> will interpret the byte under the cursor as the start of an inode pointer (as if it were part of an directory entry). This will be a two byte pointer for the minix file system, four bytes for ext2fs and xiafs.</p>
<dt><code>n, p</code></p>
<dd>Next/previous block in file. If the displayed file is indexed by the current inode, you can step to the next or previous block in the chain.</p>
<dt><code>p</code></p>
<dd>Paste block from copy buffer.</p>
<dt><code>w</code></p>
<dd>Write the current block to the recovery file.</p>
<dt><code>0123456789!@#$%^</code></p>
<dd>tag this block to be recovered. Under Minix, this will display nine blocks which represent the block pointers in an inode. 0-6 are direct blocks, 7 is the indirect block, and 8 is the double indirect block. One day there may be an option for more direct blocks to make recovery easier. When a block is tagged, the status line will reflect this. To untag a block, go to recover mode and set the block&#8217;s pointer to zero.</p>
<dt><code>#</code></p>
<dd>This will prompt the user to enter a block number. The numbers may be entered in the same format described in inode mode (decimal, hex, or octal).</p>
<dt><code>^R</code></p>
<dd>Look up inode which references this block.</p>
<dt><code>/</code></p>
<dd>Search for a string. You will be prompted for a case-sensative search string. The search will proceede from the current block, if a match is found, the block pointer will be advanced and the matching block will be displayed.</dl>
</dl>
<p> <code>Recover Mode:</code> </p>
<p> In recover mode, the tagged blocks are displayed and may be edited by hand. When they are correct the user can dump the file. The user is prompted for a filename which can be 80 chars, the default file is &quot;./RECOVER.file&quot;. </p>
<dl>
<dd>
<dl>
<dt><code>0123456789!@#$%^</code></p>
<dd>Will prompt the user to enter a numeric value for the specified block index. The format of the input should be the same as that described in inode mode.</p>
<dt><code>c</code></p>
<dd>Check that all the blocks marked for recovery are unused. Complete recovery will be impossible if any blocks are reported in use, but you might be able to salvage a large chunk of your file.</p>
<dt><code>r</code></p>
<dd>Write out the recovered file.</p>
<dt><code>u</code></p>
<dd>Unmark all blocks. The recovery inode will be filled with zeroes.</dl>
</dl>
<p> <code>Directory View</code> </p>
<p> Accessable from inode and block mode. In block mode, it formats the current block as a directory entry with no syntax checking (i.e. it might not really be a directory block). In inode mode, it uses the block pointers to determine what to display. You can use the up and down arrow keys to scroll the display if there are too many entries to display at once. </p>
<dt><code>d</code></p>
<dd>If the cursor is on a directory, it will follow the link and display that directory. Use <code>D</code> to do the same and set the current inode to the new directory inode.</p>
<dt><code>i</code></p>
<dd>Set the current inode to the inode under the cursor.</p>
<dt><code>I</code></p>
<dd>Set the current inode and immediately view it in inode mode.</p>
<dt><code>n, p</code></p>
<dd>Next/previous block in directory. If the directory being viewed is indexed by the current inode, you can step to the next or previous block in the chain. </p>
</dl>
<h2>EXAMPLES (command line)</h2>
<p>lde -I 1 -N 10 /dev/hda1</p>
<dl>
<dd>Display inodes 1-10 on the screen.</dl>
<p> lde -b 34 /dev/hda1 | more</p>
<dl>
<dd>Display block 34 on the screen (formatted in hex and ascii).</dl>
<p> lde -D 100 -N 51 /dev/hda1 &gt; MyOuput</p>
<dl>
<dd>Cat blocks 100-150 to stdout (binary data), which is equivalent to </p>
<p> dd if=/dev/hda1 of=MyOutput bs=1024 count=51 skip=100</dl>
<p> lde -I 1 &#8211;recoverable /dev/hda5</p>
<dl>
<dd>Display all inodes on /dev/hda5 which have been deleted, but can be recovered.</dl>
<p> lde -I 1 &#8211;recoverable /dev/hda5 | grep &quot;Sep 23&quot;</p>
<dl>
<dd>Display all inodes on /dev/hda5 which have been deleted today September 23, but can be recovered. The date format is that of <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3):</p>
<dl>
<dd>&quot;Wed Jun 30 21:49:08 1993&quot;</dl>
<p> <code>Note:</code> the day will have a leading space if is less than 10.</dl>
<p> lde -b 100 &#8211;ilookup /dev/hda1</p>
<dl>
<dd>Find first inode that references block 100 on /dev/hda1 (to search for multiple occurances, use the curses interface).</dl>
<p> lde &#8211;paranoid -T tgz &#8211;ilookup &#8211;recoverable /dev/hda5</p>
<dl>
<dd>Find all tgz files which have been deleted, display possible inodes and check if it is possible to recover the files, open the file system read only while searching.</dl>
<p> See docs/UNERASE included with the lde distribution for more examples and instructions for the best way to go about restoring files.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-fsck-minix/">fsck.minix</a></code>(8), <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-xfsck/">xfsck</a></code>(8), <code><a href="/docs/linux/man/8-debugfs/">debugfs</a></code>(8)</p>
<h2>Author</h2>
<p>Scott D. Heavner (sdh [at] po.cwru.edu) </p>
<p> For more info, see the lde project page at sourceforge <i>&lt;<a rel="nofollow" href="http://lde.sourceforge.net/">http://lde.sourceforge.net/</a>&gt;</i>.</p>
