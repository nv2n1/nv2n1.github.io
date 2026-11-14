---
title: "zip(1)"
name: "zip"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zip/"
description: "zip – package and compress (archive) files"
---

<h2 class="name">NAME</h2>
<p> zip &#8211; package and compress (archive) files </p>
<h2>SYNOPSIS</h2>
<p> <code>zip</code> [-<code>aABcdDeEfFghjklLmoqrRSTuvVwXyz!@$</code>] [&#8211;longoption &#8230;] [-<code>b</code> path] [-<code>n</code> suffixes] [-<code>t</code> date] [-<code>tt</code> date] [<i>zipfile</i> [<i>file</i> &#8230;]] [<code>-xi</code> list] </p>
<p> <code>zipcloak</code> (see separate man page) </p>
<p> <code>zipnote</code> (see separate man page) </p>
<p> <code>zipsplit</code> (see separate man page) </p>
<p> Note: Command line processing in <i>zip</i> has been changed to support long options and handle all options and arguments more consistently. Some old command lines that depend on command line inconsistencies may no longer work.</p>
<h2>DESCRIPTION</h2>
<p> <i>zip</i> is a compression and file packaging utility for Unix, VMS, MSDOS, OS/2, Windows 9x/NT/XP, Minix, Atari, Macintosh, Amiga, and Acorn RISC OS. It is analogous to a combination of the Unix commands <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1) and <i><a href="/docs/linux/man/1-compress/">compress</a></i>(1) and is compatible with PKZIP (Phil Katz&#8217;s ZIP for MSDOS systems). </p>
<p> A companion program (<i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1)) unpacks <i>zip</i> archives. The <i>zip</i> and <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) programs can work with archives produced by PKZIP (supporting most PKZIP features up to PKZIP version 4.6), and PKZIP and PKUNZIP can work with archives produced by <i>zip</i> (with some exceptions, notably streamed archives, but recent changes in the zip file standard may facilitate better compatibility). <i>zip</i> version 3.0 is compatible with PKZIP 2.04 and also supports the Zip64 extensions of PKZIP 4.5 which allow archives as well as files to exceed the previous 2 GB limit (4 GB in some cases). <i>zip</i> also now supports <code>bzip2</code> compression if the <code>bzip2</code> library is included when <i>zip</i> is compiled. Note that PKUNZIP 1.10 cannot extract files produced by PKZIP 2.04 or <i>zip 3.0</i>. You must use PKUNZIP 2.04g or <i>unzip 5.0p1</i> (or later versions) to extract them. </p>
<p> See the <code>EXAMPLES</code> section at the bottom of this page for examples of some typical uses of <i>zip</i>. </p>
<p> <code>Large Archives and Zip64.</code> <i>zip</i> automatically uses the Zip64 extensions when files larger than 4 GB are added to an archive, an archive containing Zip64 entries is updated (if the resulting archive still needs Zip64), the size of the archive will exceed 4 GB, or when the number of entries in the archive will exceed about 64K. Zip64 is also used for archives streamed from standard input as the size of such archives are not known in advance, but the option <code>-fz-</code> can be used to force <i>zip</i> to create PKZIP 2 compatible archives (as long as Zip64 extensions are not needed). You must use a PKZIP 4.5 compatible unzip, such as <i>unzip 6.0</i> or later, to extract files using the Zip64 extensions. </p>
<p> In addition, streamed archives, entries encrypted with standard encryption, or split archives created with the pause option may not be compatible with PKZIP as data descriptors are used and PKZIP at the time of this writing does not support data descriptors (but recent changes in the PKWare published zip standard now include some support for the data descriptor format <i>zip</i> uses). </p>
<p> <code>Mac OS X.</code> Though previous Mac versions had their own <i>zip</i> port, <i>zip</i> supports Mac OS X as part of the Unix port and most Unix features apply. References to &quot;MacOS&quot; below generally refer to MacOS versions older than OS X. Support for some Mac OS features in the Unix Mac OS X port, such as resource forks, is expected in the next <i>zip</i> release. </p>
<p> For a brief help on <i>zip</i> and <i>unzip</i>, run each without specifying any parameters on the command line. </p>
<h2>USE</h2>
<p> The program is useful for packaging a set of files for distribution; for archiving files; and for saving disk space by temporarily compressing unused files or directories. </p>
<p> The <i>zip</i> program puts one or more compressed files into a single <i>zip</i> archive, along with information about the files (name, path, date, time of last modification, protection, and check information to verify file integrity). An entire directory structure can be packed into a <i>zip</i> archive with a single command. Compression ratios of 2:1 to 3:1 are common for text files. <i>zip</i> has one compression method (deflation) and can also store files without compression. (If <code>bzip2</code> support is added, <i>zip</i> can also compress using <code>bzip2</code> compression, but such entries require a reasonably modern unzip to decompress. When <code>bzip2</code> compression is selected, it replaces deflation as the default method.) <i>zip</i> automatically chooses the better of the two (deflation or store or, if <code>bzip2</code> is selected, <code>bzip2</code> or store) for each file to be compressed. </p>
<p> <code>Command format.</code> The basic command format is</p>
<dl>
<dt>
<dd> <code>zip</code> options archive inpath inpath &#8230;</dl>
<p> where <code>archive</code> is a new or existing <i>zip</i> archive and <code>inpath</code> is a directory or file path optionally including wildcards. When given the name of an existing <i>zip</i> archive, <i>zip</i> will replace identically named entries in the <i>zip</i> archive (matching the relative names as stored in the archive) or add entries for new names. For example, if <i>foo.zip</i> exists and contains <i>foo/file1</i> and <i>foo/file2</i>, and the directory <i>foo</i> contains the files <i>foo/file1</i> and <i>foo/file3</i>, then:</p>
<dl>
<dt>
<dd> zip -r foo.zip foo</dl>
<p> or more concisely</p>
<dl>
<dt>
<dd> zip -r foo foo</dl>
<p> will replace <i>foo/file1</i> in <i>foo.zip</i> and add <i>foo/file3</i> to <i>foo.zip</i>. After this, <i>foo.zip</i> contains <i>foo/file1</i>, <i>foo/file2</i>, and <i>foo/file3</i>, with <i>foo/file2</i> unchanged from before. </p>
<p> So if before the zip command is executed <i>foo.zip</i> has:</p>
<dl>
<dt>
<dd> foo/file1 foo/file2</dl>
<p> and directory foo has:</p>
<dl>
<dt>
<dd> file1 file3</dl>
<p> then <i>foo.zip</i> will have:</p>
<dl>
<dt>
<dd> foo/file1 foo/file2 foo/file3</dl>
<p> where <i>foo/file1</i> is replaced and <i>foo/file3</i> is new. </p>
<p> <code>-@&nbsp;file lists.</code> If a file list is specified as <code>-@</code> [Not on MacOS], <i>zip</i> takes the list of input files from standard input instead of from the command line. For example,</p>
<dl>
<dt>
<dd> zip -@ foo</dl>
<p> will store the files listed one per line on stdin in <i>foo.zip</i>. </p>
<p> Under Unix, this option can be used to powerful effect in conjunction with the <i>find</i>&nbsp;(1) command. For example, to archive all the C source files in the current directory and its subdirectories:</p>
<dl>
<dt>
<dd> find . -name &quot;*.[ch]&quot; -print | zip source -@</dl>
<p> (note that the pattern must be quoted to keep the shell from expanding it). </p>
<p> <code>Streaming input and output.</code> <i>zip</i> will also accept a single dash (&quot;-&quot;) as the zip file name, in which case it will write the zip file to standard output, allowing the output to be piped to another program. For example:</p>
<dl>
<dt>
<dd> zip -r &#8211; . | dd of=/dev/nrst0 obs=16k</dl>
<p> would write the zip output directly to a tape with the specified block size for the purpose of backing up the current directory. </p>
<p> <i>zip</i> also accepts a single dash (&quot;-&quot;) as the name of a file to be compressed, in which case it will read the file from standard input, allowing zip to take input from another program. For example:</p>
<dl>
<dt>
<dd> tar cf &#8211; . | zip backup &#8211;</dl>
<p> would compress the output of the tar command for the purpose of backing up the current directory. This generally produces better compression than the previous example using the -r option because <i>zip</i> can take advantage of redundancy between files. The backup can be restored using the command</p>
<dl>
<dt>
<dd> unzip -p backup | tar xf &#8211;</dl>
<p> When no zip file name is given and stdout is not a terminal, <i>zip</i> acts as a filter, compressing standard input to standard output. For example,</p>
<dl>
<dt>
<dd> tar cf &#8211; . | zip | dd of=/dev/nrst0 obs=16k</dl>
<p> is equivalent to</p>
<dl>
<dt>
<dd> tar cf &#8211; . | zip &#8211; &#8211; | dd of=/dev/nrst0 obs=16k</dl>
<p> <i>zip</i> archives created in this manner can be extracted with the program <i>funzip</i> which is provided in the <i>unzip</i> package, or by <i>gunzip</i> which is provided in the <i>gzip</i> package (but some <i>gunzip</i> may not support this if <i>zip</i> used the Zip64 extensions). For example:</p>
<dl>
<dt>
<dd> dd if=/dev/nrst0 ibs=16k | funzip | tar xvf &#8211;</dl>
<p> The stream can also be saved to a file and <i>unzip</i> used. </p>
<p> If Zip64 support for large files and archives is enabled and <i>zip</i> is used as a filter, <i>zip</i> creates a Zip64 archive that requires a PKZIP 4.5 or later compatible unzip to read it. This is to avoid ambiguities in the zip file structure as defined in the current zip standard (PKWARE AppNote) where the decision to use Zip64 needs to be made before data is written for the entry, but for a stream the size of the data is not known at that point. If the data is known to be smaller than 4 GB, the option <code>-fz-</code> can be used to prevent use of Zip64, but <i>zip</i> will exit with an error if Zip64 was in fact needed. <i>zip 3</i> and <i>unzip 6</i> and later can read archives with Zip64 entries. Also, <i>zip</i> removes the Zip64 extensions if not needed when archive entries are copied (see the <code>-U</code> (<code>&#8211;copy</code>) option). </p>
<p> When directing the output to another file, note that all options should be before the redirection including <code>-x</code>. For example:</p>
<dl>
<dt>
<dd> zip archive &quot;*.h&quot; &quot;*.c&quot; -x donotinclude.h orthis.h &gt; tofile</dl>
<p> <code>Zip files.</code> When changing an existing <i>zip</i> archive, <i>zip</i> will write a temporary file with the new contents, and only replace the old one when the process of creating the new version has been completed without error. </p>
<p> If the name of the <i>zip</i> archive does not contain an extension, the extension <code>.zip</code> is added. If the name already contains an extension other than <code>.zip</code>, the existing extension is kept unchanged. However, split archives (archives split over multiple files) require the <code>.zip</code> extension on the last split. </p>
<p> <code>Scanning and reading files.</code> When <i>zip</i> starts, it scans for files to process (if needed). If this scan takes longer than about 5 seconds, <i>zip</i> will display a &quot;Scanning files&quot; message and start displaying progress dots every 2 seconds or every so many entries processed, whichever takes longer. If there is more than 2 seconds between dots it could indicate that finding each file is taking time and could mean a slow network connection for example. (Actually the initial file scan is a two-step process where the directory scan is followed by a sort and these two steps are separated with a space in the dots. If updating an existing archive, a space also appears between the existing file scan and the new file scan.) The scanning files dots are not controlled by the <code>-ds</code> dot size option, but the dots are turned off by the <code>-q</code> quiet option. The <code>-sf</code> show files option can be used to scan for files and get the list of files scanned without actually processing them. </p>
<p> If <i>zip</i> is not able to read a file, it issues a warning but continues. See the <code>-MM</code> option below for more on how <i>zip</i> handles patterns that are not matched and files that are not readable. If some files were skipped, a warning is issued at the end of the zip operation noting how many files were read and how many skipped. </p>
<p> <code>Command modes.</code> <i>zip</i> now supports two distinct types of command modes, <code>external</code> and <code>internal</code>. The <code>external</code> modes (add, update, and freshen) read files from the file system (as well as from an existing archive) while the <code>internal</code> modes (delete and copy) operate exclusively on entries in an existing archive. </p>
<dl>
<dt><code>add&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Update existing entries and add new files. If the archive does not exist create it. This is the default mode.</p>
<dt><code>update&nbsp;</code>(<code>-u</code>)</p>
<dd> Update existing entries if newer on the file system and add new files. If the archive does not exist issue warning then create a new archive.</p>
<dt><code>freshen&nbsp;</code>(<code>-f</code>)</p>
<dd> Update existing entries of an archive if newer on the file system. Does not add new files to the archive.</p>
<dt><code>delete&nbsp;</code>(<code>-d</code>)</p>
<dd> Select entries in an existing archive and delete them.</p>
<dt><code>copy&nbsp;</code>(<code>-U</code>)</p>
<dd> Select entries in an existing archive and copy them to a new archive. This new mode is similar to <code>update</code> but command line patterns select entries in the existing archive rather than files from the file system and it uses the <code>&#8211;out</code> option to write the resulting archive to a new file rather than update the existing archive, leaving the original archive unchanged.</dl>
<p> The new File Sync option (<code>-FS</code>) is also considered a new mode, though it is similar to <code>update</code>. This mode synchronizes the archive with the files on the OS, only replacing files in the archive if the file time or size of the OS file is different, adding new files, and deleting entries from the archive where there is no matching file. As this mode can delete entries from the archive, consider making a backup copy of the archive. </p>
<p> Also see <code>-DF</code> for creating difference archives. </p>
<p> See each option description below for details and the <code>EXAMPLES</code> section below for examples. </p>
<p> <code>Split archives.</code> <i>zip</i> version 3.0 and later can create split archives. A <code>split archive</code> is a standard zip archive split over multiple files. (Note that split archives are not just archives split in to pieces, as the offsets of entries are now based on the start of each split. Concatenating the pieces together will invalidate these offsets, but <i>unzip</i> can usually deal with it. <i>zip</i> will usually refuse to process such a spliced archive unless the <code>-FF</code> fix option is used to fix the offsets.) </p>
<p> One use of split archives is storing a large archive on multiple removable media. For a split archive with 20 split files the files are typically named (replace ARCHIVE with the name of your archive) ARCHIVE.z01, ARCHIVE.z02, &#8230;, ARCHIVE.z19, ARCHIVE.zip. Note that the last file is the <code>.zip</code> file. In contrast, <code>spanned archives</code> are the original multi-disk archive generally requiring floppy disks and using volume labels to store disk numbers. <i>zip</i> supports split archives but not spanned archives, though a procedure exists for converting split archives of the right size to spanned archives. The reverse is also true, where each file of a spanned archive can be copied in order to files with the above names to create a split archive. </p>
<p> Use <code>-s</code> to set the split size and create a split archive. The size is given as a number followed optionally by one of k (kB), m (MB), g (GB), or t (TB) (the default is m). The <code>-sp</code> option can be used to pause <i>zip</i> between splits to allow changing removable media, for example, but read the descriptions and warnings for both <code>-s</code> and <code>-sp</code> below. </p>
<p> Though <i>zip</i> does not update split archives, <i>zip</i> provides the new option <code>-O</code> (<code>&#8211;output-file</code> or <code>&#8211;out</code>) to allow split archives to be updated and saved in a new archive. For example,</p>
<dl>
<dt>
<dd> zip inarchive.zip foo.c bar.c &#8211;out outarchive.zip</dl>
<p> reads archive <code>inarchive.zip</code>, even if split, adds the files <code>foo.c</code> and <code>bar.c</code>, and writes the resulting archive to <code>outarchive.zip</code>. If <code>inarchive.zip</code> is split then <code>outarchive.zip</code> defaults to the same split size. Be aware that if <code>outarchive.zip</code> and any split files that are created with it already exist, these are always overwritten as needed without warning. This may be changed in the future. </p>
<p> <code>Unicode.</code> Though the zip standard requires storing paths in an archive using a specific character set, in practice zips have stored paths in archives in whatever the local character set is. This creates problems when an archive is created or updated on a system using one character set and then extracted on another system using a different character set. When compiled with Unicode support enabled on platforms that support wide characters, <i>zip</i> now stores, in addition to the standard local path for backward compatibility, the UTF-8 translation of the path. This provides a common universal character set for storing paths that allows these paths to be fully extracted on other systems that support Unicode and to match as close as possible on systems that don&#8217;t. </p>
<p> On Win32 systems where paths are internally stored as Unicode but represented in the local character set, it&#8217;s possible that some paths will be skipped during a local character set directory scan. <i>zip</i> with Unicode support now can read and store these paths. Note that Win 9x systems and FAT file systems don&#8217;t fully support Unicode. </p>
<p> Be aware that console windows on Win32 and Unix, for example, sometimes don&#8217;t accurately show all characters due to how each operating system switches in character sets for display. However, directory navigation tools should show the correct paths if the needed fonts are loaded. </p>
<p> <code>Command line format.</code> This version of <i>zip</i> has updated command line processing and support for long options. </p>
<p> Short options take the form</p>
<dl>
<dt>
<dd> -s[-][s[-]&#8230;][value][=value][&nbsp;value]</dl>
<p> where s is a one or two character short option. A short option that takes a value is last in an argument and anything after it is taken as the value. If the option can be negated and &quot;-&quot; immediately follows the option, the option is negated. Short options can also be given as separate arguments</p>
<dl>
<dt>
<dd> -s[-][value][=value][&nbsp;value]&nbsp;-s[-][value][=value][&nbsp;value]&nbsp;&#8230;</dl>
<p> Short options in general take values either as part of the same argument or as the following argument. An optional = is also supported. So</p>
<dl>
<dt>
<dd> -ttmmddyyyy</dl>
<p> and</p>
<dl>
<dt>
<dd> -tt=mmddyyyy</dl>
<p> and</p>
<dl>
<dt>
<dd> -tt mmddyyyy</dl>
<p> all work. The <code>-x</code> and <code>-i</code> options accept lists of values and use a slightly different format described below. See the <code>-x</code> and <code>-i</code> options. </p>
<p> Long options take the form</p>
<dl>
<dt>
<dd> &#8211;longoption[-][=value][ value]</dl>
<p> where the option starts with &#8211;, has a multicharacter name, can include a trailing dash to negate the option (if the option supports it), and can have a value (option argument) specified by preceding it with = (no spaces). Values can also follow the argument. So</p>
<dl>
<dt>
<dd> &#8211;before-date=mmddyyyy</dl>
<p> and</p>
<dl>
<dt>
<dd> &#8211;before-date mmddyyyy</dl>
<p> both work. </p>
<p> Long option names can be shortened to the shortest unique abbreviation. See the option descriptions below for which support long options. To avoid confusion, avoid abbreviating a negatable option with an embedded dash (&quot;-&quot;) at the dash if you plan to negate it (the parser would consider a trailing dash, such as for the option <code>&#8211;some-option</code> using <code>&#8211;some-</code> as the option, as part of the name rather than a negating dash). This may be changed to force the last dash in <code>&#8211;some-</code> to be negating in the future.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;ascii</code></p>
<dd> [Systems using EBCDIC] Translate file to ASCII format. </p>
<dt><code>-A</code></p>
<dd>
<dt><code>&#8211;adjust-sfx</code></p>
<dd> Adjust self-extracting executable archive. A self-extracting executable archive is created by prepending the SFX stub to an existing archive. The <code>-A</code> option tells <i>zip</i> to adjust the entry offsets stored in the archive to take into account this &quot;preamble&quot; data.</dl>
<p> Note: self-extracting archives for the Amiga are a special case. At present, only the Amiga port of <i>zip</i> is capable of adjusting or updating these without corrupting them. -J can be used to remove the SFX stub if other updates need to be made. </p>
<dl>
<dt><code>-AC</code></p>
<dd>
<dt><code>&#8211;archive-clear</code></p>
<dd> [WIN32] Once archive is created (and tested if <code>-T</code> is used, which is recommended), clear the archive bits of files processed. WARNING: Once the bits are cleared they are cleared. You may want to use the <code>-sf</code> show files option to store the list of files processed in case the archive operation must be repeated. Also consider using the <code>-MM</code> must match option. Be sure to check out <code>-DF</code> as a possibly better way to do incremental backups. </p>
<dt><code>-AS</code></p>
<dd>
<dt><code>&#8211;archive-set</code></p>
<dd> [WIN32] Only include files that have the archive bit set. Directories are not stored when <code>-AS</code> is used, though by default the paths of entries, including directories, are stored as usual and can be used by most unzips to recreate directories. </p>
<p> The archive bit is set by the operating system when a file is modified and, if used with <code>-AC</code>, <code>-AS</code> can provide an incremental backup capability. However, other applications can modify the archive bit and it may not be a reliable indicator of which files have changed since the last archive operation. Alternative ways to create incremental backups are using <code>-t</code> to use file dates, though this won&#8217;t catch old files copied to directories being archived, and <code>-DF</code> to create a differential archive. </p>
<dt><code>-B</code></p>
<dd>
<dt><code>&#8211;binary</code></p>
<dd> [VM/CMS and MVS] force file to be read binary (default is text). </p>
<dt><code>-B</code>n</p>
<dd> [TANDEM] set Edit/Enscribe formatting options with n defined as</p>
<dl>
<dt>
<dd> bit 0: Don&#8217;t add delimiter (Edit/Enscribe)</dl>
<dl>
<dt>
<dd> bit 1: Use LF rather than CR/LF as delimiter (Edit/Enscribe)</dl>
<dl>
<dt>
<dd> bit 2: Space fill record to maximum record length (Enscribe)</dl>
<dl>
<dt>
<dd> bit 3: Trim trailing space (Enscribe)</dl>
<dl>
<dt>
<dd> bit 8: Force 30K (Expand) large read for unstructured files</dl>
<dt><code>-b&nbsp;</code>path</p>
<dd>
<dt><code>&#8211;temp-path&nbsp;</code>path</p>
<dd> Use the specified <i>path</i> for the temporary <i>zip</i> archive. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -b /tmp stuff *</dl>
</dl>
<dt>
<dd> will put the temporary <i>zip</i> archive in the directory <i>/tmp</i>, copying over <i>stuff.zip</i> to the current directory when done. This option is useful when updating an existing archive and the file system containing this old archive does not have enough space to hold both old and new archives at the same time. It may also be useful when streaming in some cases to avoid the need for data descriptors. Note that using this option may require <i>zip</i> take additional time to copy the archive file when done to the destination file system. </p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;entry-comments</code></p>
<dd> Add one-line comments for each file. File operations (adding, updating) are done first, and the user is then prompted for a one-line comment for each file. Enter the comment followed by return, or just return for no comment. </p>
<dt><code>-C</code></p>
<dd>
<dt><code>&#8211;preserve-case</code></p>
<dd> [VMS] Preserve case all on VMS. Negating this option (<code>-C-</code>) downcases. </p>
<dt><code>-C2</code></p>
<dd>
<dt><code>&#8211;preserve-case-2</code></p>
<dd> [VMS] Preserve case ODS2 on VMS. Negating this option (<code>-C2-</code>) downcases. </p>
<dt><code>-C5</code></p>
<dd>
<dt><code>&#8211;preserve-case-5</code></p>
<dd> [VMS] Preserve case ODS5 on VMS. Negating this option (<code>-C5-</code>) downcases. </p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;delete</code></p>
<dd> Remove (delete) entries from a <i>zip</i> archive. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -d foo foo/tom/junk foo/harry/\* \*.o</dl>
</dl>
<dt>
<dd> will remove the entry <i>foo/tom/junk</i>, all of the files that start with <i>foo/harry/</i>, and all of the files that end with <code>.o</code> (in any path). Note that shell pathname expansion has been inhibited with backslashes, so that <i>zip</i> can see the asterisks, enabling <i>zip</i> to match on the contents of the <i>zip</i> archive instead of the contents of the current directory. (The backslashes are not used on MSDOS-based platforms.) Can also use quotes to escape the asterisks as in</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -d foo foo/tom/junk &quot;foo/harry/*&quot; &quot;*.o&quot;</dl>
</dl>
<dt>
<dd> Not escaping the asterisks on a system where the shell expands wildcards could result in the asterisks being converted to a list of files in the current directory and that list used to delete entries from the archive.</p>
<dt>
<dd> Under MSDOS, <code>-d</code> is case sensitive when it matches names in the <i>zip</i> archive. This requires that file names be entered in upper case if they were zipped by PKZIP on an MSDOS system. (We considered making this case insensitive on systems where paths were case insensitive, but it is possible the archive came from a system where case does matter and the archive could include both <code>Bar</code> and <code>bar</code> as separate files in the archive.) But see the new option <code>-ic</code> to ignore case in the archive. </p>
<dt><code>-db</code></p>
<dd>
<dt><code>&#8211;display-bytes</code></p>
<dd> Display running byte counts showing the bytes zipped and the bytes to go. </p>
<dt><code>-dc</code></p>
<dd>
<dt><code>&#8211;display-counts</code></p>
<dd> Display running count of entries zipped and entries to go. </p>
<dt><code>-dd</code></p>
<dd>
<dt><code>&#8211;display-dots</code></p>
<dd> Display dots while each entry is zipped (except on ports that have their own progress indicator). See <code>-ds</code> below for setting dot size. The default is a dot every 10 MB of input file processed. The <code>-v</code> option also displays dots (previously at a much higher rate than this but now <code>-v</code> also defaults to 10 MB) and this rate is also controlled by <code>-ds</code>. </p>
<dt><code>-df</code></p>
<dd>
<dt><code>&#8211;datafork</code></p>
<dd> [MacOS] Include only data-fork of files zipped into the archive. Good for exporting files to foreign operating-systems. Resource-forks will be ignored at all. </p>
<dt><code>-dg</code></p>
<dd>
<dt><code>&#8211;display-globaldots</code></p>
<dd> Display progress dots for the archive instead of for each file. The command</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;zip -qdgds 10m</dl>
</dl>
<dt>
<dd> will turn off most output except dots every 10 MB. </p>
<dt><code>-ds&nbsp;</code>size</p>
<dd>
<dt><code>&#8211;dot-size&nbsp;</code>size</p>
<dd> Set amount of input file processed for each dot displayed. See <code>-dd</code> to enable displaying dots. Setting this option implies <code>-dd</code>. Size is in the format nm where n is a number and m is a multiplier. Currently m can be k (KB), m (MB), g (GB), or t (TB), so if n is 100 and m is k, size would be 100k which is 100 KB. The default is 10 MB.</p>
<dt>
<dd> The <code>-v</code> option also displays dots and now defaults to 10 MB also. This rate is also controlled by this option. A size of 0 turns dots off.</p>
<dt>
<dd> This option does not control the dots from the &quot;Scanning files&quot; message as <i>zip</i> scans for input files. The dot size for that is fixed at 2 seconds or a fixed number of entries, whichever is longer. </p>
<dt><code>-du</code></p>
<dd>
<dt><code>&#8211;display-usize</code></p>
<dd> Display the uncompressed size of each entry. </p>
<dt><code>-dv</code></p>
<dd>
<dt><code>&#8211;display-volume</code></p>
<dd> Display the volume (disk) number each entry is being read from, if reading an existing archive, and being written to. </p>
<dt><code>-D</code></p>
<dd>
<dt><code>&#8211;no-dir-entries</code></p>
<dd> Do not create entries in the <i>zip</i> archive for directories. Directory entries are created by default so that their attributes can be saved in the zip archive. The environment variable ZIPOPT can be used to change the default options. For example under Unix with sh:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> ZIPOPT=&quot;-D&quot;; export ZIPOPT</dl>
</dl>
<dt>
<dd> (The variable ZIPOPT can be used for any option, including <code>-i</code> and <code>-x</code> using a new option format detailed below, and can include several options.) The option <code>-D</code> is a shorthand for <code>-x</code> &quot;*/&quot; but the latter previously could not be set as default in the ZIPOPT environment variable as the contents of ZIPOPT gets inserted near the beginning of the command line and the file list had to end at the end of the line.</p>
<dt>
<dd> This version of <i>zip</i> does allow <code>-x</code> and <code>-i</code> options in ZIPOPT if the form</p>
<dt>
<dd> <code>-x</code>&nbsp;file file &#8230;<code>&nbsp;@</code></p>
<dt>
<dd> is used, where the @ (an argument that is just @) terminates the list. </p>
<dt><code>-DF</code></p>
<dd>
<dt><code>&#8211;difference-archive</code></p>
<dd> Create an archive that contains all new and changed files since the original archive was created. For this to work, the input file list and current directory must be the same as during the original <i>zip</i> operation.</p>
<dt>
<dd> For example, if the existing archive was created using</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foofull .</dl>
</dl>
<dt>
<dd> from the <i>bar</i> directory, then the command</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foofull . -DF &#8211;out foonew</dl>
</dl>
<dt>
<dd> also from the <i>bar</i> directory creates the archive <i>foonew</i> with just the files not in <i>foofull</i> and the files where the size or file time of the files do not match those in <i>foofull</i>. </p>
<p> Note that the timezone environment variable TZ should be set according to the local timezone in order for this option to work correctly. A change in timezone since the original archive was created could result in no times matching and all files being included. </p>
<p> A possible approach to backing up a directory might be to create a normal archive of the contents of the directory as a full backup, then use this option to create incremental backups. </p>
<dt><code>-e</code></p>
<dd>
<dt><code>&#8211;encrypt</code></p>
<dd> Encrypt the contents of the <i>zip</i> archive using a password which is entered on the terminal in response to a prompt (this will not be echoed; if standard error is not a tty, <i>zip</i> will exit with an error). The password prompt is repeated to save the user from typing errors. </p>
<dt><code>-E</code></p>
<dd>
<dt><code>&#8211;longnames</code></p>
<dd> [OS/2] Use the .LONGNAME Extended Attribute (if found) as filename. </p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;freshen</code></p>
<dd> Replace (freshen) an existing entry in the <i>zip</i> archive only if it has been modified more recently than the version already in the <i>zip</i> archive; unlike the update option (<code>-u</code>) this will not add files that are not already in the <i>zip</i> archive. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -f foo</dl>
</dl>
<dt>
<dd> This command should be run from the same directory from which the original <i>zip</i> command was run, since paths stored in <i>zip</i> archives are always relative.</p>
<dt>
<dd> Note that the timezone environment variable TZ should be set according to the local timezone in order for the <code>-f</code>, <code>-u</code> and <code>-o</code> options to work correctly.</p>
<dt>
<dd> The reasons behind this are somewhat subtle but have to do with the differences between the Unix-format file times (always in GMT) and most of the other operating systems (always local time) and the necessity to compare the two. A typical TZ value is &#8220;MET-1MEST&#8221; (Middle European time with automatic adjustment for &#8220;summertime&#8221; or Daylight Savings Time).</p>
<dt>
<dd> The format is TTThhDDD, where TTT is the time zone such as MET, hh is the difference between GMT and local time such as -1 above, and DDD is the time zone when daylight savings time is in effect. Leave off the DDD if there is no daylight savings time. For the US Eastern time zone EST5EDT. </p>
<dt><code>-F</code></p>
<dd>
<dt><code>&#8211;fix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd>
<dt><code>-FF</code></p>
<dd>
<dt><code>&#8211;fixfix&nbsp;<wbr>&nbsp;</code></p>
<dd> Fix the <i>zip</i> archive. The <code>-F</code> option can be used if some portions of the archive are missing, but requires a reasonably intact central directory. The input archive is scanned as usual, but <i>zip</i> will ignore some problems. The resulting archive should be valid, but any inconsistent entries will be left out.</p>
<dt>
<dd> When doubled as in <code>-FF</code>, the archive is scanned from the beginning and <i>zip</i> scans for special signatures to identify the limits between the archive members. The single <code>-F</code> is more reliable if the archive is not too much damaged, so try this option first.</p>
<dt>
<dd> If the archive is too damaged or the end has been truncated, you must use <code>-FF</code>. This is a change from <i>zip 2.32</i>, where the <code>-F</code> option is able to read a truncated archive. The <code>-F</code> option now more reliably fixes archives with minor damage and the <code>-FF</code> option is needed to fix archives where <code>-F</code> might have been sufficient before.</p>
<dt>
<dd> Neither option will recover archives that have been incorrectly transferred in ascii mode instead of binary. After the repair, the <code>-t</code> option of <i>unzip</i> may show that some files have a bad CRC. Such files cannot be recovered; you can remove them from the archive using the <code>-d</code> option of <i>zip</i>.</p>
<dt>
<dd> Note that <code>-FF</code> may have trouble fixing archives that include an embedded zip archive that was stored (without compression) in the archive and, depending on the damage, it may find the entries in the embedded archive rather than the archive itself. Try <code>-F</code> first as it does not have this problem.</p>
<dt>
<dd> The format of the fix commands have changed. For example, to fix the damaged archive <i>foo.zip</i>,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -F foo &#8211;out foofix</dl>
</dl>
<dt>
<dd> tries to read the entries normally, copying good entries to the new archive <i>foofix.zip</i>. If this doesn&#8217;t work, as when the archive is truncated, or if some entries you know are in the archive are missed, then try</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -FF foo &#8211;out foofixfix</dl>
</dl>
<dt>
<dd> and compare the resulting archive to the archive created by <code>-F</code>. The <code>-FF</code> option may create an inconsistent archive. Depending on what is damaged, you can then use the <code>-F</code> option to fix that archive.</p>
<dt>
<dd> A split archive with missing split files can be fixed using <code>-F</code> if you have the last split of the archive (the <code>.zip</code> file). If this file is missing, you must use <code>-FF</code> to fix the archive, which will prompt you for the splits you have.</p>
<dt>
<dd> Currently the fix options can&#8217;t recover entries that have a bad checksum or are otherwise damaged. </p>
<dt><code>-FI</code></p>
<dd>
<dt><code>&#8211;fifo</code></p>
<dd> [Unix] Normally <i>zip</i> skips reading any FIFOs (named pipes) encountered, as <i>zip</i> can hang if the FIFO is not being fed. This option tells <i>zip</i> to read the contents of any FIFO it finds. </p>
<dt><code>-FS</code></p>
<dd>
<dt><code>&#8211;filesync</code></p>
<dd> Synchronize the contents of an archive with the files on the OS. Normally when an archive is updated, new files are added and changed files are updated but files that no longer exist on the OS are not deleted from the archive. This option enables a new mode that checks entries in the archive against the file system. If the file time and file size of the entry matches that of the OS file, the entry is copied from the old archive instead of being read from the file system and compressed. If the OS file has changed, the entry is read and compressed as usual. If the entry in the archive does not match a file on the OS, the entry is deleted. Enabling this option should create archives that are the same as new archives, but since existing entries are copied instead of compressed, updating an existing archive with <code>-FS</code> can be much faster than creating a new archive. Also consider using <code>-u</code> for updating an archive.</p>
<dt>
<dd> For this option to work, the archive should be updated from the same directory it was created in so the relative paths match. If few files are being copied from the old archive, it may be faster to create a new archive instead.</p>
<dt>
<dd> Note that the timezone environment variable TZ should be set according to the local timezone in order for this option to work correctly. A change in timezone since the original archive was created could result in no times matching and recompression of all files.</p>
<dt>
<dd> This option deletes files from the archive. If you need to preserve the original archive, make a copy of the archive first or use the <code>&#8211;out</code> option to output the updated archive to a new file. Even though it may be slower, creating a new archive with a new archive name is safer, avoids mismatches between archive and OS paths, and is preferred. </p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;grow &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Grow (append to) the specified <i>zip</i> archive, instead of creating a new one. If this operation fails, <i>zip</i> attempts to restore the archive to its original state. If the restoration fails, the archive might become corrupted. This option is ignored when there&#8217;s no existing archive or when at least one archive member must be updated or deleted. </p>
<dt><code>-h</code></p>
<dd>
<dt><code>-?</code></p>
<dd>
<dt><code>&#8211;help &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Display the <i>zip</i> help information (this also appears if <i>zip</i> is run with no arguments). </p>
<dt><code>-h2</code></p>
<dd>
<dt><code>&#8211;more-help</code></p>
<dd> Display extended help including more on command line format, pattern matching, and more obscure options. </p>
<dt><code>-i&nbsp;</code>files</p>
<dd>
<dt><code>&#8211;include&nbsp;</code>files</p>
<dd> Include only the specified files, as in:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo . -i \*.c</dl>
</dl>
<dt>
<dd> which will include only the files that end in <i></i>.c in the current directory and its subdirectories. (Note for PKZIP users: the equivalent command is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> pkzip -rP foo *.c</dl>
</dl>
<dt>
<dd> PKZIP does not allow recursion in directories other than the current one.) The backslash avoids the shell filename substitution, so that the name matching is performed by <i>zip</i> at all directory levels. [This is for Unix and other systems where \ escapes the next character. For other systems where the shell does not process * do not use \ and the above is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo . -i *.c</dl>
</dl>
<dt>
<dd> Examples are for Unix unless otherwise specified.] So to include dir, a directory directly under the current directory, use</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo . -i dir/\*</dl>
</dl>
<dt>
<dd> or</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo . -i &quot;dir/*&quot;</dl>
</dl>
<dt>
<dd> to match paths such as dir/a and dir/b/file.c [on ports without wildcard expansion in the shell such as MSDOS and Windows</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo . -i dir/*</dl>
</dl>
<dt>
<dd> is used.] Note that currently the trailing / is needed for directories (as in</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo . -i dir/</dl>
</dl>
<dt>
<dd> to include directory dir).</p>
<dt>
<dd> The long option form of the first example is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo . &#8211;include \*.c</dl>
</dl>
<dt>
<dd> and does the same thing as the short option form.</p>
<dt>
<dd> Though the command syntax used to require <code>-i</code> at the end of the command line, this version actually allows <code>-i</code> (or <code>&#8211;include</code>) anywhere. The list of files terminates at the next argument starting with <code>&#8211;</code>, the end of the command line, or the list terminator <code>@</code> (an argument that is just @). So the above can be given as</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -i \*.c @ -r foo .</dl>
</dl>
<dt>
<dd> for example. There must be a space between the option and the first file of a list. For just one file you can use the single value form</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -i\*.c -r foo .</dl>
</dl>
<dt>
<dd> (no space between option and value) or</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip &#8211;include=\*.c -r foo .</dl>
</dl>
<dt>
<dd> as additional examples. The single value forms are not recommended because they can be confusing and, in particular, the <code>-ifile</code> format can cause problems if the first letter of <code>file</code> combines with <code>i</code> to form a two-letter option starting with <code>i</code>. Use <code>-sc</code> to see how your command line will be parsed.</p>
<dt>
<dd> Also possible:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo . -i [at] include.lst</dl>
</dl>
<dt>
<dd> which will only include the files in the current directory and its subdirectories that match the patterns in the file include.lst.</p>
<dt>
<dd> Files to <code>-i</code> and <code>-x</code> are patterns matching internal archive paths. See <code>-R</code> for more on patterns. </p>
<dt><code>-I</code></p>
<dd>
<dt><code>&#8211;no-image</code></p>
<dd> [Acorn RISC OS] Don&#8217;t scan through Image files. When used, <i>zip</i> will not consider Image files (eg. DOS partitions or Spark archives when SparkFS is loaded) as directories but will store them as single files. </p>
<p> For example, if you have SparkFS loaded, zipping a Spark archive will result in a zipfile containing a directory (and its content) while using the &#8216;I&#8217; option will result in a zipfile containing a Spark archive. Obviously this second case will also be obtained (without the &#8216;I&#8217; option) if SparkFS isn&#8217;t loaded. </p>
<dt><code>-ic</code></p>
<dd>
<dt><code>&#8211;ignore-case</code></p>
<dd> [VMS, WIN32] Ignore case when matching archive entries. This option is only available on systems where the case of files is ignored. On systems with case-insensitive file systems, case is normally ignored when matching files on the file system but is not ignored for -f (freshen), -d (delete), -U (copy), and similar modes when matching against archive entries (currently -f ignores case on VMS) because archive entries can be from systems where case does matter and names that are the same except for case can exist in an archive. The <code>-ic</code> option makes all matching case insensitive. This can result in multiple archive entries matching a command line pattern. </p>
<dt><code>-j</code></p>
<dd>
<dt><code>&#8211;junk-paths</code></p>
<dd> Store just the name of a saved file (junk the path), and do not store directory names. By default, <i>zip</i> will store the full path (relative to the current directory). </p>
<dt><code>-jj</code></p>
<dd>
<dt><code>&#8211;absolute-path</code></p>
<dd> [MacOS] record Fullpath (+ Volname). The complete path including volume will be stored. By default the relative path will be stored. </p>
<dt><code>-J</code></p>
<dd>
<dt><code>&#8211;junk-sfx</code></p>
<dd> Strip any prepended data (e.g. a SFX stub) from the archive.</p>
<dt><code>-k</code></p>
<dd>
<dt><code>&#8211;DOS-names</code></p>
<dd> Attempt to convert the names and paths to conform to MSDOS, store only the MSDOS attribute (just the user write attribute from Unix), and mark the entry as made under MSDOS (even though it was not); for compatibility with PKUNZIP under MSDOS which cannot handle certain names such as those with two dots.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;to-crlf</code></p>
<dd> Translate the Unix end-of-line character LF into the MSDOS convention CR LF. This option should not be used on binary files. This option can be used on Unix if the zip file is intended for PKUNZIP under MSDOS. If the input files already contain CR LF, this option adds an extra CR. This is to ensure that <code>unzip -a</code> on Unix will get back an exact copy of the original file, to undo the effect of <code>zip -l</code>. See <code>-ll</code> for how binary files are handled.</p>
<dt><code>-la</code></p>
<dd>
<dt><code>&#8211;log-append</code></p>
<dd> Append to existing logfile. Default is to overwrite.</p>
<dt><code>-lf&nbsp;</code>logfilepath</p>
<dd>
<dt><code>&#8211;logfile-path&nbsp;</code>logfilepath</p>
<dd> Open a logfile at the given path. By default any existing file at that location is overwritten, but the <code>-la</code> option will result in an existing file being opened and the new log information appended to any existing information. Only warnings and errors are written to the log unless the <code>-li</code> option is also given, then all information messages are also written to the log.</p>
<dt><code>-li</code></p>
<dd>
<dt><code>&#8211;log-info</code></p>
<dd> Include information messages, such as file names being zipped, in the log. The default is to only include the command line, any warnings and errors, and the final status.</p>
<dt><code>-ll</code></p>
<dd>
<dt><code>&#8211;from-crlf</code></p>
<dd> Translate the MSDOS end-of-line CR LF into Unix LF. This option should not be used on binary files. This option can be used on MSDOS if the zip file is intended for unzip under Unix. If the file is converted and the file is later determined to be binary a warning is issued and the file is probably corrupted. In this release if <code>-ll</code> detects binary in the first buffer read from a file, <i>zip</i> now issues a warning and skips line end conversion on the file. This check seems to catch all binary files tested, but the original check remains and if a converted file is later determined to be binary that warning is still issued. A new algorithm is now being used for binary detection that should allow line end conversion of text files in <code>UTF-8</code> and similar encodings.</p>
<dt><code>-L</code></p>
<dd>
<dt><code>&#8211;license</code></p>
<dd> Display the <i>zip</i> license.</p>
<dt><code>-m</code></p>
<dd>
<dt><code>&#8211;move &nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Move the specified files into the <i>zip</i> archive; actually, this deletes the target directories/files after making the specified <i>zip</i> archive. If a directory becomes empty after removal of the files, the directory is also removed. No deletions are done until <i>zip</i> has created the archive without error. This is useful for conserving disk space, but is potentially dangerous so it is recommended to use it in combination with <code>-T</code> to test the archive before removing all input files.</p>
<dt><code>-MM</code></p>
<dd>
<dt><code>&#8211;must-match</code></p>
<dd> All input patterns must match at least one file and all input files found must be readable. Normally when an input pattern does not match a file the &quot;name not matched&quot; warning is issued and when an input file has been found but later is missing or not readable a missing or not readable warning is issued. In either case <i>zip</i> continues creating the archive, with missing or unreadable new files being skipped and files already in the archive remaining unchanged. After the archive is created, if any files were not readable <i>zip</i> returns the OPEN error code (18 on most systems) instead of the normal success return (0 on most systems). With <code>-MM</code> set, <i>zip</i> exits as soon as an input pattern is not matched (whenever the &quot;name not matched&quot; warning would be issued) or when an input file is not readable. In either case <i>zip</i> exits with an OPEN error and no archive is created.</p>
<dt>
<dd> This option is useful when a known list of files is to be zipped so any missing or unreadable files will result in an error. It is less useful when used with wildcards, but <i>zip</i> will still exit with an error if any input pattern doesn&#8217;t match at least one file and if any matched files are unreadable. If you want to create the archive anyway and only need to know if files were skipped, don&#8217;t use <code>-MM</code> and just check the return code. Also <code>-lf</code> could be useful.</p>
<dt><code>-n&nbsp;</code>suffixes</p>
<dd>
<dt><code>&#8211;suffixes&nbsp;</code>suffixes</p>
<dd> Do not attempt to compress files named with the given <code>suffixes</code>. Such files are simply stored (0% compression) in the output zip file, so that <i>zip</i> doesn&#8217;t waste its time trying to compress them. The suffixes are separated by either colons or semicolons. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -rn .Z:.zip:.tiff:.gif:.snd foo foo</dl>
</dl>
<dt>
<dd> will copy everything from <i>foo</i> into <i>foo.zip</i>, but will store any files that end in <i>.Z</i>, <i>.zip</i>, <i>.tiff</i>, <i>.gif</i>, or <i>.snd</i> without trying to compress them (image and sound files often have their own specialized compression methods). By default, <i>zip</i> does not compress files with extensions in the list <i>.Z:.zip:.zoo:.arc:.lzh:.arj.</i> Such files are stored directly in the output archive. The environment variable ZIPOPT can be used to change the default options. For example under Unix with csh:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> setenv ZIPOPT &quot;-n .gif:.zip&quot;</dl>
</dl>
<dt>
<dd> To attempt compression on all files, use:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -n : foo</dl>
</dl>
<dt>
<dd> The maximum compression option <code>-9</code> also attempts compression on all files regardless of extension.</p>
<dt>
<dd> On Acorn RISC OS systems the suffixes are actually filetypes (3 hex digit format). By default, <i>zip</i> does not compress files with filetypes in the list DDC:D96:68E (i.e. Archives, CFS files and PackDir files).</p>
<dt><code>-nw</code></p>
<dd>
<dt><code>&#8211;no-wild</code></p>
<dd> Do not perform internal wildcard processing (shell processing of wildcards is still done by the shell unless the arguments are escaped). Useful if a list of paths is being read and no wildcard substitution is desired.</p>
<dt><code>-N</code></p>
<dd>
<dt><code>&#8211;notes</code></p>
<dd> [Amiga, MacOS] Save Amiga or MacOS filenotes as zipfile comments. They can be restored by using the -N option of <i>unzip</i>. If -c is used also, you are prompted for comments only for those files that do not have filenotes.</p>
<dt><code>-o</code></p>
<dd>
<dt><code>&#8211;latest-time</code></p>
<dd> Set the &quot;last modified&quot; time of the <i>zip</i> archive to the latest (oldest) &quot;last modified&quot; time found among the entries in the <i>zip</i> archive. This can be used without any other operations, if desired. For example:</p>
<dt>
<dd> zip -o foo</p>
<dt>
<dd> will change the last modified time of <code>foo.zip</code> to the latest time of the entries in <code>foo.zip</code>.</p>
<dt><code>-O </code>output-file</p>
<dd>
<dt><code>&#8211;output-file </code>output-file</p>
<dd> Process the archive changes as usual, but instead of updating the existing archive, output the new archive to output-file. Useful for updating an archive without changing the existing archive and the input archive must be a different file than the output archive. </p>
<p> This option can be used to create updated split archives. It can also be used with <code>-U</code> to copy entries from an existing archive to a new archive. See the <code>EXAMPLES</code> section below. </p>
<p> Another use is converting <i>zip</i> files from one split size to another. For instance, to convert an archive with 700 MB CD splits to one with 2 GB DVD splits, can use:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -s 2g cd-split.zip &#8211;out dvd-split.zip</dl>
</dl>
<dt>
<dd> which uses copy mode. See <code>-U</code> below. Also:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -s 0 split.zip &#8211;out unsplit.zip</dl>
</dl>
<dt>
<dd> will convert a split archive to a single-file archive. </p>
<p> Copy mode will convert stream entries (using data descriptors and which should be compatible with most unzips) to normal entries (which should be compatible with all unzips), except if standard encryption was used. For archives with encrypted entries, <i>zipcloak</i> will decrypt the entries and convert them to normal entries.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;paths</code></p>
<dd> Include relative file paths as part of the names of files stored in the archive. This is the default. The <code>-j</code> option junks the paths and just stores the names of the files.</p>
<dt><code>-P&nbsp;</code>password</p>
<dd>
<dt><code>&#8211;password&nbsp;</code>password</p>
<dd> Use <i>password</i> to encrypt zipfile entries (if any). <code>THIS IS INSECURE!</code> Many multi-user operating systems provide ways for any user to see the current command line of any other user; even on stand-alone systems there is always the threat of over-the-shoulder peeking. Storing the plaintext password as part of a command line in an automated script is even worse. Whenever possible, use the non-echoing, interactive prompt to enter passwords. (And where security is truly important, use strong encryption such as Pretty Good Privacy instead of the relatively weak standard encryption provided by zipfile utilities.)</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Quiet mode; eliminate informational messages and comment prompts. (Useful, for example, in shell scripts and background tasks).</p>
<dt><code>-Q</code>n</p>
<dd>
<dt><code>&#8211;Q-flag&nbsp;</code>n</p>
<dd> [QDOS] store information about the file in the file header with n defined as</p>
<dl>
<dt>
<dd> bit 0: Don&#8217;t add headers for any file</dl>
<dl>
<dt>
<dd> bit 1: Add headers for all files</dl>
<dl>
<dt>
<dd> bit 2: Don&#8217;t wait for interactive key press on exit</dl>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;recurse-paths</code></p>
<dd> Travel the directory structure recursively; for example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo.zip foo</dl>
</dl>
<dt>
<dd> or more concisely</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo foo</dl>
</dl>
<dt>
<dd> In this case, all the files and directories in <code>foo</code> are saved in a <i>zip</i> archive named <code>foo.zip</code>, including files with names starting with <code>&quot;.&quot;</code>, since the recursion does not use the shell&#8217;s file-name substitution mechanism. If you wish to include only a specific subset of the files in directory <code>foo</code> and its subdirectories, use the <code>-i</code> option to specify the pattern of files to be included. You should not use <code>-r</code> with the name <code>&quot;.*&quot;</code>, since that matches <code>&quot;..&quot;</code> which will attempt to zip up the parent directory (probably not what was intended).</p>
<dt>
<dd> Multiple source directories are allowed as in</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo foo1 foo2</dl>
</dl>
<dt>
<dd> which first zips up <code>foo1</code> and then <code>foo2</code>, going down each directory.</p>
<dt>
<dd> Note that while wildcards to <code>-r</code> are typically resolved while recursing down directories in the file system, any <code>-R</code>, <code>-x</code>, and <code>-i</code> wildcards are applied to internal archive pathnames once the directories are scanned. To have wildcards apply to files in subdirectories when recursing on Unix and similar systems where the shell does wildcard substitution, either escape all wildcards or put all arguments with wildcards in quotes. This lets <i>zip</i> see the wildcards and match files in subdirectories using them as it recurses.</p>
<dt><code>-R</code></p>
<dd>
<dt><code>&#8211;recurse-patterns</code></p>
<dd> Travel the directory structure recursively starting at the current directory; for example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -R foo &quot;*.c&quot;</dl>
</dl>
<dt>
<dd> In this case, all the files matching <code>*.c</code> in the tree starting at the current directory are stored into a <i>zip</i> archive named <code>foo.zip</code>. Note that <code>*.c</code> will match <code>file.c</code>, <code>a/file.c</code> and <code>a/b/.c</code>. More than one pattern can be listed as separate arguments. Note for PKZIP users: the equivalent command is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> pkzip -rP foo *.c</dl>
</dl>
<dt>
<dd> Patterns are relative file paths as they appear in the archive, or will after zipping, and can have optional wildcards in them. For example, given the current directory is <code>foo</code> and under it are directories <code>foo1</code> and <code>foo2</code> and in <code>foo1</code> is the file <code>bar.c</code>,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -R foo/*</dl>
</dl>
<dt>
<dd> will zip up <code>foo</code>, <code>foo/foo1</code>, <code>foo/foo1/bar.c</code>, and <code>foo/foo2</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -R */bar.c</dl>
</dl>
<dt>
<dd> will zip up <code>foo/foo1/bar.c</code>. See the note for <code>-r</code> on escaping wildcards. </p>
<dt><code>-RE</code></p>
<dd>
<dt><code>&#8211;regex</code></p>
<dd> [WIN32] Before <i>zip</i> <i>3.0</i>, regular expression list matching was enabled by default on Windows platforms. Because of confusion resulting from the need to escape &quot;[&quot; and &quot;]&quot; in names, it is now off by default for Windows so &quot;[&quot; and &quot;]&quot; are just normal characters in names. This option enables [] matching again. </p>
<dt><code>-s&nbsp;</code>splitsize</p>
<dd>
<dt><code>&#8211;split-size&nbsp;</code>splitsize</p>
<dd> Enable creating a split archive and set the split size. A split archive is an archive that could be split over many files. As the archive is created, if the size of the archive reaches the specified split size, that split is closed and the next split opened. In general all splits but the last will be the split size and the last will be whatever is left. If the entire archive is smaller than the split size a single-file archive is created. </p>
<p> Split archives are stored in numbered files. For example, if the output archive is named <code>archive</code> and three splits are required, the resulting archive will be in the three files <code>archive.z01</code>, <code>archive.z02</code>, and <code>archive.zip</code>. Do not change the numbering of these files or the archive will not be readable as these are used to determine the order the splits are read. </p>
<p> Split size is a number optionally followed by a multiplier. Currently the number must be an integer. The multiplier can currently be one of <code>k</code> (kilobytes), <code>m</code> (megabytes), <code>g</code> (gigabytes), or <code>t</code> (terabytes). As 64k is the minimum split size, numbers without multipliers default to megabytes. For example, to create a split archive called <code>foo</code> with the contents of the <code>bar</code> directory with splits of 670 MB that might be useful for burning on CDs, the command:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -s 670m -r foo bar</dl>
</dl>
<dt>
<dd> could be used. </p>
<p> Currently the old splits of a split archive are not excluded from a new archive, but they can be specifically excluded. If possible, keep the input and output archives out of the path being zipped when creating split archives. </p>
<p> Using <code>-s</code> without <code>-sp</code> as above creates all the splits where <code>foo</code> is being written, in this case the current directory. This split mode updates the splits as the archive is being created, requiring all splits to remain writable, but creates split archives that are readable by any unzip that supports split archives. See <code>-sp</code> below for enabling split pause mode which allows splits to be written directly to removable media. </p>
<p> The option <code>-sv</code> can be used to enable verbose splitting and provide details of how the splitting is being done. The <code>-sb</code> option can be used to ring the bell when <i>zip</i> pauses for the next split destination. </p>
<p> Split archives cannot be updated, but see the <code>-O</code> (<code>&#8211;out</code>) option for how a split archive can be updated as it is copied to a new archive. A split archive can also be converted into a single-file archive using a split size of 0 or negating the <code>-s</code> option:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -s 0 split.zip &#8211;out single.zip</dl>
</dl>
<dt>
<dd> Also see <code>-U</code> (<code>&#8211;copy</code>) for more on using copy mode.</p>
<dt><code>-sb</code></p>
<dd>
<dt><code>&#8211;split-bell</code></p>
<dd> If splitting and using split pause mode, ring the bell when <i>zip</i> pauses for each split destination.</p>
<dt><code>-sc</code></p>
<dd>
<dt><code>&#8211;show-command</code></p>
<dd> Show the command line starting <i>zip</i> as processed and exit. The new command parser permutes the arguments, putting all options and any values associated with them before any non-option arguments. This allows an option to appear anywhere in the command line as long as any values that go with the option go with it. This option displays the command line as <i>zip</i> sees it, including any arguments from the environment such as from the <code>ZIPOPT</code> variable. Where allowed, options later in the command line can override options earlier in the command line.</p>
<dt><code>-sf</code></p>
<dd>
<dt><code>&#8211;show-files</code></p>
<dd> Show the files that would be operated on, then exit. For instance, if creating a new archive, this will list the files that would be added. If the option is negated, <code>-sf-</code>, output only to an open log file. Screen display is not recommended for large lists.</p>
<dt><code>-so</code></p>
<dd>
<dt><code>&#8211;show-options</code></p>
<dd> Show all available options supported by <i>zip</i> as compiled on the current system. As this command reads the option table, it should include all options. Each line includes the short option (if defined), the long option (if defined), the format of any value that goes with the option, if the option can be negated, and a small description. The value format can be no value, required value, optional value, single character value, number value, or a list of values. The output of this option is not intended to show how to use any option but only show what options are available.</p>
<dt><code>-sp</code></p>
<dd>
<dt><code>&#8211;split-pause</code></p>
<dd> If splitting is enabled with <code>-s</code>, enable split pause mode. This creates split archives as <code>-s</code> does, but stream writing is used so each split can be closed as soon as it is written and <i>zip</i> will pause between each split to allow changing split destination or media. </p>
<p> Though this split mode allows writing splits directly to removable media, it uses stream archive format that may not be readable by some unzips. Before relying on splits created with <code>-sp</code>, test a split archive with the unzip you will be using. </p>
<p> To convert a stream split archive (created with <code>-sp</code>) to a standard archive see the <code>&#8211;out</code> option.</p>
<dt><code>-su</code></p>
<dd>
<dt><code>&#8211;show-unicode</code></p>
<dd> As <code>-sf</code>, but also show Unicode version of the path if exists.</p>
<dt><code>-sU</code></p>
<dd>
<dt><code>&#8211;show-just-unicode</code></p>
<dd> As <code>-sf</code>, but only show Unicode version of the path if exists, otherwise show the standard version of the path.</p>
<dt><code>-sv</code></p>
<dd>
<dt><code>&#8211;split-verbose</code></p>
<dd> Enable various verbose messages while splitting, showing how the splitting is being done.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;system-hidden</code></p>
<dd> [MSDOS, OS/2, WIN32 and ATARI] Include system and hidden files.</p>
<dl>
<dt>
<dd> [MacOS] Includes finder invisible files, which are ignored otherwise.</dl>
<dt><code>-t&nbsp;</code>mmddyyyy</p>
<dd>
<dt><code>&#8211;from-date&nbsp;</code>mmddyyyy</p>
<dd> Do not operate on files modified prior to the specified date, where <code>mm</code> is the month (00-12), <code>dd</code> is the day of the month (01-31), and <code>yyyy</code> is the year. The <i>ISO 8601</i> date format <code>yyyy-mm-dd</code> is also accepted. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -rt 12071991 infamy foo </p>
<p> zip -rt 1991-12-07 infamy foo</dl>
</dl>
<dt>
<dd> will add all the files in <code>foo</code> and its subdirectories that were last modified on or after 7 December 1991, to the <i>zip</i> archive <code>infamy.zip</code>.</p>
<dt><code>-tt&nbsp;</code>mmddyyyy</p>
<dd>
<dt><code>&#8211;before-date&nbsp;</code>mmddyyyy</p>
<dd> Do not operate on files modified after or at the specified date, where <code>mm</code> is the month (00-12), <code>dd</code> is the day of the month (01-31), and <code>yyyy</code> is the year. The <i>ISO 8601</i> date format <code>yyyy-mm-dd</code> is also accepted. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -rtt 11301995 infamy foo </p>
<p> zip -rtt 1995-11-30 infamy foo</dl>
</dl>
<dt>
<dd> will add all the files in <code>foo</code> and its subdirectories that were last modified before 30 November 1995, to the <i>zip</i> archive <code>infamy.zip</code>.</p>
<dt><code>-T</code></p>
<dd>
<dt><code>&#8211;test&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Test the integrity of the new zip file. If the check fails, the old zip file is unchanged and (with the <code>-m</code> option) no input files are removed.</p>
<dt><code>-TT&nbsp;</code>cmd</p>
<dd>
<dt><code>&#8211;unzip-command&nbsp;</code>cmd</p>
<dd> Use command cmd instead of &#8216;unzip -tqq&#8217; to test an archive when the <code>-T</code> option is used. On Unix, to use a copy of unzip in the current directory instead of the standard system unzip, could use:</p>
<dt>
<dd> zip archive file1 file2 -T -TT &quot;./unzip -tqq&quot;</p>
<dt>
<dd> In cmd, {} is replaced by the name of the temporary archive, otherwise the name of the archive is appended to the end of the command. The return code is checked for success (0 on Unix).</p>
<dt><code>-u</code></p>
<dd>
<dt><code>&#8211;update</code></p>
<dd> Replace (update) an existing entry in the <i>zip</i> archive only if it has been modified more recently than the version already in the <i>zip</i> archive. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -u stuff *</dl>
</dl>
<dt>
<dd> will add any new files in the current directory, and update any files which have been modified since the <i>zip</i> archive <i>stuff.zip</i> was last created/modified (note that <i>zip</i> will not try to pack <i>stuff.zip</i> into itself when you do this).</p>
<dt>
<dd> Note that the <code>-u</code> option with no input file arguments acts like the <code>-f</code> (freshen) option.</p>
<dt><code>-U</code></p>
<dd>
<dt><code>&#8211;copy-entries</code></p>
<dd> Copy entries from one archive to another. Requires the <code>&#8211;out</code> option to specify a different output file than the input archive. Copy mode is the reverse of <code>-d</code> delete. When delete is being used with <code>&#8211;out</code>, the selected entries are deleted from the archive and all other entries are copied to the new archive, while copy mode selects the files to include in the new archive. Unlike <code>-u</code> update, input patterns on the command line are matched against archive entries only and not the file system files. For instance,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip inarchive &quot;*.c&quot; &#8211;copy &#8211;out outarchive</dl>
</dl>
<dt>
<dd> copies entries with names ending in <code>.c</code> from <code>inarchive</code> to <code>outarchive</code>. The wildcard must be escaped on some systems to prevent the shell from substituting names of files from the file system which may have no relevance to the entries in the archive. </p>
<p> If no input files appear on the command line and <code>&#8211;out</code> is used, copy mode is assumed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip inarchive &#8211;out outarchive</dl>
</dl>
<dt>
<dd> This is useful for changing split size for instance. Encrypting and decrypting entries is not yet supported using copy mode. Use <i>zipcloak</i> for that.</p>
<dt><code>-UN&nbsp;</code>v</p>
<dd>
<dt><code>&#8211;unicode&nbsp;</code>v</p>
<dd> Determine what <i>zip</i> should do with Unicode file names. <i>zip 3.0</i>, in addition to the standard file path, now includes the UTF-8 translation of the path if the entry path is not entirely 7-bit ASCII. When an entry is missing the Unicode path, <i>zip</i> reverts back to the standard file path. The problem with using the standard path is this path is in the local character set of the zip that created the entry, which may contain characters that are not valid in the character set being used by the unzip. When <i>zip</i> is reading an archive, if an entry also has a Unicode path, <i>zip</i> now defaults to using the Unicode path to recreate the standard path using the current local character set. </p>
<p> This option can be used to determine what <i>zip</i> should do with this path if there is a mismatch between the stored standard path and the stored UTF-8 path (which can happen if the standard path was updated). In all cases, if there is a mismatch it is assumed that the standard path is more current and <i>zip</i> uses that. Values for <code>v</code> are</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> q &#8211; quit if paths do not match</p>
<dt>
<dd> w &#8211; warn, continue with standard path</p>
<dt>
<dd> i &#8211; ignore, continue with standard path</p>
<dt>
<dd> n &#8211; no Unicode, do not use Unicode paths</dl>
</dl>
<dt>
<dd> The default is to warn and continue. </p>
<p> Characters that are not valid in the current character set are escaped as <code>#Uxxxx</code> and <code>#Lxxxxxx</code>, where x is an ASCII character for a hex digit. The first is used if a 16-bit character number is sufficient to represent the Unicode character and the second if the character needs more than 16 bits to represent it&#8217;s Unicode character code. Setting <code>-UN</code> to</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> e &#8211; escape</dl>
</dl>
<dt>
<dd> as in</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip archive -sU -UN=e</dl>
</dl>
<dt>
<dd> forces <i>zip</i> to escape all characters that are not printable 7-bit ASCII. </p>
<p> Normally <i>zip</i> stores UTF-8 directly in the standard path field on systems where UTF-8 is the current character set and stores the UTF-8 in the new extra fields otherwise. The option</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> u &#8211; UTF-8</dl>
</dl>
<dt>
<dd> as in</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip archive dir -r -UN=UTF8</dl>
</dl>
<dt>
<dd> forces <i>zip</i> to store UTF-8 as native in the archive. Note that storing UTF-8 directly is the default on Unix systems that support it. This option could be useful on Windows systems where the escaped path is too large to be a valid path and the UTF-8 version of the path is smaller, but native UTF-8 is not backward compatible on Windows systems. </p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Verbose mode or print diagnostic version info.</p>
<dt>
<dd> Normally, when applied to real operations, this option enables the display of a progress indicator during compression (see <code>-dd</code> for more on dots) and requests verbose diagnostic info about zipfile structure oddities.</p>
<dt>
<dd> However, when <code>-v</code> is the only command line argument a diagnostic screen is printed instead. This should now work even if stdout is redirected to a file, allowing easy saving of the information for sending with bug reports to Info-ZIP. The version screen provides the help screen header with program name, version, and release date, some pointers to the Info-ZIP home and distribution sites, and shows information about the target environment (compiler type and version, OS version, compilation date and the enabled optional features used to create the <i>zip</i> executable).</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;VMS-portable</code></p>
<dd> [VMS] Save VMS file attributes. (Files are truncated at EOF.) When a -V archive is unpacked on a non-VMS system, some file types (notably Stream_LF text files and pure binary files like fixed-512) should be extracted intact. Indexed files and file types with embedded record sizes (notably variable-length record types) will probably be seen as corrupt elsewhere.</p>
<dt><code>-VV</code></p>
<dd>
<dt><code>&#8211;VMS-specific</code></p>
<dd> [VMS] Save VMS file attributes, and all allocated blocks in a file, including any data beyond EOF. Useful for moving ill-formed files among VMS systems. When a -VV archive is unpacked on a non-VMS system, almost all files will appear corrupt.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;VMS-versions</code></p>
<dd> [VMS] Append the version number of the files to the name, including multiple versions of files. Default is to use only the most recent version of a specified file.</p>
<dt><code>-ww</code></p>
<dd>
<dt><code>&#8211;VMS-dot-versions</code></p>
<dd> [VMS] Append the version number of the files to the name, including multiple versions of files, using the .nnn format. Default is to use only the most recent version of a specified file.</p>
<dt><code>-ws</code></p>
<dd>
<dt><code>&#8211;wild-stop-dirs</code></p>
<dd> Wildcards match only at a directory level. Normally <i>zip</i> handles paths as strings and given the paths</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> /foo/bar/dir/file1.c</p>
<dt>
<dd> /foo/bar/file2.c</dl>
</dl>
<dt>
<dd> an input pattern such as</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> /foo/bar/*</dl>
</dl>
<dt>
<dd> normally would match both paths, the * matching <code>dir/file1.c</code> and <code>file2.c</code>. Note that in the first case a directory boundary (/) was crossed in the match. With <code>-ws</code> no directory bounds will be included in the match, making wildcards local to a specific directory level. So, with <code>-ws</code> enabled, only the second path would be matched. </p>
<p> When using <code>-ws</code>, use ** to match across directory boundaries as * does normally.</p>
<dt><code>-x&nbsp;</code>files</p>
<dd>
<dt><code>&#8211;exclude&nbsp;</code>files</p>
<dd> Explicitly exclude the specified files, as in:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo foo -x \*.o</dl>
</dl>
<dt>
<dd> which will include the contents of <code>foo</code> in <code>foo.zip</code> while excluding all the files that end in <code>.o</code>. The backslash avoids the shell filename substitution, so that the name matching is performed by <i>zip</i> at all directory levels.</p>
<dt>
<dd> Also possible:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo foo -x [at] exclude.lst</dl>
</dl>
<dt>
<dd> which will include the contents of <code>foo</code> in <code>foo.zip</code> while excluding all the files that match the patterns in the file <code>exclude.lst</code>.</p>
<dt>
<dd> The long option forms of the above are</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo foo &#8211;exclude \*.o</dl>
</dl>
<dt>
<dd> and</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo foo &#8211;exclude @exclude.lst</dl>
</dl>
<dt>
<dd> Multiple patterns can be specified, as in:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo foo -x \*.o \*.c</dl>
</dl>
<dt>
<dd> If there is no space between <code>-x</code> and the pattern, just one value is assumed (no list):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -r foo foo -x\*.o</dl>
</dl>
<dt>
<dd>
<dt>
<dd> See <code>-i</code> for more on include and exclude.</p>
<dt><code>-X</code></p>
<dd>
<dt><code>&#8211;no-extra</code></p>
<dd> Do not save extra file attributes (Extended Attributes on OS/2, uid/gid and file times on Unix). The zip format uses extra fields to include additional information for each entry. Some extra fields are specific to particular systems while others are applicable to all systems. Normally when <i>zip</i> reads entries from an existing archive, it reads the extra fields it knows, strips the rest, and adds the extra fields applicable to that system. With <code>-X</code>, <i>zip</i> strips all old fields and only includes the Unicode and Zip64 extra fields (currently these two extra fields cannot be disabled). </p>
<p> Negating this option, <code>-X-</code>, includes all the default extra fields, but also copies over any unrecognized extra fields.</p>
<dt><code>-y</code></p>
<dd>
<dt><code>&#8211;symlinks</code></p>
<dd> For UNIX and VMS (V8.3 and later), store symbolic links as such in the <i>zip</i> archive, instead of compressing and storing the file referred to by the link. This can avoid multiple copies of files being included in the archive as <i>zip</i> recurses the directory trees and accesses files directly and by links.</p>
<dt><code>-z</code></p>
<dd>
<dt><code>&#8211;archive-comment</code></p>
<dd> Prompt for a multi-line comment for the entire <i>zip</i> archive. The comment is ended by a line containing just a period, or an end of file condition (^D on Unix, ^Z on MSDOS, OS/2, and VMS). The comment can be taken from a file:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -z foo &lt; foowhat</dl>
</dl>
<dt><code>-Z&nbsp;</code>cm</p>
<dd>
<dt><code>&#8211;compression-method&nbsp;</code>cm</p>
<dd> Set the default compression method. Currently the main methods supported by <i>zip</i> are <code>store</code> and <code>deflate</code>. Compression method can be set to: </p>
<p> <code>store</code> &#8211; Setting the compression method to <code>store</code> forces <i>zip</i> to store entries with no compression. This is generally faster than compressing entries, but results in no space savings. This is the same as using <code>-0</code> (compression level zero). </p>
<p> <code>deflate</code> &#8211; This is the default method for <i>zip</i>. If <i>zip</i> determines that storing is better than deflation, the entry will be stored instead. </p>
<p> <code>bzip2</code> &#8211; If <code>bzip2</code> support is compiled in, this compression method also becomes available. Only some modern unzips currently support the <code>bzip2</code> compression method, so test the unzip you will be using before relying on archives using this method (compression method 12). </p>
<p> For example, to add <code>bar.c</code> to archive <code>foo</code> using <code>bzip2</code> compression:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -Z bzip2 foo bar.c</dl>
</dl>
<dt>
<dd> The compression method can be abbreviated:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -Zb foo bar.c</dl>
</dl>
<dt>
<dd>
<dt><code>-#</code></p>
<dd>
<dt><code>(-0, -1, -2, -3, -4, -5, -6, -7, -8, -9)</code></p>
<dd> Regulate the speed of compression using the specified digit <code>#</code>, where <code>-0</code> indicates no compression (store all files), <code>-1</code> indicates the fastest compression speed (less compression) and <code>-9</code> indicates the slowest compression speed (optimal compression, ignores the suffix list). The default compression level is <code>-6.</code> </p>
<p> Though still being worked, the intention is this setting will control compression speed for all compression methods. Currently only deflation is controlled.</p>
<dt><code>-!</code></p>
<dd>
<dt><code>&#8211;use-privileges</code></p>
<dd> [WIN32] Use privileges (if granted) to obtain all aspects of WinNT security.</p>
<dt><code>-@</code></p>
<dd>
<dt><code>&#8211;names-stdin</code></p>
<dd> Take the list of input files from standard input. Only one filename per line.</p>
<dt><code>-$</code></p>
<dd>
<dt><code>&#8211;volume-label</code></p>
<dd> [MSDOS, OS/2, WIN32] Include the volume label for the drive holding the first file to be compressed. If you want to include only the volume label or to force a specific drive, use the drive name as first file name, as in:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip -$ foo a: c:bar</dl>
</dl>
<dt>
<dd></dl>
<h2>EXAMPLES</h2>
<p> The simplest example:</p>
<dl>
<dt>
<dd> zip stuff *</dl>
<p> creates the archive <i>stuff.zip</i> (assuming it does not exist) and puts all the files in the current directory in it, in compressed form (the <code>.zip</code> suffix is added automatically, unless the archive name contains a dot already; this allows the explicit specification of other suffixes). </p>
<p> Because of the way the shell on Unix does filename substitution, files starting with &quot;.&quot; are not included; to include these as well:</p>
<dl>
<dt>
<dd> zip stuff .* *</dl>
<p> Even this will not include any subdirectories from the current directory. </p>
<p> To zip up an entire directory, the command:</p>
<dl>
<dt>
<dd> zip -r foo foo</dl>
<p> creates the archive <i>foo.zip</i>, containing all the files and directories in the directory <i>foo</i> that is contained within the current directory. </p>
<p> You may want to make a <i>zip</i> archive that contains the files in <i>foo</i>, without recording the directory name, <i>foo</i>. You can use the <code>-j</code> option to leave off the paths, as in:</p>
<dl>
<dt>
<dd> zip -j foo foo/*</dl>
<p> If you are short on disk space, you might not have enough room to hold both the original directory and the corresponding compressed <i>zip</i> archive. In this case, you can create the archive in steps using the <code>-m</code> option. If <i>foo</i> contains the subdirectories <i>tom</i>, <i>dick</i>, and <i>harry</i>, you can:</p>
<dl>
<dt>
<dd> zip -rm foo foo/tom<br />
 zip -rm foo foo/dick<br />
 zip -rm foo foo/harry</dl>
<p> where the first command creates <i>foo.zip</i>, and the next two add to it. At the completion of each <i>zip</i> command, the last created archive is deleted, making room for the next <i>zip</i> command to function. </p>
<p> Use <code>-s</code> to set the split size and create a split archive. The size is given as a number followed optionally by one of k (kB), m (MB), g (GB), or t (TB). The command</p>
<dl>
<dt>
<dd> zip -s 2g -r split.zip foo</dl>
<p> creates a split archive of the directory foo with splits no bigger than 2 GB each. If foo contained 5 GB of contents and the contents were stored in the split archive without compression (to make this example simple), this would create three splits, split.z01 at 2 GB, split.z02 at 2 GB, and split.zip at a little over 1 GB. </p>
<p> The <code>-sp</code> option can be used to pause <i>zip</i> between splits to allow changing removable media, for example, but read the descriptions and warnings for both <code>-s</code> and <code>-sp</code> below. </p>
<p> Though <i>zip</i> does not update split archives, <i>zip</i> provides the new option <code>-O</code> (<code>&#8211;output-file</code>) to allow split archives to be updated and saved in a new archive. For example,</p>
<dl>
<dt>
<dd> zip inarchive.zip foo.c bar.c &#8211;out outarchive.zip</dl>
<p> reads archive <code>inarchive.zip</code>, even if split, adds the files <code>foo.c</code> and <code>bar.c</code>, and writes the resulting archive to <code>outarchive.zip</code>. If <code>inarchive.zip</code> is split then <code>outarchive.zip</code> defaults to the same split size. Be aware that <code>outarchive.zip</code> and any split files that are created with it are always overwritten without warning. This may be changed in the future. </p>
<h2>PATTERN MATCHING</h2>
<p> This section applies only to Unix. Watch this space for details on MSDOS and VMS operation. However, the special wildcard characters <code>*</code> and <code>[]</code> below apply to at least MSDOS also. </p>
<p> The Unix shells (<i>sh</i>, <i>csh</i>, <i>bash</i>, and others) normally do filename substitution (also called &quot;globbing&quot;) on command arguments. Generally the special characters are:</p>
<dl>
<dt><code>?</code></p>
<dd> match any single character</p>
<dt><code>*</code></p>
<dd> match any number of characters (including none)</p>
<dt><code>[]</code></p>
<dd> match any character in the range indicated within the brackets (example: [a-f], [0-9]). This form of wildcard matching allows a user to specify a list of characters between square brackets and if any of the characters match the expression matches. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip archive &quot;*.[hc]&quot;</dl>
</dl>
<dt>
<dd> would archive all files in the current directory that end in <code>.h</code> or <code>.c</code>. </p>
<p> Ranges of characters are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip archive &quot;[a-f]*&quot;</dl>
</dl>
<dt>
<dd> would add to the archive all files starting with &quot;a&quot; through &quot;f&quot;. </p>
<p> Negation is also supported, where any character in that position not in the list matches. Negation is supported by adding <code>!</code> or <code>^</code> to the beginning of the list:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> zip archive &quot;*.[!o]&quot;</dl>
</dl>
<dt>
<dd> matches files that don&#8217;t end in &quot;.o&quot;. </p>
<p> On WIN32, [] matching needs to be turned on with the -RE option to avoid the confusion that names with [ or ] have caused. </p>
</dl>
<p> When these characters are encountered (without being escaped with a backslash or quotes), the shell will look for files relative to the current path that match the pattern, and replace the argument with a list of the names that matched. </p>
<p> The <i>zip</i> program can do the same matching on names that are in the <i>zip</i> archive being modified or, in the case of the <code>-x</code> (exclude) or <code>-i</code> (include) options, on the list of files to be operated on, by using backslashes or quotes to tell the shell not to do the name expansion. In general, when <i>zip</i> encounters a name in the list of files to do, it first looks for the name in the file system. If it finds it, it then adds it to the list of files to do. If it does not find it, it looks for the name in the <i>zip</i> archive being modified (if it exists), using the pattern matching characters described above, if present. For each match, it will add that name to the list of files to be processed, unless this name matches one given with the <code>-x</code> option, or does not match any name given with the <code>-i</code> option. </p>
<p> The pattern matching includes the path, and so patterns like \*.o match names that end in &quot;.o&quot;, no matter what the path prefix is. Note that the backslash must precede every special character (i.e. ?*[]), or the entire argument must be enclosed in double quotes (&quot;&quot;). </p>
<p> In general, use backslashes or double quotes for paths that have wildcards to make <i>zip</i> do the pattern matching for file paths, and always for paths and strings that have spaces or wildcards for <code>-i</code>, <code>-x</code>, <code>-R</code>, <code>-d</code>, and <code>-U</code> and anywhere <i>zip</i> needs to process the wildcards.</p>
<h2>ENVIRONMENT</h2>
<p> The following environment variables are read and used by <i>zip</i> as described.</p>
<dl>
<dt><code>ZIPOPT&nbsp;<wbr>&nbsp;</code></p>
<dd> contains default options that will be used when running <i>zip</i>. The contents of this environment variable will get added to the command line just after the <code>zip</code> command.</p>
<dt><code>ZIP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> [Not on RISC OS and VMS] see ZIPOPT</p>
<dt><code>Zip$Options</code></p>
<dd> [RISC OS] see ZIPOPT</p>
<dt><code>Zip$Exts</code></p>
<dd> [RISC OS] contains extensions separated by a : that will cause native filenames with one of the specified extensions to be added to the zip file with basename and extension swapped.</p>
<dt><code>ZIP_OPTS</code></p>
<dd> [VMS] see ZIPOPT</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-compress/">compress</a>(1), <a href="/docs/linux/man/1-shar/">shar</a>(1), <a href="/docs/linux/man/1-tar/">tar</a>(1), <a href="/docs/linux/man/1-unzip/">unzip</a>(1), <a href="/docs/linux/man/1-gzip/">gzip</a>(1)</p>
<h2>DIAGNOSTICS</h2>
<p> The exit status (or error level) approximates the exit codes defined by PKWARE and takes on the following values, except under VMS:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> normal; no errors or warnings detected.</p>
<dt>2</p>
<dd> unexpected end of zip file.</p>
<dt>3</p>
<dd> a generic error in the zipfile format was detected. Processing may have completed successfully anyway; some broken zipfiles created by other archivers have simple work-arounds.</p>
<dt>4</p>
<dd> <i>zip</i> was unable to allocate memory for one or more buffers during program initialization.</p>
<dt>5</p>
<dd> a severe error in the zipfile format was detected. Processing probably failed immediately.</p>
<dt>6</p>
<dd> entry too large to be processed (such as input files larger than 2 GB when not using Zip64 or trying to read an existing archive that is too large) or entry too large to be split with <i>zipsplit</i></p>
<dt>7</p>
<dd> invalid comment format</p>
<dt>8</p>
<dd> <i>zip</i> -T failed or out of memory</p>
<dt>9</p>
<dd> the user aborted <i>zip</i> prematurely with control-C (or similar)</p>
<dt>10</p>
<dd> <i>zip</i> encountered an error while using a temp file</p>
<dt>11</p>
<dd> read or seek error</p>
<dt>12</p>
<dd> <i>zip</i> has nothing to do</p>
<dt>13</p>
<dd> missing or empty zip file</p>
<dt>14</p>
<dd> error writing to a file</p>
<dt>15</p>
<dd> <i>zip</i> was unable to create a file to write to</p>
<dt>16</p>
<dd> bad command line parameters</p>
<dt>18</p>
<dd> <i>zip</i> could not open a specified file to read</p>
<dt>19</p>
<dd> <i>zip</i> was compiled with options not supported on this system</dl>
</dl>
<p> VMS interprets standard Unix (or PC) return values as other, scarier-looking things, so <i>zip</i> instead maps them into VMS-style status codes. In general, <i>zip</i> sets VMS Facility = 1955 (0x07A3), Code = 2* Unix_status, and an appropriate Severity (as specified in ziperr.h). More details are included in the VMS-specific documentation. See [.vms]NOTES.TXT and [.vms]vms_msg_gen.c.</p>
<h2>BUGS</h2>
<p> <i>zip</i> 3.0 is not compatible with PKUNZIP 1.10. Use <i>zip</i> 1.1 to produce <i>zip</i> files which can be extracted by PKUNZIP 1.10. </p>
<p> <i>zip</i> files produced by <i>zip</i> 3.0 must not be <i>updated</i> by <i>zip</i> 1.1 or PKZIP 1.10, if they contain encrypted members or if they have been produced in a pipe or on a non-seekable device. The old versions of <i>zip</i> or PKZIP would create an archive with an incorrect format. The old versions can list the contents of the zip file but cannot extract it anyway (because of the new compression algorithm). If you do not use encryption and use regular disk files, you do not have to care about this problem. </p>
<p> Under VMS, not all of the odd file formats are treated properly. Only stream-LF format <i>zip</i> files are expected to work with <i>zip</i>. Others can be converted using Rahul Dhesi&#8217;s BILF program. This version of <i>zip</i> handles some of the conversion internally. When using Kermit to transfer zip files from VMS to MSDOS, type &quot;set file type block&quot; on VMS. When transferring from MSDOS to VMS, type &quot;set file type fixed&quot; on VMS. In both cases, type &quot;set file type binary&quot; on MSDOS. </p>
<p> Under some older VMS versions, <i>zip</i> may hang for file specifications that use DECnet syntax <i>foo::*.*.</i> </p>
<p> On OS/2, zip cannot match some names, such as those including an exclamation mark or a hash sign. This is a bug in OS/2 itself: the 32-bit DosFindFirst/Next don&#8217;t find such names. Other programs such as GNU tar are also affected by this bug. </p>
<p> Under OS/2, the amount of Extended Attributes displayed by DIR is (for compatibility) the amount returned by the 16-bit version of DosQueryPathInfo(). Otherwise OS/2 1.3 and 2.0 would report different EA sizes when DIRing a file. However, the structure layout returned by the 32-bit DosQueryPathInfo() is a bit different, it uses extra padding bytes and link pointers (it&#8217;s a linked list) to have all fields on 4-byte boundaries for portability to future RISC OS/2 versions. Therefore the value reported by <i>zip</i> (which uses this 32-bit-mode size) differs from that reported by DIR. <i>zip</i> stores the 32-bit format for portability, even the 16-bit MS-C-compiled version running on OS/2 1.3, so even this one shows the 32-bit-mode size.</p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1997-2008 Info-ZIP. </p>
<p> Currently distributed under the Info-ZIP license. </p>
<p> Copyright (C) 1990-1997 Mark Adler, Richard B. Wales, Jean-loup Gailly, Onno van der Linden, Kai Uwe Rommel, Igor Mandrichenko, John Bush and Paul Kienitz. </p>
<p> Original copyright: </p>
<p> Permission is granted to any individual or institution to use, copy, or redistribute this software so long as all of the original files are included, that it is not sold for profit, and that this copyright notice is retained. </p>
<p> LIKE ANYTHING ELSE THAT&#8217;S FREE, ZIP AND ITS ASSOCIATED UTILITIES ARE PROVIDED AS IS AND COME WITH NO WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED. IN NO EVENT WILL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DAMAGES RESULTING FROM THE USE OF THIS SOFTWARE. </p>
<p> Please send bug reports and comments using the web page at: <i><a rel="nofollow" href="http://www.info-zip.org">www.info-zip.org</a></i>. For bug reports, please include the version of <i>zip</i> (see <i>zip -h</i>), the make options used to compile it (see <i>zip -v</i>), the machine and operating system in use, and as much additional information as possible.</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Thanks to R. P. Byrne for his <i>Shrink.Pas</i> program, which inspired this project, and from which the shrink algorithm was stolen; to Phil Katz for placing in the public domain the <i>zip</i> file format, compression format, and .ZIP filename extension, and for accepting minor changes to the file format; to Steve Burg for clarifications on the deflate format; to Haruhiko Okumura and Leonid Broukhis for providing some useful ideas for the compression algorithm; to Keith Petersen, Rich Wales, Hunter Goatley and Mark Adler for providing a mailing list and <i>ftp</i> site for the Info-ZIP group to use; and most importantly, to the Info-ZIP group itself (listed in the file <i>infozip.who</i>) without whose tireless testing and bug-fixing efforts a portable <i>zip</i> would not have been possible. Finally we should thank (blame) the first Info-ZIP moderator, David Kirschbaum, for getting us into this mess in the first place. The manual page was rewritten for Unix by R. P. C. Rodgers and updated by E. Gordon for <i>zip</i> 3.0. </p>
<h2>Index</h2>
