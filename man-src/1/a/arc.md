---
title: "arc(1)"
name: "arc"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arc/"
description: "arc – pc archive utility"
---

<h2>NAME</h2>
<p> arc &#8211; pc archive utility</p>
<h2>SYNOPSIS</h2>
<p> <code>arc</code> a|m|u|f|d|x|e|r|p|l|v|t|c [ biswnoq ] [ g<i>password</i> ] <i>archive </i> [ <i>filename</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>Arc</i> is a general archive and file compression utility, used to maintain a compressed archive of files. An <i>archive</i> is a single file that combines many files, reducing storage space and allowing multiple files to be handled as one. <i>Arc</i> uses one of several compression methods for each file within the <i>archive</i>, based on whichever method yields the smallest result.</p>
<h2>INSTRUCTIONS</h2>
<p> Execute <i>arc</i> with no arguments for fairly verbose, usable instructions.</p>
<h2>COMMAND SWITCHES</h2>
<dl>
<dt>a</p>
<dd> add files to archive. Copies the indicated files to the archive.</p>
<dt>m</p>
<dd> move files to archive. Same as &#8216;a&#8217; switch except that the files are deleted from the directory as they are moved to the archive.</p>
<dt>u</p>
<dd> update files in archive. This switch will replace archived files when the named file is newer than the archived copy. New files will be added automatically.</p>
<dt>f</p>
<dd> freshen files in archive. Same as &#8216;u&#8217; except that new files will not be added.</p>
<dt>d</p>
<dd> delete files in archive. The named files are removed from the archive.</p>
<dt>x,e</p>
<dd> extract files from archive. The named files are extracted from the archive and created in the current directory in an uncompressed state.</p>
<dt>r</p>
<dd> run one file with arguments from archive. Any program may be executed directly from the archive. The parameters given after the program name are passed to the program without modification.</p>
<dt>p</p>
<dd> copy files from archive to standard output. Useful with I/O redirection. A form-feed is appended after each file, to ease use with printers.</p>
<dt>l</p>
<dd> list files in archive. Limited information listing of files contained in an archive. Displays the filename, original length, and date last modified. If the &#8216;n&#8217; option (see below) is used, only the filename is displayed.</p>
<dt>v</p>
<dd> verbose listing of files in archive. Complete information listing of files contained in an archive. Displays the filename, original length, storage method, storage factor (% savings), compressed size, date, time, and CRC.</p>
<dt>t</p>
<dd> test archive integrity. Computes CRC values for each member of the archive and compares against the previously saved value.</p>
<dt>c</p>
<dd> convert entry to new packing method. Convert files stored with older methods to newer methods that are more efficient. Also useful for files previously archived with the &#8216;s&#8217; option.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>b</p>
<dd> retain backup copy of archive. Keep the original archive file and rename to .BAK. This switch may be used with the following commands: a, m, u, f, d, c.</p>
<dt>i</p>
<dd> suppress image mode. This switch causes files to be treated as text files, and will translate their end-of-line sequence. (Unix&#8217;s &#8216;
&#8217; vs. &#8216;
&#8217; used on many other systems.) The default is to perform no translation when compressing or extracting files. This option makes dealing with text files much nicer, though the &#8216;tr&#8217; command can also be used. (&#8216;&#8217; in makefiles and C source code is such a nuisance&#8230;)</p>
<dt>s</p>
<dd> suppress compression. This forces new files to be saved using Method 2 (no compression). This switch may be used with the following commands: a, m, u, f, c.</p>
<dt>w</p>
<dd> suppress warning messages. This switch will keep warning messages from being displayed which is the default. Most warnings concern the deletion or existence of files with the same name.</p>
<dt>n</p>
<dd> suppress notes and comments. This switch will keep useful notes from being displayed which is the default. Most notes indicate what stage of compression is being run (analyze, compaction, storage).</p>
<dt>o</p>
<dd> overwrite existing files when extracting. This switch will make existing files silently get overwritten, instead of asking for confirmation, which is the default.</p>
<dt>q</p>
<dd> force Squash compression method. This switch causes the Squash compression method to be used, instead of Crunch, which is the default.</p>
<dt>g</p>
<dd> encrypt/decrypt archive entry. This is used to encode files so that others may not read them. BE CAREFUL! This must be the last parameter in the switches because everything following is part of the password.</dl>
<h2>PROGRAMMING NOTES</h2>
<p> <i>Arc</i> Version 2 differs from version 1 in that archive entries are automatically compressed when they are added to the archive, making a separate compression step unecessary. The nature of the compression is indicated by the header version number placed in each archive entry, as follows: </p>
<pre>
         1 = Old style, no compression
         2 = New style, no compression
         3 = Compression of repeated characters only
         4 = Compression of repeated characters plus Huffman SQueezing
         5 = Lempel-Zev packing of repeated strings (old style)
         6 = Lempel-Zev packing of repeated strings (new style)
         7 = Lempel-Zev Williams packing with improved hash function
         8 = Dynamic Lempel-Zev packing with adaptive reset
         9 = Squashing
</pre>
<p> Type 5, Lempel-Zev packing, was added as of version 4.0 </p>
<p> Type 6 is Lempel-Zev packing where runs of repeated characters have been collapsed, and was added as of version 4.1 </p>
<p> Type 7 is a variation of Lempel-Zev using a different hash function which yields speed improvements of 20-25%, and was added as of version 4.6 </p>
<p> Type 8 is a different implementation of Lempel-Zev, using a variable code size and an adaptive block reset, and was added as of version 5.0 </p>
<p> Type 9 is another variation of Lempel-Zev, using a larger hash table. This method was developed by Phil Katz, and is not supported by the &quot;official&quot; <code>ARC</code> programs. </p>
<p> <i>Arc</i> will look for environment variables named <i>ARCTEMP</i> or <i>TMPDIR</i>, which, if present, indicates the pathname where temporary files should be created. This is typically the location of a RAMdisk on a microcomputer, &quot;/tmp/&quot; or left unset. </p>
<p> See the included documentation file for more details.</p>
<h2>HISTORY</h2>
<p> <i>Arc</i> has been in use in the CP/M and MSDOS world for many years. Thom Henderson developed the original version, but it is important to note that <i>arc</i> is based on the file compression theories developed by Huffman, Welch, Knott, Knuth, and many other scientists. This implementation is based on version 5.21 of the MSDOS program.</p>
<h2>BUGS</h2>
<p> <i>Arc</i> behaves just like the PC version of the program; all functions of the &quot;usage&quot; display are working. Full compatibility with PC ARC files is maintained, the price for which is that <i>arc</i> doesn&#8217;t like long filenames, and can only archive files with names of up to 12 characters. It will *sometimes* do The Right Thing with them, but I suggest you put long-winded filenames in a &quot;shar&quot; before <i>arc</i>ing them. </p>
<p> There shouldn&#8217;t be any problems, (hah!) but if you find any, please send them to me at: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>hyc [at] hanauma.jpl.nasa.gov</p>
<h2>AUTHORS</h2>
<p> Original MSDOS program by Thom Henderson<br />
 COPYRIGHT(C) 1985-87 by System Enhancement Associates; ALL RIGHTS RESERVED </p>
<p> Original Lempel-Zev code derived from compress 4.0. Modified to support Squashing by Dan Lanciani (ddl [at] harvard.edu) Ported from MSDOS by Howard Chu, with help from John Gilmore (hoptoad!gnu), James Turner (daisy!turner) and others. </p>
<h2>Index</h2>
