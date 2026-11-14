---
title: "unzip(1)"
name: "unzip"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unzip/"
description: "unzip – list, test and extract compressed files in a ZIP archive"
---

<h2 class="name">NAME</h2>
<p> unzip &#8211; list, test and extract compressed files in a ZIP archive </p>
<h2>SYNOPSIS</h2>
<p> <code>unzip</code> [<code>-Z</code>] [<code>-cflptTuvz</code>[<code>abjnoqsCDKLMUVWX$/:^</code>]] <i>file</i>[<i>.zip</i>] [<i>file(s)</i>&nbsp;&#8230;] [<code>-x</code>&nbsp;<i>xfile(s)</i>&nbsp;&#8230;] [<code>-d</code>&nbsp;<i>exdir</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>unzip</i> will list, test, or extract files from a ZIP archive, commonly found on MS-DOS systems. The default behavior (with no options) is to extract into the current directory (and subdirectories below it) all files from the specified ZIP archive. A companion program, <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), creates ZIP archives; both programs are compatible with archives created by PKWARE&#8217;s <i>PKZIP</i> and <i>PKUNZIP</i> for MS-DOS, but in many cases the program options or default behaviors differ.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>file</i>[<i>.zip</i>]</p>
<dd> Path of the ZIP archive(s). If the file specification is a wildcard, each matching file is processed in an order determined by the operating system (or file system). Only the filename can be a wildcard; the path itself cannot. Wildcard expressions are similar to those supported in commonly used Unix shells (<i>sh</i>, <i>ksh</i>, <i>csh</i>) and may contain:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> matches a sequence of 0 or more characters</p>
<dt>?</p>
<dd> matches exactly 1 character</p>
<dt>[&#8230;]</p>
<dd> matches any single character found inside the brackets; ranges are specified by a beginning character, a hyphen, and an ending character. If an exclamation point or a caret (`!&#8217; or `^&#8217;) follows the left bracket, then the range of characters within the brackets is complemented (that is, anything <i>except</i> the characters inside the brackets is considered a match). To specify a verbatim left bracket, the three-character sequence &#8220;[[]&#8221; has to be used.</dl>
</dl>
<dt>
<dd> (Be sure to quote any character that might otherwise be interpreted or modified by the operating system, particularly under Unix and VMS.) If no matches are found, the specification is assumed to be a literal filename; and if that also fails, the suffix .zip is appended. Note that self-extracting ZIP files are supported, as with any other ZIP archive; just specify the .exe suffix (if any) explicitly.</p>
<dt>[<i>file(s)</i>]</p>
<dd> An optional list of archive members to be processed, separated by spaces. (VMS versions compiled with VMSCLI defined must delimit files with commas instead. See <code>-v</code> in <code>OPTIONS</code> below.) Regular expressions (wildcards) may be used to match multiple members; see above. Again, be sure to quote expressions that would otherwise be expanded or modified by the operating system.</p>
<dt>[<code>-x</code>&nbsp;<i>xfile(s)</i>]</p>
<dd> An optional list of archive members to be excluded from processing. Since wildcard characters normally match (`/&#8217;) directory separators (for exceptions see the option <code>-W</code>), this option may be used to exclude any files that are in subdirectories. For example, &#8220;unzip foo *.[ch] -x */*&#8221; would extract all C source files in the main directory, but none in any subdirectories. Without the <code>-x</code> option, all C source files in all directories within the zipfile would be extracted.</p>
<dt>[<code>-d</code>&nbsp;<i>exdir</i>]</p>
<dd> An optional directory to which to extract files. By default, all files and subdirectories are recreated in the current directory; the <code>-d</code> option allows extraction in an arbitrary directory (always assuming one has permission to write to the directory). This option need not appear at the end of the command line; it is also accepted before the zipfile specification (with the normal options), immediately after the zipfile specification, or between the <i>file(s)</i> and the <code>-x</code> option. The option and directory may be concatenated without any white space between them, but note that this may cause normal shell behavior to be suppressed. In particular, &#8220;-d&nbsp;~&#8221; (tilde) is expanded by Unix C shells into the name of the user&#8217;s home directory, but &#8220;-d~&#8221; is treated as a literal subdirectory &#8220;<code>~</code>&#8221; of the current directory.</dl>
<h2>OPTIONS</h2>
<p> Note that, in order to support obsolescent hardware, <i>unzip</i>&#8216;s usage screen is limited to 22 or 23 lines and should therefore be considered only a reminder of the basic <i>unzip</i> syntax rather than an exhaustive list of all possible flags. The exhaustive list follows:</p>
<dl>
<dt><code>-Z</code></p>
<dd> <i><a href="/docs/linux/man/1-zipinfo/">zipinfo</a></i>(1) mode. If the first option on the command line is <code>-Z</code>, the remaining options are taken to be <i><a href="/docs/linux/man/1-zipinfo/">zipinfo</a></i>(1) options. See the appropriate manual page for a description of these options.</p>
<dt><code>-A</code></p>
<dd> [OS/2, Unix DLL] print extended help for the DLL&#8217;s programming interface (API).</p>
<dt><code>-c</code></p>
<dd> extract files to stdout/screen (&#8220;CRT&#8221;). This option is similar to the <code>-p</code> option except that the name of each file is printed as it is extracted, the <code>-a</code> option is allowed, and ASCII-EBCDIC conversion is automatically performed if appropriate. This option is not listed in the <i>unzip</i> usage screen.</p>
<dt><code>-f</code></p>
<dd> freshen existing files, i.e., extract only those files that already exist on disk and that are newer than the disk copies. By default <i>unzip</i> queries before overwriting, but the <code>-o</code> option may be used to suppress the queries. Note that under many operating systems, the TZ (timezone) environment variable must be set correctly in order for <code>-f</code> and <code>-u</code> to work properly (under Unix the variable is usually set automatically). The reasons for this are somewhat subtle but have to do with the differences between DOS-format file times (always local time) and Unix-format times (always in GMT/UTC) and the necessity to compare the two. A typical TZ value is &#8220;PST8PDT&#8221; (US Pacific time with automatic adjustment for Daylight Savings Time or &#8220;summer time&#8221;).</p>
<dt><code>-l</code></p>
<dd> list archive files (short format). The names, uncompressed file sizes and modification dates and times of the specified files are printed, along with totals for all files specified. If UnZip was compiled with OS2_EAS defined, the <code>-l</code> option also lists columns for the sizes of stored OS/2 extended attributes (EAs) and OS/2 access control lists (ACLs). In addition, the zipfile comment and individual file comments (if any) are displayed. If a file was archived from a single-case file system (for example, the old MS-DOS FAT file system) and the <code>-L</code> option was given, the filename is converted to lowercase and is prefixed with a caret (^).</p>
<dt><code>-p</code></p>
<dd> extract files to pipe (stdout). Nothing but the file data is sent to stdout, and the files are always extracted in binary format, just as they are stored (no conversions).</p>
<dt><code>-t</code></p>
<dd> test archive files. This option extracts each specified file in memory and compares the CRC (cyclic redundancy check, an enhanced checksum) of the expanded file with the original file&#8217;s stored CRC value.</p>
<dt><code>-T</code></p>
<dd> [most OSes] set the timestamp on the archive(s) to that of the newest file in each one. This corresponds to <i>zip</i>&#8216;s <code>-go</code> option except that it can be used on wildcard zipfiles (e.g., &#8220;unzip -T \*.zip&#8221;) and is much faster.</p>
<dt><code>-u</code></p>
<dd> update existing files and create new ones if needed. This option performs the same function as the <code>-f</code> option, extracting (with query) files that are newer than those with the same name on disk, and in addition it extracts those files that do not already exist on disk. See <code>-f</code> above for information on setting the timezone properly.</p>
<dt><code>-v</code></p>
<dd> list archive files (verbose format) or show diagnostic version info. This option has evolved and now behaves as both an option and a modifier. As an option it has two purposes: when a zipfile is specified with no other options, <code>-v</code> lists archive files verbosely, adding to the basic <code>-l</code> info the compression method, compressed size, compression ratio and 32-bit CRC. In contrast to most of the competing utilities, <i>unzip</i> removes the 12 additional header bytes of encrypted entries from the compressed size numbers. Therefore, compressed size and compression ratio figures are independent of the entry&#8217;s encryption status and show the correct compression performance. (The complete size of the encrypted compressed data stream for zipfile entries is reported by the more verbose <i><a href="/docs/linux/man/1-zipinfo/">zipinfo</a></i>(1) reports, see the separate manual.) When no zipfile is specified (that is, the complete command is simply &#8220;unzip -v&#8221;), a diagnostic screen is printed. In addition to the normal header with release date and version, <i>unzip</i> lists the home Info-ZIP ftp site and where to find a list of other ftp and non-ftp sites; the target operating system for which it was compiled, as well as (possibly) the hardware on which it was compiled, the compiler and version used, and the compilation date; any special compilation options that might affect the program&#8217;s operation (see also <code>DECRYPTION</code> below); and any options stored in environment variables that might do the same (see <code>ENVIRONMENT OPTIONS</code> below). As a modifier it works in conjunction with other options (e.g., <code>-t</code>) to produce more verbose or debugging output; this is not yet fully implemented but will be in future releases.</p>
<dt><code>-z</code></p>
<dd> display only the archive comment.</dl>
<h2>MODIFIERS</h2>
<dl>
<dt><code>-a</code></p>
<dd> convert text files. Ordinarily all files are extracted exactly as they are stored (as &#8220;binary&#8221; files). The <code>-a</code> option causes files identified by <i>zip</i> as text files (those with the `t&#8217; label in <i>zipinfo</i> listings, rather than `b&#8217;) to be automatically extracted as such, converting line endings, end-of-file characters and the character set itself as necessary. (For example, Unix files use line feeds (LFs) for end-of-line (EOL) and have no end-of-file (EOF) marker; Macintoshes use carriage returns (CRs) for EOLs; and most PC operating systems use CR+LF for EOLs and control-Z for EOF. In addition, IBM mainframes and the Michigan Terminal System use EBCDIC rather than the more common ASCII character set, and NT supports Unicode.) Note that <i>zip</i>&#8216;s identification of text files is by no means perfect; some &#8220;text&#8221; files may actually be binary and vice versa. <i>unzip</i> therefore prints &#8220;[text]&#8221; or &#8220;[binary]&#8221; as a visual check for each file it extracts when using the <code>-a</code> option. The <code>-aa</code> option forces all files to be extracted as text, regardless of the supposed file type. On VMS, see also <code>-S</code>.</p>
<dt><code>-b</code></p>
<dd> [general] treat all files as binary (no text conversions). This is a shortcut for <code>&#8212;a</code>.</p>
<dt><code>-b</code></p>
<dd> [Tandem] force the creation files with filecode type 180 (&#8216;C&#8217;) when extracting Zip entries marked as &quot;text&quot;. (On Tandem, <code>-a</code> is enabled by default, see above).</p>
<dt><code>-b</code></p>
<dd> [VMS] auto-convert binary files (see <code>-a</code> above) to fixed-length, 512-byte record format. Doubling the option (<code>-bb</code>) forces all files to be extracted in this format. When extracting to standard output (<code>-c</code> or <code>-p</code> option in effect), the default conversion of text record delimiters is disabled for binary (<code>-b</code>) resp. all (<code>-bb</code>) files.</p>
<dt><code>-B</code></p>
<dd> [when compiled with UNIXBACKUP defined] save a backup copy of each overwritten file. The backup file is gets the name of the target file with a tilde and optionally a unique sequence number (up to 5 digits) appended. The sequence number is applied whenever another file with the original name plus tilde already exists. When used together with the &quot;overwrite all&quot; option <code>-o</code>, numbered backup files are never created. In this case, all backup files are named as the original file with an appended tilde, existing backup files are deleted without notice. This feature works similarly to the default behavior of <i><a href="/docs/linux/man/1-emacs/">emacs</a></i>(1) in many locations.</p>
<dt>
<dd> Example: the old copy of &#8220;foo&#8221; is renamed to &#8220;foo~&#8221;.</p>
<dt>
<dd> Warning: Users should be aware that the <code>-B</code> option does not prevent loss of existing data under all circumstances. For example, when <i>unzip</i> is run in overwrite-all mode, an existing &#8220;foo~&#8221; file is deleted before <i>unzip</i> attempts to rename &#8220;foo&#8221; to &#8220;foo~&#8221;. When this rename attempt fails (because of a file locks, insufficient privileges, or &#8230;), the extraction of &#8220;foo~&#8221; gets cancelled, but the old backup file is already lost. A similar scenario takes place when the sequence number range for numbered backup files gets exhausted (99999, or 65535 for 16-bit systems). In this case, the backup file with the maximum sequence number is deleted and replaced by the new backup version without notice.</p>
<dt><code>-C</code></p>
<dd> use case-insensitive matching for the selection of archive entries from the command-line list of extract selection patterns. <i>unzip</i>&#8216;s philosophy is &#8220;you get what you ask for&#8221; (this is also responsible for the <code>-L</code>/<code>-U</code> change; see the relevant options below). Because some file systems are fully case-sensitive (notably those under the Unix operating system) and because both ZIP archives and <i>unzip</i> itself are portable across platforms, <i>unzip</i>&#8216;s default behavior is to match both wildcard and literal filenames case-sensitively. That is, specifying &#8220;makefile&#8221; on the command line will <i>only</i> match &#8220;makefile&#8221; in the archive, not &#8220;Makefile&#8221; or &#8220;MAKEFILE&#8221; (and similarly for wildcard specifications). Since this does not correspond to the behavior of many other operating/file systems (for example, OS/2 HPFS, which preserves mixed case but is not sensitive to it), the <code>-C</code> option may be used to force all filename matches to be case-insensitive. In the example above, all three files would then match &#8220;makefile&#8221; (or &#8220;make*&#8221;, or similar). The <code>-C</code> option affects file specs in both the normal file list and the excluded-file list (xlist).</p>
<dt>
<dd> Please note that the <code>-C</code> option does neither affect the search for the zipfile(s) nor the matching of archive entries to existing files on the extraction path. On a case-sensitive file system, <i>unzip</i> will never try to overwrite a file &#8220;FOO&#8221; when extracting an entry &#8220;foo&#8221;!</p>
<dt><code>-D</code></p>
<dd> skip restoration of timestamps for extracted items. Normally, <i>unzip</i> tries to restore all meta-information for extracted items that are supplied in the Zip archive (and do not require privileges or impose a security risk). By specifying <code>-D</code>, <i>unzip</i> is told to suppress restoration of timestamps for directories explicitly created from Zip archive entries. This option only applies to ports that support setting timestamps for directories (currently ATheOS, BeOS, MacOS, OS/2, Unix, VMS, Win32, for other <i>unzip</i> ports, <code>-D</code> has no effect). The duplicated option <code>-DD</code> forces suppression of timestamp restoration for all extracted entries (files and directories). This option results in setting the timestamps for all extracted entries to the current time.</p>
<dt>
<dd> On VMS, the default setting for this option is <code>-D</code> for consistency with the behaviour of BACKUP: file timestamps are restored, timestamps of extracted directories are left at the current time. To enable restoration of directory timestamps, the negated option <code>&#8211;D</code> should be specified. On VMS, the option <code>-D</code> disables timestamp restoration for all extracted Zip archive items. (Here, a single <code>-D</code> on the command line combines with the default <code>-D</code> to do what an explicit <code>-DD</code> does on other systems.)</p>
<dt><code>-E</code></p>
<dd> [MacOS only] display contents of MacOS extra field during restore operation.</p>
<dt><code>-F</code></p>
<dd> [Acorn only] suppress removal of NFS filetype extension from stored filenames.</p>
<dt><code>-F</code></p>
<dd> [non-Acorn systems supporting long filenames with embedded commas, and only if compiled with ACORN_FTYPE_NFS defined] translate filetype information from ACORN RISC OS extra field blocks into a NFS filetype extension and append it to the names of the extracted files. (When the stored filename appears to already have an appended NFS filetype extension, it is replaced by the info from the extra field.)</p>
<dt><code>-i</code></p>
<dd> [MacOS only] ignore filenames stored in MacOS extra fields. Instead, the most compatible filename stored in the generic part of the entry&#8217;s header is used.</p>
<dt><code>-j</code></p>
<dd> junk paths. The archive&#8217;s directory structure is not recreated; all files are deposited in the extraction directory (by default, the current one).</p>
<dt><code>-J</code></p>
<dd> [BeOS only] junk file attributes. The file&#8217;s BeOS file attributes are not restored, just the file&#8217;s data.</p>
<dt><code>-J</code></p>
<dd> [MacOS only] ignore MacOS extra fields. All Macintosh specific info is skipped. Data-fork and resource-fork are restored as separate files.</p>
<dt><code>-K</code></p>
<dd> [AtheOS, BeOS, Unix only] retain SUID/SGID/Tacky file attributes. Without this flag, these attribute bits are cleared for security reasons.</p>
<dt><code>-L</code></p>
<dd> convert to lowercase any filename originating on an uppercase-only operating system or file system. (This was <i>unzip</i>&#8216;s default behavior in releases prior to 5.11; the new default behavior is identical to the old behavior with the <code>-U</code> option, which is now obsolete and will be removed in a future release.) Depending on the archiver, files archived under single-case file systems (VMS, old MS-DOS FAT, etc.) may be stored as all-uppercase names; this can be ugly or inconvenient when extracting to a case-preserving file system such as OS/2 HPFS or a case-sensitive one such as under Unix. By default <i>unzip</i> lists and extracts such filenames exactly as they&#8217;re stored (excepting truncation, conversion of unsupported characters, etc.); this option causes the names of all files from certain systems to be converted to lowercase. The <code>-LL</code> option forces conversion of every filename to lowercase, regardless of the originating file system.</p>
<dt><code>-M</code></p>
<dd> pipe all output through an internal pager similar to the Unix <i><a href="/docs/linux/man/1-more/">more</a></i>(1) command. At the end of a screenful of output, <i>unzip</i> pauses with a &#8220;&#8211;More&#8211;&#8221; prompt; the next screenful may be viewed by pressing the Enter (Return) key or the space bar. <i>unzip</i> can be terminated by pressing the &#8220;q&#8221; key and, on some systems, the Enter/Return key. Unlike Unix <i><a href="/docs/linux/man/1-more/">more</a></i>(1), there is no forward-searching or editing capability. Also, <i>unzip</i> doesn&#8217;t notice if long lines wrap at the edge of the screen, effectively resulting in the printing of two or more lines and the likelihood that some text will scroll off the top of the screen before being viewed. On some systems the number of available lines on the screen is not detected, in which case <i>unzip</i> assumes the height is 24 lines.</p>
<dt><code>-n</code></p>
<dd> never overwrite existing files. If a file already exists, skip the extraction of that file without prompting. By default <i>unzip</i> queries before extracting any file that already exists; the user may choose to overwrite only the current file, overwrite all files, skip extraction of the current file, skip extraction of all existing files, or rename the current file.</p>
<dt><code>-N</code></p>
<dd> [Amiga] extract file comments as Amiga filenotes. File comments are created with the -c option of <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), or with the -N option of the Amiga port of <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), which stores filenotes as comments.</p>
<dt><code>-o</code></p>
<dd> overwrite existing files without prompting. This is a dangerous option, so use it with care. (It is often used with <code>-f</code>, however, and is the only way to overwrite directory EAs under OS/2.)</p>
<dt><code>-P</code>&nbsp;<i>password</i></p>
<dd> use <i>password</i> to decrypt encrypted zipfile entries (if any). <code>THIS IS INSECURE!</code> Many multi-user operating systems provide ways for any user to see the current command line of any other user; even on stand-alone systems there is always the threat of over-the-shoulder peeking. Storing the plaintext password as part of a command line in an automated script is even worse. Whenever possible, use the non-echoing, interactive prompt to enter passwords. (And where security is truly important, use strong encryption such as Pretty Good Privacy instead of the relatively weak encryption provided by standard zipfile utilities.)</p>
<dt><code>-q</code></p>
<dd> perform operations quietly (<code>-qq</code> = even quieter). Ordinarily <i>unzip</i> prints the names of the files it&#8217;s extracting or testing, the extraction methods, any file or zipfile comments that may be stored in the archive, and possibly a summary when finished with each archive. The <code>-q</code>[<code>q</code>] options suppress the printing of some or all of these messages.</p>
<dt><code>-s</code></p>
<dd> [OS/2, NT, MS-DOS] convert spaces in filenames to underscores. Since all PC operating systems allow spaces in filenames, <i>unzip</i> by default extracts filenames with spaces intact (e.g., &#8220;EA DATA. SF&#8221;). This can be awkward, however, since MS-DOS in particular does not gracefully support spaces in filenames. Conversion of spaces to underscores can eliminate the awkwardness in some cases.</p>
<dt><code>-S</code></p>
<dd> [VMS] convert text files (<code>-a</code>, <code>-aa</code>) into Stream_LF record format, instead of the text-file default, variable-length record format. (Stream_LF is the default record format of VMS <i>unzip</i>. It is applied unless conversion (<code>-a</code>, <code>-aa</code> and/or <code>-b</code>, <code>-bb</code>) is requested or a VMS-specific entry is processed.)</p>
<dt><code>-U</code></p>
<dd> [UNICODE_SUPPORT only] modify or disable UTF-8 handling. When UNICODE_SUPPORT is available, the option <code>-U</code> forces <i>unzip</i> to escape all non-ASCII characters from UTF-8 coded filenames as &#8220;#Uxxxx&#8221; (for UCS-2 characters, or &#8220;#Lxxxxxx&#8221; for unicode codepoints needing 3 octets). This option is mainly provided for debugging purpose when the fairly new UTF-8 support is suspected to mangle up extracted filenames.</p>
<dt>
<dd> The option <code>-UU</code> allows to entirely disable the recognition of UTF-8 encoded filenames. The handling of filename codings within <i>unzip</i> falls back to the behaviour of previous versions.</p>
<dt>
<dd> [old, obsolete usage] leave filenames uppercase if created under MS-DOS, VMS, etc. See <code>-L</code> above.</p>
<dt><code>-V</code></p>
<dd> retain (VMS) file version numbers. VMS files can be stored with a version number, in the format file.ext;##. By default the &#8220;;##&#8221; version numbers are stripped, but this option allows them to be retained. (On file systems that limit filenames to particularly short lengths, the version numbers may be truncated or stripped regardless of this option.)</p>
<dt><code>-W</code></p>
<dd> [only when WILD_STOP_AT_DIR compile-time option enabled] modifies the pattern matching routine so that both `?&#8217; (single-char wildcard) and `*&#8217; (multi-char wildcard) do not match the directory separator character `/&#8217;. (The two-character sequence &#8220;**&#8221; acts as a multi-char wildcard that includes the directory separator in its matched characters.) Examples:</dl>
<pre>
    &quot;*.c&quot; matches &quot;foo.c&quot; but not &quot;mydir/foo.c&quot;
    &quot;**.c&quot; matches both &quot;foo.c&quot; and &quot;mydir/foo.c&quot;
    &quot;*/*.c&quot; matches &quot;bar/foo.c&quot; but not &quot;baz/bar/foo.c&quot;
    &quot;??*/*&quot; matches &quot;ab/foo&quot; and &quot;abc/foo&quot;
            but not &quot;a/foo&quot; or &quot;a/b/foo&quot;
</pre>
<dl>
<dt>
<dd> This modified behaviour is equivalent to the pattern matching style used by the shells of some of UnZip&#8217;s supported target OSs (one example is Acorn RISC OS). This option may not be available on systems where the Zip archive&#8217;s internal directory separator character `/&#8217; is allowed as regular character in native operating system filenames. (Currently, UnZip uses the same pattern matching rules for both wildcard zipfile specifications and zip entry selection patterns in most ports. For systems allowing `/&#8217; as regular filename character, the -W option would not work as expected on a wildcard zipfile specification.)</p>
<dt><code>-X</code></p>
<dd> [VMS, Unix, OS/2, NT, Tandem] restore owner/protection info (UICs and ACL entries) under VMS, or user and group info (UID/GID) under Unix, or access control lists (ACLs) under certain network-enabled versions of OS/2 (Warp Server with IBM LAN Server/Requester 3.0 to 5.0; Warp Connect with IBM Peer 1.0), or security ACLs under Windows NT. In most cases this will require special system privileges, and doubling the option (<code>-XX</code>) under NT instructs <i>unzip</i> to use privileges for extraction; but under Unix, for example, a user who belongs to several groups can restore files owned by any of those groups, as long as the user IDs match his or her own. Note that ordinary file attributes are always restored&#8211;this option applies only to optional, extra ownership info available on some operating systems. [NT&#8217;s access control lists do not appear to be especially compatible with OS/2&#8217;s, so no attempt is made at cross-platform portability of access privileges. It is not clear under what conditions this would ever be useful anyway.]</p>
<dt><code>-Y</code></p>
<dd> [VMS] treat archived file name endings of &#8220;.nnn&#8221; (where &#8220;nnn&#8221; is a decimal number) as if they were VMS version numbers (&#8220;;nnn&#8221;). (The default is to treat them as file types.) Example: </p>
<pre>
     &quot;a.b.3&quot; -&gt; &quot;a.b;3&quot;.
</pre>
<dt><code>-$</code></p>
<dd> [MS-DOS, OS/2, NT] restore the volume label if the extraction medium is removable (e.g., a diskette). Doubling the option (<code>-$$</code>) allows fixed media (hard disks) to be labelled as well. By default, volume labels are ignored.</p>
<dt><code>-/</code>&nbsp;<i>extensions</i></p>
<dd> [Acorn only] overrides the extension list supplied by Unzip$Ext environment variable. During extraction, filename extensions that match one of the items in this extension list are swapped in front of the base name of the extracted file.</p>
<dt><code>-:</code></p>
<dd> [all but Acorn, VM/CMS, MVS, Tandem] allows to extract archive members into locations outside of the current &#8220; extraction root folder&#8221;. For security reasons, <i>unzip</i> normally removes &#8220;parent dir&#8221; path components (&#8220;../&#8221;) from the names of extracted file. This safety feature (new for version 5.50) prevents <i>unzip</i> from accidentally writing files to &#8220;sensitive&#8221; areas outside the active extraction folder tree head. The <code>-:</code> option lets <i>unzip</i> switch back to its previous, more liberal behaviour, to allow exact extraction of (older) archives that used &#8220;../&#8221; components to create multiple directory trees at the level of the current extraction folder. This option does not enable writing explicitly to the root directory (&#8220;/&#8221;). To achieve this, it is necessary to set the extraction target folder to root (e.g. <code>-d / </code>). However, when the <code>-:</code> option is specified, it is still possible to implicitly write to the root directory by specifying enough &#8220;../&#8221; path components within the zip archive. Use this option with extreme caution.</p>
<dt><code>-^</code></p>
<dd> [Unix only] allow control characters in names of extracted ZIP archive entries. On Unix, a file name may contain any (8-bit) character code with the two exception &#8216;/&#8217; (directory delimiter) and NUL (0x00, the C string termination indicator), unless the specific file system has more restrictive conventions. Generally, this allows to embed ASCII control characters (or even sophisticated control sequences) in file names, at least on &#8216;native&#8217; Unix file systems. However, it may be highly suspicious to make use of this Unix &quot;feature&quot;. Embedded control characters in file names might have nasty side effects when displayed on screen by some listing code without sufficient filtering. And, for ordinary users, it may be difficult to handle such file names (e.g. when trying to specify it for open, copy, move, or delete operations). Therefore, <i>unzip</i> applies a filter by default that removes potentially dangerous control characters from the extracted file names. The <code>-^</code> option allows to override this filter in the rare case that embedded filename control characters are to be intentionally restored.</p>
<dt><code>-2</code></p>
<dd> [VMS] force unconditionally conversion of file names to ODS2-compatible names. The default is to exploit the destination file system, preserving case and extended file name characters on an ODS5 destination file system; and applying the ODS2-compatibility file name filtering on an ODS2 destination file system.</dl>
<h2>ENVIRONMENT OPTIONS</h2>
<p> <i>unzip</i>&#8216;s default behavior may be modified via options placed in an environment variable. This can be done with any option, but it is probably most useful with the <code>-a</code>, <code>-L</code>, <code>-C</code>, <code>-q</code>, <code>-o</code>, or <code>-n</code> modifiers: make <i>unzip</i> auto-convert text files by default, make it convert filenames from uppercase systems to lowercase, make it match names case-insensitively, make it quieter, or make it always overwrite or never overwrite files as it extracts them. For example, to make <i>unzip</i> act as quietly as possible, only reporting errors, one would use one of the following commands:</p>
<dl>
<dt>
&nbsp;<wbr>&nbsp;Unix Bourne shell:</p>
<dd> UNZIP=-qq; export UNZIP</p>
<dt>
&nbsp;<wbr>&nbsp;Unix C shell:</p>
<dd> setenv UNZIP -qq</p>
<dt>
&nbsp;<wbr>&nbsp;OS/2 or MS-DOS:</p>
<dd> set UNZIP=-qq</p>
<dt>
&nbsp;<wbr>&nbsp;VMS&nbsp;(quotes for&nbsp;<i>lowercase</i>):</p>
<dd> define UNZIP_OPTS &quot;-qq&quot;</dl>
<p> Environment options are, in effect, considered to be just like any other command-line options, except that they are effectively the first options on the command line. To override an environment option, one may use the &#8220;minus operator&#8221; to remove it. For instance, to override one of the quiet-flags in the example above, use the command </p>
<pre>
unzip --q[<i>other options</i>] zipfile
</pre>
<p> The first hyphen is the normal switch character, and the second is a minus sign, acting on the q option. Thus the effect here is to cancel one quantum of quietness. To cancel both quiet flags, two (or more) minuses may be used: </p>
<pre>
unzip -t--q zipfile
unzip ---qt zipfile
</pre>
<p> (the two are equivalent). This may seem awkward or confusing, but it is reasonably intuitive: just ignore the first hyphen and go from there. It is also consistent with the behavior of Unix <i><a href="/docs/linux/man/1-nice/">nice</a></i>(1). </p>
<p> As suggested by the examples above, the default variable names are UNZIP_OPTS for VMS (where the symbol used to install <i>unzip</i> as a foreign command would otherwise be confused with the environment variable), and UNZIP for all other operating systems. For compatibility with <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), UNZIPOPT is also accepted (don&#8217;t ask). If both UNZIP and UNZIPOPT are defined, however, UNZIP takes precedence. <i>unzip</i>&#8216;s diagnostic option (<code>-v</code> with no zipfile name) can be used to check the values of all four possible <i>unzip</i> and <i>zipinfo</i> environment variables. </p>
<p> The timezone variable (TZ) should be set according to the local timezone in order for the <code>-f</code> and <code>-u</code> to operate correctly. See the description of <code>-f</code> above for details. This variable may also be necessary to get timestamps of extracted files to be set correctly. The WIN32 (Win9x/ME/NT4/2K/XP/2K3) port of <i>unzip</i> gets the timezone configuration from the registry, assuming it is correctly set in the Control Panel. The TZ variable is ignored for this port.</p>
<h2>DECRYPTION</h2>
<p> Encrypted archives are fully supported by Info-ZIP software, but due to United States export restrictions, de-/encryption support might be disabled in your compiled binary. However, since spring 2000, US export restrictions have been liberated, and our source archives do now include full crypt code. In case you need binary distributions with crypt support enabled, see the file &#8220;WHERE&#8221; in any Info-ZIP source or binary distribution for locations both inside and outside the US. </p>
<p> Some compiled versions of <i>unzip</i> may not support decryption. To check a version for crypt support, either attempt to test or extract an encrypted archive, or else check <i>unzip</i>&#8216;s diagnostic screen (see the <code>-v</code> option above) for &#8220;[decryption]&#8221; as one of the special compilation options. </p>
<p> As noted above, the <code>-P</code> option may be used to supply a password on the command line, but at a cost in security. The preferred decryption method is simply to extract normally; if a zipfile member is encrypted, <i>unzip</i> will prompt for the password without echoing what is typed. <i>unzip</i> continues to use the same password as long as it appears to be valid, by testing a 12-byte header on each file. The correct password will always check out against the header, but there is a 1-in-256 chance that an incorrect password will as well. (This is a security feature of the PKWARE zipfile format; it helps prevent brute-force attacks that might otherwise gain a large speed advantage by testing only the header.) In the case that an incorrect password is given but it passes the header test anyway, either an incorrect CRC will be generated for the extracted data or else <i>unzip</i> will fail during the extraction because the &#8220;decrypted&#8221; bytes do not constitute a valid compressed data stream. </p>
<p> If the first password fails the header check on some file, <i>unzip</i> will prompt for another password, and so on until all files are extracted. If a password is not known, entering a null password (that is, just a carriage return or &#8220;Enter&#8221;) is taken as a signal to skip all further prompting. Only unencrypted files in the archive(s) will thereafter be extracted. (In fact, that&#8217;s not quite true; older versions of <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1) and <i><a href="/docs/linux/man/1-zipcloak/">zipcloak</a></i>(1) allowed null passwords, so <i>unzip</i> checks each encrypted file to see if the null password works. This may result in &#8220;false positives&#8221; and extraction errors, as noted above.) </p>
<p> Archives encrypted with 8-bit passwords (for example, passwords with accented European characters) may not be portable across systems and/or other archivers. This problem stems from the use of multiple encoding methods for such characters, including Latin-1 (ISO 8859-1) and OEM code page 850. DOS <i>PKZIP</i> 2.04g uses the OEM code page; Windows <i>PKZIP</i> 2.50 uses Latin-1 (and is therefore incompatible with DOS <i>PKZIP</i>); Info-ZIP uses the OEM code page on DOS, OS/2 and Win3.x ports but ISO coding (Latin-1 etc.) everywhere else; and Nico Mak&#8217;s <i>WinZip</i> 6.x does not allow 8-bit passwords at all. <i>UnZip</i> 5.3 (or newer) attempts to use the default character set first (e.g., Latin-1), followed by the alternate one (e.g., OEM code page) to test passwords. On EBCDIC systems, if both of these fail, EBCDIC encoding will be tested as a last resort. (EBCDIC is not tested on non-EBCDIC systems, because there are no known archivers that encrypt using EBCDIC encoding.) ISO character encodings other than Latin-1 are not supported. The new addition of (partially) Unicode (resp. UTF-8) support in <i>UnZip</i> 6.0 has not yet been adapted to the encryption password handling in <i>unzip</i>. On systems that use UTF-8 as native character encoding, <i>unzip</i> simply tries decryption with the native UTF-8 encoded password; the built-in attempts to check the password in translated encoding have not yet been adapted for UTF-8 support and will consequently fail.</p>
<h2>EXAMPLES</h2>
<p> To use <i>unzip</i> to extract all members of the archive <i>letters.zip</i> into the current directory and subdirectories below it, creating any subdirectories as necessary: </p>
<pre>
unzip letters
</pre>
<p> To extract all members of <i>letters.zip</i> into the current directory only: </p>
<pre>
unzip -j letters
</pre>
<p> To test <i>letters.zip</i>, printing only a summary message indicating whether the archive is OK or not: </p>
<pre>
unzip -tq letters
</pre>
<p> To test <i>all</i> zipfiles in the current directory, printing only the summaries: </p>
<pre>
unzip -tq \*.zip
</pre>
<p> (The backslash before the asterisk is only required if the shell expands wildcards, as in Unix; double quotes could have been used instead, as in the source examples below.)&nbsp;<wbr>&nbsp;To extract to standard output all members of <i>letters.zip</i> whose names end in <i>.tex</i>, auto-converting to the local end-of-line convention and piping the output into <i><a href="/docs/linux/man/1-more/">more</a></i>(1): </p>
<pre>
unzip -ca letters \*.tex | more
</pre>
<p> To extract the binary file <i>paper1.dvi</i> to standard output and pipe it to a printing program: </p>
<pre>
unzip -p articles paper1.dvi | dvips
</pre>
<p> To extract all FORTRAN and C source files&#8211;*.f, *.c, *.h, and Makefile&#8211;into the /tmp directory: </p>
<pre>
unzip source.zip &quot;*.[fch]&quot; Makefile -d /tmp
</pre>
<p> (the double quotes are necessary only in Unix and only if globbing is turned on). To extract all FORTRAN and C source files, regardless of case (e.g., both *.c and *.C, and any makefile, Makefile, MAKEFILE or similar): </p>
<pre>
unzip -C source.zip &quot;*.[fch]&quot; makefile -d /tmp
</pre>
<p> To extract any such files but convert any uppercase MS-DOS or VMS names to lowercase and convert the line-endings of all of the files to the local standard (without respect to any files that might be marked &#8220;binary&#8221;): </p>
<pre>
unzip -aaCL source.zip &quot;*.[fch]&quot; makefile -d /tmp
</pre>
<p> To extract only newer versions of the files already in the current directory, without querying (NOTE: be careful of unzipping in one timezone a zipfile created in another&#8211;ZIP archives other than those created by Zip 2.1 or later contain no timezone information, and a &#8220;newer&#8221; file from an eastern timezone may, in fact, be older): </p>
<pre>
unzip -fo sources
</pre>
<p> To extract newer versions of the files already in the current directory and to create any files not already there (same caveat as previous example): </p>
<pre>
unzip -uo sources
</pre>
<p> To display a diagnostic screen showing which <i>unzip</i> and <i>zipinfo</i> options are stored in environment variables, whether decryption support was compiled in, the compiler with which <i>unzip</i> was compiled, etc.: </p>
<pre>
unzip -v
</pre>
<p> In the last five examples, assume that UNZIP or UNZIP_OPTS is set to -q. To do a singly quiet listing: </p>
<pre>
unzip -l file.zip
</pre>
<p> To do a doubly quiet listing: </p>
<pre>
unzip -ql file.zip
</pre>
<p> (Note that the &#8220;.zip&#8221; is generally not necessary.) To do a standard listing: </p>
<pre>
unzip --ql file.zip
</pre>
<p> or </p>
<pre>
unzip -l-q file.zip
</pre>
<p> or </p>
<pre>
unzip -l--q file.zip
</pre>
<p> (Extra minuses in options don&#8217;t hurt.)</p>
<h2>TIPS</h2>
<p> The current maintainer, being a lazy sort, finds it very useful to define a pair of aliases: tt for &#8220;unzip -tq&#8221; and ii for &#8220;unzip -Z&#8221; (or &#8220;zipinfo&#8221;). One may then simply type &#8220;tt zipfile&#8221; to test an archive, something that is worth making a habit of doing. With luck <i>unzip</i> will report &#8220;No errors detected in compressed data of zipfile.zip,&#8221; after which one may breathe a sigh of relief. </p>
<p> The maintainer also finds it useful to set the UNZIP environment variable to &#8220;-aL&#8221; and is tempted to add &#8220;-C&#8221; as well. His ZIPINFO variable is set to &#8220;-z&#8221;.</p>
<h2>DIAGNOSTICS</h2>
<p> The exit status (or error level) approximates the exit codes defined by PKWARE and takes on the following values, except under VMS:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> normal; no errors or warnings detected.</p>
<dt>1</p>
<dd> one or more warning errors were encountered, but processing completed successfully anyway. This includes zipfiles where one or more files was skipped due to unsupported compression method or encryption with an unknown password.</p>
<dt>2</p>
<dd> a generic error in the zipfile format was detected. Processing may have completed successfully anyway; some broken zipfiles created by other archivers have simple work-arounds.</p>
<dt>3</p>
<dd> a severe error in the zipfile format was detected. Processing probably failed immediately.</p>
<dt>4</p>
<dd> <i>unzip</i> was unable to allocate memory for one or more buffers during program initialization.</p>
<dt>5</p>
<dd> <i>unzip</i> was unable to allocate memory or unable to obtain a tty to read the decryption password(s).</p>
<dt>6</p>
<dd> <i>unzip</i> was unable to allocate memory during decompression to disk.</p>
<dt>7</p>
<dd> <i>unzip</i> was unable to allocate memory during in-memory decompression.</p>
<dt>8</p>
<dd> [currently not used]</p>
<dt>9</p>
<dd> the specified zipfiles were not found.</p>
<dt>10</p>
<dd> invalid options were specified on the command line.</p>
<dt>11</p>
<dd> no matching files were found.</p>
<dt>50</p>
<dd> the disk is (or was) full during extraction.</p>
<dt>51</p>
<dd> the end of the ZIP archive was encountered prematurely.</p>
<dt>80</p>
<dd> the user aborted <i>unzip</i> prematurely with control-C (or similar)</p>
<dt>81</p>
<dd> testing or extraction of one or more files failed due to unsupported compression methods or unsupported decryption.</p>
<dt>82</p>
<dd> no files were found due to bad decryption password(s). (If even one file is successfully processed, however, the exit status is 1.)</dl>
</dl>
<p> VMS interprets standard Unix (or PC) return values as other, scarier-looking things, so <i>unzip</i> instead maps them into VMS-style status codes. The current mapping is as follows: 1 (success) for normal exit, 0x7fff0001 for warning errors, and (0x7fff000? + 16*normal_unzip_exit_status) for all other errors, where the `?&#8217; is 2 (error) for <i>unzip</i> values 2, 9-11 and 80-82, and 4 (fatal error) for the remaining ones (3-8, 50, 51). In addition, there is a compilation option to expand upon this behavior: defining RETURN_CODES results in a human-readable explanation of what the error status means.</p>
<h2>BUGS</h2>
<p> Multi-part archives are not yet supported, except in conjunction with <i>zip</i>. (All parts must be concatenated together in order, and then &#8220;zip -F&#8221; (for <i>zip 2.x</i>) or &#8220;zip -FF&#8221; (for <i>zip 3.x</i>) must be performed on the concatenated archive in order to &#8220;fix&#8221; it. Also, <i>zip 3.0</i> and later can combine multi-part (split) archives into a combined single-file archive using &#8220;zip -s- inarchive -O outarchive&#8221;. See the <i>zip 3</i> manual page for more information.) This will definitely be corrected in the next major release. </p>
<p> Archives read from standard input are not yet supported, except with <i>funzip</i> (and then only the first member of the archive can be extracted). </p>
<p> Archives encrypted with 8-bit passwords (e.g., passwords with accented European characters) may not be portable across systems and/or other archivers. See the discussion in <code>DECRYPTION</code> above. </p>
<p> <i>unzip</i>&#8216;s <code>-M</code> (&#8220;more&#8221;) option tries to take into account automatic wrapping of long lines. However, the code may fail to detect the correct wrapping locations. First, TAB characters (and similar control sequences) are not taken into account, they are handled as ordinary printable characters. Second, depending on the actual system / OS port, <i>unzip</i> may not detect the true screen geometry but rather rely on &quot;commonly used&quot; default dimensions. The correct handling of tabs would require the implementation of a query for the actual tabulator setup on the output console. </p>
<p> Dates, times and permissions of stored directories are not restored except under Unix. (On Windows NT and successors, timestamps are now restored.) </p>
<p> [MS-DOS] When extracting or testing files from an archive on a defective floppy diskette, if the &#8220;Fail&#8221; option is chosen from DOS&#8217;s &#8220;Abort, Retry, Fail?&#8221; message, older versions of <i>unzip</i> may hang the system, requiring a reboot. This problem appears to be fixed, but control-C (or control-Break) can still be used to terminate <i>unzip</i>. </p>
<p> Under DEC Ultrix, <i>unzip</i> would sometimes fail on long zipfiles (bad CRC, not always reproducible). This was apparently due either to a hardware bug (cache memory) or an operating system bug (improper handling of page faults?). Since Ultrix has been abandoned in favor of Digital Unix (OSF/1), this may not be an issue anymore. </p>
<p> [Unix] Unix special files such as FIFO buffers (named pipes), block devices and character devices are not restored even if they are somehow represented in the zipfile, nor are hard-linked files relinked. Basically the only file types restored by <i>unzip</i> are regular files, directories and symbolic (soft) links. </p>
<p> [OS/2] Extended attributes for existing directories are only updated if the <code>-o</code> (&#8220;overwrite all&#8221;) option is given. This is a limitation of the operating system; because directories only have a creation time associated with them, <i>unzip</i> has no way to determine whether the stored attributes are newer or older than those on disk. In practice this may mean a two-pass approach is required: first unpack the archive normally (with or without freshening/updating existing files), then overwrite just the directory entries (e.g., &#8220;unzip -o foo */&#8221;). </p>
<p> [VMS] When extracting to another directory, only the <i>[.foo]</i> syntax is accepted for the <code>-d</code> option; the simple Unix <i>foo</i> syntax is silently ignored (as is the less common VMS <i>foo.dir</i> syntax). </p>
<p> [VMS] When the file being extracted already exists, <i>unzip</i>&#8216;s query only allows skipping, overwriting or renaming; there should additionally be a choice for creating a new version of the file. In fact, the &#8220;overwrite&#8221; choice does create a new version; the old version is not overwritten or deleted.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-funzip/">funzip</a></i>(1), <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), <i><a href="/docs/linux/man/1-zipcloak/">zipcloak</a></i>(1), <i><a href="/docs/linux/man/1-zipgrep/">zipgrep</a></i>(1), <i><a href="/docs/linux/man/1-zipinfo/">zipinfo</a></i>(1), <i><a href="/docs/linux/man/1-zipnote/">zipnote</a></i>(1), <i><a href="/docs/linux/man/1-zipsplit/">zipsplit</a></i>(1)</p>
<h2>URL</h2>
<p> The Info-ZIP home page is currently at </p>
<pre>
<a rel="nofollow" href="http://www.info-zip.org/pub/infozip/">http://www.info-zip.org/pub/infozip/</a>
</pre>
<p> or </p>
<pre>
<a href="ftp://ftp.info-zip.org/pub/infozip/">ftp://ftp.info-zip.org/pub/infozip/</a> .
</pre>
<h2>AUTHORS</h2>
<p> The primary Info-ZIP authors (current semi-active members of the Zip-Bugs workgroup) are: Ed Gordon (Zip, general maintenance, shared code, Zip64, Win32, Unix, Unicode); Christian Spieler (UnZip maintenance coordination, VMS, MS-DOS, Win32, shared code, general Zip and UnZip integration and optimization); Onno van der Linden (Zip); Mike White (Win32, Windows GUI, Windows DLLs); Kai Uwe Rommel (OS/2, Win32); Steven M. Schweda (VMS, Unix, support of new features); Paul Kienitz (Amiga, Win32, Unicode); Chris Herborth (BeOS, QNX, Atari); Jonathan Hudson (SMS/QDOS); Sergio Monesi (Acorn RISC OS); Harald Denker (Atari, MVS); John Bush (Solaris, Amiga); Hunter Goatley (VMS, Info-ZIP Site maintenance); Steve Salisbury (Win32); Steve Miller (Windows CE GUI), Johnny Lee (MS-DOS, Win32, Zip64); and Dave Smith (Tandem NSK). </p>
<p> The following people were former members of the Info-ZIP development group and provided major contributions to key parts of the current code: Greg &#8220;Cave Newt&#8221; Roelofs (UnZip, unshrink decompression); Jean-loup Gailly (deflate compression); Mark Adler (inflate decompression, fUnZip). </p>
<p> The author of the original unzip code upon which Info-ZIP&#8217;s was based is Samuel H. Smith; Carl Mascott did the first Unix port; and David P. Kirschbaum organized and led Info-ZIP in its early days with Keith Petersen hosting the original mailing list at WSMR-SimTel20. The full list of contributors to UnZip has grown quite large; please refer to the CONTRIBS file in the UnZip source distribution for a relatively complete version.</p>
<h2>VERSIONS</h2>
<dl>
<dt>v1.2 15 Mar 89</p>
<dd> Samuel H. Smith</p>
<dt>v2.0 &nbsp;9 Sep 89</p>
<dd> Samuel H. Smith</p>
<dt>v2.x fall 1989</p>
<dd> many Usenet contributors</p>
<dt>v3.0 &nbsp;1 May 90</p>
<dd> Info-ZIP (DPK, consolidator)</p>
<dt>v3.1 15 Aug 90</p>
<dd> Info-ZIP (DPK, consolidator)</p>
<dt>v4.0 &nbsp;1 Dec 90</p>
<dd> Info-ZIP (GRR, maintainer)</p>
<dt>v4.1 12 May 91</p>
<dd> Info-ZIP</p>
<dt>v4.2 20 Mar 92</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.0 21 Aug 92</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.01 15 Jan 93</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.1 &nbsp;7 Feb 94</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.11 &nbsp;2 Aug 94</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.12 28 Aug 94</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.2 30 Apr 96</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.3 22 Apr 97</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.31 31 May 97</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.32 &nbsp;3 Nov 97</p>
<dd> Info-ZIP (Zip-Bugs subgroup, GRR)</p>
<dt>v5.4 28 Nov 98</p>
<dd> Info-ZIP (Zip-Bugs subgroup, SPC)</p>
<dt>v5.41 16 Apr 00</p>
<dd> Info-ZIP (Zip-Bugs subgroup, SPC)</p>
<dt>v5.42 14 Jan 01</p>
<dd> Info-ZIP (Zip-Bugs subgroup, SPC)</p>
<dt>v5.5 17 Feb 02</p>
<dd> Info-ZIP (Zip-Bugs subgroup, SPC)</p>
<dt>v5.51 22 May 04</p>
<dd> Info-ZIP (Zip-Bugs subgroup, SPC)</p>
<dt>v5.52 28 Feb 05</p>
<dd> Info-ZIP (Zip-Bugs subgroup, SPC)</p>
<dt>v6.0 20 Apr 09</p>
<dd> Info-ZIP (Zip-Bugs subgroup, SPC) </p>
</dl>
<h2>Index</h2>
