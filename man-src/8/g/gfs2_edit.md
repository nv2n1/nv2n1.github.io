---
title: "gfs2_edit(8)"
name: "gfs2_edit"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs2_edit/"
description: "gfs2_edit – Display, print or edit GFS2 or GFS internal structures."
---

<p>gfs2_edit &#8211; Display, print or edit GFS2 or GFS internal structures.</p>
<h2>Synopsis</h2>
<p><code>gfs2_edit</code> [<i>OPTION</i>]&#8230; [<i>DEVICE</i>] </p>
<h2>Description</h2>
<p>The gfs2_edit command is a tool used to examine, edit or display internal data structures of a GFS2 or GFS file system. The gfs2_edit command can be run interactively, as described below in INTERACTIVE MODE. Caution: Several options of the gfs2_edit command alter the file system metadata and can cause file system corruption. These options should be used with great care. </p>
<h2>Options</h2>
<dl>
<dt><code>-p</code> [<i>struct</i> | <i>block</i>] [<i>blocktype</i>] [<i>blockalloc [val]</i>] [<i>blockbits</i>] [<i>blockrg</i>] [<i>find sb|rg|rb|di|in|lf|jd|lh|ld|ea|ed|lb|13|qc</i>] [<i>field &lt;field&gt; [val]</i>]</p>
<dd>Print a gfs2 data structure in human-readable format to stdout. You can enter either a block number or a data structure name. Block numbers may be specified in hex (e.g., 0x10) or decimal (e.g., 16). </p>
<p> You can specify the following well-known locations with the -p option. </p>
<p> <i>sb</i>, <i>superblock</i> &#8211; Print the superblock. </p>
<p> <i>root</i> &#8211; Print the root directory. </p>
<p> <i>master</i> &#8211; Print the master system directory. </p>
<p> <i>jindex</i> &#8211; Print the journal index system directory. </p>
<p> <i>per_node</i> &#8211; Print the per_node system directory. </p>
<p> <i>inum</i> &#8211; Print the system inum file. </p>
<p> <i>statfs</i> &#8211; Print the system statfs file. </p>
<p> <i>rindex</i>, <i>rgindex</i> &#8211; Print the resource group index system file. </p>
<p> <i>rg X</i> &#8211; Print the resource group information for RG X (zero-based). </p>
<p> <i>rgs</i> &#8211; Print the resource group information. </p>
<p> <i>quota</i> &#8211; Print the contents of the system quota file. </p>
<p> <i>identify</i> &#8211; Identify a data block rather than print the block&#8217;s contents. </p>
<p> <i>size</i> &#8211; Print the device size information. </p>
<p> <i>journalX</i> &#8211; Print the contents of journal X, where X is a journal number from 0 to &lt;the number of journals in your file system &#8211; 1&gt;. Only the journal headers and journal descriptors are dumped. For journal descriptors, this option prints out every file system block number logged in that section of the journal. The actual journaled blocks are not printed. </p>
<p> If you specify a block number rather than a structure name, gfs2_edit will print out a breakdown of the structure for that block. For example: <code>gfs2_edit -p sb</code> will print the superblock, but so does <code>gfs2_edit -p 0x10</code> and <code>gfs2_edit -p 16</code>. </p>
<p> If you specify -p without a block or structure name, gfs2_edit prints the superblock. </p>
<p> You can specify more than one data structure with a single -p option. For example, <code>gfs2_edit -p inum statfs /dev/sda1</code> prints the system inum file and the system statfs file on /dev/sda1. </p>
<p> Optionally, you may specify the keyword <i>blocktype</i> to print out the gfs2 block type for the specified block. Valid gfs2 block types are: 0 (Clump), 1 (Superblock), 2 (Resource Group Header), 3 (Resource Group Bitmap), 4 (Dinode), 5 (Indirect Block), 6 (Leaf), 7 (Journaled data), 8 (Log Header), 9 (Log descriptor), 10 (Extended attribute), 11 (Eattr Data), 12 (Log Buffer), 13 (Invalid), and 14 (Quota Change). </p>
<p> Optionally, you may specify the keyword <i>blockalloc</i> with an optional value to assign. If no value is specified, the blockalloc keyword will print the block allocation type for the specified block. Valid block allocation types are: 0 (Free block), 1 (Data block), 2 (Unlinked block), and 3 (Metadata block). If a value from 0 to 3 is specified, the resource group bitmap will be changed to the new value. This may be used, for example, to artificially free or allocate a block in order to test fsck.gfs2&#8217;s ability to detect and fix the problem. </p>
<p> Optionally, you may specify the keyword <i>blockbits</i>. This option will locate and print the block containing the bitmap corresponding to the specified block. </p>
<p> Optionally, you may specify the keyword <i>blockrg</i>. This option will locate and print the block number of the resource group that holds information about the specified block. </p>
<p> You may also use gfs2_edit to find the next occurrence of a metadata block of a certain type. Valid metadata types are: <i>none</i> (unused metadata clump block), <i>sb</i> (superblock), <i>rg</i> (resource group), <i>rb</i> (rg bitmap), <i>di</i> (disk inode aka dinode), <i>in</i> (indirect block list), <i>lf</i> (directory leaf), <i>jd</i> (journaled data), <i>lh</i> (journal log header), <i>ld</i> (journal log descriptor), <i>ea</i> (extended attribute), <i>ed</i> (ea data block), <i>lb</i> (log buffer), <i>13</i> (unused block type 13), <i>qc</i> (quota change). The block AFTER the one specified with -p is the starting point for the search. For example, if you specify <code>gfs2_edit -p rg 12 find rg /dev/your/device</code>, it will find the rg that follows rg 12 (normally, this would be rg 13). Note, however, that since metadata often appears in the journals, it could be a copy of a different RG, inside a journal. Also note that gfs2_edit will only find <code>allocated</code> metadata blocks unless the type specified is none, sb, rg or rb. In other words, if you try to find a disk inode, it will only find an allocated dinode, not a deallocated one. </p>
<p> Optionally, you may specify the keyword <i>field</i> followed by a valid metadata field name. Right now, only the fields in disk inodes and resource groups are allowed. If no value is specified after the field, the value of the field will be printed to stdout. If a value is specified, the field&#8217;s value will be changed. This may be used, for example, to artificially change the di_size field for an inode in order to test fsck.gfs2&#8217;s ability to detect and fix the problem. </p>
<dt><code>-s</code> [<i>structure</i> | <i>block</i>]</p>
<dd>Specify a starting block for interactive mode. Any of the well-known locations found in the -p option may be specified. If you want to start on a particular resource group, specify it in quotes, e.g. -s &quot;rg 3&quot;</p>
<dt><code>-h, -help, -usage</code></p>
<dd>Print help information.</p>
<dt><code>-c</code> [<i>0</i> | <i>1</i>]</p>
<dd>Use alternate color scheme for interactive mode: 0=normal (dark colors on white background), or 1 (light colors on black background).</p>
<dt><code>-V</code></p>
<dd>Print program version information only.</p>
<dt><code>-x</code></p>
<dd>Print in hex mode.</p>
<dt><code>-z &lt;0-9&gt;</code></p>
<dd>Compress metadata with gzip compression level 1 to 9 (default 9). 0 means no compression at all.</p>
<dt><code>rg</code> <i>&lt;rg&gt;</i> <i>&lt;device&gt;</i></p>
<dd>Print the contents of Resource Group <i>&lt;rg&gt;</i> on <i>&lt;device&gt;</i>. </p>
<p> <i>&lt;rg&gt;</i> is a number from 0 to X &#8211; 1, where X is the number of RGs.</p>
<dt><code>rgcount</code> <i>&lt;device&gt;</i></p>
<dd>Print the number of Resource Groups in the file system on <i>&lt;device&gt;</i>.</p>
<dt><code>rgflags</code> <i>&lt;rg&gt;</i> [<i>new_value</i>] <i>&lt;device&gt;</i></p>
<dd>Print and/or modify the rg_flags value of Resource Group <i>&lt;rg&gt;</i> on <i>&lt;device&gt;</i>. </p>
<p> <i>&lt;rg&gt;</i> is a number from 0 to X &#8211; 1, where X is the number of RGs. If <i>new_value</i> is not specified, the current rg_flags value will be printed but not modified. If <i>new_value</i> is specified, the rg_flags field will be overwritten with the new value.</p>
<dt><code>printsavedmeta</code> <i>&lt;filename&gt;</i></p>
<dd>Print off a list of blocks from &lt;filename&gt; that were saved with the savemeta option.</p>
<dt><code>savemeta</code> <i>&lt;device&gt;</i> <i>&lt;filename&gt;</i></p>
<dd>Save off the GFS2 metadata (not user data) for the file system on the specified device to a file given by &lt;filename&gt;. You can use this option to analyze file system problems without revealing sensitive information that may be contained in the files. This option works quickly by using the system bitmap blocks in the resource groups to determine the location of all the metadata. If there is corruption in the bitmaps, resource groups or rindex file, this method may fail and you may need to use the savemetaslow option. The destination file is compressed using gzip unless -z 0 is specified.</p>
<dt><code>savemetaslow</code> <i>&lt;device&gt;</i> <i>&lt;filename&gt;</i></p>
<dd>Save off GFS2 metadata, as with the savemeta option, examining every block in the file system for metadata. This option is less prone to failure due to file system corruption than the savemeta option, but it is extremely slow. The destination file is compressed using gzip unless -z 0 is specified.</p>
<dt><code>savergs</code> <i>&lt;device&gt;</i> <i>&lt;filename&gt;</i></p>
<dd>Save off only the GFS2 resource group metadata for the file system on the specified device to a file given by &lt;filename&gt;. The destination file is compressed using gzip unless -z 0 is specified.</p>
<dt><code>restoremeta</code> <i>&lt;filename&gt;</i> <i>&lt;dest device&gt;</i></p>
<dd>Take a compressed or uncompressed file created with the savemeta option and restores its contents on top of the specified destination device. <code>WARNING</code>: When you use this option, the file system and all data on the destination device is destroyed. Since only metadata (but no data) is restored, every file in the resulting file system is likely to be corrupt. The ONLY purpose of this option is to examine and debug file system problems by restoring and examining the state of the saved metadata. If the destination file system is the same size or larger than the source file system where the metadata was saved, the resulting file system will be the same size as the source. If the destination device is smaller than the source file system, gfs2_edit will restore as much as it can, then quit, leaving you with a file system that probably will not mount, but from which you might still be able to figure out what is wrong with the source file system. </p>
</dl>
<h2>Interactive Mode</h2>
<p>If you specify a device on the gfs2_edit command line and you specify no options other than -c, gfs2_edit will act as an interactive GFS2 file system editor for the file system you specify. There are three display modes: hex mode, structure mode and pointers mode. You use the m key to switch between the modes, as described below. The modes are as follows:</p>
<dl>
<dt>Hex mode (default)</p>
<dd>Display or edit blocks of the file system in hexadecimal and ascii. </p>
<p> Lines at the top indicate the currently displayed block in both hex and decimal. If the block contains a GFS2 data structure, the name of that structure will appear in the upper right corner of the display. If the block is a well-known block, such as the superblock or rindex, there will be a line to indicate what it is. </p>
<p> In hex mode, you can edit blocks by pressing <code>&lt;enter&gt;</code> and entering hexadecimal digits to replace the highlighted hex digits. Do NOT precede the numbers with &quot;0x&quot;. For example, if you want to change the value at offset 0x60 from a 0x12 to 0xef, position your cursor to offset 0x60, so that the 12 is highlighted, then press <code>&lt;enter&gt;</code> and type in &quot;ef&quot;. Press <code>&lt;escape&gt;</code> or <code>&lt;enter&gt;</code> to exit edit mode. </p>
<p> In hex mode, different colors indicate different things. For example, in the default color scheme, the GFS2 data structure will be black, data offsets will be light blue, and actual data (anything after the gfs2 data structure) will be red. </p>
<dt>Structure mode</p>
<dd>Decode the file system block into its GFS2 structure and display the values of that structure. This mode is most useful for jumping around the file system. For example, you can use the arrow keys to position down to a pointer and press <code>J</code> to jump to that block. </p>
<dt>Pointers mode</p>
<dd>Display any additional information appearing on the block. For example, if an inode has block pointers, this will display them and allow you to scroll through them. You can also position to one of them and press <code>J</code> to jump to that block. </p>
</dl>
<h2>Interactive mode command keys:</h2>
<dl>
<dt><code>q</code> or <code>&lt;esc&gt;</code></p>
<dd>The <code>q</code> or <code>&lt;escape&gt;</code> keys are used to exit gfs2_edit. </p>
<dt><code>&lt;arrow/movement keys&gt;</code> up, down, right, left, pg-up, pg-down, home, end</p>
<dd>The arrow keys are used to highlight an area of the display. The <code>J</code> key may be used to jump to the block that is highlighted. </p>
<dt><code>m</code> &#8211; Mode switch</p>
<dd>The <code>m</code> key is used to switch between the three display modes. The initial mode is hex mode. Pressing the <code>m</code> key once switches to structure mode. Pressing it a second time switches from structure mode to pointers mode. Pressing it a third time takes you back to hex mode again. </p>
<dt><code>j</code> &#8211; Jump to block</p>
<dd>The <code>j</code> key jumps to the block number that is currently highlighted. In hex mode, hitting J will work when any byte of the pointer is highlighted. </p>
<dt><code>g</code> &#8211; Goto block</p>
<dd>The <code>g</code> key asks for a block number, then jumps there. Note that in many cases, you can also arrow up so that the current block number is highlighted, then press <code>&lt;enter&gt;</code> to enter a block number to jump to. </p>
<dt><code>h</code> &#8211; Help display</p>
<dd>The <code>h</code> key causes the interactive help display to be shown. </p>
<dt><code>e</code> &#8211; Extended mode</p>
<dd>The <code>e</code> key causes gfs2_edit to switch to extended (&quot;pointers&quot;) mode. </p>
<dt><code>c</code> &#8211; Color scheme</p>
<dd>The <code>c</code> key causes gfs2_edit to switch to its alternate color scheme. </p>
<dt><code>f</code> &#8211; Forward block</p>
<dd>The <code>f</code> key causes you to scroll forward one block. This does not affect the &quot;jump&quot; status. In other words, if you use the <code>f</code> key to move forward several blocks, pressing <code>&lt;backspace&gt;</code> will not roll you back up. </p>
<dt><code>&lt;enter&gt;</code> &#8211; Edit value</p>
<dd>The <code>&lt;enter&gt;</code> key causes you to go from display mode to edit mode. If you are in hex mode and you hit enter, you can type new hex values at the cursor&#8217;s current location. Note: pressing <code>&lt;enter&gt;</code> in structure mode allows you to enter a new value, with the following restrictions: For gfs2 disk inodes and resource groups, it will actually change the value on disk. However, inode numbers may not be changed. For all other structures, the values entered are ignored. </p>
<p> If you use the up arrow key to highlight the block number, then press <code>&lt;enter&gt;</code>, you may then enter a new block number, or any of the well-known block locations listed above (e.g. sb, rindex, inum, rg 17, etc.) and gfs2_edit will jump to the block specified. If you specify a slash character followed by a metadata type, gfs2_edit will search for the next occurrence of that metadata block type, and jump there. It will take you to block 0 if it does not find any more blocks of the specified metadata type. </p>
<dt><code>&lt;home&gt;</code></p>
<dd>If you are in pointers mode, this takes you back to the starts of the pointers you are viewing. Otherwise it takes you back to the superblock. </p>
<dt><code>&lt;backspace&gt;</code></p>
<dd>This takes you back to the block you were displaying before a jump. </p>
<dt><code>&lt;space&gt;</code></p>
<dd>This takes you forward to the block you were displaying when you hit <code>&lt;backspace&gt;</code>. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt>gfs2_edit /dev/roth_vg/roth_lv</p>
<dd>Display and optionally edit the file system on /dev/roth_vg/roth_lv </p>
<dt>gfs2_edit -p sb /dev/vg0/lvol0</p>
<dd>Print the superblock of the gfs2 file system located on /dev/vg0/lvol0. </p>
<dt>gfs2_edit -p identify 2746 2748 /dev/sda2</p>
<dd>Print out what kind of blocks are at block numbers 2746 and 2748 on device /dev/sda2. </p>
<dt>gfs2_edit -p rindex /dev/sda1</p>
<dd>Print the resource group index system file located on device /dev/sda1. </p>
<dt>gfs2_edit savemeta /dev/sda1 /tmp/our_fs</p>
<dd>Save off all metadata (but no user data) to file /tmp/our_fs. </p>
<dt>gfs2_edit -p root /dev/my_vg/my_lv</p>
<dd>Print the contents of the root directory in /dev/my_vg/my_lv. </p>
<dt>gfs2-edit -x -p 0x3f7a /dev/sda1</p>
<dd>Print the contents of block 16250 of /dev/sda1 in hex. </p>
<dt>gfs2_edit -p 12345 /dev/sdc2</p>
<dd>Print the gfs2 data structure at block 12345. </p>
<dt>gfs2_edit rgcount /dev/sdb1</p>
<dd>Print how many Resource Groups exist for /dev/sdb1. </p>
<dt>gfs2_edit -p rg 17 /dev/sdb1</p>
<dd>Print the contents of the eighteenth Resource Group on /dev/sdb1. </p>
<dt>gfs2_edit rgflags 3 /dev/sdb1</p>
<dd>Print the rg_flags value for the fourth Resource Group on /dev/sdb1. </p>
<dt>gfs2_edit rgflags 3 8 /dev/sdb1</p>
<dd>Set the GFS2_RGF_NOALLOC flag on for the fourth Resource Group on /dev/sdb1. </p>
<dt>gfs2_edit -p 25 blockalloc /dev/roth_vg/roth_lv</p>
<dd>Print the block allocation type of block 25. May produce this output: 3 (Metadata) </p>
<dt>gfs2_edit -p 25 blockalloc 1 /dev/roth_vg/roth_lv</p>
<dd>Change the block allocation type of block 25 to data. May produce this output: 1 </p>
<dt>gfs2_edit -p 25 blocktype /dev/roth_vg/roth_lv</p>
<dd>Print the metadata block type of block 25. May produce this output: 4 (Block 25 is type 4: Dinode) </p>
<dt>gfs2_edit -p 25 field di_size /dev/roth_vg/roth_lv</p>
<dd>Print the di_size field of block 25. May produce this output: 134217728 </p>
<dt>gfs2_edit -x -p 25 field di_size /dev/roth_vg/roth_lv</p>
<dd>Print the di_size field of block 25, in hexidecimal. May produce this output: 0x8000000 </p>
<dt>gfs2_edit -p 25 field di_size 0x4000 /dev/roth_vg/roth_lv</p>
<dd>Change the di_size field of block 25 to the hexidecimal value 0x4000. May produce this output: 16384</dl>
<h2>Known Bugs</h2>
<dl>
<dt>The directory code does not work well. It might be confused</p>
<dd>by directory &quot;sentinel&quot; entries. </p>
</dl>
