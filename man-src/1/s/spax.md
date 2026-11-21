---

title: "spax(1)"
name: "spax"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spax/"
description: "pax – portable archive interchange"
---

<h2>NAME</h2>
<p> pax - portable archive interchange  </p>
<dl>
<dt><code>spax</code></dt>
<dd> <p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<i>other options</i>] [-cdnv] [-H|-L] [-f&nbsp;<wbr><i>archive] [-o options</i>]... [-s <i>replstr]... [pattern</i>...] </p>
 </dd>
<dt><code>spax</code></dt>
<dd> <p> -r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<i>other options</i>] [-cdiknuv] [-H|-L] [-f&nbsp;<wbr><i>archive] [-o options</i>]... [-p&nbsp;<wbr><i>string</i>]... [-s&nbsp;<wbr><i>replstr</i>]... [<i>pattern...] </p>
 </dd>
<dt></i><code>spax</code></dt>
<dd> <p> -w&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<i>other options</i>] [-dituvX] [-H|-L] [-b&nbsp;<wbr><i>blocksize</i>] [-a] [-f&nbsp;<wbr><i>archive] [-o options</i>]... [-s&nbsp;<wbr><i>replstr</i>]... [-x&nbsp;<wbr><i>format</i>] [<i>file</i>...] </p>
 </dd>
<dt><code>spax</code></dt>
<dd> <p> -r -w[<i>other options</i>] [-diklntuvX] [-H|-L] [-o&nbsp;<wbr><i>options</i>]... [-p&nbsp;<wbr><i>string</i>]... [-s&nbsp;<wbr><i>replstr</i>]... [<i>file</i>...] <i>directory</i> </p>
 </dd></dl>
<p> The <code>pax </code> utility shall read, write, and write lists of the members of archive files and copy directory hierarchies. A variety of archive formats shall be supported; see the <code>-x</code> format option. </p>
<p> The action to be taken depends on the presence of the <code>-r</code> and <code>-w</code> options. The four combinations of <code>-r</code> and <code>-w</code> are referred to as the four modes of operation: <code>list</code>, <code>read</code>, <code>write</code>, and <code>copy</code> modes, corresponding respectively to the four forms shown in the SYNOPSIS section. </p>
<dl>
<dt><code>list</code></dt>
<dd> <p> In <code>list</code> mode (when neither <code>-r</code> nor <code>-w</code> are specified), <code>pax</code> shall write the names of the members of the archive file read from the standard input, with pathnames matching the specified <i>patterns</i>, to standard output. If a named file is of type directory, the file hierarchy rooted at that file shall be listed as well. </p>
 </dd>
<dt><code>read</code></dt>
<dd> <p> In <code>read</code> mode (when <code>-r</code> is specified, but <code>-w</code> is not), <code>pax</code> shall extract the members of the archive file read from the standard input, with pathnames matching the specified <i>patterns</i>. If an extracted file is of type directory, the file hierarchy rooted at that file shall be extracted as well. The extracted files shall be created performing pathname resolution with the directory in which <code>pax</code> was invoked as the current working directory. </p>
<p> If an attempt is made to extract a directory when the directory already exists, this shall not be considered an error. If an attempt is made to extract a FIFO when the FIFO already exists, this shall not be considered an error. </p>
<p> The ownership, access, and modification times, and file mode of the restored files are discussed under the <code>-p</code> option. </p>
 </dd>
<dt><code>write</code></dt>
<dd> <p> In <code>write</code> mode (when <code>-w</code> is specified, but <code>-r</code> is not), <code>pax</code> shall write the contents of the file operands to the standard output in an archive format. If no file operands are specified, a list of files to copy, one per line, shall be read from the standard input. A file of type directory shall include all of the files in the file hierarchy rooted at the file. </p>
 </dd>
<dt><code>copy</code></dt>
<dd> <p> In <code>copy</code> mode (when both <code>-r</code> and <code>-w</code> are specified), <code>pax</code> shall copy the file operands to the destination directory. </p>
<p> If no file operands are specified, a list of files to copy, one per line, shall be read from the standard input. A file of type directory shall include all of the files in the file hierarchy rooted at the file. </p>
<p> The effect of the <code>copy</code> shall be as if the copied files were written to an archive file and then subsequently extracted, except that there may be hard links between the original and the copied files. If the destination directory is a subdirectory of one of the files to be copied, the results are unspecified. If the destination directory is a file of a type not defined by the System Interfaces volume of IEEE Std 1003.1-2001, the results are implementation-defined; otherwise, it shall be an error for the file named by the directory operand not to exist, not be writable by the user, or not be a file of type directory. </p>
 </dd></dl>
<p> In <code>read</code> or <code>copy</code> modes, if intermediate directories are necessary to extract an archive member, <code>pax </code> shall perform actions equivalent to the <code>mkdir</code>() function defined in the System Interfaces volume of IEEE Std 1003.1-2001, called with the following arguments: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> The intermediate directory used as the <code>path</code> argument. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> The value of the bitwise-inclusive <code>OR </code> of <code>S_IRWXU</code>, <code>S_IRWXG</code>, and <code>S_IRWXO</code> as the <i>mode</i> argument. </p>
 </dd></dl>
<p> If any specified <i>pattern</i> or <i>file</i> operands are not matched by at least one file or archive member, <code>pax </code> shall write a diagnostic message to standard error for each one that did not match and exit with a non-zero exit status. </p>
<p> The archive formats described in the <code>EXTENDED DESCRIPTION</code> section shall be automatically detected on input. The default output archive format shall be implementation-defined. </p>
<p> The <code>spax</code> implementation defaults to <code>-x ustar</code>. </p>
<p> A single archive can span multiple files. The <code>pax</code> utility shall determine, in an implementation-defined manner, what file to read or write as the next file. </p>
<p> If the selected archive format supports the specification of linked files, it shall be an error if these files cannot be linked when the archive is extracted, except that if the files to be linked are symbolic links and the system is not capable of making hard links to symbolic links, then separate copies of the symbolic link shall be created instead. For archive formats that do not store file contents with each name that causes a hard link, if the file that contains the data is not extracted during this <code>pax</code> session, either the data shall be restored from the original file, or a diagnostic message shall be displayed with the name of a file that can be used to extract the data. In traversing directories, <code>pax</code> shall detect infinite loops; that is, entering a previously visited directory that is an ancestor of the last file visited. When it detects an infinite loop, <code>pax</code> shall write a diagnostic message to standard error and shall terminate. </p>
<h2>OPTIONS</h2>
<p> The <code>pax</code> utility shall conform to the Base Definitions volume of IEEE Std 1003.1-2001, Section 12.2, Utility Syntax Guidelines, except that the order of presentation of the <code>-o</code>, <code>-p</code>, and <code>-s</code> options is significant. </p>
<p> See also the &quot;OTHER OPTIONS&quot; section. </p>
<p> The following options shall be supported: </p>
<dl>
<dt><code>-r</code></dt>
<dd> <p> Read an archive file from standard input. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Write files to the standard output in the specified archive format. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Append files to the end of the archive. It is implementation-defined which devices on the system support appending. Additional file formats unspecified by this volume of IEEE Std 1003.1-2001 may impose restrictions on appending. </p>
 </dd>
<dt><code>-b</code><i> blocksize</i></dt>
<dd> <p> Block the output at a positive decimal integer number of bytes per write to the archive file. Devices and archive formats may impose restrictions on blocking. Blocking shall be automatically determined on input. Conforming applications shall not specify a blocksize value larger than 32256. Default blocking when creating archives depends on the archive format. (See the <code>-x </code> option below.) </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Match all file or archive members except those specified by the pattern or file operands. </p>
 </dd>
<dt><code>-d</code></dt>
<dd> <p> Cause files of type directory being copied or archived or archive members of type directory being extracted or listed to match only the file or archive member itself and not the file hierarchy rooted at the file. </p>
 </dd>
<dt><code>-f</code><i> archive</i></dt>
<dd> <p> Specify the pathname of the input or output archive, overriding the default standard input (in <code>list</code> or <code>read</code> modes) or standard output (<code>write</code> mode). </p>
 </dd>
<dt><code>-H</code></dt>
<dd> <p> If a symbolic link referencing a file of type directory is specified on the command line, <code>pax </code> shall archive the file hierarchy rooted in the file referenced by the link, using the name of the link as the root of the file hierarchy. Otherwise, if a symbolic link referencing a file of any other file type which <code>pax </code> can normally archive is specified on the command line, then <code>pax </code> shall archive the file referenced by the link, using the name of the link. The default behavior shall be to archive the symbolic link itself. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> Interactively rename files or archive members. For each archive member matching a pattern operand or file matching a file operand, a prompt shall be written to the file /dev/tty. The prompt shall contain the name of the file or archive member, but the format is otherwise unspecified. A line shall then be read from /dev/tty. If this line is blank, the file or archive member shall be skipped. If this line consists of a single period, the file or archive member shall be processed with no modification to its name. Otherwise, its name shall be replaced with the contents of the line. The <code>pax</code> utility shall immediately exit with a non-zero exit status if end-of-file is encountered when reading a response or if /dev/tty cannot be opened for reading and writing. </p>
<p> The results of extracting a hard link to a file that has been renamed during extraction are unspecified. </p>
 </dd>
<dt><code>-k</code></dt>
<dd> <p> Prevent the overwriting of existing files. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> (The letter ell.) In copy mode, hard links shall be made between the source and destination file hierarchies whenever possible. If specified in conjunction with <code>-H </code> or <code>-L</code>, when a symbolic link is encountered, the hard link created in the destination file hierarchy shall be to the file referenced by the symbolic link. If specified when neither <code>-H </code> nor <code>-L </code> is specified, when a symbolic link is encountered, the implementation shall create a hard link to the symbolic link in the source file hierarchy or copy the symbolic link to the destination. </p>
 </dd>
<dt><code>-L</code></dt>
<dd> <p> If a symbolic link referencing a file of type directory is specified on the command line or encountered during the traversal of a file hierarchy, <code>pax </code> shall archive the file hierarchy rooted in the file referenced by the link, using the name of the link as the root of the file hierarchy. Otherwise, if a symbolic link referencing a file of any other file type which <code>pax </code> can normally archive is specified on the command line or encountered during the traversal of a file hierarchy, <code>pax </code> shall archive the file referenced by the link, using the name of the link. The default behavior shall be to archive the symbolic link itself. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Select the first archive member that matches each pattern operand. No more than one archive member shall be matched for each pattern (although members of type directory shall still match the file hierarchy rooted at that file). </p>
 </dd>
<dt><code>-o</code><i> options</i></dt>
<dd> <p> Provide information to the implementation to modify the algorithm for extracting or writing files. The value of options shall consist of one or more comma-separated keywords of the form: </p>
 </dd>
<dl>
<dd> <p> <code>keyword[[:]=</code><i>value</i><code>][,keyword[[:]=</code><i>value</i><code>],</code><i>...]</i> </p>
<p> Some keywords apply only to certain file formats, as indicated with each description. Use of keywords that are inapplicable to the file format being processed produces undefined results. </p>
<p> Keywords in the options argument shall be a string that would be a valid portable filename as described in the Base Definitions volume of IEEE Std 1003.1-2001, Section 3.276, Portable Filename Character Set. </p>
 </dd>
<dl>
<dt><code>Note:</code></dt>
<dd> <p> Keywords are not expected to be filenames, merely to follow the same character composition rules as portable filenames. </p>
 </dd></dl>
<p> Keywords can be preceded with white space. The value field shall consist of zero or more characters; within value, the application shall precede any literal comma with a backslash, which shall be ignored, but preserves the comma as part of value. A comma as the final character, or a comma followed solely by white space as the final characters, in options shall be ignored. Multiple <code>-o </code> options can be specified; if keywords given to these multiple <code>-o </code> options conflict, the keywords and values appearing later in command line sequence shall take precedence and the earlier shall be silently ignored. The following keyword values of options shall be supported for the file formats as indicated: </p>
<dl>
<dt><code>delete=</code><i>pattern</i></dt>
<dd> <p> (Applicable only to the <code>-x pax </code> format.) When used in write or copy mode, <code>pax </code> shall omit from extended header records that it produces any keywords matching the string pattern. When used in read or list mode, <code>pax</code> shall ignore any keywords matching the string pattern in the extended header records. In both cases, matching shall be performed using the pattern matching notation described in Patterns Matching a Single Character and Patterns Matching Multiple Characters. For example: </p>
 </dd>
<dl>
<dd> <p> <code>-o delete=</code><i>security.*</i> </p>
<p> would suppress security-related information. See <code>pax Extended Header </code> for extended header record keyword usage. </p>
<p> When multiple <code>-o delete=</code><i>pattern</i> options are specified, the patterns shall be additive; all keywords matching the specified string patterns shall be omitted from extended header records that <code>pax </code> produces. </p>
 </dd></dl>
<dt><code>exthdr.name=</code><i>string</i></dt>
<dd> <p> (Applicable only to the <code>-x pax </code> format.) This keyword allows user control over the name that is written into the ustar header blocks for the extended header produced under the circumstances described in <code>pax Header Block.</code> The name shall be the contents of string, after the following character substitutions have been made: </p>
 </dd>
<dl>
<dd> <p> <center> </p>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td><code>string Includes:</code></td>
<td><code>Replaced By:</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<td><hr />
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
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>%p</td>
<td>The process ID of the pax process.
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>%%</td>
<td>A &#8216;%&#8216; character.
</td>
</tr>
</table>
</table>
<p> </center> </p>
<p> Any other &#8216;%&#8216; characters in string produce undefined results. </p>
<p> If no -o exthdr.name= string is specified, <code>pax </code> shall use the following default value: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>%d/PaxHeaders.%p/%f </p>
 </dd></dl>
<dt><code>globexthdr.name=</code><i>string</i></dt>
<dd> <p> (Applicable only to the <code>-x pax </code> format.) When used in write or copy mode with the appropriate options, <code>pax</code> shall create global extended header records with ustar header blocks that will be treated as regular files by previous versions of <code>pax</code>. This keyword allows user control over the name that is written into the ustar header blocks for global extended header records. The name shall be the contents of string, after the following character substitutions have been made: </p>
 </dd>
<dl>
<dd> <p> <center> </p>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td><code>string Includes:</code></td>
<td><code>Replaced By:</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>%p</td>
<td>The process ID of the pax process.
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>%%</td>
<td>A &#8216;%&#8216; character.
</td>
</tr>
</table>
</table>
<p> </center> </p>
<p> Any other &#8216;%&#8216; characters in string produce undefined results. </p>
<p> If no <code>-o globexthdr.name=</code><i>string</i> is specified, <code>pax </code> shall use the following default value: </p>
<p> $TMPDIR/GlobalHead.%p.%n </p>
<p> where <code>$TMPDIR </code> represents the value of the <code>TMPDIR</code> environment variable. If <code>TMPDIR </code> is not set, <code>pax </code> shall use /tmp. </p>
 </dd></dl>
<dt><code>invalid=</code><i>action</i></dt>
<dd> <p> (Applicable only to the <code>-x pax </code> format.) This keyword allows user control over the action <code>pax </code> takes upon encountering values in an extended header record that, in read or copy mode, are invalid in the destination hierarchy or, in list mode, cannot be written in the codeset and current locale of the implementation. The following are invalid values that shall be recognized by <code>pax</code>: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>+</code></dt>
<dd> <p> In read or copy mode, a filename or link name that contains character encodings invalid in the destination hierarchy. (For example, the name may contain embedded NULs.) </p>
 </dd>
<dt><code>+</code></dt>
<dd> <p> In read or copy mode, a filename or link name that is longer than the maximum allowed in the destination hierarchy (for either a pathname component or the entire pathname). </p>
 </dd>
<dt><code>+</code></dt>
<dd> <p> In list mode, any character string value (filename, link name, user name, and so on) that cannot be written in the codeset and current locale of the implementation. </p>
 </dd></dl>
<p> The following mutually-exclusive values of the action argument are supported: </p>
<dl>
<dt><code>bypass</code></dt>
<dd> <p> In read or copy mode, <code>pax </code> shall bypass the file, causing no change to the destination hierarchy. In list mode, <code>pax </code> shall write all requested valid values for the file, but its method for writing invalid values is unspecified. </p>
 </dd>
<dt><code>rename</code></dt>
<dd> <p> In read or copy mode, <code>pax </code> shall act as if the <code>-i</code> option were in effect for each file with invalid filename or link name values, allowing the user to provide a replacement name interactively. In list mode, <code>pax </code> shall behave identically to the bypass action. </p>
 </dd>
<dt><code>UTF-8</code></dt>
<dd> <p> When used in read, copy, or list mode and a filename, link name, owner name, or any other field in an extended header record cannot be translated from the <code>pax </code> UTF-8 codeset format to the codeset and current locale of the implementation, <code>pax </code> shall use the actual UTF-8 encoding for the name. </p>
 </dd>
<dt><code>write</code></dt>
<dd> <p> In read or copy mode, <code>pax </code> shall write the file, translating the name, regardless of whether this may overwrite an existing file with a valid name. In list mode, <code>pax </code> shall behave identically to the bypass action. </p>
 </dd></dl>
<p> If no <code>-o invalid=</code><i>option</i> is specified, <code>pax </code> shall act as if <code>-o invalid= bypass </code> were specified. Any overwriting of existing files that may be allowed by the <code>-o invalid=</code> actions shall be subject to permission(<code>-p</code>) and modification time (<code>-u</code>) restrictions, and shall be suppressed if the <code>-k </code> option is also specified. </dl>
 </p>
<dt><code>linkdata</code></dt>
<dd> <p> (Applicable only to the <code>-x pax </code> format.) In write mode, <code>pax </code> shall write the contents of a file to the archive even when that file is merely a hard link to a file whose contents have already been written to the archive. </p>
 </dd>
<dt><code>listopt=</code><i>format</i></dt>
<dd> <p> This keyword specifies the output format of the table of contents produced when the <code>-v </code> option is specified in list mode. See List Mode Format Specifications. To avoid ambiguity, the listopt= format shall be the only or final keyword= value pair in a <code>-o </code><i>option-argument</i>; all characters in the remainder of the option-argument shall be considered part of the format string. When multiple -o listopt= format options are specified, the format strings shall be considered a single, concatenated string, evaluated in command line order. </p>
 </dd>
<dt><code>times</code></dt>
<dd> <p> (Applicable only to the <code>-x pax </code> format.) When used in write or copy mode, <code>pax </code> shall include atime and mtime extended header records for each file. See <code>pax Extended Header File Times</code>. </p>
 </dd></dl>
<p> In addition to these keywords, if the <code>-x pax </code> format is specified, any of the keywords and values defined in <code>pax Extended Header</code>, including implementation extensions, can be used in <code>-o</code><i> option-arguments</i>, in either of two modes: </p>
<dl>
<dt><code>keyword=</code><i>value</i></dt>
<dd> <p> When used in write or copy mode, these keyword/value pairs shall be included at the beginning of the archive as typeflag g global extended header records. When used in read or list mode, these keyword/value pairs shall act as if they had been at the beginning of the archive as typeflag g global extended header records. </p>
 </dd>
<dt><code>keyword:=</code><i>value</i></dt>
<dd> <p> When used in write or copy mode, these keyword/value pairs shall be included as records at the beginning of a typeflag x extended header for each file. (This shall be equivalent to the equal-sign form except that it creates no typeflag g global extended header records.) When used in read or list mode, these keyword/value pairs shall act as if they were included as records at the end of each extended header; thus, they shall override any global or file-specific extended header record keywords of the same names. For example, in the command: </p>
 </dd>
<dl>
<dd> <p> <code>pax -r -o &quot;gname:=mygroup,&quot; &lt;archive</code> </p>
<p> the group name will be forced to a new value for all files read from the archive. </p>
 </dd></dl>
</dl>
<p> The precedence of <code>-o</code> keywords over various fields in the archive is described in <code>pax Extended Header Keyword Precedence</code>. </dl>
 </p>
<dt><code>-p</code><i> string</i></dt>
<dd> <p> Specify one or more file characteristic options (privileges). The string option-argument shall be a string specifying file characteristics to be retained or discarded on extraction. The string shall consist of the specification characters a , e, m, o, and p. Other implementation-defined characters can be included. Multiple characteristics can be concatenated within the same string and multiple <code>-p </code> options can be specified. The meaning of the specification characters are as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>a</code></dt>
<dd> <p> Do not preserve file access times. </p>
 </dd>
<dt><code>e</code></dt>
<dd> <p> Preserve the user ID, group ID, file mode bits (see the Base Definitions volume of IEEE Std 1003.1-2001, Section 3.168, File Mode Bits), access time, modification time, and any other implementation-defined file characteristics. </p>
 </dd>
<dt><code>m</code></dt>
<dd> <p> Do not preserve file modification times. </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> Preserve the user ID and group ID. </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> Preserve the file mode bits. Other implementation-defined file mode attributes may be preserved. </p>
 </dd></dl>
<p> In the preceding list, &quot;preserve&quot; indicates that an attribute stored in the archive shall be given to the extracted file, subject to the permissions of the invoking process. The access and modification times of the file shall be preserved unless otherwise specified with the <code>-p </code> option or not stored in the archive. All attributes that are not preserved shall be determined as part of the normal file creation action (see File Read, Write, and Creation). </p>
<p> If neither the e nor the o specification character is specified, or the user ID and group ID are not preserved for any reason, <code>pax </code> shall not set the S_ISUID and S_ISGID bits of the file mode. </p>
<p> If the preservation of any of these items fails for any reason, <code>pax </code> shall write a diagnostic message to standard error. Failure to preserve these items shall affect the final exit status, but shall not cause the extracted file to be deleted. </p>
<p> If file characteristic letters in any of the string option-arguments are duplicated or conflict with each other, the ones given last shall take precedence. For example, if <code>-p eme</code> is specified, file modification times are preserved. </dl>
 </p>
<dt><code>-s</code><i> replstr</i></dt>
<dd> <p> Modify file or archive member names named by pattern or file operands according to the substitution expression replstr, using the syntax of the ed utility. The concepts of &quot;address&quot; and &quot;line&quot; are meaningless in the context of the <code>pax </code> utility, and shall not be supplied. The format shall be: </p>
 </dd>
<dl>
<dd> <p> <code>-s /old/new/[gp]</code> </p>
<p> where as in ed, old is a basic regular expression and new can contain an ampersand, &#8216;\n&#8217; (where n is a digit) backreferences, or subexpression matching. The old string shall also be permitted to contain &lt;newline&gt;s. </p>
<p> Any non-null character can be used as a delimiter ( &#8216;/&#8216; shown here). Multiple <code>-s </code> expressions can be specified; the expressions shall be applied in the order specified, terminating with the first successful substitution. The optional trailing &#8216;g&#8217; is as defined in the ed utility. The optional trailing &#8216;p&#8217; shall cause successful substitutions to be written to standard error. File or archive member names that substitute to the empty string shall be ignored when reading and writing archives. </p>
 </dd></dl>
<dt><code>-t</code></dt>
<dd> <p> When reading files from the file system, and if the user has the permissions required by utime() to do so, set the access time of each file read to the access time that it had before being read by <code>pax</code>. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Ignore files that are older (having a less recent file modification time) than a pre-existing file or archive member with the same name. In read mode, an archive member with the same name as a file in the file system shall be extracted if the archive member is newer than the file. In write mode, an archive file member with the same name as a file in the file system shall be superseded if the file is newer than the archive member. If <code>-a </code> is also specified, this is accomplished by appending to the archive; otherwise, it is unspecified whether this is accomplished by actual replacement in the archive or by appending to the archive. In copy mode, the file in the destination hierarchy shall be replaced by the file in the source hierarchy or by a link to the file in the source hierarchy if the file in the source hierarchy is newer. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> In list mode, produce a verbose table of contents (see the STDOUT section). Otherwise, write archive member pathnames to standard error (see the STDERR section). </p>
 </dd>
<dt><code>-x</code><i> format</i></dt>
<dd> <p> Specify the output archive format. The <code>pax </code> utility shall support the following formats: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>cpio</code></dt>
<dd> <p> The cpio interchange format; see the EXTENDED DESCRIPTION section. The default blocksize for this format for character special archive files shall be 5120. Implementations shall support all blocksize values less than or equal to 32256 that are multiples of 512. </p>
 </dd>
<dt><code>pax</code></dt>
<dd> <p> The <code>pax</code> interchange format; see the <code>EXTENDED DESCRIPTION</code> section. The default blocksize for this format for character special archive files shall be 5120. Implementations shall support all blocksize values less than or equal to 32256 that are multiples of 512. </p>
 </dd>
<dt><code>ustar</code></dt>
<dd> <p> The tar interchange format; see the EXTENDED DESCRIPTION section. The default blocksize for this format for character special archive files shall be 10240. Implementations shall support all blocksize values less than or equal to 32256 that are multiples of 512. </p>
 </dd></dl>
<p> Implementation-defined formats shall specify a default block size as well as any other block sizes supported for character special archive files. </p>
<p> Any attempt to append to an archive file in a format different from the existing archive format shall cause <code>pax </code> to exit immediately with a non-zero exit status. </p>
<p> In copy mode, if no <code>-x </code> format is specified, <code>pax </code> shall behave as if <code>-x pax</code> were specified. </dl>
 </p>
<dt><code>-X</code></dt>
<dd> <p> When traversing the file hierarchy specified by a pathname, <code>pax </code> shall not descend into directories that have a different device ID ( st_dev; see the System Interfaces volume of IEEE Std 1003.1-2001, stat()). </p>
 </dd></dl>
<p> Specifying more than one of the mutually-exclusive options <code>-H </code> and <code>-L </code> shall not be considered an error and the last option specified shall determine the behavior of the utility. </p>
<p> The options that operate on the names of files or archive members (<code>-c</code>, <code>-i</code>, <code>-n</code>, <code>-s</code>, <code>-u</code>, and <code>-v</code>) shall interact as follows. In read mode, the archive members shall be selected based on the user-specified pattern operands as modified by the <code>-c</code>, <code>-n</code>, and <code>-u</code> options. Then, any <code>-s </code> and <code>-i </code> options shall modify, in that order, the names of the selected files. The <code>-v</code> option shall write names resulting from these modifications. </p>
<p> In write mode, the files shall be selected based on the user-specified pathnames as modified by the <code>-n </code> and <code>-u options.</code> Then, any <code>-s </code> and <code>-i </code> options shall modify, in that order, the names of these selected files. The <code>-v </code> option shall write names resulting from these modifications. </p>
<p> If both the <code>-u </code> and <code>-n </code> options are specified, <code>pax </code> shall not consider a file selected unless it is newer than the file to which it is compared. </p>
<h3>List Mode Format Specifications</h3>
<p> The manual page for <code>spax</code> is not yet ready. The following text is a quotation from the POSIX.1-2001 standard. </p>
<p> In <code>list</code> mode with the <code>-o listopt=</code><i>format</i> option, the <i>format</i> argument shall be applied for each selected file. The <code>pax </code> utility shall append a &lt;newline&gt; to the <code>listopt</code> output for each selected file. The <i>format</i> argument shall be used as the <i>format</i> string described in the Base Definitions volume of IEEE Std 1003.1-2001, Chapter 5, File Format Notation, with the exceptions 1. through 5. defined in the EXTENDED DESCRIPTION section of <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), plus the following exceptions: </p>
<dl>
<dt><code>6.</code></dt>
<dd> <p> The sequence (<i>keyword</i>) can occur before a format conversion specifier. The conversion argument is defined by the value of <i>keyword</i>. The implementation shall support the following <i>keywords</i>: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> Any of the Field Name entries in ustar Header Block and Octet-Oriented cpio Archive Entry. The implementation may support the <i>cpio</i> keywords without the leading <code>c_</code> in addition to the form required by Values for <code>cpio</code> <code>c_mode</code> Field. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Any keyword defined for the extended header in <code>pax Extended Header</code>. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Any keyword provided as an implementation-defined extension within the extended header defined in <code>pax Extended Header</code>. </p>
 </dd></dl>
<p> For example, the sequence &quot;%(charset)s&quot; is the string value of the name of the character set in the extended header. </p>
<p> The result of the keyword conversion argument shall be the value from the applicable header field or extended header, without any trailing NULs. </p>
<p> All keyword values used as conversion arguments shall be translated from the UTF-8 encoding to the character set appropriate for the local file system, user database, and so on, as applicable. </dl>
 </p>
<dt><code>7.</code></dt>
<dd> <p> An additional conversion specifier character, <code>T</code>, shall be used to specify time formats. The <code>T</code> conversion specifier character can be preceded by the sequence (<code>keyword=</code><i>subformat</i>), where <i>subformat</i> is a date format as defined by date operands. The default <i>keyword</i> shall be <code>mtime </code> and the default subformat shall be: </p>
 </dd></dl>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%b&nbsp;<wbr>%e&nbsp;<wbr>%H:%M&nbsp;<wbr>%Y </p>
<dl>
<dt><code>8.</code></dt>
<dd> <p> An additional conversion specifier character, <code>M</code>, shall be used to specify the file mode string as defined in <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) Standard Output. If (<i>keyword</i>) is omitted, the <code>mode </code> <i>keyword</i> shall be used. For example, <code>%.1M</code> writes the single character corresponding to the <i>&lt;entry type&gt;</i> field of the <code>ls -l</code> command. </p>
 </dd>
<dt><code>9.</code></dt>
<dd> <p> An additional conversion specifier character, <code>D</code>, shall be used to specify the device for block or special files, if applicable, in an implementation-defined format. If not applicable, and (<i>keyword</i>) is specified, then this conversion shall be equivalent to <code>%(keyword)u</code>. If not applicable, and (<i>keyword</i>) is omitted, then this conversion shall be equivalent to &lt;space&gt;. </p>
 </dd>
<dt><code>10.</code></dt>
<dd> <p> An additional conversion specifier character, <code>F</code>, shall be used to specify a pathname. The <code>F</code> conversion character can be preceded by a sequence of comma-separated keywords: </p>
 </dd></dl>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(keyword[,keyword]&nbsp;<wbr>...&nbsp;<wbr>) </p>
<dl>
<dd> <p> The values for all the keywords that are non-null shall be concatenated together, each separated by a &#8216;/&#8216;. The default shall be (<code>path</code>) if the keyword path is defined; otherwise, the default shall be (<code>prefix, name</code>). </p>
 </dd></dl>
<dl>
<dt><code>11. </code></dt>
<dd> <p> An additional conversion specifier character, <code>L</code>, shall be used to specify a symbolic line expansion. If the current file is a symbolic link, then <code>%L</code> shall expand to: </p>
 </dd></dl>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;%s -&gt;&nbsp;<wbr>%s&quot;,&nbsp;<wbr>&lt;value of keyword&gt;,&nbsp;<wbr>&lt;contents of link&gt; </p>
<p> Otherwise, the <code>%L</code> conversion specification shall be the equivalent of <code>%F</code>. </p>
<h2>OPERANDS</h2>
<p> The following operands shall be supported: </p>
<dl>
<dt><i>directory</i></dt>
<dd> <p> The destination directory pathname for copy mode. </p>
 </dd>
<dt><i>file</i></dt>
<dd> <p> A pathname of a file to be copied or archived. </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> A pattern matching one or more pathnames of archive members. A pattern must be given in the name-generating notation of the pattern matching notation in Pattern Matching Notation , including the filename expansion rules in Patterns Used for Filename Expansion. The default, if no pattern is specified, is to select all members in the archive. </p>
 </dd></dl>
<h2>STDIN</h2>
<p> In <code>write</code> mode, the standard input shall be used only if no <i>file</i> operands are specified. It shall be a text file containing a list of pathnames, one per line, without leading or trailing &lt;blank&gt;s. </p>
<p> In <code>list</code> and <code>read</code> modes, if <code>-f</code> is not specified, the standard input shall be an archive file. </p>
<p> Otherwise, the standard input shall not be used. </p>
<h2>INPUT FILES</h2>
<p> The input file named by the <i>archive </i> option-argument, or standard input when the archive is read from there, shall be a file formatted according to one of the specifications in the EXTENDED DESCRIPTION section or some other implementation-defined format. </p>
<p> The file <code>/dev/tty</code> shall be used to write prompts and read responses. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables shall affect the execution of <code>pax</code>: </p>
<dl>
<dt><code>LANG</code></dt>
<dd> <p> Provide a default value for the internationalization variables that are unset or null. (See the Base Definitions volume of IEEE Std 1003.1-2001, Section 8.2, Internationalization Variables for the precedence of internationalization variables used to determine the values of locale categories.) </p>
 </dd>
<dt><code>LC_ALL</code></dt>
<dd> <p> If set to a non-empty string value, override the values of all the other internationalization variables. </p>
 </dd>
<dt><code>LC_COLLATE</code></dt>
<dd> <p> Determine the locale for the behavior of ranges, equivalence classes, and multi-character collating elements used in the pattern matching expressions for the pattern operand, the basic regular expression for the <code>-s</code> option, and the extended regular expression defined for the <code>yesexpr</code> locale keyword in the LC_MESSAGES category. </p>
 </dd>
<dt><code>LC_CTYPE</code></dt>
<dd> <p> Determine the locale for the interpretation of sequences of bytes of text data as characters (for example, single-byte as opposed to multi-byte characters in arguments and input files), the behavior of character classes used in the extended regular expression defined for the <code>yesexpr</code> locale keyword in the LC_MESSAGES category, and pattern matching. </p>
 </dd>
<dt><code>LC_MESSAGES</code></dt>
<dd> <p> Determine the locale for the processing of affirmative responses that should be used to affect the format and contents of diagnostic messages written to standard error. </p>
 </dd>
<dt><code>LC_TIME</code></dt>
<dd> <p> Determine the format and contents of date and time strings when the <code>-v </code> option is specified. </p>
 </dd>
<dt><code>NLSPATH</code></dt>
<dd> <p> [XSI] [Option Start] Determine the location of message catalogs for the processing of LC_MESSAGES . [Option End] </p>
 </dd>
<dt><code>TMPDIR</code></dt>
<dd> <p> Determine the pathname that provides part of the default global extended header record file, as described for the <code>-o globexthdr=</code> keyword in the OPTIONS section. </p>
 </dd>
<dt><code>TZ</code></dt>
<dd> <p> Determine the timezone used to calculate date and time strings when the <code>-v </code> option is specified. If TZ is unset or null, an unspecified default timezone shall be used. </p>
 </dd></dl>
<h2>ASYNCHRONOUS EVENTS</h2>
<p> Default. </p>
<h2>STDOUT</h2>
<p> In <code>write </code> mode, if <code>-f </code> is not specified, the standard output shall be the archive formatted according to one of the specifications in the EXTENDED DESCRIPTION section, or some other implementation-defined format (see <code>-x</code><i> format</i><code>).</code> </p>
<p> In <code>list </code> mode, when the <code>-o listopt= </code> format has been specified, the selected archive members shall be written to standard output using the format described under List Mode Format Specifications. In <code>list </code> mode without the <code>-o listopt= </code> format option, the table of contents of the selected archive members shall be written to standard output using the following format: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&quot;%s\n&quot;,&nbsp;<wbr>&lt;pathname&gt; </p>
<p> If the <code>-v </code> option is specified in <code>list </code> mode, the table of contents of the selected archive members shall be written to standard output using the following formats. </p>
<p> For pathnames representing hard links to previous members of the archive: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&quot;%s&nbsp;<wbr>==&nbsp;<wbr>%s\n&quot;,&nbsp;<wbr>&lt;ls -l listing&gt;,&nbsp;<wbr>&lt;linkname&gt; </p>
<p> For all other pathnames: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&quot;%s\n&quot;,&nbsp;<wbr>&lt;ls -l listing&gt; </p>
<p> where <i>&lt;ls -l listing&gt;</i> shall be the format specified by the <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) utility with the <code>-l </code> option. When writing pathnames in this format, it is unspecified what is written for fields for which the underlying archive format does not have the correct information, although the correct number of &lt;blank&gt;-separated fields shall be written. </p>
<p> In <code>list </code> mode, standard output shall not be buffered more than a line at a time. </p>
<h2>STDERR</h2>
<p> If <code>-v </code> is specified in <code>read</code>, <code>write</code>, or <code>copy </code> modes, <code>pax </code> shall write the pathnames it processes to the standard error output using the following format: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&quot;%s\n&quot;,&nbsp;<wbr>&lt;pathname&gt; </p>
<p> These pathnames shall be written as soon as processing is begun on the file or archive member, and shall be flushed to standard error. The trailing &lt;newline&gt;, which shall not be buffered, is written when the file has been read or written. </p>
<p> If the <code>-s </code> option is specified, and the replacement string has a trailing <code>&#8216;p&#8217;</code>, substitutions shall be written to standard error in the following format: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&quot;%s&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>%s\n&quot;,&nbsp;<wbr>&lt;original pathname&gt;,&nbsp;<wbr>&lt;new pathname&gt; </p>
<p> In all operating modes of <code>pax</code>, optional messages of unspecified format concerning the input archive format and volume number, the number of files, blocks, volumes, and media parts as well as other diagnostic messages may be written to standard error. </p>
<p> In all formats, for both standard output and standard error, it is unspecified how non-printable characters in pathnames or link names are written. </p>
<p> When <code>pax</code> is in <code>read </code> mode or <code>list </code> mode, using the <code>-x pax </code> archive format, and a filename, link name, owner name, or any other field in an extended header record cannot be translated from the <code>pax</code> UTF-8 codeset format to the codeset and current locale of the implementation, <code>pax </code> shall write a diagnostic message to standard error, shall process the file as described for the <code>-o invalid=</code> option, and then shall process the next file in the archive. </p>
<h2>OUTPUT FILES</h2>
<p> In <code>read </code> mode, the extracted output files shall be of the archived file type. In <code>copy </code> mode, the copied output files shall be the type of the file being copied. In either mode, existing files in the destination hierarchy shall be overwritten only when all permission (<code>-p</code>), modification time (<code>-u</code>), and invalid-value (<code>-o invalid=</code>) tests allow it. </p>
<p> In <code>write </code> mode, the output file named by the <code>-f </code> option-argument shall be a file formatted according to one of the specifications in the EXTENDED DESCRIPTION section, or some other implementation-defined format. </p>
<h2>EXTENDED DESCRIPTION</h2>
<h3>pax Interchange Format</h3>
<p> A <code>pax </code> archive tape or file produced in the <code>-x pax </code> format shall contain a series of blocks. The physical layout of the archive shall be identical to the <code>ustar </code> format described in ustar Interchange Format. Each file archived shall be represented by the following sequence: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> An optional header block with extended header records. This header block is of the form described in <code>pax Header Block</code>, with a <i>typeflag </i> value of <code>x</code> or <code>g</code>. The extended header records, described in <code>pax Extended Header</code>, shall be included as the data for this header block. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> A header block that describes the file. Any fields in the preceding optional extended header shall override the associated fields in this header block for this file. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Zero or more blocks that contain the contents of the file. </p>
 </dd></dl>
</dl>
<p> At the end of the archive file there shall be two 512-byte blocks filled with binary zeros, interpreted as an end-of-archive indicator. </p>
<p> A schematic of an example archive with global extended header records and two actual files is shown in <code>pax Format Archive</code> Example. In the example, the second file in the archive has no extended header preceding it, presumably because it has no need for extended attributes. </p>
<p> <center> <code>Figure: pax Format Archive Example</code> <br />
 </center> <center> </p>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td>ustar Header [typeflag = &#8216;g&#8217;]</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>Global Extended Header Data</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>ustar Header [typeflag = &#8216;x&#8217;]</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>Extended Header Data</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>ustar Header [typeflag = &#8216;0&#8217;]</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>Data for File 1</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>ustar Header [typeflag = &#8216;0&#8217;]</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>Data for File 2</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>Block of binary Zeroes</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>Block of binary Zeroes</td>
</tr>
</table>
</table>
<p> </center> </p>
<h3>pax Header Block</h3>
<p> The <code>pax</code> header block shall be identical to the <code>ustar</code> header block described in <code>ustar Interchange Format</code>, except that two additional <i>typeflag </i> values are defined: </p>
<dl>
<dt><code>x</code></dt>
<dd> <p> Represents extended header records for the following file in the archive (which shall have its own <code>ustar </code> header block). The format of these extended header records shall be as described in <code>pax Extended Header</code>. </p>
 </dd>
<dt><code>g</code></dt>
<dd> <p> Represents global extended header records for the following files in the archive. The format of these extended header records shall be as described in <code>pax Extended Header</code>. Each value shall affect all subsequent files that do not override that value in their own extended header record and until another global extended header record is reached that provides another value for the same field. The <i>typeflag </i> <code>g</code> global headers should not be used with interchange media that could suffer partial data loss in transporting the archive. </p>
 </dd></dl>
<p> For both of these types, the size field shall be the size of the extended header records in octets. The other fields in the header block are not meaningful to this version of the <code>pax</code> utility. However, if this archive is read by a <code>pax </code> utility conforming to the ISO POSIX-2:1993 standard, the header block fields are used to create a regular file that contains the extended header records as data. Therefore, header block field values should be selected to provide reasonable file access to this regular file. </p>
<p> A further difference from the <code>ustar </code> header block is that data blocks for files of <i>typeflag </i> <code>1</code> (the digit one) (hard link) may be included, which means that the size field may be greater than zero. Archives created by <code>pax -o linkdata </code> shall include these data blocks with the hard links. </p>
<h3>pax Extended Header</h3>
<p> A <code>pax </code> extended header contains values that are inappropriate for the <code>ustar</code> header block because of limitations in that format: fields requiring a character encoding other than that described in the ISO/IEC 646:1991 standard, fields representing file attributes not described in the <code>ustar</code> header, and fields whose format or length do not fit the requirements of the <code>ustar</code> header. The values in an extended header add attributes to the following file (or files; see the description of the <i>typeflag </i> <code>g </code> header block) or override values in the following header block(s), as indicated in the following list of keywords. </p>
<p> An extended header shall consist of one or more records, each constructed as follows: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&quot;%d&nbsp;<wbr>%s=%s\n&quot;,&nbsp;<wbr>&lt;length&gt;,&nbsp;<wbr>&lt;keyword&gt;,&nbsp;<wbr>&lt;value&gt; </p>
<p> The extended header records shall be encoded according to the ISO/IEC 10646-1:2000 standard (UTF-8). The <i>&lt;length&gt; </i> field, &lt;blank&gt;, equals sign, and &lt;newline&gt; shown shall be limited to the portable character set, as encoded in UTF-8. The <i>&lt;keyword&gt; </i> and <i>&lt;value&gt; </i> fields can be any UTF-8 characters. The <i>&lt;length&gt;</i> field shall be the decimal length of the extended header record in octets, including the trailing &lt;newline&gt;. </p>
<p> The <i>&lt;keyword&gt;</i> field shall be one of the entries from the following list or a keyword provided as an implementation extension. Keywords consisting entirely of lowercase letters, digits, and periods are reserved for future standardization. A keyword shall not include an equals sign. (In the following list, the notations &quot;file(s)&quot; or &quot;block(s)&quot; is used to acknowledge that a keyword affects the following single file after a <i>typeflag </i> <code>x </code> extended header, but possibly multiple files after <i>typeflag </i> <code>g</code>. Any requirements in the list for <code>pax </code> to include a record when in <code>write</code> or <code>copy </code> mode shall apply only when such a record has not already been provided through the use of the <code>-o </code> option. When used in <code>copy</code> mode, <code>pax </code> shall behave as if an archive had been created with applicable extended header records and then extracted.) </p>
<dl>
<dt><code>atime</code></dt>
<dd> <p> The file access time for the following file(s), equivalent to the value of the <i>st_atime </i> member of the <code>stat </code> structure for a file, as described by the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) function. The access time shall be restored if the process has the appropriate privilege required to do so. The format of the <i>&lt;value&gt; </i> shall be as described in <code>pax Extended Header File Times</code>. </p>
 </dd>
<dt><code>charset</code></dt>
<dd> <p> The name of the character set used to encode the data in the following file(s). The entries in the following table are defined to refer to known standards; additional names may be agreed on between the originator and recipient. </p>
 </dd></dl>
<p> <center> </p>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td><code>&lt;value&gt;</code></td>
<td><code>Formal Standard</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<p> </center> </p>
<p> The encoding is included in an extended header for information only; when <code>pax </code> is used as described in IEEE Std 1003.1-2001, it shall not translate the file data into any other encoding. The <code>BINARY </code> entry indicates unencoded binary data. </p>
<p> When used in <code>write</code> or <code>copy </code> mode, it is implementation-defined whether <code>pax </code> includes a charset extended header record for a file. </p>
<dl>
<dt><code>comment</code></dt>
<dd> <p> A series of characters used as a comment. All characters in the <i>&lt;value&gt; </i> field shall be ignored by <code>pax</code>. </p>
 </dd>
<dt><code>gid</code></dt>
<dd> <p> The group ID of the group that owns the file, expressed as a decimal number using digits from the ISO/IEC 646:1991 standard. This record shall override the <i>gid </i> field in the following header block(s). When used in <code>write </code> or <code>copy </code> mode, <code>pax </code> shall include a gid extended header record for each file whose group ID is greater than 2097151 (octal 7777777). </p>
 </dd>
<dt><code>gname</code></dt>
<dd> <p> The group of the file(s), formatted as a group name in the group database. This record shall override the <code>gid </code> and <code>gname</code> fields in the following header block(s), and any <code>gid </code> extended header record. When used in <code>read</code>, <code>copy</code>, or <code>list </code> mode, <code>pax</code> shall translate the name from the UTF-8 encoding in the header record to the character set appropriate for the group database on the receiving system. If any of the UTF-8 characters cannot be translated, and if the <code>-o invalid=</code>UTF-8 option is not specified, the results are implementation-defined. When used in <code>write </code> or <code>copy </code> mode, <code>pax</code> shall include a <code>gname </code> extended header record for each file whose group name cannot be represented entirely with the letters and digits of the portable character set. </p>
 </dd>
<dt><code>linkpath</code></dt>
<dd> <p> The pathname of a link being created to another file, of any type, previously archived. This record shall override the <i>linkname </i> field in the following <code>ustar </code> header block(s). The following <code>ustar </code> header block shall determine the type of link created. If <i>typeflag </i> of the following header block is 1, it shall be a hard link. If <i>typeflag </i> is 2, it shall be a symbolic link and the linkpath value shall be the contents of the symbolic link. The <code>pax </code> utility shall translate the name of the link (contents of the symbolic link) from the UTF-8 encoding to the character set appropriate for the local file system. When used in <code>write </code> or <code>copy </code> mode, <code>pax </code> shall include a linkpath extended header record for each link whose pathname cannot be represented entirely with the members of the portable character set other than NUL. </p>
 </dd>
<dt><code>mtime</code></dt>
<dd> <p> The file modification time of the following file(s), equivalent to the value of the <i>st_mtime </i> member of the <code>stat</code> structure for a file, as described in the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) function. This record shall override the <i>mtime </i> field in the following header block(s). The modification time shall be restored if the process has the appropriate privilege required to do so. The format of the <i>&lt;value&gt; </i> shall be as described in <code>pax Extended Header File Times</code>. </p>
 </dd>
<dt><code>path</code></dt>
<dd> <p> The pathname of the following file(s). This record shall override the <i>name </i> and <i>prefix </i> fields in the following header block(s). The <code>pax </code> utility shall translate the pathname of the file from the UTF-8 encoding to the character set appropriate for the local file system. </p>
<p> When used in <code>write </code> or <code>copy </code> mode, <code>pax </code> shall include a <i>path</i> extended header record for each file whose pathname cannot be represented entirely with the members of the portable character set other than NUL. </p>
 </dd>
<dt><code>realtime.</code><i>any</i></dt>
<dd> <p> The keywords prefixed by &quot;realtime.&quot; are reserved for future standardization. </p>
 </dd>
<dt><code>security.</code><i>any</i></dt>
<dd> <p> The keywords prefixed by &quot;security.&quot; are reserved for future standardization. </p>
 </dd>
<dt><code>size</code></dt>
<dd> <p> The size of the file in octets, expressed as a decimal number using digits from the ISO/IEC 646:1991 standard. This record shall override the <i>size </i> field in the following header block(s). When used in <code>write </code> or <code>copy </code> mode, <code>pax </code> shall include a <i>size </i> extended header record for each file with a size value greater than 8589934591 (octal 77777777777). </p>
 </dd>
<dt><code>uid</code></dt>
<dd> <p> The user ID of the file owner, expressed as a decimal number using digits from the ISO/IEC 646:1991 standard. This record shall override the <i>uid </i> field in the following header block(s). When used in <code>write </code> or <code>copy</code> mode, <code>pax </code> shall include a <i>uid </i> extended header record for each file whose owner ID is greater than 2097151 (octal 7777777). </p>
 </dd>
<dt><code>uname</code></dt>
<dd> <p> The owner of the following file(s), formatted as a user name in the user database. This record shall override the <i>uid </i> and <i>uname </i> fields in the following header block(s), and any <i>uid</i> extended header record. When used in <code>read</code>, <code>copy</code>, or <code>list</code> mode, <code>pax </code> shall translate the name from the UTF-8 encoding in the header record to the character set appropriate for the user database on the receiving system. If any of the UTF-8 characters cannot be translated, and if the <code>-o invalid=</code>UTF-8 option is not specified, the results are implementation-defined. When used in <code>write </code> or <code>copy </code> mode, <code>pax</code> shall include a <i>uname </i> extended header record for each file whose user name cannot be represented entirely with the letters and digits of the portable character set. </p>
 </dd></dl>
<p> If the <i>&lt;value&gt; </i> field is zero length, it shall delete any header block field, previously entered extended header value, or global extended header value of the same name. </p>
<p> If a keyword in an extended header record (or in a <code>-o</code> option-argument) overrides or deletes a corresponding field in the <code>ustar </code> header block, <code>pax </code> shall ignore the contents of that header block field. </p>
<p> Unlike the <code>ustar </code> header block fields, NULs shall not delimit <i>&lt;value&gt;</i>s; all characters within the <i>&lt;value&gt; </i> field shall be considered data for the field. None of the length limitations of the <code>ustar </code> header block fields in <code>ustar Header Block </code> shall apply to the extended header records. </p>
<h3>pax Extended Header Keyword Precedence</h3>
<p> This section describes the precedence in which the various header records and fields and command line options are selected to apply to a file in the archive. When <code>pax </code> is used in <code>read </code> or <code>list </code> modes, it shall determine a file attribute in the following sequence: </p>
<dl>
<dd>  </dd>
<dl>
<dt>1.</dt>
<dd> <p> If <code>-o delete=</code><i>keyword-prefix</i> is used, the affected attributes shall be determined from step 7., if applicable, or ignored otherwise. </p>
 </dd>
<dt>2.</dt>
<dd> <p> If <code>-o </code><i>keyword:=</i> is used, the affected attributes shall be ignored. </p>
 </dd>
<dt>3.</dt>
<dd> <p> If <code>-o </code><i>keyword:=value</i> is used, the affected attribute shall be assigned the value. </p>
 </dd>
<dt>4.</dt>
<dd> <p> If there is a <i>typeflag </i> <code>x </code> extended header record, the affected attribute shall be assigned the <i>&lt;value&gt;</i>. When extended header records conflict, the last one given in the header shall take precedence. </p>
 </dd>
<dt>5.</dt>
<dd> <p> If <code>-o </code><i>keyword=value</i> is used, the affected attribute shall be assigned the value. </p>
 </dd>
<dt>6.</dt>
<dd> <p> If there is a <i>typeflag </i> <code>g </code> global extended header record, the affected attribute shall be assigned the <i>&lt;value&gt;</i>. When global extended header records conflict, the last one given in the global header shall take precedence. </p>
 </dd>
<dt>7.</dt>
<dd> <p> Otherwise, the attribute shall be determined from the <code>ustar</code> header block. </p>
 </dd></dl>
</dl>
<h3>pax Extended Header File Times</h3>
<p> The <code>pax </code> utility shall write an <code>mtime </code> record for each file in <code>write</code> or <code>copy </code> modes if the file&#8217;s modification time cannot be represented exactly in the <code>ustar </code> header logical record described in <code>ustar Interchange Format</code>. This can occur if the time is out of <code>ustar </code> range, or if the file system of the underlying implementation supports non-integer time granularities and the time is not an integer. All of these time records shall be formatted as a decimal representation of the time in seconds since the Epoch. If a period (&#8216;.&#8216;) decimal point character is present, the digits to the right of the point shall represent the units of a subsecond timing granularity, where the first digit is tenths of a second and each subsequent digit is a tenth of the previous digit. In <code>read </code> or <code>copy </code> mode, the <code>pax </code> utility shall truncate the time of a file to the greatest value that is not greater than the input header file time. In <code>write </code> or <code>copy </code> mode, the <code>pax </code> utility shall output a time exactly if it can be represented exactly as a decimal number, and otherwise shall generate only enough digits so that the same time shall be recovered if the file is extracted on a system whose underlying implementation supports the same time granularity. </p>
<h3>ustar Interchange Format</h3>
<p> A <code>ustar </code> archive tape or file shall contain a series of logical records. Each logical record shall be a fixed-size logical record of 512 octets (see below). Although this format may be thought of as being stored on 9-track industry-standard 12.7 mm (0.5 in) magnetic tape, other types of transportable media are not excluded. Each file archived shall be represented by a header logical record that describes the file, followed by zero or more logical records that give the contents of the file. At the end of the archive file there shall be two 512-octet logical records filled with binary zeros, interpreted as an end-of-archive indicator. </p>
<p> The logical records may be grouped for physical I/O operations, as described under the <code>-b</code><i> blocksize </i> and <code>-x</code><i> ustar </i> options. Each group of logical records may be written with a single operation equivalent to the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) function. On magnetic tape, the result of this write shall be a single tape physical block. The last physical block shall always be the full size, so logical records after the two zero logical records may contain undefined data. </p>
<p> The header logical record shall be structured as shown in the following table. All lengths and offsets are in decimal. </p>
<p> <center> <code>Table: ustar Header Block</code> <br />
 </center> <center> </p>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td><code>Field Name</code></td>
<td><code>Octet Offset</code></td>
<td><code>Length (in Octets)</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>name</td>
<td>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>100&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>mode</td>
<td>100&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>uid</td>
<td>108&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>gid</td>
<td>116&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>size</td>
<td>124&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>mtime</td>
<td>136&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>chksum</td>
<td>148&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>typeflag</td>
<td>156&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>linkname</td>
<td>157&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>100&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>magic</td>
<td>257&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>version</td>
<td>263&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>uname</td>
<td>265&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>gname</td>
<td>297&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>devmajor</td>
<td>329&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>devminor</td>
<td>337&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>prefix</td>
<td>345&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>155&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
</table>
</table>
<p> </center> </p>
<p> All characters in the header logical record shall be represented in the coded character set of the ISO/IEC 646:1991 standard. For maximum portability between implementations, names should be selected from characters represented by the portable filename character set as octets with the most significant bit zero. If an implementation supports the use of characters outside of slash and the portable filename character set in names for files, users, and groups, one or more implementation-defined encodings of these characters shall be provided for interchange purposes. </p>
<p> However, the <code>pax </code> utility shall never create filenames on the local system that cannot be accessed via the procedures described in IEEE Std 1003.1-2001. If a filename is found on the medium that would create an invalid filename, it is implementation-defined whether the data from the file is stored on the file hierarchy and under what name it is stored. The <code>pax </code> utility may choose to ignore these files as long as it produces an error indicating that the file is being ignored. </p>
<p> Each field within the header logical record is contiguous; that is, there is no padding used. Each character on the archive medium shall be stored contiguously. </p>
<p> The fields <i>magic</i>, <i>uname</i>, and <i>gname </i> are character strings each terminated by a NUL character. The fields <i>name</i>, <i>linkname</i>, and <i>prefix </i> are NUL-terminated character strings except when all characters in the array contain non-NUL characters including the last character. The <i>version </i> field is two octets containing the characters &quot;00&quot; (zero-zero). The <i>typeflag </i> contains a single character. All other fields are leading zero-filled octal numbers using digits from the ISO/IEC 646:1991 standard IRV. Each numeric field is terminated by one or more &lt;space&gt; or NUL characters. </p>
<p> The <i>name </i> and the <i>prefix </i> fields shall produce the pathname of the file. A new pathname shall be formed, if <i>prefix </i> is not an empty string (its first character is not NUL), by concatenating <i>prefix</i> (up to the first NUL character), a slash character, and <i>name</i>; otherwise, <i>name</i> is used alone. In either case, <i>name </i> is terminated at the first NUL character. If <i>prefix </i> begins with a NUL character, it shall be ignored. In this manner, pathnames of at most 256 characters can be supported. If a pathname does not fit in the space provided, <code>pax </code> shall notify the user of the error, and shall not store any part of the file-header or data-on the medium. </p>
<p> The <i>linkname </i> field, described below, shall not use the <i>prefix </i> to produce a pathname. As such, a <i>linkname </i> is limited to 100 characters. If the name does not fit in the space provided, <code>pax</code> shall notify the user of the error, and shall not attempt to store the link on the medium. </p>
<p> The <i>mode </i> field provides 12 bits encoded in the ISO/IEC 646:1991 standard octal digit representation. The encoded bits shall represent the following values: </p>
<p> <center> <code>Table: ustar mode Field</code> <br />
 </center> <center> </p>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td><code>Bit</code></td>
<td><code>IEEE Std</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Value</code></td>
<td><code>1003.1-2001 Bit</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<p> </center> </p>
<p> When appropriate privilege is required to set one of these mode bits, and the user restoring the files from the archive does not have the appropriate privilege, the mode bits for which the user does not have appropriate privilege shall be ignored. Some of the mode bits in the archive format are not mentioned elsewhere in this volume of IEEE Std 1003.1-2001. If the implementation does not support those bits, they may be ignored. </p>
<p> The <i>uid and </i> <i>gid </i> fields are the user and group ID of the owner and group of the file, respectively. </p>
<p> The <i>size </i> field is the size of the file in octets. If the <i>typeflag</i> field is set to specify a file to be of type 1 (a link) or 2 (a symbolic link), the <i>size </i> field shall be specified as zero. If the <i>typeflag </i> field is set to specify a file of type 5 (directory), the size field shall be interpreted as described under the definition of that record type. No data logical records are stored for types 1, 2, or 5. If the typeflag field is set to 3 (character special file), 4 (block special file), or 6 (FIFO), the meaning of the <i>size </i> field is unspecified by this volume of IEEE Std 1003.1-2001, and no data logical records shall be stored on the medium. Additionally, for type 6, the <i>size </i> field shall be ignored when reading. If the <i>typeflag </i> field is set to any other value, the number of logical records written following the header shall be (size+511)/512, ignoring any fraction in the result of the division. </p>
<p> The <i>mtime </i> field shall be the modification time of the file at the time it was archived. It is the ISO/IEC 646:1991 standard representation of the octal value of the modification time obtained from the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) function. </p>
<p> The <i>chksum </i> field shall be the ISO/IEC 646:1991 standard IRV representation of the octal value of the simple sum of all octets in the header logical record. Each octet in the header shall be treated as an unsigned value. These values shall be added to an unsigned integer, initialized to zero, the precision of which is not less than 17 bits. When calculating the checksum, the <i>chksum</i> field is treated as if it were all spaces. </p>
<p> The <i>typeflag </i> field specifies the type of file archived. If a particular implementation does not recognize the type, or the user does not have appropriate privilege to create that type, the file shall be extracted as if it were a regular file if the file type is defined to have a meaning for the <i>size </i> field that could cause data logical records to be written on the medium (see the previous description for <i>size</i>). If conversion to a regular file occurs, the <code>pax </code> utility shall produce an error indicating that the conversion took place. All of the <i>typeflag </i> fields shall be coded in the ISO/IEC 646:1991 standard IRV: </p>
<dl>
<dt><code>0</code></dt>
<dd> <p> Represents a regular file. For backwards-compatibility, a <i>typeflag</i> value of binary zero (&#8216;\0&#8217;) should be recognized as meaning a regular file when extracting files from the archive. Archives written with this version of the archive file format create regular files with a <i>typefla</i> value of the ISO/IEC 646:1991 standard IRV &#8216;0&#8217;. </p>
 </dd>
<dt><code>1</code></dt>
<dd> <p> Represents a file linked to another file, of any type, previously archived. Such files are identified by having the same device and file serial numbers, and pathnames that refer to different directory entries. All such files shall be archived as linked files. The linked-to name is specified in the <i>linkname </i> field with a NUL-character terminator if it is less than 100 octets in length. </p>
 </dd>
<dt><code>2</code></dt>
<dd> <p> Represents a symbolic link. The contents of the symbolic link shall be stored in the <i>linkname </i> field. </p>
 </dd>
<dt><code>3,4 </code></dt>
<dd> <p> Represent character special files and block special files respectively. In this case the <i>devmajor </i> and <i>devminor </i> fields shall contain information defining the device, the format of which is unspecified by this volume of IEEE Std 1003.1-2001. Implementations may map the device specifications to their own local specification or may ignore the entry. </p>
 </dd>
<dt><code>5</code></dt>
<dd> <p> Specifies a directory or subdirectory. On systems where disk allocation is performed on a directory basis, the <i>size </i> field shall contain the maximum number of octets (which may be rounded to the nearest disk block allocation unit) that the directory may hold. A <i>size </i> field of zero indicates no such limiting. Systems that do not support limiting in this manner should ignore the <i>size </i> field. </p>
 </dd>
<dt><code>6</code></dt>
<dd> <p> Specifies a FIFO special file. Note that the archiving of a FIFO file archives the existence of this file and not its contents. </p>
 </dd>
<dt><code>7</code></dt>
<dd> <p> Reserved to represent a file to which an implementation has associated some high-performance attribute. Implementations without such extensions should treat this file as a regular file (type 0). </p>
 </dd>
<dt><code>A-Z</code></dt>
<dd> <p> The letters &#8216;A&#8217; to &#8216;Z&#8217;, inclusive, are reserved for custom implementations. All other values are reserved for future versions of IEEE Std 1003.1-2001. </p>
 </dd></dl>
<p> It is unspecified whether files with pathnames that refer to the same directory entry are archived as linked files or as separate files. If they are archived as linked files, this means that attempting to extract both pathnames from the resulting archive will always cause an error (unless the <code>-u </code> option is used) because the link cannot be created. </p>
<p> It is unspecified whether files with the same device and file serial numbers being appended to an archive are treated as linked files to members that were in the archive before the append. </p>
<p> Attempts to archive a socket using <code>ustar</code> interchange format shall produce a diagnostic message. Handling of other file types is implementation-defined. </p>
<p> The <i>magic </i> field is the specification that this archive was output in this archive format. If this field contains <code>ustar </code> (the five characters from the ISO/IEC 646:1991 standard IRV shown followed by NUL), the <i>uname </i> and <i>gname </i> fields shall contain the ISO/IEC 646:1991 standard IRV representation of the owner and group of the file, respectively (truncated to fit, if necessary). When the file is restored by a privileged, protection-preserving version of the utility, the user and group databases shall be scanned for these names. If found, the user and group IDs contained within these files shall be used rather than the values contained within the <i>uid </i> and <i>gid </i> fields. </p>
<h3>cpio Interchange Format</h3>
<p> The octet-oriented <code>cpio </code> archive format shall be a series of entries, each comprising a header that describes the file, the name of the file, and then the contents of the file. </p>
<p> An archive may be recorded as a series of fixed-size blocks of octets. This blocking shall be used only to make physical I/O more efficient. The last group of blocks shall always be at the full size. </p>
<p> For the octet-oriented <code>cpio </code> archive format, the individual entry information shall be in the order indicated and described by the following table; see also the <code>&lt;cpio.h&gt; </code> header. </p>
<p> <center> <code>Table: Octet-Oriented cpio Archive Entry</code> <br />
 </center> <center> </p>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td><code>Header Field Name</code></td>
<td><code>Length (in Octets)</code></td>
<td><code>Interpreted as</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>c_magic</td>
<td>6</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_dev</td>
<td>6</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_ino</td>
<td>6</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_mode</td>
<td>6</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_uid</td>
<td>6</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_gid</td>
<td>6</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_nlink</td>
<td>6</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_rdev</td>
<td>6</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_mtime</td>
<td>11</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_namesize</td>
<td>6</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td>c_filesize</td>
<td>11</td>
<td>Octal number
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>Filename Field Name</code></td>
<td>Length</td>
<td>Interpreted as
</td>
</tr>
<tr VALIGN=top>
<td>c_name</td>
<td>c_namesize</td>
<td>Pathname string
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>File Data Field Name</code></td>
<td>Length</td>
<td>Interpreted as
</td>
</tr>
<tr VALIGN=top>
<td>c_filedata</td>
<td>c_filesize</td>
<td>Data
</td>
</tr>
</table>
</table>
<p> </center> </p>
<h3>cpio Header</h3>
<p> For each file in the archive, a header as defined previously shall be written. The information in the header fields is written as streams of the ISO/IEC 646:1991 standard characters interpreted as octal numbers. The octal numbers shall be extended to the necessary length by appending the ISO/IEC 646:1991 standard IRV zeros at the most-significant-digit end of the number; the result is written to the most-significant digit of the stream of octets first. The fields shall be interpreted as follows: </p>
<dl>
<dt><code>c_magic</code></dt>
<dd> <p> Identify the archive as being a transportable archive by containing the identifying value &quot;070707&quot;. </p>
 </dd>
<dt><code>c_dev</code>, <code>c_ino</code></dt>
<dd> <p> Contains values that uniquely identify the file within the archive (that is, no files contain the same pair of <i>c_dev </i> and <i>c_ino </i> values unless they are links to the same file). The values shall be determined in an unspecified manner. </p>
 </dd>
<dt><code>c_mode</code></dt>
<dd> <p> Contains the file type and access permissions as defined in the following table. </p>
 </dd>
<dl>
<dd> <p> <center> <code>Table: Values for cpio c_mode Field</code> <br />
 </center> <center> </p>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td><code>File Permissions Name</code></td>
<td><code>Value</code></td>
<td><code>Indicates</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>C_IRUSR</td>
<td>000400</td>
<td>Read by owner
</td>
</tr>
<tr VALIGN=top>
<td>C_IWUSR</td>
<td>000200</td>
<td>Write by owner
</td>
</tr>
<tr VALIGN=top>
<td>C_IXUSR</td>
<td>000100</td>
<td>Execute by owner
</td>
</tr>
<tr VALIGN=top>
<td>C_IRGRP</td>
<td>000040</td>
<td>Read by group
</td>
</tr>
<tr VALIGN=top>
<td>C_IWGRP</td>
<td>000020</td>
<td>Write by group
</td>
</tr>
<tr VALIGN=top>
<td>C_IXGRP</td>
<td>000010</td>
<td>Execute by group
</td>
</tr>
<tr VALIGN=top>
<td>C_IROTH</td>
<td>000004</td>
<td>Read by others
</td>
</tr>
<tr VALIGN=top>
<td>C_IWOTH</td>
<td>000002</td>
<td>Write by others
</td>
</tr>
<tr VALIGN=top>
<td>C_IXOTH</td>
<td>000001</td>
<td>Execute by others
</td>
</tr>
<tr VALIGN=top>
<td>C_ISUID</td>
<td>004000</td>
<td>Set uid
</td>
</tr>
<tr VALIGN=top>
<td>C_ISGID</td>
<td>002000</td>
<td>Set gid
</td>
</tr>
<tr VALIGN=top>
<td>C_ISVTX</td>
<td>001000</td>
<td>Reserved
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td><code>File Type Name</code></td>
<td>Value</td>
<td>Indicates
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>C_ISDIR</td>
<td>0040000</td>
<td>Directory
</td>
</tr>
<tr VALIGN=top>
<td>C_ISFIFO</td>
<td>0010000</td>
<td>FIFO
</td>
</tr>
<tr VALIGN=top>
<td>C_ISREG</td>
<td>0100000</td>
<td>Regular file
</td>
</tr>
<tr VALIGN=top>
<td>C_ISLNK</td>
<td>0120000</td>
<td>Symbolic link
</td>
</tr>
<tr VALIGN=top>
<td>C_ISBLK</td>
<td>0060000</td>
<td>Block special file
</td>
</tr>
<tr VALIGN=top>
<td>C_ISCHR</td>
<td>0020000</td>
<td>Character special file
</td>
</tr>
<tr VALIGN=top>
<td>C_ISSOCK</td>
<td>0140000</td>
<td>Socket
</td>
</tr>
<tr VALIGN=top>
<td>C_ISCTG</td>
<td>0110000</td>
<td>Reserved
</td>
</tr>
</table>
</table>
<p> </center> </p>
<p> Directories, FIFOs, symbolic links, and regular files shall be supported on a system conforming to this volume of IEEE Std 1003.1-2001; additional values defined previously are reserved for compatibility with existing systems. Additional file types may be supported; however, such files should not be written to archives intended to be transported to other systems. </p>
 </dd></dl>
<dt><code>c_uid</code></dt>
<dd> <p> Contains the user ID of the owner. </p>
 </dd>
<dt><code>c_gid</code></dt>
<dd> <p> Contains the group ID of the group. </p>
 </dd>
<dt><code>c_nlink</code></dt>
<dd> <p> Contains a number greater than or equal to the number of links in the archive referencing the file. If the <code>-a </code> option is used to append to a <i>cpio</i> archive, then the <code>pax </code> utility need not account for the files in the existing part of the archive when calculating the <i>c_nlink </i> values for the appended part of the archive, and need not alter the <i>c_nlink </i> values in the existing part of the archive if additional files with the same <i>c_dev </i> and <i>c_ino </i> values are appended to the archive. </p>
 </dd>
<dt><code>c_rdev</code></dt>
<dd> <p> Contains implementation-defined information for character or block special files. </p>
 </dd>
<dt><code>c_mtime</code></dt>
<dd> <p> Contains the latest time of modification of the file at the time the archive was created. </p>
 </dd>
<dt><code>c_namesize</code></dt>
<dd> <p> Contains the length of the pathname, including the terminating NUL character. </p>
 </dd>
<dt><code>c_filesize</code></dt>
<dd> <p> Contains the length of the file in octets. This shall be the length of the data section following the header structure. </p>
 </dd></dl>
<h3>cpio Filename</h3>
<p> The <i>c_name </i> field shall contain the pathname of the file. The length of this field in octets is the value of <i>c_namesize</i>. </p>
<p> If a filename is found on the medium that would create an invalid pathname, it is implementation-defined whether the data from the file is stored on the file hierarchy and under what name it is stored. </p>
<p> All characters shall be represented in the ISO/IEC 646:1991 standard IRV. For maximum portability between implementations, names should be selected from characters represented by the portable filename character set as octets with the most significant bit zero. If an implementation supports the use of characters outside the portable filename character set in names for files, users, and groups, one or more implementation-defined encodings of these characters shall be provided for interchange purposes. However, the <code>pax </code> utility shall never create filenames on the local system that cannot be accessed via the procedures described previously in this volume of IEEE Std 1003.1-2001. If a filename is found on the medium that would create an invalid filename, it is implementation-defined whether the data from the file is stored on the local file system and under what name it is stored. The <code>pax </code> utility may choose to ignore these files as long as it produces an error indicating that the file is being ignored. </p>
<h3>cpio File Data</h3>
<p> Following <i>c_name</i>, there shall be <i>c_filesize </i> octets of data. Interpretation of such data occurs in a manner dependent on the file. If <i>c_filesize </i> is zero, no data shall be contained in <i>c_filedata</i>. </p>
<p> When restoring from an archive: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> If the user does not have the appropriate privilege to create a file of the specified type, <code>pax</code> shall ignore the entry and write an error message to standard error. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Only regular files have data to be restored. Presuming a regular file meets any selection criteria that might be imposed on the format-reading utility by the user, such data shall be restored. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> If a user does not have appropriate privilege to set a particular mode flag, the flag shall be ignored. Some of the mode flags in the archive format are not mentioned elsewhere in this volume of IEEE Std 1003.1-2001. If the implementation does not support those flags, they may be ignored. </p>
 </dd></dl>
<h3>cpio Special Entries</h3>
<p> FIFO special files, directories, and the trailer shall be recorded with <i>c_filesize </i> equal to zero. For other special files, <i>c_filesize</i> is unspecified by this volume of IEEE Std 1003.1-2001. The header for the next file entry in the archive shall be written directly after the last octet of the file entry preceding it. A header denoting the filename <code>TRAILER!!!</code> shall indicate the end of the archive; the contents of octets in the last block of the archive following such a header are undefined. </p>
<h2>EXIT STATUS</h2>
<p> The following exit values shall be returned: </p>
<dl>
<dt><code> 0</code></dt>
<dd> <p> All files were processed successfully. </p>
 </dd>
<dt><code>&gt;0</code></dt>
<dd> <p> An error occurred. </p>
 </dd></dl>
<h2>CONSEQUENCES OF ERRORS</h2>
<p> If <code>pax </code> cannot create a file or a link when reading an archive or cannot find a file when writing an archive, or cannot preserve the user ID, group ID, or file mode when the <code>-p </code> option is specified, a diagnostic message shall be written to standard error and a non-zero exit status shall be returned, but processing shall continue. In the case where <code>pax </code> cannot create a link to a file, <code>pax </code> shall not, by default, create a second copy of the file. </p>
<p> If the extraction of a file from an archive is prematurely terminated by a signal or error, <code>pax </code> may have only partially extracted the file or (if the <code>-n </code> option was not specified) may have extracted a file of the same name as that specified by the user, but which is not the file the user wanted. Additionally, the file modes of extracted directories may have additional bits from the S_IRWXU mask set as well as incorrect modification and access times. </p>
<p> <br />
 </p>
<hr />
<p> <br />
 <i>The following sections are informative.</i> </p>
<h2>APPLICATION USAGE</h2>
<p> Caution is advised when using the <code>-a </code> option to append to a <i>cpio</i> format archive. If any of the files being appended happen to be given the same <i>c_dev </i> and <i>c_ino </i> values as a file in the existing part of the archive, then they may be treated as links to that file on extraction. Thus, it is risky to use <code>-a </code> with <i>cpio </i> format except when it is done on the same system that the original archive was created on, and with the same <code>pax </code> utility, and in the knowledge that there has been little or no file system activity since the original archive was created that could lead to any of the files appended being given the same <i>c_dev </i> and <i>c_ino </i> values as an unrelated file in the existing part of the archive. Also, when (intentionally) appending additional links to a file in the existing part of the archive, the <i>c_nlink </i> values in the modified archive can be smaller than the number of links to the file in the archive, which may mean that the links are not preserved on extraction. </p>
<p> The <code>-p </code> (privileges) option was invented to reconcile differences between historical <code>tar </code> and <code>cpio </code> implementations. In particular, the two utilities use <code>-m </code> in diametrically opposed ways. The <code>-p</code> option also provides a consistent means of extending the ways in which future file attributes can be addressed, such as for enhanced security systems or high-performance files. Although it may seem complex, there are really two modes that are most commonly used: </p>
<dl>
<dt><code>-p e</code></dt>
<dd> <p> ``Preserve everything&quot;. This would be used by the historical superuser, someone with all the appropriate privileges, to preserve all aspects of the files as they are recorded in the archive. The <code>e </code> flag is the sum of <code>o </code> and <code>p</code>, and other implementation-defined attributes. </p>
 </dd>
<dt><code>-p p</code></dt>
<dd> <p> ``Preserve&quot; the file mode bits. This would be used by the user with regular privileges who wished to preserve aspects of the file other than the ownership. The file times are preserved by default, but two other flags are offered to disable these and use the time of extraction. </p>
 </dd></dl>
<p> The one pathname per line format of standard input precludes pathnames containing &lt;newline&gt;s. Although such pathnames violate the portable filename guidelines, they may exist and their presence may inhibit usage of <code>pax </code> within shell scripts. This problem is inherited from historical archive programs. The problem can be avoided by listing filename arguments on the command line instead of on standard input. </p>
<p> It is almost certain that appropriate privileges are required for <code>pax </code> to accomplish parts of this volume of IEEE Std 1003.1-2001. Specifically, creating files of type block special or character special, restoring file access times unless the files are owned by the user (the <code>-t </code> option), or preserving file owner, group, and mode (the <code>-p </code> option) all probably require appropriate privileges. </p>
<p> In <code>read </code> mode, implementations are permitted to overwrite files when the archive has multiple members with the same name. This may fail if permissions on the first version of the file do not permit it to be overwritten. </p>
<p> The <code>cpio </code> and <code>ustar </code> formats can only support files up to 8589934592 bytes (8 * 2^30) in size. </p>
<h2>EXAMPLES</h2>
<p> The following command: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pax -w -f&nbsp;<wbr>/dev/rmt/1m .</code> </p>
<p> copies the contents of the current directory to tape drive 1, medium density (assuming historical System V device naming procedures-the historical BSD device name would be /dev/rmt9). </p>
<p> The following commands: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mkdir newdirpax -rw olddir newdir</code> </p>
<p> copy the olddir directory hierarchy to newdir. </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pax -r -s&nbsp;<wbr>&#8216;,^//*usr//*,,&#8216;&nbsp;<wbr>-f a.pax</code> </p>
<p> reads the archive a.pax, with all files rooted in /usr in the archive extracted relative to the current directory. </p>
<p> Using the option: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-o listopt=&quot;%M&nbsp;<wbr>%(atime)T&nbsp;<wbr>%(size)D&nbsp;<wbr>%(name)s&quot;</code> </p>
<p> overrides the default output description in Standard Output and instead writes: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-rw-rw--- Jan 12 15:53 1492&nbsp;<wbr>/usr/foo/bar</code> </p>
<p> Using the options: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-o listopt=&#8216;%L\t%(size)D\n%.7&#8217;&nbsp;<wbr>\</code> <br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-o listopt=&#8216;(name)s\n%(atime)T\n%T&#8217;</code> </p>
<p> overrides the default output description in Standard Output and instead writes: </p>
<p> <code>/usr/foo/bar -&gt; /tmp 1492</code> <br />
 <code>/usr/fo</code> <br />
 <code>Jan 12 1991</code> <br />
 <code>Jan 31 15:53</code> </p>
<h2>RATIONALE</h2>
<p> The <code>pax</code> utility was new for the ISO POSIX-2:1993 standard. It represents a peaceful compromise between advocates of the historical <code>tar </code> and <code>cpio </code> utilities. </p>
<p> A fundamental difference between <code>cpio </code> and <code>tar </code> was in the way directories were treated. The <code>cpio </code> utility did not treat directories differently from other files, and to select a directory and its contents required that each file in the hierarchy be explicitly specified. For <code>tar</code>, a directory matched every file in the file hierarchy it rooted. </p>
<p> The <code>pax </code> utility offers both interfaces; by default, directories map into the file hierarchy they root. The <code>-d </code> option causes <code>pax </code> to skip any file not explicitly referenced, as <i>cpio </i> historically did. The <code>tar </code> - style behavior was chosen as the default because it was believed that this was the more common usage and because <code>tar </code> is the more commonly available interface, as it was historically provided on both System V and BSD implementations. </p>
<p> The data interchange format specification in this volume of IEEE Std 1003.1-2001 requires that processes with &quot;appropriate privileges&quot; shall always restore the ownership and permissions of extracted files exactly as archived. If viewed from the historic equivalence between superuser and &quot;appropriate privileges&quot;, there are two problems with this requirement. First, users running as superusers may unknowingly set dangerous permissions on extracted files. Second, it is needlessly limiting, in that superusers cannot extract files and own them as superuser unless the archive was created by the superuser. (It should be noted that restoration of ownerships and permissions for the superuser, by default, is historical practice in <i>cpio</i>, but not in <code>tar</code>.) In order to avoid these two problems, the <i>pax </i> specification has an additional &quot;privilege&quot; mechanism, the <code>-p </code> option. Only a <code>pax </code> invocation with the privileges needed, and which has the <code>-p </code> option set using the <code>e</code> specification character, has the &quot;appropriate privilege&quot; to restore full ownership and permission information. </p>
<p> Note also that this volume of IEEE Std 1003.1-2001 requires that the file ownership and access permissions shall be set, on extraction, in the same fashion as the <code><a href="/docs/linux/man/2-creat/">creat</a></code>(2) function when provided with the mode stored in the archive. This means that the file creation mask of the user is applied to the file permissions. </p>
<p> Users should note that directories may be created by <code>pax </code> while extracting files with permissions that are different from those that existed at the time the archive was created. When extracting sensitive information into a directory hierarchy that no longer exists, users are encouraged to set their file creation mask appropriately to protect these files during extraction. </p>
<p> The table of contents output is written to standard output to facilitate pipeline processing. </p>
<p> An early proposal had hard links displaying for all pathnames. This was removed because it complicates the output of the case where <code>-v </code> is not specified and does not match historical <code>cpio</code> usage. The hard-link information is available in the <code>-v </code> display. </p>
<p> The description of the <code>-l </code> option allows implementations to make hard links to symbolic links. IEEE Std 1003.1-2001 does not specify any way to create a hard link to a symbolic link, but many implementations provide this capability as an extension. If there are hard links to symbolic links when an archive is created, the implementation is required to archive the hard link in the archive (unless <code>-H </code> or <code>-L </code> is specified). When in <code>read </code> mode and in <code>copy</code> mode, implementations supporting hard links to symbolic links should use them when appropriate. </p>
<p> The archive formats inherited from the POSIX.1-1990 standard have certain restrictions that have been brought along from historical usage. For example, there are restrictions on the length of pathnames stored in the archive. When <code>pax is used in </code> <code>copy</code> (<code>-rw</code>) mode (copying directory hierarchies), the ability to use extensions from the <code>-x</code><i> pax </i> format overcomes these restrictions. </p>
<p> The default blocksize value of 5120 bytes for <code>cpio </code> was selected because it is one of the standard block-size values for <code>cpio</code>, set when the <code>-B </code> option is specified. (The other default block-size value for <code>cpio </code> is 512 bytes, and this was considered to be too small.) The default block value of 10240 bytes for <code>tar </code> was selected because that is the standard block-size value for BSD <code>tar</code>. The maximum block size of 32256 bytes (2^15-512 bytes) is the largest multiple of 512 bytes that fits into a signed 16-bit tape controller transfer register. There are known limitations in some historical systems that would prevent larger blocks from being accepted. Historical values were chosen to improve compatibility with historical scripts using <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1) or similar utilities to manipulate archives. Also, default block sizes for any file type other than character special file has been deleted from this volume of IEEE Std 1003.1-2001 as unimportant and not likely to affect the structure of the resulting archive. </p>
<p> Implementations are permitted to modify the block-size value based on the archive format or the device to which the archive is being written. This is to provide implementations with the opportunity to take advantage of special types of devices, and it should not be used without a great deal of consideration as it almost certainly decreases archive portability. </p>
<p> The intended use of the <code>-n </code> option was to permit extraction of one or more files from the archive without processing the entire archive. This was viewed by the standard developers as offering significant performance advantages over historical implementations. The <code>-n </code> option in early proposals had three effects; the first was to cause special characters in patterns to not be treated specially. The second was to cause only the first file that matched a pattern to be extracted. The third was to cause <code>pax </code> to write a diagnostic message to standard error when no file was found matching a specified pattern. Only the second behavior is retained by this volume of IEEE Std 1003.1-2001, for many reasons. First, it is in general not acceptable for a single option to have multiple effects. Second, the ability to make pattern matching characters act as normal characters is useful for parts of <code>pax</code> other than file extraction. Third, a finer degree of control over the special characters is useful because users may wish to normalize only a single special character in a single filename. Fourth, given a more general escape mechanism, the previous behavior of the <code>-n </code> option can be easily obtained using the <code>-s </code> option or a sed script. Finally, writing a diagnostic message when a pattern specified by the user is unmatched by any file is useful behavior in all cases. </p>
<p> In this version, the <code>-n </code> was removed from the copy mode synopsis of <code>pax</code>; it is inapplicable because there are no pattern operands specified in this mode. </p>
<p> There is another method than <code>pax </code> for copying subtrees in IEEE Std 1003.1-2001 described as part of the <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1) utility. Both methods are historical practice: <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1) provides a simpler, more intuitive interface, while <code>pax </code> offers a finer granularity of control. Each provides additional functionality to the other; in particular, <code>pax </code> maintains the hard-link structure of the hierarchy while <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1) does not. It is the intention of the standard developers that the results be similar (using appropriate option combinations in both utilities). The results are not required to be identical; there seemed insufficient gain to applications to balance the difficulty of implementations having to guarantee that the results would be exactly identical. </p>
<p> A single archive may span more than one file. It is suggested that implementations provide informative messages to the user on standard error whenever the archive file is changed. </p>
<p> The <code>-d </code> option (do not create intermediate directories not listed in the archive) found in early proposals was originally provided as a complement to the historic <code>-d </code> option of <code>cpio</code>. It has been deleted. </p>
<p> The <code>-s </code> option in early proposals specified a subset of the substitution command from the ed utility. As there was no reason for only a subset to be supported, the <code>-s </code> option is now compatible with the current ed specification. Since the delimiter can be any non-null character, the following usage with single spaces is valid: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pax -s&nbsp;<wbr>&quot;&nbsp;<wbr>foo bar&nbsp;<wbr>&quot;&nbsp;<wbr>...</code> </p>
<p> The <code>-t description is worded so as to note that this may cause the</code> access time update caused by some other activity (which occurs while the file is being read) to be overwritten. </p>
<p> The default behavior of <code>pax </code> with regard to file modification times is the same as historical implementations of <code>tar</code>. It is not the historical behavior of <code>cpio</code>. </p>
<p> Because the <code>-i </code> option uses <code>/dev/tty</code>, utilities without a controlling terminal are not able to use this option. </p>
<p> The <code>-y </code> option, found in early proposals, has been deleted because a line containing a single period for the <code>-i </code> option has equivalent functionality. The special lines for the <code>-i </code> option (a single period and the empty line) are historical practice in <code>cpio</code>. </p>
<p> In early drafts, a <code>-e</code><i> charmap</i> option was included to increase portability of files between systems using different coded character sets. This option was omitted because it was apparent that consensus could not be formed for it. In this version, the use of UTF-8 should be an adequate substitute. </p>
<p> The <code>-k </code> option was added to address international concerns about the dangers involved in the character set transformations of <code>-e</code> (if the target character set were different from the source, the filenames might be transformed into names matching existing files) and also was made more general to protect files transferred between file systems with different <i>{NAME_MAX} </i> values (truncating a filename on a smaller system might also inadvertently overwrite existing files). As stated, it prevents any overwriting, even if the target file is older than the source. This version adds more granularity of options to solve this problem by introducing the <code>-o invalid=</code><i>option</i> - specifically the UTF-8 action. (Note that an existing file that is named with a UTF-8 encoding is still subject to overwriting in this case. The <code>-k </code> option closes that loophole.) </p>
<p> Some of the file characteristics referenced in this volume of IEEE Std 1003.1-2001 might not be supported by some archive formats. For example, neither the <code>tar </code> nor <code>cpio </code> formats contain the file access time. For this reason, the <code>e </code> specification character has been provided, intended to cause all file characteristics specified in the archive to be retained. </p>
<p> It is required that extracted directories, by default, have their access and modification times and permissions set to the values specified in the archive. This has obvious problems in that the directories are almost certainly modified after being extracted and that directory permissions may not permit file creation. One possible solution is to create directories with the mode specified in the archive, as modified by the <i>umask </i> of the user, with sufficient permissions to allow file creation. After all files have been extracted, <code>pax </code> would then reset the access and modification times and permissions as necessary. </p>
<p> The list-mode formatting description borrows heavily from the one defined by the <code><a href="/docs/linux/man/1-printf/">printf</a></code>(1) utility. However, since there is no separate operand list to get conversion arguments, the format was extended to allow specifying the name of the conversion argument as part of the conversion specification. </p>
<p> The <code>T </code> conversion specifier allows time fields to be displayed in any of the date formats. Unlike the <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) utility, <code>pax </code> does not adjust the format when the date is less than six months in the past. This makes parsing the output more predictable. </p>
<p> The <code>D </code> conversion specifier handles the ability to display the major/minor or file size, as with <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), by using %-8(size)D. </p>
<p> The <code>L </code> conversion specifier handles the ls display for symbolic links. </p>
<p> Conversion specifiers were added to generate existing known types used for <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1). </p>
<h3>pax Interchange Format</h3>
<p> The new POSIX data interchange format was developed primarily to satisfy international concerns that the <code>ustar </code> and <code>cpio </code> formats did not provide for file, user, and group names encoded in characters outside a subset of the ISO/IEC 646:1991 standard. The standard developers realized that this new POSIX data interchange format should be very extensible because there were other requirements they foresaw in the near future: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> Support international character encodings and locale information </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Support security information (ACLs, and so on) </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Support future file types, such as realtime or contiguous files </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Include data areas for implementation use </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Support systems with words larger than 32 bits and timers with subsecond granularity </p>
 </dd></dl>
<p> The following were not goals for this format because these are better handled by separate utilities or are inappropriate for a portable format: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> Encryption </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Compression </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Data translation between locales and codesets </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> inode storage </p>
 </dd></dl>
<p> The format chosen to support the goals is an extension of the <code>ustar </code> format. Of the two formats previously available, only the <code>ustar </code> format was selected for extensions because: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> It was easier to extend in an upwards-compatible way. It offered version flags and header block type fields with room for future standardization. The <code>cpio </code> format, while possessing a more flexible file naming methodology, could not be extended without breaking some theoretical implementation or using a dummy filename that could be a legitimate filename. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> Industry experience since the original &quot;<code>tar</code>&nbsp;<wbr>wars&quot; fought in developing the ISO POSIX-1 standard has clearly been in favor of the <code>ustar </code> format, which is generally the default output format selected for <code>pax </code> implementations on new systems. </p>
 </dd></dl>
<p> The new format was designed with one additional goal in mind: reasonable behavior when an older <code>tar </code> or <code>pax </code> utility happened to read an archive. Since the POSIX.1-1990 standard mandated that a &quot;format-reading utility&quot; had to treat unrecognized <i>typeflag </i> values as regular files, this allowed the format to include all the extended information in a pseudo-regular file that preceded each real file. An option is given that allows the archive creator to set up reasonable names for these files on the older systems. Also, the normative text suggests that reasonable file access values be used for this <code>ustar </code> header block. Making these header files inaccessible for convenient reading and deleting would not be reasonable. File permissions of 600 or 700 are suggested. </p>
<p> The ustar <i>typeflag </i> field was used to accommodate the additional functionality of the new format rather than <i>magic </i> or <i>version</i> because the POSIX.1-1990 standard (and, by reference, the previous version of <code>pax</code>), mandated the behavior of the format-reading utility when it encountered an unknown <i>typeflag</i>, but was silent about the other two fields. </p>
<p> Early proposals of the first revision to IEEE Std 1003.1-2001 contained a proposed archive format that was based on compatibility with the standard for tape files (ISO 1001, similar to the format used historically on many mainframes and minicomputers). This format was overly complex and required considerable overhead in volume and header records. Furthermore, the standard developers felt that it would not be acceptable to the community of POSIX developers, so it was later changed to be a format more closely related to historical practice on POSIX systems. </p>
<p> The <i>prefix</i> and <i>name </i> split of pathnames in <code>ustar </code> was replaced by the single path extended header record for simplicity. </p>
<p> The concept of a global extended header (typeflag <code> g</code>) was controversial. If this were applied to an archive being recorded on magnetic tape, a few unreadable blocks at the beginning of the tape could be a serious problem; a utility attempting to extract as many files as possible from a damaged archive could lose a large percentage of file header information in this case. However, if the archive were on a reliable medium, such as a CD-ROM, the global extended header offers considerable potential size reductions by eliminating redundant information. Thus, the text warns against using the global method for unreliable media and provides a method for implanting global information in the extended header for each file, rather than in the <i>typeflag</i><code> g</code> records. </p>
<p> No facility for data translation or filtering on a per-file basis is included because the standard developers could not invent an interface that would allow this in an efficient manner. If a filter, such as encryption or compression, is to be applied to all the files, it is more efficient to apply the filter to the entire archive as a single file. The standard developers considered interfaces that would invoke a shell script for each file going into or out of the archive, but the system overhead in this approach was considered to be too high. </p>
<p> One such approach would be to have <code>filter= </code> records that give a pathname for an executable. When the program is invoked, the file and archive would be open for standard input/output and all the header fields would be available as environment variables or command-line arguments. The standard developers did discuss such schemes, but they were omitted from IEEE Std 1003.1-2001 due to concerns about excessive overhead. Also, the program itself would need to be in the archive if it were to be used portably. </p>
<p> There is currently no portable means of identifying the character set(s) used for a file in the file system. Therefore, <code>pax </code> has not been given a mechanism to generate charset records automatically. The only portable means of doing this is for the user to write the archive using the <i>-o charset=</i>string command line option. This assumes that all of the files in the archive use the same encoding. The &quot;implementation-defined&quot; text is included to allow for a system that can identify the encodings used for each of its files. </p>
<p> The table of standards that accompanies the charset record description is acknowledged to be very limited. Only a limited number of character set standards is reasonable for maximal interchange. Any character set is, of course, possible by prior agreement. It was suggested that EBCDIC be listed, but it was omitted because it is not defined by a formal standard. Formal standards, and then only those with reasonably large followings, can be included here, simply as a matter of practicality. The <i>&lt;value&gt;</i>s represent names of officially registered character sets in the format required by the ISO 2375:1985 standard. </p>
<p> The normal comma or &lt;blank&gt;-separated list rules are not followed in the case of keyword options to allow ease of argument parsing for <code>getopts</code>. </p>
<p> Further information on character encodings is in <code>pax </code> Archive <code>Character Set Encoding/Decoding</code>. </p>
<p> The standard developers have reserved keyword name space for vendor extensions. It is suggested that the format to be used is: </p>
<p> <code> VENDOR.</code><i>keyword</i> </p>
<p> where <code>VENDOR </code> is the name of the vendor or organization in all uppercase letters. It is further suggested that the keyword following the period be named differently than any of the standard keywords so that it could be used for future standardization, if appropriate, by omitting the <code>VENDOR </code> prefix. </p>
<p> The &lt;<i>length</i>&gt; field in the extended header record was included to make it simpler to step through the records, even if a record contains an unknown format (to a particular <code>pax</code>) with complex interactions of special characters. It also provides a minor integrity checkpoint within the records to aid a program attempting to recover files from a damaged archive. </p>
<p> There are no extended header versions of the <i>devmajor </i> and <i>devminor</i> fields because the unspecified format <code>ustar </code> header field should be sufficient. If they are not, vendor-specific extended keywords (such as <code>VENDOR.devmajor</code>) should be used. </p>
<p> Device and i-number labeling of files was not adopted from <code>cpio</code>; files are interchanged strictly on a symbolic name basis, as in <code>ustar</code>. </p>
<p> Just as with the <code>ustar </code> format descriptions, the new format makes no special arrangements for multi-volume archives. Each of the <code>pax</code> archive types is assumed to be inside a single POSIX file and splitting that file over multiple volumes (diskettes, tape cartridges, and so on), processing their labels, and mounting each in the proper sequence are considered to be implementation details that cannot be described portably. </p>
<p> The <code>pax </code> format is intended for interchange, not only for backup on a single (family of) systems. It is not as densely packed as might be possible for backup: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> It contains information as coded characters that could be coded in binary. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> It identifies extended records with name fields that could be omitted in favor of a fixed-field layout. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> It translates names into a portable character set and identifies locale-related information, both of which are probably unnecessary for backup. </p>
 </dd></dl>
<p> The requirements on restoring from an archive are slightly different from the historical wording, allowing for non-monolithic privilege to bring forward as much as possible. In particular, attributes such as &quot;high performance file&quot; might be broadly but not universally granted while set-user-ID or <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2) might be much more restricted. There is no implication in IEEE Std 1003.1-2001 that the security information be honored after it is restored to the file hierarchy, in spite of what might be improperly inferred by the silence on that topic. That is a topic for another standard. </p>
<p> Links are recorded in the fashion described here because a link can be to any file type. It is desirable in general to be able to restore part of an archive selectively and restore all of those files completely. If the data is not associated with each link, it is not possible to do this. However, the data associated with a file can be large, and when selective restoration is not needed, this can be a significant burden. The archive is structured so that files that have no associated data can always be restored by the name of any link name of any link, and the user may choose whether data is recorded with each instance of a file that contains data. The format permits mixing of both types of links in a single archive; this can be done for special needs, and <code>pax </code> is expected to interpret such archives on input properly, despite the fact that there is no <code>pax </code> option that would force this mixed case on output. (When <code>-o</code><i> linkdata </i> is used, the output must contain the duplicate data, but the implementation is free to include it or omit it when <code>-o</code><i> linkdata </i> is not used.) </p>
<p> The time values are included as extended header records for those implementations needing more than the eleven octal digits allowed by the <code>ustar </code> format. Portable file timestamps cannot be negative. If <code>pax </code> encounters a file with a negative timestamp in <code>copy </code> or <code>write </code> mode, it can reject the file, substitute a non-negative timestamp, or generate a non-portable timestamp with a leading &#8216;-&#8216;. Even though some implementations can support finer file-time granularities than seconds, the normative text requires support only for seconds since the Epoch because the ISO POSIX-1 standard states them that way. The <code>ustar </code> format includes only <i>mtime</i>; the new format adds <i>atime </i> and <i>ctime </i> for symmetry. The atime access time restored to the file system will be affected by the <code>-p</code><i> a</i> and <code>-p</code><i> e</i> options. The <i>ctime </i> creation time (actually <i>inode </i> modification time) is described with &quot;appropriate privilege&quot; so that it can be ignored when writing to the file system. POSIX does not provide a portable means to change file creation time. Nothing is intended to prevent a non-portable implementation of <code>pax </code> from restoring the value. </p>
<p> The <i>gid</i>, <i>size</i>, and <i>uid </i> extended header records were included to allow expansion beyond the sizes specified in the regular <code>tar</code> header. New file system architectures are emerging that will exhaust the 12-digit size field. There are probably not many systems requiring more than 8 digits for user and group IDs, but the extended header values were included for completeness, allowing overrides for all of the decimal values in the <code>tar</code> header. </p>
<p> The standard developers intended to describe the effective results of <code>pax </code> with regard to file ownerships and permissions; implementations are not restricted in timing or sequencing the restoration of such, provided the results are as specified. </p>
<p> Much of the text describing the extended headers refers to use in &quot;<code>write</code> or <code>copy</code> modes&quot;. The <code>copy </code> mode references are due to the normative text: &quot;The effect of the copy shall be as if the copied files were written to an archive file and then subsequently extracted ...&quot;. There is certainly no way to test whether <code>pax </code> is actually generating the extended headers in <code>copy </code> mode, but the effects must be as if it had. </p>
<h3>pax Archive Character Set Encoding/Decoding</h3>
<p> There is a need to exchange archives of files between systems of different native codesets. Filenames, group names, and user names must be preserved to the fullest extent possible when an archive is read on the receiving platform. Translation of the contents of files is not within the scope of the <code>pax </code> utility. </p>
<p> There will also be the need to represent characters that are not available on the receiving platform. These unsupported characters cannot be automatically folded to the local set of characters due to the chance of collisions. This could result in overwriting previous extracted files from the archive or pre-existing files on the system. </p>
<p> For these reasons, the codeset used to represent characters within the extended header records of the <code>pax </code> archive must be sufficiently rich to handle all commonly used character sets. The fields requiring translation include, at a minimum, filenames, user names, group names, and link pathnames. Implementations may wish to have localized extended keywords that use non-portable characters. </p>
<p> The standard developers considered the following options: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> The archive creator specifies the well-defined name of the source codeset. The receiver must then recognize the codeset name and perform the appropriate translations to the destination codeset. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> The archive creator includes within the archive the character mapping table for the source codeset used to encode extended header records. The receiver must then read the character mapping table and perform the appropriate translations to the destination codeset. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> The archive creator translates the extended header records in the source codeset into a canonical form. The receiver must then perform the appropriate translations to the destination codeset. </p>
 </dd></dl>
<p> The approach that incorporates the name of the source codeset poses the problem of codeset name registration, and makes the archive useless to <code>pax </code> archive decoders that do not recognize that codeset. </p>
<p> Because parts of an archive may be corrupted, the standard developers felt that including the character map of the source codeset was too fragile. The loss of this one key component could result in making the entire archive useless. (The difference between this and the global extended header decision was that the latter has a workaround-duplicating extended header records on unreliable media-but this would be too burdensome for large character set maps.) </p>
<p> Both of the above approaches also put an undue burden on the <code>pax</code> archive receiver to handle the cross-product of all source and destination codesets. </p>
<p> To simplify the translation from the source codeset to the canonical form and from the canonical form to the destination codeset, the standard developers decided that the internal representation should be a stateless encoding. A stateless encoding is one where each codepoint has the same meaning, without regard to the decoder being in a specific state. An example of a stateful encoding would be the Japanese Shift-JIS; an example of a stateless encoding would be the ISO/IEC 646:1991 standard (equivalent to 7-bit ASCII). </p>
<p> For these reasons, the standard developers decided to adopt a canonical format for the representation of file information strings. The obvious, well-endorsed candidate is the ISO/IEC 10646-1:2000 standard (based in part on Unicode), which can be used to represent the characters of virtually all standardized character sets. The standard developers initially agreed upon using UCS2 (16-bit Unicode) as the internal representation. This repertoire of characters provides a sufficiently rich set to represent all commonly-used codesets. </p>
<p> However, the standard developers found that the 16-bit Unicode representation had some problems. It forced the issue of standardizing byte ordering. The 2-byte length of each character made the extended header records twice as long for the case of strings coded entirely from historical 7-bit ASCII. For these reasons, the standard developers chose the UTF-8 defined in the ISO/IEC 10646-1:2000 standard. This multi-byte representation encodes UCS2 or UCS4 characters reliably and deterministically, eliminating the need for a canonical byte ordering. In addition, NUL octets and other characters possibly confusing to POSIX file systems do not appear, except to represent themselves. It was realized that certain national codesets take up more space after the encoding, due to their placement within the UCS range; it was felt that the usefulness of the encoding of the names outweighs the disadvantage of size increase for file, user, and group names. </p>
<p> The encoding of UTF-8 is as follows: </p>
<table>
<tr VALIGN=top>
<td><code>UCS4 Hex Encoding</code></td>
<td><code>UTF-8 Binary Encoding</code>
</td>
</tr>
<tr VALIGN=top>
<td>00000000-0000007F</td>
<td>0xxxxxxx
</td>
</tr>
<tr VALIGN=top>
<td>00000080-000007FF</td>
<td>110xxxxx 10xxxxxx
</td>
</tr>
<tr VALIGN=top>
<td>00000800-0000FFFF</td>
<td>1110xxxx 10xxxxxx 10xxxxxx
</td>
</tr>
<tr VALIGN=top>
<td>00010000-001FFFFF</td>
<td>11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
</td>
</tr>
<tr VALIGN=top>
<td>00200000-03FFFFFF</td>
<td>111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
</td>
</tr>
<tr VALIGN=top>
<td>04000000-7FFFFFFF</td>
<td>1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
</td>
</tr>
</table>
<p> where each &#8216;<i>x</i>&#8216; represents a bit value from the character being translated. </p>
<h3>ustar Interchange Format</h3>
<p> The description of the <code>ustar </code> format reflects numerous enhancements over pre-1988 versions of the historical <code>tar </code> utility. The goal of these changes was not only to provide the functional enhancements desired, but also to retain compatibility between new and old versions. This compatibility has been retained. Archives written using the old archive format are compatible with the new format. </p>
<p> Implementors should be aware that the previous file format did not include a mechanism to archive directory type files. For this reason, the convention of using a filename ending with slash was adopted to specify a directory on the archive. </p>
<p> The total size of the <i>name </i> and <i>prefix </i> fields have been set to meet the minimum requirements for <i>{PATH_MAX}</i> If a pathname will fit within the <i>name </i> field, it is recommended that the pathname be stored there without the use of the <i>prefix </i> field. Although the name field is known to be too small to contain <i>{PATH_MAX}</i> characters, the value was not changed in this version of the archive file format to retain backwards-compatibility, and instead the <i>prefix </i> was introduced. Also, because of the earlier version of the format, there is no way to remove the restriction on the <i>linkname </i> field being limited in size to just that of the <i>name</i> field. </p>
<p> The <i>size </i> field is required to be meaningful in all implementation extensions, although it could be zero. This is required so that the data blocks can always be properly counted. </p>
<p> It is suggested that if device special files need to be represented that cannot be represented in the standard format, that one of the extension types (<code>A</code>-<code>Z</code>) be used, and that the additional information for the special file be represented as data and be reflected in the <i>size </i> field. </p>
<p> Attempting to restore a special file type, where it is converted to ordinary data and conflicts with an existing filename, need not be specially detected by the utility. If run as an ordinary user, <code>pax </code> should not be able to overwrite the entries in, for example, <code>/dev </code> in any case (whether the file is converted to another type or not). If run as a privileged user, it should be able to do so, and it would be considered a bug if it did not. The same is true of ordinary data files and similarly named special files; it is impossible to anticipate the needs of the user (who could really intend to overwrite the file), so the behavior should be predictable (and thus regular) and rely on the protection system as required. </p>
<p> The value <code>7 </code> in the <i>typeflag </i> field is intended to define how contiguous files can be stored in a <code>ustar </code> archive. IEEE Std 1003.1-2001 does not require the contiguous file extension, but does define a standard way of archiving such files so that all conforming systems can interpret these file types in a meaningful and consistent manner. On a system that does not support extended file types, the <code>pax </code> utility should do the best it can with the file and go on to the next. </p>
<p> The file protection modes are those conventionally used by the <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) utility. This is extended beyond the usage in the ISO POSIX-2 standard to support the &quot;shared text&quot; or &quot;sticky&quot; bit. It is intended that the conformance document should not document anything beyond the existence of and support of such a mode. Further extensions are expected to these bits, particularly with overloading the set-user-ID and set-group-ID flags. </p>
<h3>cpio Interchange Format</h3>
<p> The reference to appropriate privilege in the <code>cpio </code> format refers to an error on standard output; the <code>ustar </code> format does not make comparable statements. </p>
<p> The model for this format was the historical System V <code>cpio -c </code> data interchange format. This model documents the portable version of the <code>cpio </code> format and not the binary version. It has the flexibility to transfer data of any type described within IEEE Std 1003.1-2001, yet is extensible to transfer data types specific to extensions beyond IEEE Std 1003.1-2001 (for example, contiguous files). Because it describes existing practice, there is no question of maintaining upwards-compatibility. </p>
<h3>cpio Header</h3>
<p> There has been some concern that the size of the <i>c_ino </i> field of the header is too small to handle those systems that have very large inode numbers. However, the <i>c_ino </i> field in the header is used strictly as a hard-link resolution mechanism for archives. It is not necessarily the same value as the inode number of the file in the location from which that file is extracted. </p>
<p> The name <i>c_magic </i> is based on historical usage. </p>
<h3>cpio Filename</h3>
<p> For most historical implementations of the <code>cpio </code> utility, <i>{PATH_MAX} </i> octets can be used to describe the pathname without the addition of any other header fields (the NUL character would be included in this count). <i>{PATH_MAX} </i> is the minimum value for pathname size, documented as 256 bytes. However, an implementation may use <i>c_namesize </i> to determine the exact length of the pathname. With the current description of the <code>&lt;cpio.h&gt; </code> header, this pathname size can be as large as a number that is described in six octal digits. </p>
<p> Two values are documented under the <i>c_mode</i> field values to provide for extensibility for known file types: </p>
<dl>
<dt><code>0110 000</code></dt>
<dd> <p> Reserved for contiguous files. The implementation may treat the rest of the information for this archive like a regular file. If this file type is undefined, the implementation may create the file as a regular file. </p>
 </dd></dl>
<p> This provides for extensibility of the <code>cpio </code> format while allowing for the ability to read old archives. Files of an unknown type may be read as &quot;regular files&quot; on some implementations. On a system that does not support extended file types, the <code>pax </code> utility should do the best it can with the file and go on to the next. </p>
<h2>FUTURE DIRECTIONS</h2>
<p> None. </p>
<p> <br />
 <i>End of informative sections.</i> <br />
 </p>
<hr />
<h2>SEE ALSO</h2>
<p> Shell Command Language, <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1), <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1), <code><a href="/docs/linux/man/1-getopts/">getopts</a></code>(1), <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), the Base Definitions volume of IEEE Std 1003.1-2001, <code>&lt;cpio.h&gt;</code>, the System Interfaces volume of IEEE Std 1003.1-2001, <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-creat/">creat</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2). </p>
<h2>CHANGE HISTORY</h2>
<p> First released in Issue 4. </p>
<h3>Issue 5</h3>
<p> A note is added to the APPLICATION USAGE indicating that the <code>cpio</code> and <code>tar </code> formats can only support files up to 8 gigabytes in size. </p>
<h3>Issue 6</h3>
<p> The <code>pax </code> utility is aligned with the IEEE P1003.2b draft standard: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> Support has been added for symbolic links in the options and interchange formats. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> A new format has been devised, based on extensions to <code>ustar</code>. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> References to the &quot;extended&quot; <code>tar </code> and <code>cpio </code> formats derived from the POSIX.1-1990 standard have been changed to remove the &quot;extended&quot; adjective because this could cause confusion with the extended <code>tar </code> header added in this revision. (All references to tar are actually to <code>ustar</code>.) </p>
 </dd></dl>
<p> The <code>TZ </code> entry is added to the ENVIRONMENT VARIABLES section. </p>
<p> IEEE PASC Interpretation 1003.2 #168 is applied, clarifying that <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2) and <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3) calls can ignore an [EEXIST] error when extracting an archive. </p>
<p> IEEE PASC Interpretation 1003.2 #180 is applied, clarifying how extracted files are created when in <code>read </code> mode. </p>
<p> IEEE PASC Interpretation 1003.2 #181 is applied, clarifying the description of the <code>-t </code> option. </p>
<p> IEEE PASC Interpretation 1003.2 #195 is applied. </p>
<p> IEEE PASC Interpretation 1003.2 #206 is applied, clarifying the handling of links for the <code>-H</code>, <code>-L</code>, and <code>-l </code> options. </p>
<p> IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/35 is applied, adding the process ID of the <code>pax </code> process into certain fields. This change provides a method for the implementation to ensure that different instances of <code>pax </code> extracting a file named <code>/a/b/foo </code> will not collide when processing the extended header information associated with <code>foo</code>. </p>
<p> IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/36 is applied, changing <code>-x B </code> to <code>-x pax </code> in the OPTIONS section. </p>
<p> IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/20 is applied, updating the SYNOPSIS to be consistent with the normative text. </p>
<p> IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/21 is applied, updating the DESCRIPTION to describe the behavior when files to be linked are symbolic links and the system is not capable of making hard links to symbolic links. </p>
<p> IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/22 is applied, updating the OPTIONS section to describe the behavior for how multiple options are to be handled. </p>
<p> IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/23 is applied, updating the <code>write </code> option within the OPTIONS section. </p>
<p> IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/24 is applied, adding a paragraph into the OPTIONS section that states that specifying more than one of the mutually-exclusive options (<code>-H</code> and <code>-L</code>) is not considered an error and that the last option specified will determine the behavior of the utility. </p>
<p> IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/25 is applied, removing the <i>ctime </i> paragraph within the EXTENDED DESCRIPTION. There is a contradiction in the definition of the <i>ctime </i> keyword for the <code>pax </code> extended header, in that the <i>st_ctime </i> member of the <code>stat </code> structure does not refer to a file creation time. No field in the standard stat structure from <code>&lt;sys/stat.h&gt; </code> includes a file creation time. </p>
<p> IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/26 is applied, making it clear that <i>typeflag </i> <code>1 </code> RB ( ustar Interchange Format) applies not only to files that are hard-linked, but also to files that are aliased via symlinks. </p>
<p> IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/27 is applied, clarifying the <code>cpio </code> <i>c_nlink</i> field. </p>
<p> End of quoted text from the POSIX.1-2001 standard.  </p>
<h2>OTHER OPTIONS</h2>
<p> The following <i>other options</i> are implemented as extension to the POSIX standard. Note that some other non-POSIX options are mentioned in <i>-help</i> and <i>-xhelp</i> output - these are also supported in <code><a href="/docs/linux/man/1-spax/">spax</a></code>(1) and are well described in <code><a href="/docs/linux/man/1-star/">star</a></code>(1) manual page. </p>
<dl>
<dt><code>-help</code></dt>
<dd> <p> Prints a summary of the most important options for <code><a href="/docs/linux/man/1-spax/">spax</a></code>(1) and exits. </p>
 </dd>
<dt><code>-xhelp</code></dt>
<dd> <p> Prints a summary of the less important options for <code><a href="/docs/linux/man/1-spax/">spax</a></code>(1) and exits. </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Prints the <code>spax</code> version number string and exists. </p>
 </dd>
<dt><code>-do-statistics</code></dt>
<dd> <p> Print statistic messages at the end of a <code><a href="/docs/linux/man/1-spax/">spax</a></code>(1) run. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<h2>ENVIRONMENT</h2>
<h2>FILES</h2>
<h2>SEE ALSO</h2>
<h2>DIAGNOSTICS</h2>
<h2>NOTES</h2>
<p> The Institute of Electrical and Electronics Engineers and The Open Group, have given us permission to reprint portions of their documentation. In the following statement, the phrase ``this text&#8217;&#8216; refers to portions of the system documentation. </p>
<p> Portions of this text are reprinted and reproduced in electronic form in the <code>sfind </code> manual, from IEEE Std 1003.1, 2004 Edition, Standard for Information Technology -- Portable Operating System Interface (POSIX), The Open Group Base Specifications Issue 6, Copyright (C) 2001-2004 by the Institute of Electrical and Electronics Engineers, Inc and The Open Group. In the event of any discrepancy between these versions and the original IEEE and The Open Group Standard, the original IEEE and The Open Group Standard is the referee document. The original Standard can be obtained online at <code><a rel="nofollow" href="http://www.opengroup.org/unix/online.html">http://www.opengroup.org/unix/online.html</a></code>.  </p>
<h2>BUGS</h2>
<h2>AUTHOR</h2>
<pre><code>Joerg Schilling
Seestr. 110
D-13353 Berlin
Germany
</code></pre>
<p> Mail bugs and suggestions to: </p>
<p> <code>schilling [at] fokus.fraunhofer.de</code> or <code>js [at] cs.tu-berlin.de</code> or <code>joerg [at] schily.isdn.cs.tu-berlin.de</code> </p>
