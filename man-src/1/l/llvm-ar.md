---
title: "llvm-ar(1)"
name: "llvm-ar"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-ar/"
description: "llvm-ar – LLVM archiver"
---

<h2 class="name">NAME</h2>
<p> llvm-ar &#8211; LLVM archiver </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-ar</code> [-]{dmpqrtx}[Rabfikouz] [relpos] [count] &lt;archive&gt; [files&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-ar</code> command is similar to the common Unix utility, <tt>&quot;ar&quot;</tt>. It archives several files together into a single file. The intent for this is to produce archive libraries by <font SIZE="-1">LLVM</font> bitcode that can be linked into an <font SIZE="-1">LLVM</font> program. However, the archive can contain any kind of file. By default, <code>llvm-ar</code> generates a symbol table that makes linking faster because only the symbol table needs to be consulted, not each individual file member of the archive. </p>
<p> The <code>llvm-ar</code> command can be used to <i>read</i> both <font SIZE="-1">SVR4</font> and <font SIZE="-1">BSD</font> style archive files. However, it cannot be used to write them. While the <code>llvm-ar</code> command produces files that are <i>almost</i> identical to the format used by other <tt>&quot;ar&quot;</tt> implementations, it has two significant departures in order to make the archive appropriate for <font SIZE="-1">LLVM</font>. The first departure is that <code>llvm-ar</code> only uses <font SIZE="-1">BSD4</font>.4 style long path names (stored immediately after the header) and never contains a string table for long names. The second departure is that the symbol table is formated for efficient construction of an in-memory data structure that permits rapid (red-black tree) lookups. Consequently, archives produced with <code>llvm-ar</code> usually won&#8217;t be readable or editable with any <tt>&quot;ar&quot;</tt> implementation or useful for linking. Using the <tt>&quot;f&quot;</tt> modifier to flatten file names will make the archive readable by other <tt>&quot;ar&quot;</tt> implementations but not for linking because the symbol table format for <font SIZE="-1">LLVM</font> is unique. If an <font SIZE="-1">SVR4</font> or <font SIZE="-1">BSD</font> style archive is used with the <tt>&quot;r&quot;</tt> (replace) or <tt>&quot;q&quot;</tt> (quick update) operations, the archive will be reconstructed in <font SIZE="-1">LLVM</font> format. This means that the string table will be dropped (in deference to <font SIZE="-1">BSD</font> 4.4 long names) and an <font SIZE="-1">LLVM</font> symbol table will be added (by default). The system symbol table will be retained. </p>
<p> Here&#8217;s where <code>llvm-ar</code> departs from previous <tt>&quot;ar&quot;</tt> implementations:</p>
<dl>
<dt><i>Symbol Table</i></p>
<dd> Since <code>llvm-ar</code> is intended to archive bitcode files, the symbol table won&#8217;t make much sense to anything but <font SIZE="-1">LLVM</font>. Consequently, the symbol table&#8217;s format has been simplified. It consists simply of a sequence of pairs of a file member index number as an <font SIZE="-1">LSB</font> 4byte integer and a null-terminated string.</p>
<dt><i>Long Paths</i></p>
<dd> Some <tt>&quot;ar&quot;</tt> implementations (<font SIZE="-1">SVR4</font>) use a separate file member to record long path names (&gt; 15 characters). <code>llvm-ar</code> takes the <font SIZE="-1">BSD</font> 4.4 and Mac <font SIZE="-1">OS</font> X approach which is to simply store the full path name immediately preceding the data for the file. The path name is null terminated and may contain the slash (/) character.</p>
<dt><i>Compression</i></p>
<dd> <code>llvm-ar</code> can compress the members of an archive to save space. The compression used depends on what&#8217;s available on the platform and what choices the <font SIZE="-1">LLVM</font> Compressor utility makes. It generally favors bzip2 but will select between &#8220;no compression&#8221; or bzip2 depending on what makes sense for the file&#8217;s content.</p>
<dt><i>Directory Recursion</i></p>
<dd> Most <tt>&quot;ar&quot;</tt> implementations do not recurse through directories but simply ignore directories if they are presented to the program in the <i>files</i> option. <code>llvm-ar</code>, however, can recurse through directory structures and add all the files under a directory, if requested.</p>
<dt><i></i><font SIZE="-1"><i>TOC</i></font><i> Verbose Output</i></p>
<dd> When <code>llvm-ar</code> prints out the verbose table of contents (<tt>&quot;tv&quot;</tt> option), it precedes the usual output with a character indicating the basic kind of content in the file. A blank means the file is a regular file. A &#8216;Z&#8217; means the file is compressed. A &#8216;B&#8217; means the file is an <font SIZE="-1">LLVM</font> bitcode file. An &#8216;S&#8217; means the file is the symbol table.</dl>
<h2>OPTIONS</h2>
<p> The options to <code>llvm-ar</code> are compatible with other <tt>&quot;ar&quot;</tt> implementations. However, there are a few modifiers (<i>zR</i>) that are not found in other <tt>&quot;ar&quot;</tt>s. The options to <code>llvm-ar</code> specify a single basic operation to perform on the archive, a variety of modifiers for that operation, the name of the archive file, and an optional list of file names. These options are used to determine how <code>llvm-ar</code> should process the archive file. </p>
<p> The Operations and Modifiers are explained in the sections below. The minimal set of options is at least one operator and the name of the archive. Typically archive files end with a <tt>&quot;.a&quot;</tt> suffix, but this is not required. Following the <i>archive-name</i> comes a list of <i>files</i> that indicate the specific members of the archive to operate on. If the <i>files</i> option is not specified, it generally means either &#8220;none&#8221; or &#8220;all&#8221; members, depending on the operation.</p>
<h2>Operations</h2>
<dl>
<dt>d</p>
<dd> Delete files from the archive. No modifiers are applicable to this operation. The <i>files</i> options specify which members should be removed from the archive. It is not an error if a specified file does not appear in the archive. If no <i>files</i> are specified, the archive is not modified.</p>
<dt>m[abi]</p>
<dd> Move files from one location in the archive to another. The <i>a</i>, <i>b</i>, and <i>i</i> modifiers apply to this operation. The <i>files</i> will all be moved to the location given by the modifiers. If no modifiers are used, the files will be moved to the end of the archive. If no <i>files</i> are specified, the archive is not modified.</p>
<dt>p[k]</p>
<dd> Print files to the standard output. The <i>k</i> modifier applies to this operation. This operation simply prints the <i>files</i> indicated to the standard output. If no <i>files</i> are specified, the entire archive is printed. Printing bitcode files is ill-advised as they might confuse your terminal settings. The <i>p</i> operation never modifies the archive.</p>
<dt>q[Rfz]</p>
<dd> Quickly append files to the end of the archive. The <i>R</i>, <i>f</i>, and <i>z</i> modifiers apply to this operation. This operation quickly adds the <i>files</i> to the archive without checking for duplicates that should be removed first. If no <i>files</i> are specified, the archive is not modified. Because of the way that <code>llvm-ar</code> constructs the archive file, its dubious whether the <i>q</i> operation is any faster than the <i>r</i> operation.</p>
<dt>r[Rabfuz]</p>
<dd> Replace or insert file members. The <i>R</i>, <i>a</i>, <i>b</i>, <i>f</i>, <i>u</i>, and <i>z</i> modifiers apply to this operation. This operation will replace existing <i>files</i> or insert them at the end of the archive if they do not exist. If no <i>files</i> are specified, the archive is not modified.</p>
<dt>t[v]</p>
<dd> Print the table of contents. Without any modifiers, this operation just prints the names of the members to the standard output. With the <i>v</i> modifier, <code>llvm-ar</code> also prints out the file type (B=bitcode, Z=compressed, S=symbol table, blank=regular file), the permission mode, the owner and group, the size, and the date. If any <i>files</i> are specified, the listing is only for those files. If no <i>files</i> are specified, the table of contents for the whole archive is printed.</p>
<dt>x[oP]</p>
<dd> Extract archive members back to files. The <i>o</i> modifier applies to this operation. This operation retrieves the indicated <i>files</i> from the archive and writes them back to the operating system&#8217;s file system. If no <i>files</i> are specified, the entire archive is extract.</dl>
<h2>Modifiers (operation specific)</h2>
<p> The modifiers below are specific to certain operations. See the Operations section (above) to determine which modifiers are applicable to which operations.</p>
<dl>
<dt>[a]</p>
<dd> When inserting or moving member files, this option specifies the destination of the new files as being <tt>&quot;a&quot;</tt>fter the <i>relpos</i> member. If <i>relpos</i> is not found, the files are placed at the end of the archive.</p>
<dt>[b]</p>
<dd> When inserting or moving member files, this option specifies the destination of the new files as being <tt>&quot;b&quot;</tt>efore the <i>relpos</i> member. If <i>relpos</i> is not found, the files are placed at the end of the archive. This modifier is identical to the the <i>i</i> modifier.</p>
<dt>[f]</p>
<dd> Normally, <code>llvm-ar</code> stores the full path name to a file as presented to it on the command line. With this option, truncated (15 characters max) names are used. This ensures name compatibility with older versions of <tt>&quot;ar&quot;</tt> but may also thwart correct extraction of the files (duplicates may overwrite). If used with the <i>R</i> option, the directory recursion will be performed but the file names will all be <tt>&quot;f&quot;</tt>lattened to simple file names.</p>
<dt>[i]</p>
<dd> A synonym for the <i>b</i> option.</p>
<dt>[k]</p>
<dd> Normally, <code>llvm-ar</code> will not print the contents of bitcode files when the <i>p</i> operation is used. This modifier defeats the default and allows the bitcode members to be printed.</p>
<dt>[N]</p>
<dd> This option is ignored by <code>llvm-ar</code> but provided for compatibility.</p>
<dt>[o]</p>
<dd> When extracting files, this option will cause <code>llvm-ar</code> to preserve the original modification times of the files it writes.</p>
<dt>[P]</p>
<dd> use full path names when matching</p>
<dt>[R]</p>
<dd> This modifier instructions the <i>r</i> option to recursively process directories. Without <i>R</i>, directories are ignored and only those <i>files</i> that refer to files will be added to the archive. When <i>R</i> is used, any directories specified with <i>files</i> will be scanned (recursively) to find files to be added to the archive. Any file whose name begins with a dot will not be added.</p>
<dt>[u]</p>
<dd> When replacing existing files in the archive, only replace those files that have a time stamp than the time stamp of the member in the archive.</p>
<dt>[z]</p>
<dd> When inserting or replacing any file in the archive, compress the file first. This modifier is safe to use when (previously) compressed bitcode files are added to the archive; the compressed bitcode files will not be doubly compressed.</dl>
<h2>Modifiers (generic)</h2>
<p> The modifiers below may be applied to any operation.</p>
<dl>
<dt>[c]</p>
<dd> For all operations, <code>llvm-ar</code> will always create the archive if it doesn&#8217;t exist. Normally, <code>llvm-ar</code> will print a warning message indicating that the archive is being created. Using this modifier turns off that warning.</p>
<dt>[s]</p>
<dd> This modifier requests that an archive index (or symbol table) be added to the archive. This is the default mode of operation. The symbol table will contain all the externally visible functions and global variables defined by all the bitcode files in the archive. Using this modifier is more efficient that using llvm-ranlib which also creates the symbol table.</p>
<dt>[S]</p>
<dd> This modifier is the opposite of the <i>s</i> modifier. It instructs <code>llvm-ar</code> to not build the symbol table. If both <i>s</i> and <i>S</i> are used, the last modifier to occur in the options will prevail.</p>
<dt>[v]</p>
<dd> This modifier instructs <code>llvm-ar</code> to be verbose about what it is doing. Each editing operation taken against the archive will produce a line of output saying what is being done.</dl>
<h2>STANDARDS</h2>
<p> The <code>llvm-ar</code> utility is intended to provide a superset of the <font SIZE="-1">IEEE</font> Std 1003.2 (<font SIZE="-1">POSIX</font>.2) functionality for <tt>&quot;ar&quot;</tt>. <code>llvm-ar</code> can read both <font SIZE="-1">SVR4</font> and <font SIZE="-1">BSD4</font>.4 (or Mac <font SIZE="-1">OS</font> X) archives. If the <tt>&quot;f&quot;</tt> modifier is given to the <tt>&quot;x&quot;</tt> or <tt>&quot;r&quot;</tt> operations then <code>llvm-ar</code> will write <font SIZE="-1">SVR4</font> compatible archives. Without this modifier, <code>llvm-ar</code> will write <font SIZE="-1">BSD4</font>.4 compatible archives that have long names immediately after the header and indicated using the &#8220;#1/ddd&#8221; notation for the name in the header.</p>
<h2>FILE FORMAT</h2>
<p> The file format for <font SIZE="-1">LLVM</font> Archive files is similar to that of <font SIZE="-1">BSD</font> 4.4 or Mac <font SIZE="-1">OSX</font> archive files. In fact, except for the symbol table, the <tt>&quot;ar&quot;</tt> commands on those operating systems should be able to read <font SIZE="-1">LLVM</font> archive files. The details of the file format follow. </p>
<p> Each archive begins with the archive magic number which is the eight printable characters &#8220;!&lt;arch&gt;
&#8221; where 
 represents the newline character (0x0A). Following the magic number, the file is composed of even length members that begin with an archive header and end with a 
 padding character if necessary (to make the length even). Each file member is composed of a header (defined below), an optional newline-terminated &#8220;long file name&#8221; and the contents of the file. </p>
<p> The fields of the header are described in the items below. All fields of the header contain only <font SIZE="-1">ASCII</font> characters, are left justified and are right padded with space characters.</p>
<dl>
<dt>name &#8211; char[16]</p>
<dd> This field of the header provides the name of the archive member. If the name is longer than 15 characters or contains a slash (/) character, then this field contains <tt>&quot;#1/nnn&quot;</tt> where <tt>&quot;nnn&quot;</tt> provides the length of the name and the <tt>&quot;#1/&quot;</tt> is literal. In this case, the actual name of the file is provided in the <tt>&quot;nnn&quot;</tt> bytes immediately following the header. If the name is 15 characters or less, it is contained directly in this field and terminated with a slash (/) character.</p>
<dt>date &#8211; char[12]</p>
<dd> This field provides the date of modification of the file in the form of a decimal encoded number that provides the number of seconds since the epoch (since 00:00:00 Jan 1, 1970) per Posix specifications.</p>
<dt>uid &#8211; char[6]</p>
<dd> This field provides the user id of the file encoded as a decimal <font SIZE="-1">ASCII</font> string. This field might not make much sense on non-Unix systems. On Unix, it is the same value as the st_uid field of the stat structure returned by the <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) operating system call.</p>
<dt>gid &#8211; char[6]</p>
<dd> This field provides the group id of the file encoded as a decimal <font SIZE="-1">ASCII</font> string. This field might not make much sense on non-Unix systems. On Unix, it is the same value as the st_gid field of the stat structure returned by the <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) operating system call.</p>
<dt>mode &#8211; char[8]</p>
<dd> This field provides the access mode of the file encoded as an octal <font SIZE="-1">ASCII</font> string. This field might not make much sense on non-Unix systems. On Unix, it is the same value as the st_mode field of the stat structure returned by the <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) operating system call.</p>
<dt>size &#8211; char[10]</p>
<dd> This field provides the size of the file, in bytes, encoded as a decimal <font SIZE="-1">ASCII</font> string. If the size field is negative (starts with a minus sign, 0x02D), then the archive member is stored in compressed form. The first byte of the archive member&#8217;s data indicates the compression type used. A value of 0 (0x30) indicates that no compression was used. A value of 2 (0x32) indicates that bzip2 compression was used.</p>
<dt>fmag &#8211; char[2]</p>
<dd> This field is the archive file member magic number. Its content is always the two characters back tick (0x60) and newline (0x0A). This provides some measure utility in identifying archive files that have been corrupted.</dl>
<p> The <font SIZE="-1">LLVM</font> symbol table has the special name &#8220;#_LLVM_SYM_TAB_#&#8221;. It is presumed that no regular archive member file will want this name. The <font SIZE="-1">LLVM</font> symbol table is simply composed of a sequence of triplets: byte offset, length of symbol, and the symbol itself. Symbols are not null or newline terminated. Here are the details on each of these items:</p>
<dl>
<dt>offset &#8211; vbr encoded 32-bit integer</p>
<dd> The offset item provides the offset into the archive file where the bitcode member is stored that is associated with the symbol. The offset value is 0 based at the start of the first &#8220;normal&#8221; file member. To derive the actual file offset of the member, you must add the number of bytes occupied by the file signature (8 bytes) and the symbol tables. The value of this item is encoded using variable bit rate encoding to reduce the size of the symbol table. Variable bit rate encoding uses the high bit (0x80) of each byte to indicate if there are more bytes to follow. The remaining 7 bits in each byte carry bits from the value. The final byte does not have the high bit set.</p>
<dt>length &#8211; vbr encoded 32-bit integer</p>
<dd> The length item provides the length of the symbol that follows. Like this <i>offset</i> item, the length is variable bit rate encoded.</p>
<dt>symbol &#8211; character array</p>
<dd> The symbol item provides the text of the symbol that is associated with the <i>offset</i>. The symbol is not terminated by any character. Its length is provided by the <i>length</i> field. Note that is allowed (but unwise) to use non-printing characters (even 0x00) in the symbol. This allows for multiple encodings of symbol names.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-ar</code> succeeds, it will exit with 0. A usage error, results in an exit code of 1. A hard (file system typically) error results in an exit code of 2. Miscellaneous or unknown errors result in an exit code of 3.</p>
<h2>SEE ALSO</h2>
<p> llvm-ranlib, <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1)</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
