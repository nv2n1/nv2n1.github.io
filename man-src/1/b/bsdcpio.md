---
title: "bsdcpio(1)"
name: "bsdcpio"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsdcpio/"
description: "cpio – copy files to and from archives"
---

<h2>NAME</h2>
<p> <code>cpio</code> &#8211; copy files to and from archives</p>
<h2>SYNOPSIS</h2>
<p> Br q Fl i [<i>options</i> ] [<i>pattern &#8230;</i> ] [<i>&lt; archive</i> ]<br />
 Br q Fl o [<i>options</i> ] <i>&lt; name-list</i> [<i>&gt; archive</i> ]<br />
 Br q Fl p [<i>options</i> ] <i>dest-dir</i> <i>&lt; name-list</i></p>
<h2>DESCRIPTION</h2>
<p> copies files between archives and directories. This implementation can extract from tar, pax, cpio, zip, jar, ar, and ISO 9660 cdrom images and can create tar, pax, cpio, ar, and shar archives. </p>
<p> The first option to is a mode indicator from the following list:</p>
<dl>
<dt><code>-i</code></dt>
<dd> Input. Read an archive from standard input (unless overridden) and extract the contents to disk or (if the &#8211;<code>t</code> option is specified) list the contents to standard output. If one or more file patterns are specified, only files matching one of the patterns will be extracted.</dd>
<dt><code>-o</code></dt>
<dd> Output. Read a list of filenames from standard input and produce a new archive on standard output (unless overridden) containing the specified items.</dd>
<dt><code>-p</code></dt>
<dd> Pass-through. Read a list of filenames from standard input and copy the files to the specified directory.</dd></dl>
<h2>OPTIONS</h2>
<p> Unless specifically stated otherwise, options are applicable in all operating modes.</p>
<dl>
<dt><code>-0 , &#8211;null</code></dt>
<dd> Read filenames separated by NUL characters instead of newlines. This is necessary if any of the filenames being read might contain newlines.</dd>
<dt><code>-A</code></dt>
<dd> (o mode only) Append to the specified archive. (Not yet implemented.)</dd>
<dt><code>-a</code></dt>
<dd> (o and p modes) Reset access times on files after they are read.</dd>
<dt><code>-B</code></dt>
<dd> (o mode only) Block output to records of 5120 bytes.</dd>
<dt><code>-C </code><i>size</i></dt>
<dd> (o mode only) Block output to records of <i>size</i> bytes.</dd>
<dt><code>-c</code></dt>
<dd> (o mode only) Use the old POSIX portable character format. Equivalent to &#8211;<code>-format </code><i>odc</i></dd>
<dt><code>-d , &#8211;make-directories</code></dt>
<dd> (i and p modes) Create directories as necessary.</dd>
<dt><code>-E </code><i>file</i></dt>
<dd> (i mode only) Read list of file name patterns from <i>file</i> to list and extract.</dd>
<dt><code>-F </code><i>file , &#8211;</i><code>-file </code><i>file</i></dt>
<dd> Read archive from or write archive to <i>file</i></dd>
<dt><code>-f </code><i>pattern</i></dt>
<dd> (i mode only) Ignore files that match <i>pattern</i></dd>
<dt><code>-H </code><i>format , &#8211;</i><code>-format </code><i>format</i></dt>
<dd> (o mode only) Produce the output archive in the specified format. Supported formats include: </dd>
<dl>
<dt><i>cpio</i></dt>
<dd> Synonym for <i>odc</i></dd>
<dt><i>newc</i></dt>
<dd> The SVR4 portable cpio format.</dd>
<dt><i>odc</i></dt>
<dd> The old POSIX.1 portable octet-oriented cpio format.</dd>
<dt><i>pax</i></dt>
<dd> The POSIX.1 pax format, an extension of the ustar format.</dd>
<dt><i>ustar</i></dt>
<dd> The POSIX.1 tar format.</dd></dl>
<p> The default format is <i>odc</i> See libarchive-formats5 for more complete information about the formats currently supported by the underlying libarchive(3) library.</p>
<dt><code>-h , &#8211;help</code></dt>
<dd> Print usage information.</dd>
<dt><code>-I </code><i>file</i></dt>
<dd> Read archive from <i>file</i></dd>
<dt><code>-i , &#8211;extract</code></dt>
<dd> Input mode. See above for description.</dd>
<dt><code>&#8211;insecure</code></dt>
<dd> (i and p mode only) Disable security checks during extraction or copying. This allows extraction via symbolic links and path names containing `..&#8217; in the name.</dd>
<dt><code>-J , &#8211;xz</code></dt>
<dd> (o mode only) Compress the file with xz-compatible compression before writing it. In input mode, this option is ignored; xz compression is recognized automatically on input.</dd>
<dt><code>-j</code></dt>
<dd> Synonym for &#8211;<code>y</code></dd>
<dt><code>-L</code></dt>
<dd> (o and p modes) All symbolic links will be followed. Normally, symbolic links are archived and copied as symbolic links. With this option, the target of the link will be archived or copied instead.</dd>
<dt><code>-l , &#8211;link</code></dt>
<dd> (p mode only) Create links from the target directory to the original files, instead of copying.</dd>
<dt><code>&#8211;lrzip</code></dt>
<dd> (o mode only) Compress the resulting archive with <a href="/docs/linux/man/1-lrzip/">lrzip</a>(1). In input mode, this option is ignored.</dd>
<dt><code>&#8211;lzma</code></dt>
<dd> (o mode only) Compress the file with lzma-compatible compression before writing it. In input mode, this option is ignored; lzma compression is recognized automatically on input.</dd>
<dt><code>&#8211;lzop</code></dt>
<dd> (o mode only) Compress the resulting archive with <a href="/docs/linux/man/1-lzop/">lzop</a>(1). In input mode, this option is ignored.</dd>
<dt><code>-m , &#8211;preserve-modification-time</code></dt>
<dd> (i and p modes) Set file modification time on created files to match those in the source.</dd>
<dt><code>-n , &#8211;numeric-uid-gid</code></dt>
<dd> (i mode, only with &#8211;<code>t</code> Display numeric uid and gid. By default, displays the user and group names when they are provided in the archive, or looks up the user and group names in the system password database.</dd>
<dt><code>&#8211;no-preserve-owner</code></dt>
<dd> (i mode only) Do not attempt to restore file ownership. This is the default when run by non-root users.</dd>
<dt><code>-O </code><i>file</i></dt>
<dd> Write archive to <i>file</i></dd>
<dt><code>-o , &#8211;create</code></dt>
<dd> Output mode. See above for description.</dd>
<dt><code>-p , &#8211;pass-through</code></dt>
<dd> Pass-through mode. See above for description.</dd>
<dt><code>&#8211;preserve-owner</code></dt>
<dd> (i mode only) Restore file ownership. This is the default when run by the root user.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> Suppress unnecessary messages.</dd>
<dt><code>-R </code>[user [: [group , &#8211;<code>-owner </code>[user [: [group ] ] ] ] ] ]</dt>
<dd> Set the owner and/or group on files in the output. If group is specified with no user (for example, &#8211;<code>R </code><i>:wheel</i> then the group will be set but not the user. If the user is specified with a trailing colon and no group (for example, &#8211;<code>R </code><i>root:</i> then the group will be set to the user&#8217;s default group. If the user is specified with no trailing colon, then the user will be set but not the group. In &#8211;<code>i</code> and &#8211;<code>p</code> modes, this option can only be used by the super-user. (For compatibility, a period can be used in place of the colon.)</dd>
<dt><code>-r</code></dt>
<dd> (All modes.) Rename files interactively. For each file, a prompt is written to /dev/tty containing the name of the file and a line is read from /dev/tty If the line read is blank, the file is skipped. If the line contains a single period, the file is processed normally. Otherwise, the line is taken to be the new name of the file.</dd>
<dt><code>-t , &#8211;list</code></dt>
<dd> (i mode only) List the contents of the archive to stdout; do not restore the contents to disk.</dd>
<dt><code>-u , &#8211;unconditional</code></dt>
<dd> (i and p modes) Unconditionally overwrite existing files. Ordinarily, an older file will not overwrite a newer file on disk.</dd>
<dt><code>-V , &#8211;dot</code></dt>
<dd> Print a dot to stderr for each file as it is processed. Superseded by &#8211;<code>v</code></dd>
<dt><code>-v , &#8211;verbose</code></dt>
<dd> Print the name of each file to stderr as it is processed. With &#8211;<code>t</code> provide a detailed listing of each file.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print the program version information and exit.</dd>
<dt><code>-y</code></dt>
<dd> (o mode only) Compress the archive with bzip2-compatible compression before writing it. In input mode, this option is ignored; bzip2 compression is recognized automatically on input.</dd>
<dt><code>-Z</code></dt>
<dd> (o mode only) Compress the archive with compress-compatible compression before writing it. In input mode, this option is ignored; compression is recognized automatically on input.</dd>
<dt><code>-z</code></dt>
<dd> (o mode only) Compress the archive with gzip-compatible compression before writing it. In input mode, this option is ignored; gzip compression is recognized automatically on input.</dd></dl>
<h2>EXIT STATUS</h2>
<p> Ex -std</p>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>:</code></p>
<dl>
<dt><code>LANG</code></dt>
<dd> The locale to use. See <a href="/docs/linux/man/7-environ/">environ</a>(7) for more information.</dd>
<dt><code>TZ</code></dt>
<dd> The timezone to use when displaying dates. See <a href="/docs/linux/man/7-environ/">environ</a>(7) for more information.</dd></dl>
<h2>EXAMPLES</h2>
<p> The command is traditionally used to copy file hierarchies in conjunction with the <a href="/docs/linux/man/1-find/">find</a>(1) command. The first example here simply copies all files from src to dest </p>
<blockquote><p><tt></tt><code>find src | -pmud dest </code> </p></blockquote>
<p> By carefully selecting options to the <a href="/docs/linux/man/1-find/">find</a>(1) command and combining it with other standard utilities, it is possible to exercise very fine control over which files are copied. This next example copies files from src to dest that are more than 2 days old and whose names match a particular pattern: </p>
<blockquote><p><tt></tt><code>find src -mtime </code><i>+2 | </i><code>grep foo[bar] | -pdmu dest </code> </p></blockquote>
<p> This example copies files from src to dest that are more than 2 days old and which contain the word Do foobar Dc : </p>
<blockquote><p><tt></tt><code>find src -mtime </code><i>+2 | </i><code>xargs grep -l foobar | -pdmu dest </code> </p></blockquote>
<h2>COMPATIBILITY</h2>
<p> The mode options i, o, and p and the options a, B, c, d, f, l, m, r, t, u, and v comply with SUSv2. </p>
<p> The old POSIX.1 standard specified that only &#8211;<code>i</code> &#8211;<code>o</code> and &#8211;<code>p</code> were interpreted as command-line options. Each took a single argument of a list of modifier characters. For example, the standard syntax allows &#8211;<code>imu</code> but does not support &#8211;<code>miu</code> or &#8211;<code>i -m -u</code> since <i>m</i> and <i>u</i> are only modifiers to &#8211;<code>i</code> they are not command-line options in their own right. The syntax supported by this implementation is backwards-compatible with the standard. For best compatibility, scripts should limit themselves to the standard syntax.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1), <a href="/docs/linux/man/1-tar/">tar</a>(1), <a href="/docs/linux/man/1-gzip/">gzip</a>(1), <a href="/docs/linux/man/1-mt/">mt</a>(1), pax(1), libarchive(3), <a href="/docs/linux/man/5-cpio/">cpio</a>(5), libarchive-formats5, <a href="/docs/linux/man/5-tar/">tar</a>(5)</p>
<h2>STANDARDS</h2>
<p> There is no current POSIX standard for the cpio command; it appeared in St -p1003.1-96 but was dropped from St -p1003.1-2001 . </p>
<p> The cpio, ustar, and pax interchange file formats are defined by St -p1003.1-2001 for the pax command.</p>
<h2>HISTORY</h2>
<p> The original <code>cpio</code> and <code>find</code> utilities were written by Dick Haight while working in AT&amp;T&#8217;s Unix Support Group. They first appeared in 1977 in PWB/UNIX 1.0, the &#8220;Programmer&#8217;s Work Bench&#8221; system developed for use within AT&amp;T. They were first released outside of AT&amp;T as part of System III Unix in 1981. As a result, <code>cpio</code> actually predates <code>tar</code> even though it was not well-known outside of AT&amp;T until some time later. </p>
<p> This is a complete re-implementation based on the libarchive(3) library.</p>
<h2>BUGS</h2>
<p> The cpio archive format has several basic limitations: It does not store user and group names, only numbers. As a result, it cannot be reliably used to transfer files between systems with dissimilar user and group numbering. Older cpio formats limit the user and group numbers to 16 or 18 bits, which is insufficient for modern systems. The cpio archive formats cannot support files over 4 gigabytes, except for the &#8220;odc&#8221; variant, which can support files up to 8 gigabytes. </p>
