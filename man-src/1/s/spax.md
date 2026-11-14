---
title: "spax(1)"
name: "spax"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spax/"
description: "pax – portable archive interchange"
---

<h2>NAME</h2>
<p> pax &#8211; portable archive interchange</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>spax</code></p>
<dd> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<i>other options</i>] [-cdnv] [-H|-L] [-f&nbsp;<wbr><i>archive] [-o options</i>]&#8230; [-s <i>replstr]&#8230; [pattern</i>&#8230;] </p>
<dt><code>spax</code></p>
<dd> -r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<i>other options</i>] [-cdiknuv] [-H|-L] [-f&nbsp;<wbr><i>archive] [-o options</i>]&#8230; [-p&nbsp;<wbr><i>string</i>]&#8230; [-s&nbsp;<wbr><i>replstr</i>]&#8230; [<i>pattern&#8230;] </p>
<dt></i><code>spax</code></p>
<dd> -w&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<i>other options</i>] [-dituvX] [-H|-L] [-b&nbsp;<wbr><i>blocksize</i>] [-a] [-f&nbsp;<wbr><i>archive] [-o options</i>]&#8230; [-s&nbsp;<wbr><i>replstr</i>]&#8230; [-x&nbsp;<wbr><i>format</i>] [<i>file</i>&#8230;] </p>
<dt><code>spax</code></p>
<dd> -r -w[<i>other options</i>] [-diklntuvX] [-H|-L] [-o&nbsp;<wbr><i>options</i>]&#8230; [-p&nbsp;<wbr><i>string</i>]&#8230; [-s&nbsp;<wbr><i>replstr</i>]&#8230; [<i>file</i>&#8230;] <i>directory</i></dl>
<h2>DESCRIPTION</h2>
<p> The <code>pax </code> utility shall read, write, and write lists of the members of archive files and copy directory hierarchies. A variety of archive formats shall be supported; see the <code>-x</code> format option. </p>
<p> The action to be taken depends on the presence of the <code>-r</code> and <code>-w</code> options. The four combinations of <code>-r</code> and <code>-w</code> are referred to as the four modes of operation: <code>list</code>, <code>read</code>, <code>write</code>, and <code>copy</code> modes, corresponding respectively to the four forms shown in the SYNOPSIS section.</p>
<dl>
<dt><code>list</code></p>
<dd> In <code>list</code> mode (when neither <code>-r</code> nor <code>-w</code> are specified), <code>pax</code> shall write the names of the members of the archive file read from the standard input, with pathnames matching the specified <i>patterns</i>, to standard output. If a named file is of type directory, the file hierarchy rooted at that file shall be listed as well.</p>
<dt><code>read</code></p>
<dd> In <code>read</code> mode (when <code>-r</code> is specified, but <code>-w</code> is not), <code>pax</code> shall extract the members of the archive file read from the standard input, with pathnames matching the specified <i>patterns</i>. If an extracted file is of type directory, the file hierarchy rooted at that file shall be extracted as well. The extracted files shall be created performing pathname resolution with the directory in which <code>pax</code> was invoked as the current working directory. </p>
<p> If an attempt is made to extract a directory when the directory already exists, this shall not be considered an error. If an attempt is made to extract a FIFO when the FIFO already exists, this shall not be considered an error. </p>
<p> The ownership, access, and modification times, and file mode of the restored files are discussed under the <code>-p</code> option.</p>
<dt><code>write</code></p>
<dd> In <code>write</code> mode (when <code>-w</code> is specified, but <code>-r</code> is not), <code>pax</code> shall write the contents of the file operands to the standard output in an archive format. If no file operands are specified, a list of files to copy, one per line, shall be read from the standard input. A file of type directory shall include all of the files in the file hierarchy rooted at the file.</p>
<dt><code>copy</code></p>
<dd> In <code>copy</code> mode (when both <code>-r</code> and <code>-w</code> are specified), <code>pax</code> shall copy the file operands to the destination directory. </p>
<p> If no file operands are specified, a list of files to copy, one per line, shall be read from the standard input. A file of type directory shall include all of the files in the file hierarchy rooted at the file. </p>
<p> The effect of the <code>copy</code> shall be as if the copied files were written to an archive file and then subsequently extracted, except that there may be hard links between the original and the copied files. If the destination directory is a subdirectory of one of the files to be copied, the results are unspecified. If the destination directory is a file of a type not defined by the System Interfaces volume of IEEE Std 1003.1-2001, the results are implementation-defined; otherwise, it shall be an error for the file named by the directory operand not to exist, not be writable by the user, or not be a file of type directory.</dl>
<p> In <code>read</code> or <code>copy</code> modes, if intermediate directories are necessary to extract an archive member, <code>pax </code> shall perform actions equivalent to the <code>mkdir</code>() function defined in the System Interfaces volume of IEEE Std 1003.1-2001, called with the following arguments:</p>
<dl>
<dt><code>&bull;</code></p>
<dd> The intermediate directory used as the <code>path</code> argument.</p>
<dt><code>&bull;</code></p>
<dd> The value of the bitwise-inclusive <code>OR </code> of <code>S_IRWXU</code>, <code>S_IRWXG</code>, and <code>S_IRWXO</code> as the <i>mode</i> argument.</dl>
<p> If any specified <i>pattern</i> or <i>file</i> operands are not matched by at least one file or archive member, <code>pax </code> shall write a diagnostic message to standard error for each one that did not match and exit with a non-zero exit status. </p>
<p> The archive formats described in the <code>EXTENDED DESCRIPTION</code> section shall be automatically detected on input. The default output archive format shall be implementation-defined. </p>
<p> The <code>spax</code> implementation defaults to <code>-x ustar</code>. </p>
<p> A single archive can span multiple files. The <code>pax</code> utility shall determine, in an implementation-defined manner, what file to read or write as the next file. </p>
<p> If the selected archive format supports the specification of linked files, it shall be an error if these files cannot be linked when the archive is extracted, except that if the files to be linked are symbolic links and the system is not capable of making hard links to symbolic links, then separate copies of the symbolic link shall be created instead. For archive formats that do not store file contents with each name that causes a hard link, if the file that contains the data is not extracted during this <code>pax</code> session, either the data shall be restored from the original file, or a diagnostic message shall be displayed with the name of a file that can be used to extract the data. In traversing directories, <code>pax</code> shall detect infinite loops; that is, entering a previously visited directory that is an ancestor of the last file visited. When it detects an infinite loop, <code>pax</code> shall write a diagnostic message to standard error and shall terminate. </p>
<h2>OPTIONS</h2>
<p> The <code>pax</code> utility shall conform to the Base Definitions volume of IEEE Std 1003.1-2001, Section 12.2, Utility Syntax Guidelines, except that the order of presentation of the <code>-o</code>, <code>-p</code>, and <code>-s</code> options is significant. </p>
<p> See also the &quot;OTHER OPTIONS&quot; section. </p>
<p> The following options shall be supported:</p>
<dl>
<dt><code>-r</code></p>
<dd> Read an archive file from standard input.</p>
<dt><code>-w</code></p>
<dd> Write files to the standard output in the specified archive format.</p>
<dt><code>-a</code></p>
<dd> Append files to the end of the archive. It is implementation-defined which devices on the system support appending. Additional file formats unspecified by this volume of IEEE Std 1003.1-2001 may impose restrictions on appending.</p>
<dt><code>-b</code><i> blocksize</i></p>
<dd> Block the output at a positive decimal integer number of bytes per write to the archive file. Devices and archive formats may impose restrictions on blocking. Blocking shall be automatically determined on input. Conforming applications shall not specify a blocksize value larger than 32256. Default blocking when creating archives depends on the archive format. (See the <code>-x </code> option below.)</p>
<dt><code>-c</code></p>
<dd> Match all file or archive members except those specified by the pattern or file operands.</p>
<dt><code>-d</code></p>
<dd> Cause files of type directory being copied or archived or archive members of type directory being extracted or listed to match only the file or archive member itself and not the file hierarchy rooted at the file.</p>
<dt><code>-f</code><i> archive</i></p>
<dd> Specify the pathname of the input or output archive, overriding the default standard input (in <code>list</code> or <code>read</code> modes) or standard output (<code>write</code> mode).</p>
<dt><code>-H</code></p>
<dd> If a symbolic link referencing a file of type directory is specified on the command line, <code>pax </code> shall archive the file hierarchy rooted in the file referenced by the link, using the name of the link as the root of the file hierarchy. Otherwise, if a symbolic link referencing a file of any other file type which <code>pax </code> can normally archive is specified on the command line, then <code>pax </code> shall archive the file referenced by the link, using the name of the link. The default behavior shall be to archive the symbolic link itself.</p>
<dt><code>-i</code></p>
<dd> Interactively rename files or archive members. For each archive member matching a pattern operand or file matching a file operand, a prompt shall be written to the file /dev/tty. The prompt shall contain the name of the file or archive member, but the format is otherwise unspecified. A line shall then be read from /dev/tty. If this line is blank, the file or archive member shall be skipped. If this line consists of a single period, the file or archive member shall be processed with no modification to its name. Otherwise, its name shall be replaced with the contents of the line. The <code>pax</code> utility shall immediately exit with a non-zero exit status if end-of-file is encountered when reading a response or if /dev/tty cannot be opened for reading and writing. </p>
<p> The results of extracting a hard link to a file that has been renamed during extraction are unspecified.</p>
<dt><code>-k</code></p>
<dd> Prevent the overwriting of existing files.</p>
<dt><code>-l</code></p>
<dd> (The letter ell.) In copy mode, hard links shall be made between the source and destination file hierarchies whenever possible. If specified in conjunction with <code>-H </code> or <code>-L</code>, when a symbolic link is encountered, the hard link created in the destination file hierarchy shall be to the file referenced by the symbolic link. If specified when neither <code>-H </code> nor <code>-L </code> is specified, when a symbolic link is encountered, the implementation shall create a hard link to the symbolic link in the source file hierarchy or copy the symbolic link to the destination.</p>
<dt><code>-L</code></p>
<dd> If a symbolic link referencing a file of type directory is specified on the command line or encountered during the traversal of a file hierarchy, <code>pax </code> shall archive the file hierarchy rooted in the file referenced by the link, using the name of the link as the root of the file hierarchy. Otherwise, if a symbolic link referencing a file of any other file type which <code>pax </code> can normally archive is specified on the command line or encountered during the traversal of a file hierarchy, <code>pax </code> shall archive the file referenced by the link, using the name of the link. The default behavior shall be to archive the symbolic link itself.</p>
<dt><code>-n</code></p>
<dd> Select the first archive member that matches each pattern operand. No more than one archive member shall be matched for each pattern (although members of type directory shall still match the file hierarchy rooted at that file).</p>
<dt><code>-o</code><i> options</i></p>
<dd> Provide information to the implementation to modify the algorithm for extracting or writing files. The value of options shall consist of one or more comma-separated keywords of the form:</p>
<dl>
<dt>
<dd>
<p> <code>keyword[[:]=</code><i>value</i><code>][,keyword[[:]=</code><i>value</i><code>],</code><i>&#8230;]</i> </p>
<p> Some keywords apply only to certain file formats, as indicated with each description. Use of keywords that are inapplicable to the file format being processed produces undefined results. </p>
<p> Keywords in the options argument shall be a string that would be a valid portable filename as described in the Base Definitions volume of IEEE Std 1003.1-2001, Section 3.276, Portable Filename Character Set.</p>
<dl>
<dt><code>Note:</code></p>
<dd> Keywords are not expected to be filenames, merely to follow the same character composition rules as portable filenames.</dl>
<p> Keywords can be preceded with white space. The value field shall consist of zero or more characters; within value, the application shall precede any literal comma with a backslash, which shall be ignored, but preserves the comma as part of value. A comma as the final character, or a comma followed solely by white space as the final characters, in options shall be ignored. Multiple <code>-o </code> options can be specified; if keywords given to these multiple <code>-o </code> options conflict, the keywords and values appearing later in command line sequence shall take precedence and the earlier shall be silently ignored. The following keyword values of options shall be supported for the file formats as indicated:</p>
<dl>
<dt><code>delete=</code><i>pattern</i></p>
<dd> (Applicable only to the <code>-x pax </code> format.) When used in write or copy mode, <code>pax </code> shall omit from extended header records that it produces any keywords matching the string pattern. When used in read or list mode, <code>pax</code> shall ignore any keywords matching the string pattern in the extended header records. In both cases, matching shall be performed using the pattern matching notation described in Patterns Matching a Single Character and Patterns Matching Multiple Characters. For example:</p>
<dl>
<dt>
<dd>
<p> <code>-o delete=</code><i>security.*</i> </p>
<p> would suppress security-related information. See <code>pax Extended Header </code> for extended header record keyword usage. </p>
<p> When multiple <code>-o delete=</code><i>pattern</i> options are specified, the patterns shall be additive; all keywords matching the specified string patterns shall be omitted from extended header records that <code>pax </code> produces.</dl>
<dt><code>exthdr.name=</code><i>string</i></p>
<dd> (Applicable only to the <code>-x pax </code> format.) This keyword allows user control over the name that is written into the ustar header blocks for the extended header produced under the circumstances described in <code>pax Header Block.</code> The name shall be the contents of string, after the following character substitutions have been made:</p>
<dl>
<dt>
<dd>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>string Includes:</code></td>
<td><code>Replaced By:</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>%d</td>
<td>The directory name of the file, equivalent
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>to the result of the dirname utility on the
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>translated pathname.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>%f</td>
<td>The filename of the file, equivalent to the
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>result of the basename utility on the
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>translated pathname.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>%p</td>
<td>The process ID of the pax process.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>%%</td>
<td>A &#8216;%&#8217; character.
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Any other &#8216;%&#8217; characters in string produce undefined results. </p>
<p> If no -o exthdr.name= string is specified, <code>pax </code> shall use the following default value: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%d/PaxHeaders.%p/%f </p>
</dl>
<dt><code>globexthdr.name=</code><i>string</i></p>
<dd> (Applicable only to the <code>-x pax </code> format.) When used in write or copy mode with the appropriate options, <code>pax</code> shall create global extended header records with ustar header blocks that will be treated as regular files by previous versions of <code>pax</code>. This keyword allows user control over the name that is written into the ustar header blocks for global extended header records. The name shall be the contents of string, after the following character substitutions have been made:</p>
<dl>
<dt>
<dd>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>string Includes:</code></td>
<td><code>Replaced By:</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>%n</td>
<td>An integer that represents the sequence
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>number of the global extended header record
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>in the archive, starting at 1.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>%p</td>
<td>The process ID of the pax process.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>%%</td>
<td>A &#8216;%&#8217; character.
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Any other &#8216;%&#8217; characters in string produce undefined results. </p>
<p> If no <code>-o globexthdr.name=</code><i>string</i> is specified, <code>pax </code> shall use the following default value: </p>
<p> $TMPDIR/GlobalHead.%p.%n </p>
<p> where <code>$TMPDIR </code> represents the value of the <code>TMPDIR</code> environment variable. If <code>TMPDIR </code> is not set, <code>pax </code> shall use /tmp.</dl>
<dt><code>invalid=</code><i>action</i></p>
<dd> (Applicable only to the <code>-x pax </code> format.) This keyword allows user control over the action <code>pax </code> takes upon encountering values in an extended header record that, in read or copy mode, are invalid in the destination hierarchy or, in list mode, cannot be written in the codeset and current locale of the implementation. The following are invalid values that shall be recognized by <code>pax</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>+</code></p>
<dd> In read or copy mode, a filename or link name that contains character encodings invalid in the destination hierarchy. (For example, the name may contain embedded NULs.)</p>
<dt><code>+</code></p>
<dd> In read or copy mode, a filename or link name that is longer than the maximum allowed in the destination hierarchy (for either a pathname component or the entire pathname).</p>
<dt><code>+</code></p>
<dd> In list mode, any character string value (filename, link name, user name, and so on) that cannot be written in the codeset and current locale of the implementation.</dl>
<p> The following mutually-exclusive values of the action argument are supported:</p>
<dl>
<dt><code>bypass</code></p>
<dd> In read or copy mode, <code>pax </code> shall bypass the file, causing no change to the destination hierarchy. In list mode, <code>pax </code> shall write all requested valid values for the file, but its method for writing invalid values is unspecified.</p>
<dt><code>rename</code></p>
<dd> In read or copy mode, <code>pax </code> shall act as if the <code>-i</code> option were in effect for each file with invalid filename or link name values, allowing the user to provide a replacement name interactively. In list mode, <code>pax </code> shall behave identically to the bypass action.</p>
<dt><code>UTF-8</code></p>
<dd> When used in read, copy, or list mode and a filename, link name, owner name, or any other field in an extended header record cannot be translated from the <code>pax </code> UTF-8 codeset format to the codeset and current locale of the implementation, <code>pax </code> shall use the actual UTF-8 encoding for the name.</p>
<dt><code>write</code></p>
<dd> In read or copy mode, <code>pax </code> shall write the file, translating the name, regardless of whether this may overwrite an existing file with a valid name. In list mode, <code>pax </code> shall behave identically to the bypass action.</dl>
<p> If no <code>-o invalid=</code><i>option</i> is specified, <code>pax </code> shall act as if <code>-o invalid= bypass </code> were specified. Any overwriting of existing files that may be allowed by the <code>-o invalid=</code> actions shall be subject to permission(<code>-p</code>) and modification time (<code>-u</code>) restrictions, and shall be suppressed if the <code>-k </code> option is also specified.</dl>
<dt><code>linkdata</code></p>
<dd> (Applicable only to the <code>-x pax </code> format.) In write mode, <code>pax </code> shall write the contents of a file to the archive even when that file is merely a hard link to a file whose contents have already been written to the archive.</p>
<dt><code>listopt=</code><i>format</i></p>
<dd> This keyword specifies the output format of the table of contents produced when the <code>-v </code> option is specified in list mode. See List Mode Format Specifications. To avoid ambiguity, the listopt= format shall be the only or final keyword= value pair in a <code>-o </code><i>option-argument</i>; all characters in the remainder of the option-argument shall be considered part of the format string. When multiple -o listopt= format options are specified, the format strings shall be considered a single, concatenated string, evaluated in command line order.</p>
<dt><code>times</code></p>
<dd> (Applicable only to the <code>-x pax </code> format.) When used in write or copy mode, <code>pax </code> shall include atime and mtime extended header records for each file. See <code>pax Extended Header File Times</code>.</dl>
<p> In addition to these keywords, if the <code>-x pax </code> format is specified, any of the keywords and values defined in <code>pax Extended Header</code>, including implementation extensions, can be used in <code>-o</code><i> option-arguments</i>, in either of two modes:</p>
<dl>
<dt><code>keyword=</code><i>value</i></p>
<dd> When used in write or copy mode, these keyword/value pairs shall be included at the beginning of the archive as typeflag g global extended header records. When used in read or list mode, these keyword/value pairs shall act as if they had been at the beginning of the archive as typeflag g global extended header records.</p>
<dt><code>keyword:=</code><i>value</i></p>
<dd> When used in write or copy mode, these keyword/value pairs shall be included as records at the beginning of a typeflag x extended header for each file. (This shall be equivalent to the equal-sign form except that it creates no typeflag g global extended header records.) When used in read or list mode, these keyword/value pairs shall act as if they were included as records at the end of each extended header; thus, they shall override any global or file-specific extended header record keywords of the same names. For example, in the command:</p>
<dl>
<dt>
<dd>
<p> <code>pax -r -o &quot;gname:=mygroup,&quot; &lt;archive</code> </p>
<p> the group name will be forced to a new value for all files read from the archive.</dl>
</dl>
<p> The precedence of <code>-o</code> keywords over various fields in the archive is described in <code>pax Extended Header Keyword Precedence</code>.</dl>
<dt><code>-p</code><i> string</i></p>
<dd> Specify one or more file characteristic options (privileges). The string option-argument shall be a string specifying file characteristics to be retained or discarded on extraction. The string shall consist of the specification characters a , e, m, o, and p. Other implementation-defined characters can be included. Multiple characteristics can be concatenated within the same string and multiple <code>-p </code> options can be specified. The meaning of the specification characters are as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>a</code></p>
<dd> Do not preserve file access times.</p>
<dt><code>e</code></p>
<dd> Preserve the user ID, group ID, file mode bits (see the Base Definitions volume of IEEE Std 1003.1-2001, Section 3.168, File Mode Bits), access time, modification time, and any other implementation-defined file characteristics.</p>
<dt><code>m</code></p>
<dd>
<p> Do not preserve file modification times.</p>
<dt><code>o</code></p>
<dd> Preserve the user ID and group ID.</p>
<dt><code>p</code></p>
<dd> Preserve the file mode bits. Other implementation-defined file mode attributes may be preserved.</dl>
<p> In the preceding list, &quot;preserve&quot; indicates that an attribute stored in the archive shall be given to the extracted file, subject to the permissions of the invoking process. The access and modification times of the file shall be preserved unless otherwise specified with the <code>-p </code> option or not stored in the archive. All attributes that are not preserved shall be determined as part of the normal file creation action (see File Read, Write, and Creation). </p>
<p> If neither the e nor the o specification character is specified, or the user ID and group ID are not preserved for any reason, <code>pax </code> shall not set the S_ISUID and S_ISGID bits of the file mode. </p>
<p> If the preservation of any of these items fails for any reason, <code>pax </code> shall write a diagnostic message to standard error. Failure to preserve these items shall affect the final exit status, but shall not cause the extracted file to be deleted. </p>
<p> If file characteristic letters in any of the string option-arguments are duplicated or conflict with each other, the ones given last shall take precedence. For example, if <code>-p eme</code> is specified, file modification times are preserved.</dl>
<dt><code>-s</code><i> replstr</i></p>
<dd> Modify file or archive member names named by pattern or file operands according to the substitution expression replstr, using the syntax of the ed utility. The concepts of &quot;address&quot; and &quot;line&quot; are meaningless in the context of the <code>pax </code> utility, and shall not be supplied. The format shall be:</p>
<dl>
<dt>
<dd>
<p> <code>-s /old/new/[gp]</code> </p>
<p> where as in ed, old is a basic regular expression and new can contain an ampersand, &#8216;
&#8217; (where n is a digit) backreferences, or subexpression matching. The old string shall also be permitted to contain &lt;newline&gt;s. </p>
<p> Any non-null character can be used as a delimiter ( &#8216;/&#8217; shown here). Multiple <code>-s </code> expressions can be specified; the expressions shall be applied in the order specified, terminating with the first successful substitution. The optional trailing &#8216;g&#8217; is as defined in the ed utility. The optional trailing &#8216;p&#8217; shall cause successful substitutions to be written to standard error. File or archive member names that substitute to the empty string shall be ignored when reading and writing archives.</dl>
<dt><code>-t</code></p>
<dd> When reading files from the file system, and if the user has the permissions required by utime() to do so, set the access time of each file read to the access time that it had before being read by <code>pax</code>.</p>
<dt><code>-u</code></p>
<dd> Ignore files that are older (having a less recent file modification time) than a pre-existing file or archive member with the same name. In read mode, an archive member with the same name as a file in the file system shall be extracted if the archive member is newer than the file. In write mode, an archive file member with the same name as a file in the file system shall be superseded if the file is newer than the archive member. If <code>-a </code> is also specified, this is accomplished by appending to the archive; otherwise, it is unspecified whether this is accomplished by actual replacement in the archive or by appending to the archive. In copy mode, the file in the destination hierarchy shall be replaced by the file in the source hierarchy or by a link to the file in the source hierarchy if the file in the source hierarchy is newer.</p>
<dt><code>-v</code></p>
<dd> In list mode, produce a verbose table of contents (see the STDOUT section). Otherwise, write archive member pathnames to standard error (see the STDERR section).</p>
<dt><code>-x</code><i> format</i></p>
<dd> Specify the output archive format. The <code>pax </code> utility shall support the following formats:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cpio</code></p>
<dd> The cpio interchange format; see the EXTENDED DESCRIPTION section. The default blocksize for this format for character special archive files shall be 5120. Implementations shall support all blocksize values less than or equal to 32256 that are multiples of 512.</p>
<dt><code>pax</code></p>
<dd> The <code>pax</code> interchange format; see the <code>EXTENDED DESCRIPTION</code> section. The default blocksize for this format for character special archive files shall be 5120. Implementations shall support all blocksize values less than or equal to 32256 that are multiples of 512.</p>
<dt><code>ustar</code></p>
<dd> The tar interchange format; see the EXTENDED DESCRIPTION section. The default blocksize for this format for character special archive files shall be 10240. Implementations shall support all blocksize values less than or equal to 32256 that are multiples of 512.</dl>
<p> Implementation-defined formats shall specify a default block size as well as any other block sizes supported for character special archive files. </p>
<p> Any attempt to append to an archive file in a format different from the existing archive format shall cause <code>pax </code> to exit immediately with a non-zero exit status. </p>
<p> In copy mode, if no <code>-x </code> format is specified, <code>pax </code> shall behave as if <code>-x pax</code> were specified.</dl>
<dt><code>-X</code></p>
<dd> When traversing the file hierarchy specified by a pathname, <code>pax </code> shall not descend into directories that have a different device ID ( st_dev; see the System Interfaces volume of IEEE Std 1003.1-2001, stat()).</dl>
<p> Specifying more than one of the mutually-exclusive options <code>-H </code> and <code>-L </code> shall not be considered an error and the last option specified shall determine the behavior of the utility. </p>
<p> The options that operate on the names of files or archive members (<code>-c</code>, <code>-i</code>, <code>-n</code>, <code>-s</code>, <code>-u</code>, and <code>-v</code>) shall interact as follows. In read mode, the archive members shall be selected based on the user-specified pattern operands as modified by the <code>-c</code>, <code>-n</code>, and <code>-u</code> options. Then, any <code>-s </code> and <code>-i </code> options shall modify, in that order, the names of the selected files. The <code>-v</code> option shall write names resulting from these modifications. </p>
<p> In write mode, the files shall be selected based on the user-specified pathnames as modified by the <code>-n </code> and <code>-u options.</code> Then, any <code>-s </code> and <code>-i </code> options shall modify, in that order, the names of these selected files. The <code>-v </code> option shall write names resulting from these modifications. </p>
<p> If both the <code>-u </code> and <code>-n </code> options are specified, <code>pax </code> shall not consider a file selected unless it is newer than the file to which it is compared. </p>
<h3>List Mode Format Specifications</h3>
<p> The manual page for <code>spax</code> is not yet ready. The following text is a quotation from the POSIX.1-2001 standard. </p>
<p> In <code>list</code> mode with the <code>-o listopt=</code><i>format</i> option, the <i>format</i> argument shall be applied for each selected file. The <code>pax </code> utility shall append a &lt;newline&gt; to the <code>listopt</code> output for each selected file. The <i>format</i> argument shall be used as the <i>format</i> string described in the Base Definitions volume of IEEE Std 1003.1-2001, Chapter 5, File Format Notation, with the exceptions 1. through 5. defined in the EXTENDED DESCRIPTION section of <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), plus the following exceptions:</p>
<dl>
<dt><code>6.</code></p>
<dd> The sequence (<i>keyword</i>) can occur before a format conversion specifier. The conversion argument is defined by the value of <i>keyword</i>. The implementation shall support the following <i>keywords</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&bull;</code></p>
<dd> Any of the Field Name entries in ustar Header Block and Octet-Oriented cpio Archive Entry. The implementation may support the <i>cpio</i> keywords without the leading <code>c_</code> in addition to the form required by Values for <code>cpio</code> <code>c_mode</code> Field.</p>
<dt><code>&bull;</code></p>
<dd> Any keyword defined for the extended header in <code>pax Extended Header</code>.</p>
<dt><code>&bull;</code></p>
<dd> Any keyword provided as an implementation-defined extension within the extended header defined in <code>pax Extended Header</code>.</dl>
<p> For example, the sequence &quot;%(charset)s&quot; is the string value of the name of the character set in the extended header. </p>
<p> The result of the keyword conversion argument shall be the value from the applicable header field or extended header, without any trailing NULs. </p>
<p> All keyword values used as conversion arguments shall be translated from the UTF-8 encoding to the character set appropriate for the local file system, user database, and so on, as applicable.</dl>
<dt><code>7.</code></p>
<dd> An additional conversion specifier character, <code>T</code>, shall be used to specify time formats. The <code>T</code> conversion specifier character can be preceded by the sequence (<code>keyword=</code><i>subformat</i>), where <i>subformat</i> is a date format as defined by date operands. The default <i>keyword</i> shall be <code>mtime </code> and the default subformat shall be:</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%b&nbsp;<wbr>%e&nbsp;<wbr>%H:%M&nbsp;<wbr>%Y </p>
<dl>
<dt><code>8.</code></p>
<dd> An additional conversion specifier character, <code>M</code>, shall be used to specify the file mode string as defined in <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) Standard Output. If (<i>keyword</i>) is omitted, the <code>mode </code> <i>keyword</i> shall be used. For example, <code>%.1M</code> writes the single character corresponding to the <i>&lt;entry type&gt;</i> field of the <code>ls -l</code> command.</p>
<dt><code>9.</code></p>
<dd> An additional conversion specifier character, <code>D</code>, shall be used to specify the device for block or special files, if applicable, in an implementation-defined format. If not applicable, and (<i>keyword</i>) is specified, then this conversion shall be equivalent to <code>%(keyword)u</code>. If not applicable, and (<i>keyword</i>) is omitted, then this conversion shall be equivalent to &lt;space&gt;.</p>
<dt><code>10.</code></p>
<dd> An additional conversion specifier character, <code>F</code>, shall be used to specify a pathname. The <code>F</code> conversion character can be preceded by a sequence of comma-separated keywords:</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(keyword[,keyword]&nbsp;<wbr>&#8230;&nbsp;<wbr>)</p>
<dl>
<dt>
<dd> The values for all the keywords that are non-null shall be concatenated together, each separated by a &#8216;/&#8217;. The default shall be (<code>path</code>) if the keyword path is defined; otherwise, the default shall be (<code>prefix, name</code>).</dl>
<dl>
<dt><code>11. </code></p>
<dd> An additional conversion specifier character, <code>L</code>, shall be used to specify a symbolic line expansion. If the current file is a symbolic link, then <code>%L</code> shall expand to:</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;%s -&gt;&nbsp;<wbr>%s&quot;,&nbsp;<wbr>&lt;value of keyword&gt;,&nbsp;<wbr>&lt;contents of link&gt; </p>
<p> Otherwise, the <code>%L</code> conversion specification shall be the equivalent of <code>%F</code>. </p>
<h2>OPERANDS</h2>
<p> The following operands shall be supported:</p>
<dl>
<dt><i>directory</i></p>
<dd> The destination directory pathname for copy mode.</p>
<dt><i>file</i></p>
<dd> A pathname of a file to be copied or archived.</p>
<dt><i>pattern</i></p>
<dd> A pattern matching one or more pathnames of archive members. A pattern must be given in the name-generating notation of the pattern matching notation in Pattern Matching Notation , including the filename expansion rules in Patterns Used for Filename Expansion. The default, if no pattern is specified, is to select all members in the archive. </p>
</dl>
<h2>STDIN</h2>
<p> In <code>write</code> mode, the standard input shall be used only if no <i>file</i> operands are specified. It shall be a text file containing a list of pathnames, one per line, without leading or trailing &lt;blank&gt;s. </p>
<p> In <code>list</code> and <code>read</code> modes, if <code>-f</code> is not specified, the standard input shall be an archive file. </p>
<p> Otherwise, the standard input shall not be used. </p>
<h2>INPUT FILES</h2>
<p> The input file named by the <i>archive </i> option-argument, or standard input when the archive is read from there, shall be a file formatted according to one of the specifications in the EXTENDED DESCRIPTION section or some other implementation-defined format. </p>
<p> The file <code>/dev/tty</code> shall be used to write prompts and read responses. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables shall affect the execution of <code>pax</code>:</p>
<dl>
<dt><code>LANG</code></p>
<dd> Provide a default value for the internationalization variables that are unset or null. (See the Base Definitions volume of IEEE Std 1003.1-2001, Section 8.2, Internationalization Variables for the precedence of internationalization variables used to determine the values of locale categories.)</p>
<dt><code>LC_ALL</code></p>
<dd> If set to a non-empty string value, override the values of all the other internationalization variables.</p>
<dt><code>LC_COLLATE</code></p>
<dd> Determine the locale for the behavior of ranges, equivalence classes, and multi-character collating elements used in the pattern matching expressions for the pattern operand, the basic regular expression for the <code>-s</code> option, and the extended regular expression defined for the <code>yesexpr</code> locale keyword in the LC_MESSAGES category.</p>
<dt><code>LC_CTYPE</code></p>
<dd> Determine the locale for the interpretation of sequences of bytes of text data as characters (for example, single-byte as opposed to multi-byte characters in arguments and input files), the behavior of character classes used in the extended regular expression defined for the <code>yesexpr</code> locale keyword in the LC_MESSAGES category, and pattern matching.</p>
<dt><code>LC_MESSAGES</code></p>
<dd> Determine the locale for the processing of affirmative responses that should be used to affect the format and contents of diagnostic messages written to standard error.</p>
<dt><code>LC_TIME</code></p>
<dd> Determine the format and contents of date and time strings when the <code>-v </code> option is specified.</p>
<dt><code>NLSPATH</code></p>
<dd> [XSI] [Option Start] Determine the location of message catalogs for the processing of LC_MESSAGES . [Option End]</p>
<dt><code>TMPDIR</code></p>
<dd> Determine the pathname that provides part of the default global extended header record file, as described for the <code>-o globexthdr=</code> keyword in the OPTIONS section.</p>
<dt><code>TZ</code></p>
<dd> Determine the timezone used to calculate date and time strings when the <code>-v </code> option is specified. If TZ is unset or null, an unspecified default timezone shall be used. </p>
</dl>
<h2>ASYNCHRONOUS EVENTS</h2>
<p> Default. </p>
<h2>STDOUT</h2>
<p> In <code>write </code> mode, if <code>-f </code> is not specified, the standard output shall be the archive formatted according to one of the specifications in the EXTENDED DESCRIPTION section, or some other implementation-defined format (see <code>-x</code><i> format</i><code>).</code> </p>
<p> In <code>list </code> mode, when the <code>-o listopt= </code> format has been specified, the selected archive members shall be written to standard output using the format described under List Mode Format Specifications. In <code>list </code> mode without the <code>-o listopt= </code> format option, the table of contents of the selected archive members shall be written to standard output using the following format: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;%s
&quot;,&nbsp;<wbr>&lt;pathname&gt; </p>
<p> If the <code>-v </code> option is specified in <code>list </code> mode, the table of contents of the selected archive members shall be written to standard output using the following formats. </p>
<p> For pathnames representing hard links to previous members of the archive: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;%s&nbsp;<wbr>==&nbsp;<wbr>%s
&quot;,&nbsp;<wbr>&lt;ls -l listing&gt;,&nbsp;<wbr>&lt;linkname&gt; </p>
<p> For all other pathnames: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;%s
&quot;,&nbsp;<wbr>&lt;ls -l listing&gt; </p>
<p> where <i>&lt;ls -l listing&gt;</i> shall be the format specified by the <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) utility with the <code>-l </code> option. When writing pathnames in this format, it is unspecified what is written for fields for which the underlying archive format does not have the correct information, although the correct number of &lt;blank&gt;-separated fields shall be written. </p>
<p> In <code>list </code> mode, standard output shall not be buffered more than a line at a time. </p>
<h2>STDERR</h2>
<p> If <code>-v </code> is specified in <code>read</code>, <code>write</code>, or <code>copy </code> modes, <code>pax </code> shall write the pathnames it processes to the standard error output using the following format: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;%s
&quot;,&nbsp;<wbr>&lt;pathname&gt; </p>
<p> These pathnames shall be written as soon as processing is begun on the file or archive member, and shall be flushed to standard error. The trailing &lt;newline&gt;, which shall not be buffered, is written when the file has been read or written. </p>
<p> If the <code>-s </code> option is specified, and the replacement string has a trailing <code>&#8216;p&#8217;</code>, substitutions shall be written to standard error in the following format: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;%s&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>%s
&quot;,&nbsp;<wbr>&lt;original pathname&gt;,&nbsp;<wbr>&lt;new pathname&gt; </p>
<p> In all operating modes of <code>pax</code>, optional messages of unspecified format concerning the input archive format and volume number, the number of files, blocks, volumes, and media parts as well as other diagnostic messages may be written to standard error. </p>
<p> In all formats, for both standard output and standard error, it is unspecified how non-printable characters in pathnames or link names are written. </p>
<p> When <code>pax</code> is in <code>read </code> mode or <code>list </code> mode, using the <code>-x pax </code> archive format, and a filename, link name, owner name, or any other field in an extended header record cannot be translated from the <code>pax</code> UTF-8 codeset format to the codeset and current locale of the implementation, <code>pax </code> shall write a diagnostic message to standard error, shall process the file as described for the <code>-o invalid=</code> option, and then shall process the next file in the archive. </p>
<h2>OUTPUT FILES</h2>
<p> In <code>read </code> mode, the extracted output files shall be of the archived file type. In <code>copy </code> mode, the copied output files shall be the type of the file being copied. In either mode, existing files in the destination hierarchy shall be overwritten only when all permission (<code>-p</code>), modification time (<code>-u</code>), and invalid-value (<code>-o invalid=</code>) tests allow it. </p>
<p> In <code>write </code> mode, the output file named by the <code>-f </code> option-argument shall be a file formatted according to one of the specifications in the EXTENDED DESCRIPTION section, or some other implementation-defined format. </p>
<h2>EXTENDED DESCRIPTION</h2>
<h3>pax Interchange Format</h3>
<p> A <code>pax </code> archive tape or file produced in the <code>-x pax </code> format shall contain a series of blocks. The physical layout of the archive shall be identical to the <code>ustar </code> format described in ustar Interchange Format. Each file archived shall be represented by the following sequence:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&bull;</code></p>
<dd> An optional header block with extended header records. This header block is of the form described in <code>pax Header Block</code>, with a <i>typeflag </i> value of <code>x</code> or <code>g</code>. The extended header records, described in <code>pax Extended Header</code>, shall be included as the data for this header block.</p>
<dt><code>&bull;</code></p>
<dd> A header block that describes the file. Any fields in the preceding optional extended header shall override the associated fields in this header block for this file.</p>
<dt><code>&bull;</code></p>
<dd> Zero or more blocks that contain the contents of the file.</dl>
</dl>
<p> At the end of the archive file there shall be two 512-byte blocks filled with binary zeros, interpreted as an end-of-archive indicator. </p>
<p> A schematic of an example archive with global extended header records and two actual files is shown in <code>pax Format Archive</code> Example. In the example, the second file in the archive has no extended header preceding it, presumably because it has no need for extended attributes. </p>
<p> <center> <code>Figure: pax Format Archive Example</code><br />
 </center> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td>ustar Header [typeflag = &#8216;g&#8217;]</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Global Extended Header Data</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ustar Header [typeflag = &#8216;x&#8217;]</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Extended Header Data</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ustar Header [typeflag = &#8216;0&#8217;]</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Data for File 1</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ustar Header [typeflag = &#8216;0&#8217;]</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Data for File 2</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Block of binary Zeroes</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Block of binary Zeroes</td>
</tr>
</table>
</table>
<p></center> </p>
<h3>pax Header Block</h3>
<p> The <code>pax</code> header block shall be identical to the <code>ustar</code> header block described in <code>ustar Interchange Format</code>, except that two additional <i>typeflag </i> values are defined:</p>
<dl>
<dt><code>x</code></p>
<dd> Represents extended header records for the following file in the archive (which shall have its own <code>ustar </code> header block). The format of these extended header records shall be as described in <code>pax Extended Header</code>.</p>
<dt><code>g</code></p>
<dd> Represents global extended header records for the following files in the archive. The format of these extended header records shall be as described in <code>pax Extended Header</code>. Each value shall affect all subsequent files that do not override that value in their own extended header record and until another global extended header record is reached that provides another value for the same field. The <i>typeflag </i> <code>g</code> global headers should not be used with interchange media that could suffer partial data loss in transporting the archive.</dl>
<p> For both of these types, the size field shall be the size of the extended header records in octets. The other fields in the header block are not meaningful to this version of the <code>pax</code> utility. However, if this archive is read by a <code>pax </code> utility conforming to the ISO POSIX-2:1993 standard, the header block fields are used to create a regular file that contains the extended header records as data. Therefore, header block field values should be selected to provide reasonable file access to this regular file. </p>
<p> A further difference from the <code>ustar </code> header block is that data blocks for files of <i>typeflag </i> <code>1</code> (the digit one) (hard link) may be included, which means that the size field may be greater than zero. Archives created by <code>pax -o linkdata </code> shall include these data blocks with the hard links. </p>
<h3>pax Extended Header</h3>
<p> A <code>pax </code> extended header contains values that are inappropriate for the <code>ustar</code> header block because of limitations in that format: fields requiring a character encoding other than that described in the ISO/IEC 646:1991 standard, fields representing file attributes not described in the <code>ustar</code> header, and fields whose format or length do not fit the requirements of the <code>ustar</code> header. The values in an extended header add attributes to the following file (or files; see the description of the <i>typeflag </i> <code>g </code> header block) or override values in the following header block(s), as indicated in the following list of keywords. </p>
<p> An extended header shall consist of one or more records, each constructed as follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;%d&nbsp;<wbr>%s=%s
&quot;,&nbsp;<wbr>&lt;length&gt;,&nbsp;<wbr>&lt;keyword&gt;,&nbsp;<wbr>&lt;value&gt; </p>
<p> The extended header records shall be encoded according to the ISO/IEC 10646-1:2000 standard (UTF-8). The <i>&lt;length&gt; </i> field, &lt;blank&gt;, equals sign, and &lt;newline&gt; shown shall be limited to the portable character set, as encoded in UTF-8. The <i>&lt;keyword&gt; </i> and <i>&lt;value&gt; </i> fields can be any UTF-8 characters. The <i>&lt;length&gt;</i> field shall be the decimal length of the extended header record in octets, including the trailing &lt;newline&gt;. </p>
<p> The <i>&lt;keyword&gt;</i> field shall be one of the entries from the following list or a keyword provided as an implementation extension. Keywords consisting entirely of lowercase letters, digits, and periods are reserved for future standardization. A keyword shall not include an equals sign. (In the following list, the notations &quot;file(s)&quot; or &quot;block(s)&quot; is used to acknowledge that a keyword affects the following single file after a <i>typeflag </i> <code>x </code> extended header, but possibly multiple files after <i>typeflag </i> <code>g</code>. Any requirements in the list for <code>pax </code> to include a record when in <code>write</code> or <code>copy </code> mode shall apply only when such a record has not already been provided through the use of the <code>-o </code> option. When used in <code>copy</code> mode, <code>pax </code> shall behave as if an archive had been created with applicable extended header records and then extracted.)</p>
<dl>
<dt><code>atime</code></p>
<dd> The file access time for the following file(s), equivalent to the value of the <i>st_atime </i> member of the <code>stat </code> structure for a file, as described by the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) function. The access time shall be restored if the process has the appropriate privilege required to do so. The format of the <i>&lt;value&gt; </i> shall be as described in <code>pax Extended Header File Times</code>.</p>
<dt><code>charset</code></p>
<dd> The name of the character set used to encode the data in the following file(s). The entries in the following table are defined to refer to known standards; additional names may be agreed on between the originator and recipient.</dl>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>&lt;value&gt;</code></td>
<td ALIGN=center><code>Formal Standard</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 646 1990</td>
<td>ISO/IEC 646:1990
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 1 1998</td>
<td>ISO/IEC 8859-1:1998
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 2 1999</td>
<td>ISO/IEC 8859-2:1999
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 3 1999</td>
<td>ISO/IEC 8859-3:1999
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 4 1998</td>
<td>ISO/IEC 8859-4:1998
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 5 1999</td>
<td>ISO/IEC 8859-5:1999
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 6 1999</td>
<td>ISO/IEC 8859-6:1999
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 7 1987</td>
<td>ISO/IEC 8859-7:1987
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 8 1999</td>
<td>ISO/IEC 8859-8:1999
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 9 1999</td>
<td>ISO/IEC 8859-9:1999
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 10 1998</td>
<td>ISO/IEC 8859-10:1998
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 13 1998</td>
<td>ISO/IEC 8859-13:1998
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 14 1998</td>
<td>ISO/IEC 8859-14:1998
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 8859 15 1999</td>
<td>ISO/IEC 8859-15:1999
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 10646 2000</td>
<td>ISO/IEC 10646:2000
</td>
</tr>
<tr VALIGN=top>
<td>ISO-IR 10646 2000 UTF-8</td>
<td>ISO/IEC 10646, UTF-8 encoding
</td>
</tr>
<tr VALIGN=top>
<td>BINARY</td>
<td>None
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The encoding is included in an extended header for information only; when <code>pax </code> is used as described in IEEE Std 1003.1-2001, it shall not translate the file data into any other encoding. The <code>BINARY </code> entry indicates unencoded binary data. </p>
<p> When used in <code>write</code> or <code>copy </code> mode, it is implementation-defined whether <code>pax </code> includes a charset extended header record for a file.</p>
<dl>
<dt><code>comment</code></p>
<dd> A series of characters used as a comment. All characters in the <i>&lt;value&gt; </i> field shall be ignored by <code>pax</code>.</p>
<dt><code>gid</code></p>
<dd> The group ID of the group that owns the file, expressed as a decimal number using digits from the ISO/IEC 646:1991 standard. This record shall override the <i>gid </i> field in the following header block(s). When used in <code>write </code> or <code>copy </code> mode, <code>pax </code> shall include a gid extended header record for each file whose group ID is greater than 2097151 (octal 7777777).</p>
<dt><code>gname</code></p>
<dd> The group of the file(s), formatted as a group name in the group database. This record shall override the <code>gid </code> and <code>gname</code> fields in the following header block(s), and any <code>gid </code> extended header record. When used in <code>read</code>, <code>copy</code>, or <code>list </code> mode, <code>pax</code> shall translate the name from the UTF-8 encoding in the header record to the character set appropriate for the group database on the receiving system. If any of the UTF-8 characters cannot be translated, and if the <code>-o invalid=</code>UTF-8 option is not specified, the results are implementation-defined. When used in <code>write </code> or <code>copy </code> mode, <code>pax</code> shall include a <code>gname </code> extended header record for each file whose group name cannot be represented entirely with the letters and digits of the portable character set.</p>
<dt><code>linkpath</code></p>
<dd> The pathname of a link being created to another file, of any type, previously archived. This record shall override the <i>linkname </i> field in the following <code>ustar </code> header block(s). The following <code>ustar </code> header block shall determine the type of link created. If <i>typeflag </i> of the following header block is 1, it shall be a hard link. If <i>typeflag </i> is 2, it shall be a symbolic link and the linkpath value shall be the contents of the symbolic link. The <code>pax </code> utility shall translate the name of the link (contents of the symbolic link) from the UTF-8 encoding to the character set appropriate for the local file system. When used in <code>write </code> or <code>copy </code> mode, <code>pax </code> shall include a linkpath extended header record for each link whose pathname cannot be represented entirely with the members of the portable character set other than NUL.</p>
<dt><code>mtime</code></p>
<dd> The file modification time of the following file(s), equivalent to the value of the <i>st_mtime </i> member of the <code>stat</code> structure for a file, as described in the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) function. This record shall override the <i>mtime </i> field in the following header block(s). The modification time shall be restored if the process has the appropriate privilege required to do so. The format of the <i>&lt;value&gt; </i> shall be as described in <code>pax Extended Header File Times</code>.</p>
<dt><code>path</code></p>
<dd> The pathname of the following file(s). This record shall override the <i>name </i> and <i>prefix </i> fields in the following header block(s). The <code>pax </code> utility shall translate the pathname of the file from the UTF-8 encoding to the character set appropriate for the local file system. </p>
<p> When used in <code>write </code> or <code>copy </code> mode, <code>pax </code> shall include a <i>path</i> extended header record for each file whose pathname cannot be represented entirely with the members of the portable character set other than NUL.</p>
<dt><code>realtime.</code><i>any</i></p>
<dd> The keywords prefixed by &quot;realtime.&quot; are reserved for future standardization.</p>
<dt><code>security.</code><i>any</i></p>
<dd> The keywords prefixed by &quot;security.&quot; are reserved for future standardization.</p>
<dt><code>size</code></p>
<dd> The size of the file in octets, expressed as a decimal number using digits from the ISO/IEC 646:1991 standard. This record shall override the <i>size </i> field in the following header block(s). When used in <code>write </code> or <code>copy </code> mode, <code>pax </code> shall include a <i>size </i> extended header record for each file with a size value greater than 8589934591 (octal 77777777777).</p>
<dt><code>uid</code></p>
<dd> The user ID of the file owner, expressed as a decimal number using digits from the ISO/IEC 646:1991 standard. This record shall override the <i>uid </i> field in the following header block(s). When used in <code>write </code> or <code>copy</code> mode, <code>pax </code> shall include a <i>uid </i> extended header record for each file whose owner ID is greater than 2097151 (octal 7777777).</p>
<dt><code>uname</code></p>
<dd> The owner of the following file(s), formatted as a user name in the user database. This record shall override the <i>uid </i> and <i>uname </i> fields in the following header block(s), and any <i>uid</i> extended header record. When used in <code>read</code>, <code>copy</code>, or <code>list</code> mode, <code>pax </code> shall translate the name from the UTF-8 encoding in the header record to the character set appropriate for the user database on the receiving system. If any of the UTF-8 characters cannot be translated, and if the <code>-o invalid=</code>UTF-8 option is not specified, the results are implementation-defined. When used in <code>write </code> or <code>copy </code> mode, <code>pax</code> shall include a <i>uname </i> extended header record for each file whose user name cannot be represented entirely with the letters and digits of the portable character set.</dl>
<p> If the <i>&lt;value&gt; </i> field is zero length, it shall delete any header block field, previously entered extended header value, or global extended header value of the same name. </p>
<p> If a keyword in an extended header record (or in a <code>-o</code> option-argument) overrides or deletes a corresponding field in the <code>ustar </code> header block, <code>pax </code> shall ignore the contents of that header block field. </p>
<p> Unlike the <code>ustar </code> header block fields, NULs shall not delimit <i>&lt;value&gt;</i>s; all characters within the <i>&lt;value&gt; </i> field shall be considered data for the field. None of the length limitations of the <code>ustar </code> header block fields in <code>ustar Header Block </code> shall apply to the extended header records. </p>
<h3>pax Extended Header Keyword Precedence</h3>
<p> This section describes the precedence in which the various header records and fields and command line options are selected to apply to a file in the archive. When <code>pax </code> is used in <code>read </code> or <code>list </code> modes, it shall determine a file attribute in the following sequence:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> If <code>-o delete=</code><i>keyword-prefix</i> is used, the affected attributes shall be determined from step 7., if applicable, or ignored otherwise.</p>
<dt>2.</p>
<dd> If <code>-o </code><i>keyword:=</i> is used, the affected attributes shall be ignored.</p>
<dt>3.</p>
<dd> If <code>-o </code><i>keyword:=value</i> is used, the affected attribute shall be assigned the value.</p>
<dt>4.</p>
<dd> If there is a <i>typeflag </i> <code>x </code> extended header record, the affected attribute shall be assigned the <i>&lt;value&gt;</i>. When extended header records conflict, the last one given in the header shall take precedence.</p>
<dt>5.</p>
<dd> If <code>-o </code><i>keyword=value</i> is used, the affected attribute shall be assigned the value.</p>
<dt>6.</p>
<dd> If there is a <i>typeflag </i> <code>g </code> global extended header record, the affected attribute shall be assigned the <i>&lt;value&gt;</i>. When global extended header records conflict, the last one given in the global header shall take precedence.</p>
<dt>7.</p>
<dd> Otherwise, the attribute shall be determined from the <code>ustar</code> header block.</dl>
</dl>
<h3>pax Extended Header File Times</h3>
<p> The <code>pax </code> utility shall write an <code>mtime </code> record for each file in <code>write</code> or <code>copy </code> modes if the file&#8217;s modification time cannot be represented exactly in the <code>ustar </code> header logical record described in <code>ustar Interchange Format</code>. This can occur if the time is out of <code>ustar </code> range, or if the file system of the underlying implementation supports non-integer time granularities and the time is not an integer. All of these time records shall be formatted as a decimal representation of the time in seconds since the Epoch. If a period (&#8216;.&#8217;) decimal point character is present, the digits to the right of the point shall represent the units of a subsecond timing granularity, where the first digit is tenths of a second and each subsequent digit is a tenth of the previous digit. In <code>read </code> or <code>copy </code> mode, the <code>pax </code> utility shall truncate the time of a file to the greatest value that is not greater than the input header file time. In <code>write </code> or <code>copy </code> mode, the <code>pax </code> utility shall output a time exactly if it can be represented exactly as a decimal number, and otherwise shall generate only enough digits so that the same time shall be recovered if the file is extracted on a system whose underlying implementation supports the same time granularity. </p>
<h3>ustar Interchange Format</h3>
<p> A <code>ustar </code> archive tape or file shall contain a series of logical records. Each logical record shall be a fixed-size logical record of 512 octets (see below). Although this format may be thought of as being stored on 9-track industry-standard 12.7 mm (0.5 in) magnetic tape, other types of transportable media are not excluded. Each file archived shall be represented by a header logical record that describes the file, followed by zero or more logical records that give the contents of the file. At the end of the archive file there shall be two 512-octet logical records filled with binary zeros, interpreted as an end-of-archive indicator. </p>
<p> The logical records may be grouped for physical I/O operations, as described under the <code>-b</code><i> blocksize </i> and <code>-x</code><i> ustar </i> options. Each group of logical records may be written with a single operation equivalent to the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) function. On magnetic tape, the result of this write shall be a single tape physical block. The last physical block shall always be the full size, so logical records after the two zero logical records may contain undefined data. </p>
<p> The header logical record shall be structured as shown in the following table. All lengths and offsets are in decimal. </p>
<p> <center> <code>Table: ustar Header Block</code><br />
 </center> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Field Name</code></td>
<td ALIGN=center><code>Octet Offset</code></td>
<td ALIGN=center><code>Length (in Octets)</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>name</td>
<td ALIGN=right>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>100&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>mode</td>
<td ALIGN=right>100&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>uid</td>
<td ALIGN=right>108&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>gid</td>
<td ALIGN=right>116&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>size</td>
<td ALIGN=right>124&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>mtime</td>
<td ALIGN=right>136&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>chksum</td>
<td ALIGN=right>148&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>typeflag</td>
<td ALIGN=right>156&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>linkname</td>
<td ALIGN=right>157&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>100&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>magic</td>
<td ALIGN=right>257&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>version</td>
<td ALIGN=right>263&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>uname</td>
<td ALIGN=right>265&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>gname</td>
<td ALIGN=right>297&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>devmajor</td>
<td ALIGN=right>329&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>devminor</td>
<td ALIGN=right>337&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>prefix</td>
<td ALIGN=right>345&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>155&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> All characters in the header logical record shall be represented in the coded character set of the ISO/IEC 646:1991 standard. For maximum portability between implementations, names should be selected from characters represented by the portable filename character set as octets with the most significant bit zero. If an implementation supports the use of characters outside of slash and the portable filename character set in names for files, users, and groups, one or more implementation-defined encodings of these characters shall be provided for interchange purposes. </p>
<p> However, the <code>pax </code> utility shall never create filenames on the local system that cannot be accessed via the procedures described in IEEE Std 1003.1-2001. If a filename is found on the medium that would create an invalid filename, it is implementation-defined whether the data from the file is stored on the file hierarchy and under what name it is stored. The <code>pax </code> utility may choose to ignore these files as long as it produces an error indicating that the file is being ignored. </p>
<p> Each field within the header logical record is contiguous; that is, there is no padding used. Each character on the archive medium shall be stored contiguously. </p>
<p> The fields <i>magic</i>, <i>uname</i>, and <i>gname </i> are character strings each terminated by a NUL character. The fields <i>name</i>, <i>linkname</i>, and <i>prefix </i> are NUL-terminated character strings except when all characters in the array contain non-NUL characters including the last character. The <i>version </i> field is two octets containing the characters &quot;00&quot; (zero-zero). The <i>typeflag </i> contains a single character. All other fields are leading zero-filled octal numbers using digits from the ISO/IEC 646:1991 standard IRV. Each numeric field is terminated by one or more &lt;space&gt; or NUL characters. </p>
<p> The <i>name </i> and the <i>prefix </i> fields shall produce the pathname of the file. A new pathname shall be formed, if <i>prefix </i> is not an empty string (its first character is not NUL), by concatenating <i>prefix</i> (up to the first NUL character), a slash character, and <i>name</i>; otherwise, <i>name</i> is used alone. In either case, <i>name </i> is terminated at the first NUL character. If <i>prefix </i> begins with a NUL character, it shall be ignored. In this manner, pathnames of at most 256 characters can be supported. If a pathname does not fit in the space provided, <code>pax </code> shall notify the user of the error, and shall not store any part of the file-header or data-on the medium. </p>
<p> The <i>linkname </i> field, described below, shall not use the <i>prefix </i> to produce a pathname. As such, a <i>linkname </i> is limited to 100 characters. If the name does not fit in the space provided, <code>pax</code> shall notify the user of the error, and shall not attempt to store the link on the medium. </p>
<p> The <i>mode </i> field provides 12 bits encoded in the ISO/IEC 646:1991 standard octal digit representation. The encoded bits shall represent the following values: </p>
<p> <center> <code>Table: ustar mode Field</code><br />
 </center> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Bit</code></td>
<td ALIGN=center><code>IEEE Std</code></td>
<td ALIGN=center><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>Value</code></td>
<td ALIGN=center><code>1003.1-2001 Bit</code></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>04000</td>
<td>S_ISUID</td>
<td>Set UID on execution.
</td>
</tr>
<tr VALIGN=top>
<td>02000</td>
<td>S_ISGID</td>
<td>Set GID on execution.
</td>
</tr>
<tr VALIGN=top>
<td>01000</td>
<td>&lt;reserved&gt;</td>
<td>Reserved for future standardization.
</td>
</tr>
<tr VALIGN=top>
<td>00400</td>
<td>S_IRUSR</td>
<td>Read permission for file owner class.
</td>
</tr>
<tr VALIGN=top>
<td>00200</td>
<td>S_IWUSR</td>
<td>Write permission for file owner class.
</td>
</tr>
<tr VALIGN=top>
<td>00100</td>
<td>S_IXUSR</td>
<td>Execute/search permission for file owner class.
</td>
</tr>
<tr VALIGN=top>
<td>00040</td>
<td>S_IRGRP</td>
<td>Read permission for file group class.
</td>
</tr>
<tr VALIGN=top>
<td>00020</td>
<td>S_IWGRP</td>
<td>Write permission for file group class.
</td>
</tr>
<tr VALIGN=top>
<td>00010</td>
<td>S_IXGRP</td>
<td>Execute/search permission for file group class.
</td>
</tr>
<tr VALIGN=top>
<td>00004</td>
<td>S_IROTH</td>
<td>Read permission for file other class.
</td>
</tr>
<tr VALIGN=top>
<td>00002</td>
<td>S_IWOTH</td>
<td>Write permission for file other class.
</td>
</tr>
<tr VALIGN=top>
<td>00001</td>
<td>S_IXOTH</td>
<td>Execute/search permission for file other class.
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> When appropriate privilege is required to set one of these mode bits, and the user restoring the files from the archive does not have the appropriate privilege, the mode bits for which the user does not have appropriate privilege shall be ignored. Some of the mode bits in the archive format are not mentioned elsewhere in this volume of IEEE Std 1003.1-2001. If the implementation does not support those bits, they may be ignored. </p>
<p> The <i>uid and </i> <i>gid </i> fields are the user and group ID of the owner and group of the file, respectively. </p>
<p> The <i>size </i> field is the size of the file in octets. If the <i>typeflag</i> field is set to specify a file to be of type 1 (a link) or 2 (a symbolic link), the <i>size </i> field shall be specified as zero. If the <i>typeflag </i> field is set to specify a file of type 5 (directory), the size field shall be interpreted as described under the definition of that record type. No data logical records are stored for types 1, 2, or 5. If the typeflag field is set to 3 (character special file), 4 (block special file), or 6 (FIFO), the meaning of the <i>size </i> field is unspecified by this volume of IEEE Std 1003.1-2001, and no data logical records shall be stored on the medium. Additionally, for type 6, the <i>size </i> field shall be ignored when reading. If the <i>typeflag </i> field is set to any other value, the number of logical records written following the header shall be (size+511)/512, ignoring any fraction in the result of the division. </p>
<p> The <i>mtime </i> field shall be the modification time of the file at the time it was archived. It is the ISO/IEC 646:1991 standard representation of the octal value of the modification time obtained from the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) function. </p>
<p> The <i>chksum </i> field shall be the ISO/IEC 646:1991 standard IRV representation of the octal value of the simple sum of all octets in the header logical record. Each octet in the header shall be treated as an unsigned value. These values shall be added to an unsigned integer, initialized to zero, the precision of which is not less than 17 bits. When calculating the checksum, the <i>chksum</i> field is treated as if it were all spaces. </p>
<p> The <i>typeflag </i> field specifies the type of file archived. If a particular implementation does not recognize the type, or the user does not have appropriate privilege to create that type, the file shall be extracted as if it were a regular file if the file type is defined to have a meaning for the <i>size </i> field that could cause data logical records to be written on the medium (see the previous description for <i>size</i>). If conversion to a regular file occurs, the <code>pax </code> utility shall produce an error indicating that the conversion took place. All of the <i>typeflag </i> fields shall be coded in the ISO/IEC 646:1991 standard IRV:</p>
<dl>
<dt><code>0</code></p>
<dd> Represents a regular file. For backwards-compatibility, a <i>typeflag</i> value of binary zero (&#8216;
