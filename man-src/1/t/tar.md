---
title: "tar(1)"
name: "tar"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tar/"
description: "tar – an archiving utility"
---

<h2 class="name">NAME</h2>
<p> tar &#8211; an archiving utility </p>
<h2>SYNOPSIS</h2>
<h3>Traditional usage</h3>
<p> <code>tar</code> {<code>A</code>|<code>c</code>|<code>d</code>|<code>r</code>|<code>t</code>|<code>u</code>|<code>x</code>}[<code>GnSkUWOmpsMBiajJzZhPlRvwo</code>] [<i>ARG</i>&#8230;]</p>
<h3>UNIX-style usage</h3>
<p> <code>tar</code> <code>-A</code> [<i>OPTIONS</i>] <i>ARCHIVE</i> <i>ARCHIVE</i> </p>
<p> <code>tar</code> <code>-c</code> [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>FILE</i>&#8230;] </p>
<p> <code>tar</code> <code>-d</code> [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>FILE</i>&#8230;] </p>
<p> <code>tar</code> <code>-t</code> [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>MEMBER</i>&#8230;] </p>
<p> <code>tar</code> <code>-r</code> [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>FILE</i>&#8230;] </p>
<p> <code>tar</code> <code>-u</code> [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>FILE</i>&#8230;] </p>
<p> <code>tar</code> <code>-x</code> [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>MEMBER</i>&#8230;]</p>
<h3>GNU-style usage</h3>
<p> <code>tar</code> {<code>&#8211;catenate</code>|<code>&#8211;concatenate</code>} [<i>OPTIONS</i>] <i>ARCHIVE</i> <i>ARCHIVE</i> </p>
<p> <code>tar</code> <code>&#8211;create</code> [<code>&#8211;file</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>FILE</i>&#8230;] </p>
<p> <code>tar</code> {<code>&#8211;diff</code>|<code>&#8211;compare</code>} [<code>&#8211;file</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>FILE</i>&#8230;] </p>
<p> <code>tar</code> <code>&#8211;delete</code> [<code>&#8211;file</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>MEMBER</i>&#8230;] </p>
<p> <code>tar</code> <code>&#8211;append</code> [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>FILE</i>&#8230;] </p>
<p> <code>tar</code> <code>&#8211;list</code> [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>MEMBER</i>&#8230;] </p>
<p> <code>tar</code> <code>&#8211;test-label</code> [<code>&#8211;file</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>LABEL</i>&#8230;] </p>
<p> <code>tar</code> <code>&#8211;update</code> [<code>&#8211;file</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>FILE</i>&#8230;] </p>
<p> <code>tar</code> <code>&#8211;update</code> [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>FILE</i>&#8230;] </p>
<p> <code>tar</code> {<code>&#8211;extract</code>|<code>&#8211;get</code>} [<code>-f</code> <i>ARCHIVE</i>] [<i>OPTIONS</i>] [<i>MEMBER</i>&#8230;]</p>
<h2>NOTE</h2>
<p> This manpage is a short description of GNU <code>tar</code>. For a detailed discussion, including examples and usage recommendations, refer to the <code>GNU Tar Manual</code> available in texinfo format. If the <code>info</code> reader and the tar documentation are properly installed on your system, the command </p>
<dl>
<dt>
</dt><dd> <code>info tar</code></dd></dl>
<p> should give you access to the complete manual. </p>
<p> You can also view the manual using the info mode in <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1), or find it in various formats online at </p>
<dl>
<dt>
</dt><dd> <code><a rel="nofollow" href="http://www.gnu.org/software/tar/manual">http://www.gnu.org/software/tar/manual</a></code></dd></dl>
<p> If any discrepancies occur between this manpage and the <code>GNU Tar Manual</code>, the later shall be considered the authoritative source.</p>
<h2>DESCRIPTION</h2>
<p> GNU <code>tar</code> is an archiving program designed to store multiple files in a single file (an <code>archive</code>), and to manipulate such archives. The archive can be either a regular file or a device (e.g. a tape drive, hence the name of the program, which stands for <code>t</code>ape <code>ar</code>chiver), which can be located either on the local or on a remote machine. </p>
<h3>Option styles</h3>
<p> Options to GNU <code>tar</code> can be given in three different styles. In <code>traditional style</code>, the first argument is a cluster of option letters and all subsequent arguments supply arguments to those options that require them. The arguments are read in the same order as the option letters. Any command line words that remain after all options has been processed are treated as non-optional arguments: file or archive member names. </p>
<p> For example, the <code>c</code> option requires creating the archive, the <code>v</code> option requests the verbose operation, and the <code>f</code> option takes an argument that sets the name of the archive to operate upon. The following command, written in the traditional style, instructs tar to store all files from the directory <code>/etc</code> into the archive file <code>etc.tar</code> verbosely listing the files being archived: </p>
<p> tar cfv etc.tar /etc </p>
<p> In <code>UNIX </code>or<code> short-option style</code>, each option letter is prefixed with a single dash, as in other command line utilities. If an option takes argument, the argument follows it, either as a separate command line word, or immediately following the option. However, if the option takes an <code>optional</code> argument, the argument must follow the option letter without any intervening whitespace, as in <code>-g/tmp/snar.db</code>. </p>
<p> Any number of options not taking arguments can be clustered together after a single dash, e.g. <code>-vkp</code>. Options that take arguments (whether mandatory or optional), can appear at the end of such a cluster, e.g. <code>-vkpf a.tar</code>. </p>
<p> The example command above written in the <code>short-option style</code> could look like: </p>
<p> tar -cvf etc.tar /etc or tar -c -v -f etc.tar /etc </p>
<p> In <code>GNU </code>or<code> long-option style</code>, each option begins with two dashes and has a meaningful name, consisting of lower-case letters and dashes. When used, the long option can be abbreviated to its initial letters, provided that this does not create ambiguity. Arguments to long options are supplied either as a separate command line word, immediately following the option, or separated from the option by an equals sign with no intervening whitespace. Optional arguments must always use the latter method. </p>
<p> Here are several ways of writing the example command in this style: </p>
<p> tar &#8211;create &#8211;file etc.tar &#8211;verbose /etc or (abbreviating some options): tar &#8211;cre &#8211;file=etc.tar &#8211;verb /etc </p>
<p> The options in all three styles can be intermixed, although doing so with old options is not encouraged.</p>
<h3>Operation mode</h3>
<p> The options listed in the table below tell GNU <code>tar</code> what operation it is to perform. Exactly one of them must be given. Meaning of non-optional arguments depends on the operation mode requested.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;catenate</code>, <code>&#8211;concatenate</code></dt>
<dd> Append archive to the end of another archive. The arguments are treated as the names of archives to append. All archives must be of the same format as the archive they are appended to, otherwise the resulting archive might be unusable with non-GNU implementations of <code>tar</code>. Notice also that when more than one archive is given, the members from archives other than the first one will be accessible in the resulting archive only if using the <code>-i</code> (<code>&#8211;ignore-zeros</code>) option. </dd>
<p> Compressed archives cannot be concatenated.</p>
<dt><code>-c</code>, <code>&#8211;create</code></dt>
<dd> Create a new archive. Arguments supply the names of the files to be archived. Directories are archived recursively, unless the <code>&#8211;no-recursion</code> option is given.</dd>
<dt><code>-d</code>, <code>&#8211;diff</code>, <code>&#8211;compare</code></dt>
<dd> Find differences between archive and file system. The arguments are optional and specify archive members to compare. If not given, the current working directory is assumed.</dd>
<dt><code>&#8211;delete</code></dt>
<dd> Delete from the archive. The arguments supply names of the archive members to be removed. At least one argument must be given. </dd>
<p> This option does not operate on compressed archives. There is no short option equivalent.</p>
<dt><code>-r</code>, <code>&#8211;append</code></dt>
<dd> Append files to the end of an archive. Arguments have the same meaning as for <code>-c</code> (<code>&#8211;create</code>).</dd>
<dt><code>-t</code>, <code>&#8211;list</code></dt>
<dd> List the contents of an archive. Arguments are optional. When given, they specify the names of the members to list.</dd>
<dt><code>&#8211;test-label</dt>
<dd> Test the archive volume label and exit. When used without arguments, it prints the volume label (if any) and exits with status 0</code>. When one or more command line arguments are given. <code>tar</code> compares the volume label with each argument. It exits with code <code>0</code> if a match is found, and with code <code>1</code> otherwise. No output is displayed, unless used together with the <code>-v</code> (<code>&#8211;verbose</code>) option. </dd>
<p> There is no short option equivalent for this option.</p>
<dt><code>-u</code>, <code>&#8211;update</code></dt>
<dd> Append files which are newer than the corresponding copy in the archive. Arguments have the same meaning as with <code>-c</code> and <code>-r</code> options. Notice, that newer files don&#8217;t replace their old archive copies, but instead are appended to the end of archive. The resulting archive can thus contain several members of the same name, corresponding to various versions of the same file.</dd>
<dt><code>-x</code>, <code>&#8211;extract</code>, <code>&#8211;get</code></dt>
<dd> Extract files from an archive. Arguments are optional. When given, they specify names of the archive members to be extracted.</dd>
<dt>
</dt><dt><code>&#8211;show-defaults</code></dt>
<dd>
</dd><dd> Show built-in defaults for various <code>tar</code> options and exit. No arguments are allowed.</dd>
<dt><code>-?</code>, <code>&#8211;help</dt>
<dd> Display a short option summary and exit. No arguments allowed.</dd>
<dt>&#8211;usage</code></dt>
<dd> Display a list of available options and exit. No arguments allowed.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print program version and copyright information and exit.</dd></dl>
<h2>OPTIONS</h2>
<h3>Operation modifiers</h3>
<dl>
<dt><code>&#8211;check-device</code></dt>
<dd> Check device numbers when creating incremental archives (default).</dd>
<dt><code>-g</code>, <code>&#8211;listed-incremental</code>=<i>FILE</i></dt>
<dd> Handle new GNU-format incremental backups. <i>FILE</i> is the name of a <code>snapshot file</code>, where tar stores additional information which is used to decide which files changed since the previous incremental dump and, consequently, must be dumped again. If <i>FILE</i> does not exist when creating an archive, it will be created and all files will be added to the resulting archive (the <code>level 0</code> dump). To create incremental archives of non-zero level <code>N</code>, create a copy of the snapshot file created during the level <code>N-1</code>, and use it as <i>FILE</i>. </dd>
<p> When listing or extracting, the actual contents of <i>FILE</i> is not inspected, it is needed only due to syntactical requirements. It is therefore common practice to use <code>/dev/null</code> in its place.</p>
<dt><code>&#8211;hole-detection</code>=<i>METHOD</i></dt>
<dd> Use <i>METHOD</i> to detect holes in sparse files. This option implies <code>&#8211;sparse</code>. Valid values for <i>METHOD</i> are <code>seek</code> and <code>raw</code>. Default is <code>seek</code> with fallback to <code>raw</code> when not applicable.</dd>
<dt><code>-G</code>, <code>&#8211;incremental</code></dt>
<dd> Handle old GNU-format incremental backups.</dd>
<dt><code>&#8211;ignore-failed-read</code></dt>
<dd> Do not exit with nonzero on unreadable files.</dd>
<dt><code>&#8211;level</code>=<i>NUMBER</i></dt>
<dd> Set dump level for created listed-incremental archive. Currently only <code>&#8211;level=0</code> is meaningful: it instructs <code>tar</code> to truncate the snapshot file before dumping, thereby forcing a level 0 dump.</dd>
<dt><code>-n</code>, <code>&#8211;seek</code></dt>
<dd> Assume the archive is seekable. Normally <code>tar</code> determines automatically whether the archive can be seeked or not. This option is intended for use in cases when such recognition fails. It takes effect only if the archive is open for reading (e.g. with <code>&#8211;list</code> or <code>&#8211;extract</code> options).</dd>
<dt><code>&#8211;no-check-device</code></dt>
<dd> Do not check device numbers when creating incremental archives.</dd>
<dt><code>&#8211;no-seek</code></dt>
<dd> Assume the archive is not seekable.</dd>
<dt><code>&#8211;occurrence</code>[=<i>N</i>]</dt>
<dd> Process only the <i>N</i>th occurrence of each file in the archive. This option is valid only when used with one of the following subcommands: <code>&#8211;delete</code>, <code>&#8211;diff</code>, <code>&#8211;extract</code> or <code>&#8211;list</code> and when a list of files is given either on the command line or via the <code>-T</code> option. The default <i>N</i> is <code>1</code>.</dd>
<dt><code>&#8211;restrict</code></dt>
<dd> Disable the use of some potentially harmful options.</dd>
<dt><code>&#8211;sparse-version</code>=<i>MAJOR</i>[.<i>MINOR</i>]</dt>
<dd> Set version of the sparse format to use (implies <code>&#8211;sparse</code>). This option implies <code>&#8211;sparse</code>. Valid argument values are <code>0.0</code>, <code>0.1</code>, and <code>1.0</code>. For a detailed discussion of sparse formats, refer to the <code>GNU Tar Manual</code>, appendix <code>D</code>, &quot;<code>Sparse Formats</code>&quot;. Using <code>info</code> reader, it can be accessed running the following command: <code>info tar &#8216;Sparse Formats&#8217;</code>.</dd>
<dt><code>-S</code>, <code>&#8211;sparse</code></dt>
<dd> Handle sparse files efficiently. Some files in the file system may have segments which were actually never written (quite often these are database files created by such systems as <code>DBM</code>). When given this option, <code>tar</code> attempts to determine if the file is sparse prior to archiving it, and if so, to reduce the resulting archive size by not dumping empty parts of the file.</dd></dl>
<h3>Overwrite control</h3>
<p> These options control <code>tar</code> actions when extracting a file over an existing copy on disk.</p>
<dl>
<dt><code>-k</code>, <code>&#8211;keep-old-files</code></dt>
<dd> Don&#8217;t replace existing files when extracting.</dd>
<dt><code>&#8211;keep-newer-files</code></dt>
<dd> Don&#8217;t replace existing files that are newer than their archive copies.</dd>
<dt><code>&#8211;keep-directory-symlink</code></dt>
<dd> Don&#8217;t replace existing symlinks to directories when extracting.</dd>
<dt><code>&#8211;no-overwrite-dir</code></dt>
<dd> Preserve metadata of existing directories.</dd>
<dt><code>&#8211;one-top-level</code>[<code>=</code><i>DIR</i>]</dt>
<dd> Extract all files into <i>DIR</i>, or, if used without argument, into a subdirectory named by the base name of the archive (minus standard compression suffixes recognizable by <code>&#8211;auto-compress).</dd>
<dt>&#8211;overwrite</code></dt>
<dd> Overwrite existing files when extracting.</dd>
<dt><code>&#8211;overwrite-dir</code></dt>
<dd> Overwrite metadata of existing directories when extracting (default).</dd>
<dt><code>&#8211;recursive-unlink</code></dt>
<dd> Recursively remove all files in the directory prior to extracting it.</dd>
<dt><code>&#8211;remove-files</code></dt>
<dd> Remove files from disk after adding them to the archive.</dd>
<dt><code>&#8211;skip-old-files</dt>
<dd> Don&#8217;t replace existing files when extracting, silently skip over them.</dd>
<dt>-U</code>, <code>&#8211;unlink-first</code></dt>
<dd> Remove each file prior to extracting over it.</dd>
<dt><code>-W</code>, <code>&#8211;verify</code></dt>
<dd> Verify the archive after writing it.</dd></dl>
<h3>Output stream selection</h3>
<dl>
<dt><code>&#8211;ignore-command-error</code></dt>
<dd>
</dd><dt>Ignore subprocess exit codes.</dt>
<dd>
</dd><dt><code>&#8211;no-ignore-command-error</code></dt>
<dd> Treat non-zero exit codes of children as error (default).</dd>
<dt><code>-O</code>, <code>&#8211;to-stdout</code></dt>
<dd> Extract files to standard output.</dd>
<dt><code>&#8211;to-command</code>=<i>COMMAND</i></dt>
<dd> Pipe extracted files to <i>COMMAND</i>. The argument is the pathname of an external program, optionally with command line arguments. The program will be invoked and the contents of the file being extracted supplied to it on its standard input. Additional data will be supplied via the following environment variables:</dd>
<dl>
<dl>
<dt><code>TAR_FILETYPE</code></dt>
<dd> Type of the file. It is a single letter with the following meaning: </dd>
<pre>
        f           Regular file
        d           Directory
        l           Symbolic link
        h           Hard link
        b           Block device
        c           Character device
</pre>
<p> Currently only regular files are supported.</p>
<dt><code>TAR_MODE</code></dt>
<dd> File mode, an octal number.</dd>
<dt><code>TAR_FILENAME</code></dt>
<dd> The name of the file.</dd>
<dt><code>TAR_REALNAME</code></dt>
<dd> Name of the file as stored in the archive.</dd>
<dt><code>TAR_UNAME</code></dt>
<dd> Name of the file owner.</dd>
<dt><code>TAR_GNAME</code></dt>
<dd> Name of the file owner group.</dd>
<dt><code>TAR_ATIME</code></dt>
<dd> Time of last access. It is a decimal number, representing seconds since the Epoch. If the archive provides times with nanosecond precision, the nanoseconds are appended to the timestamp after a decimal point.</dd>
<dt><code>TAR_MTIME</code></dt>
<dd> Time of last modification.</dd>
<dt><code>TAR_CTIME</code></dt>
<dd> Time of last status change.</dd>
<dt><code>TAR_SIZE</code></dt>
<dd> Size of the file.</dd>
<dt><code>TAR_UID</code></dt>
<dd> UID of the file owner.</dd>
<dt><code>TAR_GID</code></dt>
<dd> GID of the file owner.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Additionally, the following variables contain information about <code>tar</code> operation mode and the archive being processed:</p>
</dd><dl>
<dt><code>TAR_VERSION</code></dt>
<dd> GNU <code>tar</code> version number.</dd>
<dt><code>TAR_ARCHIVE</code></dt>
<dd> The name of the archive <code>tar</code> is processing.</dd>
<dt><code>TAR_BLOCKING_FACTOR</code></dt>
<dd> Current blocking factor, i.e. number of 512-byte blocks in a record.</dd>
<dt><code>TAR_VOLUME</code></dt>
<dd> Ordinal number of the volume <code>tar</code> is processing (set if reading a multi-volume archive).</dd>
<dt><code>TAR_FORMAT</code></dt>
<dd> Format of the archive being processed. One of: <code>gnu</code>, <code>oldgnu</code>, <code>posix</code>, <code>ustar</code>, <code>v7</code>.</dd>
<dt><code>TAR_SUBCOMMAND</code></dt>
<dd> A short option (with a leading dash) describing the operation <code>tar</code> is executing.</dd></dl>
</dl>
</dl>
<h3>Handling of file attributes</h3>
<dl>
<dt><code>&#8211;atime-preserve</code>[=<i>METHOD</i>]</dt>
<dd> Preserve access times on dumped files, either by restoring the times after reading (<i>METHOD</i>=<code>replace</code>, this is the default) or by not setting the times in the first place (<i>METHOD</i>=<code>system</code>)</dd>
<dt><code>&#8211;delay-directory-restore</code></dt>
<dd> Delay setting modification times and permissions of extracted directories until the end of extraction. Use this option when extracting from an archive which has unusual member ordering.</dd>
<dt><code>&#8211;group</code>=<i>NAME</i>[:<i>GID</i>]</dt>
<dd> Force <i>NAME</i> as group for added files. If <i>GID</i> is not supplied, <i>NAME</i> can be either a user name or numeric GID. In this case the missing part (GID or name) will be inferred from the current host&#8217;s group database. </dd>
<p> When used with <code>&#8211;group-map</code>=<i>FILE</i>, affects only those files whose owner group is not listed in <i>FILE</i>.</p>
<dt><code>&#8211;group-map</code>=<i>FILE</i></dt>
<dd> Read group translation map from <i>FILE</i>. Empty lines are ignored. Comments are introduced with <code>#</code> sign and extend to the end of line. Each non-empty line in <i>FILE</i> defines translation for a single group. It must consist of two fields, delimited by any amount of whitespace: </dd>
<p> <i>OLDGRP</i> <i>NEWGRP</i>[<code>:</code><i>NEWGID</i>] </p>
<p> <i>OLDGRP</i> is either a valid group name or a GID prefixed with <code>+</code>. Unless <i>NEWGID</i> is supplied, <i>NEWGRP</i> must also be either a valid group name or a <code>+</code><i>GID</i>. Otherwise, both <i>NEWGRP</i> and <i>NEWGID</i> need not be listed in the system group database. </p>
<p> As a result, each input file with owner group <i>OLDGRP</i> will be stored in archive with owner group <i>NEWGRP</i> and GID <i>NEWGID</i>.</p>
<dt><code>&#8211;mode</code>=<i>CHANGES</i></dt>
<dd> Force symbolic mode <i>CHANGES</i> for added files.</dd>
<dt><code>&#8211;mtime</code>=<i>DATE-OR-FILE</i></dt>
<dd> Set mtime for added files. <i>DATE-OR-FILE</i> is either a date/time in almost arbitrary format, or the name of an existing file. In the latter case the mtime of that file will be used.</dd>
<dt><code>-m</code>, <code>&#8211;touch</code></dt>
<dd> Don&#8217;t extract file modified time.</dd>
<dt><code>&#8211;no-delay-directory-restore</code></dt>
<dd> Cancel the effect of the prior <code>&#8211;delay-directory-restore</code> option.</dd>
<dt><code>&#8211;no-same-owner</code></dt>
<dd> Extract files as yourself (default for ordinary users).</dd>
<dt><code>&#8211;no-same-permissions</code></dt>
<dd> Apply the user&#8217;s umask when extracting permissions from the archive (default for ordinary users).</dd>
<dt><code>&#8211;numeric-owner</code></dt>
<dd> Always use numbers for user/group names.</dd>
<dt><code>&#8211;owner</code>=<i>NAME</i>[:<i>UID</i>]</dt>
<dd> Force <i>NAME</i> as owner for added files. If <i>UID</i> is not supplied, <i>NAME</i> can be either a user name or numeric UID. In this case the missing part (UID or name) will be inferred from the current host&#8217;s user database. </dd>
<p> When used with <code>&#8211;owner-map</code>=<i>FILE</i>, affects only those files whose owner is not listed in <i>FILE</i>.</p>
<dt><code>&#8211;owner-map</code>=<i>FILE</i></dt>
<dd> Read owner translation map from <i>FILE</i>. Empty lines are ignored. Comments are introduced with <code>#</code> sign and extend to the end of line. Each non-empty line in <i>FILE</i> defines translation for a single UID. It must consist of two fields, delimited by any amount of whitespace: </dd>
<p> <i>OLDUSR</i> <i>NEWUSR</i>[<code>:</code><i>NEWUID</i>] </p>
<p> <i>OLDUSR</i> is either a valid user name or a UID prefixed with <code>+</code>. Unless <i>NEWUID</i> is supplied, <i>NEWUSR</i> must also be either a valid user name or a <code>+</code><i>UID</i>. Otherwise, both <i>NEWUSR</i> and <i>NEWUID</i> need not be listed in the system user database. </p>
<p> As a result, each input file owned by <i>OLDUSR</i> will be stored in archive with owner name <i>NEWUSR</i> and UID <i>NEWUID</i>.</p>
<dt><code>-p</code>, <code>&#8211;preserve-permissions</code>, <code>&#8211;same-permissions</code></dt>
<dd> extract information about file permissions (default for superuser)</dd>
<dt><code>&#8211;same-owner</code></dt>
<dd> Try extracting files with the same ownership as exists in the archive (default for superuser).</dd>
<dt><code>-s</code>, <code>&#8211;preserve-order</code>, <code>&#8211;same-order</code></dt>
<dd> Sort names to extract to match archive</dd>
<dt><code>&#8211;sort=</code><i>ORDER</i></dt>
<dd> When creating an archive, sort directory entries according to <i>ORDER</i>, which is one of <code>none</code>, <code>name</code>, or <code>inode</code>. </dd>
<p> The default is <code>&#8211;sort=none</code>, which stores archive members in the same order as returned by the operating system. </p>
<p> Using <code>&#8211;sort=name</code> ensures the member ordering in the created archive is uniform and reproducible. </p>
<p> Using <code>&#8211;sort=inode</code> reduces the number of disk seeks made when creating the archive and thus can considerably speed up archivation. This sorting order is supported only if the underlying system provides the necessary information.</dl>
<h3>Extended file attributes</h3>
<dl>
<dt><code>&#8211;acls</code></dt>
<dd> Enable POSIX ACLs support.</dd>
<dt><code>&#8211;no-acls</code></dt>
<dd> Disable POSIX ACLs support.</dd>
<dt><code>&#8211;selinux</code></dt>
<dd> Enable SELinux context support.</dd>
<dt><code>&#8211;no-selinux</code></dt>
<dd> Disable SELinux context support.</dd>
<dt><code>&#8211;xattrs</code></dt>
<dd> Enable extended attributes support.</dd>
<dt><code>&#8211;no-xattrs</code></dt>
<dd> Disable extended attributes support.</dd>
<dt><code>&#8211;xattrs-exclude=</code><i>PATTERN</i></dt>
<dd> Specify the exclude pattern for xattr keys. <i>PATTERN</i> is a POSIX regular expression, e.g. <code>&#8211;xattrs-exclude=&#8217;^user.&#8217;</code>, to exclude attributes from the user namespace.</dd>
<dt><code>&#8211;xattrs-include=</code><i>PATTERN</i></dt>
<dd> Specify the include pattern for xattr keys. <i>PATTERN</i> is a POSIX regular expression.</dd></dl>
<h3>Device selection and switching</h3>
<dl>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>ARCHIVE</i></dt>
<dd> Use archive file or device <i>ARCHIVE</i>. If this option is not given, <code>tar</code> will first examine the environment variable `TAPE&#8217;. If it is set, its value will be used as the archive name. Otherwise, <code>tar</code> will assume the compiled-in default. The default value can be inspected either using the <code>&#8211;show-defaults</code> option, or at the end of the <code>tar &#8211;help</code> output. </dd>
<p> An archive name that has a colon in it specifies a file or device on a remote machine. The part before the colon is taken as the machine name or IP address, and the part after it as the file or device pathname, e.g.: </p>
<p> &#8211;file=remotehost:/dev/sr0 </p>
<p> An optional username can be prefixed to the hostname, placing a <code>@</code> sign between them. </p>
<p> By default, the remote host is accessed via the <code><a href="/docs/linux/man/1-rsh/">rsh</a></code>(1) command. Nowadays it is common to use <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) instead. You can do so by giving the following command line option: </p>
<p> &#8211;rsh-command=/usr/bin/ssh </p>
<p> The remote machine should have the <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8) command installed. If its pathname does not match <code>tar</code>&#8216;s default, you can inform <code>tar</code> about the correct pathname using the <code>&#8211;rmt-command</code> option.</p>
<dt><code>&#8211;force-local</code></dt>
<dd> Archive file is local even if it has a colon.</dd>
<dt><code>-F</code>, <code>&#8211;info-script</code>=<i>COMMAND</i>, <code>&#8211;new-volume-script</code>=<i>COMMAND</i></dt>
<dd> Run <i>COMMAND</i> at the end of each tape (implies <code>-M</code>). The command can include arguments. When started, it will inherit <code>tar</code>&#8216;s environment plus the following variables:</dd>
<dl>
<dl>
<dt><code>TAR_VERSION</code></dt>
<dd> GNU <code>tar</code> version number.</dd>
<dt><code>TAR_ARCHIVE</code></dt>
<dd> The name of the archive <code>tar</code> is processing.</dd>
<dt><code>TAR_BLOCKING_FACTOR</code></dt>
<dd> Current blocking factor, i.e. number of 512-byte blocks in a record.</dd>
<dt><code>TAR_VOLUME</code></dt>
<dd> Ordinal number of the volume <code>tar</code> is processing (set if reading a multi-volume archive).</dd>
<dt><code>TAR_FORMAT</code></dt>
<dd> Format of the archive being processed. One of: <code>gnu</code>, <code>oldgnu</code>, <code>posix</code>, <code>ustar</code>, <code>v7</code>.</dd>
<dt><code>TAR_SUBCOMMAND</code></dt>
<dd> A short option (with a leading dash) describing the operation <code>tar</code> is executing.</dd>
<dt><code>TAR_FD</code></dt>
<dd> File descriptor which can be used to communicate the new volume name to <code>tar</code>.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> If the info script fails, <code>tar</code> exits; otherwise, it begins writing the next volume.</dd></dl>
<dt><code>-L</code>, <code>&#8211;tape-length</code>=<i>N</i></dt>
<dd> Change tape after writing <i>N</i>x1024 bytes. If <i>N</i> is followed by a size suffix (see the subsection <code>Size suffixes</code> below), the suffix specifies the multiplicative factor to be used instead of 1024. </dd>
<p> This option implies <code>-M</code>.</p>
<dt><code>-M</code>, <code>&#8211;multi-volume</code></dt>
<dd> Create/list/extract multi-volume archive.</dd>
<dt><code>&#8211;rmt-command</code>=<i>COMMAND</i></dt>
<dd> Use <i>COMMAND</i> instead of <code>rmt</code> when accessing remote archives. See the description of the <code>-f</code> option, above.</dd>
<dt><code>&#8211;rsh-command</code>=<i>COMMAND</i></dt>
<dd> Use <i>COMMAND</i> instead of <code>rsh</code> when accessing remote archives. See the description of the <code>-f</code> option, above.</dd>
<dt><code>&#8211;volno-file</code>=<i>FILE</i></dt>
<dd> When this option is used in conjunction with <code>&#8211;multi-volume</code>, <code>tar</code> will keep track of which volume of a multi-volume archive it is working in <i>FILE</i>.</dd></dl>
<h3>Device blocking</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;blocking-factor</code>=<i>BLOCKS</i></dt>
<dd> Set record size to <i>BLOCKS</i>x<code>512</code> bytes.</dd>
<dt><code>-B</code>, <code>&#8211;read-full-records</code></dt>
<dd> When listing or extracting, accept incomplete input records after end-of-file marker.</dd>
<dt><code>-i</code>, <code>&#8211;ignore-zeros</code></dt>
<dd> Ignore zeroed blocks in archive. Normally two consecutive 512-blocks filled with zeroes mean EOF and tar stops reading after encountering them. This option instructs it to read further and is useful when reading archives created with the <code>-A</code> option.</dd>
<dt><code>&#8211;record-size</code>=<i>NUMBER</i></dt>
<dd> Set record size. <i>NUMBER</i> is the number of bytes per record. It must be multiple of <code>512</code>. It can can be suffixed with a <code>size suffix</code>, e.g. <code>&#8211;record-size=10K</code>, for 10 Kilobytes. See the subsection <code>Size suffixes</code>, for a list of valid suffixes.</dd></dl>
<h3>Archive format selection</h3>
<dl>
<dt><code>-H</code>, <code>&#8211;format</code>=<i>FORMAT</i></dt>
<dd> Create archive of the given format. Valid formats are:</dd>
<dl>
<dl>
<dt><code>gnu</code></dt>
<dd> GNU tar 1.13.x format</dd>
<dt><code>oldgnu</code></dt>
<dd> GNU format as per tar &lt;= 1.12.</dd>
<dt><code>pax</code>, <code>posix</code></dt>
<dd> POSIX 1003.1-2001 (pax) format.</dd>
<dt><code>ustar</code></dt>
<dd> POSIX 1003.1-1988 (ustar) format.</dd>
<dt><code>v7</code></dt>
<dd> Old V7 tar format.</dd></dl>
</dl>
<dt><code>&#8211;old-archive</code>, <code>&#8211;portability</code></dt>
<dd> Same as <code>&#8211;format=v7</code>.</dd>
<dt><code>&#8211;pax-option</code>=<i>keyword</i>[[:]=<i>value</i>][,<i>keyword</i>[[:]=<i>value</i>]]&#8230;</dt>
<dd> Control pax keywords when creating <code>PAX</code> archives (<code>-H pax</code>). This option is equivalent to the <code>-o</code> option of the <code>pax</code>(1) utility.</dd>
<dt><code>&#8211;posix</code></dt>
<dd> Same as <code>&#8211;format=posix</code>.</dd>
<dt><code>-V</code>, <code>&#8211;label</code>=<i>TEXT</i></dt>
<dd> Create archive with volume name <i>TEXT</i>. If listing or extracting, use <i>TEXT</i> as a globbing pattern for volume name.</dd></dl>
<h3>Compression options</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;auto-compress</code></dt>
<dd> Use archive suffix to determine the compression program.</dd>
<dt><code>-I</code>, <code>&#8211;use-compress-program</code><i>=COMMAND</i></dt>
<dd> Filter data through <i>COMMAND</i>. It must accept the <code>-d</code> option, for decompression. The argument can contain command line options.</dd>
<dt><code>-j</code>, <code>&#8211;bzip2</code></dt>
<dd> Filter the archive through <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1).</dd>
<dt><code>-J</code>, <code>&#8211;xz</code></dt>
<dd> Filter the archive through <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1).</dd>
<dt><code>&#8211;lzip</code></dt>
<dd> Filter the archive through <code><a href="/docs/linux/man/1-lzip/">lzip</a></code>(1).</dd>
<dt><code>&#8211;lzma</code></dt>
<dd> Filter the archive through <code><a href="/docs/linux/man/1-lzma/">lzma</a></code>(1).</dd>
<dt><code>&#8211;lzop</code></dt>
<dd> Filter the archive through <code><a href="/docs/linux/man/1-lzop/">lzop</a></code>(1).</dd>
<dt><code>&#8211;no-auto-compress</code></dt>
<dd> Do not use archive suffix to determine the compression program.</dd>
<dt><code>-z</code>, <code>&#8211;gzip</code>, <code>&#8211;gunzip</code>, <code>&#8211;ungzip</code></dt>
<dd> Filter the archive through <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1).</dd>
<dt><code>-Z</code>, <code>&#8211;compress</code>, <code>&#8211;uncompress</code></dt>
<dd> Filter the archive through <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1).</dd>
<dt><code>&#8211;zstd</code></dt>
<dd> Filter the archive through <code><a href="/docs/linux/man/1-zstd/">zstd</a></code>(1).</dd></dl>
<h3>Local file selection</h3>
<dl>
<dt><code>&#8211;add-file</code>=<i>FILE</i></dt>
<dd> Add <i>FILE</i> to the archive (useful if its name starts with a dash).</dd>
<dt><code>&#8211;backup</code>[=<i>CONTROL</i>]</dt>
<dd> Backup before removal. The <i>CONTROL</i> argument, if supplied, controls the backup policy. Its valid values are:</dd>
<dl>
<dl>
<dt><code>none</code>, <code>off</code></dt>
<dd> Never make backups.</dd>
<dt><code>t</code>, <code>numbered</code></dt>
<dd> Make numbered backups.</dd>
<dt><code>nil</code>, <code>existing</code></dt>
<dd> Make numbered backups if numbered backups exist, simple backups otherwise.</dd>
<dt><code>never</code>, <code>simple</code></dt>
<dd> Always make simple backups</dd>
<dl>
</dl>
<p> If <i>CONTROL</i> is not given, the value is taken from the <code>VERSION_CONTROL</code> environment variable. If it is not set, <code>existing</code> is assumed.</dl>
</dl>
<dt><code>-C</code>, <code>&#8211;directory</code>=<i>DIR</i></dt>
<dd> Change to <i>DIR</i> before performing any operations. This option is order-sensitive, i.e. it affects all options that follow.</dd>
<dt><code>&#8211;exclude</code>=<i>PATTERN</i></dt>
<dd> Exclude files matching <i>PATTERN</i>, a <code><a href="/docs/linux/man/3-glob/">glob</a></code>(3)-style wildcard pattern.</dd>
<dt><code>&#8211;exclude-backups</code></dt>
<dd> Exclude backup and lock files.</dd>
<dt><code>&#8211;exclude-caches</code></dt>
<dd> Exclude contents of directories containing file <code>CACHEDIR.TAG</code>, except for the tag file itself.</dd>
<dt><code>&#8211;exclude-caches-all</code></dt>
<dd> Exclude directories containing file <code>CACHEDIR.TAG</code> and the file itself.</dd>
<dt><code>&#8211;exclude-caches-under</code></dt>
<dd> Exclude everything under directories containing <code>CACHEDIR.TAG</code></dd>
<dt><code>&#8211;exclude-ignore=</code><i>FILE</i></dt>
<dd> Before dumping a directory, see if it contains <i>FILE</i>. If so, read exclusion patterns from this file. The patterns affect only the directory itself.</dd>
<dt><code>&#8211;exclude-ignore-recursive=</code><i>FILE</i></dt>
<dd> Same as <code>&#8211;exclude-ignore</code>, except that patterns from <i>FILE</i> affect both the directory and all its subdirectories.</dd>
<dt><code>&#8211;exclude-tag</code>=<i>FILE</i></dt>
<dd> Exclude contents of directories containing <i>FILE</i>, except for <i>FILE</i> itself.</dd>
<dt><code>&#8211;exclude-tag-all</code>=<i>FILE</i></dt>
<dd> Exclude directories containing <i>FILE</i>.</dd>
<dt><code>&#8211;exclude-tag-under</code>=<i>FILE</i></dt>
<dd> Exclude everything under directories containing <i>FILE</i>.</dd>
<dt><code>&#8211;exclude-vcs</code></dt>
<dd> Exclude version control system directories.</dd>
<dt><code>&#8211;exclude-vcs-ignores</code></dt>
<dd> Exclude files that match patterns read from VCS-specific ignore files. Supported files are: <code>.cvsignore</code>, <code>.gitignore</code>, <code>.bzrignore</code>, and <code>.hgignore</code>.</dd>
<dt><code>-h</code>, <code>&#8211;dereference</code></dt>
<dd> Follow symlinks; archive and dump the files they point to.</dd>
<dt><code>&#8211;hard-dereference</code></dt>
<dd> Follow hard links; archive and dump the files they refer to.</dd>
<dt><code>-K</code>, <code>&#8211;starting-file</code>=<i>MEMBER</i></dt>
<dd> Begin at the given member in the archive.</dd>
<dt><code>&#8211;newer-mtime</code>=<i>DATE</i></dt>
<dd> Work on files whose data changed after the <i>DATE</i>. If <i>DATE</i> starts with <code>/</code> or <code>.</code> it is taken to be a file name; the mtime of that file is used as the date.</dd>
<dt><code>&#8211;no-null</code></dt>
<dd> Disable the effect of the previous <code>&#8211;null</code> option.</dd>
<dt><code>&#8211;no-recursion</code></dt>
<dd> Avoid descending automatically in directories.</dd>
<dt><code>&#8211;no-unquote</code></dt>
<dd> Do not unquote input file or member names.</dd>
<dt><code>&#8211;no-verbatim-files-from</code></dt>
<dd> Treat each line read from a file list as if it were supplied in the command line. I.e., leading and trailing whitespace is removed and, if the resulting string begins with a dash, it is treated as <code>tar</code> command line option. </dd>
<p> This is the default behavior. The <code>&#8211;no-verbatim-files-from</code> option is provided as a way to restore it after <code>&#8211;verbatim-files-from</code> option. </p>
<p> This option is positional: it affects all <code>&#8211;files-from</code> options that occur after it in, until <code>&#8211;verbatim-files-from</code> option or end of line, whichever occurs first. </p>
<p> It is implied by the <code>&#8211;no-null</code> option.</p>
<dt><code>&#8211;null</code></dt>
<dd> Instruct subsequent <code>-T</code> options to read null-terminated names verbatim (disables special handling of names that start with a dash). </dd>
<p> See also <code>&#8211;verbatim-files-from</code>.</p>
<dt><code>-N</code>, <code>&#8211;newer</code>=<i>DATE</i>, <code>&#8211;after-date</code>=<i>DATE</i></dt>
<dd> Only store files newer than DATE. If <i>DATE</i> starts with <code>/</code> or <code>.</code> it is taken to be a file name; the mtime of that file is used as the date.</dd>
<dt><code>&#8211;one-file-system</code></dt>
<dd> Stay in local file system when creating archive.</dd>
<dt><code>-P</code>, <code>&#8211;absolute-names</code></dt>
<dd> Don&#8217;t strip leading slashes from file names when creating archives.</dd>
<dt><code>&#8211;recursion</code></dt>
<dd> Recurse into directories (default).</dd>
<dt><code>&#8211;suffix</code>=<i>STRING</i></dt>
<dd> Backup before removal, override usual suffix. Default suffix is <code>~</code>, unless overridden by environment variable <code>SIMPLE_BACKUP_SUFFIX</code>.</dd>
<dt><code>-T</code>, <code>&#8211;files-from</code>=<i>FILE</i></dt>
<dd> Get names to extract or create from <i>FILE</i>. </dd>
<p> Unless specified otherwise, the <i>FILE</i> must contain a list of names separated by ASCII <code>LF</code> (i.e. one name per line). The names read are handled the same way as command line arguments. They undergo quote removal and word splitting, and any string that starts with a <code>&#8211;</code> is handled as <code>tar</code> command line option. </p>
<p> If this behavior is undesirable, it can be turned off using the <code>&#8211;verbatim-files-from</code> option. </p>
<p> The <code>&#8211;null</code> option instructs <code>tar</code> that the names in <i>FILE</i> are separated by ASCII <code>NUL</code> character, instead of <code>LF</code>. It is useful if the list is generated by <code><a href="/docs/linux/man/1-find/">find</a></code>(1) <code>-print0</code> predicate.</p>
<dt><code>&#8211;unquote</code></dt>
<dd> Unquote file or member names (default).</dd>
<dt><code>&#8211;verbatim-files-from</code></dt>
<dd> Treat each line obtained from a file list as a file name, even if it starts with a dash. File lists are supplied with the <code>&#8211;files-from</code> (<code>-T</code>) option. The default behavior is to handle names supplied in file lists as if they were typed in the command line, i.e. any names starting with a dash are treated as <code>tar</code> options. The <code>&#8211;verbatim-files-from</code> option disables this behavior. </dd>
<p> This option affects all <code>&#8211;files-from</code> options that occur after it in the command line. Its effect is reverted by the <code>&#8211;no-verbatim-files-from} option. </p>
<p> This option is implied by the &#8211;null</code> option. </p>
<p> See also <code>&#8211;add-file</code>.</p>
<dt><code>-X</code>, <code>&#8211;exclude-from</code>=<i>FILE</i></dt>
<dd> Exclude files matching patterns listed in FILE.</dd></dl>
<h3>File name transformations</h3>
<dl>
<dt><code>&#8211;strip-components</code>=<i>NUMBER</i></dt>
<dd> Strip <i>NUMBER</i> leading components from file names on extraction.</dd>
<dt><code>&#8211;transform</code>=<i>EXPRESSION</i>, <code>&#8211;xform</code>=<i>EXPRESSION</i></dt>
<dd> Use sed replace <i>EXPRESSION</i> to transform file names.</dd></dl>
<h3>File name matching options</h3>
<p> These options affect both exclude and include patterns.</p>
<dl>
<dt><code>&#8211;anchored</code></dt>
<dd> Patterns match file name start.</dd>
<dt><code>&#8211;ignore-case</code></dt>
<dd> Ignore case.</dd>
<dt><code>&#8211;no-anchored</code></dt>
<dd> Patterns match after any <code>/</code> (default for exclusion).</dd>
<dt><code>&#8211;no-ignore-case</code></dt>
<dd> Case sensitive matching (default).</dd>
<dt><code>&#8211;no-wildcards</code></dt>
<dd> Verbatim string matching.</dd>
<dt><code>&#8211;no-wildcards-match-slash</code></dt>
<dd> Wildcards do not match <code>/</code>.</dd>
<dt><code>&#8211;wildcards</code></dt>
<dd> Use wildcards (default for exclusion).</dd>
<dt><code>&#8211;wildcards-match-slash</code></dt>
<dd> Wildcards match <code>/</code> (default for exclusion).</dd></dl>
<h3>Informative output</h3>
<dl>
<dt><code>&#8211;checkpoint</code>[=<i>N</i>]</dt>
<dd> Display progress messages every <i>N</i>th record (default 10).</dd>
<dt><code>&#8211;checkpoint-action</code>=<i>ACTION</i></dt>
<dd> Run <i>ACTION</i> on each checkpoint.</dd>
<dt><code>&#8211;clamp-mtime</code></dt>
<dd> Only set time when the file is more recent than what was given with &#8211;mtime.</dd>
<dt><code>&#8211;full-time</code></dt>
<dd> Print file time to its full resolution.</dd>
<dt><code>&#8211;index-file</code>=<i>FILE</i></dt>
<dd> Send verbose output to <i>FILE</i>.</dd>
<dt><code>-l</code>, <code>&#8211;check-links</code></dt>
<dd> Print a message if not all links are dumped.</dd>
<dt><code>&#8211;no-quote-chars</code>=<i>STRING</i></dt>
<dd> Disable quoting for characters from <i>STRING</i>.</dd>
<dt><code>&#8211;quote-chars</code>=<i>STRING</i></dt>
<dd> Additionally quote characters from <i>STRING</i>.</dd>
<dt><code>&#8211;quoting-style</code>=<i>STYLE</i></dt>
<dd> Set quoting style for file and member names. Valid values for <i>STYLE</i> are <code>literal</code>, <code>shell</code>, <code>shell-always</code>, <code>c</code>, <code>c-maybe</code>, <code>escape</code>, <code>locale</code>, <code>clocale</code>.</dd>
<dt><code>-R</code>, <code>&#8211;block-number</code></dt>
<dd> Show block number within archive with each message.</dd>
<dt><code>&#8211;show-omitted-dirs</code></dt>
<dd> When listing or extracting, list each directory that does not match search criteria.</dd>
<dt><code>&#8211;show-transformed-names</code>, <code>&#8211;show-stored-names</code></dt>
<dd> Show file or archive names after transformation by <code>&#8211;strip</code> and <code>&#8211;transform</code> options.</dd>
<dt><code>&#8211;totals</code>[=<i>SIGNAL</i>]</dt>
<dd> Print total bytes after processing the archive. If <i>SIGNAL</i> is given, print total bytes when this signal is delivered. Allowed signals are: <code>SIGHUP</code>, <code>SIGQUIT</code>, <code>SIGINT</code>, <code>SIGUSR1</code>, and <code>SIGUSR2</code>. The <code>SIG</code> prefix can be omitted.</dd>
<dt><code>&#8211;utc</code></dt>
<dd> Print file modification times in UTC.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Verbosely list files processed. Each instance of this option on the command line increases the verbosity level by one. The maximum verbosity level is 3. For a detailed discussion of how various verbosity levels affect tar&#8217;s output, please refer to <code>GNU Tar Manual</code>, subsection 2.5.1 &quot;<code>The &#8211;verbose Option</code>&quot;.</dd>
<dt><code>&#8211;warning</code>=<i>KEYWORD</i></dt>
<dd> Enable or disable warning messages identified by <i>KEYWORD</i>. The messages are suppressed if <i>KEYWORD</i> is prefixed with <code>no-</code> and enabled otherwise. </dd>
<p> Multiple <code>&#8211;warning</code> messages accumulate. </p>
<p> Keywords controlling general <code>tar</code> operation:</p>
<dl>
<dl>
<dt><code>all</code></dt>
<dd> Enable all warning messages. This is the default.</dd>
<dt><code>none</code></dt>
<dd> Disable all warning messages.</dd>
<dt><code>filename-with-nuls</code></dt>
<dd> &quot;%s: file name read contains nul character&quot;</dd>
<dt><code>alone-zero-block</code></dt>
<dd> &quot;A lone zero block at %s&quot;</dd>
<dt>
</dt><dd>Keywords applicable for <code>tar &#8211;create</code>:</dd>
<dt><code>cachedir</code></dt>
<dd> &quot;%s: contains a cache directory tag %s; %s&quot;</dd>
<dt><code>file-shrank</code></dt>
<dd> &quot;%s: File shrank by %s bytes; padding with zeros&quot;</dd>
<dt><code>xdev</code></dt>
<dd> &quot;%s: file is on a different filesystem; not dumped&quot;</dd>
<dt><code>file-ignored</code></dt>
<dd> &quot;%s: Unknown file type; file ignored&quot;<br />
 &quot;%s: socket ignored&quot;<br />
 &quot;%s: door ignored&quot;</dd>
<dt><code>file-unchanged</code></dt>
<dd> &quot;%s: file is unchanged; not dumped&quot;</dd>
<dt><code>ignore-archive</code></dt>
<dd> &quot;%s: file is the archive; not dumped&quot;</dd>
<dt><code>file-removed</code></dt>
<dd> &quot;%s: File removed before we read it&quot;</dd>
<dt><code>file-changed</code></dt>
<dd> &quot;%s: file changed as we read it&quot;</dd>
<dt><code>failed-read</code></dt>
<dd> Suppresses warnings about unreadable files or directories. This keyword applies only if used together with the <code>&#8211;ignore-failed-read</code> option.</dd>
<dt>
</dt><dd>Keywords applicable for <code>tar &#8211;extract</code>:</dd>
<dt><code>existing-file</code></dt>
<dd> &quot;%s: skipping existing file&quot;</dd>
<dt><code>timestamp</code></dt>
<dd> &quot;%s: implausibly old time stamp %s&quot;<br />
 &quot;%s: time stamp %s is %s s in the future&quot;</dd>
<dt><code>contiguous-cast</code></dt>
<dd> &quot;Extracting contiguous files as regular files&quot;</dd>
<dt><code>symlink-cast</code></dt>
<dd> &quot;Attempting extraction of symbolic links as hard links&quot;</dd>
<dt><code>unknown-cast</code></dt>
<dd> &quot;%s: Unknown file type &#8216;%c&#8217;, extracted as normal file&quot;</dd>
<dt><code>ignore-newer</code></dt>
<dd> &quot;Current %s is newer or same age&quot;</dd>
<dt><code>unknown-keyword</code></dt>
<dd> &quot;Ignoring unknown extended header keyword &#8216;%s&#8217;&quot;</dd>
<dt><code>decompress-program</code></dt>
<dd> Controls verbose description of failures occurring when trying to run alternative decompressor programs. This warning is disabled by default (unless <code>&#8211;verbose</code> is used). A common example of what you can get when using this warning is: </dd>
<p> $ tar &#8211;warning=decompress-program -x -f archive.Z tar (child): cannot run compress: No such file or directory tar (child): trying gzip </p>
<p> This means that <code>tar</code> first tried to decompress <code>archive.Z</code> using <code>compress</code>, and, when that failed, switched to <code>gzip</code>.</p>
<dt><code>record-size</code></dt>
<dd> &quot;Record size = %lu blocks&quot;</dd>
<dt>
</dt><dd>Keywords controlling incremental extraction:</dd>
<dt><code>rename-directory</code></dt>
<dd> &quot;%s: Directory has been renamed from %s&quot;<br />
 &quot;%s: Directory has been renamed&quot;</dd>
<dt><code>new-directory</code></dt>
<dd> &quot;%s: Directory is new&quot;</dd>
<dt><code>xdev</code></dt>
<dd> &quot;%s: directory is on a different device: not purging&quot;</dd>
<dt><code>bad-dumpdir</code></dt>
<dd> &quot;Malformed dumpdir: &#8216;X&#8217; never used&quot;</dd></dl>
</dl>
<dt><code>-w</code>, <code>&#8211;interactive</code>, <code>&#8211;confirmation</code></dt>
<dd> Ask for confirmation for every action.</dd></dl>
<h3>Compatibility options</h3>
<dl>
<dt><code>-o</code></dt>
<dd> When creating, same as <code>&#8211;old-archive</code>. When extracting, same as <code>&#8211;no-same-owner</code>.</dd></dl>
<h3>Size suffixes</h3>
<pre>
        Suffix    Units                   Byte Equivalent
        b         Blocks                  <i>SIZE</i> x 512
        B         Kilobytes               <i>SIZE</i> x 1024
        c         Bytes                   <i>SIZE</i>
        G         Gigabytes               <i>SIZE</i> x 1024^3
        K         Kilobytes               <i>SIZE</i> x 1024
        k         Kilobytes               <i>SIZE</i> x 1024
        M         Megabytes               <i>SIZE</i> x 1024^2
        P         Petabytes               <i>SIZE</i> x 1024^5
        T         Terabytes               <i>SIZE</i> x 1024^4
        w         Words                   <i>SIZE</i> x 2
</pre>
<h2>RETURN VALUE</h2>
<p> Tar exit code indicates whether it was able to successfully perform the requested operation, and if not, what kind of error occurred.</p>
<dl>
<dt><code>0</code></dt>
<dd> Successful termination.</dd>
<dt><code>1</code></dt>
<dd> <i>Some files differ.</i> If tar was invoked with the <code>&#8211;compare</code> (<code>&#8211;diff</code>, <code>-d</code>) command line option, this means that some files in the archive differ from their disk counterparts. If tar was given one of the <code>&#8211;create</code>, <code>&#8211;append</code> or <code>&#8211;update</code> options, this exit code means that some files were changed while being archived and so the resulting archive does not contain the exact copy of the file set.</dd>
<dt><code>2</code></dt>
<dd> <i>Fatal error.</i> This means that some fatal, unrecoverable error occurred.</dd></dl>
<p> If a subprocess that had been invoked by <code>tar</code> exited with a nonzero exit code, <code>tar</code> itself exits with that code as well. This can happen, for example, if a compression option (e.g. <code>-z</code>) was used and the external compressor program failed. Another example is <code>rmt</code> failure during backup to a remote device.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-lzma/">lzma</a></code>(1), <code><a href="/docs/linux/man/1-lzop/">lzop</a></code>(1), <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1), <code><a href="/docs/linux/man/1-zstd/">zstd</a></code>(1). </p>
<p> Complete <code>tar</code> manual: run <code>info tar</code> or use <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1) info mode to read it. </p>
<p> Online copies of <code>GNU tar</code> documentation in various formats can be found at: </p>
<p> <code><a rel="nofollow" href="http://www.gnu.org/software/tar/manual">http://www.gnu.org/software/tar/manual</a></code></p>
<h2>BUG REPORTS</h2>
<p> Report bugs to &lt;bug-tar [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013-2019 Free Software Foundation, Inc.<br />
 License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
