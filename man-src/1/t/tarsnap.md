---
title: "tarsnap(1)"
name: "tarsnap"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tarsnap/"
description: "tarsnap – manipulate remote encrypted backups"
---

<h2>NAME</h2>
<p> <code>tarsnap</code> &#8211; manipulate remote encrypted backups</p>
<h2>SYNOPSIS</h2>
<p> Br q Fl c &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>-cachedir </code><i>cache-dir</i> &#8211;<code>f </code><i>archive-name</i> [<i>options</i> ] [<i>files | directories</i> ]<br />
 Br q Fl d &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>-cachedir </code><i>cache-dir</i> &#8211;<code>f </code><i>archive-name</i> [<i>options</i> ]<br />
 Br q Fl t | Fl x &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>f </code><i>archive-name</i> [<i>options</i> ] [<i>patterns</i> ]<br />
 Br q Fl r &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>f </code><i>archive-name</i><br />
 Br q Fl -list-archives &#8211;<code>-keyfile </code><i>key-file</i><br />
 Br q Fl -print-stats &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>-cachedir </code><i>cache-dir</i> [-<code>f </code><i>archive-name</i> ]<br />
 Br q Fl -recover &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>-cachedir </code><i>cache-dir</i><br />
 Br q Fl -fsck &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>-cachedir </code><i>cache-dir</i><br />
 Br q Fl -fsck-prune &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>-cachedir </code><i>cache-dir</i><br />
 Br q Fl -nuke &#8211;<code>-keyfile </code><i>key-file</i></p>
<h2>DESCRIPTION</h2>
<p> creates, reads, deletes, and otherwise manages online backups. </p>
<p> The first option to is a mode indicator from the following list:</p>
<dl>
<dt><code>-c</code></p>
<dd> Create an archive containing the specified items and name.</p>
<dt><code>-d</code></p>
<dd> Delete the specified archive.</p>
<dt><code>-t</code></p>
<dd> List archive contents to stdout.</p>
<dt><code>-x</code></p>
<dd> Extract to disk from the archive.</p>
<dt><code>-r</code></p>
<dd> Read the specified archive, convert it to a tar stream, and write it to stdout.</p>
<dt><code>&#8211;list-archives</code></p>
<dd> Print the names of archives stored. If the &#8211;<code>v</code> flag is specified one or more times, the creation time of each archive is also printed; if the &#8211;<code>v</code> flag is specified two or more times, the command line with which was invoked to create each archive is also printed.</p>
<dt><code>&#8211;print-stats</code></p>
<dd> Print global statistics concerning the archives stored, and optionally information about individual archive(s). See &quot;PRINTING ARCHIVE STATISTICS&quot; below for information on the output format.</p>
<dt><code>&#8211;recover</code></p>
<dd> Recover a partial archive from a checkpoint if such an archive exists. This is also done automatically the next time an archive is created or deleted.</p>
<dt><code>&#8211;fsck</code></p>
<dd> Perform some integrity checks on the archives stored, and reconstruct the cache directory <i>cache-dir</i> In the unlikely event that there are corrupted archives, will exit and request that it be run with the &#8211;<code>-fsck-prune</code> option.</p>
<dt><code>&#8211;fsck-prune</code></p>
<dd> Run as &#8211;<code>-fsck</code> but if corrupt archives are detected, prune the broken data.</p>
<dt><code>&#8211;nuke</code></p>
<dd> Delete all of the archives stored. To protect against accidental data loss, will ask you to type the text &quot;No Tomorrow&quot; when using the &#8211;<code>-nuke</code> command.</dl>
<p> In &#8211;<code>c</code> mode, each specified file or directory is added to the archive in the order specified on the command line. By default, the contents of each directory are also archived. </p>
<p> In &#8211;<code>t</code> or &#8211;<code>x</code> mode, the entire command line is read and parsed before the archive is opened. The pathnames or patterns on the command line indicate which items in the archive should be processed. Patterns are shell-style globbing patterns as documented in <a href="/docs/linux/man/1-tcsh/">tcsh</a>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>@ archive-file </code></p>
<dd> (c mode only) The specified archive file is read and the entries in it will be appended to the current archive. As an example, </p>
<blockquote><p><tt></tt><code>-c &#8211;keyfile </code><i>key-file &#8211;</i><code>-cachedir </code><i>cache-dir &#8211;</i><code>f </code><i>mybackup </i><code>@ backup.tar </code> </p></blockquote>
<p> reads the archive file backup.tar from disk and stores it using <code>.</code></p>
<dt><code>@@ </code><i>archive-name</i></p>
<dd> (c mode only) The specified archive is read and the entries in it will be appended to the current archive.</p>
<dt><code>&#8211;aggressive-networking</code></p>
<dd> (c mode only) Use multiple TCP connections to send data to the server. If the upload rate is congestion-limited rather than being limited by individual bottleneck(s), this may allow tarsnap to use a significantly larger fraction of the available bandwidth, at the expense of slowing down any other network traffic.</p>
<dt><code>-C </code><i>directory</i></p>
<dd> (c and x modes only) In c mode, this changes the directory before adding the following files. In x mode, change directories after opening the archive but before extracting entries from the archive.</p>
<dt><code>&#8211;cachedir </code><i>cache-dir</i></p>
<dd> (c, d, print-stats, and fsck modes) Cache information about the archives stored by in the directory <i>cache-dir</i> The contents of this directory will not be backed up by <code>,</code> so it should not be used for any other purpose. If the directory <i>cache-dir</i> is lost, it can be reconstructed by running <code>&#8211;fsck</code></p>
<dt><code>&#8211;check-links</code></p>
<dd> (c mode only) Issue a warning message unless all links to each file are archived.</p>
<dt><code>&#8211;checkpoint-bytes </code><i>bytespercheckpoint</i></p>
<dd> (c mode only) Create a checkpoint after every <i>bytespercheckpoint</i> bytes of uploaded data. The value <i>bytespercheckpoint</i> must be at least 1000000, and a higher value is recommended since creating a checkpoint in an archive can take a few seconds and several hundred kB of bandwidth.</p>
<dt><code>&#8211;chroot</code></p>
<dd> (x mode only) Fn chroot to the current directory after processing any &#8211;<code>C</code> options and before extracting any files.</p>
<dt><code>&#8211;configfile </code><i>file</i></p>
<dd> Add <i>file</i> to the list of configuration files to be read; options set via these take priority over the default configuration files. This option can be specified multiple times, in which case all the files will be read; where settings conflict, the earlier configuration file will take priority.</p>
<dt><code>&#8211;disk-pause </code><i>X</i></p>
<dd> (c mode only) Pause for <i>X</i> ms between storing archive entries and after every 64 kB of file data. This will slow down and thereby reduce its impact on other applications. For archiving files which are stored on an ATA disk and are not in the operating system disk cache, a value of &#8211;<code>-disk-pause </code><i>10</i> will approximately double the time taken.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> (c mode only) Don&#8217;t really create an archive; just simulate doing so. The list of paths added to an archive (if the &#8211;<code>v</code> option is used) and statistics printed (if the &#8211;<code>-print-stats</code> option is used) will be identical to if is run without the &#8211;<code>-dry-run</code> option. </p>
<p> Note that the &#8211;<code>-maxbw</code> option does not work in combination with &#8211;<code>-dry-run</code> since no bandwidth is actually used, and that since does not contact the server when performing a dry run, it will not detect an attempt to create an archive with the same name as one which already exists.</p>
<dt><code>&#8211;exclude </code><i>pattern</i></p>
<dd> (c, x, and t modes only) Do not process files or directories that match the specified pattern. Note that exclusions take precedence over patterns or filenames specified on the command line.</p>
<dt><code>-f </code><i>archive-name</i></p>
<dd> (c, d, x, t, r, and print-stats modes only) Operate on the archive <i>archive-name</i> In mode c, if archive creation is interrupted by ^Q, the SIGQUIT signal, or reaching the bandwidth limit specified via a &#8211;<code>-maxbw</code> option, the archive will be stored with &quot;.part&quot; appended to its name. In mode print-stats, if <i>archive-name</i> is *, statistics will be printed for every archive. In the print-stats and d modes, &#8211;<code>f </code><i>archive-name</i> can be specified multiple times, in which case the operation (printing statistics, or deletion) will be performed for each of the specified archives. </p>
<p> Note that each archive created must have a different name; consequently many users find it useful to include timestamps in archive names when repeatedly creating archives from the same files/directories (e.g., daily backups).</p>
<dt><code>-H</code></p>
<dd> (c mode only) Symbolic links named on the command line will be followed; the target of the link will be archived, not the link itself.</p>
<dt><code>-h</code></p>
<dd> (c mode only) Synonym for &#8211;<code>L</code></p>
<dt><code>&#8211;humanize-numbers</code></p>
<dd> Use SI prefixes to make numbers printed by &#8211;<code>-print-stats</code> more readable.</p>
<dt><code>-I</code></p>
<dd> Synonym for &#8211;<code>T</code></p>
<dt><code>&#8211;include </code><i>pattern</i></p>
<dd> (c, x, and t modes only) Process only files or directories that match the specified pattern. Note that exclusions specified with &#8211;<code>-exclude</code> take precedence over inclusions. If no inclusions are explicitly specified, all entries are processed by default. The &#8211;<code>-include</code> option is especially useful when filtering archives. For example, the command </p>
<blockquote><p><tt></tt><code>-c -f </code><i>foo-backup &#8211;</i><code>-include=&#8217;*foo*&#8217; @@ </code><i>all-backup</i> </p></blockquote>
<p> creates a new archive <i>foo-backup</i> containing only the entries from <i>all-backup</i> containing the string `foo&#8217;</p>
<dt><code>&#8211;insane-filesystems</code></p>
<dd> (c mode only) Allow descent into synthetic filesystems such as procfs. Normally archiving of such filesystems is a silly thing to do, hence the name of the option.</p>
<dt><code>-k</code></p>
<dd> (x mode only) Do not overwrite existing files. In particular, if a file appears more than once in an archive, later copies will not overwrite earlier copies.</p>
<dt><code>&#8211;keep-newer-files</code></p>
<dd> (x mode only) Do not overwrite existing files that are newer than the versions appearing in the archive being extracted.</p>
<dt><code>&#8211;keyfile key-file </code></p>
<dd> (all modes) Obtain encryption, authentication, and access keys from <i>key-file</i> This file should have been generated by tarsnap-keygen1.</p>
<dt><code>-L</code></p>
<dd> (c mode only) All symbolic links will be followed. Normally, symbolic links are archived as such. With this option, the target of the link will be archived instead.</p>
<dt><code>-l</code></p>
<dd> This is a synonym for the &#8211;<code>-check-links</code> option.</p>
<dt><code>&#8211;lowmem</code></p>
<dd> (c mode only) Reduce memory usage by not caching small files. This may be useful when backing up files of average size less than 1 MB if the available RAM in kilobytes is less than the number of files being backed up.</p>
<dt><code>-m</code></p>
<dd> (x mode only) Do not extract modification time. By default, the modification time is set to the time stored in the archive.</p>
<dt><code>&#8211;maxbw </code><i>numbytes</i></p>
<dd> (c mode only) Interrupt archival if more than <i>numbytes</i> bytes of upstream bandwidth is used (see INTERRUPTING ARCHIVAL below for details).</p>
<dt><code>&#8211;maxbw-rate </code><i>bytespersecond</i></p>
<dd> Limit download and upload bandwidth used to <i>bytespersecond</i> bytes per second.</p>
<dt><code>&#8211;maxbw-rate-down </code><i>bytespersecond</i></p>
<dd> Limit download bandwidth used to <i>bytespersecond</i> bytes per second.</p>
<dt><code>&#8211;maxbw-rate-up </code><i>bytespersecond</i></p>
<dd> Limit upload bandwidth used to <i>bytespersecond</i> bytes per second.</p>
<dt><code>-n</code></p>
<dd> (c mode only) Do not recursively archive the contents of directories.</p>
<dt><code>&#8211;newer </code><i>date</i></p>
<dd> (c mode only) Only include files and directories newer than the specified date. This compares ctime entries.</p>
<dt><code>&#8211;newer-mtime </code><i>date</i></p>
<dd> (c mode only) Like &#8211;<code>-newer</code> except it compares mtime entries instead of ctime entries.</p>
<dt><code>&#8211;newer-than file </code></p>
<dd> (c mode only) Only include files and directories newer than the specified file. This compares ctime entries.</p>
<dt><code>&#8211;newer-mtime-than file </code></p>
<dd> (c mode only) Like &#8211;<code>-newer-than</code> except it compares mtime entries instead of ctime entries.</p>
<dt><code>&#8211;nodump</code></p>
<dd> (c mode only) Honor the nodump file flag by skipping this file.</p>
<dt><code>&#8211;noisy-warnings</code></p>
<dd> Be verbose when warning about network glitches. This is probably only useful for debugging purposes.</p>
<dt><code>&#8211;normalmem</code></p>
<dd> Ignore any <code>lowmem</code> or <code>verylowmem</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-aggressive-networking</code></p>
<dd> Ignore any <code>aggressive-networking</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-config-exclude</code></p>
<dd> Ignore any <code>exclude</code> option specified in a configuration file. Normally <code>exclude</code> options specified via configuration files and the command line all take effect.</p>
<dt><code>&#8211;no-config-include</code></p>
<dd> Ignore any <code>include</code> option specified in a configuration file. Normally <code>include</code> options specified via configuration files and the command line all take effect.</p>
<dt><code>&#8211;no-default-config</code></p>
<dd> Do not read the default configuration files /etc/tarsnap.conf and ~/.tarsnaprc</p>
<dt><code>&#8211;no-disk-pause</code></p>
<dd> Ignore any <code>disk-pause</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-humanize-numbers</code></p>
<dd> Ignore any <code>humanize-numbers</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-insane-filesystems</code></p>
<dd> Ignore any <code>insane-filesystems</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-maxbw</code></p>
<dd> Ignore any <code>maxbw</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-maxbw-rate-down</code></p>
<dd> Ignore any <code>maxbw-rate-down</code> option specified in a configuration file. If a <code>maxbw-rate</code> option is specified in a configuration file, it will not affect the download bandwidth used, but may affect the upload bandwidth used (unless &#8211;<code>-no-maxbw-rate-up</code> is also specified).</p>
<dt><code>&#8211;no-maxbw-rate-up</code></p>
<dd> Ignore any <code>maxbw-rate-up</code> option specified in a configuration file. If a <code>maxbw-rate</code> option is specified in a configuration file, it will not affect the upload bandwidth used, but may affect the download bandwidth used (unless &#8211;<code>-no-maxbw-rate-down</code> is also specified).</p>
<dt><code>&#8211;no-nodump</code></p>
<dd> Ignore any <code>nodump</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-print-stats</code></p>
<dd> Ignore any <code>print-stats</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-quiet</code></p>
<dd> Ignore any <code>quiet</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-snaptime</code></p>
<dd> Ignore any <code>snaptime</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-store-atime</code></p>
<dd> Ignore any <code>store-atime</code> option specified in a configuration file.</p>
<dt><code>&#8211;no-totals</code></p>
<dd> Ignore any <code>totals</code> option specified in a configuration file.</p>
<dt><code>&#8211;null</code></p>
<dd> (use with &#8211;<code>I</code> &#8211;<code>T</code> or &#8211;<code>X</code> Filenames or patterns are separated by null characters, not by newlines. This is often used to read filenames output by the &#8211;<code>print0</code> option to <a href="/docs/linux/man/1-find/">find</a>(1).</p>
<dt><code>&#8211;numeric-owner</code></p>
<dd> (x mode only) Ignore symbolic user and group names when restoring archives to disk, only numeric uid and gid values will be obeyed.</p>
<dt><code>-O</code></p>
<dd> (x and t modes only) In extract (-x) mode, files will be written to standard out rather than being extracted to disk. In list (-t) mode, the file listing will be written to stderr rather than the usual stdout.</p>
<dt><code>-o</code></p>
<dd> (x mode only) Use the user and group of the user running the program rather than those specified in the archive. Note that this has no significance unless &#8211;<code>p</code> is specified, and the program is being run by the root user. In this case, the file modes and flags from the archive will be restored, but ACLs or owner information in the archive will be discarded.</p>
<dt><code>&#8211;one-file-system</code></p>
<dd> (c mode only) Do not cross mount points.</p>
<dt><code>-P</code></p>
<dd> (c, x, and t modes only) Preserve pathnames. By default, absolute pathnames (those that begin with a / character) have the leading slash removed both when creating archives and extracting from them. Also, will refuse to extract archive entries whose pathnames contain .. or whose target directory would be altered by a symlink. This option suppresses these behaviors.</p>
<dt><code>-p</code></p>
<dd> (x mode only) Preserve file permissions. Attempt to restore the full permissions, including owner, file modes, file flags and ACLs, if available, for each item extracted from the archive. By default, newly-created files are owned by the user running <code>,</code> the file mode is restored for newly-created regular files, and all other types of entries receive default permissions. If is being run by root, the default is to restore the owner unless the &#8211;<code>o</code> option is also specified.</p>
<dt><code>&#8211;print-stats</code></p>
<dd> (c and d modes only) Print statistics for the archive being created (c mode) or delete (d mode). See &quot;PRINTING ARCHIVE STATISTICS&quot; below for information on the output format.</p>
<dt><code>-q ( &#8211;fast-read</code></p>
<dd> (x and t modes only) Extract or list only the first archive entry that matches each pattern or filename operand. Exit as soon as each specified pattern or filename has been matched. By default, the archive is always read to the very end, since there can be multiple entries with the same name and, by convention, later entries overwrite earlier entries. This option is provided as a performance optimization.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Avoid printing some warnings. Currently the warnings which are silenced by this option are &quot;Removing leading &#8216;/&#8217; &#8230;&quot;, &quot;Not adding cache directory to archive&quot;, &quot;&#8230; file may have grown while being archived&quot;, and &quot;Skipping entry on filesystem of type &#8230;&quot;, but it is likely that other warnings will be silenced by this option in future versions of <code>.</code></p>
<dt><code>-S</code></p>
<dd> (x mode only) Extract files as sparse files. For every block on disk, check first if it contains any non-NULL bytes and seek over it otherwise. This works similar to the conv=sparse option of dd.</p>
<dt><code>-s </code><i>pattern</i></p>
<dd> Modify file or archive member names according to pattern The pattern has the format /old/new/[gps]. old is a basic regular expression. If it doesn&#8217;t apply, the pattern is skipped. new is the replacement string of the matched part. ~ is substituted with the match, \1 to \9 with the contents of the corresponding captured group. The optional trailing g specifies that matching should continue after the matched part and stop on the first unmatched pattern. The optional trailing s specifies that the pattern applies to the value of symbolic links. The optional trailing p specifies that after a successful substitution the original path name and the new path name should be printed to standard error.</p>
<dt><code>&#8211;strip-components </code><i>count</i></p>
<dd> (x mode only) Remove the specified number of leading path elements. Pathnames with fewer elements will be silently skipped. Note that the pathname is edited after checking inclusion/exclusion patterns but before security checks.</p>
<dt><code>&#8211;snaptime file </code></p>
<dd> (c mode only) This option MUST be specified when creating a backup from a filesystem snapshot, and file must have a modification time prior to when the filesystem snapshot was created. (This is necessary to prevent races between file modification and snapshot creation which could result in failing to recognize that a file has been modified.)</p>
<dt><code>&#8211;store-atime</code></p>
<dd> (c mode only) Enable the storing of file access times. The default behaviour of is to not store file access times, since this can cause a significant amount of bandwidth and storage to be wasted when the same set of files are archived several times (e.g., if daily backup archives are created) due to itself accessing files and thereby causing their access times to be changed.</p>
<dt><code>-T </code><i>filename</i></p>
<dd> (c, x, and t modes only) In x or t mode, will read the list of names to be extracted from filename In c mode, will read names to be archived from filename The special name &#8220;-C&#8221; on a line by itself will cause the current directory to be changed to the directory specified on the following line. Names are terminated by newlines unless &#8211;<code>-null</code> is specified. Note that &#8211;<code>-null</code> also disables the special handling of lines containing &#8220;-C&#8221;</p>
<dt><code>&#8211;totals</code></p>
<dd> (c mode only) Print the size of the archive after creating it. This option is provided mainly for compatibility with GNU tar; in most situations the &#8211;<code>-print-stats</code> option will be far more useful.</p>
<dt><code>-U</code></p>
<dd> (x mode only) Unlink files before creating them. Without this option, overwrites existing files, which preserves existing hardlinks. With this option, existing hardlinks will be broken, as will any symlink that would affect the location of an extracted file.</p>
<dt><code>-v</code></p>
<dd> (c, t, x, and list-archives modes only) Produce verbose output. In create and extract modes, will list each file name as it is read from or written to the archive. In list mode, will produce output similar to that of <a href="/docs/linux/man/1-ls/">ls</a>(1). Additional &#8211;<code>v</code> options will provide additional detail.</p>
<dt><code>&#8211;verylowmem</code></p>
<dd> (c mode only) Reduce memory usage, by approximately a factor of 2 beyond the memory usage when &#8211;<code>-lowmem</code> is specified, by not caching anything.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version of <code>,</code> and exit.</p>
<dt><code>-w</code></p>
<dd> (c and x modes only) Ask for confirmation for every action.</p>
<dt><code>-X </code><i>filename</i></p>
<dd> (c, x, and t modes only) Read a list of exclusion patterns from the specified file. See &#8211;<code>-exclude</code> for more information about the handling of exclusions.</dl>
<h2>SIGNALS</h2>
<p> provides special treatment of the following signals:</p>
<dl>
<dt><code>SIGUSR1 &amp; SIGINFO</code></p>
<dd> On receipt of the SIGUSR1 signal or (on platforms where it exists) the SIGINFO signal, prints the current file or directory being processed, and (for files) its progress within the file. Note that due to network buffering this position will not align precisely with how much data has been sent to or received from the server.</p>
<dt><code>SIGUSR2</code></p>
<dd> On receipt of the SIGUSR2 signal, if is creating an archive (mode c), it will create a checkpoint at the current position.</p>
<dt><code>SIGQUIT</code></p>
<dd> On receipt of the SIGQUIT signal, if is creating an archive (mode c) it will truncate the archive at the current position and exit (see &quot;INTERRUPTING ARCHIVAL&quot; below).</dl>
<h2>PRINTING ARCHIVE STATISTICS</h2>
<p> Statistics on archives can be printed by running &#8211;<code>-print-stats</code> and during archive creation or deletion statistics on the created or deleted archive can be printed using the &#8211;<code>-print-stats</code> option. In either case, will print to the standard output a table in the following format: </p>
<pre>
                                       Total size  Compressed size
All archives                         104491640436      51510524844
  (unique data)                       14830618089       7733620463
This archive                            808723344        289077325
New data                                 17858641          5658308
</pre>
<p> In this example, the combined size of all archives stored by using the same keys is 104 GB, and the combined size post-compression would be 51 GB; but after removing duplicate blocks, there is only 14.8 GB which is compressed down to 7.7 GB. (It is this 7.7 GB which is stored via the Tarsnap service and must thus be paid for.) The newly created archive is 808 MB in size (compressible to 289 MB), but only 17.8 MB of the data is new, and after compression only 5.6 MB is uploaded to the Tarsnap server.</p>
<h2>INTERRUPTING ARCHIVAL</h2>
<p> Upon receipt of the <code>SIGQUIT</code> signal or Q, or if the bandwidth limit specified via a &#8211;<code>-maxbw</code> option is reached, will interrupt the creation of an archive and truncate it at the current position. When an archive is truncated, it will be named according to the user-specified name plus &quot;.part&quot; to denote the fact that it is incomplete. Such a truncated archive may be useful in its own right, but also offers the benefit that future attempts to archive the same data will be faster and use less bandwidth.</p>
<h2>FIREWALLS</h2>
<p> communicates with the server via a TCP connection to port 9279; in some environments it may be necessary to add a firewall rule to allow outgoing TCP connections to this port. At the present time (July 2009) there is only one IP address in use for the server, so network administrators may wish to hard-code that IP address; however, it is likely that at some point in the future that IP address will change and/or other IP addresses will be added.</p>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>:</code></p>
<dl>
<dt><code>LANG</code></p>
<dd> The locale to use. See <a href="/docs/linux/man/7-environ/">environ</a>(7) for more information.</p>
<dt><code>TZ</code></p>
<dd> The timezone to use when displaying dates. See <a href="/docs/linux/man/7-environ/">environ</a>(7) for more information.</dl>
<h2>EXIT STATUS</h2>
<p> Ex -std</p>
<h2>EXAMPLES</h2>
<p> Register with the server and generate keys: </p>
<blockquote><p><tt></tt><code>tarsnap-keygen &#8211;keyfile /usr/tarsnap.key &#8211;user </code><i>me [at] example.com &#8211;</i><code>-machine </code><i>myserver</i> </p></blockquote>
<p> Perform a backup of /usr/home and /other/stuff/to/backup </p>
<blockquote><p><tt></tt><code>&#8211;keyfile /usr/tarsnap.key &#8211;cachedir /usr/tarsnap-cache -c -f </code><i>backup-2008-04-24 /usr/home /other/stuff/to/backup </i> </p></blockquote>
<p> Perform another backup, a day later; this is much faster since tarsnap will avoid storing data which was previously stored: </p>
<blockquote><p><tt></tt><code>&#8211;keyfile /usr/tarsnap.key &#8211;cachedir /usr/tarsnap-cache -c -f </code><i>backup-2008-04-25 /usr/home /other/stuff/to/backup </i> </p></blockquote>
<p> List the archives: </p>
<blockquote><p><tt></tt><code>&#8211;keyfile /usr/tarsnap.key &#8211;list-archives</code> </p></blockquote>
<p> Delete the first backup, leaving the second backup intact: </p>
<blockquote><p><tt></tt><code>&#8211;keyfile /usr/tarsnap.key &#8211;cachedir /usr/tarsnap-cache -d -f </code><i>backup-2008-04-24</i> </p></blockquote>
<p> List the files in the remaining backup: </p>
<blockquote><p><tt></tt><code>&#8211;keyfile /usr/tarsnap.key -tv -f </code><i>backup-2008-04-25</i> </p></blockquote>
<p> Restore two users&#8217; home directories from the backup: </p>
<blockquote><p><tt></tt><code>&#8211;keyfile /usr/tarsnap.key -x -f </code><i>backup-2008-04-25 usr/home/auser usr/home/anotheruser </i> </p></blockquote>
<p> In /etc/crontab to create a backup of the entire system at 10:32 each day: </p>
<blockquote><p><tt>32 10 * * * root </tt><code>&#8211;keyfile /usr/tarsnap.key &#8211;cachedir /usr/tarsnap-cache -c -f </code><i>backup-`date +\%Y\%m\%d` / </i> </p></blockquote>
<p> Note that the &#8211;<code>-keyfile</code> and &#8211;<code>-cachedir</code> options can be specified via the tarsnap.conf5 configuration file, in which case they may be omitted from the command line.</p>
<h2>SECURITY</h2>
<p> Certain security issues are common to many archiving programs, including <code>.</code> In particular, carefully-crafted archives can request that extract files to locations outside of the target directory. This can potentially be used to cause unwitting users to overwrite files they did not intend to overwrite. If the archive is being extracted by the superuser, any file on the system can potentially be overwritten. There are three ways this can happen. Although has mechanisms to protect against each one, savvy users should be aware of the implications: </p>
<ul>
<li> Archive entries can have absolute pathnames. By default, removes the leading / character from filenames before restoring them to guard against this problem.
<li> Archive entries can have pathnames that include .. components. By default, will not extract files containing .. components in their pathname.
<li> Archive entries can exploit symbolic links to restore files to other directories. An archive can restore a symbolic link to another directory, then use that link to restore a file into that directory. To guard against this, checks each extracted path for symlinks. If the final path element is a symlink, it will be removed and replaced with the archive entry. If &#8211;<code>U</code> is specified, any intermediate symlink will also be unconditionally removed. If neither &#8211;<code>U</code> nor &#8211;<code>P</code> is specified, will refuse to extract the entry. </ul>
<p> Although cryptographically signs archives in such a manner that it is believed to be unfeasible for an attacker to forge an archive without having possession of <i>key-file</i> you may wish to examine the contents of archive(s) with </p>
<blockquote><p><tt></tt><code>-t &#8211;keyfile </code><i>key-file &#8211;</i><code>f </code><i>archive-name</i> </p></blockquote>
<p> before extraction. Note that the &#8211;<code>P</code> option to disables the security checks above and allows you to extract an archive while preserving any absolute pathnames, .. components, or symlinks to other directories.</p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/tarsnap.conf </code></p>
<dd> The system global configuration file. Parameters specified here only take effect if they are not specified via the current user&#8217;s local configuration file or via the command line.</p>
<dt><code>~/.tarsnaprc </code></p>
<dd> The configuration file for the current user. Parameters specified here take effect unless they are specified via the command line.</dl>
<h2>SEE ALSO</h2>
<p> tarsnap-keygen1, tarsnap.conf5, <a href="/docs/linux/man/5-tar/">tar</a>(5)</p>
<h2>HISTORY</h2>
<p> A <code>tar</code> command appeared in Seventh Edition Unix, which was released in January, 1979. There have been numerous other implementations, many of which extended the file format. John Gilmore&#8217;s <code>pdtar</code> public-domain implementation (circa November, 1987) was quite influential, and formed the basis of GNU tar. GNU tar was included as the standard system tar in FreeBSD beginning with FreeBSD 1.0, but was replaced by Tim Kientzle&#8217;s <code>bsdtar</code> utility and <a href="/docs/linux/man/3-libarchive/">libarchive</a>(3) library in FreeBSD 5.3. </p>
<p> is built around <code>bsdtar</code> and <a href="/docs/linux/man/3-libarchive/">libarchive</a>(3).</p>
<h2>BUGS</h2>
<p> This program follows St -p1003.1-96 for the definition of the &#8211;<code>l</code> option to <a href="/docs/linux/man/5-tar/">tar</a>(5). Note that GNU tar prior to version 1.15 treated &#8211;<code>l</code> as a synonym for the &#8211;<code>-one-file-system</code> option. </p>
<p> To archive a file called @foo @@foo or -foo you must specify it as ./@foo ./@@foo or ./-foo respectively. </p>
<p> In create mode, a leading ./ is always removed. A leading / is stripped unless the &#8211;<code>P</code> option is specified. </p>
<p> Hard link information may be lost if an archive file which is included via the <code>@ archive-file </code> option is in a non-&quot;tar&quot; format. (This is a consequence of the incompatible ways that different archive formats store hardlink information.) </p>
<p> There are alternative long options for many of the short options that are deliberately not documented. </p>
<p> The limit specified by a &#8211;<code>-maxbw</code> option is not strictly enforced; in particular, due to the need to cleanly terminate an archive, the amount of bandwidth used may slightly exceed the limit. </p>
<h2>Index</h2>
