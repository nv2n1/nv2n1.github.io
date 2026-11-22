---

title: "star(1)"
name: "star"
section: "1"
letter: "s"
url: "/docs/linux/man/1-star/"
description: "star – unique standard tape archiver"
---

<p> star - unique standard tape archiver  </p>
<h2>SYNOPSIS</h2>
<p> <code>star&nbsp;<wbr></code> <i>command</i> [<i>options</i>] [<code>-find</code>] <i>file1 ... filen</i> [<i>find_expr</i>] <br/>
 <code>ustar</code> <i>command</i> [<i>options</i>] [<code>-find</code>] <i>file1 ... filen</i> [<i>find_expr</i>] <br/>
 <code>tar&nbsp;<wbr>&nbsp;<wbr></code> <i>command</i> [<i>options</i>] <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code> <i>file1 ... filen</i> <br/>
 <code>star&nbsp;<wbr></code> <code>-copy&nbsp;<wbr>&nbsp;<wbr></code> [<i>options</i>] [<code>-find</code>] <i>file1 ...</i> [<i>f_expr</i>] directory <br/>
 <code>star&nbsp;<wbr></code> <code>-copy&nbsp;<wbr>&nbsp;<wbr></code> [<i>options</i>] <code>-C</code> <i>from_directory . to_directory</i>  </p>
<h2>DESCRIPTION</h2>
<p> <code>Star</code> is a very fast <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) like tape archiver with improved functionality. </p>
<p> <code>Star</code> archives and extracts multiple files to and from a single file called a <i>tarfile. </i> A <i>tarfile</i> is usually a magnetic tape, but it can be any file. In all cases, appearance of a directory name refers to the files and (recursively) subdirectories of that directory. </p>
<p> <code>Star&#8217;s</code> actions are controlled by the mandatory command flags from the list below. The way <code>star </code> acts may be modified by additional options. </p>
<p> Note that unpacking tar archives may be a security risk because <code>star</code> may overwrite existing files. See SECURITY NOTES for more information.  </p>
<h2>FEATURES</h2>
<p> <code>Star</code> includes the first free implementation of <code>POSIX.1-2001</code> extended <code>tar</code> headers. The <code>POSIX.1-2001</code> extended <code>tar</code> headers define a new standard way for going beyond the limitations of the historic <code>tar</code> format. They allow (among others) to archive all UNIX time stamps in sub-second resolution, files of arbitrary size and filenames without length limitation using <code>UNICODE UTF-8</code> coding for best exchange compatibility. </p>
<p> <code>Star</code> by default uses a fifo to optimize data flow from/to tape. This results in a normally streaming tape during the whole backup. See <code>-fifo </code> and <code>fs=</code> option to get information on how to find the best fifo size. </p>
<p> <code>Star </code> includes a pattern matcher to control the list of files to be processed. This gives a convenient interface for archiving and restoring complex lists of files. In conjunction with the <code>-w </code> flag it is easy to merge a <code>tar</code> archive into an existing file tree. See also <code>-U </code> option. In create mode use the <code>pat=</code> option to specify either select or exclude patterns (depending on the <code>-V</code> flag). In extract or list mode all file type arguments are interpreted as select patterns while the patterns specified with the <code>pat=</code> option may be used as select or exclude patterns (depending on the <code>-V</code> flag). Have a look at the description of the <code>-C</code> option to learn how to fetch files from a list of directories (in create mode) or to distribute files to a list of directories (in extract mode). A substitute option allows <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1) like pattern substitution in file names. </p>
<p> <code>Star</code> includes an enhanced function that is similar to the <code><a href="/docs/linux/man/1-find/">find</a></code>(1) command (see <code>sfind</code>(1)). This allows to use <code>find</code> expressions, even in extract or list mode, directly on the content on an archive. The extensions to <code><a href="/docs/linux/man/1-find/">find</a></code>(1) allow to modify the file metadata. </p>
<p> <code>Star </code> includes a sophisticated diff command. Several diff options allow user tailorable functionality. <code>Star </code> won&#8217;t show you differences you are not interested in. Check the <code>diffopts=</code> option for more details. </p>
<p> <code>Star </code> has no limitation on filename length. Pathnames and linknames up to <i>PATH_MAX</i> (1023 bytes with old OS versions and 4095 bytes with POSIX.1-2001) may be archived. Later versions may be able to deal with longer pathnames. </p>
<p> <code>Star </code> deals with all 3 times, available for files on UNIX systems if the archive format is either chosen from the star specific formats or is a format that uses POSIX.1-2001 extended headers. This is either done in second resolution by using a star specific POSIX.1-1988 compatible extension or in sub second resolution by using POSIX.1-2001 extended headers. <code>Star </code> is able to store and restore all 3 times (mtime, atime and even ctime). On Solaris 2.x systems, <code>star </code> is able to do backups without changing any of the 3 the times. </p>
<p> If used with the <code>H=</code><i>ustar</i> option, or if called as <code>ustar</code> or <code>tar</code> while the <code>H=</code>headertype option is not used, <code>star</code> is 100% POSIX compliant. </p>
<p> <code>Star&#8217;s </code> default format (if called as <code>star</code>) is <i>xstar</i> and is as posix compliant as possible. Enhancements to the standard that prevent correct extraction of single files when using a different <code>tar </code> implementation that is only POSIX.1-1988 compliant may occur, but they only affect single files with a pathname that is longer than 100+130 chars or when archiving sparse files with the <code>-sparse</code> option in effect. All other files will extract correctly. See the description for the <code>H=</code><i>headertype</i> option below for more information on archive formats and possible archive interchange problems. </p>
<p> <code>Star </code> makes it easy to repair corrupted filesystems. After a fsck -y has been run on the filesystem, <code>star </code> is able to restore only the missing files automatically. Use then <i>star -diff</i> to check for differences (see EXAMPLES for more information). </p>
<p> <code>Star </code> automatically recognizes the type of the archive. <code>Star </code> therefore is able to handle features and properties of different archive types in their native mode, if it knows about the peculiarities of the archive type. See the <code>H=</code>headertype option for more details. To be able to do this, <code>star</code> adds hidden fingerprints to the archive header that allows to recognise all star specific archive formats. The GNU tar format is recognised by the way it deviates from the standard. </p>
<p> <code>Star </code> automatically recognizes and handles byte swapped archives. There is no option to manually control byte swapping. </p>
<p> <code>Star</code> automatically recognizes and handles compressed archives inside plain files. </p>
<p> <code>Star</code> is able to archive and restore <code>Access Control Lists</code> for files using POSIX.1-2001 extended headers.  </p>
<h2>COMMAND</h2>
<p> In native mode, <code>star</code> is compatible to the command line syntax of a typical POSIX command and for this reason expects <i>commands</i> and <i>options</i> to start with a single dash (-). In this case, commands and options may be specified separately, all boolean or increment type options may be specified either separately or combined. For compatibility with GNU programs, long options may alternatively start with a double dash. In compatibility mode to POSIX <code>tar</code>, <code>star</code> expects commands and options to appear as one single string that does not start with a dash. In POSIX tar compatibility mode, additional non POSIX options may be specified but must appear after the POSIX options and their args and need to start with a dash. </p>
<dl>
<dt><code>-c</code></dt>
<dd> <p> Create a new <i>tarfile</i> and write named files into it. Writing starts at the beginning of <i>tarfile.</i> See -v option for information on how to increase verbosity while the archive is written. </p>
 </dd>
<dt><code>-copy</code></dt>
<dd> <p> Copy named files to the target directory which is the last file type argument. The target directory must exist. The shorthand <code>-cx</code> instead of <code>-copy</code> is not allowed because this could be a result of a typo. </p>
<p> If the option <code>-diff</code> has been specified in addition, <code>star</code> performs a one pass directory tree compare instead of copying files. The shorthand <code>-c -diff</code> instead of <code>-copy -diff</code> is also allowed. </p>
<p> On operating systems with slow file I/O (such as Linux), it may help to use <code>-no-fsync</code> in addition, but then <code>star</code> is unable to detect all error conditions; so use with care. </p>
<p> If the option <code>-t</code> has been specified in addition, the last file type argument is not a target directory and <code>star</code> is performing a one pass listing instead of copying files. This makes sense as the listing from <code>star</code> may be better readable than the output from <code>ls -lR</code>. The shorthand <code>-c -t</code> or <code>-ct</code> instead of <code>-copy -t</code> is also allowed. </p>
<p> The job is by default done in the best archive mode. This implies that it defaults to <code>H=exustar -dump</code>. When in <code>-copy</code> mode, <code>star</code> forks into two processes and data exchange is done via the shared memory from the FIFO. This gives the best possible performance. Without FIFO, the <code>-copy</code> mode will not work. </p>
<p> The <code>list=</code> option, patterns and substitutions apply only to the create side of the copy command. </p>
 </dd>
<dt><code>-diff</code></dt>
<dd> <p> Compare the content and the attributes of the files from the archive in <i>tarfile</i> to the filesystem. This may also be used to compare two file trees in the filesystem. If you use a set of <i>diffopts</i> that fits your needs, it will give - in many cases - a more readable output than diff -r. If you use <code>star&#8217;s</code> dump extensions for the tar archive, the <code>-diff</code> option allows to find even if the directory in the file tree contains more files than the archive. This way, it is possible to compare all properties of two file trees in one run. See <i>diffopts </i> for more details. Adding one or more <code>-v</code> options increases the verbosity. With <code>-vv</code> and above, the directory content is compared also if <code>star</code> is reading a tar archive that has been created in <code>-dump</code> mode. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> No extraction. Show what <code>star </code> would do, in case the <code>-x</code> command had been specified. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Replace files in a <i>tarfile.</i> The named files are written to the end of <i>tarfile.</i> This implies that later, the appropriate files will be found more than once on the <i>tarfile.</i> </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Table of contents. List the contents of the <i>tarfile.</i> If the -v flag is used, the listing is similar to the format of ls -l output. With this option, the flags <code>-a</code>, <code>-atime</code> and <code>-ctime</code> have a different meaning if the archive is in <code>star</code>, <code>xstar</code>, <code>xustar</code>, <code>exustar</code>, or <code>pax </code> format. The option <code>-a</code> or <code>-atime</code> lists the access time instead of the modification time, the option <code>-ctime</code> lists the file creation time instead of the modification time. The option <code>-tpath</code> may be used in addition to modify the output so it may be used in shell scripts. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Update a <i>tarfile.</i> The named files are written to the end of <i>tarfile</i> if they are not already there or if the files are newer than the files of the same name found in the archive. The -r and -u command only work if the <code>tar</code> archives is a regular file or if the <code>tar</code> archive is an unblocked tape that may backspace. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> Extract the named files from the <i>tarfile.</i> If no filename argument or pattern is specified, the entire content of the <i>tarfile</i> is restored. If the -U flag is not used, <code>star </code> extracts no file which is older than the corresponding file on disk. </p>
<p> On operating systems with slow file I/O (such as Linux), it may help to use <code>-no-fsync</code> in addition, but then <code>star</code> is unable to detect all error conditions; so use with care. </p>
 </dd></dl>
<p> Except for the shorthands documented above, exactly one of the commands above must be specified. </p>
<p> If one or more patterns or substitution commands have been specified, they apply to any of the command listed above. In copy mode, all patterns and substitute commands apply to the create side. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></dt>
<dd> <p> Print a summary of the most important options for <code><a href="/docs/linux/man/1-star/">star</a></code>(1). </p>
 </dd>
<dt><code>-xhelp</code></dt>
<dd> <p> Print a summary of the less important options for <code><a href="/docs/linux/man/1-star/">star</a></code>(1). </p>
 </dd>
<dt><code>-/</code></dt>
<dd> <p> Don&#8217;t strip leading slashes from file names when extracting an archive. Tar archives containing absolute pathnames are usually a bad idea. With other <code>tar </code> implementations, they may possibly never be extracted without clobbering existing files. <code>Star </code> for that reason, by default strips leading slashes from filenames when in extract mode. As it may be impossible to create an archive where leading slashes have been stripped while retaining correct path names, <code>star</code> does not strip leading slashes in create mode. </p>
<p> See SECURITY NOTES for more information. </p>
 </dd>
<dt><code>-..</code></dt>
<dd> <p> Don&#8217;t skip files that contain /../ in the name. Tar archives containing names with /../ could be used to compromise the system. If they are unpacked together with a lot of other files, this would in most cases not even be noticed. For this reason, <code>star</code> by default does not extract files that contain /../ in the name if <code>star</code> is not in interactive mode (see <code>-w</code> option). </p>
<p> See SECURITY NOTES for more information. </p>
 </dd>
<dt><code>-7z</code></dt>
<dd> <p> run the input or output through a <code>p7zip</code> pipe - see option <code>-z</code> below. </p>
<p> Note that the <code>p7zip</code> program currently does not operate on a pipe but on a /tmp file copy and thus limits the maximum archive size. </p>
 </dd>
<dt><code>-0</code></dt>
<dd>  </dd>
<dt><code>-1</code></dt>
<dd>  </dd>
<dt><code>-2</code></dt>
<dd>  </dd>
<dt><code>-3</code></dt>
<dd>  </dd>
<dt><code>-4</code></dt>
<dd>  </dd>
<dt><code>-5</code></dt>
<dd>  </dd>
<dt><code>-6</code></dt>
<dd>  </dd>
<dt><code>-7</code></dt>
<dd> <p> Select an archive entry from <code>/etc/default/star</code>. The format for the archive entries is the same as the format in <code>/etc/default/tar</code> in Solaris. </p>
 </dd>
<dt><code>-acl</code></dt>
<dd> <p> Handle <code>Access Control List</code> (ACL) information in create and extract mode. If <code>-acl</code> has been specified, <code>star </code> is in create mode and the header type is <code>exustar</code>, <code>star</code> will add ACL information to the archive using POSIX.1-2001 extended headers. If <code>-acl</code> has been specified and <code>star </code> is in extract mode, <code>star</code> will try to restore ACL information. If there is no ACL information for one or all files in the archive, <code>star</code> will clear the ACL information for the specific file. Note that if <code>-acl</code> has not been specified, <code>star</code> will not handle ACL information at all and files may inherit ACL information from the parent directories. If the <code>-acl</code> option has been specified, <code>star</code> assumes that the <code>-p</code> option has been specified too. </p>
 </dd>
<dt><code>artype=</code><i>headertype</i></dt>
<dd> <p> Generate a tape archive in <i>headertype</i> format. If this option is used in extract/list mode this forces <code>star</code> to interpret the headers to be of type <i>headertype.</i> As <code>star</code> even in case of a user selected extract archive format does format checking, it may be that you will not be able to unpack a specific archive with all possible forced archive formats. Selecting the old <code>tar</code> format for extraction will always work though. Valid parameter for <i>headertype</i> are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>help</code></dt>
<dd> <p> Print a help message about possible header types. </p>
 </dd>
<dt><code>v7tar</code></dt>
<dd> <p> Old UNIX V7 <code>tar</code> format. This archive format may only store plain files. Pathnames or linknames longer than 99 chars may not be archived. </p>
<p> If the <code>v7tar</code> format has been selected, <code>star</code> will not use enhancements to the historic UNIX V7 tar format. File size is limited to 2 GB - 2 bytes, uid/gid is limited to 262143. Sparse files will be filled up with zeroes. </p>
 </dd>
<dt><code>tar</code></dt>
<dd> <p> Old BSD UNIX <code>tar</code> format. This archive format may only store plain files, directories and symbolic links. Pathnames or linknames longer than 99 chars may not be archived. See also the <code>-d</code> option as a note to some even older tar implementations. </p>
<p> If the <code>tar</code> format has been selected, <code>star</code> will not use enhancements to the historic tar format. File size is limited to 2 GB - 2 bytes, uid/gid is limited to 262143. Sparse files will be filled up with zeroes. </p>
 </dd>
<dt><code>star</code></dt>
<dd> <p> Old <code>star </code> standard format. This is an upward/downward compatible enhancement of the <i>old </i> (pre Posix) UNIX <code>tar</code> format. It has been introduced in 1985 and therefore is not Posix compliant. The <code>star</code> format allows to archive special files (even sockets) and records access time and creation time besides the modification time. Newer versions of the old <code>star </code> format allow very long filenames (100+155 chars and above), linknames &gt; 100 chars and sparse files (if <code>-sparse</code> is used). This format is able to copy the device nodes on HP-UX that have 24 bits in the minor device number, which is more then the 21 bits that are possible with the POSIX-1003.1-1988 archive format. </p>
<p> The nonstandard extensions are located in the space between the link name and the POSIX file name prefix. As the <code>star</code> format does not use a POSIX magic string, the extensions do not interfere with the POSIX tar formats. The last 4 bytes of the <code>tar</code> header contain a &#8216;tar\0&#8217; signature. </p>
 </dd>
<dt><code>gnutar</code></dt>
<dd> <p> This is a commonly used, but unfortunately not Posix compliant (although designed after 1987) enhancement to the old <code>tar </code> format. The <code>gnutar</code> format has been defined between 1989 and 1994. Do not use the <code>gnutar</code> archive format unless you want to create an archive for a target system that is known to have only the gnutar program available. The <code>gnutar</code> archive format violates basic rules for any (even the historic) tar archive format, in special when sparse files are archived using the <code>-sparse</code> option. Using the <code>gnutar</code> archive format causes a high risk that the resulting archive may only be read by gnutar or by <code>star</code>. The implementation of the gnutar archive format within <code>star</code> is not complete, but sufficient for most gnutar archives. See NOTES for more information. </p>
 </dd>
<dt><code>ustar</code></dt>
<dd> <p> IEEE/Posix1003/IEC-9945-1-1988 Standard Data Interchange format. With this option in effect, <code>star </code> will generate 100% POSIX.1-1988 compliant <code>tar</code> archives. Files with pathnames longer than 100+155 chars or linknames longer than 100 chars may not be archived. If <code>star</code> is called as <code>ustar</code> the default archive format is <code>ustar</code>. </p>
<p> If the <code>ustar</code> format has been selected, <code>star</code> will not use enhancements to the POSIX.1-1988 tar format, the archive will be strictly conforming. File size is limited to 8 GB, uid/gid/major/minor is limited to 2097151. Sparse files will be filled up with zeroes. </p>
 </dd>
<dt><code>pax</code></dt>
<dd> <p> The IEEE/Posix1003/IEC-9945-1-1988 successor is the POSIX-1003.1-2001 Standard Data Interchange format. It is called the <code>pax</code> archive format. </p>
<p> If the <code>pax</code> format has been selected, <code>star</code> will not use enhancements to the POSIX.1-2001 tar format, the archive will be strictly conforming. File size is unlimited, uid/gid/uname/gidname is unlimited, major/minor is limited to 2097151. Sparse files will be filled up with zeroes. </p>
 </dd>
<dt><code>xstar</code></dt>
<dd> <p> The extended standard <code>tar</code> format has been introduced in 1994. <code>Star</code> uses the <code>xstar</code> format as default archive format. This is an upward/downward compatible enhancement of the IEEE/Posix1003/IEC-9945-1 Standard Data Interchange format. It allows among others very long filenames (100+130 chars and above) and records access time and creation time. Sparse files will be archived correctly (if <code>-sparse</code> is used). </p>
<p> The access time and creation time are stored at the end of the POSIX file name prefix (this limits the prefix to 130 chars). These extensions do not interfere with the POSIX standard as the fields for mtime and ctime field are always separated from the POSIX file name prefix by a null byte. The last 4 bytes of the <code>tar</code> header contain a &#8216;tar\0&#8217; signature. </p>
<p> The <code>xstar</code> format is the default format when <code>star</code> is neither called as <code>tar </code> nor called as <code>ustar</code>. </p>
 </dd>
<dt><code>xustar</code></dt>
<dd> <p> A new format introduced 1998, that omits the &#8216;tar\0&#8217; signature at the end of the <code>tar</code> header. It is otherwise identical to the <code>xstar</code> format. As some <code>tar</code> implementations do not follow the POSIX rules and compute the checksum for less than 512 bytes of the <code>tar</code> header, this format may help to avoid problems with these broken <code>tar</code> implementations. The main other difference to the <code>xstar</code> format is that the <code>xustar</code> format uses POSIX.1-2001 extended headers to overcome limitations of the historic <code>tar</code> format while the <code>xstar</code> format uses proprietary extensions. The <code>xustar</code> format is the default format when <code>star</code> is called as <code>tar</code>. </p>
<p> File size is unlimited, uid/gid/uname/gidname is unlimited, major/minor is unlimited. Sparse files will be archived correctly (if <code>-sparse</code> is used). </p>
 </dd>
<dt><code>exustar</code></dt>
<dd> <p> A format similar to the <code>xustar</code> format but with forced POSIX.1-2001 extended headers. If this format is used together with the <code>-acl</code> option, <code>star</code> records Access Control Lists (ACLs) in POSIX.1-2001 extended headers. </p>
<p> The <code>exustar</code> format allows to archive all file types but it does not archive more than the POSIX.1-1988 set by default. If the <code>-dump</code> option is used or if <code>star</code> is otherwise on dump mode, star archives all file types and in addition archives more meta data then usual. </p>
<p> File size is unlimited, uid/gid/uname/gidname is unlimited, major/minor is unlimited. Sparse files will be archived correctly (if <code>-sparse</code> is used). </p>
 </dd>
<dt><code>suntar</code></dt>
<dd> <p> The extended header format found on Solaris 7/8/9. This format is similar to the <code>pax</code> format but does not handle <i>atime</i> and <i>ctime</i> and in addition uses &#8216;X&#8217; as the typeflag for the extended headers instead of the standard &#8216;x&#8217;. </p>
<p> File size is unlimited, uid/gid/uname/gidname is unlimited, major/minor is unlimited. Sparse files will be filled up with zeroes. </p>
 </dd>
<dt><code>bin</code></dt>
<dd> <p> The cpio UNIX V7 binary format. This is a format with big interoperability problems. Try to avoid this format. It is only present to make the <code>scpio</code> command SVr4 compliant. </p>
 </dd>
<dt><code>cpio</code></dt>
<dd> <p> The POSIX.1-1988 <code>cpio</code> format. This format uses octal ascii headers. A similar format is created by calling <i>cpio -o -c</i> on pre SYSVr4 systems and by calling <i>cpio -o -Hodc</i> on SYSVr4 systems. The POSIX.1-1988 <code>cpio</code> format allows a file name length up to 262142 characters and allows to archive nearly any file type. File size is limited to 8 GB, uid/gid/st_dev is limited to 262143. The way major and minor device numbers are stored inside the st_dev field is implementation dependent. </p>
<p> Even though this archive format is covered by the POSIX.1-1988 standard, it has a lower portability than the <code>ustar</code> format. Try to avoid the <code>cpio</code> archive format. </p>
 </dd>
<dt><code>odc</code></dt>
<dd> <p> This archive format is similar to the The POSIX.1-1988 <code>cpio</code> format but the file name length is limited to 255 characters and the socket file type is not allowed. This archive format has been introduced to allow non POSIX cpio implementations such as the cpio program on SYSV to accept the archive. Use this format whenever you are not sure if the target system offers a fully POSIX compliant cpio program. </p>
<p> Even though this archive format is covered by the POSIX.1-1988 standard, it has a lower portability than the <code>ustar</code> format. Try to avoid the <code>odc</code> archive format. </p>
 </dd>
<dt><code>asc</code></dt>
<dd> <p> Tell <code>star</code> to create a <code>cpio</code> archive in the ascii format that is created with <i>cpio -o -c</i> on SYSVr4 systems. It uses extended (32 bit) numbers for uid&#8217;s, gid&#8217;s and device numbers but limits the file size to 4 GB - 2 bytes although the format has been specified after the POSIX.1-1988 cpio format. Try to avoid the <code>asc</code> archive format because of its limited portability. </p>
 </dd>
<dt><code>crc</code></dt>
<dd> <p> This format is similar to the <code>asc</code> cpio format but in addition uses a simple byte based checksum called here as <code>CRC</code>. This algorithm is simple Sum32 -- not a polynomial CRC. Try to avoid the <code>crc</code> archive format because of its limited portability. </p>
 </dd></dl>
<p> All <code>tar</code> archive formats may be interchanged if the archive contains no files that may not be archived by using the old <code>tar</code> format. Archives in the <i>xstar </i> format may be extracted by any 100% POSIX compliant <code>tar</code> implementation if they contain no files with pathnames &gt;&nbsp;<wbr>100+130 chars and if they contain no sparse files that have been archived by using the <code>-sparse</code> option. </dl>
 </p>
<dt><code>-ask_remove</code></dt>
<dd> <p> obsoleted by -ask-remove </p>
 </dd>
<dt><code>-ask-remove</code></dt>
<dd> <p> Ask to remove non writable files on extraction. By default, <code>star</code> will not overwrite files that are read only. If this option is in effect, <code>star</code> will ask whether it should remove these files to allow the extraction of a file in the following way: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>remove &#8216;</code><i>filename</i><code>&#8216; ? Y(es)/N(o) :</code> </p>
 </dd></dl>
</dl>
<dt><code>-atime</code>, <code>-a</code></dt>
<dd> <p> Reset access time of files after storing them to <i>tarfile.</i> On Solaris 2.x, (if invoked by root) <code>star </code> uses the <i>_FIOSATIME </i> ioctl to do this. This enables <code>star </code> not to trash the <i>ctime</i> while resetting the <i>atime</i> of the files. If the <code>-atime</code> option is used in conjunction with the list command, <code>star </code> lists access time instead of modification time. (This works only in conjunction with the <code>star</code>, <code>xstar</code>, <code>xustar</code>, <code>exustar</code>, and with the <code>pax </code> format.) Another option to retain the access time for the the files that are going to be archives is to readonly mount a <code>UFS snapshot</code> and to archive files from the mount point of the UFS snapshot. </p>
 </dd>
<dt><code>-B</code></dt>
<dd> <p> Force <code>star</code> to perform multiple reads (if necessary) to fill a block. This option exists so that <code>star </code> can work across the Ethernet, since pipes and sockets return partial blocks even when more data is coming. If <code>star</code> uses <i>stdin</i> as archive file, <code>star</code> behaves as if it has been called with the <code>-B</code> option. For this reason, the option -B in practice is rarely needed. </p>
 </dd>
<dt><code>-block-number</code></dt>
<dd> <p> Print the archive block number (archive offset / 512) at the beginning of each line when in verbose mode. This allows to write backup scripts that archive the offsets for files and that use </p>
<p> <code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>mt fsr</code><i> blockno</i> </p>
<p> to skip to the tape block number of interest in a fast way<br/>
 if a single file needs to be restored. </p>
 </dd>
<dt><code>blocks=</code>#, <code>b=</code># </dt>
<dd> <p> Set the blocking factor of the <i>tarfile</i> to #&nbsp;<wbr>times 512 bytes (unless a different multiplication factor has been specified - see <code>bs=</code> option for possible multiplication factors). Changing the blocking factor only makes sense when the archive is located on a real tape device or when the archive is accessed via the remote tape protocol (see <code>f=</code> option below). The default is to use a blocking factor of 20 i.e. 10 kBytes. Increasing the blocksize will speed up the backup. For portability with very old <code>tar</code> implementations (pre BSD 4.2 or pre AT&amp;T SVR4), blocksize should not be more than 10 kBytes. For POSIX.1-1988 compatibility, blocksize should be no more than 10 kBytes. For POSIX.1-2001 compatibility, blocksize should be no more than 32 kBytes. Most systems also have a hardware limitation for the blocksize, 32 kBytes and 63 kBytes are common limits on many systems. The upper limit in any case is the size of the buffer RAM in the tape drive. Make a test if you want to make sure that the target system will handle the intended blocksize. If you use <code>star</code> for data exchange via tape, it is a good idea to use a blocksize of 10 kBytes unless you are sure that the reading system will handle a larger blocksize. If you use <code>star</code> for backup purposes with recent hardware (e.g. DLT tape drives), a blocksize of 256 kBytes results in sufficient speed and seems to be a good choice. <code>Star</code> allows block sizes up to 2 GByte if the system does not impose a smaller limit. If you want to determine the blocking factor when reading an unknown <code>tar</code> archive on tape, specify a blocking factor that is higher than the supposed blocking factor of the tape. <code>Star </code> then will determine the blocking factor by reading the first record of the tape and print a message: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>star: Blocksize = # records.</code> </p>
 </dd></dl>
<p> Where # is the blocking factor in multiples of 512 bytes. The <i>blocks=</i> option and the <i>bs=</i> option are equivalent methods to specify the tape block size. The <code>blocks= </code> option is preferred by people who like to use an option that behaves similar to the interface of the historic <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) implementations. </dl>
 </p>
<dt><code>bs=</code># </dt>
<dd> <p> Set output block size to #. You may use the same method as in <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1) and <code>sdd</code>(1). The number representing the size is taken in bytes unless otherwise specified. If a number is followed directly by the letter `.&#8216;, `w&#8217;, `b&#8217;, `k&#8217;, `m&#8217;, `g&#8217;, `t&#8217;, or `p&#8217;, the size is multiplied by 1, 2, 512, 1024, 1024*1024, 1024*1024*1024, 1024*1024*1024*1024 or 1024*1024*1024*1024*1024. If the size consists of numbers separated by `x&#8217; or `*&#8216;, multiplication of the two numbers is performed. Thus <i>bs=7x8k</i> will specify a blocksize of 56 kBytes. Blocksize must be a multiple of 512 bytes. See also the description of the <i>blocks=</i> option for more details on blocksizes. The option <code>bs=</code> is preferred by people who like to use an option that behaves similar to the interface used by <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1) and <code>sdd</code>(1). </p>
 </dd>
<dt><code>-bsdchdir</code></dt>
<dd> <p> Switch the behavior of the <code>C=</code> option to BSD style. The default behavior of <code>star</code> is to stay in a working directory until a new <code>C=</code> is seen. With BSD tar, the <code>C=</code> option is only related to the next file type argument. </p>
 </dd>
<dt><code>-bz</code></dt>
<dd> <p> run the input or output through a <code>bzip2</code> pipe - see option <code>-z </code> <code>-Z</code> and <code>-j</code> below. As the <code>-bz</code> the <code>-j</code> the <code>-Z</code> and the <code>-z</code> option are non standard, it makes sense to omit the <code>-bz</code> the <code>-j</code> the <code>-Z</code> and the <code>-z</code> options inside shell scripts if you are going to extract a compressed archive that is located inside a plain file as <code>star</code> will auto detect compression and choose the right decompression option to extract. </p>
 </dd>
<dt><code>C=</code><i>dir</i></dt>
<dd>  </dd>
<dt><code>-C</code><i> dir</i></dt>
<dd> <p> Perform a <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2) operation to <i>dir</i> before storing or extracting the next files. In all cases, <code>star </code> will perform the <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2) operation relative to the current working directory of the shell. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> In list mode (with the <code>-t</code> flag), <code>star</code> ignores all <i>-C</i> options. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> In create mode (with the <code>-c</code>, <code>-r</code> and <code>-u</code> flag), <code>star</code> walks through all <i>-C</i> options and file type arguments. While a BSD derived <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) implementation goes back to the current working directory after storing one file argument that immediately follows the <i>-C</i> option, <code>star</code> changes the directory only if a new <code>-C</code> option follows. To emulate the behavior of a BSD derived <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), add a <code>-C</code><i> .</i> option after the file argument. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> In extract mode (with the <code>-x</code>, <code>-n</code> and <code>-diff</code> flag), <code>star</code> builds a pattern list together with corresponding directories from previous <code>C=</code><i>dir</i> options and performs a <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2) to the corresponding directory of a matching pattern. All <code>pat=</code> options that do not follow a <code>C=</code><i>dir</i> option are interpreted as if they were preceded by a <code>-C</code><i> .</i> option. See EXAMPLES for more information. </p>
 </dd></dl>
</dl>
<dt><code>compress-program=</code><i>name</i></dt>
<dd> <p> Set a named compress program. The program must compress in a pipe when called without parameters and decompress when run with the <code>-d</code> option in a pipe. This option is otherwise similar to the <code>-z</code> the <code>-j</code> the <code>-Z</code> and the <code>-bz</code> option. </p>
 </dd>
<dt><code>-copydlinks</code></dt>
<dd> <p> Try to recursively copy the content of linked directories instead of creating the link. This is an experimental feature that may help to unpack archives on DOS. </p>
 </dd>
<dt><code>-copyhardlinks</code></dt>
<dd> <p> This option allows to copy hardlinked targets rather than creating the link. It helps to extract <code>tar</code> files on systems that do not implement hardlinks (e.g. BeOS). </p>
 </dd>
<dt><code>-copylinks</code></dt>
<dd> <p> This option allows to copy both, hard- and symlinked targets rather than creating a link. It helps to extract <code>tar</code> files on systems that do not implement links (e.g. OS/2). To extract and copy all symlinks correctly, you may need to call <code>star</code> twice as <code>star</code> cannot copy files that appear in the archive later than a symlink pointing to them. </p>
 </dd>
<dt><code>-copysymlinks</code></dt>
<dd> <p> This option allows to copy symlinked targets rather than creating a symbolic link. It helps to extract <code>tar</code> files on systems that do not implement links (e.g. OS/2). To extract and copy all symlinks correctly, you may need to call <code>star</code> twice as <code>star</code> cannot copy files that appear in the archive later than a symlink pointing to them. </p>
 </dd>
<dt><code>-cpio-statistics</code></dt>
<dd> <p> Instead of the <code>star </code> flavor of the statistics, print statistics in <code>cpio</code> flavor. </p>
 </dd>
<dt><code>-ctime</code></dt>
<dd> <p> If used with the list command, this lists <i>ctime </i> rather than <i>mtime</i> if the archive format is <code>star</code>, <code>xstar</code>, <code>xustar</code>, <code>exustar</code>, or <code>pax</code>. </p>
<p> If star is run as root and if <code>-ctime </code> is used with the extract command and the same archive formats, this causes <code>star</code> to try to restore even the <i>ctime </i> of a file by generating time storms. You should not do this when in multi user mode because this may confuse programs like cron and the news system. Although <code>star</code> tries to eliminate the accumulative effects of the time storm, there is a tendency for the system clock to slow down a bit. The clock typically lags about one millisecond per extracted file. Use with care and check the system clock after using this feature. </p>
<p> If used with the create command this changes the behavior of the <i>newer=</i> option. <code>Star</code>, in this case compares the <i>ctime</i> of all files to the <i>mtime</i> of the stamp file rather then comparing the <i>mtimes</i> of both files. </p>
 </dd>
<dt><code>-cumulative</code></dt>
<dd> <p> A shorthand for <code>-dump-cumulative</code>. See <code>-dump-cumulative</code> for more information. </p>
 </dd>
<dt><code>-D</code></dt>
<dd> <p> Do not descend directories when in create mode. Normally, <code>star </code> descends the whole tree if it encounters a directory in in its file parameters. The option <code>-D</code> is in effect by default if the <code>list=</code><i>file</i> option is used. If you like <code>star</code> to descend directories found in the list file, use the <code>-dodesc</code> option (see below). </p>
 </dd>
<dt><code>-d</code></dt>
<dd> <p> Do not store/create directories. Old versions of <code>tar </code> such as published with the seventh edition of UNIX are not able to deal with directories in <code>tar</code> archives. If a <code>tar</code> archive is generated without directories this avoids problems with <code>tar</code> implementations found on SYSVr3 and earlier. If used during extract, no intermediate missing directories are created. </p>
 </dd>
<dt><code>-data-change-warn</code></dt>
<dd> <p> If the size of a file changes while the file is being archived, treat this condition as a warning only that does not cause a non zero exit code. A warning message is still written if the condition is not otherwise ignored by another rule from an <code>errctl=</code> option. The <code>-data-change-warn</code> option works as if the last error control option was </p>
<p> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>errctl=</code><i>&quot;WARN|GROW|SHRINK <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>*&quot;</i><br/>
 </p>
<p> The <code>-e</code> option or an <code>ABORT</code> entry in a condition set up by <code>errctl=</code> has a higher precedence than the <code>-data-change-warn</code> option. This option is ignored in extract or list mode. </p>
 </dd>
<dt><code>-debug</code></dt>
<dd> <p> Print debug messages. Among other things, this gives debug messages for header type recognition, <code>tar</code> type properties, EOF recognition, opening of remote archives and fifo internals. </p>
 </dd>
<dt><code>diffopts=</code><i>optlst</i></dt>
<dd> <p> Comma separated list of diffopts. Valid members in <i>optlst</i> are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>help</code></dt>
<dd> <p> Print a summary of possible members of the diffopts list. </p>
 </dd>
<dt><code>!</code></dt>
<dd> <p> Invert the meaning of the following string. No comma is needed after the exclamation mark. </p>
 </dd>
<dt><code>not</code></dt>
<dd> <p> Invert the meaning of all members in the diffopts list i.e. exclude all present options from an initially complete set compare list. When using <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1) you might have problems to use <code>!</code> due to its strange parser. This is why the <code>not</code> alias exists. </p>
 </dd>
<dt><code>perm</code></dt>
<dd> <p> Compare file permissions. With this option in effect, <code>star </code> compares the low order 12 bits of the st_mode field. </p>
 </dd>
<dt><code>mode</code></dt>
<dd> <p> Same as <i>perm.</i> </p>
 </dd>
<dt><code>symperm</code></dt>
<dd> <p> Compare permissions even in case the target file on the local filesystem is a symbolic link. By default, <code>star</code> will not compare the permission of symbolic links as most systems cannot set the permission of symbolic links. <code>Star</code> compares <code>symperm</code> only if <code>perm</code> is compared also. </p>
 </dd>
<dt><code>type</code></dt>
<dd> <p> Compare file type. Note that <code>star</code> cannot compare the file type in case of a hard link. </p>
 </dd>
<dt><code>nlink</code></dt>
<dd> <p> Compare link count on hardlinks. This only works if the archive is in <code>exustar</code> format and contains <code>star&#8217;s</code> dump extensions. </p>
 </dd>
<dt><code>uid</code></dt>
<dd> <p> Compare numerical user id of file. </p>
 </dd>
<dt><code>gid</code></dt>
<dd> <p> Compare numerical group id of file. </p>
 </dd>
<dt><code>uname</code></dt>
<dd> <p> Compare ASCII version of user id of file. The user name is mapped via the file /etc/passwd. </p>
 </dd>
<dt><code>gname</code></dt>
<dd> <p> Compare ASCII version of group id of file. The group name is mapped via the file /etc/group. </p>
 </dd>
<dt><code>id</code></dt>
<dd> <p> Shorthand for: <i>uid,gid,uname,gname</i>. Compare all user/group related info of file. Note that this will always find differences if the source and target system use different user or group mappings. </p>
 </dd>
<dt><code>size</code></dt>
<dd> <p> Compare file size. Note that <code>star</code> cannot compare the file size in case of a hard link. </p>
 </dd>
<dt><code>data</code></dt>
<dd> <p> Compare content of file. If <code>star</code> already found that the size of the files differ, it will not compare the content anymore. If the size of the files differ, <code>star</code> will always report different data. </p>
 </dd>
<dt><code>cont</code></dt>
<dd> <p> Same as <i>data.</i> </p>
 </dd>
<dt><code>rdev</code></dt>
<dd> <p> Compare major/minor numbers for device nodes. </p>
 </dd>
<dt><code>hardlink</code></dt>
<dd> <p> Compare target of hardlinks. </p>
 </dd>
<dt><code>symlink</code></dt>
<dd> <p> Compare target of symlinks. This evaluates the paths returned by the <a href="/docs/linux/man/2-readlink/">readlink</a>(2) call. </p>
<p> Two symlinks are considered equal, it they either have a characterwise identical link-name, or if they either both use an absolute path name or both use a relative path name and the following is true: Both symlinks point to the same file that must exist or both pathnames look similar enough. </p>
 </dd>
<dt><code>sympath</code></dt>
<dd> <p> Compare the target pathnames of symlinks. This characterwise compares the strings returned from the <a href="/docs/linux/man/2-readlink/">readlink</a>(2) call. </p>
 </dd>
<dt><code>sparse</code></dt>
<dd> <p> Compare if either both files are sparse or not. If only one of both files is sparse, then a difference is flagged. This only works with if the archive format is <code>star</code>, <code>xstar</code>, <code>xustar</code>, <code>exustar</code>, or <code>gnutar</code>. </p>
 </dd>
<dt><code>atime</code></dt>
<dd> <p> Compare access time of file. This only works with if the archive format is <code>star</code>, <code>xstar</code>, <code>xustar</code>, <code>exustar</code>, or <code>pax</code>. </p>
 </dd>
<dt><code>mtime</code></dt>
<dd> <p> Compare modification time of file. </p>
 </dd>
<dt><code>ctime</code></dt>
<dd> <p> This only works with if the archive format is <code>star</code>, <code>xstar</code>, <code>xustar</code>, <code>exustar</code>, or <code>pax</code>. </p>
 </dd>
<dt><code>lmtime</code></dt>
<dd> <p> Compare the modification time even in case the target file on the local filesystem is a symbolic link. By default, <code>star</code> will not compare the modification time of symbolic links as most systems cannot set the modification time of symbolic links. <code>Star</code> compares <code>lmtime</code> only if <code>mtime</code> is compared also. </p>
 </dd>
<dt><code>times</code></dt>
<dd> <p> Shorthand for: <i>atime,mtime,ctime</i>. </p>
 </dd>
<dt><code>dir</code></dt>
<dd> <p> Compare the content of directories. This only works if the archive is in <code>exustar</code> format and contains <code>star&#8217;s</code> dump extensions. Together with increased verbose level (<code>-vv</code>) this will print a list of files that are only in the archive and a list of files that are only on the current filesystem. </p>
 </dd>
<dt><code>xtimes</code></dt>
<dd> <p> Shorthand for: <i>atime,mtime,ctime,lmtime</i>. </p>
 </dd>
<dt><code>acl</code></dt>
<dd> <p> Compare access control lists. This only works if the archive is in <code>exustar</code> format and has been created with <code>star&#8217;s</code> <code>-acl</code> option. You need to specify the <code>-acl</code> option in addition when running the diff. </p>
 </dd>
<dt><code>xattr</code></dt>
<dd> <p> Compare extended file attributes. This only works if the archive is in <code>exustar</code> format and has been created with <code>star&#8217;s</code> <code>-xattr</code> option. You need to specify the <code>-xattr</code> option in addition when running the diff. </p>
 </dd>
<dt><code>fflags</code></dt>
<dd> <p> Compare extended file flags. This only works if the archive is in <code>exustar</code> format and has been created with <code>star&#8217;s</code> <code>-xfflags</code> option. You need to specify the <code>-xfflags</code> option in addition when running the diff. </p>
 </dd></dl>
<p> If <i>optlst</i> starts with a ! the meaning of all members in <i>optlst</i> is inverted as with the <i>not</i> optlist member. In this case, <code>star</code> starts with a complete list that includes <code>atime</code> and <code>lmtime</code>. Reasonable diff options to use when comparing against a copy of a directory tree are <code>diffopts=!atime,ctime,lmtime</code>. </p>
<p> If <i>diffopts</i> are not specified, <code>star </code> compares everything but the access time of the files and the modification time of symbolic links. </dl>
 </p>
<dt><code>dir-group=</code><i>group</i></dt>
<dd> <p> If <code>star</code> extracts archives as root, this option allows to control the group id of intermediate directories created by <code>star</code>. </p>
 </dd>
<dt><code>dir-owner=</code><i>user</i></dt>
<dd> <p> If <code>star</code> extracts archives as root, this option allows to control the owner of intermediate directories created by </p>
 </dd>
<dt><code>-dirmode</code></dt>
<dd> <p> If in create mode (i.e. when storing files to archive), <code>star </code> stores directories past the corresponding files. This guarantees that even old <code>tar</code> implementations without a directory cache will be able to restore the correct times of directories. The option <code>-dirmode</code> should only be used if the archive needs to be extracted by an old <code>tar</code> implementation. If <code>star</code> is used to extract an archive that has been created with <code>-dirmode</code> the directories will not get an old time stamp unless the option <code>-U</code> is used while extracting the archive. </p>
 </dd>
<dt><code>-dodesc</code></dt>
<dd> <p> Force <code>star</code> to descend directories found in a <code>list=</code><i>file.</i> See also the <code>-D</code> option above. The <code>-dodesc</code> option only works in create mode. </p>
 </dd>
<dt><code>-dump</code></dt>
<dd> <p> Allows to create archives with the same number of attributes as an archive that has been created with the <code>level=</code> option but without the restrictions that apply to a true dump. </p>
<p> The resultant archive may be seen as a <i>level-less</i> dump which includes similar attributes as a level 0 dump but may span more than a single file system and does not need to use a <code>-C</code> option. It has been originally introduced to make it easier to implement a <code>star</code> version that supports <i>true incremental dumps</i>, but it is kept as it gives additional benefits. <code>Star</code> currently sets the archive type to <code>exustar</code> and, in addition archives more inode meta data inside POSIX.1-2001 extended headers. See also <code>level=</code> option and the section <code>INCREMENTAL BACKUPS</code> for more information on <i>true incremental dumps</i>. </p>
 </dd>
<dt><code>-dump-cumulative</code></dt>
<dd> <p> instructs <code>star</code> to perform incremental dumps relatively to the last incremental dump of the same level. Incremental dumps with a level higher than 0 are normally done relatively to the content of a previous dump with lower level. If incremental dumps and restores are going to be used to synchronize filesystem content, every successive incremental dump will increase in size if <code>-dump-cumulative</code> is not used. See section <code>SYNCHRONIZING FILESYSTEMS</code> for more information. </p>
 </dd>
<dt><code>dumpdate=</code><i>name</i></dt>
<dd> <p> Tells <code>star</code> to use the <code>mtime</code> of the time stamp file <i>name</i> instead of using the start time of <code>star</code>. This is needed when <code>star</code> is run on file system snapshots. If <code>star</code> would use the the start time with snapshots, all files that have been modified between the setup of the snapshot and the start of <code>star</code> would be missing on the backup. </p>
 </dd>
<dt><code>-dumpmeta</code></dt>
<dd> <p> changes the behavior of <code>star</code> in incremental dump mode. If <code>-dumpmeta</code> is used and only the inode change time (st_ctime) of a file has been updated since the last incremental dump, <code>star</code> will archive only the <code>meta</code> data of the file (e.g. uid, permissions, ...) but not the file content. Using <code>-dumpmeta</code> will result in smaller incremental dumps, but files that have been created between two incrementals and set to an old date in st_mtime (e.g. as a result from a tar extract) will not be archived with full content. Using <code>-dumpmeta</code> thus may result in incomplete incremental dumps, use with extreme care. </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> Exit immediately with exit status -3 (253) if any unexpected error occurs. The <code>-e</code> option works as if the last error control option was </p>
<p> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>errctl=</code><i>&quot;ABORT|ALL|DIFF <code>&nbsp;<wbr>&nbsp;<wbr></code>*&quot;</i><br/>
 </p>
<p> This allows to use the <code>errctl=</code> option together with the <code>-e</code> option and thus to ignore some error conditions while aborting on all other conditions. </p>
 </dd>
<dt><code>errctl=</code><i> name</i></dt>
<dd>  </dd>
<dt><code>errctl=</code><i> error control spec</i></dt>
<dd> <p> Add the content from file <i>name</i> to the error control definitions or add <i>error control spec</i> to the error control definitions. More than one error control file and more than one <i>error control spec</i> as well as a mixture of both forms is possible. </p>
<p> The reason for using error control is to make <code>star</code> quiet about error conditions that are known to be irrelevant on the quality of the archive or restore run or to tell <code>star </code> to abort on certain error conditions instead of trying to continue with the archive. </p>
<p> A typical reason to use error control is to suppress warnings about growing log files while doing a backup on a live file system. Another typical reason to use error control is to tell <code>star</code> to abort if e.g. a file could not be archived instead of continuing to archive other files from a list. </p>
<p> The error control file contains a set of lines, each starting with a list of error conditions to be ignored followed by white space followed by a file name pattern (see <code>match</code>(1) or <code>patmatch</code>(3) for more information). The <i>error control spec</i> uses the same syntax as a single line from the error control file. If the file name pattern needs to start with white space, use a backslash to escape the start of the file name. It is not possible to have new line characters in the file name pattern. Whenever an error situation is encountered, <code>star</code> checks the lines in the error control file starting from the top. If the current error condition is listed on a line in the error control file, then <code>star</code> checks whether the pattern on the rest of the line matches the current file name. If this is the case, <code>star</code> uses the current error control specification to control the current error condition. </p>
<p> The list of error conditions to be handled may use one or more (in this case separated by a &#8216;|&#8216; character) identifiers from the list below: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>ABORT</code></dt>
<dd> <p> If this meta condition is included in an error condition, <code>star</code> aborts (exits) as soon as possible after this error condition has been seen instead of making <code>star</code> quiet about the condition. This error condition flag may only be used together with at another error condition or a list of error conditions (separated by a &#8216;|&#8216; character). </p>
 </dd>
<dt><code>WARN</code></dt>
<dd> <p> If this meta condition is included in an error condition, <code>star</code> prints the warning about the error condition but the error condition does not affect the exit code of <code>star</code> and the error statistics (which is printed to the end) does not include the related errors. This error condition flag may only be used together with at another error condition or a list of error conditions (separated by a &#8216;|&#8216; character). The <code>WARN</code> meta condition has a lower precedence than <code>ABORT</code>. </p>
 </dd>
<dt><code>DIFF</code></dt>
<dd> <p> Suppress output in case that <code>star -diff</code> did encounter any differences. </p>
 </dd>
<dt><code>ALL</code></dt>
<dd> <p> This is a shortcut for all error conditions below. </p>
 </dd>
<dt><code>STAT</code></dt>
<dd> <p> Suppress warnings that <code>star </code> could not <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) a file. </p>
 </dd>
<dt><code>GETACL</code></dt>
<dd> <p> Suppress warnings about files on which <code>star</code> had problems to retrieve the ACL information. </p>
 </dd>
<dt><code>OPEN</code></dt>
<dd> <p> Suppress warnings about files that could not be opened. </p>
 </dd>
<dt><code>READ</code></dt>
<dd> <p> Suppress warnings read errors on files. </p>
 </dd>
<dt><code>WRITE</code></dt>
<dd> <p> Suppress warnings write errors on files. </p>
 </dd>
<dt><code>READLINK</code></dt>
<dd> <p> Suppress warnings <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2) errors on symbolic links. </p>
 </dd>
<dt><code>GROW</code></dt>
<dd> <p> Suppress warnings about files that did grow while they have been archived. </p>
 </dd>
<dt><code>SHRINK</code></dt>
<dd> <p> Suppress warnings about files that did shrink while they have been archived. </p>
 </dd>
<dt><code>MISSLINK</code></dt>
<dd> <p> Suppress warnings about files for which <code>star</code> was unable to archive all hard links. </p>
 </dd>
<dt><code>NAMETOOLONG</code></dt>
<dd> <p> Suppress warnings about files that could not be archived because the name of the file is too long for the archive format. </p>
 </dd>
<dt><code>FILETOOBIG</code></dt>
<dd> <p> Suppress warnings about files that could not be archived because the size of the file is too big for the archive format. </p>
 </dd>
<dt><code>SPECIALFILE</code></dt>
<dd> <p> Suppress warnings about files that could not be archived because the file type is not supported by the archive format. </p>
 </dd>
<dt><code>GETXATTR</code></dt>
<dd> <p> Suppress warnings about files on that <code>star</code> could not retrieve the extended file attribute information. </p>
 </dd>
<dt><code>SETTIME</code></dt>
<dd> <p> Suppress warnings about files on that <code>star</code> could not set the time information during extraction. </p>
 </dd>
<dt><code>SETMODE</code></dt>
<dd> <p> Suppress warnings about files on that <code>star</code> could not set the access modes during extraction. </p>
 </dd>
<dt><code>SECURITY</code></dt>
<dd> <p> Suppress warnings about files that have been skipped on extraction because they have been considered to be a security risk. This currently applies to all files that have a &#8216;/../&#8216; sequence inside when <code>-..</code> has not been specified. </p>
 </dd>
<dt><code>LSECURITY</code></dt>
<dd> <p> Suppress warnings about links that have been skipped on extraction because they have been considered to be a security risk. This currently applies to all link names that start with &#8216;/&#8216; or have a &#8216;/../&#8216; sequence inside when <code>-secure-links</code> has been specified. In this case, <code>star </code> tries to match the link name against the pattern in the error control file. </p>
 </dd>
<dt><code>SAMEFILE</code></dt>
<dd> <p> Suppress warnings about links that have been skipped on extraction because source and target of the link are pointing to the same file. If <code>star</code> would not skip these files, it would end up with removing the file completely. In this case, <code>star </code> tries to match the link name against the pattern in the error control file. </p>
 </dd>
<dt><code>BADACL</code></dt>
<dd> <p> Suppress warnings access control list conversion problems. </p>
 </dd>
<dt><code>SETACL</code></dt>
<dd> <p> Suppress warnings about files on that <code>star</code> could not set the ACL information during extraction. </p>
 </dd>
<dt><code>SETXATTR</code></dt>
<dd> <p> Suppress warnings about files on that <code>star</code> could not set the extended file attribute information during extraction. </p>
 </dd></dl>
</dl>
<p> If a specific error condition is ignored, then the error condition is not only handled in a silent way but also excluded from the error statistics that are printed at the end of the <code>star</code> run. </p>
<p> Be very careful when using error control as you may ignore any error condition. If you ignore the wrong error conditions, you may not be able to see real problems anymore. </p>
<dt><code>-exclude-from</code><i> name</i></dt>
<dd> <p> Exclude from named file, this is an alias for the <code>-X</code> option. See <code>-X</code> option for more information. </p>
 </dd>
<dt><code>-F</code>,<code>-FF</code> ... </dt>
<dd> <p> Fast and simple exclude option for create mode. With one <code>-F</code> argument, <code>star</code> ignores all directories called <i>SCCS</i> and <i>RCS.</i> With two <code>-F</code> arguments, <code>star</code> in addition ignores all files called <i>core errs a.out</i> all files ending with <i>.o</i>. <i>OBJ/</i>. With three <code>-F</code> arguments, <code>star</code> ignores all sub trees starting from a directory that includes a file <i>.mirror</i> or <i>.exclude</i> and all object files and files called <i>core errs a.out</i> all files ending with <i>.o</i>. With four <code>-F</code> arguments, <code>star</code> ignores all sub trees starting from a directory that includes a file <i>.mirror</i> or <i>.exclude</i> the latter files are excluded too as well as and all object files and files called <i>core errs a.out</i> all files ending with <i>.o</i>. With five <code>-F</code> arguments, <code>star</code> in addition again excludes all directories called <i>SCCS</i> and <i>RCS.</i> </p>
 </dd>
<dt><code>-fifo</code></dt>
<dd> <p> Use a <i>fifo</i> to optimize data flow from/to <i>tarfile.</i> This option is in effect by default (it may be changed at compile time). The default fifo size is 8 MBytes on all platforms except Linux versions that do not support mmap() (4 MB because kernels before 2.4 did not handle big shared memory areas) and Sun/mc68000 (1 MB). This will <code>star</code> make even work on a tiny machine like a Sun 3/50. The fifo size may be modified with the <i>fs=</i> option. A rule of dumb for the fifo size is to use more than the buffer size of the tape drive and less then half of the real memory of the machine. A good choice would be to use a fifo size between 8 and 256 MB. This may increase backup speed up to 5% compared to the speed achieved with the default fifo size. Note that with a DLT drive that gives 12MB/s transfer rate, a fifo of 256 MB size will keep the tape at least streaming in units of 20 seconds. All options that start with the <code>-f</code> sequence are sensitive to typo problems, see BUGS section for more information. </p>
 </dd>
<dt><code>-fifostats</code></dt>
<dd> <p> Print fifo statistics at the end of a <code>star</code> run when the fifo has been in effect. All options that start with the <code>-f</code> sequence are sensitive to typo problems, see BUGS section for more information. </p>
 </dd>
<dt><code>file=</code>tarfilename, <code>f=</code>tarfilename </dt>
<dd> <p> Use <i>tarfilename </i> as the name for the <code>tar</code> archive. Currently up to 100 <code>file=</code> options are possible. Specifying more then one <code>file= </code> option make sense in multi volume mode. In this case <code>star</code> will use the next name in the list every time a media change is needed. To make <code>star </code> behave consistent with the single file case, <code>star</code> loops over the list of known archive files. Note that if <code>star</code> is installed suid root and the first tarfile is a remote archive, only the connection to this archive will be created with root privileges. After this connection has been established as root, <code>star</code> switches back to the id of the caller. If any of the other archives in the list is located on a different host, <code>star</code> will not be able to open this archive later on, unless run by root. </p>
<p> <code>Star</code> normally uses <i>stdin</i>/<i>stdout</i> for the <code>tar</code> archive because the most common way to use <code>star</code> is in conjunction with pipes. If <code>star</code> is installed suid root or if it has been called by root, <i>tarfilename</i> may be in remote syntax: user [at] host:filename as in <code><a href="/docs/linux/man/1-rcp/">rcp</a></code>(1) even if invoked by non root users. See SUID NOTES for more information. </p>
<p> To make a file local although it includes a colon (:), the filename must start with: <i>&#8216;/&#8216;</i>, <i>&#8216;./&#8216;</i> or <i>&#8216;../&#8216;</i> </p>
<p> Note that if <code>star </code> talks to an old <code>rmt</code> remote tape server that does not support symbolic open modes, it does not open a remote tape with the <code>O_CREAT</code> open flag because this would be extremely dangerous. If the <code>rmt </code> server on the other side is the <code>rmt</code> server that comes with <code>star</code> or the GNU <code>rmt</code> server, <code>star</code> may use the symbolic mode for the open flags. Only the symbolic open modes allow to send all possible open modes in a portable way to remote tape servers. </p>
<p> It is recommended to use the <code>rmt</code> server that comes with <code>star</code>. It is the only <code>rmt</code> server that gives platform independent compatibility with BSD, Sun and GNU <code>rmt </code> clients and it includes security features that may be set up in /etc/default/rmt. All options that start with the <code>-f</code> sequence are sensitive to typo problems, see BUGS section for more information. </p>
<p> See ENVIRONMENT section for information on how to use <code><a href="/docs/linux/man/1-ssh/">ssh</a>(1)</code> to create a remote tape server connection. </p>
<p> Note that if <code>file=</code><i>-</i> has been specified, it is no longer possible to use the <code>-find</code> <code>-exec</code> primary. </p>
 </dd>
<dt><code>-find</code></dt>
<dd> <p> This option acts a separator. If it is used, all <code>star</code> options must be to the left of the <code>-find</code> option. To the right of the <code>-find</code> option, <code>star</code> accepts the <code>find</code> command line syntax only. </p>
<p> The <code>find</code> expression acts as a filter between the source of file names and the consumer, which may either be the archiving engine or list/extract engine. If the <code>find</code> expression evaluated as TRUE, then the related file is selected for processing, otherwise it is omited. </p>
<p> In order to make the evaluation of the <code>find</code> expression more convenient, <code>star</code> implements additional <code>find primaries</code> that have side effects on the file meta data. <code>Star</code> implements the following additional <code>find</code> primaries: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-chgrp</code><i> gname</i></dt>
<dd> <p> The primary always evaluates as true; it sets the group of the file to <i>gname</i>. </p>
 </dd>
<dt><code>-chmod</code><i> mode</i></dt>
<dd> <p> The primary always evaluates as true; it sets the permissions of the file to <i>mode</i>. Octal and symbolic permissions are accepted for <i>mode</i> as with <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1). </p>
 </dd>
<dt><code>-chown</code><i> uname</i></dt>
<dd> <p> The primary always evaluates as true; it sets the owner of the file to <i>uname</i>. </p>
 </dd>
<dt><code>-false</code></dt>
<dd> <p> The primary always evaluates as false; it allows to make the result of the full expression different from the result of a part of the expression. </p>
 </dd>
<dt><code>-true</code></dt>
<dd> <p> The primary always evaluates as true; it allows to make the result of the full expression different from the result of a part of the expression. </p>
 </dd></dl>
<p> The command line: </p>
<p> <code>star -c f=o.tar -find . ( -type d -ls -o false ) -o ! -type d</code> </p>
<p> lists all directories and archives all non-directories to the archive <code>o.tar</code>. </p>
<p> The command line: </p>
<p> <code>star -c f=o.tar -find . ( -type d -chown root -o true )</code> </p>
<p> archives all directories so they appear to be owned by root in the archive, all non-directories are archived as they are in the file system. </p>
<p> Note that the <code>-ls</code>, <code>-exec </code> and the <code>-ok</code> primary cannot be used if <code>stdin </code> or stdout has been redirected by the <code>list=</code><i>-</i> of by the <code>file=</code><i>-</i> options. </dl>
 </p>
<dt><code>-force_hole</code></dt>
<dd> <p> obsoleted by -force-hole </p>
 </dd>
<dt><code>-force-hole</code></dt>
<dd> <p> Try to extract all files with holes. This even works with files that are created without the <code>-sparse </code> option. <code>Star</code>, in this case examines the content of the files in the archive and replaces writes to parts containing binary zeroes with seeks. </p>
<p> If used together with the <code>-sparse</code> option in create mode, <code>star</code> assumes all files to be sparse and archives files with blocks of nulls as sparse files. </p>
<p> This option should be used with extreme care because you sometimes get in trouble when files get unattended holes. All options that start with the <code>-f</code> sequence are sensitive to typo problems, see BUGS section for more information. </p>
 </dd>
<dt><code>-force_remove</code></dt>
<dd> <p> obsoleted by -force-remove </p>
 </dd>
<dt><code>-force-remove</code></dt>
<dd> <p> Force to remove non writable files on extraction. By default, <code>star</code> will not overwrite files that are read only. If this option is in effect, <code>star</code> will silently remove these files to allow the extraction of a file. All options that start with the <code>-f</code> sequence are sensitive to typo problems, see BUGS section for more information. </p>
 </dd>
<dt><code>-force-restore</code></dt>
<dd> <p> Force an incremental restore even if the incremental dump is only a partial dump. See <code>-wtardumps</code>, <code>level=</code> and section <code>INCREMENTAL BACKUPS</code> for more information. </p>
 </dd>
<dt><code>fs=</code># </dt>
<dd> <p> Set fifo size to #. See <i>bs=</i> for the possible syntax. The default size of the fifo is 1 Mbyte on Sun mc68000 systems, 4 Mbytes on non mmap() aware Linux systems and 8 Mbytes on all other systems. See <code>-fifo</code> option for hints on using the right fifo size. </p>
 </dd>
<dt><code>fs-name=</code><i>mount_point</i></dt>
<dd> <p> Use <i>mount_point</i> when recording information in <code>/etc/tardumps</code> and when comparing against information in <code>/etc/tardumps</code> for incremental backups. This makes sense when backups are made using file system snapshots and allows <code>/etc/tardumps</code> and the archive to contain the real name of the file system instead of the temporary mount point that is used for the snapshot device. </p>
 </dd>
<dt><code>H=</code><i>headertype</i></dt>
<dd> <p> See <code>artype=</code><i>headertype</i> option. Note that POSIX.1-2001 defines an option <code>-H</code> that follows symbolic links that have been encountered on the command line. For this reason, the old star option <code>H=</code><i>headertype</i> option may go away in the future even though this option has been in use by cpio since 1989. </p>
 </dd>
<dt><code>-h, -L</code></dt>
<dd> <p> Follow symbolic links as if they were files. Normally <code>star</code> will not follow symbolic links but stores their values in <i>tarfile.</i> See also the <code>-L</code> option. </p>
 </dd>
<dt><code>-hardlinks</code></dt>
<dd> <p> In extract mode, this option tells <code>star</code> to try to create a hardlink whenever a symlink is encountered in the archive. In create mode, this option tells <code>star</code> to try to archive a hardlink whenever a symlink is encountered in the file system. </p>
 </dd>
<dt><code>-hpdev</code></dt>
<dd> <p> Allow 24 bits for the minor device number using 8 octal digits. Note that although it allows to create <code>tar</code> archives that can be read with HP-UX tar, this creates <code>tar</code> archives which violate POSIX.1-1988. This option is only needed if you like to use a POSIX.1-1988 based archive format that does not include extensions. If you use the <code>xstar</code> format, <code>star</code> will use a base 256 extension that allows bigger major/minor numbers by default, if you use the <code>xustar </code> or the <code>exustar</code> format there is no limitation at all as these formats use POSIX.1-2001 extended headers to archive the major/minor numbers by default. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> Ignore checksum errors on <code>tar</code> headers. If this option is specified, <code>star</code> will not exit if a header with a bad checksum is found but search for the next valid header. </p>
 </dd>
<dt><code>-install</code></dt>
<dd> <p> Carefully replace existing files when extracting files. This is done similar to <code><a href="/docs/linux/man/1-install/">install</a></code>(1) by first extracting the files into a temporary name and renaming the file to the final name after the extraction of that file was successful. </p>
<p> As <code>star</code> by default does not remove non-empty directories, an install that needs to remove existing non-empty directories may also need the options <code>-force-remove</code> and <code>-remove-recursive</code>. </p>
 </dd>
<dt><code>-j</code></dt>
<dd> <p> run the input or output through a <code>bzip2</code> pipe - see option <code>-z </code> <code>-Z</code> and <code>-bz</code> below. As the <code>-bz</code> the <code>-j</code> the <code>-Z</code> and the <code>-z</code> option are non standard, it makes sense to omit the <code>-bz</code> the <code>-j</code> the <code>-Z</code> and the <code>-z</code> options inside shell scripts if you are going to extract a compressed archive that is located inside a plain file as <code>star</code> will auto detect compression and choose the right decompression option to extract. </p>
 </dd>
<dt><code>-keep-nonempty-dirs</code></dt>
<dd> <p> Do not complain about trying to remove nonempty directories in case that <code>-remove-recursive</code> has not been specified. </p>
 </dd>
<dt><code>-keep_old_files</code></dt>
<dd> <p> obsoleted by -keep-old-files </p>
 </dd>
<dt><code>-keep-old-files</code>, <code>-k</code></dt>
<dd> <p> Keep existing files rather than restoring them from <i>tarfile. </i> This saves files from being clobbered even if <i>tarfile</i> contains a more recent version of the corresponding file. </p>
<p> See SECURITY NOTES for more information. </p>
 </dd>
<dt><code>-L, -h</code></dt>
<dd> <p> Follow symbolic links as if they were files. Normally <code>star</code> will not follow symbolic links but stores their values in <i>tarfile.</i> See also the <code>-h</code> option. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Do not print a warning message if not all links to hard linked files could be dumped. This option is evaluated in the opposite way to historic <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) implementations and to POSIX.1. POSIX.1 requests that by default no warning messages will be printed and <code>-l</code> will enable warning messages when not all links could be archived. </p>
 </dd>
<dt><code>level=</code>dumplevel </dt>
<dd> <p> Set level for incremental dumps. This option is used to switch <code>star</code> into <i>true incremental dump</i> mode. The <code>dumplevel</code> may be in the range between 0..99. </p>
<p> In <i>true incremental dump</i> mode, a <code>-C</code> option which is followed by the name a mount point and a dot (&#8216;.&#8216;) as starting directory name is required. Only a single file system may be handled at a time. If the directory following the <code>-C</code> option is not referring to a root directory of a file system, the dump is called a <code>partial dump</code>. If the directory following the <code>-C</code> option is referring to a root directory of a file system and no other restrictions apply that exclude certain files from the dump, the dump is called a <code>full dump</code>. </p>
<p> By default, the <code>tardumps</code> database is not written. See also the <code>tardumps=</code><i>name</i> and <code>-wtardumps</code> options and the section <code>INCREMENTAL BACKUPS</code> for more information. </p>
 </dd>
<dt><code>-link-data</code></dt>
<dd> <p> In create mode, include the data for files even if these files are hard links. This feature in create mode is currently only available for the <code>exustar</code> archive format and only in case <code>-sparse</code> has not been specified. </p>
<p> In extract mode, allow <code>star</code> to deal with data in hard linked files even if the standard would not allow this for the used archive format. </p>
 </dd>
<dt><code>-link-dirs</code></dt>
<dd> <p> When in create mode, try to find hard linked directories. Using <code>-link-dirs</code> will force <code>star</code> to keep track of all directories that will go into the archive and thus causes a lot more memory to be allocated than in the default case. </p>
<p> If you like to extract a <code>cpio</code> archive that contains hard linked directories, you also need to specify <code>-link-dirs</code> in extract or diff mode. This is needed because many <code>cpio</code> implementations create buggy archives with respect to hard links. If <code>star</code> would look for hard linked directories in all cases, it would detect many pseudo hard links to directories. Use <code>-link-dirs</code> with care if you extract <code>cpio</code> archives. </p>
<p> Note that not all filesystem allow to create hard links to directories. Also note that even though a non-root user is able detect and archive hard linked directories, all known operating systems require the extraction to be done as root in order to be able to create or remove hard links to directories. For this reason its only recommended to use this option when doing accurate backups and when hard links to directories are expected. </p>
<p> When the option <code>-link-dirs</code> is not used and hard links to directories are present, the appendant sub-tree will appear more than once on the archive and <code>star</code> will print <i>Linkcount below zero</i> warnings for non directory hard links inside the sub-tree. </p>
 </dd>
<dt><code>list=</code>filename </dt>
<dd> <p> Read filenames for store/create/list/diff command from <i>filename.</i> The file <i>filename</i> must contain a list of path names, each on a separate line. This option implies the <code>-D </code> option. To force <code>star</code> to descend directories, use the <code>-dodesc</code> option in this case. See also the <code>-X</code> option. </p>
<p> Note that if <code>list=</code><i>-</i> has been specified, it is no longer possible to use the <code>-find</code> <code>-exec</code> primary. </p>
 </dd>
<dt><code>-lowmem</code></dt>
<dd> <p> Try to run with reduced memory requirements. This causes <code>star</code> to default to 1 MB of FIFO memory. Instead of allocating memory to hold the directory content and reading the directory at once, <code>star</code> reads the directory name by name. This may cause <code>star</code> to close the directory if it rans out of file descriptors because of deeply nested directories. If a directory then does not support <code><a href="/docs/linux/man/3-telldir/">telldir</a>(3)/<a href="/docs/linux/man/3-seekdir/">seekdir</a>(3)</code>, <code>star</code> will fail. <br/>
 </p>
 </dd>
<dt><code>-lzip</code></dt>
<dd> <p> run the input or output through a <code>lzip</code> pipe - see option <code>-z</code> below. </p>
 </dd>
<dt><code>-lzo</code></dt>
<dd> <p> run the input or output through a <code>lzop</code> pipe - see option <code>-z</code> below. </p>
 </dd>
<dt><code>-M</code>, <code>-xdev</code></dt>
<dd> <p> Do not descend mount points. This is useful when doing backups of complete file systems. See NOTES for more information. </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> Do not restore access and modification time. (Access time is only available if <code>star</code> is reading <code>star</code>, <code>xstar</code>, <code>xustar</code>, <code>exustar</code>, or <code>pax</code> archives). If <code>star</code> extracts other archive types, the <code>-m</code> flag only refers to the modification time. </p>
 </dd>
<dt><code>-match-tree</code></dt>
<dd> <p> If in create mode a pattern does not match a directory, and <code>-match-tree</code> has been specified, the whole directory tree is excluded from the archive and from further directory scans. By default, <code>star</code> excludes the directory but still recursively scans the content of this directory as complex patterns could allow files inside the directory tree to match. Using <code>-match-tree</code> allows to efficiently exclude whole trees from scanning. This helps to avoid scannings directory trees that are on remote file systems or contain excessive bad blocks. </p>
 </dd>
<dt><code>maxsize=</code># </dt>
<dd> <p> Do not store files in <i>tarfile</i> if they are bigger than #. See <i>bs=</i> for the possible syntax. By default, the number is multiplied by 1024, so the value counts in units of kBytes. If the size specifier ends with a valid multiplication character (e.g &#8216;.&#8216; for bytes or &#8216;M&#8217; for MB) the specified size is used as specified and not multiplied by 1024. See <code>bs=</code> option for all possible multipliers. </p>
 </dd>
<dt><code>-meta</code></dt>
<dd> <p> In create mode, <code>-meta</code> causes <code>star</code> to archive all <code>meta</code> data of the file (e.g. uid, permissions, ...) but not the file content. In extract mode, it causes <code>star</code> to restore all <code>meta</code> data but not the file content. In addition, in extract mode no plain file, special file or directory will be created. <code>Meta</code> files are needed to support incremental backups. </p>
<p> Warning: Do not try to extract <code>star</code> archives containing <code>meta</code> files using other tar implementations if they are not aware of the <code>meta</code> file extensions of <code>star</code>. <code>Star</code> tries to force all tar implementations that are not standard compliant to abort. <code>Star </code> also tries to make all non POSIX.1-2001 compliant tar implementations unable to find a valid filename. However when other POSIX.1-2001 aware tar implementations come up and don&#8217;t know about <code>meta</code> files, they will destroy files on disk. </p>
<p> The problems result from the only current fallback in the POSIX standard that tells tar implementations to treat all unknown file types as if they were plain files. As <code>meta</code> files are needed for incremental backups, I am looking for people and companies who like to support me to be able to add the <code>meta</code> file concept to the POSIX.1-2005 standard. </p>
 </dd>
<dt><code>-modebits</code></dt>
<dd> <p> This options allows you to create <code>tar</code> archives that include more than 12 bits from st_mode. Note this create <code>tar</code> archives that violate POSIX but some <code>tar</code> implementations insist in reading such nonstandard archives. </p>
 </dd>
<dt><code>-multivol</code></dt>
<dd> <p> Switch to multi volume mode. In multi volume mode, there will be no logical EOF marker written to the end of a single tape. If <code>-multivol</code> is used in read mode, a hard EOF on input (if not preceded by a logical EOF) triggers a medium change operation. </p>
<p> Specifying <code>-multivol</code> tells <code>star</code> to split files across volumes if needed. This way, a virtual archive is created that spans more than one medium. Multi volume mode is needed whenever it is not possible to split the archiving or extracting into several logically independent tasks. This is true for e.g. incremental dump/restore operations where inode numbers need to be traced for the whole task. </p>
<p> When <code>tsize=</code><i>#</i> has been specified, but <code>star </code> is not in multi volume mode, files cannot be split across volumes. </p>
<p> When <code>-multivol</code> has been specified in create mode together with <code>tsize=</code><i>#</i> then a media change is initiated exactly after an amount of <i>tsize</i> data has been written. When <code>-multivol</code> has been specified in create mode and <code>tsize=</code><i>#</i> has not been specified, then the medium change is triggered by a EOT condition from writing the medium. This allows to use media where the size cannot be known in advance (e.g. tapes with build in compression); it does not work if the EOT condition is not returned in sync with the related write operation. For this reason, it is expected that data buffering inside a device driver cannot be used. </p>
<p> Depending on the selected archive format, <code>star</code> writes a volume header at the beginning of a new medium. This medium header allows to verify the correct volume after a change during read back. It is recommended to use the <code>exustar</code> format for best results. In create mode, <code>-multivol</code> is only supported for archives types that allow to write reliable multi volume header information. </p>
<p> See <code>tsize=</code><i>#</i> option for more information. </p>
<p> Note that <code>-multivol</code> is an interactive option that prevents <code>star</code> from being used in non-interactive environments. If you like to use it in a non-interactive environment, you need to specify <code>new-volume-script=</code><i>script</i> in addition in order to automate the media change procedure. </p>
 </dd>
<dt><code>newer=</code>filename </dt>
<dd> <p> Do not store files to <i>tarfile</i> if their modification time is not newer than the modification time of <i>filename.</i> See <code>-ctime</code> option for changing this behavior. </p>
 </dd>
<dt><code>-newest</code></dt>
<dd> <p> In conjunction with the list command this lists you only the newest file in <i>tarfile.</i> </p>
 </dd>
<dt><code>-newest_file</code></dt>
<dd> <p> obsoleted by -newest-file </p>
 </dd>
<dt><code>-newest-file</code></dt>
<dd> <p> In conjunction with the list command this lists you only the newest regular file in <i>tarfile.</i> </p>
 </dd>
<dt><code>new-volume-script=</code><i>script</i></dt>
<dd> <p> Call <i>script</i> at end of each tape if in multi volume mode. If this option is not in effect, <code>star</code> will ask the user to confirm the volume change. The script is called with two parameters. The first parameter is the next volume number and the second parameter is the next archive file name. </p>
 </dd>
<dt><code>-nodump</code></dt>
<dd> <p> If this option is set, <code>star</code> will not dump files that have the <code>nodump</code> flag set. Note that this currently only works on BSD-4.4 derivates and on Linux. On Linux, using this option will cause a performance degradation (the system time increases by 10%) because of the unlucky kernel interface. </p>
 </dd>
<dt><code>-no-dirslash</code></dt>
<dd> <p> Do not add a slash to the end of directory names if writing to an archive. Historic tar archive formats did only allow to specify plain files and hard links. Around 1980, BSD added a feature to specify a directory on tape by adding a slash to the end of the name. POSIX.1-1988 defined the first official tar archive format that had a clean method to specify the type of a directory. As old tar formats need the slash to recognize a directory, <code>-no-dirslash</code> may not be used if archives should be compatible with the old tar format. </p>
 </dd>
<dt><code>-no_fifo</code></dt>
<dd> <p> obsoleted by -no-fifo </p>
 </dd>
<dt><code>-no-fifo</code></dt>
<dd> <p> Don&#8217;t use a <i>fifo</i> to optimize data flow from/to <i>tarfile.</i> Currently the <i>-fifo </i> option is used as default. (This may be changed at compile time.) </p>
 </dd>
<dt><code>-no-fsync</code></dt>
<dd> <p> Do not call <code><a href="/docs/linux/man/2-fsync/">fsync</a>(2)</code> for each file that has been extracted from the archive. Using <code>-no-fsync</code> may speed up extraction on operating systems with slow file I/O (such as Linux), but includes the risk that <code>star</code> may not be able to detect extraction problems that occur after the call to <code><a href="/docs/linux/man/2-close/">close</a></code>(2). A typical cause for such problems is a NFS file system that fills up before the buffer cache is synced or a write error that occurs while the buffer cache is synced. There may be other reasons. Use with extreme care. </p>
 </dd>
<dt><code>-nochown</code>, <code>-o</code></dt>
<dd> <p> Do not restore owner and group of files. This may be used if super user privileges are needed to overwrite existing files but the local ownership of the existing files should not change. </p>
 </dd>
<dt><code>-no-p</code></dt>
<dd> <p> Do not restore files and directories to their original permissions. This option is needed only if <code>star</code> is called by the super user and the permissions should not be restored from the archive. See also the <code>-p</code> option. The <code>-p</code> options has a higher precedence than the <code>-no-p</code> option. </p>
 </dd>
<dt><code>-no_statistics</code></dt>
<dd> <p> obsoleted by -no-statistics </p>
 </dd>
<dt><code>-no-statistics</code></dt>
<dd> <p> Do not print statistic messages at the end of a <code>star</code> run. </p>
 </dd>
<dt><code>-no-xheader</code></dt>
<dd> <p> Do not create or extract POSIX.1-2001 extended headers. This option may be used if you like to read an archive with broken extended headers. </p>
 </dd>
<dt><code>-not</code>, <code>-V</code></dt>
<dd> <p> Invert the meaning of the pattern list. i.e. use those files which do not match any of the pattern. Note that this option only applies to patterns that have been specified via the <code>pattern=</code>pattern or <code>pat=</code>pattern option. Patterns specified as file type arguments will not be affected. </p>
 </dd>
<dt><code>-notarg</code>, <code>-pax-c</code></dt>
<dd> <p> Match all file or archive members except those specified by the pattern or file operands. </p>
 </dd>
<dt><code>-nowarn</code></dt>
<dd> <p> Do not print warning messages. This sometimes is useful to make the output more readable (e.g. when hundreds of files that are going to be extracted are not newer in the archive then on the filesystem). </p>
 </dd>
<dt><code>-numeric</code></dt>
<dd> <p> Use the numeric user/group fields in the listing rather than the default. The default allows to list the ASCII version of user/group of the file and to extract the owners of the files based on numeric values rather than the names. In create mode, no user/groups names are put on the archive. The <code>-numeric</code> option also applies when ACLs are going to be archived or extracted. </p>
 </dd>
<dt><code>-O</code></dt>
<dd> <p> Be compatible to old versions of <code>tar</code>. If <code>star </code> is invoked with this option, <code>star </code> generates archives which are fully compatible with old UNIX <code>tar</code> archives. If in extract mode, <code>star </code> ignores any additional info in the headers. This implies neither that archives generated with this option are binary equal with archives generated by old <code>tar</code> versions nor that <code>star </code> is trying to comprehend all bugs that are found in old <code>tar</code> versions. The bug in old <code>tar</code> versions that cause a reversal of a space and a NULL byte in the checksum field is not repeated. If you want to have signed checksums you have to specify the <i>-signed-checksum</i> option too. If you want directories not to be archived in order to be compatible to very old historic tar archives, you need to specify the <i>-d</i> option too. </p>
<p> This option is superseeded by the <code>H=</code>headertype option. </p>
 </dd>
<dt><code>-o</code>, <code>-nochown</code></dt>
<dd> <p> Do not restore owner and group of files. This may be used if super user privileges are needed to overwrite existing files but the local ownership of the existing files should not change. </p>
 </dd>
<dt><code>-onull</code>, <code>-nullout</code></dt>
<dd> <p> Do not actually write to the archive but compute and add the sizes. This is useful when trying to figure out if a tape may hold the current backup. Please only use the <code>-onull</code> option as it is a similar option as used by the <code>sdd</code>(1) command. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Allow <code>star</code> to write a partial record as the last record. Normally, <code>star </code> writes each record with the same size. This option is useful on unblocked tapes i.e. cartridge tapes like QIC tapes as well as with archives that are located in files. If you use this option on local files, the size of the archive will be smaller. If you use this option on cartridge tapes, is makes sure that later - in extract mode - <code>star</code> will read up to the end of file marker on the tape and the next call to <code>star</code> will read from the next archive on the same tape. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Restore files and directories to their original permissions. Without this option, they are created using the permissions in the archive and the present <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2). If <code>star</code> is called by the super user, <code>star</code> behaves as if it has been called with the <code>-p</code> option. See also <code>-no-p</code> option. If the archive contains Access Control Lists (ACLs) in POSIX.1-2001 extended headers, <code>star</code> will restore the access control lists from the archive for files if the -acl option is specified. If the option -acl has not been specified, ACLs are not restored at all. </p>
 </dd>
<dt><code>pattern=</code>pattern, <code>pat=</code>pattern </dt>
<dd> <p> Set matching pattern to <i>pattern.</i> A maximum of 100 pattern=pat options may be specified. As each pattern is unlimited in length, this is no real limitation. If more than one pattern is specified, a file matches if any of the specified pattern matches. Patterns may be used in create mode to select or exclude files from the list of file type arguments or the files located in a sub tree of a file type argument directory. By default, <code>star</code> scans the whole directory tree underneath a directory that is in the argument list. This may be modified by using the <code>-match-tree</code> option. In extract or list mode, all file type arguments are interpreted to be select pattern and all option type patterns may be either select or exclude patterns depending on the presence or absence of the <code>-not</code> option. If you use file type select patterns, they work exactly like the method used by other (non pattern aware) <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) implementations. File type select patterns do not offer pattern matching but allow to restore subtrees. To extract a complete sub tree from the directory <i>dir</i> with <code>star</code> using the <code>pattern=</code> option, use <code>pattern=</code> <i>dir/\\*</i> if you like to select a subtree by using the historic method, use <i>dir</i> as file type argument. If you only like to extract the directory itself, use <i>dir/</i> as file type argument. See manual page for <code>match</code>(1) for more details of the pattern matcher. All patterns are selection patterns by default. To make them exclude patterns, use the <code>-not</code> or the <code>-V </code> option. </p>
 </dd>
<dt><code>pkglist=</code><i>file</i></dt>
<dd> <p> This is (for now) an internal interface for the Schily Source Package System (sps). It only works in create mode and behaves similar to the <code>list=</code> option, but it allows to overwrite the <code>permissions</code>, the <code>uid</code> and <code>gid</code> values from the content of the <code>pkglist=</code> file. Each line from the <code>pkglist=</code> file contains a file name followed by the permission, a user name and a group name. The permission is an octal character string. Each value that is not used to overwrite the original values may be replaced by a &#8216;?&#8216;. The fields are separated by spaces, so the <code>pkglist=</code> option does not allow files that contain newline or space characters. </p>
 </dd>
<dt><code>-pax-c</code>, <code>-notarg</code></dt>
<dd> <p> Match all file or archive members except those specified by the pattern or file operands. </p>
 </dd>
<dt><code>-pax-H</code></dt>
<dd> <p> Follow symbolic links that have been encountered on the command line. If the referenced file does not exist, the file information and type will be for the link itself. If the link is referencing a file type that cannot be archived with the current archive format, the file information and type will be for the link itself. </p>
 </dd>
<dt><code>-pax-i</code></dt>
<dd> <p> Do interactive renaming in a way that has been defined for POSIX <code>pax</code>. <code>Star</code> will print the original filename and prompt for a reply. If you type just <code>RETURN</code>, than the file is skipped. If you type &#8216;.&#8216;, then the original file name is retained. If you type anything else, then this is taken as the new file name. </p>
<p> Note that <code>-pax-i</code> is an interactive option that prevents <code>star</code> from being used in non-interactive environments. </p>
 </dd>
<dt><code>-pax-L</code></dt>
<dd> <p> Follow symbolic links. If the referenced file does not exist, the file information and type will be for the link itself. If the link is referencing a file type that cannot be archived with the current archive format, the file information and type will be for the link itself. </p>
 </dd>
<dt><code>-pax-ls</code></dt>
<dd> <p> Switch listing format to the format defined for POSIX <code>pax</code> and <code>ls</code>. </p>
 </dd>
<dt><code>-pax-match</code></dt>
<dd> <p> Allow file type arguments to be recognised as regular expressions in a way that has been defined for POSIX <code>pax</code>. </p>
 </dd>
<dt><code>-pax-n</code></dt>
<dd> <p> Allow each pattern to match only once. If a pattern matches a directors, then the whole sub tree matches the pattern. </p>
 </dd>
<dt><code>-pax-p</code><i> string</i></dt>
<dd> <p> PAX style privileges string. Several characters (each has its own meaning). The following characters are defined: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>a</code></dt>
<dd> <p> Do not preserve file access times. This option is currently ignored. </p>
 </dd>
<dt><code>e</code></dt>
<dd> <p> Preserve the user ID, group ID, file mode bits. This is equivalent to calling <code>star -p -acl -xfflags</code>. </p>
 </dd>
<dt><code>m</code></dt>
<dd> <p> Do not preserve file modification times. This is currently equivalent to calling <code>star -m</code>. </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> Preserve the user ID and group ID. This is the default for <code>star</code> if called as root. </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> Preserve the file mode bits. This is equivalent to calling <code>star -p</code>. </p>
 </dd></dl>
</dl>
<dt><code>-prinodes</code></dt>
<dd> <p> Print inode numbers in verbose list mode if the archive contains inode numbers. </p>
 </dd>
<dt><code>-print-artype</code></dt>
<dd> <p> Check the type of the archive, print the archive and compression type on a single line and exit. </p>
 </dd>
<dt><code>-qic24</code></dt>
<dd> <p> Set tape volume size to 61440 kBytes. See <code>tsize=</code><i>#</i> option for more information. </p>
 </dd>
<dt><code>-qic120</code></dt>
<dd> <p> Set tape volume size to 128000 kBytes. See <code>tsize=</code><i>#</i> option for more information. </p>
 </dd>
<dt><code>-qic150</code></dt>
<dd> <p> Set tape volume size to 153600 kBytes. See <code>tsize=</code><i>#</i> option for more information. </p>
 </dd>
<dt><code>-qic250</code></dt>
<dd> <p> Set tape volume size to 256000 kBytes. See <code>tsize=</code><i>#</i> option for more information. </p>
 </dd>
<dt><code>-qic525</code></dt>
<dd> <p> Set tape volume size to 512500 kBytes. See <code>tsize=</code><i>#</i> option for more information. </p>
 </dd>
<dt><code>-read0</code></dt>
<dd> <p> Read null terminated file names from the file specified with the <code>list=</code> option. </p>
 </dd>
<dt><code>-refresh_old_files</code></dt>
<dd> <p> obsoleted by -refresh-old-files </p>
 </dd>
<dt><code>-refresh-old-files</code></dt>
<dd>  </dd>
<dt><code>-refresh</code></dt>
<dd> <p> Do not create new files. Only already existing files may be overwritten from <i>tarfile </i> if either newer versions are present in the archive or if the <code>-U</code> flag is used. This allows to overwrite files by more recent files from an archive that contains more files than the target directory should contain. The option <code>-refresh-old-files</code> is the same as the <code>-refresh</code> option. </p>
 </dd>
<dt><code>-remove_first</code></dt>
<dd> <p> obsoleted by -remove-first </p>
 </dd>
<dt><code>-remove-first</code></dt>
<dd> <p> Remove files before extraction. If this option is in effect, <code>star</code> will remove files before extracting a file from the archive. This is needed if you want to change the file type or if you need to break a hard link. If you do not use either <code>-ask-remove</code> or <code>-force-remove</code> together with <code>-remove-first</code>, this option is useless and no files will be removed. </p>
 </dd>
<dt><code>-remove_recursive</code></dt>
<dd> <p> obsoleted by -remove-recursive </p>
 </dd>
<dt><code>-remove-recursive</code></dt>
<dd> <p> Remove files recursive. If removing of a file is permitted, <code>star</code> will only remove files, specials and empty directories. If this option is in effect, <code>star</code> will be allowed to recursively removes non empty directories too. </p>
 </dd>
<dt><code>-restore</code></dt>
<dd> <p> switches <code>star</code> into <i>true incremental restore</i> mode. A file named <code>star-symtable</code> and a directory named <code>star-tmpdir</code> is created in the root directory of the file system where the extraction takes place. If <code>-restore</code> has been specified, star behaves as if <code>-xdot</code> has been specified too. See also <code>level=</code> option and section <code>INCREMENTAL BACKUPS</code> for more information. </p>
<p> Note: Do not use the <code>-restore</code> option if you only like to restore a single file or a list of selected files. </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> Do not store/create special files. A special files is any file except plain files, symbolic links and directories. You need to be super user to extract special files. </p>
 </dd>
<dt><code>-s</code><i> replstr</i></dt>
<dd> <p> Modify file or archive member names named by a pattern according to the substitution expression <i>replstr</i>. The format of <i>replstr</i> is: </p>
<p> <code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>-s&nbsp;<wbr></code><i>/old/new/[gp]</i> </p>
<p> The<br/>
 <code>old</code> pattern may use regular expressions and the <code>new</code> string may contain the special character &#8216;&amp;&#8216;. The character &#8216;&amp;&#8216; is substituted by the string that matches the <code>old</code> pattern. The optional trailing &#8216;g&#8217; means global substitution. If &#8216;g&#8217; is not used, a substitution pattern is only used once on a name. If the optional trailing &#8216;p&#8217; is used, the substitution is printed to standard error. </p>
<p> Up to 100 substitute options may be used. If more than one substitute option has been specified, <code>star</code> will loop over all substitute patterns until one matches. </p>
<p> If the name substitutes to the empty string, the file is skipped. </p>
 </dd>
<dt><code>-secure-links</code></dt>
<dd> <p> Do not extract hard links or symbolic links if the link name (the target of the link) starts with a slash (/) or if /../ is contained in the link name. Tar archives containing such links could be used to compromise the system. If they are unpacked together with a lot of other files, this may not even be noticed. </p>
<p> As the usability of a tar archiver would be limited if <code>-secure-links</code> checking would be done by default, <code>star</code> makes link checking optional. </p>
<p> If you unpacked a tar archive using the <code>-secure-links</code> and did not get a security warning at the end of the <code>star</code> run, all files and links have been extracted. If you get a warning, you should unpack the archive a second time and specify the options <code>-k</code>, <code>-w</code> and <code>-nowarn</code> in addition to the options used for the first run. See SECURITY NOTES for more information. </p>
 </dd>
<dt><code>-shm</code></dt>
<dd> <p> Use System V shared memory for fifo. Normally <code>star</code> is compiled to use mapped /dev/zero pages for the fifo, if the operating system supports this. If <code>star</code> is compiled to have both code for mapped pages and for System V shared memory, <code>star</code> will use shared memory instead of the default. If the <i>-help</i> menu doesn&#8217;t show the <i>-shm </i> flag you have no choice. When using System V shared memory, you may have to raise the system&#8217;s internal limit for shared memory resources to get enough shared memory for <code>star</code>. </p>
 </dd>
<dt><code>-signed_checksum</code></dt>
<dd> <p> obsoleted by -signed-checksum </p>
 </dd>
<dt><code>-signed-checksum</code></dt>
<dd> <p> Use signed chars to calculate checksums. This violates the <code>tar</code> specs but old versions of <code>tar </code> derived from the seventh edition of UNIX are implemented in this way. Note: Only filenames and linknames containing chars with the most significant bit set may trigger this problem because all other fields only contain 7 bit ASCII characters, octal digits or binary zeroes. </p>
 </dd>
<dt><code>-silent</code></dt>
<dd> <p> Suppress informational messages like <i>foobar is sparse</i>. </p>
 </dd>
<dt><code>-sparse</code></dt>
<dd> <p> Handle files with holes effectively on store/create. Note that sparse files may not be archived this way if the archive format is <code>tar</code>, <code>ustar</code>, <code>suntar</code>, <code>pax</code>, or any <code>cpio</code> variant. On Solaris-2.3 ... Solaris-2.5.1 there is a special ioctl() called <i>_FIOAI</i> that allows root to get the allocation info more efficiently. On Solaris 11 there is an enhanced <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) call with addidional whence values <code>SEEK_HOLE</code> and <code>SEEK_DATA</code> that allow to find holes in an efficient way. Other operating systems lack support to get the real allocation list and force <code>star</code> to scan the files to look for blocks that only contain null characters. This may <code>star</code> cause to assume more holes to be present than the number that the file really contains. </p>
 </dd>
<dt><code>-symlinks</code></dt>
<dd> <p> This option tells <code>star</code> in extract mode to try to create a symlink whenever a hardlink is encountered in the archive. </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> If the option <code>file= </code> or <code>f= </code> is omitted and the -T option is present, <code>star</code> will use the device indicated by the <code>TAPE </code> environment variable, if set. </p>
 </dd>
<dt><code>tardumps=</code><i>name</i></dt>
<dd> <p> Set the file name for tar dump dates database to <code>name</code>. The default name is <code>/etc/tardumps</code>. Use in combination with the <code>level= </code> option to create <i>true incremental dumps</i>. See also <code>-wtardumps</code> option and section <code>INCREMENTAL BACKUPS</code> for more information. </p>
 </dd>
<dt><code>-time</code></dt>
<dd> <p> Print timing info. See DIAGNOSTICS for more information. </p>
 </dd>
<dt><code>-to_stdout</code></dt>
<dd> <p> obsoleted by -to-stdout </p>
 </dd>
<dt><code>-to-stdout</code></dt>
<dd> <p> Extract files to stdout. This option may be used to extract <i>tarfiles</i> containing <i>tarfiles</i> (see examples below). </p>
 </dd>
<dt><code>-tpath</code></dt>
<dd> <p> Use this option together with the <i>-t</i> option or with <i>-cv</i> (verbose create) to get only a list of the pathnames of the files in the archive. This may be used in shell scripts to generate a name list. If used together with the <i>-diff </i> option, <code>star</code> will only print the names of the files that differ. A second run of <code>star </code> may then be used to restore all files that had differences to the archive. Use the <i>list=</i> option to specify the namelist in this case. </p>
 </dd>
<dt><code>tsize=</code># </dt>
<dd> <p> Set tape volume size to # to enable multi volume tape support. The value refers to the archive size without compression. See <i>bs=</i> for the possible syntax. By default, the number is multiplied by 512, so the value counts in units of 512 byte blocks. If the size specifier ends with a valid multiplication character (e.g &#8216;.&#8216; for bytes or &#8216;M&#8217; for MB) the specified size is used as specified and not multiplied by 512. With this option in effect, <code>star </code> is able to archive filesystems that are bigger then the tape size. If the option <code>tsize=</code># without <code>-multivol</code> then no file will be split across volumes and each volume may in theory be read back separately. Files that do not fit on a single tape may not be stored in this mode. If <code>-multivol</code> has been specified in addition, <code>star</code> will split files when the maximum allowed tape size has been reached. If the tape volume size is not a multiple of the tape block size, the tape volume size is silently rounded down to a value that is a multiple of the tape block size. </p>
<p> See <code>-multivol</code> option for more information. </p>
 </dd>
<dt><code>-U</code></dt>
<dd> <p> Restore files unconditionally. By default, an older file from the archive will not replace a corresponding newer file on disk. </p>
 </dd>
<dt><code>umask=</code><i>mask</i></dt>
<dd> <p> Set <code>star&#8217;s</code> umask to <i>mask</i>. This allows to control the permissions for intermediate directories that are created by <code>star</code> in extract mode. See also <code>-p</code> option. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Increment verbose level by one. This normally results in more output during operation. See also in the description for the <i>-t</i> flag. Normally, <code>star</code> does its work silently. If the verbose level is 2 or more and <code>star</code> is in create or update mode, <code>star</code> will produce a listing to the format of the ls -l output. </p>
 </dd>
<dt><code>-V</code>, <code>-not</code></dt>
<dd> <p> Invert the meaning of the pattern list. i.e. use those files which do not match any of the pattern. Note that this option only applies to patterns that have been specified via the <code>pattern=</code>pattern or <code>pat=</code>pattern option. Patterns specified as file type arguments will not be affected. </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Print version information and exit. </p>
 </dd>
<dt><code>VOLHDR=</code>name </dt>
<dd> <p> Use <i>name</i> to generate a volume header. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Do interactive creation, extraction or renaming. For every file that matches the list of patterns and that has a more recent modification time in the <code>tar</code> archive (if in extract mode and the -U option is not specified) <code>star </code> prints its name and asks: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>get/put ? Y(es)/N(o)/C(hange name) :</code> </p>
 </dd></dl>
<p> You may answer either `N&#8217; for No or &lt;Return&gt; to skip this file. If you answer `Y&#8217; the file is extracted or archived on tape with its original name. If you answer `C&#8217;, you are prompted for a new name. This name is used for the filename on disk if <code>star </code> is in extract mode or for the archive name if <code>star </code> is in create mode. </dl>
 </p>
<p> See SECURITY NOTES for more information. </p>
<p> Note that <code>-w</code> is an interactive option that prevents <code>star</code> from being used in non-interactive environments. </p>
<dt><code>-wready</code></dt>
<dd> <p> This option tells <code>Star </code> to wait up to two minutes for the drive to become ready. It has been added as a hack for a bug in the SunOS/Solaris <i>st</i> device driver. This driver has problems to sense the loading time with Exabyte drives with factory settings. It also makes sense to use <code>-wready</code> if multiple remote backups are made. In this case, the remote connection is closed while the remote tape server is still writing a file mark. If another remote backup is initiated before the old remote server did finish to write the file mark, it would be impossible to open the tape driver unless <code>-wready</code> is specified to tell <code>star</code> to wait for the drive to become ready again. </p>
 </dd>
<dt><code>-wtardumps</code></dt>
<dd> <p> Tell <code>star</code> to update the file that contains the tar dump dates data base if in dump mode. If the dump is not a <code>full dump</code>, the tar dump dates data base file is not written. See also <code>tardumps=</code><i>name</i> and <code>-C</code> option or <code>INCREMENTAL BACKUPS</code> section for more information. </p>
 </dd>
<dt><code>-X</code><i> filename</i></dt>
<dd> <p> Use the file <i>filename</i> as a file containing a list of path names to be excluded from the store/create/list/diff operation. The file <i>filename</i> must contain a list of path names, each on a separate line. Be careful with white space and note that path names in the list may not contain new lines. Multiple <code>-X</code> options may be used. Each argument must refer to a file containing path names. The <code>-X</code> option has precedence before other options that select files to be included in the operation. See also <code>list=</code> option. </p>
 </dd>
<dt><code>-xattr</code></dt>
<dd>  </dd>
<dt><code>-xattr-linux</code></dt>
<dd> <p> Store and extract extended file attributes as found on Linux systems. This option only makes sense when creating or extracting <code>exustar</code> archives as it is based on POSIX.1-2001 extended tar headers. </p>
<p> The method used in the current implementation could be used to store and extract extended file attributes from BSD too. Note that the current implementation is not generic enough to cover more general extended file attribute implementations as found on Solaris. If <code>star</code> starts to implement a method that covers extended file attributes on Solaris, the new method will be used then <code>-xattr</code> has been specified and <code>-xattr-linux</code> will refer to the old method. The method used with <code>-xattr-linux</code> may go away in the future. </p>
 </dd>
<dt><code>xdebug=</code><i>#, </i><code>xd=</code><i>#</i></dt>
<dd> <p> Set extended debug level to #. </p>
 </dd>
<dt><code>-xdev</code>, <code>-M</code></dt>
<dd> <p> Do not descend mount points. This is useful when doing backups of complete file systems. See NOTES for more information. </p>
 </dd>
<dt><code>-xdir</code></dt>
<dd> <p> Extract directories even if the corresponding directories on the archive are not newer. This is useful when for some reason, the directories are recorded after their content (see <code>-dirmode</code> option), or when the permissions of some directories must be set in any case. As the classical UNIX <code>cpio</code> program does not implement delayed directory permission and time stamp setting, <code>cpio</code> users often create archives in reverse order (directories past their content). For this reason, it makes sense to use <code>-xdir</code> while extracting <code>cpio</code> archives. </p>
 </dd>
<dt><code>-xdot</code></dt>
<dd> <p> Unconditionally extract the first directory in the archive if the name of this directory is either &#8216;.&#8216; or &#8216;./&#8216;. This helps to extract archives in an expected way if the target directory is a newly created empty directory. As this directory is newer than the top level directory in the archive, <code>star</code> would usually skip this directory during extraction. The effect of this directory is as if <code>-xdir</code> has been specified but is switched off after the first directory has been found. </p>
 </dd>
<dt><code>-xfflags</code></dt>
<dd> <p> Store and extract extended file flags as found on BSD and Linux systems. This option only makes sense when creating or extracting <code>exustar</code> archives as it is based on POSIX.1-2001 extended tar headers. See NOTES section for problems with <code>-xfflags</code> on Linux systems. </p>
 </dd>
<dt><code>-xmeta</code></dt>
<dd> <p> Extract <code>meta files</code> as if they were files. <code>Meta files</code> in archives are plain files that do not contain any content data in the archive. They may be created by using the <code>-meta</code> option in <code>star&#8217;s </code> create mode. Existing files are not overwritten. If a file is missing, a zero sized file is created. If the option <code>-meta</code> is used together with the option <code>-force-hole</code>, missing plain files are created as sparse empty files of the original size. </p>
 </dd>
<dt><code>-xz</code></dt>
<dd> <p> run the input or output through a <code>xz</code> pipe - see option <code>-z</code> below. </p>
 </dd>
<dt><code>-Z</code></dt>
<dd> <p> run the input or output through a <code>compress</code> pipe - see option <code>-z </code> below. </p>
 </dd>
<dt><code>-z</code></dt>
<dd> <p> run the input or output through a <code>gzip</code> pipe. This is currently a quick and dirty hack, that mainly will cover the most common usage to compress the <code>tar</code> output if it is a file. No reblocking will be done, so this option will currently only make sense on plain files. As the <code>-bz</code> the <code>-j</code> the <code>-Z</code> and the <code>-z</code> option are non standard, it makes sense to omit the <code>-bz</code> the <code>-j</code> the <code>-Z</code> and the <code>-z</code> options inside shell scripts if you are going to extract a compressed archive that is located inside a plain file as <code>star</code> will auto detect compression and choose the right decompression option to extract. The environment variable <code>STAR_COMPRESS_FLAG</code> may be used to specify one option for gzip. If you want to write write compressed archives to tape, you should use <br/>
 <i>star -c . | gzip | sdd ibs=4k obs=32k -fill of=/dev/rmt/1bn</i> <br/>
 or <br/>
 <i>star -c . | gzip | sdd ibs=4k obs=32k -fill ovsize=60m of=/dev/rmt/1bn</i> <br/>
 if the tape can hold 60 MB. </p>
 </dd></dl>
<h2>INCREMENTAL BACKUPS</h2>
<p> <code>Star</code> is able to back up file system in full and incremental mode. To allow incremental backups, the file system must implement POSIX semantics. </p>
<p> To be more verbose: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> The filesystem needs to uniquely identify files by the two numbers <code>st_dev</code> (The device ID of the device containing the file) and <code>st_ino</code> (The file serial number). If a file is renamed, these numbers need to be retained. Both numbers need to be a cardinal scalar that is expressible in a decimal number. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> The filesystem needs to implement at least two time stamps, <code>st_mtime</code> the file&#8217;s last modification time and <code>st_ctime</code> the file&#8217;s last status change time. Both time stamps need to be dealt with as documented by the POSIX standard. Both numbers need to be a cardinal scalar that is expressible in a decimal number. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> The filesystem needs to allow to rename files and directories by either calling <code><a href="/docs/linux/man/2-rename/">rename</a>(2),</code> or <code><a href="/docs/linux/man/2-link/">link</a>(2)</code> and <code><a href="/docs/linux/man/2-unlink/">unlink</a>(2).</code> </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> The filesystem needs to honor and preserve the case of file names. </p>
 </dd></dl>
<p> The incremental backup method used by <code>star</code> depends on comparing the time stamps of all files against the time of the last backup. Note that this method only works correctly if the level 0 backup and all higher level incrementals include the whole file system. As <code>star</code> archives all inode meta data, <code>star</code> is able to detect renamed files by comparing the <code>inode numbers</code> of all files while in incremental restore mode. </p>
<p> Detecting renamed files only works if <code>star</code>, while in backup mode, scans the whole file system tree for each full and incremental backup. This will work in case no files are excluded and the dump starts at the root directory of a file system. In case that no files are renamed from excluded parts to included parts, partial backups may be taken also. Partial backups only make sense if a complete directory sub tree is excluded (e.g. by using the <code>pat=</code> option) or if a partial backup starts at a sub directory that is not the root directory of the file system. </p>
<p> To create a level 0 dump call: </p>
<p> <code>star -c -xdev -sparse -acl -link-dirs level=0 -wtardumps \</code> <br/>
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>f=</code><i>archive-name</i> -C /<i>filestem-mount-point</i> . </p>
<p> To create a level 1 dump call: </p>
<p> <code>star -c -xdev -sparse -acl -link-dirs level=1 -wtardumps \</code> <br/>
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>f=</code><i>archive-name</i> -C /<i>filestem-mount-point</i> . </p>
<p> Do not forget the dot at the end of the command line that specifies the directory to start the operation. </p>
<p> Backups from live filesystems should be avoided. On operating systems that support <code>file system snapshots</code>, backups should be made from a read-only mount of a snapshot. Be careful that all files that have been created between setting up a snapshot and starting an incremental backup may be missing from all backups unless the <code>dumpdate=</code><i>name</i> option is used. </p>
<p> If the system that is going to be backed up is not acting as a file server, it makes sense to shut down all services that may result in inconsistent file states before setting up the filesystem snapshot. After the filesystem snapshot has been set up, the services may be restarted. </p>
<p> If the the system that is going to be backed up is acting as a file server, it may be that services on remote clients cause inconsistent file states unless all such services that remotely access files are shut down before the snapshot is set up. </p>
<p> <code>Star</code> includes options that help to deal with <code>file system snapshots</code>. The following example backs up a file system on Solaris using a file system snapshot: </p>
<p> <code>echo &gt; /tmp/snapstamp</code> </p>
<p> <code>mount -r `fssnap -F ufs -o \</code> <br/>
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>backing-store=/var/tmp/EXPORT-NFS.snap /export/nfs` /mnt</code> </p>
<p> <code>star -c -xdev -sparse -acl -link-dirs level=0 -wtardumps \</code> <br/>
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>f=</code><i>archive-name</i> dumpdate=/tmp/snapstamp \ <br/>
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fs-name=/export/nfs -C /mnt .</code> </p>
<p> First a file with a current time stamp is created, then a snapshot for /export/nfs is created and mounted on /mnt. The following <code>star</code> command then creates a level 0 backup from the file system using the time the snapshot was created and the original mount point of the file system for /etc/tardumps and the archive header. </p>
<p> Note that if the backup is done on a live file system, it may be unreliable. A typical problem problem in this context is caused by growing log files. As growing files are not a real problem with backups, the best way of dealing with growing files is to set up a <code>star</code> error control file (see <code>errctl=</code> option) and to tell <code>star </code> to ignore growing files.  </p>
<h2>BACKUP SCHEDULES</h2>
<p> Full (level 0) dumps should be made on a regular base (e.g. once a month). As a full dump may take a long time and takes a lot of tape, it is wise to make higher level incremental dumps with shorter intervals. The next table shows a dump level list that may be used if monthly full dumps take place: </p>
<dl>
<dd> <pre><code> Sun Mon Tue Wed Thu Fri 
 Week 1:       0 10 10 10 10 5
  Week 2:       10 10 10 10 10 5
  Week 3:       10 10 10 10 10 5
  Week 4:       10 10 10 10 10 5 
</code></pre>
 </dd></dl>
<p> The level 10 dumps made between Monday and Friday accumulate all changes made within the week. If you don&#8217;t like this, use the following backup schedule: </p>
<dl>
<dd> <pre><code> Sun Mon Tue Wed Thu Fri 
 Week 1:       0 20 30 40 50 5
  Week 2:       10 20 30 40 50 5
  Week 3:       10 20 30 40 50 5
  Week 4:       10 20 30 40 50 5 
</code></pre>
 </dd></dl>
<p> Note that in this case, 7 dumps need to be restored if the a crash happens at the worst case date (just before the Friday dump in week 2 or later). </p>
<h2>INCREMENTAL RESTORES</h2>
<p> Incremental restores should be made to an empty file system (except for the <code>lost+found</code> directory). <code>Star</code> is currently unable to perform incremental restores to a file system that contains active mount points. </p>
<p> The incremental restore procedure starts with restoring the last full (level 0) dump. Then the latest incremental dump of each dump level (with ascending order of dump levels) need to be restored. </p>
<p> Let us assume the first example from the section <code>BACKUP SCHEDULES</code> for the backup schedule. If a disk crash happens before the Thursday dump of week 3 has been made, the following restore procedure needs to be applied: </p>
<dl>
<dt><code>level 0</code></dt>
<dd> <p> starting with an empty disk, the full (level 0) dump from week 1 is restored. </p>
 </dd>
<dt><code>level 5</code></dt>
<dd> <p> after the level 0 restore has been finished, the level 5 dump from Friday in week 2 is restored. </p>
 </dd>
<dt><code>level 10</code></dt>
<dd> <p> after the level 5 restore has been finished, the level 10 dump from Wednesday in week 3 is restored. </p>
 </dd></dl>
<p> The disk now contains the same files as it did when the level 10 dump has been made on Wednesday of week 3. </p>
<p> To extract a level 0 dump call: </p>
<p> <code>cd /</code><i>filestem-mount-point</i> <br/>
 <code>star -xpU -restore f=</code><i>archive-name</i> </p>
<p> This creates the directory <code>star-tmpdir</code> and the database <code>star-symtable</code> in the root directory of the new file system. Subsequent restores with higher level backups depend on these files. </p>
<p> To extract a level 1 (or higher) dump call: </p>
<p> <code>cd /</code><i>filestem-mount-point</i> <br/>
 <code>star -xpU -restore f=</code><i>archive-name</i> </p>
<p> Note that the environment variable <code>STAR_DEBUG</code> exists, <code>star</code> does not remove files with link count 1 that have been removed between incremental dumps. These files are moved to the directory <code>star-tmpdir</code>. Before you start to extract the next incremental, you need to remove all files in <code>star-tmpdir</code>. </p>
<h2>SYNCHRONIZING FILESYSTEMS</h2>
<p> <code>Star</code> may be used to synchronize filesystem content. To do this, an initial copy of the current content of the source filesystem needs to be performed first. </p>
<p> To create an initial copy of a filesystem call: </p>
<p> <code>star -c -xdev -sparse -acl -link-dirs level=0 -wtardumps \</code> <br/>
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-C /</code><i>filestem-mount-point</i> . | \ <br/>
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>star -xpU -restore -C /</code><i>extract-target-dir</i> </p>
<p> In order to perform subsequent synchronization of the target filesystem with the content of the source filesystem, a modified incremental dump/restore procedure may be used. </p>
<p> To copy incremental content of a filesystem call: </p>
<p> <code>star -c -xdev -sparse -acl -link-dirs level=1 -wtardumps \</code> <br/>
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-cumulative -C /</code><i>filestem-mount-point</i> . | \ <br/>
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>star -xpU -restore -C /</code><i>extract-target-dir</i> </p>
<p> Note that like with backups in general, copies from a live filesystem should be avoided. On operating systems that support <code>file system snapshots</code>, copies should be made from a read-only mount of a snapshot. Be careful that all files that have been created between setting up a snapshot and starting an incremental copy may be missing from all copies unless the <code>dumpdate=</code><i>name</i> option is used. </p>
<p> See section <code>INCREMENTAL BACKUPS</code> to learn how to modify the command line in case <code>file system snapshots</code> are used.  </p>
<h2>SIGNALS</h2>
<p> If <code>star </code> handles a signal, it first prints the statistics. <code>Star </code> handles the following signals: </p>
<dl>
<dt><code>SIGINT</code></dt>
<dd> <p> usually generated by ^C from the controlling tty. Upon receipt of a SIGINT, <code>star </code> prints statistics and exits. If in create mode i.e. storing files to archive, <code>star </code> finishes with the current file to ensure that no partial file is written to the archive, write an eof record and then exits. </p>
 </dd>
<dt><code>SIGHUP</code></dt>
<dd> <p> not to be generated from a tty. The actions are the same as upon receipt of a SIGINT. </p>
 </dd>
<dt><code>SIGQUIT</code></dt>
<dd> <p> usually generated by ^\ from the controlling tty. Upon receipt of a SIGQUIT, <code>star </code> prints statistics and continues with the current operation. This is useful to watch the progress of the current operation. </p>
 </dd></dl>
<h2>EXIT STATUS</h2>
<p> The following exit values are returned: </p>
<dl>
<dt><code>0</code></dt>
<dd> <p> All files were processed successfully. </p>
 </dd>
<dt><code>-3 / 253</code></dt>
<dd> <p> <code>Star</code> has been called with the option <code>-e</code>, or the <code>errctl=</code> option has been used to mark the current error fatal. </p>
 </dd>
<dt><code>-2 / 254</code></dt>
<dd> <p> One or more files could not be processed successfully. </p>
 </dd>
<dt><code>-1 / 255</code></dt>
<dd> <p> Command line parsing error. </p>
 </dd>
<dt><code>&gt;0</code></dt>
<dd> <p> Other positive exit codes: The <code>errno</code> of the call that caused the fatal error. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> To get a listing in a way similar to ls -l one might use: </p>
<dl>
<dd> <p> <code>example% star -tv f=/dev/rmt/1bn</code> </p>
 </dd></dl>
<p> The same command as listed above in a <code>POSIX tar</code> command line syntax compliant way is: </p>
<dl>
<dd> <p> <code>example% star tvf /dev/rmt/1mbn</code> </p>
 </dd></dl>
<p> To copy the directory tree in <i>/home/someuser</i> to the directory <i>/home/fs</i> use: </p>
<dl>
<dd> <pre><code>
 example% (cd /home/someuser; star -c .) | (cd /home/fs ; star -xp) 
</code></pre>
 </dd></dl>
<p> or by using the change directory option of <code>star</code>: </p>
<dl>
<dd> <pre><code>example% star -c -C /home/someuser . | star -xp -C /home/fs
</code></pre>
 </dd></dl>
<p> Note that both examples above are not the optimum way to copy a directory tree. A more efficient way to copy a directory tree is to use the <code>-copy</code> option. </p>
<dl>
<dd> <pre><code>
 example% star -copy -p -xdot -C /home/someuser . /home/fs 
</code></pre>
 </dd></dl>
<p> To copy a file tree including the <code>Access Control List</code> entries for all files and to correctly copy sparse (holey) files use: </p>
<dl>
<dd> <pre><code>example% star -copy -p -xdot -acl -sparse -C /home/someuser . /home/fs
</code></pre>
 </dd></dl>
<p> To compare the content of a tape to the filesystem one might use: </p>
<dl>
<dd> <p> <code>example% star -diff -v f=/dev/rmt/1bn</code> </p>
 </dd></dl>
<p> To compare two directory trees one might use: </p>
<dl>
<dd> <pre><code>example% star -c . | star -C todir -diff -v diffopts=!times
</code></pre>
 </dd></dl>
<p> or better by using a method similar to the <code>-copy</code> method above: </p>
<dl>
<dd> <pre><code>example% star -c -diff -v diffopts=!times -C fromdir . todir
</code></pre>
 </dd></dl>
<p> To compare all properties of two file trees, use: </p>
<dl>
<dd> <pre><code>example% star -c -diff -vv -dump -acl -sparse -C fromdir . todir
</code></pre>
 </dd></dl>
<p> To extract a backup of the /usr tree without all files residing below /usr/openwin one might use: </p>
<dl>
<dd> <p> <code>example% star -xp -V pat=openwin/\* f=/dev/rmt/1bn</code> </p>
 </dd></dl>
<p> To extract all <i>.c </i> files to <code>src</code>, all <i>.o </i> files to <code>obj </code> and all other files to /tmp one might use: </p>
<dl>
<dd> <pre><code>example% star -xp -C src '*.c' -C obj '*.o' -C /tmp '*' f=/dev/rmt/1bn
</code></pre>
 </dd></dl>
<p> To extract files from a zipped <code>tar</code> archive that is located on a read only filesystem e.g. a CD while having the shell&#8217;s working directory on the CD one might use: </p>
<dl>
<dd> <p> <code>example% star -zxp -C /tmp f=star-1.1.tar.gz</code> </p>
 </dd></dl>
<p> to extract the files from the <code>tar</code> archive to the /tmp directory. </p>
<p> To backup a list of files generated by the <code><a href="/docs/linux/man/1-find/">find</a></code>(1) command: </p>
<dl>
<dd> <pre><code>example% find . find_options  -print | star -c list=- f=/dev/rmt/1bn
</code></pre>
 </dd></dl>
<p> Note that this does not work if the file names from output of the <code>find </code> command include new line characters. </p>
<p> To extract a <i>tarfile</i> that contains a <i>tarfile</i> one might use: </p>
<dl>
<dd> <pre><code>example% star -x -to-stdout f=/dev/rmt/1bn pat= pat  | star -xp
</code></pre>
 </dd></dl>
<p> <i>Pat, </i> in this case should match the <i>tarfile</i> in the <i>tarfile</i> on tape that should be extracted. </p>
<p> To make a backup of the root filesystem to a tape drive connected to a remote machine, one might use: </p>
<dl>
<dd> <p> <code>example# cd /</code> <br/>
 </p>
<pre><code>example# star -cM fs=128m bs=63k f=tape [at] remotehost:/dev/rmt/1bn .
</code></pre>
 </dd></dl>
<p> You need a line in /etc/passwd like the following to enable this: </p>
<dl>
<dd> <p> <code>tape:NP:60001:60001:Tape:/etc/tapehome:/opt/schily/sbin/rmt</code> </p>
 </dd></dl>
<p> And a .rhosts file in /etc/tapehome to allow remote connections from the appropriate hosts. Make sure that the file /etc/default/rmt exists and allows remote access to the requested tape drive. </p>
<p> To use a <code><a href="/docs/linux/man/1-ssh/">ssh</a>(1)</code> connection for a backup to a remote tape server, one might use: </p>
<dl>
<dd> <p> <code>example# env RSH=/usr/bin/ssh star -cM fs=128m bs=63k f=tape [at] remotehost:/dev/rmt/1bn .</code> </p>
 </dd></dl>
<p> To repair a corrupted filesystem for which no recent backup exists, do the following: </p>
<dl>
<dd> <p> <code>example# fsck -y /filesys</code> <br/>
 <code>example# mount /filesys</code> <br/>
 <code>example# cd /filesys</code> <br/>
 <code>example# star -xpk f=/dev/rmt/1bn</code> <br/>
 <code>example# mt -f /dev/rmt/1bn rewind</code> <br/>
 <code>example# star -diff -v diffopts=!times f=/dev/rmt/1bn</code> </p>
 </dd></dl>
<p> Now check the differences and decide whether to restore additional files. This may be done by generating a list containing the needed filenames and using the list= option or by using the interactive mode (see -w option). </p>
<p> If you want a list that only contains all filenames from files with differences you may use: </p>
<dl>
<dd> <p> <code>example# star -diff -tpath diffopts=!times f=/dev/rmt/1bn</code> </p>
 </dd></dl>
<p> If you are looking for files that changed the type or the access permission because this is a common case on still corrupted files, use: </p>
<dl>
<dd> <p> <code>example# star -diff -tpath diffopts=type,perm f=/dev/rmt/1bn</code> </p>
 </dd></dl>
<p> If you like to archive all directories only that are part of the directory tree under &quot;.&quot;, use: </p>
<dl>
<dd> <p> <code>example# star -c f=</code><i>archive-name</i> -find . -type d </p>
 </dd></dl>
<p> If you like to archive all files as owner root and group root and make all files world readable in the archive, use: </p>
<dl>
<dd> <p> <code>example# star -c f=</code><i>archive-name</i> -find . -chown root -chgrp root -chmod o+r </p>
 </dd></dl>
<p> If you like to list all files in an archive in a way like <code>sfind</code>(1), instead of the way used by star, use: </p>
<dl>
<dd> <p> <code>example# star -t f=</code><i>archive-name</i> -find . -ls -false </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>STAR_COMPRESS_FLAG</code></dt>
<dd> <p> If you like <code>star</code> to always create compressed files that use maximum compression, you may set the environment variable <code>STAR_COMPRESS_FLAG</code> to -9. </p>
 </dd>
<dt><code>STAR_DEBUG</code></dt>
<dd> <p> If this environment variable is present, <code>star</code> will not remove temporary files from <code>./star-tmpdir</code>. The files in this directory are files that have been removed by users before the last incremental dump did take place on the master filesystem. </p>
 </dd>
<dt><code>STAR_FIFOSIZE</code></dt>
<dd> <p> If you like to by default let <code>star</code> use a different fifo size, set this environment variable to the desired size. </p>
 </dd>
<dt><code>TAPE</code></dt>
<dd> <p> Unlike other <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) implementations, <code>star</code> defaults to use stdin/stdout for the archive. If you like <code>star</code> to use the file name from the <code>TAPE</code> environment instead, you need to specify the <code>-T</code> option too. </p>
 </dd>
<dt><code>RSH</code></dt>
<dd> <p> If the <code>RSH</code> environment is present, the remote connection will not be created via <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3) but by calling the program pointed to by <code>RSH</code>. Use e.g. <code>RSH=</code>/usr/bin/ssh to create a secure shell connection. </p>
<p> Note that this forces <code>star</code> to create a pipe to the <code><a href="/docs/linux/man/1-rsh/">rsh</a>(1)</code> program and disallows <code>star</code> to directly access the network socket to the remote server. This makes it impossible to set up performance parameters and slows down the connection compared to a <code>root</code> initiated <code><a href="/docs/linux/man/3-rcmd/">rcmd</a>(3)</code> connection. </p>
<p> See BUGS section for more information. </p>
 </dd>
<dt><code>RMT</code></dt>
<dd> <p> If the <code>RMT</code> environment is present, the remote tape server will not be the program <code>/etc/rmt</code> but the program pointed to by <code>RMT</code>. Note that the remote tape server program name will be ignored if you log in using an account that has been created with a remote tape server program as login shell. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/default/star</code></dt>
<dd> <p> Default values can be set for the following options in /etc/default/star. For example: CDR_FIFOSIZE=64m </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>STAR_FIFOSIZE</code></dt>
<dd> <p> Sets the default size of the FIFO (see also <code>fs=</code># option). </p>
 </dd>
<dt><code>STAR_FIFOSIZE_MAX</code></dt>
<dd> <p> Sets the maximum size of the FIFO (see also <code>fs=</code># option). Setting <code>STAR_FIFOSIZE_MAX</code> in <code>/etc/default/star</code> allows to overwrite global values from backup scripts for machines with less memory. </p>
 </dd>
<dt><code>archive0=</code></dt>
<dd>  </dd>
<dt><code>archive1=</code></dt>
<dd>  </dd>
<dt><code>archive2=</code></dt>
<dd>  </dd>
<dt><code>archive3=</code></dt>
<dd>  </dd>
<dt><code>archive4=</code></dt>
<dd>  </dd>
<dt><code>archive5=</code></dt>
<dd>  </dd>
<dt><code>archive6=</code></dt>
<dd>  </dd>
<dt><code>archive7=</code></dt>
<dd> <p> Archive entries for the <code>-[0..7]</code> option. </p>
<p> A correct <code>archive?=</code> line has 3..4 space separated entries. The first is the device entry (e.g. <i>archive0=/dev/tape</i>). The second is the blocking factor in 512 byte units. The third is the maximum media size in 1024 byte units. If this entry contains a 0, then the media size is unlimited. The fourth entry is optional. If it contains a &#8216;n&#8217; or a &#8216;N&#8217;, then the archive device is not a tape. </p>
<p> Examples: </p>
<p> archive0=/dev/tape 512 0 y <br/>
 archive1=/dev/fd0 1 1440 n <br/>
 archive2=/dev/rmt/0mbn 512 0 </p>
<p> If the default file does not need to be shared with the tar program from Solaris, any number may be used like a generic size option like bs=. </p>
<p> Example: </p>
<p> archive0=/dev/tape 256k 40G y </p>
 </dd></dl>
</dl>
<dt><code>/etc/tardumps</code></dt>
<dd> <p> The default name for the dump level archive. The default name is used whenever the <code>tardumps=</code><i>name</i> option has not been specified. The file is written or updated when <code>-wtardumps</code> is used. </p>
<p> The file holds one or more lines, each specifying a dump level entry. Each dump level entry starts with a mount point name followed by a TAB and one or more spaces, followed by the decimal dump level, a space and the dump time. </p>
<p> If the dump level is directly followed by a &#8216;P&#8217;, then the dump refers to a partial dump (a dump that does not include the whole filesystem). </p>
<p> The dump time itself includes the decimal representation of the UTC seconds since Jan 01 1970, a space and the textual local time representation of the dump time. </p>
<p> The numerical decimal dump time representation may be followed by a dot and a sub second value. The textual local time representation is for informational use by humans only and not evaluated by <code>star</code>. </p>
 </dd>
<dt><code>./star-symtable</code></dt>
<dd> <p> Contains a database that is needed in incremental restore mode. </p>
 </dd>
<dt><code>./star-symdump</code></dt>
<dd> <p> Contains an intermediate dump of restore database after a fatal error condition was met during an incremental restore operation. </p>
 </dd>
<dt><code>./star-tmpdir</code></dt>
<dd> <p> Is the temporary directory that is used as intermediate file storage by <code>star</code> if in incremental restore mode. </p>
 </dd>
<dt><code>./star-lock</code></dt>
<dd> <p> Is a lock file created by star when doing an incremental restore. If this file is present, it prevents <code>star</code> from running another incremental restore operation. This helps to avoid more than one restore operation at a time (e.g. from a cron script). </p>
 </dd>
<dt><code>/dev/tty</code></dt>
<dd> <p> Is used for the intercative user interface. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-spax/">spax</a></code>(1), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/1-cpio/">cpio</a></code>(1), <code>pax</code>(1), <code><a href="/docs/linux/man/1-rcp/">rcp</a></code>(1), <code><a href="/docs/linux/man/1-mt/">mt</a></code>(1), <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8), <code>match</code>(1), <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1), <code>sdd</code>(1), <code><a href="/docs/linux/man/1-rsh/">rsh</a></code>(1), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code>star</code>(4), <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3), <code>fssnap</code>(1m)  </p>
<h2>DIAGNOSTICS</h2>
<p> star: f records + p bytes (total of x bytes = d.nnk). </p>
<p> The number of full records, the number of bytes in partial records and the total amount of data in KBytes. </p>
<p> star: Total time x.yyysec (z kBytes/sec) </p>
<p> The time used and the transfer speed from/to the archive. </p>
<p> If there have been non fatal errors during the archive processing, <code>star</code> will display a delayed error summary before exiting. </p>
<h2>NOTES</h2>
<p> The command line syntax for the tar command (as defined in SUSv2 - UNIX-98) deviates from the command line syntax defined for all other commands. While the <code>POSIX command line syntax</code> requests all options to start with a dash (-) and allows to either write options separately or combined (in case of boolean flags), the <code>tar</code> command line syntax requires all options to be combined into a single string that does not start with a dash. <code>Star</code> by default assumes a command line syntax like a typical POSIX command and includes a compatibility mode that allows to specify a command line syntax as documented for the <code>UNIX-98 tar</code> command. If you believe that you found a bug in the way <code>star</code> parses the command line, please first check your command line for correctness before you make a bug report for <code>star</code>. </p>
<p> If you like to write portable shell scripts that call tar, use the <code>UNIX-98 tar</code> command line syntax (i.e. a single option string and no dash), choose the commands and options from the following set of characters ( <i>rxtuc vxfblmo</i> ) and check the shell script with both, your local tar and <code>star</code> for correct behavior. It you expect the script to call gnutar, do not include the <code>-o</code> option as gnutar implements this option in a way that violates UNIX-98. </p>
<p> <code>Star </code> strips leading ./ sequences from pathnames. This lets <code>star </code> in many cases store longer pathnames than other implementations. </p>
<p> The POSIX.1-1988 method (ustar format) of storing files with pathnames that are longer than 100 chars has some limitations: </p>
<dl>
<dd> <p> The name field (100 chars) an inserted slash (`/&#8216;) and the prefix field (155 chars) produce the pathname of the file. When recreating the original filename, name and prefix are concatenated, using a slash character in the middle. If a pathname does not fit in the space provided or may not be split at a slash character so that the parts will fit into 100 + 155 chars, the file may not be archived. Linknames longer than 100 chars may not be archived too. </p>
 </dd></dl>
<p> The <i>star</i>, <i>xstar</i>, <i>xustar</i>, <i>exustar</i>, <i>pax</i>, and <i>gnutar</i> archive formats don&#8217;t have these limitations. While gnutar uses a method that makes it impossible for other <code>tar</code> implementations (except <code>star</code>) to restore filenames that are longer than 100 chars, the <i>xstar</i>, <i>xustar</i>, <i>exustar</i> and <i>pax</i> archive format uses a method that allows an POSIX.1-1988 compliant way of storing filenames, if the POSIX method would allow this. When the archive format is <i>xustar</i>, <i>exustar</i> or <i>pax</i> very long filenames are stored using extended headers from the POSIX.1-2001 standard. </p>
<p> Some buggy <code>tar</code> implementations will generate incorrect filenames during a restore operation if the archive contains pathnames or linknames of exactly 100 chars length. </p>
<p> <code>Star</code> adds a <i>tar</i> signature in the last four bytes of each <code>tar</code> header if the archive format is <i>star</i> or <i>xstar</i>. This is no problem with the <code>star </code> archive format as it is an extension of the old pre POSIX.1-1988 tar format. On the other side, the <code>xstar</code> archive format claims to be as POSIX.1-1988 compliant as possible. Inserting this <i>tar </i> signature is a minor deviation from the standard that has the last 12 bytes of each header reserved for future use. On the other side, <code>tar</code> implementations such as some <code>pax</code> implementations that only compute checksums on the first 500 bytes of the header are violating the standard that requests the checksum to be computed on all 512 bytes of the tar header. All <code>tar</code> implementations that are 100% Posix compliant will be able to extract <code>xstar </code> archives as long as no new standard is defined that claims the last 12 bytes of the header for a different use. But then the <code>ustar version</code> number should be changed from `00&#8217; to `01&#8217;. Now, that the POSIX-2001 standard has been accepted, it is even predictable that all extensions to the standard <code>tar</code> format will go into the POSIX.1-2001 extended headers which are extensible to include any feature without future limitation. The only known <code>tar</code> implementation that also uses the last 12 bytes of the <code>tar</code> header is Sun&#8217;s <code>tar</code> which uses these 12 bytes for files that are split over several archives. Such archives created by Sun&#8217;s tar are not readable by the buggy <code>pax</code> implementation too. The Sun extension is not incompatible to the <code>star </code> signature because Sun expects an octal number at the beginning of the 12 byte field which is a null character in the <code>star</code> case. </p>
<p> <code>Star</code> uses these four bytes since 1985 without problems. If you need a 100% POSIX.1-1988 and 100% POSIX.1-2001 compliant tar archive, you may use the <i>xustar</i>, <i>exustar</i> or the <i>pax</i> archive format. The probability of falsely detecting other <code>tar</code> formats as <code>xustar </code> or <code>exustar</code> format however is higher. </p>
<p> There is no way to ask for the <i>n</i>-th occurrence of a file. </p>
<p> The way EOF is handled by <code>star</code> differs, whether the fifo is in effect or not. If the fifo is not used, <code>star </code> stops reading the archive if it encounters a logical EOF record in the archive. If the fifo is used, <code>star </code> may read until the fifo is full or until the real EOF mark on tape is reached. How much data <code>star actually reads depends on the time when the </code> <code>star</code> foreground process sends a fifo shutdown signal to the background fifo read process. </p>
<p> Gnu tar often creates <code>tar</code> archives with incorrect logical EOF marks. The standard requires two blocks that are completely zeroed, whereas gnutar often only adds one of them. </p>
<p> Old versions of <code>tar</code> found on SYSVr3 and earlier cannot read <code>tar</code> archives with a blocksize greater than 10 kBytes. </p>
<p> The method of storing <i>sparse</i> files currently used with the <i>star</i> and <i>xstar</i> format is not guaranteed to be used in later versions of <code>star</code>. If the author decides to change this method, later versions of <code>star </code> may not be able to restore sparse files from <code>tar </code> archives made by the current version of <code>star</code>. </p>
<p> Some <code>tar</code> implementations violate the standard in using only the first 500 Bytes of the header for checksum computation. These <code>tar</code> implementations will not accept <i>star </i> and <i>xstar</i> type <code>tar</code> archives. </p>
<p> Sun&#8217;s Solaris 2.x <code>tar</code> implementation violates the Posix standard. Tar archives generated by <code>star</code> cause Sun&#8217;s <code>tar</code> to print tar: impossible file type messages. You may ignore these messages. </p>
<p> Gnutar&#8217;s dumpdirs are non standard and are currently not implemented. </p>
<p> If gnutar archives sparse files with more than four holes, it produces archives that violate the standard in a way that prevents other <code>tar</code> implementations to read these archives. <code>Star </code> knows about that and is able to handle these gnutar archives. </p>
<p> The filetype <i>N</i> (LF_NAMES) from gnutar (an obsolete method of storing long names) will never be implemented. </p>
<p> Note that on operating systems (like DOS) that do not implement real pipes, <code>star</code> implements compression via a temporary file. Using compression thus is limited by the maximum file size and the available disk space. </p>
<p> The extended file flags implementation (see <code>-xfflags</code> option) on Linux is buggy by design. In order to retrieve the needed information, every file needs to be opened. If the /dev directory is included in create mode, every possible driver will be loaded which may hang the system for a long time. In the worst case, unwanted side effects from opening devices (such as causing tape drives to rewind the media) may be caused. </p>
<h2>SECURITY NOTES</h2>
<p> If you unpack a tar archive in a non empty directory, any file in that directory may be overwritten unless you specify the <code>-k</code> option. If the archive contains symbolic links or hard links, <code>star</code> may even overwrite files outside the current directory. If the directory where the archive is been unpacked is not empty and contains contains symbolic links or hard links to directories outside that directory, <code>star</code> may also overwrite files outside the current directory. As many other commands, <code>star</code> usually has all possible permissions when run as root. Unpacking archives as root thus may have fatal results to any file on your system. Be very careful when you try to extract an archive that has not been created by you. It is possible to create hand crafted tar archives that may overwrite critical files (like /etc/passwd) on your system. In addition all tar archives that have been created with the <code>list=</code> option and tar archives where the <code>C=</code> option was not specified before all file type arguments may be critical. </p>
<p> A good advise is to extract all doubtful archives as non root in an empty directory and to specify the <code>-secure-links</code> option. If you get a warning, you should unpack the archive a second time and specify the options <code>-k</code>, <code>-w</code> and <code>-nowarn</code> in addition to the options used for the first run.  </p>
<h2>SUID NOTES</h2>
<p> If <code>star</code> is installed suid root, <code>star</code> is able to make connections to remote archives for non root users. This is done by using the <a href="/docs/linux/man/3-rcmd/">rcmd</a>(3) interface to get a connection to a <a href="/docs/linux/man/8-rmt/">rmt</a>(8) server. </p>
<p> <code>Star</code> resets its effective uid back to the real user id immediately after setting up the remote connection to the rmt server and before opening any other file. </p>
<p> If <code>star </code> has not been installed suid root and not called by root, it will try to create the remote connection via <code><a href="/docs/linux/man/1-rsh/">rsh</a>(1)</code> or <code><a href="/docs/linux/man/1-ssh/">ssh</a>(1)</code> (in case the environment <code>RSH</code> has been set to <code>ssh</code>). Note that in this case, the throughput to the remote tape server will be much lower than with a connection that has been initiated via <code><a href="/docs/linux/man/3-rcmd/">rcmd</a>(3)</code>.  </p>
<h2>LIMITATIONS</h2>
<p> If <code>star</code> is running on a large file aware platform, <code>star</code> is able to handle files up to 8 GB in a mode that is compliant to the POSIX.1-1988 <code>ustar</code> format. With a nonstandard <code>star</code> specific extension, up to 95 bits may be used to code the filesize. This will handle files up to 200,000,000 TB. With the new POSIX.1-2001 extended headers used by the <i>xustar</i>, <i>exustar</i> and <i>pax</i> format, any filesize may be archived.  </p>
<h2>BUGS</h2>
<p> The fact that the <code>-f</code> option has to be implemented in a way that is compatible with old tar implementations gives several problems. The options <code>-fifostats</code>, <code>-force-hole</code>, <code>-force-remove</code> and <code>-fifo</code> interfere with the <code>-f</code> option and the fact that they exist prevents users from using filenames like e.g. <code>ifo</code> using the traditional way where the filename directly follows the string <code>-f</code> without any space between the option name and the file name. However, there is no problem to use a file named <code>ifo</code> by by calling <code>-f ifo</code>, <code>f=ifo</code>, <code>-f=ifo</code> or <code>-f= ifo</code>. Be careful not to make typos with the above options. The result could be that a file is created as a result of the mistyped option. </p>
<p> There is currently no way to set the fifo lowwater and highwater marks. </p>
<p> There is currently no way to automatically delete files in the target file tree if they are obsolete. <code>Star </code> should implement something similar to gnutar&#8217;s dumpdirs. </p>
<p> If not invoked by the super user <code>star </code> may not be able to extract files if they reside in read only directories. </p>
<p> <code>Star </code> is not able to make a complete backup of a filesystem if files are hidden by a mount that is in effect on a directory of this filesystem. This may be avoided in case of the ufs filesystem if the backup is made off a ufs snapshot (see the man page for <code>fssnap</code>(1m) It could be avoided for any filesystem if the loopback filesystem had an option that tells <i>lofs </i> not to traverse mountpoints. </p>
<p> For now (late 2002), we know that the following programs are broken and do not implement signal handling correctly: </p>
<dl>
<dt>rsh</dt>
<dd> <p> on SunOS-5.0...SunOS-5.9 </p>
 </dd>
<dt>ssh</dt>
<dd> <p> from ssh.com </p>
 </dd>
<dt>ssh</dt>
<dd> <p> from openssh.org </p>
 </dd></dl>
<p> Sun already did accept a bug report for <code><a href="/docs/linux/man/1-rsh/">rsh</a></code>(1)<code>/</code><a href="/docs/linux/man/1-ssh/">ssh</a>(1)<code>.</code> Openssh.org accepted and fixed a bug for their implementation of <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1). </p>
<p> If you use <code>star</code> to create a remote connection via an unfixed <code><a href="/docs/linux/man/1-rsh/">rsh</a></code>(1) or <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), be prepared that terminal generated signals may interrupt the remote connection. </p>
<h2>HISTORY</h2>
<p> <code>Star</code> was first created in 1982 to extract tapes on a UNIX clone that had no <code>tar</code> command. In 1985 the first fully functional version has been released as <code>mtar.</code> </p>
<p> When the old <code>star </code> format extensions have been introduced in 1985, it was renamed to <code>star</code> (Schily tar). In 1994, Posix 1003.1-1988 extensions were added and <code>star </code> was renamed to <code>star</code> (Standard tar). </p>
<h2>AUTHOR</h2>
<pre><code>Joerg Schilling
Seestr. 110
D-13353 Berlin
Germany
</code></pre>
<p> Mail bugs and suggestions to: </p>
<p> <code>schilling [at] fokus.fraunhofer.de</code> or <code>js [at] cs.tu-berlin.de</code> or <code>joerg [at] schily.isdn.cs.tu-berlin.de</code> </p>
