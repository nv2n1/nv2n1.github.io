---
title: "star(1)"
name: "star"
section: "1"
letter: "s"
url: "/docs/linux/man/1-star/"
description: "star – unique standard tape archiver"
---

<h2>NAME</h2>
<p> star &#8211; unique standard tape archiver</p>
<h2>SYNOPSIS</h2>
<p> <code>star&nbsp;<wbr></code> <i>command</i> [<i>options</i>] [<code>-find</code>] <i>file1 &#8230; filen</i> [<i>find_expr</i>]<br />
 <code>ustar</code> <i>command</i> [<i>options</i>] [<code>-find</code>] <i>file1 &#8230; filen</i> [<i>find_expr</i>]<br />
 <code>tar&nbsp;<wbr>&nbsp;<wbr></code> <i>command</i> [<i>options</i>] <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code> <i>file1 &#8230; filen</i><br />
 <code>star&nbsp;<wbr></code> <code>-copy&nbsp;<wbr>&nbsp;<wbr></code> [<i>options</i>] [<code>-find</code>] <i>file1 &#8230;</i> [<i>f_expr</i>] directory<br />
 <code>star&nbsp;<wbr></code> <code>-copy&nbsp;<wbr>&nbsp;<wbr></code> [<i>options</i>] <code>-C</code> <i>from_directory . to_directory</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Star</code> is a very fast <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) like tape archiver with improved functionality. </p>
<p> <code>Star</code> archives and extracts multiple files to and from a single file called a <i>tarfile. </i> A <i>tarfile</i> is usually a magnetic tape, but it can be any file. In all cases, appearance of a directory name refers to the files and (recursively) subdirectories of that directory. </p>
<p> <code>Star&#8217;s</code> actions are controlled by the mandatory command flags from the list below. The way <code>star </code> acts may be modified by additional options. </p>
<p> Note that unpacking tar archives may be a security risk because <code>star</code> may overwrite existing files. See SECURITY NOTES for more information.</p>
<h2>FEATURES</h2>
<p> <code>Star</code> includes the first free implementation of <code>POSIX.1-2001</code> extended <code>tar</code> headers. The <code>POSIX.1-2001</code> extended <code>tar</code> headers define a new standard way for going beyond the limitations of the historic <code>tar</code> format. They allow (among others) to archive all UNIX time stamps in sub-second resolution, files of arbitrary size and filenames without length limitation using <code>UNICODE UTF-8</code> coding for best exchange compatibility. </p>
<p> <code>Star</code> by default uses a fifo to optimize data flow from/to tape. This results in a normally streaming tape during the whole backup. See <code>-fifo </code> and <code>fs=</code> option to get information on how to find the best fifo size. </p>
<p> <code>Star </code> includes a pattern matcher to control the list of files to be processed. This gives a convenient interface for archiving and restoring complex lists of files. In conjunction with the <code>-w </code> flag it is easy to merge a <code>tar</code> archive into an existing file tree. See also <code>-U </code> option. In create mode use the <code>pat=</code> option to specify either select or exclude patterns (depending on the <code>-V</code> flag). In extract or list mode all file type arguments are interpreted as select patterns while the patterns specified with the <code>pat=</code> option may be used as select or exclude patterns (depending on the <code>-V</code> flag). Have a look at the description of the <code>-C</code> option to learn how to fetch files from a list of directories (in create mode) or to distribute files to a list of directories (in extract mode). A substitute option allows <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1) like pattern substitution in file names. </p>
<p> <code>Star</code> includes an enhanced function that is similar to the <code><a href="/docs/linux/man/1-find/">find</a></code>(1) command (see <code><a href="/docs/linux/man/1-sfind/">sfind</a></code>(1)). This allows to use <code>find</code> expressions, even in extract or list mode, directly on the content on an archive. The extensions to <code><a href="/docs/linux/man/1-find/">find</a></code>(1) allow to modify the file metadata. </p>
<p> <code>Star </code> includes a sophisticated diff command. Several diff options allow user tailorable functionality. <code>Star </code> won&#8217;t show you differences you are not interested in. Check the <code>diffopts=</code> option for more details. </p>
<p> <code>Star </code> has no limitation on filename length. Pathnames and linknames up to <i>PATH_MAX</i> (1023 bytes with old OS versions and 4095 bytes with POSIX.1-2001) may be archived. Later versions may be able to deal with longer pathnames. </p>
<p> <code>Star </code> deals with all 3 times, available for files on UNIX systems if the archive format is either chosen from the star specific formats or is a format that uses POSIX.1-2001 extended headers. This is either done in second resolution by using a star specific POSIX.1-1988 compatible extension or in sub second resolution by using POSIX.1-2001 extended headers. <code>Star </code> is able to store and restore all 3 times (mtime, atime and even ctime). On Solaris 2.x systems, <code>star </code> is able to do backups without changing any of the 3 the times. </p>
<p> If used with the <code>H=</code><i>ustar</i> option, or if called as <code>ustar</code> or <code>tar</code> while the <code>H=</code>headertype option is not used, <code>star</code> is 100% POSIX compliant. </p>
<p> <code>Star&#8217;s </code> default format (if called as <code>star</code>) is <i>xstar</i> and is as posix compliant as possible. Enhancements to the standard that prevent correct extraction of single files when using a different <code>tar </code> implementation that is only POSIX.1-1988 compliant may occur, but they only affect single files with a pathname that is longer than 100+130 chars or when archiving sparse files with the <code>-sparse</code> option in effect. All other files will extract correctly. See the description for the <code>H=</code><i>headertype</i> option below for more information on archive formats and possible archive interchange problems. </p>
<p> <code>Star </code> makes it easy to repair corrupted filesystems. After a fsck -y has been run on the filesystem, <code>star </code> is able to restore only the missing files automatically. Use then <i>star -diff</i> to check for differences (see EXAMPLES for more information). </p>
<p> <code>Star </code> automatically recognizes the type of the archive. <code>Star </code> therefore is able to handle features and properties of different archive types in their native mode, if it knows about the peculiarities of the archive type. See the <code>H=</code>headertype option for more details. To be able to do this, <code>star</code> adds hidden fingerprints to the archive header that allows to recognise all star specific archive formats. The GNU tar format is recognised by the way it deviates from the standard. </p>
<p> <code>Star </code> automatically recognizes and handles byte swapped archives. There is no option to manually control byte swapping. </p>
<p> <code>Star</code> automatically recognizes and handles compressed archives inside plain files. </p>
<p> <code>Star</code> is able to archive and restore <code>Access Control Lists</code> for files using POSIX.1-2001 extended headers.</p>
<h2>COMMAND</h2>
<p> In native mode, <code>star</code> is compatible to the command line syntax of a typical POSIX command and for this reason expects <i>commands</i> and <i>options</i> to start with a single dash (-). In this case, commands and options may be specified separately, all boolean or increment type options may be specified either separately or combined. For compatibility with GNU programs, long options may alternatively start with a double dash. In compatibility mode to POSIX <code>tar</code>, <code>star</code> expects commands and options to appear as one single string that does not start with a dash. In POSIX tar compatibility mode, additional non POSIX options may be specified but must appear after the POSIX options and their args and need to start with a dash.</p>
<dl>
<dt><code>-c</code></p>
<dd> Create a new <i>tarfile</i> and write named files into it. Writing starts at the beginning of <i>tarfile.</i> See -v option for information on how to increase verbosity while the archive is written.</p>
<dt><code>-copy</code></p>
<dd> Copy named files to the target directory which is the last file type argument. The target directory must exist. The shorthand <code>-cx</code> instead of <code>-copy</code> is not allowed because this could be a result of a typo. </p>
<p> If the option <code>-diff</code> has been specified in addition, <code>star</code> performs a one pass directory tree compare instead of copying files. The shorthand <code>-c -diff</code> instead of <code>-copy -diff</code> is also allowed. </p>
<p> On operating systems with slow file I/O (such as Linux), it may help to use <code>-no-fsync</code> in addition, but then <code>star</code> is unable to detect all error conditions; so use with care. </p>
<p> If the option <code>-t</code> has been specified in addition, the last file type argument is not a target directory and <code>star</code> is performing a one pass listing instead of copying files. This makes sense as the listing from <code>star</code> may be better readable than the output from <code>ls -lR</code>. The shorthand <code>-c -t</code> or <code>-ct</code> instead of <code>-copy -t</code> is also allowed. </p>
<p> The job is by default done in the best archive mode. This implies that it defaults to <code>H=exustar -dump</code>. When in <code>-copy</code> mode, <code>star</code> forks into two processes and data exchange is done via the shared memory from the FIFO. This gives the best possible performance. Without FIFO, the <code>-copy</code> mode will not work. </p>
<p> The <code>list=</code> option, patterns and substitutions apply only to the create side of the copy command.</p>
<dt><code>-diff</code></p>
<dd> Compare the content and the attributes of the files from the archive in <i>tarfile</i> to the filesystem. This may also be used to compare two file trees in the filesystem. If you use a set of <i>diffopts</i> that fits your needs, it will give &#8211; in many cases &#8211; a more readable output than diff -r. If you use <code>star&#8217;s</code> dump extensions for the tar archive, the <code>-diff</code> option allows to find even if the directory in the file tree contains more files than the archive. This way, it is possible to compare all properties of two file trees in one run. See <i>diffopts </i> for more details. Adding one or more <code>-v</code> options increases the verbosity. With <code>-vv</code> and above, the directory content is compared also if <code>star</code> is reading a tar archive that has been created in <code>-dump</code> mode.</p>
<dt><code>-n</code></p>
<dd> No extraction. Show what <code>star </code> would do, in case the <code>-x</code> command had been specified.</p>
<dt><code>-r</code></p>
<dd> Replace files in a <i>tarfile.</i> The named files are written to the end of <i>tarfile.</i> This implies that later, the appropriate files will be found more than once on the <i>tarfile.</i></p>
<dt><code>-t</code></p>
<dd> Table of contents. List the contents of the <i>tarfile.</i> If the -v flag is used, the listing is similar to the format of ls -l output. With this option, the flags <code>-a</code>, <code>-atime</code> and <code>-ctime</code> have a different meaning if the archive is in <code>star</code>, <code>xstar</code>, <code>xustar</code>, <code>exustar</code>, or <code>pax </code> format. The option <code>-a</code> or <code>-atime</code> lists the access time instead of the modification time, the option <code>-ctime</code> lists the file creation time instead of the modification time. The option <code>-tpath</code> may be used in addition to modify the output so it may be used in shell scripts.</p>
<dt><code>-u</code></p>
<dd> Update a <i>tarfile.</i> The named files are written to the end of <i>tarfile</i> if they are not already there or if the files are newer than the files of the same name found in the archive. The -r and -u command only work if the <code>tar</code> archives is a regular file or if the <code>tar</code> archive is an unblocked tape that may backspace.</p>
<dt><code>-x</code></p>
<dd> Extract the named files from the <i>tarfile.</i> If no filename argument or pattern is specified, the entire content of the <i>tarfile</i> is restored. If the -U flag is not used, <code>star </code> extracts no file which is older than the corresponding file on disk. </p>
<p> On operating systems with slow file I/O (such as Linux), it may help to use <code>-no-fsync</code> in addition, but then <code>star</code> is unable to detect all error conditions; so use with care.</dl>
<p> Except for the shorthands documented above, exactly one of the commands above must be specified. </p>
<p> If one or more patterns or substitution commands have been specified, they apply to any of the command listed above. In copy mode, all patterns and substitute commands apply to the create side. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a summary of the most important options for <code><a href="/docs/linux/man/1-star/">star</a></code>(1).</p>
<dt><code>-xhelp</code></p>
<dd> Print a summary of the less important options for <code><a href="/docs/linux/man/1-star/">star</a></code>(1).</p>
<dt><code>-/</code></p>
<dd> Don&#8217;t strip leading slashes from file names when extracting an archive. Tar archives containing absolute pathnames are usually a bad idea. With other <code>tar </code> implementations, they may possibly never be extracted without clobbering existing files. <code>Star </code> for that reason, by default strips leading slashes from filenames when in extract mode. As it may be impossible to create an archive where leading slashes have been stripped while retaining correct path names, <code>star</code> does not strip leading slashes in create mode. </p>
<p> See SECURITY NOTES for more information.</p>
<dt><code>-..</code></p>
<dd> Don&#8217;t skip files that contain /../ in the name. Tar archives containing names with /../ could be used to compromise the system. If they are unpacked together with a lot of other files, this would in most cases not even be noticed. For this reason, <code>star</code> by default does not extract files that contain /../ in the name if <code>star</code> is not in interactive mode (see <code>-w</code> option). </p>
<p> See SECURITY NOTES for more information.</p>
<dt><code>-7z</code></p>
<dd> run the input or output through a <code>p7zip</code> pipe &#8211; see option <code>-z</code> below. </p>
<p> Note that the <code>p7zip</code> program currently does not operate on a pipe but on a /tmp file copy and thus limits the maximum archive size. </p>
<dt><code>-0</code></p>
<dd>
<dt><code>-1</code></p>
<dd>
<dt><code>-2</code></p>
<dd>
<dt><code>-3</code></p>
<dd>
<dt><code>-4</code></p>
<dd>
<dt><code>-5</code></p>
<dd>
<dt><code>-6</code></p>
<dd>
<dt><code>-7</code></p>
<dd> Select an archive entry from <code>/etc/default/star</code>. The format for the archive entries is the same as the format in <code>/etc/default/tar</code> in Solaris.</p>
<dt><code>-acl</code></p>
<dd> Handle <code>Access Control List</code> (ACL) information in create and extract mode. If <code>-acl</code> has been specified, <code>star </code> is in create mode and the header type is <code>exustar</code>, <code>star</code> will add ACL information to the archive using POSIX.1-2001 extended headers. If <code>-acl</code> has been specified and <code>star </code> is in extract mode, <code>star</code> will try to restore ACL information. If there is no ACL information for one or all files in the archive, <code>star</code> will clear the ACL information for the specific file. Note that if <code>-acl</code> has not been specified, <code>star</code> will not handle ACL information at all and files may inherit ACL information from the parent directories. If the <code>-acl</code> option has been specified, <code>star</code> assumes that the <code>-p</code> option has been specified too.</p>
<dt><code>artype=</code><i>headertype</i></p>
<dd> Generate a tape archive in <i>headertype</i> format. If this option is used in extract/list mode this forces <code>star</code> to interpret the headers to be of type <i>headertype.</i> As <code>star</code> even in case of a user selected extract archive format does format checking, it may be that you will not be able to unpack a specific archive with all possible forced archive formats. Selecting the old <code>tar</code> format for extraction will always work though. Valid parameter for <i>headertype</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>help</code></p>
<dd> Print a help message about possible header types.</p>
<dt><code>v7tar</code></p>
<dd> Old UNIX V7 <code>tar</code> format. This archive format may only store plain files. Pathnames or linknames longer than 99 chars may not be archived. </p>
<p> If the <code>v7tar</code> format has been selected, <code>star</code> will not use enhancements to the historic UNIX V7 tar format. File size is limited to 2 GB &#8211; 2 bytes, uid/gid is limited to 262143. Sparse files will be filled up with zeroes.</p>
<dt><code>tar</code></p>
<dd> Old BSD UNIX <code>tar</code> format. This archive format may only store plain files, directories and symbolic links. Pathnames or linknames longer than 99 chars may not be archived. See also the <code>-d</code> option as a note to some even older tar implementations. </p>
<p> If the <code>tar</code> format has been selected, <code>star</code> will not use enhancements to the historic tar format. File size is limited to 2 GB &#8211; 2 bytes, uid/gid is limited to 262143. Sparse files will be filled up with zeroes.</p>
<dt><code>star</code></p>
<dd> Old <code>star </code> standard format. This is an upward/downward compatible enhancement of the <i>old </i> (pre Posix) UNIX <code>tar</code> format. It has been introduced in 1985 and therefore is not Posix compliant. The <code>star</code> format allows to archive special files (even sockets) and records access time and creation time besides the modification time. Newer versions of the old <code>star </code> format allow very long filenames (100+155 chars and above), linknames &gt; 100 chars and sparse files (if <code>-sparse</code> is used). This format is able to copy the device nodes on HP-UX that have 24 bits in the minor device number, which is more then the 21 bits that are possible with the POSIX-1003.1-1988 archive format. </p>
<p> The nonstandard extensions are located in the space between the link name and the POSIX file name prefix. As the <code>star</code> format does not use a POSIX magic string, the extensions do not interfere with the POSIX tar formats. The last 4 bytes of the <code>tar</code> header contain a &#8216;tar
