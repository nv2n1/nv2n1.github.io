---
title: "opax(1)"
name: "opax"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opax/"
description: "opax – read and write file archives and copy directory hierarchies (OpenBSD pax implementation)"
---

<h2>NAME</h2>
<p> <code>opax</code> &#8211; read and write file archives and copy directory hierarchies (OpenBSD <i>pax</i> implementation)</p>
<h2>SYNOPSIS</h2>
<p> [-<code>0cdOnvz</code> ] -words [-<code>f </code><i>archive</i> ] -words [-<code>s </code><i>replstr</i> ] <i>&#8230;</i> -words [-<code>U </code><i>user</i> ] <i>&#8230;</i> -words [-<code>G </code><i>group</i> ] <i>&#8230;</i> -words [-<code>T</code> [<i>from_date</i> ] [<i>,to_date</i> ] ] <i>&#8230;</i> [<i>pattern &#8230;</i> ]<br />
 &#8211;<code>r</code> [-<code>cdiknuvzDOYZ</code> ] -words [-<code>f </code><i>archive</i> ] -words [-<code>o </code><i>options</i> ] <i>&#8230;</i> -words [-<code>p </code><i>string</i> ] <i>&#8230;</i> -words [-<code>s </code><i>replstr</i> ] <i>&#8230;</i> [-<code>E </code><i>limit</i> ] -words [-<code>U </code><i>user</i> ] <i>&#8230;</i> -words [-<code>G </code><i>group</i> ] <i>&#8230;</i> -words [-<code>T</code> [<i>from_date</i> ] [<i>,to_date</i> ] ] <i>&#8230;</i> [<i>pattern &#8230;</i> ]<br />
 &#8211;<code>w</code> [-<code>0dituvzHLOPX</code> ] -words [-<code>b </code><i>blocksize</i> ] [[-<code>a</code> ] [-<code>f </code><i>archive</i> ] ] -words [-<code>x </code><i>format</i> ] -words [-<code>s </code><i>replstr</i> ] <i>&#8230;</i> -words [-<code>o </code><i>options</i> ] <i>&#8230;</i> -words [-<code>U </code><i>user</i> ] <i>&#8230;</i> -words [-<code>G </code><i>group</i> ] <i>&#8230;</i> -words [-<code>B </code><i>bytes</i> ] -words [-<code>T</code> [<i>from_date</i> ] [<i>,to_date</i> ] [<i>/[c][m]</i> ] ] <i>&#8230;</i> [<i>file &#8230;</i> ]<br />
 &#8211;<code>r</code> &#8211;<code>w</code> [-<code>0diklntuvDHLOPXYZ</code> ] -words [-<code>p </code><i>string</i> ] <i>&#8230;</i> -words [-<code>s </code><i>replstr</i> ] <i>&#8230;</i> -words [-<code>U </code><i>user</i> ] <i>&#8230;</i> -words [-<code>G </code><i>group</i> ] <i>&#8230;</i> -words [-<code>T</code> [<i>from_date</i> ] [<i>,to_date</i> ] [<i>/[c][m]</i> ] ] <i>&#8230;</i> [<i>file &#8230;</i> ] <i>directory</i></p>
<h2>DESCRIPTION</h2>
<p> will read, write, and list the members of an archive file, and will copy directory hierarchies. operation is independent of the specific archive format, and supports a wide variety of different archive formats. A list of supported archive formats can be found under the description of the &#8211;<code>x</code> option. </p>
<p> The presence of the &#8211;<code>r</code> and the &#8211;<code>w</code> options specifies which of the following functional modes will operate under: <i>list , read , write</i> and <i>copy</i></p>
<dl>
<dt><code>&lt;none&gt;</code></p>
<dd> <i>List</i> will write to standard output a table of contents of the members of the archive file read from standard input, whose pathnames match the specified <i>patterns</i> The table of contents contains one filename per line and is written using single line buffering.</p>
<dt><code>-r</code></p>
<dd> <i>Read</i> extracts the members of the archive file read from the standard input, with pathnames matching the specified <i>patterns</i> The archive format and blocking is automatically determined on input. When an extracted file is a directory, the entire file hierarchy rooted at that directory is extracted. All extracted files are created relative to the current file hierarchy. The setting of ownership, access and modification times, and file mode of the extracted files are discussed in more detail under the &#8211;<code>p</code> option.</p>
<dt><code>-w</code></p>
<dd> <i>Write</i> writes an archive containing the <i>file</i> operands to standard output using the specified archive format. When no <i>file</i> operands are specified, a list of files to copy with one per line is read from standard input. When a <i>file</i> operand is also a directory, the entire file hierarchy rooted at that directory will be included.</p>
<dt><code>-r -w</code></p>
<dd> <i>Copy</i> copies the <i>file</i> operands to the destination <i>directory</i> When no <i>file</i> operands are specified, a list of files to copy with one per line is read from the standard input. When a <i>file</i> operand is also a directory the entire file hierarchy rooted at that directory will be included. The effect of the <i>copy</i> is as if the copied files were written to an archive file and then subsequently extracted, except that there may be hard links between the original and the copied files (see the &#8211;<code>l</code> option below). </p>
<p> <i>Warning</i> The destination <i>directory</i> must not be one of the <i>file</i> operands or a member of a file hierarchy rooted at one of the <i>file</i> operands. The result of a <i>copy</i> under these conditions is unpredictable.</dl>
<p> While processing a damaged archive during a <i>read</i> or <i>list</i> operation, will attempt to recover from media defects and will search through the archive to locate and process the largest number of archive members possible (see the &#8211;<code>E</code> option for more details on error handling). </p>
<p> The <i>directory</i> operand specifies a destination directory pathname. If the <i>directory</i> operand does not exist, or it is not writable by the user, or it is not of type directory, will exit with a non-zero exit status. </p>
<p> The <i>pattern</i> operand is used to select one or more pathnames of archive members. Archive members are selected using the pattern matching notation described by <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3). When the <i>pattern</i> operand is not supplied, all members of the archive will be selected. When a <i>pattern</i> matches a directory, the entire file hierarchy rooted at that directory will be selected. When a <i>pattern</i> operand does not select at least one archive member, will write these <i>pattern</i> operands in a diagnostic message to standard error and then exit with a non-zero exit status. </p>
<p> The <i>file</i> operand specifies the pathname of a file to be copied or archived. When a <i>file</i> operand does not select at least one archive member, will write these <i>file</i> operand pathnames in a diagnostic message to standard error and then exit with a non-zero exit status. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-r</code></p>
<dd> Read an archive file from standard input and extract the specified <i>files</i> If any intermediate directories are needed in order to extract an archive member, these directories will be created as if <a href="/docs/linux/man/2-mkdir/">mkdir</a>(2) was called with the bitwise inclusive <code>OR</code> of <code>S_IRWXU , S_IRWXG</code> and <code>S_IRWXO</code> as the mode argument. When the selected archive format supports the specification of linked files and these files cannot be linked while the archive is being extracted, will write a diagnostic message to standard error and exit with a non-zero exit status at the completion of operation.</p>
<dt><code>-w</code></p>
<dd> Write files to the standard output in the specified archive format. When no <i>file</i> operands are specified, standard input is read for a list of pathnames with one per line without any leading or trailing Aq blanks .</p>
<dt><code>-a</code></p>
<dd> Append <i>files</i> to the end of an archive that was previously written. If an archive format is not specified with a &#8211;<code>x</code> option, the format currently being used in the archive will be selected. Any attempt to append to an archive in a format different from the format already used in the archive will cause to exit immediately with a non-zero exit status. The blocking size used in the archive volume where writing starts will continue to be used for the remainder of that archive volume. </p>
<p> <i>Warning</i> Many storage devices are not able to support the operations necessary to perform an append operation. Any attempt to append to an archive stored on such a device may damage the archive or have other unpredictable results. Tape drives in particular are more likely to not support an append operation. An archive stored in a regular file system file or on a disk device will usually support an append operation.</p>
<dt><code>-0</code></p>
<dd> Use the NUL (`
