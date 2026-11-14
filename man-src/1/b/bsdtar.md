---
title: "bsdtar(1)"
name: "bsdtar"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsdtar/"
description: "tar – manipulate tape archives"
---

<h2>NAME</h2>
<p> <code>tar</code> &#8211; manipulate tape archives</p>
<h2>SYNOPSIS</h2>
<p> [<i>bundled-flags Ao </i>args Ac [Ao <i>file Ac </i>| Ao <i>pattern Ac </i>&#8230; ] ]<br />
 Br q Fl c [<i>options</i> ] [<i>files | directories</i> ]<br />
 Br q Fl r | Fl u &#8211;<code>f </code><i>archive-file</i> [<i>options</i> ] [<i>files | directories</i> ]<br />
 Br q Fl t | Fl x [<i>options</i> ] [<i>patterns</i> ]</p>
<h2>DESCRIPTION</h2>
<p> creates and manipulates streaming archive files. This implementation can extract from tar, pax, cpio, zip, jar, ar, xar, rpm, 7-zip, and ISO 9660 cdrom images and can create tar, pax, cpio, ar, zip, 7-zip, and shar archives. </p>
<p> The first synopsis form shows a &#8220;bundled&#8221; option word. This usage is provided for compatibility with historical implementations. See COMPATIBILITY below for details. </p>
<p> The other synopsis forms show the preferred usage. The first option to is a mode indicator from the following list:</p>
<dl>
<dt><code>-c</code></p>
<dd> Create a new archive containing the specified items. The long option form is &#8211;<code>-create</code></p>
<dt><code>-r</code></p>
<dd> Like &#8211;<code>c</code> but new entries are appended to the archive. Note that this only works on uncompressed archives stored in regular files. The &#8211;<code>f</code> option is required. The long option form is &#8211;<code>-append</code></p>
<dt><code>-t</code></p>
<dd> List archive contents to stdout. The long option form is &#8211;<code>-list</code></p>
<dt><code>-u</code></p>
<dd> Like &#8211;<code>r</code> but new entries are added only if they have a modification date newer than the corresponding entry in the archive. Note that this only works on uncompressed archives stored in regular files. The &#8211;<code>f</code> option is required. The long form is &#8211;<code>-update</code></p>
<dt><code>-x</code></p>
<dd> Extract to disk from the archive. If a file with the same name appears more than once in the archive, each copy will be extracted, with later copies overwriting (replacing) earlier copies. The long option form is &#8211;<code>-extract</code></dl>
<p> In &#8211;<code>c</code> &#8211;<code>r</code> or &#8211;<code>u</code> mode, each specified file or directory is added to the archive in the order specified on the command line. By default, the contents of each directory are also archived. </p>
<p> In extract or list mode, the entire command line is read and parsed before the archive is opened. The pathnames or patterns on the command line indicate which items in the archive should be processed. Patterns are shell-style globbing patterns as documented in <a href="/docs/linux/man/1-tcsh/">tcsh</a>(1).</p>
<h2>OPTIONS</h2>
<p> Unless specifically stated otherwise, options are applicable in all operating modes.</p>
<dl>
<dt><code>@ archive </code></p>
<dd> (c and r mode only) The specified archive is opened and the entries in it will be appended to the current archive. As a simple example, </p>
<blockquote><p><tt></tt><code>-c -f &#8211; newfile @ original.tar </code> </p></blockquote>
<p> writes a new archive to standard output containing a file newfile and all of the entries from original.tar In contrast, </p>
<blockquote><p><tt></tt><code>-c -f &#8211; newfile original.tar </code> </p></blockquote>
<p> creates a new archive with only two entries. Similarly, </p>
<blockquote><p><tt></tt><code>-czf &#8211; &#8211;format pax @ &#8211; </code> </p></blockquote>
<p> reads an archive from standard input (whose format will be determined automatically) and converts it into a gzip-compressed pax-format archive on stdout. In this way, can be used to convert archives from one format to another.</p>
<dt><code>-a , &#8211;auto-compress</code></p>
<dd> (c mode only) Use the archive suffix to decide a set of the format and the compressions. As a simple example, </p>
<blockquote><p><tt></tt><code>-a -cf archive.tgz source.c source.h </code> </p></blockquote>
<p> creates a new archive with restricted pax format and gzip compression, </p>
<blockquote><p><tt></tt><code>-a -cf archive.tar.bz2.uu source.c source.h </code> </p></blockquote>
<p> creates a new archive with restricted pax format and bzip2 compression and uuencode compression, </p>
<blockquote><p><tt></tt><code>-a -cf archive.zip source.c source.h </code> </p></blockquote>
<p> creates a new archive with zip format, </p>
<blockquote><p><tt></tt><code>-a -jcf archive.tgz source.c source.h </code> </p></blockquote>
<p> ignores the &#8220;-j&#8221; option, and creates a new archive with restricted pax format and gzip compression, </p>
<blockquote><p><tt></tt><code>-a -jcf archive.xxx source.c source.h </code> </p></blockquote>
<p> if it is unknown suffix or no suffix, creates a new archive with restricted pax format and bzip2 compression.</p>
<dt><code>-B , &#8211;read-full-blocks</code></p>
<dd> Ignored for compatibility with other <a href="/docs/linux/man/1-tar/">tar</a>(1) implementations.</p>
<dt><code>-b </code><i>blocksize , &#8211;</i><code>-block-size </code><i>blocksize</i></p>
<dd> Specify the block size, in 512-byte records, for tape drive I/O. As a rule, this argument is only needed when reading from or writing to tape drives, and usually not even then as the default block size of 20 records (10240 bytes) is very common.</p>
<dt><code>-C </code><i>directory , &#8211;</i><code>-cd </code><i>directory , &#8211;</i><code>-directory </code><i>directory</i></p>
<dd> In c and r mode, this changes the directory before adding the following files. In x mode, change directories after opening the archive but before extracting entries from the archive.</p>
<dt><code>&#8211;chroot</code></p>
<dd> (x mode only) Fn chroot to the current directory after processing any &#8211;<code>C</code> options and before extracting any files.</p>
<dt><code>&#8211;disable-copyfile</code></p>
<dd> Mac OS X specific. Disable the use of <a href="/docs/linux/man/3-copyfile/">copyfile</a>(3).</p>
<dt><code>&#8211;exclude </code><i>pattern</i></p>
<dd> Do not process files or directories that match the specified pattern. Note that exclusions take precedence over patterns or filenames specified on the command line.</p>
<dt><code>&#8211;format </code><i>format</i></p>
<dd> (c, r, u mode only) Use the specified format for the created archive. Supported formats include &#8220;cpio&#8221; &#8220;pax&#8221; &#8220;shar&#8221; and &#8220;ustar&#8221; Other formats may also be supported; see libarchive-formats5 for more information about currently-supported formats. In r and u modes, when extending an existing archive, the format specified here must be compatible with the format of the existing archive on disk.</p>
<dt><code>-f </code><i>file , &#8211;</i><code>-file </code><i>file</i></p>
<dd> Read the archive from or write the archive to the specified file. The filename can be &#8211; for standard input or standard output. The default varies by system; on Fx , the default is /dev/sa0 on Linux, the default is /dev/st0</p>
<dt><code>&#8211;gid </code><i>id</i></p>
<dd> Use the provided group id number. On extract, this overrides the group id in the archive; the group name in the archive will be ignored. On create, this overrides the group id read from disk; if &#8211;<code>-gname</code> is not also specified, the group name will be set to match the group id.</p>
<dt><code>&#8211;gname </code><i>name</i></p>
<dd> Use the provided group name. On extract, this overrides the group name in the archive; if the provided group name does not exist on the system, the group id (from the archive or from the &#8211;<code>-gid</code> option) will be used instead. On create, this sets the group name that will be stored in the archive; the name will not be verified against the system group database.</p>
<dt><code>-H</code></p>
<dd> (c and r mode only) Symbolic links named on the command line will be followed; the target of the link will be archived, not the link itself.</p>
<dt><code>-h</code></p>
<dd> (c and r mode only) Synonym for &#8211;<code>L</code></p>
<dt><code>-I</code></p>
<dd> Synonym for &#8211;<code>T</code></p>
<dt><code>&#8211;help</code></p>
<dd> Show usage.</p>
<dt><code>&#8211;hfsCompression</code></p>
<dd> (x mode only) Mac OS X specific(v10.6 or later). Compress extracted regular files with HFS+ compression.</p>
<dt><code>&#8211;include </code><i>pattern</i></p>
<dd> Process only files or directories that match the specified pattern. Note that exclusions specified with &#8211;<code>-exclude</code> take precedence over inclusions. If no inclusions are explicitly specified, all entries are processed by default. The &#8211;<code>-include</code> option is especially useful when filtering archives. For example, the command </p>
<blockquote><p><tt></tt><code>-c -f new.tar &#8211;include=&#8217;*foo*&#8217; @ old.tgz </code> </p></blockquote>
<p> creates a new archive new.tar containing only the entries from old.tgz containing the string `foo&#8217;</p>
<dt><code>-J , &#8211;xz</code></p>
<dd> (c mode only) Compress the resulting archive with <a href="/docs/linux/man/1-xz/">xz</a>(1). In extract or list modes, this option is ignored. Note that, unlike other <code>tar</code> implementations, this implementation recognizes XZ compression automatically when reading archives.</p>
<dt><code>-j , &#8211;bzip , &#8211;bzip2 , &#8211;bunzip2</code></p>
<dd> (c mode only) Compress the resulting archive with <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1). In extract or list modes, this option is ignored. Note that, unlike other <code>tar</code> implementations, this implementation recognizes bzip2 compression automatically when reading archives.</p>
<dt><code>-k , &#8211;keep-old-files</code></p>
<dd> (x mode only) Do not overwrite existing files. In particular, if a file appears more than once in an archive, later copies will not overwrite earlier copies.</p>
<dt><code>&#8211;keep-newer-files</code></p>
<dd> (x mode only) Do not overwrite existing files that are newer than the versions appearing in the archive being extracted.</p>
<dt><code>-L , &#8211;dereference</code></p>
<dd> (c and r mode only) All symbolic links will be followed. Normally, symbolic links are archived as such. With this option, the target of the link will be archived instead.</p>
<dt><code>-l , &#8211;check-links</code></p>
<dd> (c and r modes only) Issue a warning message unless all links to each file are archived.</p>
<dt><code>&#8211;lrzip</code></p>
<dd> (c mode only) Compress the resulting archive with <a href="/docs/linux/man/1-lrzip/">lrzip</a>(1). In extract or list modes, this option is ignored.</p>
<dt><code>&#8211;lzma</code></p>
<dd> (c mode only) Compress the resulting archive with the original LZMA algorithm. Use of this option is discouraged and new archives should be created with &#8211;<code>-xz</code> instead. Note that, unlike other <code>tar</code> implementations, this implementation recognizes LZMA compression automatically when reading archives.</p>
<dt><code>&#8211;lzop</code></p>
<dd> (c mode only) Compress the resulting archive with <a href="/docs/linux/man/1-lzop/">lzop</a>(1). In extract or list modes, this option is ignored.</p>
<dt><code>-m , &#8211;modification-time</code></p>
<dd> (x mode only) Do not extract modification time. By default, the modification time is set to the time stored in the archive.</p>
<dt><code>-n , &#8211;norecurse , &#8211;no-recursion</code></p>
<dd> (c, r, u modes only) Do not recursively archive the contents of directories.</p>
<dt><code>&#8211;newer </code><i>date</i></p>
<dd> (c, r, u modes only) Only include files and directories newer than the specified date. This compares ctime entries.</p>
<dt><code>&#8211;newer-mtime </code><i>date</i></p>
<dd> (c, r, u modes only) Like &#8211;<code>-newer</code> except it compares mtime entries instead of ctime entries.</p>
<dt><code>&#8211;newer-than file </code></p>
<dd> (c, r, u modes only) Only include files and directories newer than the specified file. This compares ctime entries.</p>
<dt><code>&#8211;newer-mtime-than file </code></p>
<dd> (c, r, u modes only) Like &#8211;<code>-newer-than</code> except it compares mtime entries instead of ctime entries.</p>
<dt><code>&#8211;nodump</code></p>
<dd> (c and r modes only) Honor the nodump file flag by skipping this file.</p>
<dt><code>&#8211;nopreserveHFSCompression</code></p>
<dd> (x mode only) Mac OS X specific(v10.6 or later). Do not compress extracted regular files which were compressed with HFS+ compression before archived. By default, compress the regular files again with HFS+ compression.</p>
<dt><code>&#8211;null</code></p>
<dd> (use with &#8211;<code>I</code> or &#8211;<code>T</code> Filenames or patterns are separated by null characters, not by newlines. This is often used to read filenames output by the &#8211;<code>print0</code> option to <a href="/docs/linux/man/1-find/">find</a>(1).</p>
<dt><code>&#8211;no-same-owner</code></p>
<dd> (x mode only) Do not extract owner and group IDs. This is the reverse of &#8211;<code>-same-owner</code> and the default behavior if is run as non-root.</p>
<dt><code>&#8211;no-same-permissions</code></p>
<dd> (x mode only) Do not extract full permissions (SGID, SUID, sticky bit, ACLs, extended attributes or extended file flags). This is the reverse of &#8211;<code>p</code> and the default behavior if is run as non-root.</p>
<dt><code>&#8211;numeric-owner</code></p>
<dd> This is equivalent to &#8211;<code>-uname</code> Qq &#8211;<code>-gname</code> Qq . On extract, it causes user and group names in the archive to be ignored in favor of the numeric user and group ids. On create, it causes user and group names to not be stored in the archive.</p>
<dt><code>-O , &#8211;to-stdout</code></p>
<dd> (x, t modes only) In extract (-x) mode, files will be written to standard out rather than being extracted to disk. In list (-t) mode, the file listing will be written to stderr rather than the usual stdout.</p>
<dt><code>-o</code></p>
<dd> (x mode) Use the user and group of the user running the program rather than those specified in the archive. Note that this has no significance unless &#8211;<code>p</code> is specified, and the program is being run by the root user. In this case, the file modes and flags from the archive will be restored, but ACLs or owner information in the archive will be discarded.</p>
<dt><code>-o</code></p>
<dd> (c, r, u mode) A synonym for &#8211;<code>-format </code><i>ustar</i></p>
<dt><code>&#8211;older </code><i>date</i></p>
<dd> (c, r, u modes only) Only include files and directories older than the specified date. This compares ctime entries.</p>
<dt><code>&#8211;older-mtime </code><i>date</i></p>
<dd> (c, r, u modes only) Like &#8211;<code>-older</code> except it compares mtime entries instead of ctime entries.</p>
<dt><code>&#8211;older-than file </code></p>
<dd> (c, r, u modes only) Only include files and directories older than the specified file. This compares ctime entries.</p>
<dt><code>&#8211;older-mtime-than file </code></p>
<dd> (c, r, u modes only) Like &#8211;<code>-older-than</code> except it compares mtime entries instead of ctime entries.</p>
<dt><code>&#8211;one-file-system</code></p>
<dd> (c, r, and u modes) Do not cross mount points.</p>
<dt><code>&#8211;options </code><i>options</i></p>
<dd> Select optional behaviors for particular modules. The argument is a text string containing comma-separated keywords and values. These are passed to the modules that handle particular formats to control how those formats will behave. Each option has one of the following forms:</p>
<dl>
<dt><i>key=value</i></p>
<dd> The key will be set to the specified value in every module that supports it. Modules that do not support this key will ignore it.</p>
<dt><i>key</i></p>
<dd> The key will be enabled in every module that supports it. This is equivalent to <i>key </i><code>=1</code></p>
<dt><i>!key</i></p>
<dd> The key will be disabled in every module that supports it.</p>
<dt><i>module:key=value , module:key , module:!key</i></p>
<dd> As above, but the corresponding key and value will be provided only to modules whose name matches <i>module</i></dl>
<p> The currently supported modules and keys are:</p>
<dl>
<dt><code>iso9660:joliet</code></p>
<dd> Support Joliet extensions. This is enabled by default, use <code>!joliet</code> or <code>iso9660:!joliet</code> to disable.</p>
<dt><code>iso9660:rockridge</code></p>
<dd> Support Rock Ridge extensions. This is enabled by default, use <code>!rockridge</code> or <code>iso9660:!rockridge</code> to disable.</p>
<dt><code>gzip:compression-level</code></p>
<dd> A decimal integer from 1 to 9 specifying the gzip compression level.</p>
<dt><code>gzip:timestamp</code></p>
<dd> Store timestamp. This is enabled by default, use <code>!timestamp</code> or <code>gzip:!timestamp</code> to disable.</p>
<dt><code>lrzip:compression = </code><i>type</i></p>
<dd> Use <i>type</i> as compression method. Supported values are bzip2, gzip, lzo (ultra fast), and zpaq (best, extremely slow).</p>
<dt><code>lrzip:compression-level</code></p>
<dd> A decimal integer from 1 to 9 specifying the lrzip compression level.</p>
<dt><code>lzop:compression-level</code></p>
<dd> A decimal integer from 1 to 9 specifying the lzop compression level.</p>
<dt><code>xz:compression-level</code></p>
<dd> A decimal integer from 0 to 9 specifying the xz compression level.</p>
<dt><code>mtree: </code><i>keyword</i></p>
<dd> The mtree writer module allows you to specify which mtree keywords will be included in the output. Supported keywords include: <code>cksum , device , flags , gid , gname , indent</code> <code>link , md5 , mode , nlink , rmd160 , sha1 , sha256</code> <code>sha384 , sha512 , size , time , uid , uname</code> The default is equivalent to: &#8220;device, flags, gid, gname, link, mode, nlink, size, time, type, uid, uname&#8221;</p>
<dt><code>mtree:all</code></p>
<dd> Enables all of the above keywords. You can also use <code>mtree:!all</code> to disable all keywords.</p>
<dt><code>mtree:use-set</code></p>
<dd> Enable generation of <code>/set</code> lines in the output.</p>
<dt><code>mtree:indent</code></p>
<dd> Produce human-readable output by indenting options and splitting lines to fit into 80 columns.</p>
<dt><code>zip:compression = </code><i>type</i></p>
<dd> Use <i>type</i> as compression method. Supported values are store (uncompressed) and deflate (gzip algorithm).</dl>
<p> If a provided option is not supported by any module, that is a fatal error.</p>
<dt><code>-P , &#8211;absolute-paths</code></p>
<dd> Preserve pathnames. By default, absolute pathnames (those that begin with a / character) have the leading slash removed both when creating archives and extracting from them. Also, will refuse to extract archive entries whose pathnames contain .. or whose target directory would be altered by a symlink. This option suppresses these behaviors.</p>
<dt><code>-p , &#8211;insecure , &#8211;preserve-permissions</code></p>
<dd> (x mode only) Preserve file permissions. Attempt to restore the full permissions, including owner, file modes, file flags and ACLs, if available, for each item extracted from the archive. This is the default, if is being run by root and can be overridden by also specifying &#8211;<code>-no-same-owner</code> and &#8211;<code>-no-same-permissions</code></p>
<dt><code>&#8211;posix</code></p>
<dd> (c, r, u mode only) Synonym for &#8211;<code>-format </code><i>pax</i></p>
<dt><code>-q , &#8211;fast-read</code></p>
<dd> (x and t mode only) Extract or list only the first archive entry that matches each pattern or filename operand. Exit as soon as each specified pattern or filename has been matched. By default, the archive is always read to the very end, since there can be multiple entries with the same name and, by convention, later entries overwrite earlier entries. This option is provided as a performance optimization.</p>
<dt><code>-S</code></p>
<dd> (x mode only) Extract files as sparse files. For every block on disk, check first if it contains only NULL bytes and seek over it otherwise. This works similar to the conv=sparse option of dd.</p>
<dt><code>-s </code><i>pattern</i></p>
<dd> Modify file or archive member names according to pattern The pattern has the format <i>/old/new/ </i>[ghHprRsS] where <i>old</i> is a basic regular expression, <i>new</i> is the replacement string of the matched part, and the optional trailing letters modify how the replacement is handled. If <i>old</i> is not matched, the pattern is skipped. Within <i>new</i> ~ is substituted with the match, \1 to \9 with the content of the corresponding captured group. The optional trailing g specifies that matching should continue after the matched part and stop on the first unmatched pattern. The optional trailing s specifies that the pattern applies to the value of symbolic links. The optional trailing p specifies that after a successful substitution the original path name and the new path name should be printed to standard error. Optional trailing H, R, or S characters suppress substitutions for hardlink targets, regular filenames, or symlink targets, respectively. Optional trailing h, r, or s characters enable substitutions for hardlink targets, regular filenames, or symlink targets, respectively. The default is <i>hrs</i> which applies substitutions to all names. In particular, it is never necessary to specify h, r, or s.</p>
<dt><code>&#8211;same-owner</code></p>
<dd> (x mode only) Extract owner and group IDs. This is the reverse of &#8211;<code>-no-same-owner</code> and the default behavior if is run as root.</p>
<dt><code>&#8211;strip-components </code><i>count</i></p>
<dd> Remove the specified number of leading path elements. Pathnames with fewer elements will be silently skipped. Note that the pathname is edited after checking inclusion/exclusion patterns but before security checks.</p>
<dt><code>-T </code><i>filename , &#8211;</i><code>-files-from </code><i>filename</i></p>
<dd> In x or t mode, will read the list of names to be extracted from filename In c mode, will read names to be archived from filename The special name &#8220;-C&#8221; on a line by itself will cause the current directory to be changed to the directory specified on the following line. Names are terminated by newlines unless &#8211;<code>-null</code> is specified. Note that &#8211;<code>-null</code> also disables the special handling of lines containing &#8220;-C&#8221; Note: If you are generating lists of files using <a href="/docs/linux/man/1-find/">find</a>(1), you probably want to use &#8211;<code>n</code> as well.</p>
<dt><code>&#8211;totals</code></p>
<dd> (c, r, u mode only) After archiving all files, print a summary to stderr.</p>
<dt><code>-U , &#8211;unlink , &#8211;unlink-first</code></p>
<dd> (x mode only) Unlink files before creating them. This can be a minor performance optimization if most files already exist, but can make things slower if most files do not already exist. This flag also causes to remove intervening directory symlinks instead of reporting an error. See the SECURITY section below for more details.</p>
<dt><code>&#8211;uid </code><i>id</i></p>
<dd> Use the provided user id number and ignore the user name from the archive. On create, if &#8211;<code>-uname</code> is not also specified, the user name will be set to match the user id.</p>
<dt><code>&#8211;uname </code><i>name</i></p>
<dd> Use the provided user name. On extract, this overrides the user name in the archive; if the provided user name does not exist on the system, it will be ignored and the user id (from the archive or from the &#8211;<code>-uid</code> option) will be used instead. On create, this sets the user name that will be stored in the archive; the name is not verified against the system user database.</p>
<dt><code>&#8211;use-compress-program </code><i>program</i></p>
<dd> Pipe the input (in x or t mode) or the output (in c mode) through program instead of using the builtin compression support.</p>
<dt><code>-v , &#8211;verbose</code></p>
<dd> Produce verbose output. In create and extract modes, will list each file name as it is read from or written to the archive. In list mode, will produce output similar to that of <a href="/docs/linux/man/1-ls/">ls</a>(1). Additional &#8211;<code>v</code> options will provide additional detail.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version of and <code>libarchive</code> and exit.</p>
<dt><code>-w , &#8211;confirmation , &#8211;interactive</code></p>
<dd> Ask for confirmation for every action.</p>
<dt><code>-X </code><i>filename , &#8211;</i><code>-exclude-from </code><i>filename</i></p>
<dd> Read a list of exclusion patterns from the specified file. See &#8211;<code>-exclude</code> for more information about the handling of exclusions.</p>
<dt><code>-y</code></p>
<dd> (c mode only) Compress the resulting archive with <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1). In extract or list modes, this option is ignored. Note that, unlike other <code>tar</code> implementations, this implementation recognizes bzip2 compression automatically when reading archives.</p>
<dt><code>-Z , &#8211;compress , &#8211;uncompress</code></p>
<dd> (c mode only) Compress the resulting archive with <a href="/docs/linux/man/1-compress/">compress</a>(1). In extract or list modes, this option is ignored. Note that, unlike other <code>tar</code> implementations, this implementation recognizes compress compression automatically when reading archives.</p>
<dt><code>-z , &#8211;gunzip , &#8211;gzip</code></p>
<dd> (c mode only) Compress the resulting archive with <a href="/docs/linux/man/1-gzip/">gzip</a>(1). In extract or list modes, this option is ignored. Note that, unlike other <code>tar</code> implementations, this implementation recognizes gzip compression automatically when reading archives.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>:</code></p>
<dl>
<dt><code>TAR_READER_OPTIONS</code></p>
<dd> The default options for format readers and compression readers. The &#8211;<code>-options</code> option overrides this.</p>
<dt><code>TAR_WRITER_OPTIONS</code></p>
<dd> The default options for format writers and compression writers. The &#8211;<code>-options</code> option overrides this.</p>
<dt><code>LANG</code></p>
<dd> The locale to use. See <a href="/docs/linux/man/7-environ/">environ</a>(7) for more information.</p>
<dt><code>TAPE</code></p>
<dd> The default device. The &#8211;<code>f</code> option overrides this. Please see the description of the &#8211;<code>f</code> option above for more details.</p>
<dt><code>TZ</code></p>
<dd> The timezone to use when displaying dates. See <a href="/docs/linux/man/7-environ/">environ</a>(7) for more information.</dl>
<h2>EXIT STATUS</h2>
<p> Ex -std</p>
<h2>EXAMPLES</h2>
<p> The following creates a new archive called <i>file.tar.gz</i> that contains two files <i>source.c</i> and <i>source.h</i> </p>
<blockquote><p><tt></tt><code>-czf file.tar.gz source.c source.h </code> </p></blockquote>
<p> To view a detailed table of contents for this archive: </p>
<blockquote><p><tt></tt><code>-tvf file.tar.gz </code> </p></blockquote>
<p> To extract all entries from the archive on the default tape drive: </p>
<blockquote><p><tt></tt><code>-x</code> </p></blockquote>
<p> To examine the contents of an ISO 9660 cdrom image: </p>
<blockquote><p><tt></tt><code>-tf image.iso </code> </p></blockquote>
<p> To move file hierarchies, invoke as </p>
<blockquote><p><tt></tt><code>-cf &#8211; -C srcdir . | -xpf &#8211; -C destdir </code> </p></blockquote>
<p> or more traditionally </p>
<blockquote><p><tt>cd srcdir ; </tt><code>-cf &#8211; . | ( cd destdir ; -xpf &#8211; </code> </p></blockquote>
<p> In create mode, the list of files and directories to be archived can also include directory change instructions of the form <code>-C foo/baz </code> and archive inclusions of the form <code>@ archive-file </code> For example, the command line </p>
<blockquote><p><tt></tt><code>-c -f new.tar foo1 @ old.tgz -C /tmp foo2 </code> </p></blockquote>
<p> will create a new archive new.tar will read the file foo1 from the current directory and add it to the output archive. It will then read each entry from old.tgz and add those entries to the output archive. Finally, it will switch to the /tmp directory and add foo2 to the output archive. </p>
<p> An input file in <a href="/docs/linux/man/5-mtree/">mtree</a>(5) format can be used to create an output archive with arbitrary ownership, permissions, or names that differ from existing data on disk: </p>
<blockquote><p><tt>$ cat input.mtree</tt></p></blockquote>
<blockquote><p><tt>#mtree</tt></p></blockquote>
<blockquote><p><tt>usr/bin uid=0 gid=0 mode=0755 type=dir</tt></p></blockquote>
<blockquote><p><tt>usr/bin/ls uid=0 gid=0 mode=0755 type=file content=myls</tt></p></blockquote>
<blockquote><p><tt>$ tar -cvf output.tar @input.mtree</tt></p></blockquote>
<p> The &#8211;<code>-newer</code> and &#8211;<code>-newer-mtime</code> switches accept a variety of common date and time specifications, including &#8220;12 Mar 2005 7:14:29pm&#8221; &#8220;2005-03-12 19:14&#8221; &#8220;5 minutes ago&#8221; and &#8220;19:14 PST May 1&#8221; </p>
<p> The &#8211;<code>-options</code> argument can be used to control various details of archive generation or reading. For example, you can generate mtree output which only contains <code>type , time</code> and <code>uid</code> keywords: </p>
<blockquote><p><tt></tt><code>-cf file.tar &#8211;format=mtree &#8211;options=&#8217;!all,type,time,uid&#8217; dir </code> </p></blockquote>
<p> or you can set the compression level used by gzip or xz compression: </p>
<blockquote><p><tt></tt><code>-czf file.tar &#8211;options=&#8217;compression-level=9&#8242;</code> </p></blockquote>
<p> For more details, see the explanation of the Fn archive_read_set_options and Fn archive_write_set_options API calls that are described in archive_read3 and archive_write3.</p>
<h2>COMPATIBILITY</h2>
<p> The bundled-arguments format is supported for compatibility with historic implementations. It consists of an initial word (with no leading &#8211; character) in which each character indicates an option. Arguments follow as separate words. The order of the arguments must match the order of the corresponding characters in the bundled command word. For example, </p>
<blockquote><p><tt></tt><code>tbf 32 file.tar </code> </p></blockquote>
<p> specifies three flags <code>t</code> <code>b</code> and <code>f</code> The <code>b</code> and <code>f</code> flags both require arguments, so there must be two additional items on the command line. The <i>32</i> is the argument to the <code>b</code> flag, and <i>file.tar</i> is the argument to the <code>f</code> flag. </p>
<p> The mode options c, r, t, u, and x and the options b, f, l, m, o, v, and w comply with SUSv2. </p>
<p> For maximum portability, scripts that invoke <code>tar</code> should use the bundled-argument format above, should limit themselves to the <code>c</code> <code>t</code> and <code>x</code> modes, and the <code>b</code> <code>f</code> <code>m</code> <code>v</code> and <code>w</code> options. </p>
<p> Additional long options are provided to improve compatibility with other tar implementations.</p>
<h2>SECURITY</h2>
<p> Certain security issues are common to many archiving programs, including <code>.</code> In particular, carefully-crafted archives can request that extract files to locations outside of the target directory. This can potentially be used to cause unwitting users to overwrite files they did not intend to overwrite. If the archive is being extracted by the superuser, any file on the system can potentially be overwritten. There are three ways this can happen. Although has mechanisms to protect against each one, savvy users should be aware of the implications: </p>
<ul>
<li> Archive entries can have absolute pathnames. By default, removes the leading / character from filenames before restoring them to guard against this problem.
<li> Archive entries can have pathnames that include .. components. By default, will not extract files containing .. components in their pathname.
<li> Archive entries can exploit symbolic links to restore files to other directories. An archive can restore a symbolic link to another directory, then use that link to restore a file into that directory. To guard against this, checks each extracted path for symlinks. If the final path element is a symlink, it will be removed and replaced with the archive entry. If &#8211;<code>U</code> is specified, any intermediate symlink will also be unconditionally removed. If neither &#8211;<code>U</code> nor &#8211;<code>P</code> is specified, will refuse to extract the entry. </ul>
<p> To protect yourself, you should be wary of any archives that come from untrusted sources. You should examine the contents of an archive with </p>
<blockquote><p><tt></tt><code>-tf filename </code> </p></blockquote>
<p> before extraction. You should use the &#8211;<code>k</code> option to ensure that will not overwrite any existing files or the &#8211;<code>U</code> option to remove any pre-existing files. You should generally not extract archives while running with super-user privileges. Note that the &#8211;<code>P</code> option to disables the security checks above and allows you to extract an archive while preserving any absolute pathnames, .. components, or symlinks to other directories.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1), <a href="/docs/linux/man/1-compress/">compress</a>(1), <a href="/docs/linux/man/1-cpio/">cpio</a>(1), <a href="/docs/linux/man/1-gzip/">gzip</a>(1), <a href="/docs/linux/man/1-mt/">mt</a>(1), <a href="/docs/linux/man/1-pax/">pax</a>(1), <a href="/docs/linux/man/1-shar/">shar</a>(1), <a href="/docs/linux/man/1-xz/">xz</a>(1), <a href="/docs/linux/man/3-libarchive/">libarchive</a>(3), libarchive-formats5, <a href="/docs/linux/man/5-tar/">tar</a>(5)</p>
<h2>STANDARDS</h2>
<p> There is no current POSIX standard for the tar command; it appeared in St -p1003.1-96 but was dropped from St -p1003.1-2001 . The options supported by this implementation were developed by surveying a number of existing tar implementations as well as the old POSIX specification for tar and the current POSIX specification for pax. </p>
<p> The ustar and pax interchange file formats are defined by St -p1003.1-2001 for the pax command.</p>
<h2>HISTORY</h2>
<p> A <code>tar</code> command appeared in Seventh Edition Unix, which was released in January, 1979. There have been numerous other implementations, many of which extended the file format. John Gilmore&#8217;s <code>pdtar</code> public-domain implementation (circa November, 1987) was quite influential, and formed the basis of GNU tar. GNU tar was included as the standard system tar in Fx beginning with Fx 1.0 . </p>
<p> This is a complete re-implementation based on the <a href="/docs/linux/man/3-libarchive/">libarchive</a>(3) library. It was first released with Fx 5.4 in May, 2005.</p>
<h2>BUGS</h2>
<p> This program follows St -p1003.1-96 for the definition of the &#8211;<code>l</code> option. Note that GNU tar prior to version 1.15 treated &#8211;<code>l</code> as a synonym for the &#8211;<code>-one-file-system</code> option. </p>
<p> The &#8211;<code>C dir </code> option may differ from historic implementations. </p>
<p> All archive output is written in correctly-sized blocks, even if the output is being compressed. Whether or not the last output block is padded to a full block size varies depending on the format and the output device. For tar and cpio formats, the last block of output is padded to a full block size if the output is being written to standard output or to a character or block device such as a tape drive. If the output is being written to a regular file, the last block will not be padded. Many compressors, including <a href="/docs/linux/man/1-gzip/">gzip</a>(1) and <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1), complain about the null padding when decompressing an archive created by <code>,</code> although they still extract it correctly. </p>
<p> The compression and decompression is implemented internally, so there may be insignificant differences between the compressed output generated by </p>
<blockquote><p><tt></tt><code>-czf &#8211; file </code> </p></blockquote>
<p> and that generated by </p>
<blockquote><p><tt></tt><code>-cf &#8211; file | gzip</code> </p></blockquote>
<p> The default should be to read and write archives to the standard I/O paths, but tradition (and POSIX) dictates otherwise. </p>
<p> The <code>r</code> and <code>u</code> modes require that the archive be uncompressed and located in a regular file on disk. Other archives can be modified using <code>c</code> mode with the @archive-file extension. </p>
<p> To archive a file called @foo or -foo you must specify it as ./@foo or ./-foo respectively. </p>
<p> In create mode, a leading ./ is always removed. A leading / is stripped unless the &#8211;<code>P</code> option is specified. </p>
<p> There needs to be better support for file selection on both create and extract. </p>
<p> There is not yet any support for multi-volume archives or for archiving sparse files. </p>
<p> Converting between dissimilar archive formats (such as tar and cpio) using the <code>@ &#8211; </code> convention can cause hard link information to be lost. (This is a consequence of the incompatible ways that different archive formats store hardlink information.) </p>
<h2>Index</h2>
