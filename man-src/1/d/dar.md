---
title: "dar(1)"
name: "dar"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dar/"
description: "dar – creates, tests, lists, extracts, compares, merges, isolates dar archives"
---

<h2 class="name">NAME</h2>
<p> dar &#8211; creates, tests, lists, extracts, compares, merges, isolates dar archives </p>
<h2>SYNOPSIS</h2>
<p> dar [-c | -t | -l | -x | -d | -+ | -C] [&lt;path&gt;/]&lt;basename&gt; [&lt;options&gt;] [&lt;user targets&gt;] </p>
<p> dar -h </p>
<p> dar -V</p>
<h2>DESCRIPTION</h2>
<p> <code>dar</code> is a full featured backup tool, aimed for disks (floppy, CD-R(W), DVD-R(W), zip, jazz, hard-disks, usb keys, etc.) and since release 2.4.0 also adapted to tapes. </p>
<p> <code>dar</code> can store a backup in several files (called &quot;slices&quot; in the following) of a given size, eventually pausing or running a user command/script before starting the next slice. This can allow for example, the burning of the last generated slice on a DVD-R(W), Blue-ray Disk, or changing of usb key before continuing on the next one. Like its grand-brother, the great &quot;tar&quot; command, <code>dar</code> may also use compression, at the difference that compression is used inside the archive to be able to have compressed slices of the defined size. </p>
<p> But the most important feature of <code>dar</code> is its ability to make differential and decremental backups. In other words, backups that contain only new files or files that have changed from a backup of reference. Moreover with differential backup, <code>dar</code> also stores files that have been deleted since the backup of reference. Thus, when restoring, first a full backup, then additional differential backups, at each restoration you get the exact state of the filesystem at the time the differential backup was made. And of course, the reference backup may be a full or a differential backup itself, so you can make the same way incremental backups. </p>
<p> <code>dar</code> is the first backup program I know that can also remove files during restoration! By the way, in this document, &quot;archive&quot; and &quot;backup&quot; mean the same thing, and are used interchangeably. </p>
<p> Unlike the <code>tar</code> command, <code>dar</code> has not to read a whole archive nor to stick together the different parts (the slices) to get its contents: dar archive contains a table of contents (aka &quot;catalogue&quot;) located at the end of the archive, so it seeks into the archive forth and backward to extract only the required files, which is much faster than what tar is used to do. The &quot;catalogue&quot; can be copied out of the archive (operation called isolation) to be used as reference for further backup and as backup of the internal catalogue in case of archive corruption. </p>
<p> Dar can also use a sequential reading mode, in which dar acts like tar, just reading byte by byte the whole archive to know its contents and eventually extracting file at each step. In other words, the archive contents is located at both locations, all along the archive used for tar-like behavior suitable for sequential access media (tapes) and at the end for faster access, suitable for random access media (disks). However note that tar archive and dar archive are not compatible. Dar does not know anything about tar archive structure, neither tar knows anything about dar archive structure. So keep using tar if you are used to it or find no advantage in using dar. Note also that the sequential reading mode let you extract data from a partially written archive (those that failed to complete due to a lack of disk space for example). </p>
<p> Dar format is quite robust against corruption: Only the file where the corruption took place in the archive will not be possible to restore. To have the possibility to repair a corrupted archive dar can work with par2 seamlessly just specifying &quot;par2&quot; on command-line (see /etc/darrc). Last a &quot;relax&quot; reading mode is available which let dar to either ignore some incoherence in archive structure, use internal redundant information to overcome data corruption or in last resort asking the user on what to do when some archive structure information is missing (-al option). This relax mode can be used with both sequential and direct access read modes. Note that you should rather use Parchive to protect your data rather than just relying on the &quot;relax&quot; mode, which has to be seen as a the last chance solution. </p>
<p> <code>dar</code> takes care of POSIX Extended Attributes (EA in short) that are used in particular under Linux to carry File Access Control List (FACL) as well as security attributes for SELinux, and also under MacOS X EA they are used to store file forks. EA also have room for user to add any key / value paire to any file, this is known as user EA. These attributes are not specific to any particular filesystem, they exist the same way under ext3/4, HFS+ and any other filesystem. </p>
<p> <code>dar</code> also takes care of Filesystem Specific Attributes (FSA in short) which are, as you can guess, specific to one or several filesystem(s). For example the Birth date of a file exists for HFS+ and NTFS but not for ext2/3/4 filesystem. The immutable attribute exists for ext2/3/4 but not for NTFS while the nodump files does not exists for NTFS but exists for HFS+, ext2/3/4 and many other Unix filesystems. </p>
<p> Sparse files (files with holes that system reports using several hundred gigabytes while they effectively use a few kilobytes on disk) are also well managed by <code>dar:</code> they are detected, stored and restored to filesystem properly. </p>
<p> <code>dar</code> is also able to properly save and restore hard-links </p>
<p> A few words about slice before going deeper in detail: a slice is just a simple file which name is composed of a &quot;basename&quot; followed by a dot, then a number, again a dot and the extension (dar) to form the filename of that slice. On the command line you will never have to give the full file name of a slice, just the basename. The number between the dots is the slice number, which starts from 1 and may be arbitrary large (as large as your system can support the corresponding filename).</p>
<dl>
<dt>Let&#8217;s take an example:</p>
<dd> considering the basename &quot;joe&quot;, dar will make one or several slices during backup process (depending on your choice). The filenames of these slices will be: joe.1.dar joe.2.dar &#8230; joe.10.dar &#8230; etc. If you want to extract, list, or use this backup as reference, you will only have to use the basename, which is the string &quot;joe&quot; in this example.</dl>
<p> The rest of this document is organized that way:</p>
<dl>
<dt>
<dd>
<dl>
<dt>COMMANDS</p>
<dd> The seven actions you can performs with dar</p>
<dt>GENERAL OPTIONS</p>
<dd> A set of options common to all actions</p>
<dt>SAVING, ISOLATING AND MERGING SPECIFIC OPTIONS</p>
<dd> A set of options that are specific to the operation of backup, catalogue isolation and archive merging</p>
<dt>RESTORATION SPECIFIC OPTIONS</p>
<dd> A set of options that are specific to the restoration operation</p>
<dt>TESTING AND DIFFERENCE SPECIFIC OPTIONS</p>
<dd> A set of options that are specific to the operation of archive testing and archive comparison with a filesystem</p>
<dt>LISTING OPTIONS</p>
<dd> A set of options that are specific to archive listing operation</p>
<dt>EXPICIT OPTIONAL ARGUMENTS</p>
<dd> Some system do not allow optional arguments to options, this chapter explain how to overcome this restriction</p>
<dt>EXIT CODES</p>
<dd> List of values <code>dar</code> returns at end of execution. This chapter should be read if you intend to create scripts relying on dar</p>
<dt>SIGNALS</p>
<dd> details the signal and their action on a running dar process</p>
<dt>FILES</p>
<dd> List configuration files that dar checks for</p>
<dt>CONDITIONAL SYNTAX</p>
<dd> Over command line, command and options can be passed to dar thanks to a plain file (known as DCF file). This plain file can also contain a specific syntax that will let you pass an option to dar only under certain situation/condition. This chapter describes this simple syntax and the different available conditions.</p>
<dt>USER TARGETS</p>
<dd> User can add their own conditions known as user targets. This chapter describes what they are and how to use them</p>
<dt>ENVIRONMENT</p>
<dd> Dar may rely on environment variables to look for DCF files and DUC files</dl>
</dl>
<h2>OPTIONS</h2>
<p> <code>COMMANDS:</code> </p>
<p> Only seven commands define what action will be done by dar: Archive creation, archive extraction, archive listing, archive testing, archive comparison with filesystem, catalogue isolation and archive merging. These commands are described here below. </p>
<p> Once defined, a large set of options can be used to modify the way the command is performed. These options are described just after the commands chapter. </p>
<p> <code>Important note:</code> Not all system actually support long options (Solaris, FreeBSD, &#8230;). For example &#8211;create will not be available on these systems, and you will have to use -c instead. In the same way, not all system do support optional arguments (FreeBSD without GNU getopt for example), you then need to explicitly give the argument, for example in place of &quot;-z&quot; you will need to give &quot;-z 9&quot;, see &quot;EXPLICIT OPTIONAL ARGUMENTS&quot; paragraph near the end of this document for details on that point. </p>
<dl>
<dt>-c, &#8211;create [&lt;path&gt;/]&lt;basename&gt;</p>
<dd> creates a backup with the name based on &lt;basename&gt;. All the slices will be created in the directory &lt;path&gt; if specified, else in the current directory. If the destination filesystem is too small to contain all the slices of the backup, the -p option (pausing before starting new slices) might be of interest. Else, in the case the filesystem is full, dar will suspend the operation, asking for the user to make free space, then continue its operation. To make free space, the only thing you cannot do is to touch the slice being written. If the filename is &quot;-&quot; *and* no slicing is asked for (no -s option) the archive is produced on the standard output allowing the user to send the resulting archive through a pipe (or into a tape device directly or using the dar_split command).</p>
<dt>-x, &#8211;extract [&lt;path&gt;/]&lt;basename&gt;</p>
<dd> extracts files from the given backup. Slices are expected to be in the current directory or in the directory given by &lt;path&gt;. It is also possible to use symbolic links to gather slices that are not in the same directory. Path may also point to a removable device (floppy, CD, USB key, etc.), in this case, to be able to mount/unmount the device, you must not launch dar from that directory. In other words, the current directory must not on the removable media you plan to unmount (see tutorial for details). The basename may be set to &quot;-&quot;, in direct access mode (the default historical mode), you will then need dar_slave to work with dar (see -i and -o options, as well as dar_slave man page). However in sequential read mode (&#8211;sequential-mode is used on command-line), dar will read the archive from standard input (see also -i option), this can eventually be used in combination with dar_split.</p>
<dt>-l, &#8211;list [&lt;path&gt;/]&lt;basename&gt;</p>
<dd> lists the contents of the given backup. <code>dar</code> will only require the last slice of the archive in direct access mode. If however sequential mode is used, dar will read the overall archive, from the first slice to the last one. &quot;-&quot; can be used as basename, the behavior is the same as with -x option (read just above).</p>
<dt>-t, &#8211;test [&lt;path&gt;/]&lt;basename&gt;</p>
<dd> checks the backup integrity. Even without compression, dar is able to detect at least one error per file in the archive, thanks to a variable length CRC recorded per file data, file EA and file FSA in the catalogue. Archive structure (slice header, archive header, catalogue) is also protected by CRC to be able to detect any kind of archive corruption. Same remark here, &quot;-&quot; may be used as basename (see -x option above for details).</p>
<dt>-d, &#8211;diff [&lt;path&gt;/]&lt;basename&gt;</p>
<dd> compares saved files in the backup with those on the filesystem. &lt;basename&gt; may also be &quot;-&quot; (see -x option above for details). Note that the target for this operation is to be seen as a step further than archive testing, where in addition to archive coherence, the archive contents is verified to be the same as what is found on the filesystem. But if new files are present on the filesystem, dar ignores them. If you want to check for changes since a archive has been made, better use dry-run differential backup.</p>
<dt>-C, &#8211;isolate [&lt;path&gt;/]&lt;basename&gt;</p>
<dd> isolate a catalogue from its archive (that&#8217;s to say make a copy of the internal catalogue to its own archive container). The argument is the basename of the file to create which will contain the catalogue&#8217;s copy. The -A option is mandatory here to give the name of the archive to copy the catalogue from, this archive is not modified at all. Slicing is available (-s -S -p -b etc.). If the filename is &quot;-&quot; *and* no slice is asked (no -s option) the isolated catalogue is produced on the standard output, allowing the user to send the resulting archive through a pipe. Note that there is quite no difference in concept between an isolated catalogue and an archive. Thus you can do all operations on an isolated catalogue, in particular take it in place of the original backup as reference for a differential archive, archive testing, archive comparison. Note however that for comparison (-d option) as data is not present in the isolated catalogue, dar relies on embedded CRC rather than comparing data byte by byte (what is done with a plain archive), and no comparison can be performed concerning EA or FSA even if each of them have their own CRC in the catalogue because different ordering as provided by the OS of the items composing EA and FSA may lead the CRC to be different while the EA or FSA are exactly the same, so CRC here is used only to dectect archive corruption. Since release 2.4.0 you can use an isolated catalogue to rescue a corrupted internal catalogue of the archive it has been based on (see -A option).</p>
<dt>-+, &#8211;merge [&lt;path&gt;/]&lt;basename&gt;</p>
<dd> create a subset archive from one or two existing archives (the resulting archive name is the argument to this command). The dar file selection mechanism (see GENERAL OPTIONS) let the user decide which files will be present in the resulting archive and which one will be ignored. This option thus let the user merge two archives in a single one (with a filtering mechanism that accepts all files), as well as this option let the user create a smaller archive which data is taken from one or two archives of reference. Note that at no time the contents of the archives of reference is extracted to real files and directories: this is an archive to archive transfer, thus you may lack support for Extended Attribute while you will be able to fully manipulate files with their Extended Attributes from one archive to the resulting one. If the basename is &quot;-&quot; *and* no slice is asked (no -s option), the archive is produced on standard output allowing the user to send the resulting archive through a pipe. The first mandatory archive of reference is provided thanks to the -A option, while the second &quot;auxiliary&quot; (and optional) archive of reference is provided thanks to the -@ option. When a tie contention occurs (same file names from both archive have to be merged), the overwriting policy (-/ option) is used to define the one to keep in the resulting archive. By default, archive data selected for merging is uncompressed, and re-compressed. Thus the merging operation can be used to change compression algorithm of given archive as well as change its encryption. But, for better performance it is also possible thanks to the -ak option (see below the -ak option for usage restrictions) to merge files keeping them compressed, thus no decompression/re-compression is performed at all, which make the operation faster. Last it is not possible to merge two isolated catalogues.</p>
<dt>-h, &#8211;help</p>
<dd> displays help usage.</p>
<dt>-V, &#8211;version</p>
<dd> displays version information.</dl>
<p> <code>GENERAL OPTIONS:</code></p>
<dl>
<dt>-v, &#8211;verbose</p>
<dd> For backward compatibility, this is an alias to &quot;-vt -vm&quot; (both options set).</p>
<dt>-vs, &#8211;verbose=skipped</p>
<dd> Display files skipped because of file filtering exclusion specified by the user</p>
<dt>-vt, &#8211;verbose=treated</p>
<dd> Display treated files because of file filtering inclusion specified by the user or no file filtering specified at all. For each file a message is displayed *before* the file is treated. This option is not available for archive isolation and is useless for archive listing as it is always set, unless -q is used.</p>
<dt>-vd, &#8211;verbose=dir</p>
<dd> Display the directory under process. The messages shows *before* entering a directory. You can have a less verbose output than -vt while are still able to follow what&#8217;s dar is doing. Note that -vt and -vd are mutually exclusive.</p>
<dt>-vm, &#8211;verbose=messages</p>
<dd> Display detailed messages about what dar is currently performing but not related to currently treated or skipped files and directories</p>
<dt>-vf, &#8211;verbose=finished</p>
<dd> Issues a summary *after* each treated directory containing the amount of data backed up in that directory as well as the average compression ratio. This option is only available for archive creation.</p>
<dt>-va, &#8211;verbose=all</p>
<dd> activates all the previously described verbose options, see also -Q and -q options below. Note: When using dar from a script better use dar&#8217;s exit status to know which way the operation has ended (seen EXIT CODES at the end of this document). </p>
<dt>-q, &#8211;quiet</p>
<dd> Suppress the final statistics report. If no verbose output is asked beside this option, nothing is displayed if the operation succeeds. When using dar from a script better use dar&#8217;s exit status to know which way the operation has ended (seen EXIT CODES at the end of this document) </p>
<dt>-b, &#8211;beep</p>
<dd> makes the terminal ring when user action is required (like for example the creation of a new slice using the -p option)</p>
<dt>-B, &#8211;batch &lt;filename&gt;</p>
<dd> In the file which name is given in argument to this option, You can put any option or argument as used on command line, that will be parsed as if they were in place of the &quot;-B &lt;filename&gt;&quot; option. This way you can overcome the command line size limitation. Commands in the file may be disposed on several lines, and -B option can also be used inside files, leading a file to include other files. But an error occurs in case of loop (a file that includes itself directly or not) and DAR aborts immediately. Comments are allowed, and must start by a hash `#&#8217; character on each line. Note that for a line to be considered as a comment the hash character must be the first character of the line (space or tab can still precede the hash). See <code>Conditional Syntax</code> below for a more rich syntax in this type of configuration files known as DCF file (Dar Configuration File). See also the environment variable DAR_DCF_PATH in the ENVIRONMENT section at the end of this document.</dl>
<p> Note that you can use quotes simple (&#8216;arg&#8217;) double (&quot;arg&quot;) and back-quotes (`arg`) inside such file, but they need to be balanced (have an ending one). To use such character without the meaning of a quote, for example as an apostrophe, you need to escape it using a back-slack (&quot;That\&#8217;s an example&quot;). Of course to add a single back-slash as a normal character in the file you will have to double it (&quot;c:\windows&quot; for example)</p>
<dl>
<dt>-N, &#8211;noconf</p>
<dd> Do not try to read neither ~/.darrc nor /etc/darrc configuration files. See <code>files</code> section below.</p>
<dt>-Q</p>
<dd> Do not display an initial warning on stderr when not launched from a terminal (when launched from a cronjob for example). This means that all questions to the user will be answered by &#8216;no&#8217;, which most of the time will abort the program. Please note that this option cannot be used in a configuration file (-B option). Since version 2.2.2, giving this option also forces the non-interactive mode, even if dar is launched from a terminal. This makes it possible for dar to run in the background. When you do, it&#8217;s recommended to also redirect stdout and/or sterr to files: dar -Q &#8230; &amp;&gt; /dev/null &amp;</p>
<dt>-n, &#8211;no-overwrite</p>
<dd> do not allow overwriting </p>
<p> If an overwriting policy is specified (see -/ option) -n option do only apply to slices overwriting, the overwriting of files during restoration or merging is handled by the overwriting policy. Without overwriting policy, -n applies to restored files as well as generated slices.</p>
<dt>-w, &#8211;no-warn</p>
<dd> Do not warn before overwriting (applied for slice overwriting and for overwriting decision make by the overwriting policy). By default overwriting is allowed but a warning is issued before proceeding. This option may receive &#8216;a&#8217; as argument (see just below):</p>
<dt>-wa, &#8211;no-warn=all</p>
<dd> This implies the -w option, and means that over avoiding warning for file overwriting, DAR also avoids signaling a file about to be removed when its type is not the expected one. File are removed when they have been recorded as deleted since the archive of reference. At restoration of the differential archive, if a file of the given name exists, it is remove, but if the type does not match the file that was present at the time of the archive of reference (directory, plain file, fifo, socket, char or block device, etc.), a warning is normally issued to prevent the accidental removal of data that was not saved in the backup of reference. (See also -k option)</p>
<dt>-A, &#8211;ref [&lt;path&gt;]/&lt;basename&gt;</p>
<dd> Depending on the context, it specifies the archive to use as reference, which is mandatory for archive isolation (-C option) and merging operation (-+ option). Else it specifies the rescue catalogue to use when restoring (-x command), testing (-t command) or comparing (-d command) an archive. All slices of the reference backup are expected to be on the same directory given by &lt;path&gt; or the current directory by default. Usually only the last slice is required to extract the catalogue of reference. If necessary the use of symbolic links is also possible here to gather slices that do not reside in the same directory. You can also point &lt;path&gt; to a USB key, DVD-R(W) or any other mounted directory, because <code>dar</code> will pause and ask the user for required slices if they are not present. The argument to -A may be of four types:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211; An existing archive basename, which will be taken as reference</p>
<dd>
<dt>&#8211; a dash (&quot;-&quot;) in direct access mode (default mode, when &#8211;senquential-read is not used) it may imply the use of -o and -i options, this allows the archive of reference to be read from a pair of pipes with dar_slave at the other ends. Dar_slave can be run through ssh on a remote host for example. Note that this type of argument (&quot;-&quot;) is only available when -A is used for isolation (-C option) and merging (-+ options). In sequential mode (&#8211;sequential-mode is used), the archive of reference is read from standard input or from the named pipe specified by -i option. -o option has no use in sequential mode. Note that merging operation (-+ option) cannot read archive of reference in sequential mode.</p>
<dd>
<dt>&#8211; a plus sign (&quot;+&quot;) which makes the reference be the current directory status. This argument is only available for archive creation (-c option). In other word, no file&#8217;s data will be saved, just the current status of the inodes will be recorded in the catalogue. This feature is known as the &quot;snapshot&quot; backup. A snapshot backup can be used as reference later on to detect or save only the files that have changed since the snapshot was made.</p>
<dd>
<dt>&#8211; a &lt;date&gt;, if -af option has been placed before -A on the command-line or in a included file (see -B option). For more about that feature see -af option below. This form is only available for archive creation (-c option).</p>
<dd></dl>
</dl>
<p> During backup operation (-c option) the archive of reference, given thanks to the -A option, is used for comparison with existing files on the filesystem. Dar will then backup only files that have changed since the archive of reference was done. If no -A option is given, the backup operation is a full backup. With -A option if the archive of reference is a full backup some call it a differential backup, while if the archive of reference is differential backup, some call this type of backup an incremental backup. For dar there is no difference in structure between incremental and differential backup, both are usually designed globally as &quot;differential&quot; backup in the documentation. </p>
<p> During merging operation (-+ option), the contents of the -A given archive will been taken eventually with the contents of the -@ auxiliary archive if specified (see below), to form a new archive from files of this or these archives. Note that you can filter out files from the operation and setup subset of the original archive(s). </p>
<p> During Catalogue isolation (-C option), dar will create the isolated catalogue from the one given with -A option. </p>
<p> During testing, diff or extraction, (-t, -d or -x options respectively), the table of contents (the catalogue) will be read from the archive given with -A instead of using the internal catalogue of the archive. The archive given for rescue must has been previously isolated from this same archive (else the contents will not match and dar will refuse to proceed to this operation). This acts as a backup solution to the case of corruption inside an archive&#8217;s catalogue, while the best way is still to use Parchive to protect your data against media error.</dl>
<dt>-af, &#8211;alter=fixed-date</p>
<dd> Modify the -A option behavior, making it receiving a &lt;date&gt; as argument in place of the [&lt;path&gt;]/&lt;basename&gt; default argument. The &lt;date&gt; is used to define which file to save: file which modification is newer or equal to &lt;date&gt;, and which to consider unchanged: those older than &lt;date&gt;. This option has only a meaning when creating an archive (-c option) and must be placed before -A option to have an effect.</p>
<dl>
<dt>
<dd>
<p> &lt;date&gt; must be a date in the two following possible formats:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211; a number of second since Jan 1st, 1970</p>
<dd>
<dt>&#8211; a date in the following form [[[year/]month/]day-]hour:minute[:second]</p>
<dd></dl>
</dl>
<p> Here are some examples of date:</p>
<dl>
<dt>
<dd> 91836383927108078 </p>
<p> 2005/11/19-19:38:48 Which is 38 past 7 PM and 48 seconds, the 19th of November 2005 </p>
<p> 20:20 Which is 8 PM of the current day </p>
<p> 2-00:08 Which is 8 past noon, the second day of the current month </p>
<p> 2/2-14:59 Which is 1 to 3 PM, the 2nd of February in the current year</dl>
</dl>
<dt>-@, &#8211;aux [&lt;path&gt;]/&lt;basename&gt;, &#8211;on-fly-isolate [&lt;path&gt;]/&lt;basename&gt;</p>
<dd> specifies an auxiliary archive of reference (merging context) or the name of the on-fly isolated catalogue (creation context). This option is thus only available with -+ option (merging) and -c option (archive creation). Note that &#8211;aux and &#8211;on-fly-isolate are really aliases to the same option, this is the context of use (archive creation or merging) which lead it to behave a way or another.</p>
<dl>
<dt>
<dd>
<p> In a merging context, over -A option which is mandatory, you may give a second archive of reference thanks to the -@ option. This allows you to merge two archives into a single one. See also -$ option (encryption) -~ option (command execution) and -% (crypto block size) for other options concerning auxiliary archive of reference. They are the respective equivalent of -J, -F and -* options relative to archive given thanks to -A option. </p>
<p> In a backup context -@ option let the user specify the archive name for an on-fly isolation. With on-fly isolation, you can also use -$ option (to define encryption algorithm and passphrase), -~ option (to execute a command once the on-fly isolated catalogue is completed) and -% option (crypto block size). On-fly isolated catalogue is always bzip2 if possible else gzip else lzo compressed (using compression level 9) else not compressed, and it is also always a single sliced archive. Due to command-line exiguity, it is not possible to change compression algo nor slice size for the on-fly isolation. If you need a more complicated isolation, either look for a GUI over libdar, or do a normal (= not an on-fly) isolation operation (By the way it is possible to isolate an already isolated catalogue, this is equivalent to doing a copy, but you can change encryption, compression or slicing, for example), you can also use dar_xform on an isolated catalogue if you only want to change slices size (this is faster as no decompression/re-compression nor encryption/decryption is necessary). Using the merging operation on an isolated catalogue instead of isolating the isolated catalogue, leads the resulting archive to not be able to be used as a rescue for internal catalogue of the original archive. &#8211;aux-ref is a synonym to &#8211;aux.</dl>
<dt>-R, &#8211;fs-root &lt;path&gt;</p>
<dd> The path points to the directory tree containing all the files that will be enrolled in the operation (backup, restoration or comparison). By default the current directory is used. All other paths used in -P or -g options on the command line are and must be relative to this path (or to current directory if -R is not present). Note that -R is useless for testing (-t option) isolation (-C option) and merging (-+ option)</p>
<dt>-X, &#8211;exclude &lt;mask&gt;</p>
<dd> The mask is a string with wildcards (like * and ? see <a href="/docs/linux/man/7-glob/">glob</a>(7) for details) which is applied to filenames which are not directories. If a given file matches the mask, it is excluded from the operation. By default (no -X on the command line), no file is excluded from the operation. -X may be present several times on the command line, in that case a file will not be considered for the given operation if it matches at least one -X mask. See also -ar and -am options.</p>
<dt>-I, &#8211;include &lt;mask&gt;</p>
<dd> The mask is applied to filenames which are not directories (see <a href="/docs/linux/man/7-glob/">glob</a>(7) for details on wildcard characters). If a given file matches the mask and does not match any mask given with -X, the file is selected for the operation. By default (no -I and no -X on the command line), all files are included for the operation. -I may be present several times on the command line, in that case all file that match one of the -I mask will be considered for the given operation, if they do not also match one of the -X mask. See also -ar and -am options.</p>
<dt>-P, &#8211;prune &lt;path&gt;</p>
<dd> Do not consider file or directory sub-tree given by the path. -P may be present several time on the command line. The difference with -X is that the mask is not applied only to the filename, but also include the path. Moreover it applies also to directories (-X does not). By default (no -P on the command-line), no sub-tree or file is excluded from the operation, and all the directory tree (as indicated by -R option) is considered. Note that &lt;path&gt; may contains wildcards like * or ? see <code><a href="/docs/linux/man/7-glob/">glob</a>(7)</code> man page for more information.</p>
<dt>-g, &#8211;go-into &lt;path&gt;</p>
<dd> Files or directory to only take in account, as opposed to -P. -g may be present several time on command-line. Same thing here, the difference with -I is that the mask is applied to the path+filename and also concerns directories. By default all files under the -R directory are considered. Else, if one or more -g option is given, just those are selected (if they do not match any -P option). All paths given this way must be relative to the -R directory, which defaults to current directory. <code>Warning,</code> -g option cannot receive wildcards, these would not be interpreted.</p>
<dt>-[, &#8211;include-from-file &lt;listing_file&gt;</p>
<dd> Files listed in the listing file are included for the operation. No wildcard expression is interpreted in the listing file, the null character is not allowed and the carriage return is used to separate file names (one file name per line). Note that this option applies to any files and directory exactly as -g does, with an important difference however: -g option only uses relative paths to the root directory (the directory given with the -R option), while -[ can use absolute path as well. Another difference is when the argument is a directory -g will include all the subdirectories under that directory, while when the same entry is found in a listing file given to -[ only that directory will be included, no subdirectory or subfile would be enrolled in the backup, with -[ you need to list the exact set of file you want to backup. You can thus generate a listing file with the &#8216;find / -print &gt; somefile&#8217; command and give &#8216;somefile&#8217; as argument to -[ option. Note that however, dar will never save files out of the -R given root directory tree, even if some are listed in the &#8216;somefile&#8217; file.</p>
<dt>-], &#8211;exclude-from-file &lt;listing_file&gt;</p>
<dd> Files listed in the listing file are excluded from the operation. If a directory is listed in the file all its contents is excluded. This option is the opposite of -[ and acts the same was as -P option does (in particular it is compared to the whole path+filename and applies to files and directories). As for -[ option, -] listing file can contain absolute paths, but wildcards are not expanded, neither.</dl>
<p> <code>File selection in brief:</code> </p>
<p> As seen above, -I -X -P, -g, -[ and -] options are used to select the files to operate on. -I and -X only use the name of files and do not apply to directories, while -P, -g -[ and -] use the filename *and* the path, they *do* apply to directories. </p>
<p> since version 2.2.0 two modes of interpretation of these options exist. The normal original method and the ordered method:</p>
<dl>
<dt>
<dd>
<dl>
<dt>the normal method is the default and is the one that has been presented above:</p>
<dd> A directory is elected for operation if no -P or -] option excludes it. If at least one -g or -[ option is given one command line, one -g or -[ option must cover it, else it is not elected for operation. If a directory is not selected, no recursion is done in it (the directory is pruned). For non directories files, the same is true (P, -g, -[ and -] do apply) and a second test must also be satisfied: no -X option must exclude the filename, and if at least one -I option is given, one must match the given filename (using or not wildcards).</p>
<dt>the ordered method (when -am option is given on command-line):</p>
<dd> The ordered method takes care of the order of presence between -X and -I in one hand and of -P, -g, -[ and -] in the other hand (note that it has also the same action concerning EA selection when using -u and -U options, but that&#8217;s no more file selection). In the ordered method the last argument take precedence over all the previous ones, let&#8217;s take an example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>-X &quot;*.mp?&quot; -I &quot;*.mp3&quot; -I &quot;toto*&quot;</p>
<dd> Here dar will include all files except file of name &quot;*.mp?&quot; (those ending with &quot;mpX&quot; where X is any character), but it will however include those ending with &quot;.mp3&quot;. It will also include files which name begin by &quot;toto&quot; whatever they end with. This way, &quot;toto.mp2&quot; will be saved (while it matches &quot;*.mp?&quot; it also begins by &quot;toto&quot;) as well as &quot;toto.txt&quot; as well as &quot;joe.mp3&quot; (while it matches &quot;*.mp?&quot; it also ends by &quot;mp3&quot;). But will not be saved &quot;joe.mp2&quot; (because it does not begin by &quot;toto&quot;, nor ends by &quot;mp3&quot;, and match &quot;*.mp?&quot; mask). As we see the last option (-I or -X) overcomes the previous one. -P, -g, -[ and -] act together the same but as seen above they do not only act on filename, but on the whole path+filename. Note that (-g, -P, -[, -]) and (-X , -I) are independent concerning their relative order. You can mix -X -I -g -P -] -[ in any order, what will be important is the relative positions of -X options compared to -I options, and the relative positions of -g -[ -] and -P options between them.</dl>
</dl>
</dl>
<p> In logical terms, if &lt;prev_mask&gt; is the mask generated by all previous mask on the command line, -I &lt;mask&gt; generates the new following mask: &lt;prev_mask&gt; or &lt;mask&gt; . While -X &lt;mask&gt; generates the new following mask: &lt;prev_mask&gt; and not &lt;mask&gt;. This is recursive each time you add a -I or -X option. Things work the same with -P, -g, -[ and -] options.</dl>
<p> <code>This ends the file selection explication</code> let&#8217;s continue with other options. </p>
<dl>
<dt>-u, &#8211;exclude-ea &lt;mask&gt;</p>
<dd> Do not consider the Extended Attributes (EA) that are matched by the given mask. By default, no EA are excluded, if the support for EA has been activated at compilation time. This option can be used multiple times.</p>
<dt>-U, &#8211;include-ea &lt;mask&gt;</p>
<dd> Do only consider the EA that match the given mask. By default, all EA are included if no -u or -U option is present and if the support for EA has been activated at compilation time. This option can be used multiple times. See also the -am and -ae options, they also apply to -U and -u options and read below the Note concerning EA.</dl>
<p> <code>Note concerning Extended Attributes (EA)</code> </p>
<dl>
<dt>
<dd> Support for EA must be activated at compilation time (the configure script tries to do so if your system has all the required support for that). Thus you can get two binaries of dar (of the same version), one supporting EA and another which does not (dar -V to see whether EA support is activated). The archives they produce are the same and can be read by each other. The only difference is that the binary without EA support is not able to save or restore EAs, but is still able to test them and list their presence. </p>
<p> In the following when we will speak about Extended Attribute (EA) or EA entry, we will only consider a particular Extended Attribute key and its value. By opposition, the set of all EA associated to a file will be designated by &quot;EA set&quot;. </p>
<p> Since version 2.3.x the name of EA entries include the namespace for dar be able to consider any type of EA (not only &quot;system&quot; and &quot;user&quot; as previously). Thus the two previous options -u and -U have changed and now take an argument which is a mask applied to EA entry names written in the following form <i>namespace.name</i> where &quot;namespace&quot; is for example &quot;user&quot;. Note that the mask may or may not include the dot (.) and may match arbitrary part of the EA namespace+name, just remind that masks will be applied to the &quot;namespace.name&quot; global string. </p>
<p> the -am flag here also enables the ordered method, for EA selection too. The ordered versus normal method have been explained above in the file selection note, with some examples using -X and -I. Here this is the same with -U and -u, (just replace -X by -u and -I by -U, the corresponding mask will apply to Extended Attribute selection in place of file selection). </p>
<p> Another point, independently of the -am option the -ae option can be used at restoration time only. If set, when a file is about to be overwritten, all EA will be first erased before restoring those selected for restoration in the archive (according to the -U and -u options given). If not set, the EA of the existing file will be overwritten, those extra EA that are not in the archive or are not selected for restoration in regard to the -u and -U options will be preserved. If you have not used any -u/-U option at backup time and want to restore from a set of full/differential backups the EA exactly as they were, you have to use -ae for dar removes the EA before overwriting their set of EA as stored in the archive. Without -ae option dar will simply add EA to existing ones, thus get a different set of EA for a give file than those recorded at the time of the backup. </p>
<p> Last point the -acase and -an options alters the case sensitivity of the -U and -u masks that follow them on the command-line/included files as they do for -I, -X, -P, -g, -[ and -] as well. Very last point ;-), if -ac option is used during backup dar set back the atime after having read each file (see -aa/-ac options), this has as side effect to modify the ctime date of each file. But ctime change is used by dar to detect EA changes. In brief, the next time you backup a file that had to be read (thus which contents changed), its EA will be saved even if they had not changed. To avoid this side effect, don&#8217;t use the -ac option if not necessary.</dl>
<p> <code>This ends the Extended Attribute selection explication</code> let&#8217;s continue with other options. </p>
<dl>
<dt>-4 &#8211;fsa-scope &lt;family&gt;[,&lt;family&gt;[, &#8230;]</p>
<dd> Reduce the scope of Filesystem Specific Attribute (FSA) to be considered for the operation. FSA are grouped by family. Current available families are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>extX</p>
<dd> this family takes care of Linux ext2/3/4 flag attributes set by <a href="/docs/linux/man/1-chattr/">chattr</a>(1) and read by <a href="/docs/linux/man/1-lsattr/">lsattr</a>(1). Dar only considers flags that are possible to set or clear by users (or privileged user): append-only, compressed, no_dump (Yes, dar can save files having the nodump flag set and restore then afterward with that flag set!), immutable, data-journaling, secure-deletion, no-tail-merging, undeletable, noatime-update, synchronous-directory, synchronous-update, top-of-directory-hierarchy. Note that &quot;extx&quot; and &quot;ext&quot; are aliases for this FSA family. In spite of its name, this family of attributes is not limited to ext2/3/4 filesystems.</p>
<dt>
&nbsp;<wbr>HFS+</p>
<dd> this family takes care of Mac OS X HFS+ birth date of files, in addition of commonly found dates like atime (last access time), ctime (last meta data change) and mtime (last data change).</p>
<dt>none</p>
<dd> &quot;none&quot; is not a FSA family but can be used alone to ignore all FSA families.</dl>
<p> By default no restriction is done and FSA of all families are considered at restoration time, but if a family has not been activated at compilation time a warning is issued for each file that cannot have its FSA restored completely (unless this family is excluded from the scope thanks to the -4 option). At backup time, if an FSA family has not been activated at compilation time, no warning is issued and FSA of that family are ignored. Still at backup time, you can also ignore FSA that have compilation time support by excluding them from the operation thanks to this -4 option. </p>
<p> Example of use: &#8211;fsa-scope extX,HFS+</dl>
<dt>-am, &#8211;alter=mask</p>
<dd> set the ordered mode for mask. This affects the way -I and -X options are interpreted, as well as -g, -P, -[ and -] options, -Z and -Y options and -U and -u options. It can take any place on the command-line and can be placed only once. See the <code>file selection in brief</code> paragraph above for a detailed explanation of this option. It has also an incidence on the &#8211;backup-hook-exclude and &#8211;backup-hook-include options.</p>
<dt>-an, &#8211;alter=no-case</p>
<dd> set the filters in case insensitive mode. This concerns only masks specified after this option (see also -acase option below). This changes the behavior of -I, -X, -g, -P, -Z, -Y, -u and -U options.</dl>
<p> Warning: case insensitivity requires interpreting filenames which depends on the locale with which dar is run (defined by the LANG environment variable). For example if you create files with LANG set to fr_FR.UTF-8 and use non plain ASCII characters in filename, there is chances that these non ASCII characters will be stored over several bytes in that filename: so called &quot;wide characters&quot;. If then you run dar with LANG set to another value like ru_RU.koi8r, there is much chances that these wide characters do not correspond to the same letter or worse, that they do not match any valid wide character for that locale. A filename is always a sequence of bytes and always saved as such, but using &#8211;alter=no-case implies interpreting that sequence in a way that depends on the given locale (as defined by the LANG environment variable). As such, dar cannot know if a given file has to be read with fr_FR.UTF-8 locale or with it_IT.iso88591 or ru_RU.koi8r and so on, because this information is not stored in filenames. In consequence, if different locales are used on your system and you are doing a system wide backup, using &#8211;alter=no-case option may lead dar to detect invalid wide character, in that case it falls back to a byte by byte case sensitivity comparison (ASCII characters), which may not be what you would expect at first sight: Most of the time, an upper case wide character (stored on several bytes) does not match the equivalent lower case wide character (several bytes too), when case sensitivity comparison is performed byte by byte.</p>
<dl>
<dt>-acase, &#8211;alter=case</p>
<dd> set back to case sensitive mode for filters. All following masks are case sensitive, up to end of parsing or up to the next -an option. This changes the behavior of -I, -X, -g, -P, -Z, -Y, -u and -U options.</p>
<dt>-ar, &#8211;alter=regex</p>
<dd> set the filters to be interpreted as regular expressions (man <code><a href="/docs/linux/man/7-regex/">regex</a>(7)</code> ) instead of the default glob expression (man <code><a href="/docs/linux/man/7-glob/">glob</a>(7)</code> ) This modifies the -I, -X, -g, -P, -Z, -Y, -u and -U options that follows up to an eventual -ag option (see just below). Note that for -P option, the given mask matches the relative path part of the files path: Let&#8217;s take an example, assuming you have provided /usr/local to the -R option, the mask &quot;^foo$&quot; will replaced internally by &quot;^/usr/local/foo$&quot; while the mask &quot;foo$&quot; will be replaced internally by &quot;^/usr/local/.*foo$&quot;.</p>
<dt>-ag, &#8211;alter=glob</p>
<dd> This option returns to glob expressions mode (which is the default) after an -ar option has been used, this applies to any -I, -X, -g, -P, -Z, -Y, -u and -U options that follow up to an eventual new -ar option (see just above).</p>
<dt>-i, &#8211;input &lt;path&gt;</p>
<dd> is available when reading from pipe (basename is &quot;-&quot; for -x, -l, -t, -d or for -A when -c, -C or -+ is used). When reading from pipe, standard input is used, but with this option, the file &lt;path&gt; (usually a named pipe) is used instead. This option is to receive output from dar_slave program (see doc/usage_notes.html for examples of use). Note that when &#8211;sequential-read is used, dar uses a single pipe and does no more rely on dar_slave, -i option can be used to tell dar which named pipe to read the archive from, instead of the standard input.</p>
<dt>-o, &#8211;output &lt;path&gt;</p>
<dd> is available when reading from pipe (basename is &quot;-&quot; for -x, -l, -t, -d or for -A when -c, -C or -+ is used). When reading from pipe, standard output is used to send request to dar_slave, but with this option, the file &lt;path&gt; (usually a named pipe) is used instead. When standard output is used, all messages goes to standard error (not only interactive messages). See doc/usage_notes.html for examples of use. This option is not to be used in &#8211;sequential-read mode.</p>
<dt>-O, &#8211;comparison-field[=&lt;flag&gt;]</p>
<dd> When comparing with the archive of reference (-c -A) during a differential backup, when extracting (-x) or when comparing (-d) do only considers certain fields. The available flags are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>ignore-owner</p>
<dd> all fields are considered except ownership. This is useful when dar is used by a non-privileged user. It will not consider a file has changed just because of a uid or gid mismatch and at restoration dar will not even try to set the file ownership.</p>
<dt>mtime</p>
<dd> only inode type and last modification date is considered as well as inode specific attributes like file size for plain files. Ownership is ignored, permission is ignored. During comparison, difference on ownership or permission is ignored and at restoration time dar will not try to set the inode permission and ownership.</p>
<dt>inode-type</p>
<dd> Only the inode type is considered. Ownership, permission and dates are ignored. Inode specific attributes are still considered (like file size for plain files). Thus comparison will ignore differences for ownership, permission, and dates and at restoration dar will not try to set the ownership, permission and dates.</dl>
</dl>
</dl>
<p> When no flag is provided to this option, -O option acts as if the &quot;ignore-owner&quot; flag was set, which is the behavior in older releases (&lt; 2.3.0). Note also that for backward compatibility, &#8211;ignore-owner option still exists and since version 2.3.0 is just an alias to the &#8211;comparison-field=ignore-owner option. Of course if this option is not used, all fields are used for comparison or restoration.</p>
<dl>
<dt>-H[num], &#8211;hour[=num]</p>
<dd> if -H is used, two dates are considered equal if they differ from a integer number of hours, and that number is less than or equal to [num]. If not specified, num defaults to 1. This is used when making a differential backup, to compare last_modification date of inodes, at restoration or merging time if overwriting policy is based on file&#8217;s data or EA being more recent and last, when comparing an archive with a filesystem (-d option). This is to workaround some filesystems (like Samba filesystem) that seems to change the dates of files after having gone from or to daylight saving time (winter/summer time). Note that -H option has influence on the overwriting policy (see -/ option) only if it is found before on command-line or in an included file (using -B option).</p>
<dt>-E, &#8211;execute &lt;string&gt;</p>
<dd> the string is a <code>user command-line</code> to be launched between slices. For reading an archive (thus using -t, -d, -l or -x commands), the given string is executed before the slice is read or even asked, for writing an archive instead (thus using -c, -C or -+ commands), the given string is executed once the slice has been completed. Some substitution macros can be used in the string:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%%</p>
<dd> will be replaced by %</p>
<dt>%p</p>
<dd> will be replaced by the slice path</p>
<dt>%b</p>
<dd> will be replaced by the slice basename</p>
<dt>%n</p>
<dd> will be replaced by the slice number (to be read or just written). For reading, dar often needs the last slice, but initially it does not know its number. If it cannot be found in the current directory, the user command-line is then called with %n equal to 0. This is a convenient way to inform the user command to provide the last slice. If after executing the string the requested slice is still not present, dar asks the user (as usually) with a message on the terminal. Once the last slice is found, the user command-line is called a second time, with %n equal to the value of the last slice number.</p>
<dt>%N</p>
<dd> is the slice number with the leading zero as defined by &#8211;min-digits option. If this option is not used, %N is equivalent to %n.</p>
<dt>%e</p>
<dd> will be replaced by the slice extension (always substituted by &quot;dar&quot;)</p>
<dt>%c</p>
<dd> will be replaced by the context. Actually three possible values exist: &quot;init&quot;, &quot;operation&quot; and &quot;last_slice&quot;. When reading an archive for (testing, extraction, diff, listing, or while reading the archive of reference, see below the -F option), the &quot;init&quot; context takes place from the beginning up to the time the catalogue is retrieved. On a multiple slice archive this correspond to the last slice request. After, that point comes the &quot;operation&quot; context. While creating an archive, the context is always &quot;operation&quot; except when the last slice has been created, in which case the context is set to &quot;last_slice&quot;.</dl>
</dl>
<p> Several -E option can be given, given commands will then be called in the order they appear on the command line and -B included files. Such file given to -E option are known as DUC files (Dar User Command). See also the environment variable DAR_DUC_PATH in the ENVIRONMENT section at the end of this document.</p>
<dt>-F, &#8211;ref-execute &lt;string&gt;</p>
<dd> same as -E but is applied between slices of the reference archive (-A option). &#8211;execute-ref is a synonym.</p>
<dt>-~, &#8211;aux-execute &lt;string&gt;</p>
<dd> same as -E and -F but is applied between slices of the auxiliary archive (-@ option).</p>
<dt>-K, &#8211;key [[&lt;algo&gt;]:]&lt;string&gt;</p>
<dd>
<dt>-K, &#8211;key gnupg:[&lt;algo&gt;]:email[,email[&#8230;]]</p>
<dd>
<dl>
<dt>
<dd> <code>In the first syntax,</code> encrypt/decrypt the archive using the &lt;algo&gt; cipher with the &lt;string&gt; as pass phrase. An encrypted archive can only be read if the same pass phrase is given (symmetric encryption). Available ciphers are &quot;blowfish&quot; (alias &quot;bf&quot;), &quot;aes&quot;, &quot;twofish&quot;, &quot;serpent&quot; and &quot;camellia&quot; for strong encryption and &quot;scrambling&quot; (alias &quot;scram&quot;) for a very weak encryption. By default if no &lt;algo&gt; or no &#8216;:&#8217; is given, the blowfish cipher is assumed. If your password contains a column &#8216;:&#8217; you need to specify the cipher to use (or at least use the initial &#8216;:&#8217; which is equivalent to &#8216;bf:&#8217;). If the &lt;string&gt; is empty the pass phrase will be asked at execution time. Thus, the smallest argument that -K can receive is &#8216;:&#8217; which means blowfish cipher with the pass phrase asked at execution time. </p>
<p> Note that giving the passphrase as argument to -K (or -J or &#8216;-$&#8217; see below) may let other users learn pass phrase (thanks to the ps, or top program for examples). It is thus wise to either use an empty pass which will make dar ask the pass phrase when needed, or use -K (or -J option) from a Dar Command File (see -B option), assuming it has the appropriated permission to avoid other users reading it. For those paranoids that are really concerned about security of their passwords, having a password read from a DCF is not that secure, because while the file gets parsed, dar makes use of &quot;unsecured&quot; memory (memory than can be swapped to disk under heavy memory load conditions). It is only when the passphrase has been identified that locked memory (aka secure memory) is used to store the parsed passphrase. So, the most secure way to transmit a passphrase to dar, then to libdar, then to libgcrypt, is having dar asking passphrase at execution time, dar then makes use of secured (locked) memory from the beginning. </p>
<p> since archive format 9 (archive generated by release 2.5.0 and following) at reading time, it is not necessary to provide the encryption algorithm used, just the passphrase is required, dar will figure out which encryption algorithm had been used at archive creation time. You can either ommit -K in which case dar will ask for the passphrase at execution time, or you can use -K &lt;string&gt; in a DCF file as explained above (avoid using -K directly on command-line). </p>
<p> <code>The second syntax</code> starts with the word &quot;gnupg&quot; followed by a column &#8216;:&#8217; . In that situation, the same set or symmetric encryption algorithms as described above is available after the column, but the passphrase is not given by the user but randomly chosen by libdar and encrypted using the public key of the target users which email is given in a comma separated list. This random key (see also &#8211;key-length below), once encrypted is placed at the beginning and at the end of the generated archive. At reading time only the listed user will be able to read that archive thanks to their respective private key. This feature implies that each user (the archive creator as well as the target users) have their GnuPG keyring set properly. In particular, the archive creator must have validated the public keys of the target users, and the target users must own the corresponding private key in their keyring. Example: using &quot;&#8211;key gnupg::bob [at] nowhere.org,joe [at] somewhere.com&quot; will generate a blowfish encrypted archive which passprhase randomly chosen by libdar will be encrypted with the public keys of bob [at] nowhere.org and joe [at] somewhere.com. To use AES in place of blowfish one could use &quot;&#8211;key gnupg:aes:bob [at] nowhere.org,joe [at] somewhere.com&quot;. Note that no check is done about the trust you have set in GPG keyring that a particular public key is owned by the phyical person you expect. See also &#8211;sign option below. </p>
<p> Note that if you have set a passphrase on your private key, dar will ask it dynamically, which requires dar to be run from a terminal. No other way has been provided to transmit a private key&#8217;s passphrase to libdar. In consequence if you want to use dar/libdar in scripts and make use of public key algorithm you should avoid setting a passphrase to the private key you want to use. See also GNUPGHOME in the ENVIRONMENT section at the end of this document. </p>
<p> <code>Obvious but important!</code> To read a gnupg encrypted archive, you need your private key (not only the passphrase to activate it, if set). Thus if you plan to make backup of your system and encrypt the backup using gnupg, you should have a copy of this private key available out of the archive (usb key, floppy, CD/DVD, &#8230;) in order to be able to restore your backup!</dl>
<dt>-J, &#8211;ref-key [[&lt;algo&gt;]:]&lt;string&gt;</p>
<dd> same meaning/use as -K option&#8217;s first syntax, but the given key is used to decrypt the archive of reference (given with -A option). &#8211;key-ref is a synonym. Note that for archives generated using dar release 2.5.0 and above this option is no more necessary, unless you want to give the passphrase on command-line (not recommended) or in DCF file (which file would be set with restricted access permissions and/or ACL).</p>
<dt>-$, &#8211;aux-key [[&lt;algo&gt;]:]&lt;string&gt;</p>
<dd> same as -J but for the auxiliary archive of reference (given with -@ option). Here too, this option is no more necessary to read archives generated by dar release 2.5.0 and above.</p>
<dt>-#, &#8211;crypto-block &lt;size&gt;</p>
<dd> to be able to randomly access data in an archive, it is not encrypted globally but block by block. You can define the encryption block size thanks to this argument which default to 10240 bytes. Note that the syntax used for -s option is also available here (k, M, G, etc.). Note also that crypto-block is stored as a 32 bits integer thus value larger than 4GB will cause an error. Note last, that the block size given here must be provided when reading this resulting archive, using the -* option if the archive is the archive of reference (given to -A option) using -% options if the archive is the auxiliary archive of reference (given to -@ option) or using this -# option if it is the subject of the operation (listing, comparing, testing that archive). If the value is not the default and the given value is not correct in regard to the value given at archive creation time, the archive will not be possible to decrypt, it is thus safer to keep the default value (and not using at all the -#, -*, -% options).</p>
<dt>-*, &#8211;ref-crypto-block &lt;size&gt;</p>
<dd> same as &#8211;crypto-block but to read the archive of reference (-A option). &#8211;crypto-block-ref is a synonym.</p>
<dt>-%, &#8211;aux-crypto-block &lt;size&gt;</p>
<dd> same as &#8211;crypto-block but to read the auxiliary archive of reference (-@ option).</p>
<dt>-e, &#8211;dry-run</p>
<dd> Do not perform any action (backup, restoration or merging), displays all messages as if it was for real (&quot;dry run&quot; action). The &#8211;empty option is a synonym.</p>
<dt>-aSI, &#8211;alter=SI[-unit[s]]</p>
<dd> when using k M G T E Z Y prefixes to define a size, use the SI meaning: multiple of 10^3 (a Mega is 1,000,000).</p>
<dt>-abinary, &#8211;alter=binary[-unit[s]]</p>
<dd> when using k M G T E Z Y prefixes to define a size, use the historical computer science meaning: multiple of 2^10 (a Mega is 1,048,576).</dl>
<p> The &#8211;alter=SI and &#8211;alter=binary options can be used several times on the command line. They affect all prefixes which follow, even those found in files included by the -B option, up to the next &#8211;alter=binary or &#8211;alter=SI occurrence. Note that if in a file included by the -B option, an &#8211;alter=binary or &#8211;alter=SI is encountered, it affects all the following prefixes, even those outside the included files. For example, when running with the parameters &quot;-B some.dcf -s 1K&quot;, 1K may be equal to 1000 or 1024, depending on &#8211;alter=binary or &#8211;alter=SI being present in the some.dcf file. By default (before any &#8211;alter=SI/binary option is reached), binary interpretation of prefixes is done, for compatibility with older versions.</p>
<dl>
<dt>-ac, &#8211;alter=ctime</p>
<dd> When reading a filesystem (during a backup or comparison), restores the atime of all files to what it was before the file was read. This makes it appear as if it had not been read at all. However, because there is no system call to let applications changing the ctime (last inode change) of a file, setting back the atime results in the ctime being changed (hence the alter=ctime). Some recent unix system allow an application to get &#8216;furtive read mode&#8217; to the filesystem (see below). On older systems, however, for most users, having the atimes of the files changed shouldn&#8217;t be a problem, since they can be changed by any other program (running by any user!) as well (like the content-index program Beagle). Ctimes on the other hand, are the only way for security software to detect if files on your system have been replaced (by so called root-kits mostly). This means, that should you run dar with -ac, security software which uses ctimes to check, will mark every file on your system as compromised after the backup. In short, this means this option should only be used by people who know what they are doing. It&#8217;s the opinion of this writer that any software susceptible to atime changes is flakey or even broken (because of the afore mentioned reasons why atimes can change). But, that doesn&#8217;t take away that there are programs who rely on atimes remaining the same, like Leafnode NNTP caching software. Therefore this option exists.</p>
<dt>-aa, &#8211;alter=atime</p>
<dd> When specifying -aa (by opposition to -ac), the atime of every read file and directory is updated, and the ctime remains the same. In other words, Dar itself does nothing with atimes and ctimes, it only let the system do its job to update atimes when files are accessed for reading. This is in accordance with what atimes and ctimes were meant to represent. This is Dar&#8217;s default (since version 2.4.0), unless &#8216;furtive read mode&#8217; (see below) is supported by your system and dar has been compiled with this support activated.</dl>
<p> <code>Furtive read mode</code> is a mode in which neither atime nor ctime are modified while dar reads each file and directory. This provides also better performances as nothing has to be wrote back to disk. A known Unix kernel that supports this feature is Linux 2.6.8 and above (support must also be present in the standard C library of the system for dar to be able to activate this feature at compilation time). When this feature is activated, it becomes the default behavior of dar for super user ; for other users the default is -aa. If however as root user, you do not want to use &quot;furtive read mode&quot; (while it has been activated at compilation time), you can specify either -aa or -ac option.</p>
<dl>
<dt>-at, &#8211;alter=tape-marks</p>
<dd> For archive creation and merging, the default behavior (since release 2.4.0) is to add escape sequences (aka tape marks) followed by inode information all along the archive. If -at is given, dar will not add this information to the archive, resulting in a slightly smaller archive and faster backup. When reading an archive, the default behavior is to ignore these escape sequences and rather rely on the catalogue located at the end of the archive. If instead &#8211;sequential-read is given on command-line (see below), dar will avoid using the catalogue at the end of the archive and will rely on these escape sequences to know the contents of the archive, which will lead to a sequential reading of the archive, operation suitable for tape media. Note that it is not recommended to disable escape sequences (aka tape marks) by using -at option except if you are more concerned by the resulting size and execution speed of your backup (in particular if you have a lot of small files) than by the possibility to recover your data in case of corrupted or partially written archive. Without escape sequences, dar cannot sequential read an archive, which is the only way beside using an isolated catalogue to use an archive that has a corrupted catalogue or has no catalogue at all, thing that happens if a system crash occurred during the archive creation or due to lack of disk space to complete the archive.</p>
<dt>-0, &#8211;sequential-read</p>
<dd> Change dar&#8217;s behavior when reading an archive. By default, the traditional way is used, which relies on the table of contents (aka &quot;the catalogue&quot;) located at the end of the archive. With the &#8211;sequential-read option instead, dar will rely on escape sequences that are inserted all along the archive with each file&#8217;s inode information. This will lead to a sequential reading of the archive, operation suitable for tape medium. However, this feature is only available for archive format starting revision &quot;08&quot; (i.e.: since release 2.4.0) and if -at option has no been used during archive creation or merging. This option is available for archive testing (-t), comparison (-d), restoration (-x), listing (-l) and to read the archive of reference (-A option) for isolation (-C) and archive creation (-c). The sequential reading of an archive is always much slower than the usual reading method, so you should not use this option unless you really need it.</p>
<dt>-9, &#8211;min-digits &lt;num&gt;[,&lt;num ref&gt;[,&lt;num aux&gt;]]</p>
<dd> By default slice number contained in filename do not have any padded zeros, which, when sorting a directory contents alphabetically leads to read all the slice starting by &#8216;1&#8217;, then by &#8216;2&#8217;. for example, slice 1, 10, 11, 12, 13, &#8230; 2, 20, 21, 23, &#8230; etc. While dar is absolutely not perturbed by this display problem, some user shall like to have the slices sorted by order. For that reason, the &#8211;min-digits option lets you ask dar to prepend enough zeros in the slice number for it be as wide as the argument passed to &#8211;min-digits. For example, if you provide 3 for that number, dar will store the slice number as 001, 002, 003, &#8230; 999. Well, next slice will be 1000, thus it will break again the alphabetical sorting order. You are thus advised to use a number large enough to convert the number of slice you expect to use. Then, when reading your archive, you will also need to provide this same argument, else dar will fail finding the slice. In effect, when looking for slice 1 for example, dar should try opening the file &quot;basename.1.dar&quot;, but if it fails, it should try opening the file &quot;basename.01.dar&quot;, then &quot;basename.001.dar&quot;, &#8230; up to infinity. If the slice is just missing, dar would never ask you to provide it, being still looking for a slice name with an additional leading zero. The problem also arise when doing differential backup, merging or on-fly isolation, dar must know the number of zero to prepend for each of these archive. This is why the &#8211;min-digits option may receive up to three integer values, the first for the archive to create or read, the second for the archive of reference (-A option), the third for the auxiliary archive of reference (-@ option). By default, no zero is added, and it is also well working this way. But you might well set for example &quot;&#8211;min-digits 5,5,5&quot; in your ($HOME)/.darrc file to do it once and for all.</p>
<dt>&#8211;pipe-fd &lt;num&gt;</p>
<dd> will read further arguments from the file-descriptor &lt;num&gt;. The arguments read through this file-descriptor must follow a TLV (Type/Length/Value) list format. This option is not intended for human use, but for other programs launching dar like dar_manager. This feature has been added to overcome the command line length limit.</p>
<dt>-al, &#8211;alter=lax</p>
<dd> When reading an archive, dar will try to workaround data corruption of slice header, archive header and catalogue. This option is to be used as last resort solution when facing media corruption. It is rather and still strongly encourage to test archives before relying on them as well as using Parchive to do parity data of each slice to be able to recover data corruption in a much more effective manner and with much more chance of success. Dar also has the possibility to backup a catalogue using an isolated catalogue, but this does not face slice header corruption or even saved file&#8217;s data corruption (dar will detect but will not correct such event).</p>
<dt>&#8211;single-thread, -G</p>
<dd> When libdar is compiled against libthreadar, it can make use of several threads. The number of thread is not settable but depends on the number of features activated (compression, encryption, tape marks, sparse file, etc.) that require CPU intensive operations. The load-balancing type per thread used is called &quot;pipeline&quot;. As performance gain is little (not all algorithms are adapted to parallel computing) this feature is flagged as experimental: it has not been tested as intensively as other new features and it is not encouraged for use. If you want better performance, use several dar processes each for different directory trees. You&#8217;ll get several archives instead of one which isolated catalogues can be merged together (no need to merge the backups, just the isolated catalogues) and used as base for the next differential backup. Note: if you want to silent the initial warning about the fact this feature is experimental use -Q option before -G option.</dl>
<p> <code>SAVING, ISOLATION AND MERGING SPECIFIC OPTIONS (to use with -c, -C or -+)</code> </p>
<dl>
<dt>-z[[algo:]level], &#8211;compression[=[algo][:][level]]</p>
<dd> add compression within slices using gzip, bzip2, lzo or xz algorithm (if -z is not specified, no compression is performed). The compression level (an integer from 1 to 9) is optional, and is 9 by default. Be careful when using xz algorithm better specify a compression ratio less than or equal to 6 to avoid important memory requirements. A ratio of 1 means less compression and faster processing, while at the opposite a ratio of 9 gives the best compression but longest procesing time. &quot;Algo&quot; is optional, it specifies the compression algorithm to use and can take the following values &quot;gzip&quot;, &quot;bzip2&quot;, &quot;lzo&quot; or &quot;xz&quot;. &quot;gzip&quot; algorithm is used by default (for historical reasons see &#8211;gzip below). If both algorithm and compression are given, a &#8216;:&#8217; must be placed between them. Valid usage of -z option is for example: -z, -z9, -zlzo, -zgzip, -zbzip2, -zlzo:6, -zbzip2:2, -zgzip:1, -zxz:6 and so on. Usage for long option is the same: &#8211;compression, &#8211;compression=9, &#8211;compression=lzo, &#8211;compression=gzip, &#8211;compression=bzip2, &#8211;compression=lzo:6, &#8211;compression=bzip2:2, &#8211;compression=gzip:1 &#8211;compression=xz:9 and so on.</p>
<dt>&#8211;gzip[=level]</p>
<dd> Same as -z (see just above). This option is deprecated, please use &#8211;compression or -z.</p>
<dt>-s, &#8211;slice &lt;number&gt;</p>
<dd> Size of the slices in bytes. If the number is appended by k (or K), M, G, T, P E, Z or Y the size is in kilobytes, megabytes, gigabytes, terabytes, petabytes, exabytes, zettabytes or yottabytes respectively. Example: &quot;20M&quot; means 20 megabytes, by default, it is the same as giving 20971520 as argument (see also -aSI and -abinary options). If -s is not present the backup will be written to a single slice whatever the size of the backup may be (assuming your operating system can support arbitrarily large files).</p>
<dt>-S, &#8211;first-slice &lt;number&gt;</p>
<dd> -S gives the size of the first slice which may be chosen independently of the size of following slices (either bigger or smaller). This option needs -s option and by default of -S option, the size of the first slice is the same as the one of the following slices.</p>
<dt>-p [&lt;integer&gt;], &#8211;pause[=&lt;integer&gt;]</p>
<dd> pauses before writing to a new slice (this requires -s). By default there is no pause, all slices are written in the same directory, up to the end of the backup or until the filesystem is full. In this later case, the user is informed of the lack of disk space and dar stops for user action. As soon as some disk space is available, the user can continue the backup. The optional integer that this option can receive tells dar to only pause very &#8216;n&#8217; slice. Giving 3 for &#8216;n&#8217; will make dar pause only after slices 3, 6, 9 and so on. If this integer is not specified, the behavior is as if &#8216;1&#8217; was given as argument which makes dar pause after each slice.</p>
<dt>-D, &#8211;empty-dir</p>
<dd> At backup time, when excluding directories either explicitly using -P or -] options, or implicitly by giving a -g or -[ options (a directory is excluded if it does not match mask given with -g options or -[ options) <code>dar</code> does not store anything about these. But with -D option, dar stores them as empty directories. This can be useful, if excluding a mount point (like /proc or /dev/pts). At restoration time, dar will then recreate these directories (if necessary). This option has no meaning with -C and is ignored in that case. Independently of that, -D can also be used at restoration time, but it activates a slightly different feature (see restoration options below).</p>
<dt>-Z, &#8211;exclude-compression &lt;mask&gt;</p>
<dd> Filenames covered by this mask are not compressed. It is only useful in conjunction with -z option. By default, all file are compressed (if compression is used). This option can be used several times, in that case a file that matches one of the -Z mask will not be compressed. Argument given to -Z must not be include any path, just the filename (eventually/probably using wildcards).</p>
<dt>-Y, &#8211;include-compression &lt;mask&gt;</p>
<dd> Filenames covered by this mask (and not covered masks given to -Z option(s)) are the only to be compressed. It is only available with -z option. By default all files are compressed. This option can be used several times, in that case all files that match one of the -Y will be compressed, if they do not also match on of the -Z masks. The ordered method here applies too when activated (with -am option), it works exactly the same as -I and -X options, but apply to file compression, not file selection. In other word, it matches only on the file name, not on the path of files.</p>
<dt>-m, &#8211;mincompr &lt;number&gt;</p>
<dd> files which size is below this value will not be compressed. If -m is not specified it is equivalent to giving <code>-m 100</code> as argument. If you want to compress all file whatever their size is you thus need to type <code>-m 0</code> on the command line. The size unit is the byte (octet) and the same number extensions as those used with -s or -S are available here, if you want to specify the size in kilobyte, megabyte, gigabyte etc.</p>
<dt>-1, &#8211;sparse-file-min-size &lt;number&gt;</p>
<dd> Define the minimum length of zeroed bytes to replace by &quot;holes&quot;. By default, this feature is activated with a value of 15 bytes. To completely disable it, set the size to zero. Disabling this feature will bring some noticeable speed improvement but will probably make the archive slightly bigger (depending on the nature of the data). Sparse files are files that contain so called holes. On a filesystem, the portion of zeroed bytes is not stored on disk, thus an arbitrary large file with huge portion of zeros may only require a few bytes of disk storage. While dar cannot detect how is allocated a given file because it makes a filesystem abstraction (it does not know the implementation of any particular filesystem, where from its portability), however when it finds a sequence of zeroed bytes larger than the given threshold it can assume that it is in presence of a hole. Doing so, it does not store the given zeroed bytes into the archive, but place a tag beside the saved data to record the size of the hole and thus where to place the next no zeroed bytes. This makes dar archive disk space requirement much smaller when a sparse files is met. At restoration time, dar will restore holes writing normal data and seeking over the hole to write down the normal data after each hole. If the underlying file system supports sparse files, this will restore the holes. Note that there is no difference for applications whether a file is sparse or not, thus dar may well transform normal files into sparse files and viceversa, only the disk requirement will change. Last point, if dar can reduce disk requirement for archive with holes as small as 15 bytes (smaller value works but the overhead cost more than what is required to store the zeroed bytes normally), it may not be the same at restoration, because filesystem allocation unit is usually several kilobytes, however restored file will never be larger than it could be without holes. The only drawback of this feature is the additional CPU cycle it requires.</p>
<dt>-ak, &#8211;alter=keep-compressed</p>
<dd> During merging operation, keep files compressed, this has several restrictions : -z, -Z, -Y, -m are ignored, if two archives have to be merged, both must use the same compression algorithm or one of them must not use compression at all (this last restriction will probably disappear in a next version). The advantage of this option is a greater speed of execution (compression is usually CPU intensive).</p>
<dt>-ah, &#8211;alter=holes-recheck</p>
<dd> For merging, the sparse file detection mechanism is disabled by default. However if you want to activate it (assuming you have an old archive you want to convert the current archive format taking care of sparse files), you need to use -ah option to reactivate the sparse file detection mechanism. Then for merging &#8211;sparse-file-min-size can be used as described above for archive creation. In particular setting &#8211;sparse-file-min-size to zero beside -ah during merging, may also be used to convert file saved as sparse file into plain normal files.</p>
<dt>&#8211;nodump</p>
<dd> do not save files which have the &#8216;d&#8217; flag set (see <a href="/docs/linux/man/1-chattr/">chattr</a>(1) <a href="/docs/linux/man/1-lsattr/">lsattr</a>(1) ext2 commands). This option may not be available if the system dar has been compiled on did not provide support for ext2 flags. Note that this option does nothing with -+ option (merging) as no filesystem is used for that operation.</p>
<dt>-5, &#8211;exclude-by-ea[=&lt;extended attribute name&gt;]</p>
<dd> exclude inodes from backup that have been set with the EA given in argument. If not argument is given to that option the default EA used to exclude files from backup is &quot;user.libdar_no_backup&quot;. To set this attribute to a given file, use the following command: &quot;setfattr -n user.libdar_no_backup &lt;filename&gt;&quot;, to remove it: &quot;setfattr -x user.libdar_no_backup &lt;filename&gt;&quot;. Last, to check the presence this EA: &quot;getfattr &lt;filename&gt;&quot;</p>
<dt>-M, &#8211;no-mount-points</p>
<dd> stay in the same filesystem as the root directory (see -R option), subdirectory that are mounting points for other filesystems will not be saved (or saved empty if -D option is used). This option is useless and ignored for merging operation.</p>
<dt>-, , &#8211;cache-directory-tagging</p>
<dd> don&#8217;t save contents of directories that use the Cache Directory Tagging Standard. See <a rel="nofollow" href="http://www.brynosaurus.com/cachedir/spec.html">http://www.brynosaurus.com/cachedir/spec.html</a> for details. (this option is useless with -+ option)</p>
<dt>-/ , &#8211;overwriting-policy &lt;policy&gt;</p>
<dd> This option let the user define when or how file overwriting can occur at restoration or archive merging time. It does no apply to slice overwriting which are driven by the -n option, it does instead apply to file during extraction and files inside archives when merging two of them. When considering overwriting, a file is said to be &#8216;in place&#8217; while an other is known as &#8216;new&#8217; or &#8216;to be added&#8217;. At restoration time, the &#8216;in place&#8217; is the one that is present in filesystem while the &#8216;to be added&#8217; is the one from the archive. At merging time, the &#8216;in place&#8217; is the one of the &#8216;-A&#8217; archive of reference while the &#8216;to be added&#8217; is the one from the auxiliary &#8216;-@&#8217; archive or reference.</p>
<dl>
<dt>
<dd>
<p> As soon as you use -/ option -n only applies only to slice overwriting and the -r, -k and -ae options are ignored (restoration options). </p>
<p> The given &lt;policy&gt; argument is composed of actions and eventually of conditional expressions. Actions do define how to solve overwriting conflict about file&#8217;s data on one side and file&#8217;s Attributes (Extended and Filesystem Specific) on the other side. An action is thus a couple of action for Data and for EA+FSA. Actions for Data are represented by uppercase letters, while action for EA+FSA are defined by lowercase letters. Both actions are independent of each other:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>P</p>
<dd> means &#8216;Preserve&#8217;. When merging two archives, the data of the resulting archive will be taken from the &#8216;in place&#8217; file. While when extracting, the data of the inode in filesystem will be preserved (thus no overwriting will occur for the data).</p>
<dt>O</p>
<dd> means &#8216;Overwrite&#8217;. When merging two archives, the data of the resulting archive will be taken from the &#8216;to be added&#8217; file. While when extracting, the data of the inode in filesystem will be overwritten by data from the archive.</p>
<dt>S</p>
<dd> means &#8216;mark Saved and preserve&#8217;. When merging two archives, the data of the resulting archive will be marked as already saved in the archive of reference (making thus a differential archive, even if none of the original archive were differential archives). All data will be dropped in the resulting archive, but the last modification date [aka mtime] (used to detect change in file&#8217;s data) will be taken from the &#8216;in place&#8217; file. This action does not apply when extracting files, it is thus considered equal to &quot;Preserve&quot; (P) in that situation.</p>
<dt>T</p>
<dd> means &#8216;mark Saved and overwrite&#8217;. When merging two archives, the data of the resulting archive will be marked as already saved (same as &#8216;S&#8217; action): all data will be dropped in the resulting archive, however the last modification date [aka mtime] (used to detect changes in a file&#8217;s data) will be taken from the &#8216;to be added&#8217; file. This action does not apply when extracting files, it is thus considered equal to &quot;Overwrite&quot; (O) in that situation.</p>
<dt>R</p>
<dd> means &#8216;Remove&#8217;. When merging two archives, the resulting archive will not contain any entry corresponding to the file that were in conflict. This also implies that no EA will be stored for that particular entry as the entry will no more exist in the resulting archive (as if it had never yet existed). When extracting files, this will lead to file&#8217;s suppression.</p>
<dt>p</p>
<dd> means &#8216;Preserve&#8217;, same as &#8216;P&#8217; (but lowercase letter) preserve the whole EA set and FSA. When merging two archives, the Attributes set of the resulting file will be the ones of the &#8216;in place&#8217; file (whatever is the overwriting action taken for its data). While when extracting files to filesystem, the Attributes of the file in filesystem will not be changed (whatever is the overwriting action taken for its data, unless the file is removed using the &#8216;R&#8217; policy, which would remove the inode and thus also any Attributes it had).</p>
<dt>o</p>
<dd> means &#8216;Overwrite&#8217;, same as &#8216;O&#8217; (but lowercase letter) overwrite the whole EA set and FSA. When merging two archives, the Attributes set of the resulting file will be taken from the &#8216;to be added&#8217; file. While when extracting files, the Attributes set of the file in the filesystem will have its Attributes erased and replaced by those of the file in the archive (still independent of what overwriting action is taken for file&#8217;s data).</p>
<dt>s</p>
<dd> means &#8216;mark Saved and preserve&#8217;, same as &#8216;S&#8217; (but lowercase letter) for EA and FSA instead of data. When merging two archives, the EA and FSA of the resulting file are marked as already saved in the archive of reference, thus they are dropped but the date of last inode change [aka ctime] (used to detect changes in file&#8217;s EA and FSA) will be taken from the &#8216;in place&#8217; file. This action does not apply when extracting files, it is thus considered equivalent to &quot;Preserve&quot; (p) in that situation.</p>
<dt>t</p>
<dd> means &#8216;mark Saved and overwrite&#8217;, same as &#8216;T&#8217; (but lowercase letter) for EA and FSA instead of data. When merging two archives, the EA and FSA of the resulting file are marked as already saved in the archive of reference, thus they are dropped but the date of last inode change [aka ctime] (use to track changes in EA) will be taken from the &#8216;to be added&#8217; file. This action does not apply when extracting files, it is thus considered an equivalent to &quot;Overwrite&quot; (o) in that situation.</p>
<dt>m</p>
<dd> means &#8216;merge Attributes and preserve&#8217;. The resulting file in the merged archive will have Attribute entries from both the &#8216;in place&#8217; and the &#8216;to be added&#8217; files. If both files share a same Attribute entry (same FSA or for EA the same key for a given association) the one of the &#8216;in place&#8217; file is kept (where from the &#8216;preserve&#8217; notion). When extracting a file, the file in the filesystem will have its EA and FSA set enriched by the ones of the file in the archive that do not exist on filesystem, but its already existing Attributes will stay untouched.</p>
<dt>n</p>
<dd> means &#8216;merge Attributes and overwrite&#8217;. The resulting file in the merged archive will have Attribute entries from both the &#8216;in place&#8217; and the &#8216;to be added&#8217; files. If both files share a same Attribute entry (same FSA or for EA the same key for a given association) the one of the &#8216;to be added&#8217; file will be kept (where from the &#8216;overwrite&#8217; notion). When extracting file, the file in the filesystem will have its Attributes set enriched by ones of the file in the archive with some of them possibly been overwritten.</p>
<dt>r</p>
<dd> means &#8216;remove&#8217;, same as &#8216;R&#8217; but for the Attribute set (thus all EA and FSA entries) of a given file (&#8216;r&#8217; is lowercase letter here). The file of the resulting archive during merging operation will not own any EA nor any FSA, even if the &#8216;in place&#8217; and/or the &#8216;to be added&#8217; files did have some. For file extraction, this means that the file in the filesystem will loose all its EA set. The FSA cannot be &#8216;removed&#8217; from a filesystem and may not always have a default value, thus this action does not modify FSA at all in case of archive extraction. But in case of merging the FSA are removed as previously described. As for all the previous tests, this Attribute operation is independent of the operation chosen for file&#8217;s data (uppercase letters).</p>
<dt>d</p>
<dd> means &#8216;delete&#8217;. When a same EA or FSA entry is found both in the &#8216;in place&#8217; and &#8216;to be added&#8217; files, such entry will be absent in the resulting archive. In other words, when merging, the EA set and FSA will only contain EA and FSA entries specific to the &#8216;in place&#8217; and those specific to the &#8216;to be added&#8217; file. Entries in common will not be present. When extracting a file from an archive, the file on filesystem will have its EA set enriched by entries of the &#8216;to be added&#8217; file that are new to the &#8216;in place&#8217; file. The other EA entries (which are thus present in both archive and filesystem) will be removed from the set, which the other FSA will stay untouched (FSA cannot be &quot;removed&quot; from a filesystem, nor they always have a default value).</p>
<dt>*</p>
<dd> is valid for both EA and data. It tells that the action is not yet defined at this step of the evaluation and that further evaluation is required (see the &#8216;chain&#8217; operator below).</p>
<dt>A</p>
<dd> means &#8216;Ask for user decision&#8217;. This uppercase letter concerns Data overwriting. An application interaction let the user define the action for each file in conflict. Note, that this action if used alone may become very boring or painful. The idea is to use it in conditional statements (which are described below) to have dar ask for only non obvious cases.</p>
<dt>a</p>
<dd> means &#8216;Ask for user decision&#8217;. This lowercase letter is the equivalent for EA and FSA of the &#8216;A&#8217; action. It is intended to be used in the same conditional statements described below.</dl>
<p> An action is thus a couple of letters, the first being uppercase (for file&#8217;s data) the second being lowercase (for file&#8217;s EA and FSA). When -/ option is not given, the action is equivalent to &#8216;-/ Oo&#8217;, making dar proceed to file, EA and FSA overwriting. This is to stay as close as possible to the former default action where neither -n nor -w where specified. Note that -w option stays untouched, in consequences, in this default condition for -/ option, a confirmation will be asked to the user before dar proceed to any overwriting. The former -n option (still used to handle slice overwriting) can be replaced by its equivalent &#8216;-/ Pp&#8217; for resolving file overwriting conflict (never overwrite). Here follows some examples of actions, all these are done for any entry found in conflict during archive merging or archive extraction, we will see further how to define conditional actions.</p>
<dl>
<dt>-/ Rr</p>
<dd> will lead dar to remove any file from filesystem that ought to be restored(!). Note the action for EA/FSA is useless, the EA and FSA will always be erased as well as data using &#8216;R&#8217;. Thus &#8216;-/ Rp&#8217; would lead to the same result.</p>
<dt>-/ Po</p>
<dd> will keep data of the &#8216;in place&#8217; file and EA and FSA set from the &#8216;to be added&#8217; file.</p>
<dt>-/ Ss</p>
<dd> Using this option when merging an archive with itself (used both as archive of reference (-A option) and auxiliary archive of reference (-@ option) ) will provide the same action as an archive isolation of the archive of reference, but using twice more memory (so keep using the isolation operation as before! Here this is just an illustration of the possibility)</dl>
<p> As seem previously -u and -U options can be used to filter which EA entry to consider and which to ignore. The question here is to explain how this filtering mechanism interacts with the different policies we just presented above. For files that are not in conflict (found only as &#8216;in place&#8217; or as &#8216;to be added&#8217;), only the EA entries matching the EA filter are kept. For files in conflict, the overwriting policy is evaluated first, then the filtering mechanism is applied *after* it. Thus for example, using the following [ -/ &quot;Po&quot; -u &quot;*test&quot; ], when merging two archives, only EA ending with &quot;test&quot; will be retained, and when a conflict takes place, this &quot;*test&quot; ending EA will be taken from the &#8216;to be added&#8217; file if it has some EA of that type, its other EA entry will be ignored as well as any EA entry of the &#8216;in place&#8217; file even those ending by &quot;test&quot;. At restoration in using the same options, file without conflict will get restored but only EA entry ending with &quot;test&quot; will be restored, and for file with conflict (already present in filesystem), EA set of file in filesystem will be removed and replaced the EA entries of the file in archive that ends by &quot;test&quot;, if some exist. </p>
<p> the situation is similar with FSA family scope and overwriting policy. Only FSA of a family present in the scope will be retained, the overwriting policy acts first then the FSA scope is applied. Note however that any FSA present on filesystem and excluded from the FSA scope are not touched. </p>
<p> Well, now let&#8217;s see how to bring some more fun using conditional statements in all these actions. The structure to use is the following:</p>
<dl>
<dt>{&lt;condition&gt;}[&lt;action if condition is true&gt;]</p>
<dd> This syntax let you place an action (as the ones we saw just above) inside the brackets &#8216;[&#8216; and &#8216;]&#8217; (for example [Pp]) that will take effect only if the evaluation of the &lt;condition&gt; is true. Stated that a such statement is a new type of action, you may have guessed that you may use it recursively: {&lt;condition1&gt;}[{&lt;condition2&gt;}[&lt;action&gt;]).</dl>
<p> Well so far it seems useless. But instead of the &quot;if &lt;condition&gt; then &lt;action&gt; else &lt;action&gt;&quot; paradigm common to programming languages, due to the command line context it has been chosen to instead use and implicit &quot;OR&quot; operator between actions. Thus you can &quot;stack&quot; conditional statements this way: {&lt;condition1&gt;}[&lt;action1&gt;] {&lt;condition2&gt;}[&lt;action2&gt;] &lt;action3&gt;. In this example, if &lt;condition1&gt; is true then &lt;action1&gt; will be used, ELSE if &lt;condition2&gt; is true then &lt;action2&gt; will be used ELSE &lt;action3&gt; will be used. This leads to the same possibilities as what is available with programming languages, but with a slightly more simple syntax. Seen this, the recursion of conditional syntax is more interesting. For readability, you are allowed to add any space or tab in the overwriting policy, but the resulting overwriting policy must be given as a single argument to dar, thus the use of quotes (either simple &#8216;arg&#8217; or double &quot;arg&quot;) is necessary. </p>
<p> The last operator we will see is the &#8216;chain&#8217; operator. Once an expression is evaluated, the resulting couple of action may contain an &#8216;*&#8217; (undefined action for EA or data). Further evaluation must be done. The chain operator which is represented by a semi-column &#8216;;&#8217; let one to separate several independent expressions that will be evaluated in turn up to the time the couple of action is fully defined. Once an action (for EA or for Data) is defined, it can be redefined by a subsequent evaluation in the chain, however if the action is defined it cannot be set back to undefined, thus &#8216;*&#8217; will never overwrite a previously defined action. If at the end of the policy the couple of action is not fully defined, the &#8216;preserve&#8217; action is used (&#8216;P&#8217; or &#8216;p&#8217; depending on which of EA or Data is left undefined). Here follow a example of syntax:</p>
<dl>
<dt>-/ &quot;{&lt;condition1&gt;}[P*] O* ; {&lt;condition2&gt;[*p] *o} ; Rr&quot;</p>
<dd> The first expression will evaluate to either P* or O*. At this step, as the action is not completely defined, the second part of the chain is evaluated, It will end with either *p or *o. In any case, we have after this second statement of the chain a fully defined action for both data and EA (either Pp, Po, Op or Oo). Thus the evaluation stops here and the &quot;Rr&quot; policy will never be evaluated.</dl>
<p> We now have one last thing to see: the available conditions (what to place between braces &#8216;{&#8216; and &#8216;}&#8217;). Conditions are defined each by a letter, eventually followed by an argument between parenthesis. The usual logical operators are available: negation (!), conjunction (&amp;) disjunction (|). These characters must be escaped or quoted to not be interpreted by the shell when used on command-line. In particular the &#8216;!&#8217; under most shell must be quoted and escaped (-/ &#8216;{\!R}[..]..&#8217;, The escape character &#8216;\&#8217; is not necessary inside DCF files (those given to -B option) as no shell is used to interpret these files. To these usual operators has been added a new one: the &quot;inversion&quot; operator, noted &#8216;~&#8217;. Like the negation, it is an unary operator but unlike the negation, it inverses the roles of &#8216;in place&#8217; and &#8216;to be added&#8217; for the evaluation, which is slightly different from taking the negation of the result of the evaluation. All these operators follow the usual precedence: unary operators (&#8216;!&#8217; and &#8216;~&#8217;) are evaluated first, then the conjunction &#8216;&amp;&#8217; then the disjunction &#8216;|&#8217;. To override this, you can use parenthesis &#8216;(&#8216; and &#8216;)&#8217; inside the condition. Over these logical operators, the conditions are based on atomic operator that compare the &#8216;in place&#8217; file to the &#8216;to be added&#8217; file. Here they follow:</p>
<dl>
<dt>I</p>
<dd> true only if the &#8216;in place&#8217; entry is an inode (a &#8216;detruit&#8217; which record the fact that a file has been removed since the archive of reference is not an inode for example). This condition do not have any consideration toward the to be added object. Note that ~I can be used to check the nature of the &#8216;to be added&#8217; object.</p>
<dt>D</p>
<dd> true only if the &#8216;in place&#8217; entry is a directory. To know whether the &#8216;to be added&#8217; is a directory or not, one would use the &quot;inversion&quot; operator: ~D</p>
<dt>F</p>
<dd> true only if the &#8216;in place&#8217; entry is a plain file (true also if this plain file is a &#8216;hard link&#8217;, that&#8217;s it if its inode is linked several times to the directory tree)</p>
<dt>H</p>
<dd> true only if the &#8216;in place&#8217; entry is an inode linked several times to the directory tree (= hard link) it may be a plain file, a Unix socket, a pipe, char device, a block device for example.</p>
<dt>A</p>
<dd> same as H but the current &#8216;in place&#8217; entry is the first link we meet pointing to that hard linked inode.</p>
<dt>R</p>
<dd> true if the &#8216;in place&#8217; entry is more recent than or of same date as the &#8216;to be added&#8217; entry. The last modification date [aka mtime] is used for this comparison. If the &#8216;to be added&#8217; entry is not an inode (and thus has no mtime), the &#8216;in place&#8217; is considered to be more recent than the &#8216;to be added&#8217; entry. Same thing if the &#8216;in place&#8217; entry is not an inode (ad has no mtime available for comparison), it is here too assumed to be more recent.</p>
<dt>R(&lt;date&gt;)</p>
<dd> true if the &#8216;in place&#8217; entry is more recent than or of the same date as the fixed &lt;date&gt; given in argument. No consideration is done toward the &#8216;to be added&#8217; element. The &lt;date&gt; format is the same as the one used with -af option. If an entry has no mtime (it is not an inode for example) it is assumed an virtual mtime of zero.</p>
<dt>B</p>
<dd> true only if both &#8216;in place&#8217; and &#8216;to be added&#8217; are plain file (hard linked or not) and if the &#8216;in place&#8217; file&#8217;s data is larger or equal to the &#8216;to be added&#8217; file&#8217;s data. If one or both entry are not plain files (or hard link to plain file) and thus the file size comparison is not possible, the &#8216;in place&#8217; entry is assumed to be &#8216;bigger&#8217; than the &#8216;to be added&#8217; entry.</p>
<dt>S</p>
<dd> true only if the &#8216;in place&#8217; data is saved in the archive (not marked as unchanged since the archive of reference). Note that while extracting files from an archive, the &#8216;in place&#8217; file is the one in the filesystem, which always has its data &#8216;saved&#8217; (from libdar point of view). The &#8216;inversion&#8217; of this atomic operator ~S may still be interesting in the context of restoration.</p>
<dt>Y</p>
<dd> true only if the &#8216;in place&#8217; data is saved but dirty (plain file having its data changed at the time it was read for backup). Note, that restoring in sequential read mode, it is not possible to known whether a file is dirty (it is possible to know it once having read its data, but sequential reading does not allows then to skip forward to get the dirty state of the file and skip backward to eventually restore that file, depending on the overwriting policy result).</p>
<dt>X</p>
<dd> true only if the &#8216;in place&#8217; data is a sparse file</p>
<dt>T</p>
<dd> true only if the &#8216;in place&#8217; and &#8216;to be added&#8217; entries are of same type (plain file, Unix socket, named pipe, block device, char device, symlink, directory, &#8216;detruit&#8217; (which stands for file deleted since the archive of reference was done), and so on). Note that the number of links to inode (i.e. whether this is a hard links or not) is not taken into account.</p>
<dt>e</p>
<dd> true if the &#8216;in place&#8217; entry has EA (may they be saved or just recorded as existing).</p>
<dt>r</p>
<dd> true if the &#8216;in place&#8217; entry has more recent or equal dated EA to the &#8216;to be added&#8217; entry. If &#8216;to be added&#8217; has no EA or is even not an inode, true is returned. If &#8216;in place&#8217; has no EA or is even not an inode, true is returned unless &#8216;to be added&#8217; has some EA. The comparison is done on ctime dates.</p>
<dt>r(&lt;date&gt;)</p>
<dd> true if the &#8216;in place&#8217; entry has more recent or equal dated EA to the fixed &lt;date&gt; given in argument. No consideration is done toward the &#8216;to be added&#8217; element. The &lt;date&gt; format is the same as the one used with -af option. If an entry has no date (ctime date) (when it is not an inode for example) it is assumed an virtual ctime of value zero.</p>
<dt>m</p>
<dd> true only if &#8216;in place&#8217; has more or equal number of EA entry in its set of EA than &#8216;to be added&#8217; has. If an entry has not EA or is not even an inode, it is assumed it has zero entry. The comparison is done on this number. Note that the number of EA entry is not the size used to store these entries. For example, the EA entry &quot;user.test&quot; counts for 1, whatever is the length of the value associated to it.</p>
<dt>b</p>
<dd> true if the &#8216;in place&#8217; entry has bigger EA set or equal size EA set than the &#8216;to be added&#8217; entry. If an entry has no EA or is even not an inode, it is assumed that it has a zero byte length EA set. The comparison is done on this number in that case. Note that the comparison is done on the bytes used to store the whole EA set associated to a given file.</p>
<dt>s</p>
<dd> true if the &#8216;in place&#8217; entry is an inode (or a hard linked inode) and has its EA saved in the archive of reference, not only marked present but unchanged since last backup. This test does not take the &#8216;to be added&#8217; entry into account.</dl>
<p> Well, you&#8217;ve seen that uppercase letter are kept when comparison is based on the inode or data while lowercase letter is used for atomics based on EA. Now that we have completed our tour of this feature let&#8217;s see some examples:</p>
<dl>
<dt>-/ Pp</p>
<dd> as seen previously this is what does -n option for files when no overwriting policy is defined, which avoids any overwriting for Data as well as for EA.</p>
<dt>-/ &quot;{!T}[Pp] {R}[{r}[Pp]Po] {r}[Op] Oo&quot;</p>
<dd> Space and tabs are allowed to ease readability. Here the policy stands for: If files in conflicts are not of the same type then keep Data and EA of the entry &#8216;in place&#8217;. Else if &#8216;in place&#8217; has a more recent data then if &#8216;in place&#8217; has more recent EA then keep both its Data and EA, else keep only its Data and overwrite its EA. Else (if &#8216;in place&#8217; has not the more recent data), if it has the more recent EA then overwrite the data but keep its EA, else overwrite both its data and EA. This policy tends to preserve the most recent data or EA, but it does not take into account the fact that EA or Data is effectively saved into the archive of just marked as unchanged since the archive of reference.</p>
<dt>-/ &quot;{!T}[{~D}[Oo] Pp]&quot;</p>
<dd> If entries are not of the same type, if the &#8216;to be added&#8217; entry is a directory then we keep it and overwrite the &#8216;in place&#8217; entry, else we keep the &#8216;in place&#8217; entry. If entry are of same type, the policy does not provide any action, thus the default action is used: &quot;Pp&quot;. You can change this default action easily using a chain operator:</p>
<dt>-/ &quot;{!T}[{~D}[Oo] Pp] ; Aa&quot;</p>
<dd> In this case instead, if entry are of the same type, the user will be asked what to.</p>
<dt>-/ &quot;{!T|!I}[{R}[Pp] Oo] {S}[{~S}[{R}[P*] O*] P*] {~S}[O*] {R}[P*] O*] ; {s}[{~s}[{r}[*p] *o] *p] {~s}[*o] {r}[*p] *o]&quot;</p>
<dd> Well this may seems a bit too complex but just see it as an illustration of what is possible to do: If both &#8216;in place&#8217; and &#8216;to be added&#8217; are not of the same type we keep data and EA of the most recent file (last modification date). Else, both are of the same type. If both are inode we evaluate a two expressions chain (expressions are separated by a semi-column &#8216;;&#8217;) we will see in detail further. Else if they are of same type but are not inode we take the EA and data of the most recent entry (this is the last 10 chars of the string). Well, now let&#8217;s see the case of inode: The first expression in the chain sets the action for data and keep the action for EA undefined. While the seconds, is the exact equivalent but instead it leaves the action for data undefined &#8216;*&#8217; and set the action for EA. These two expressions follow the same principle: If both entries are saved (by opposition to be marked as unchanged since the archive of reference) in the archives, the most recent EA/Data is kept, else, the one of the inode that is saved is kept, but if none is saved in the archive the most recent entry (mtime/ctime) is kept.</dl>
</dl>
<dt>-^, &#8211;slice-mode perm[:user[:group]]</p>
<dd> defines the permission and ownership to use for created slices. By default, dar creates slices with read and write available for anyone letting the umask variable disable some privileges according to user&#8217;s preferences. If you need some more restricted permissions, you can provide the permission as an octal value (thus beginning by a zero), like 0600 to only grant read and write access to the user. Be careful not to avoid dar writing to its own slices, if for example you provide permission such as 0400. Note also that the umask is always applied thus specifying -^ 0777 will not grant word wide read-write access unless your umask is 0000.</p>
<dt>-_, &#8211;retry-on-change count[:max-byte]</p>
<dd> When a file has changed at the time it was read for backup, you can ask dar to retry saving it again. By default a file can be re-saved up to 3 times (this is the &#8216;count&#8217; field), you can set it to zero to disable this feature. In option the overall maximum amount of byte allowed to be wasted due to retry changing file&#8217;s backup can be given after a column charactrer (:), this is the &#8216;max-byte&#8217; field. By default (no &#8211;retry-on-change option specified) a limit of 1 wasted byte is allowed which is the mininum. Specifying zero for max-byte set no limit on the amount of wasted bytes (same as if no &#8216;max-byte&#8217; was specified), each changing file is then saved up to &#8216;count&#8217; times if necessary.</p>
<dl>
<dt>
<dd>
<p> A file is considered as changed when the last modification time has changed between the time the file has been opened for backup and the time it has been completely read. In some situation it is not possible to replace the already saved data for a file (writing archive to a pipe for example), in that situation only, a second copy of the file is added just after the first previous try which leads that previous try to becomes inaccessible, however it holds some place in the archive, where from the designation of &quot;wasted bytes&quot;. You can remove all wasted bytes from an archive using the merging/fitering feature: dar -+ new_arch -A old_arch -ak. </p>
<p> Note: since release 2.5.0, in normal condition no byte is wasted when a file changed at the time it was read for backup, except when doing a backup to pipe (using &#8216;-c -&#8216; option), except if the beginning of the modified file is located in a previous slice and except if slice hashing or strong encryption is used.</dl>
</dl>
<dl>
<dt>-ad, &#8211;alter=decremental</p>
<dd> This flag is to be used only when merging two archives. Instead of the usual merging where each files of both archives are added to the resulting archive with eventually a tie using the overwriting policy (see -/ option), here the merging builds an archive which corresponds to the decremental backup done based on two full backups. the -A backup is expected to receive the older archive while the -@ is expected to point to the more recent one. If this option is used, the eventually overwriting policy is ignored and replaced internally by -/ &quot;{T&amp;R&amp;~R&amp;(A|!H)}[S*] P* ; {(e&amp;~e&amp;r&amp;~r)|(!e&amp;!~e)}[*s] *p&quot;. Additionally, files found int the newer archive that do not existed in the older are replaced by a &#8216;detruit&#8217; entry, which marks them to be remove at restoration time. For more information about decremental backups read the usage_notes.html file in the documentation.</p>
<dt>-asecu, &#8211;alter=secu</p>
<dd> This option disable the ctime check done by default during an differential backup: If the ctime of an plain file has changed since the archive of reference was done while all other values stay unchanged (inode type, ownership, permission, last modification date), dar issues a &quot;SECURITY WARNING&quot;, as this may be the sign of the presence of a rootkit. You should use the -asecu option to disable this type of warning globally, if you are doing a differential backup of a just restored data (a differential backup with the archive used for restoration taken as reference). Effectively in that situation, as it is not possible to restore ctime, the restored data&#8217;s ctime will have changed while other parameters will be unchanged for all restored files, leading dar to issue a warning for all restored files. This security check is disabled (implicitly) if dar is run with -ac option. Last, if a file has only its EA changed since the archive of reference was done (new EA, removed EA, modified EA), the security warning will show (false positive).</p>
<dt>-., &#8211;user-comment &quot;&lt;message&gt;&quot;</p>
<dd> This option let the user add an arbitrary message into the archive header. Warning! this message is always stored in clear text, even if the archive is encrypted. You can see the message inserted in an archive displaying the archive summary (dar -l &lt;archive&gt; -q). Some macro can be used inside the &lt;message&gt;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%c</p>
<dd> is replaced by the command line used. Note that for security, any option related to archive encryption is removed (-K, -J, -$, -#, -*, -%). The command included from a DCF file (see -B option) are never added by this macro. As a consequence, if you do not want to see &#8211;user-comment stored in user comments you can add the &#8211;user-comment definition in an included file like ~/.darrc for example.</p>
<dt>%d</p>
<dd> this is the current date and time</p>
<dt>%u</p>
<dd> this is the uid under which dar has been run</p>
<dt>%g</p>
<dd> this is the gid under which dar has been run</p>
<dt>%h</p>
<dd> the hostname on which the archive has been created</p>
<dt>%%</p>
<dd> the % character.</dl>
</dl>
<dt>-3, &#8211;hash &lt;algo&gt;</p>
<dd> With this option set, when creating, isolating or merging an archive, beside each generated slices an on-fly hash file of the slice is created using the specified algorithm. Available algorithm are &quot;md5&quot;, &quot;sha1&quot; and &quot;sha512&quot;. By default no hash file is generated. The hash file generated is named based on the name of the slice with the .md5, .sha1 or .sha512 extension added to it at the end. These hash files can be processes by md5sum, sha1sum and sha512sum usual commands (md5sum -c &lt;hash file&gt;) to verify that the slice has not been corrupted. Note that the result is different than generating the hash file using md5sum or sha1sum once the slice is created, in particular if the media is faulty: calling md5sum or sha1sum on the written slice will make you compute the hash result on a possibly already corrupted file, thus the corruption will not be seen when testing the file against the hash at a later time. Note also that the creation of a hash file is not available when producing the archive on a pipe (&quot;dar -c -&quot;).</p>
<dt>-7, &#8211;sign email[,email[,&#8230;email]]</p>
<dd> When creating an archive with public key encryption (read -K option) it is also possible to sign it with one or more of your private key(s). At the difference of the hash feature above, only the randomly generated key used to cipher the archive, key that is dropped at the beginning and at the end of the archive, is signed. If the archive is modified at some place, that part will not be possible to decipher, but signature verification will stay quick and valid, unless the part that has been tempered is the key inside the archive in which case signature check will report a failure and archive will not be readable at all. If the signature is valid and the archive could be extracted without error, the whole archive could be assumed to be signed by the gnupg key owners, but read below the security note. See also GNUPGHOME in the ENVIRONMENT section at the end of this document.</p>
<dl>
<dt>
<dd>
<p> A summay information about the signature information is displayed while listing an archive in summary mode &quot;dar -l &lt;archive&gt; -q&quot;. For any operation involving a signed archive, a short message only shows if the archive is signed an one or more signature check failed, no message is displayed in case of successful signature check. This warning may be disabled using the &#8211;alter=blind-to-signatures command.</dl>
<dt>-ab, &#8211;alter=blind-to-signatures</p>
<dd> do not check whether an encrypted archive with public key that has also been signed have correct signatures.</p>
<dt>-&lt;, &#8211;backup-hook-include &lt;mask&gt;</p>
<dd> The mask is applied to path+filename during backup operation only. If a given file matches the mask, a user command (see -= option below) will be run before proceeding to the backup and once the backup will be completed. See also -&gt; option below. IMPORTANT: if using the short option, you need to enclose it between quotes: &#8216;-&lt;&#8216; for the shell not to interpret the &lt; as a redirection.</p>
<dt>-&gt; &#8211;backup-hook-exclude &lt;mask&gt;</p>
<dd> The mask is applied to path+filename during backup operation only. If a given file matches the mask, even if it matches a mask given after -&lt; option, no user command will be executed before and after its backup. The -&lt; and -&gt; options act like -g and -P, they can receive wildcard expression and thus have their comportment driven by the &#8211;alter=globe and &#8211;alter=regex expressions seen above, as well as the &#8211;alter=mask option. Last the &#8211;alter=case and &#8211;alter=no-case modify also the way case sensitivity is considered for these masks. By default, no -&gt; or -&lt; option, no file get selected for backup hook. IMPORTANT: if using the short option, you need to enclose it between quotes: &#8216;-&gt;&#8217; for the shell not to interpret the &gt; as a redirection.</p>
<dt>-=, &#8211;backup-hook-execute &lt;string&gt;</p>
<dd> for files covered by the mask provided thanks to the -&lt; and -&gt; options, the given string is executed before the backup of that file starts and once it has completed. Several macro can be used that are substituted at run time:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%%</p>
<dd> will be replaced by a literal %</p>
<dt>%p</p>
<dd> will be replaced by the full path under backup</p>
<dt>%f</p>
<dd> will be replaced by the filename (without the path)</p>
<dt>%u</p>
<dd> will be replaced by the UID of the file</p>
<dt>%g</p>
<dd> will be replaced by the GID of the file</p>
<dt>%c</p>
<dd> and most interesting, %c (c for context), will be replaced by &quot;start&quot; or by &quot;end&quot; when the command is executed before or after the backup respectively.</dl>
</dl>
<p> This way, one can stop a database just before it is about to be backed up, and restart it once the backup has completed. Note that the masks seen above that drive the execution of this command can be applied to a directory or a plain file for example. When a directory is selected for this feature, the command is logically ran before starting (with the context &quot;start&quot;) to backup any file located in that directory or in a subdirectory of it, and once all file in that directory or subdirectories have been saved, the command is ran a second time (with the context &quot;end&quot;). During that time, if any file do match the backup-hook masks, no command will be executed for these. It is assumed that when a directory has been asked for a backup-hook to be executed this hook (or user command) is prepare for backup all data located in that directory. The environment variable DAR_DUC_PATH also applies to these user commands (see -E above, or the ENVIRONMENT paragraph below).</p>
<dt>-ai, &#8211;alter=ignore-unknown-inode-type</p>
<dd> When dar meets an inode type it is not aware about (some times ago, it was the case for Door inode on Solaris for example, Door inodes are handled by dar since release 2.4.0), it issues a warning about its inability to handle such inode. This warning occurs even if that entry is filtered out by mean of -X, -I, -P, -g, -[ or -] options, as soon as some other entry in that same directory has to be considered for backup, leading dar to read that directory contents and failing on that unknown inode type (filtering is done based on the result of directory listing). This option is to avoid dar issuing such warning in that situation.</dl>
<p> <code>RESTORATION SPECIFIC OPTIONS (to use with -x)</code></p>
<dl>
<dt>-k[{ignored|only}], &#8211;deleted[={ignore|only}]</p>
<dd> Without argument or with the &quot;ignore&quot; argument, this option leads dar at restoration time to not delete files that have been deleted since the backup of reference (file overwriting can still occur). By default, files that have been destroyed since the backup of reference are deleted during restoration, but a warning is issued before proceeding, except if -w is used. If -n is used, no file will be deleted (nor overwritten), thus -k is useless when using -n. If -/ option is used, this option without argument is ignored! With the &quot;only&quot; argument, this option only consider files marked as to be removed in the archive to restore, no file are restored but some file are removed. When -konly (or &#8211;deleted=only) is used, the -/ option is ignored (at the opposition of the &quot;&#8211;no-delete=ignore&quot; option which is ignored when the -/ is used). Of course &quot;&#8211;no-delete=ignore&quot; and &quot;&#8211;no-delete=only&quot; are mutually exclusive, because if both of them were available at the same time dar would do nothing at all.</p>
<dt>-r, &#8211;recent</p>
<dd> only restore files that are absent or more recent than those present in filesystem. If -/ option is used, this option is ignored!</p>
<dt>-f, &#8211;flat</p>
<dd> do not restore directory structure. All file will be restored in the directory given to -R, if two files of the same name have to be restored, the usual scheme for warning (-w option) and overwriting (-n option) is used. No rename scheme is planned actually. When this option is set, dar does not remove files that have been stored as deleted since last backup. (-f implicitly implies -k).</p>
<dt>-ae, &#8211;alter=erase_ea</p>
<dd> [DEPRECATED use -/ instead] Drop all existing EA of files present in filesystem that will have to be restored. This way, the restored files will have the exact set of EA they had at the time of the backup. If this option is not given, a file to restore will have its EA overwritten by those present in the backup and if some extra EAs are present they will remain untouched. See the <code>Note concerning Extended Attributes (EA)</code> above for a detailed explanation about this behavior. If -/ option is used, this option is ignored!</p>
<dt>-D, &#8211;empty-dir</p>
<dd> At restoration time, if -D is not specified (default) any file and directory is restored in regard to the filtering mechanism specified (see -I, -X, -P, -g, -[ and -] options). But if -D option is provided the restoration skips directory trees that do not contain saved files. This avoid having a huge empty tree with a few restored files especially when restoring a differential archive in an empty place. Note: This feature cannot work when &#8211;sequential-read is used, as it is not possible to know whether a directory contains or not some saved files at the time the directory inode is read from the archive in sequential reading mode.</p>
<dt>-2, &#8211;dirty-behavior { ignore | no-warn }</p>
<dd> At restoration time, if a file in the archive is flagged as &quot;dirty&quot; (meaning that it had changed at the time it was saved), user is asked for confirmation before restoring it. Specifying &quot;ignore&quot; will skip those dirty files, while &quot;no-warn&quot; will restore them without user confirmation. This feature is incompatible with sequential reading mode, in this mode dar cannot know whether a file is dirty before having restored it. In consequences, in &#8211;sequential-read, once a file has been restored, if it is found to be dirty it will be removed unless dirty-behavior is set to &quot;no-warn&quot;.</p>
<dt>-/, &#8211;overwriting-policy &lt;policy&gt;</p>
<dd> Overwriting policy can be used for archive restoration to define when and how file overwriting can occur. See above the description of this option.</p>
<dt>-A, &#8211;ref [&lt;path&gt;]/&lt;basename&gt;</p>
<dd> The &#8211;ref option can be used with an isolated catalogue to rescue an archive that has a corruption in the catalogue part, see GENERAL OPTIONS above for more details.</dl>
<p> <code>TESTING AND DIFFERENCE SPECIFIC OPTIONS (to use with -t or -d)</code> </p>
<dl>
<dt>-ado-not-compare-symlink-mtime, &#8211;alter=do-not-compare-symlink-mtime</p>
<dd> With this option set, when comparing a symlink, no message shows when symlink in archive and symlink on filesystem do only differ by their mtime. See also -O option.</dl>
<p> No other specific option, but all general options are available except for example -w which is useless, as testing and comparing only read data. -A option is available as described in GENERAL OPTIONS to backup of internal catalogue of the archive (assuming you have a previously isolated catalogue available). </p>
<p> Doing a difference in sequential read mode is possible but hard linked inodes can only be compared to the filesystem the first time they are met, next hard links to this same inode cannot obtain the corresponding data because skipping backward in sequential read mode is forbidden. In that situation, the hard links are reported as skipped, meaning that data comparison could not be performed. </p>
<p> <code>LISTING OPTIONS (to use with -l)</code> </p>
<dl>
<dt>-T, &#8211;list-format=&lt;normal | tree | xml | slicing&gt;, &#8211;tree-format</p>
<dd>
<dl>
<dt>
<dd> By default, listing provides a tar-like output (the &#8216;normal&#8217; output). You can however get a tree-like output, an XML structured output or a output focusing on slice(s) where each file&#8217;s data, EA and FSA is located in. Providing -T without argument gives the same as providing the &#8216;tree&#8217; argument to it. The option &#8211;tree-format is an alias to &#8211;list-format=tree (backward compatibility). Note that the files doc/dar-catalog-*.dtd define the format of the XML output listing (This file is also installed under $PREFIX/share/doc) </p>
<p> the -Tslicing option can also be used with isolated catalogue generated with dar 2.5.0 or above, as isolated catalogues now contain a copy of the slicing layout of the archive of reference. However, if the archive of reference has been resliced (using dar_xform) after the isolated catalogue has been built, the slicing information would not be correct. For that corner case, you can use the -s and -S options with -Tslicing to specify what are the new slice sizes of the archive of reference.</dl>
<dt>-as, &#8211;alter=saved</p>
<dd> list only saved files</p>
<dt>-alist-ea, &#8211;alter=list-ea</p>
<dd> list Extended Attributes name for each file that has some.</p>
<dt>-I, -X, -P, -g, -[, -]</p>
<dd> can be used to filter file to list base on their name or path.</dl>
<p> From the general options it seems only -vm and -b stay useful here. Note that -vm displays an archive summary first, where a detailed of information about the archive can be obtained. If you want to display only this summary use -q with -l option.</p>
<dl>
<dt>displayed</p>
<dd> fields</p>
<dl>
<dt>
<dd>
<dl>
<dt>[data]</p>
<dd> possible values are [ ] or [Saved] or [InRef] or[DIRTY]. [ ] means that the data has not been saved because there is no change since backup of reference. [Saved] means that the data has been saved, and thus this archive is able to restore the file. [InRef] was used in archive generated by dar version 2.3.x and before, when isolating a catalogue from an archive and means that the file was saved in the reference archive. Last, [DIRTY] means that data is saved (like [Saved]) but has changed at the time dar was reading it for backup, leading dar to possibly store the file in a state it never had.</p>
<dt>[EA]</p>
<dd> possible values are &quot; &quot; (empty string) or [ ] or [InRef], [Saved] or [Suppr]. It Shows whether Extended Attributes are present and saved ([Saved]), are present but not saved ([ ]) which means there is no change since backup of reference, if there is no EA saved for this file (empty string) or if some EA were present in the archive of reference but none is currently available ([Suppr]). [InRef] was used when isolating a catalogue (release 2.3.x and before) from an archive and means that the file was saved in the reference archive.</p>
<dt>[FSA]</p>
<dd> Each character represent a FSA Family:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;L&quot;</p>
<dd> is the first character (L/l/-) representing ext2/3/4 FSA family</p>
<dt>&quot;H&quot;</p>
<dd> is the second character (H/h/-) representing HFS+ FSA family</p>
<dt>&quot;-&quot;</p>
<dd> the third character is reserved for future FSA family and is always a dash for now.</dl>
<p> Uppercase means the FSA set is saved, lowercase means the FSA is present in the archive of reference and has not changed since that time. Last a dash (-) means no FSA of that family has been saved for that file.</dl>
<dt>[compr]</p>
<dd> possible values are [&#8230;.%] or [&#8212;&#8211;] or [ ] or [worse]. Shows if the file has been compressed ([&#8230;%]) and the compression ratio reached &quot;(uncompressed-compressed)/uncompressed&quot;, for example [ 33%] means that the compressed data uses only 66% of the space required to store uncompressed data (33% of space saved thanks to compression), or if the file is stored without compression ([ ] see -m, -Y and -Z options) or if the file is not subject to compression because it is not a saved regular file ([&#8212;-]), or if the file takes more space compressed than its original size ([worse]), due to compression overhead. Note that 1% compression ratio brings quite no data reduction, while obviously 98% is a very performant compression (compressed file takes only 2% of the size required by the uncompressed date).</p>
<dt>[S]</p>
<dd> possible values are [ ] or [X]. [X] only applies to saved plain files, and tells that the file is stored using sparse file data structure: not all data is stored, long sequence of zeros are skipped. This also means that at restoration time, if the filesystem supports it, holes will be restored. To store hole information libdar uses escape sequence (special sequence of byte), but to avoid real data to be considered as such escape sequence, a special escape sequence is used when data looks like an escape sequence. So if a data contains a such escape sequence, it must be read as if it contains holes to be able to restore back the data in its original form. For that reason, in some rare circumstances (saving an dar archive inside a dar archive without compression or encryption, for example) a file without hole may be marked [X] as if it had holes and will be longer by on byte for each data sequence looking like an escape sequence.</p>
<dt>permission</p>
<dd> see ls man page. Note that a star (*) is prepended to the permission string if the corresponding inode is linked several times to the directory structure (hard link).</p>
<dt>user</p>
<dd> owner of the file</p>
<dt>group</p>
<dd> group owner of the file</p>
<dt>size</p>
<dd> size in byte of the file (if compression is enabled, the real size in the archive is &quot;compression rate&quot; time smaller).</p>
<dt>date</p>
<dd> the last modification date of the file. The last access time is also saved and restored, but not displayed.</p>
<dt>filename</p>
<dd> The name of the file.</p>
<dt>Extended Attributes</p>
<dd> When using -alist-ea option, for hard linked inode, the filename is followed by an integer between braces: Entries with the same number do point the the same inode.</p>
<dt>Slice(s)</p>
<dd> In -Tslice mode, each file is given the range of slices it is located in. If slice size is chosen particularily small, some slices may contain no file, EA, FSA data but only tape marks or the internal catalogue, leading the aggregation of reported slices not to cover all available slices of the archive.</dl>
</dl>
</dl>
<h2>EXPLICIT OPTIONAL ARGUMENTS</h2>
<p> When dar has not been compiled with GNU getopt, which is not present by default on some systems like FreeBSD, you may lack the optional arguments syntax. For example &quot;-z&quot; will create a parse error on command-line, or in -B configuration files. The solution is to explicitly give the argument. Here follows a list of explicit argument to use in place of optional ones:</p>
<dl>
<dt>-z</p>
<dd> must be replaced by -z 9</p>
<dt>-w</p>
<dd> must be replaced by -w d or -w default</p>
<dt>-H</p>
<dd> must be replaced by -H 1</p>
<dt>-0</p>
<dd> must be replaced by -0 ref</p>
<dt>-5</p>
<dd> must be replaced by -5 &quot;&quot;</p>
<dt>-p</p>
<dd> must be replaced by -p 1</p>
<dt>-v</p>
<dd> must be replaced by -v all</p>
<dt>-k</p>
<dd> must be replaced by -k ignore</p>
<dt>-5</p>
<dd> must be replaced by -5 user.libdar_no_backup</dl>
<p> <code>important !</code> When using GNU getopt(), optional arguments are available by sticking the argument to the short option: &quot;-z&quot; for example is available as well as &quot;-z9&quot;. But &quot;-z 9&quot; is wrong, it will be read as &quot;-z&quot; option and &quot;9&quot;, a command line argument (not an argument to the -z option). In the other side, when using a non GNU getopt this time, &quot;-z&quot; becomes an option that always requires an argument, and thus &quot;-z 9&quot; is read as &quot;-z&quot; option with &quot;9&quot; as argument, while &quot;-z9&quot; will be rejected as a unknown option, and &quot;-z&quot; alone will generate an error as no argument is provided. In consequences, you <code>need</code> a space between the option (like &quot;-z&quot;) and its argument (like &quot;9&quot;), when dar does not rely on a GNU getopt() call, which also imply you to explicitly use arguments to options listed just above. </p>
<h2>EXIT CODES</h2>
<p> <code>dar</code> exits with the following code:</p>
<dl>
<dt>0</p>
<dd> Operation successful.</p>
<dt>1</p>
<dd> Syntax error on command-line or DCF included file</p>
<dt>2</p>
<dd> Error due to a hardware problem or a lack of memory.</p>
<dt>3</p>
<dd> Detection of a condition that should never happen, and which is considered as a bug of the application.</p>
<dt>4</p>
<dd> Code issued when the user has aborted the program upon dar question from dar. This also happens when dar is not run from a terminal (for example launched from crontab) and dar has a question to the user. In that case, dar aborts the same way as if the user pressed the escape key at the question prompt.</p>
<dt>5</p>
<dd> is returned when an error concerning the treated data has been detected. While saving, this is the case when a file could not be opened or read. While restoring, it is the case when a file could not be created or replaced. While comparing, it is the case when a file in the archive does not match the one in the filesystem. While testing, it is the case when a file is corrupted in the archive.</p>
<dt>6</p>
<dd> an error occurred while executing user command (given with -E or -F option). Mainly because the creation of a new process is not possible (process table is full) or the user command returned an error code (exit status different from zero).</p>
<dt>7</p>
<dd> an error has occurred when calling a libdar routine. This means the caller (dar program), did not respect the specification of the API (and this can be considered as a particular case of bug).</p>
<dt>8</p>
<dd> the version of dar used is based in finite length integers (it has been compiled with the option &#8211;enable-mode=&#8230;). This code is returned when an integer overflow occurred. use the full version (based in the so called &quot;infinint&quot; class) to avoid this error.</p>
<dt>9</p>
<dd> this code indicates an unknown error. The exception caching code to take care of new exceptions has probably been forgotten to be update &#8230; this is a minor bug you are welcome to report.</p>
<dt>10</p>
<dd> you have tried to use a feature that has been disabled at compilation time.</p>
<dt>11</p>
<dd> some saved files have changed while dar was reading them, this may lead the data saved for this file not correspond to a valid state for this file. For example, if the beginning and the end of the file have been modified at the same time (while dar is reading it), only the change at the end will be saved (the beginning has already been read), the resulting state of the file as recorded by dar has never existed and may cause problem to the application using it. This is known as a &quot;dirty&quot; file in the archive. </p>
</dl>
<h2>SIGNALS</h2>
<p> If dar receives a signal (see <a href="/docs/linux/man/2-kill/">kill</a>(2) man page) it will take the default behavior which most of the time will abruptly abort the program, except for the following signals:</p>
<dl>
<dt>SIGINT</p>
<dd> This signal is generated by the terminal when hitting CTRL-C (with the terminal&#8217;s default settings), it can also be generated with the kill command</p>
<dt>SIGTERM</p>
<dd> This signal is generated by the system when changing of run-level in particular when doing a shutdown, it can also be generated with the kill command</p>
<dt>SIGHUP</p>
<dd> Depending on the system, this signal may be sent before the SIGTERM signal at shutdown time, it can also be generated with the kill command</p>
<dt>SIGQUIT</p>
<dd> This signal is generated by the terminal when hitting CTRL-\ (with the terminal&#8217;s default settings), it can also be generated with the kill command</p>
<dt>SIGUSR1</p>
<dd> This signal can be generated by the kill command</p>
<dt>SIGUSR2</p>
<dd> This signal can be generated by the kill command </p>
</dl>
<p> For those previous signals, two behavior exit. For SIGHUP, SIGINT, SIGQUIT, SIGTERM and SIGUSR1, a <code>delayed termination</code> is done: the backup or isolation operation is stopped, the catalogue is appended to the archive and the archive is properly completed with the correct terminator string, this way the generated archive is usable, and can be used as reference for a differential backup at a later time. Note that if an on-fly isolation had been asked, it will *not* be performed, and no user command will be launched even if dar has been configured for (-E option). For SIGUSR2 instead a <code>fast termination</code> is done: in case of backup or isolation, the archive is not completed at all, only memory and mutex are released properly. </p>
<p> For both type of termination and other operations than backup or isolation, dar&#8217;s behavior is the same: For restoration, all opened directories are closed and permissions are set back to their original values (if they had to be changed for restoration). For listing, comparison, testing, the program aborts immediately. </p>
<p> Another point, when using one of the previous signals, dar will return with the exist status <code>4</code> meaning that the user has aborted the operation. Note that answering &quot;no&quot; to a question from dar may also lead dar to exit this way. last, If before the end of the program the same signal is received a second time, dar will abort immediately. </p>
<h2>FILES</h2>
<p> <code>$HOME/.darrc</code> and <code>/etc/darrc</code> if present are read for configuration option. They share the same syntax as file given to -B option. If $HOME/.darrc is not present and only in that case, /etc/darrc is consulted. You can still launch /etc/darrc from .darrc using a statement like <code>-B /etc/darrc.</code> None of these file need to be present, but if they are they are parsed AFTER any option on the command line and AFTER included files from the command line (files given to the -B option). NOTE: if $HOME is not defined $HOME/.darrc default to /.darrc (at the root of the filesystem). </p>
<p> Else you can see <code>conditional syntax</code> below, and -N option above that leads dar to ignore the /etc/darrc and $HOME/.darrc files. </p>
<h2>CONDITIONAL SYNTAX</h2>
<p> configuration files (-B option, $HOME/.darrc and /etc/darrc) usually contain a simple list of command-line arguments, split or not over several lines, and eventually mixed with comments (see -B option for more). But, you can also use make-like targets to ask for a particular set of commands to be used in certain conditions. </p>
<p> A condition takes the form of reserved word immediately followed by a colon &#8216;:&#8217;. This word + colon must stand alone on its line, eventually with spaces or tabs beside it. The available conditions are:</p>
<dl>
<dt>extract:</p>
<dd> all option listed after this condition get used if previously on command line or file the -x option has been used</p>
<dt>create:</p>
<dd> all option listed after this condition get used if previously on command line or file (-B option) the -c option has been used</p>
<dt>list: (or listing:)</p>
<dd> if -l option has been used</p>
<dt>test:</p>
<dd> if -t option has been used</p>
<dt>diff:</p>
<dd> if -d option has been used</p>
<dt>isolate:</p>
<dd> if -C option has been used</p>
<dt>merge:</p>
<dd> if -+ option has been used</p>
<dt>reference:</p>
<dd> if -A option has been used (except when -A is used for the snapshot feature or in conjunction with -af)</p>
<dt>auxiliary:</p>
<dd> if -@ option has been used</p>
<dt>all:</p>
<dd> in any case</p>
<dt>default:</p>
<dd> if no -c, -d, -x, -t, -C, -l or -+ option has been used at this point of the parsing.</dl>
<p> The condition stops when the next condition starts, or at End of File. The commands inserted before any condition are equivalent to those inserted after the &quot;all:&quot; condition. Remark : -c -d -x -t -C and -l are mutual exclusive, only one of them can be used while calling dar. </p>
<p> Here is an example of conditional syntax</p>
<dl>
<dt>
<dd>
<p> create:<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>upon creation exclude the </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>following files from compression<br />
 -Z &quot;*.mp3&quot; -Z &quot;*.mpg&quot; </p>
<p> all:<br />
 -b<br />
 -p </p>
<p> default:<br />
 # this will get read if not<br />
 # command has been set yet<br />
 -V<br />
 # thus by default dar shows its version </p>
<p> all:<br />
 -v<br />
 # for any command we also ask to be verbose<br />
 # this is added to the previous all: condition</dl>
<p> Last point, you may have several time the same condition (several <code>all:</code> ) for example. They will be concatenated together. </p>
<h2>USER TARGETS</h2>
<p> User targets are arbitrary words found on command line, that do not start by a dash (&#8216;-&#8216;). On most system they should be placed after command and options. They are collected from command-line first, then comes the parsing of command and optional arguments. Their use is to extend conditional syntax described just above by having a set of options activated by the user just adding a single word on command-line. Of course user targets must not be equal to one of the reserved words of the conditional syntax (extract, create, &#8230; all, default). A valid target is a word (thus without space) composed of lowercase or uppercase letters (case is sensitive) with eventually digits, dashes &#8216;-&#8216; or underscores &#8216;_&#8217; characters. </p>
<p> Let&#8217;s see an example of use: </p>
<p> first a DCF file named &#8216;example.dcf&#8217; that will be given on command line: </p>
<dl>
<dt>
<dd> # normal set of files considered for backup </p>
<p> create:<br />
&nbsp;<wbr>&nbsp;<wbr>-R&nbsp;<wbr>/<br />
&nbsp;<wbr>&nbsp;<wbr>-P proc<br />
&nbsp;<wbr>&nbsp;<wbr>-P sys<br />
&nbsp;<wbr>&nbsp;<wbr>-P mnt<br />
&nbsp;<wbr>&nbsp;<wbr>-D </p>
<p> # if the &quot;home&quot; user target is applied on command line the following command get added </p>
<p> home:<br />
-g home </p>
<p> # if the &quot;verbose&quot; user target is used, we will have some more verbosity &#8230; </p>
<p> verbose:<br />
&nbsp;<wbr>&nbsp;<wbr>-v<br />
&nbsp;<wbr>&nbsp;<wbr>-vs</dl>
<p> Then we could run dar in the following ways:</p>
<dl>
<dt>dar -c test -B example.dcf</p>
<dd> in that case only the command in the &quot;create:&quot; section of example.dcf would be used.</p>
<dt>dar -c test -B example.dcf verbose</p>
<dd> here over the &quot;create:&quot; target the commands under the &quot;verbose:&quot; target (-v and -vs) would be also used</p>
<dt>dar -c test -B example.dcf verbose home</p>
<dd> last we use two user targets &quot;verbose:&quot; and &quot;home:&quot; in addition the the &quot;create:&quot; target of the usual conditional syntax.</dl>
<p> Note that if the last option *may* receive an argument, the first user target that follows it will be assumed an argument to that option. To avoid this, either change the order of options on command line for the last option been an option that never or always uses an argument (for example -b never has an argument while -s always has one). Or separate the options from the user targets by the &#8212; word. And of course you can also use the explicit argument of the last option (see EXPLICIT OPTIONAL ARGUMENT section, above). </p>
<p> Second point: It is allowed to have user targets inside a DCF file. Note however that targets are collected in a first phase, which leads some part of the file to be hidden (because the corresponding conditional syntax or user target is not present). Then, the remaining part of the file is then parsed and actions for each option found is taken. At that time, new user targets found are just recorded, but they do not modify the current DCF file layout, in particular, hidden part of the file stay hidden even if the corresponding user target is read in this same file. Next DCF parsing (which may be triggered by a second -B option on the command line, or by a -B option inside the current parsed DCF file) will thus be done with the additional targets found in that first DCF file, so in a way you may have user targets that activate other user targets, but they will be activated in starting the next -B file. Here follows an examples of two DCF files, first.dcf and second.dcf:</p>
<dl>
<dt>
<dd>
<p> # cat first.dcf<br />
&nbsp;<wbr>&nbsp;<wbr>target3:<br />
&nbsp;<wbr>-K toto </p>
<p>&nbsp;<wbr>&nbsp;<wbr>target1:<br />
&nbsp;<wbr>target2<br />
&nbsp;<wbr>-B second.dcf<br />
&nbsp;<wbr>target3 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>target2:<br />
&nbsp;<wbr>#never reached<br />
&nbsp;<wbr>-s 10k </p>
<p> # cat second.dcf<br />
&nbsp;<wbr>&nbsp;<wbr>target2:<br />
&nbsp;<wbr>-v<br />
&nbsp;<wbr>&nbsp;<wbr>target3:<br />
&nbsp;<wbr>-b </p>
</dl>
<p> In that example, target1 activates both target2 and target3, but at the time of the parsing of first.dcf, neither target2 nor target3 were yet activated thus &#8216;-K toto&#8217; and &#8216;-s 10k&#8217; will never be given to dar (unless activated beside target1 before first.dcf get parsed), however when comes the time to parse second.dcf, target2 *and* target3 are activated, thus both &#8216;-v&#8217; and &#8216;-b&#8217; will be passed to dar, even if &#8216;target3&#8217; is located after &#8216;-B second.dcf&#8217; in the file first.dcf </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>DAR_DCF_PATH</p>
<dd> if set, dar looks for Dar Configuration File (DCF files, see -B option) that do not have an fully qualified path in the directories listed in DAR_DCF_PATH environment variable. This variable receives a column (:) separated list of paths and look in each of them in turn, up to the first file found under the requested name.</p>
<dt>DAR_DUC_PATH</p>
<dd> if set, dar looks for Dar User Command (DUC files, see -E, -F, -~, -= options) that do not have a fully qualified path in the directories listed in DAR_DUC_PATH. This variable receives a column (:) separated list of paths and looks in each of them in turn, up to the first file found under the requested name.</p>
<dt>GNUPGHOME</p>
<dd> for asymetric encryption and signature, the keyring used is $HOME/.gnupg by default. You can change this default by setting GNUPGHOME to the directory containing the keyring. For example, if you are running dar as root and want to use your unprivileged account keyring use the following:</p>
<dl>
<dt>
<dd>
<p> export GNUPGHOME=~myaccount/.gnupg </p>
<p> dar -K gnupg:&#8230;@&#8230;,&#8230;@&#8230; &#8211;sign:&#8230;@&#8230; etc.</dl>
</dl>
<h2>EXAMPLES</h2>
<p> You can find some more examples of use in the tutorial, mini-howto, sample scripts, and other related documentation. All these are available in dar&#8217;s source package, and are also installed beside dar in the &lt;&#8211;prefix&gt;/share/dar directory. This documentation is also available on-line at <a rel="nofollow" href="http://dar.linux.free.fr/doc/index.html">http://dar.linux.free.fr/doc/index.html</a> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dar_xform/">dar_xform</a>(1), <a href="/docs/linux/man/1-dar_slave/">dar_slave</a>(1), <a href="/docs/linux/man/1-dar_manager/">dar_manager</a>(1), <a href="/docs/linux/man/1-dar_cp/">dar_cp</a>(1), <a href="/docs/linux/man/1-dar_split/">dar_split</a>(1), TUTORIAL and NOTES included in the source package and also available at <a rel="nofollow" href="http://dar.linux.free.fr/doc/index.html">http://dar.linux.free.fr/doc/index.html</a> </p>
<h2>KNOWN LIMITATIONS</h2>
<p> dar saves and restores atime, mtime, birthtime but cannot restore ctime (last inode change), there does not seems to be a standard call to do that under UNIX. </p>
<h2>KNOWN BUGS</h2>
<p> <a rel="nofollow" href="http://sourceforge.net/p/dar/bugs/">http://sourceforge.net/p/dar/bugs/</a> </p>
<h2>AUTHOR</h2>
<pre>
<a rel="nofollow" href="http://dar.linux.free.fr/">http://dar.linux.free.fr/</a>
Denis Corbin
France
Europe
</pre>
<h2>Index</h2>
