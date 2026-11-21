---
title: "rdiff-backup(1)"
name: "rdiff-backup"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdiff-backup/"
description: "rdiff-backup – local/remote mirror and incremental backup"
---
<h2>NAME</h2>
<p> rdiff-backup - local/remote mirror and incremental backup  </p>
<h2>SYNOPSIS</h2>
<p> <code>rdiff-backup</code> <code>[</code><i>options</i><code>]</code> <code>[[[</code><i>user@</i><code>]</code><i>host1.foo</i><code>]::</code><i>source_directory</i><code>]</code> <code>[[[</code><i>user@</i><code>]</code><i>host2.foo</i><code>]::</code><i>destination_directory</i><code>]</code> </p>
<p> <code>rdiff-backup</code> <code>{{ -l | --list-increments }</code> <code>| --remove-older-than </code><i>time_interval</i> <code>| --list-at-time </code><i>time</i> <code>| --list-changed-since </code><i>time</i> <code>| --list-increment-sizes </code> <code>| --verify</code> <code>| --verify-at-time </code><i>time</i><code>}</code> <code>[[[</code><i>user@</i><code>]</code><i>host2.foo</i><code>]::</code><i>destination_directory</i><code>]</code> </p>
<p> <code>rdiff-backup --calculate-average</code> <i>statfile1 statfile2 ...</i> </p>
<p> <code>rdiff-backup --test-server</code> <code>[</code><i>user1</i><code>]</code><i>@host1.net1</i><code>::</code><i>path</i> <code>[[</code><i>user2</i><code>]</code><i>@host2.net2</i><code>::</code><i>path</i><code>]</code> <i>...</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>rdiff-backup</code> is a script, written in <code><a href="/docs/linux/man/1-python/">python</a></code>(1) that backs up one directory to another. The target directory ends up a copy (mirror) of the source directory, but extra reverse diffs are stored in a special subdirectory of that target directory, so you can still recover files lost some time ago. The idea is to combine the best features of a mirror and an incremental backup. rdiff-backup also preserves symlinks, special files, hardlinks, permissions, uid/gid ownership, and modification times. </p>
<p> <code>rdiff-backup</code> can also operate in a bandwidth efficient manner over a pipe, like <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1). Thus you can use ssh and rdiff-backup to securely back a hard drive up to a remote location, and only the differences will be transmitted. Using the default settings, rdiff-backup requires that the remote system accept ssh connections, and that <code>rdiff-backup</code> is installed in the user&#8217;s PATH on the remote system. For information on other options, see the section on <code>REMOTE OPERATION.</code> </p>
<p> Note that you <code>should not write to the mirror directory</code> except with rdiff-backup. Many of the increments are stored as reverse diffs, so if you delete or modify a file, you may lose the ability to restore previous versions of that file. </p>
<p> Finally, this man page is intended more as a precise description of the behavior and syntax of rdiff-backup. New users may want to check out the examples.html file included in the rdiff-backup distribution. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b, --backup-mode</code></dt>
<dd> <p> Force backup mode even if first argument appears to be an increment or mirror file. </p>
 </dd>
<dt><code>--calculate-average</code></dt>
<dd> <p> Enter calculate average mode. The arguments should be a number of statistics files. rdiff-backup will print the average of the listed statistics files and exit. </p>
 </dd>
<dt><code>--carbonfile </code></dt>
<dd> <p> Enable backup of MacOS X carbonfile information. </p>
 </dd>
<dt><code>--check-destination-dir</code></dt>
<dd> <p> If an rdiff-backup session fails, running rdiff-backup with this option on the destination dir will undo the failed directory. This happens automatically if you attempt to back up to a directory and the last backup failed. </p>
 </dd>
<dt><code>--compare</code></dt>
<dd> <p> This is equivalent to <code>&#8216;--compare-at-time</code><i> now</i><code>&#8216;</code> </p>
 </dd>
<dt><code>--compare-at-time </code><i>time</i></dt>
<dd> <p> Compare a directory with the backup set at the given time. This can be useful to see how archived data differs from current data, or to check that a backup is current. This only compares metadata, in the same way rdiff-backup decides whether a file has changed. </p>
 </dd>
<dt><code>--compare-full</code></dt>
<dd> <p> This is equivalent to <code>&#8216;--compare-full-at-time</code><i> now</i><code>&#8216;</code> </p>
 </dd>
<dt><code>--compare-full-at-time </code><i>time</i></dt>
<dd> <p> Compare a directory with the backup set at the given time. To compare regular files, the repository data will be copied in its entirety to the source side and compared byte by byte. This is the slowest but most complete compare option. </p>
 </dd>
<dt><code>--compare-hash</code></dt>
<dd> <p> This is equivalent to <code>&#8216;--compare-hash-at-time</code><i> now</i><code>&#8216;</code> </p>
 </dd>
<dt><code>--compare-hash-at-time </code><i>time</i></dt>
<dd> <p> Compare a directory with the backup set at the given time. Regular files will be compared by computing their SHA1 digest on the source side and comparing it to the digest recorded in the metadata. </p>
 </dd>
<dt><code>--create-full-path</code></dt>
<dd> <p> Normally only the final directory of the destination path will be created if it does not exist. With this option, all missing directories on the destination path will be created. Use this option with care: if there is a typo in the remote path, the remote filesystem could fill up very quickly (by creating a duplicate backup tree). For this reason this option is primarily aimed at scripts which automate backups. </p>
 </dd>
<dt><code>--current-time </code><i>seconds</i></dt>
<dd> <p> This option is useful mainly for testing. If set, rdiff-backup will use it for the current time instead of consulting the clock. The argument is the number of seconds since the epoch. </p>
 </dd>
<dt><code>--exclude </code><i>shell_pattern</i></dt>
<dd> <p> Exclude the file or files matched by <i>shell_pattern</i>. If a directory is matched, then files under that directory will also be matched. See the <code>FILE SELECTION</code> section for more information. </p>
 </dd>
<dt><code>--exclude-device-files</code></dt>
<dd> <p> Exclude all device files. This can be useful for security/permissions reasons or if rdiff-backup is not handling device files correctly. </p>
 </dd>
<dt><code>--exclude-fifos</code></dt>
<dd> <p> Exclude all fifo files. </p>
 </dd>
<dt><code>--exclude-filelist </code><i>filename</i></dt>
<dd> <p> Excludes the files listed in <i>filename</i>. If <i>filename</i> is handwritten you probably want <code>--exclude-globbing-filelist</code> instead. See the <code>FILE SELECTION</code> section for more information. </p>
 </dd>
<dt><code>--exclude-filelist-stdin</code></dt>
<dd> <p> Like <code>--exclude-filelist,</code> but the list of files will be read from standard input. See the <code>FILE SELECTION</code> section for more information. </p>
 </dd>
<dt><code>--exclude-globbing-filelist </code>filename </dt>
<dd> <p> Like <code>--exclude-filelist</code> but each line of the filelist will be interpreted according to the same rules as <code>--include</code> and <code>--exclude.</code> </p>
 </dd>
<dt><code>--exclude-globbing-filelist-stdin</code></dt>
<dd> <p> Like <code>--exclude-globbing-filelist</code>, but the list of files will be read from standard input. </p>
 </dd>
<dt><code>--exclude-other-filesystems</code></dt>
<dd> <p> Exclude files on file systems (identified by device number) other than the file system the root of the source directory is on. </p>
 </dd>
<dt><code>--exclude-regexp </code><i>regexp</i></dt>
<dd> <p> Exclude files matching the given regexp. Unlike the <code>--exclude</code> option, this option does not match files in a directory it matches. See the <code>FILE SELECTION</code> section for more information. </p>
 </dd>
<dt><code>--exclude-special-files</code></dt>
<dd> <p> Exclude all device files, fifo files, socket files, and symbolic links. </p>
 </dd>
<dt><code>--exclude-sockets</code></dt>
<dd> <p> Exclude all socket files. </p>
 </dd>
<dt><code>--exclude-symbolic-links</code></dt>
<dd> <p> Exclude all symbolic links. This option is automatically enabled if the backup source is running on native Windows to avoid backing-up NTFS reparse points. </p>
 </dd>
<dt><code>--exclude-if-present </code><i>filename</i></dt>
<dd> <p> Exclude directories if <i>filename</i> is present. This option needs to come before any other include or exclude options. </p>
 </dd>
<dt><code>--force</code></dt>
<dd> <p> Authorize a more drastic modification of a directory than usual (for instance, when overwriting of a destination path, or when removing multiple sessions with <code>--remove-older-than</code>). rdiff-backup will generally tell you if it needs this. <code>WARNING:</code> You can cause data loss if you mis-use this option. Furthermore, do NOT use this option when doing a restore, as it will DELETE FILES, unless you absolutely know what you are doing. </p>
 </dd>
<dt><code>--group-mapping-file </code><i>filename</i></dt>
<dd> <p> Map group names and ids according the the group mapping file <i>filename</i>. See the <code>USERS AND GROUPS</code> section for more information. </p>
 </dd>
<dt><code>--include </code><i>shell_pattern</i></dt>
<dd> <p> Similar to <code>--exclude</code> but include matched files instead. Unlike <code>--exclude</code>, this option will also match parent directories of matched files (although not necessarily their contents). See the <code>FILE SELECTION</code> section for more information. </p>
 </dd>
<dt><code>--include-filelist </code><i>filename</i></dt>
<dd> <p> Like <code>--exclude-filelist</code>, but include the listed files instead. If <i>filename</i> is handwritten you probably want <code>--include-globbing-filelist</code> instead. See the <code>FILE SELECTION</code> section for more information. </p>
 </dd>
<dt><code>--include-filelist-stdin</code></dt>
<dd> <p> Like <code>--include-filelist</code>, but read the list of included files from standard input. </p>
 </dd>
<dt><code>--include-globbing-filelist </code><i>filename</i></dt>
<dd> <p> Like <code>--include-filelist</code> but each line of the filelist will be interpreted according to the same rules as <code>--include</code> and <code>--exclude.</code> </p>
 </dd>
<dt><code>--include-globbing-filelist-stdin</code></dt>
<dd> <p> Like <code>--include-globbing-filelist</code>, but the list of files will be read from standard input. </p>
 </dd>
<dt><code>--include-regexp </code><i>regexp</i></dt>
<dd> <p> Include files matching the regular expression <i>regexp</i>. Only files explicitly matched by <i>regexp</i> will be included by this option. See the <code>FILE SELECTION</code> section for more information. </p>
 </dd>
<dt><code>--include-special-files</code></dt>
<dd> <p> Include all device files, fifo files, socket files, and symbolic links. </p>
 </dd>
<dt><code>--include-symbolic-links</code></dt>
<dd> <p> Include all symbolic links. </p>
 </dd>
<dt><code>--list-at-time </code><i>time</i></dt>
<dd> <p> List the files in the archive that were present at the given time. If a directory in the archive is specified, list only the files under that directory. </p>
 </dd>
<dt><code>--list-changed-since </code><i>time</i></dt>
<dd> <p> List the files that have changed in the destination directory since the given time. See <code>TIME FORMATS</code> for the format of <i>time</i>. If a directory in the archive is specified, list only the files under that directory. This option does not read the source directory; it is used to compare the contents of two different rdiff-backup sessions. </p>
 </dd>
<dt><code>-l, --list-increments</code></dt>
<dd> <p> List the number and date of partial incremental backups contained in the specified destination directory. No backup or restore will take place if this option is given. </p>
 </dd>
<dt><code>--list-increment-sizes</code></dt>
<dd> <p> List the total size of all the increment and mirror files by time. This may be helpful in deciding how many increments to keep, and when to --remove-older-than. Specifying a subdirectory is allowable; then only the sizes of the mirror and increments pertaining to that subdirectory will be listed. </p>
 </dd>
<dt><code>--max-file-size </code><i>size</i></dt>
<dd> <p> Exclude files that are larger than the given size in bytes </p>
 </dd>
<dt><code>--min-file-size </code><i>size</i></dt>
<dd> <p> Exclude files that are smaller than the given size in bytes </p>
 </dd>
<dt><code>--never-drop-acls</code></dt>
<dd> <p> Exit with error instead of dropping acls or acl entries. Normally this may happen (with a warning) because the destination does not support them or because the relevant user/group names do not exist on the destination side. </p>
 </dd>
<dt><code>--no-acls</code></dt>
<dd> <p> No Access Control Lists - disable backup of ACLs </p>
 </dd>
<dt><code>--no-carbonfile</code></dt>
<dd> <p> Disable backup of MacOS X carbonfile information </p>
 </dd>
<dt><code>--no-compare-inode</code></dt>
<dd> <p> This option prevents rdiff-backup from flagging a hardlinked file as changed when its device number and/or inode changes. This option is useful in situations where the source filesystem lacks persistent device and/or inode numbering. For example, network filesystems may have mount-to-mount differences in their device number (but possibly stable inode numbers); USB/1394 devices may come up at different device numbers each remount (but would generally have same inode number); and there are filesystems which don&#8217;t even have the same inode numbers from use to use. Without the option rdiff-backup may generate unnecessary numbers of tiny diff files. </p>
 </dd>
<dt><code>--no-compression</code></dt>
<dd> <p> Disable the default gzip compression of most of the .snapshot and .diff increment files stored in the rdiff-backup-data directory. A backup volume can contain compressed and uncompressed increments, so using this option inconsistently is fine. </p>
 </dd>
<dt><code>--no-compression-regexp regexp</code></dt>
<dd> <p> Do not compress increments based on files whose filenames match regexp. The default includes many common audiovisual and archive files, and may be found in Globals.py. </p>
 </dd>
<dt><code>--no-eas</code></dt>
<dd> <p> No Extended Attributes support - disable backup of EAs. </p>
 </dd>
<dt><code>--no-file-statistics</code></dt>
<dd> <p> This will disable writing to the file_statistics file in the rdiff-backup-data directory. rdiff-backup will run slightly quicker and take up a bit less space. </p>
 </dd>
<dt><code>--no-hard-links</code></dt>
<dd> <p> Don&#8217;t replicate hard links on destination side. If many hard-linked files are present, this option can drastically decrease memory usage. This option is enabled by default if the backup source or restore destination is running on native Windows. </p>
 </dd>
<dt><code>--null-separator</code></dt>
<dd> <p> Use nulls (\0) instead of newlines (\n) as line separators, which may help when dealing with filenames containing newlines. This affects the expected format of the files specified by the --{include|exclude}-filelist[-stdin] switches as well as the format of the directory statistics file. </p>
 </dd>
<dt><code>--parsable-output</code></dt>
<dd> <p> If set, rdiff-backup&#8217;s output will be tailored for easy parsing by computers, instead of convenience for humans. Currently this only applies when listing increments using the <code>-l</code> or <code>--list-increments</code> switches, where the time will be given in seconds since the epoch. </p>
 </dd>
<dt><code>--override-chars-to-quote </code></dt>
<dd> <p> If the filesystem to which we are backing up is not case-sensitive, automatic &#8216;quoting&#8217; of characters occurs. For example, a file &#8216;Developer.doc&#8217; will be converted into &#8216;;068eveloper.doc&#8217;. To override this behavior, you need to specify this option. </p>
 </dd>
<dt><code>--preserve-numerical-ids</code></dt>
<dd> <p> If set, rdiff-backup will preserve uids/gids instead of trying to preserve unames and gnames. See the <code>USERS AND GROUPS</code> section for more information. </p>
 </dd>
<dt><code>--print-statistics</code></dt>
<dd> <p> If set, summary statistics will be printed after a successful backup. If not set, this information will still be available from the session statistics file. See the <code>STATISTICS</code> section for more information. </p>
 </dd>
<dt><code>-r, --restore-as-of </code><i>restore_time</i></dt>
<dd> <p> Restore the specified directory as it was as of <i>restore_time</i>. See the <code>TIME FORMATS</code> section for more information on the format of <i>restore_time</i>, and see the <code>RESTORING</code> section for more information on restoring. </p>
 </dd>
<dt><code>--remote-cmd </code><i>cmd</i></dt>
<dd> <p> Deprecated. Please use --remote-schema instead </p>
 </dd>
<dt><code>--remote-schema </code><i>schema</i></dt>
<dd> <p> Specify an alternate method of connecting to a remote computer. This is necessary to get rdiff-backup not to use ssh for remote backups, or if, for instance, rdiff-backup is not in the PATH on the remote side. See the <code>REMOTE OPERATION</code> section for more information. </p>
 </dd>
<dt><code>--remote-tempdir </code><i>path</i></dt>
<dd> <p> Adds the --tempdir option with argument <i>path</i> when invoking remote instances of rdiff-backup. </p>
 </dd>
<dt><code>--remove-older-than </code><i>time_spec</i></dt>
<dd> <p> Remove the incremental backup information in the destination directory that has been around longer than the given time. <i>time_spec</i> can be either an absolute time, like &quot;2002-01-04&quot;, or a time interval. The time interval is an integer followed by the character s, m, h, D, W, M, or Y, indicating seconds, minutes, hours, days, weeks, months, or years respectively, or a number of these concatenated. For example, 32m means 32 minutes, and 3W2D10h7s means 3 weeks, 2 days, 10 hours, and 7 seconds. In this context, a month means 30 days, a year is 365 days, and a day is always 86400 seconds. </p>
<p> rdiff-backup cannot remove-older-than and back up or restore in a single session. In order to both backup a directory and remove old files in it, you must run rdiff-backup twice. </p>
<p> By default, rdiff-backup will only delete information from one session at a time. To remove two or more sessions at the same time, supply the <code>--force </code> option (rdiff-backup will tell you if <code>--force</code> is required). </p>
<p> Note that snapshots of deleted files are covered by this operation. Thus if you deleted a file two weeks ago, backed up immediately afterwards, and then ran rdiff-backup with --remove-older-than 10D today, no trace of that file would remain. Finally, file selection options such as --include and --exclude don&#8217;t affect --remove-older-than. </p>
 </dd>
<dt><code>--restrict </code><i>path</i></dt>
<dd> <p> Require that all file access be inside the given path. This switch, and the following two, are intended to be used with the --server switch to provide a bit more protection when doing automated remote backups. They are <code>not intended as your only line of defense</code> so please don&#8217;t do something silly like allow public access to an rdiff-backup server run with --restrict-read-only. </p>
 </dd>
<dt><code>--restrict-read-only </code><i>path</i></dt>
<dd> <p> Like <code>--restrict</code>, but also reject all write requests. </p>
 </dd>
<dt><code>--restrict-update-only </code><i>path</i></dt>
<dd> <p> Like <code>--restrict</code>, but only allow writes as part of an incremental backup. Requests for other types of writes (for instance, deleting <i>path</i>) will be rejected. </p>
 </dd>
<dt><code>--server</code></dt>
<dd> <p> Enter server mode (not to be invoked directly, but instead used by another rdiff-backup process on a remote computer). </p>
 </dd>
<dt><code>--ssh-no-compression</code></dt>
<dd> <p> When running ssh, do not use the -C option to enable compression. <code>--ssh-no-compression</code> is ignored if you specify a new schema using <code>--remote-schema.</code> </p>
 </dd>
<dt><code>--tempdir </code><i>path</i></dt>
<dd> <p> Sets the directory that rdiff-backup uses for temporary files to the given path. The environment variables TMPDIR, TEMP, and TMP can also be used to set the temporary files directory. See the documentation of the Python tempfile module for more information. </p>
 </dd>
<dt><code>--terminal-verbosity </code><i>[0-9]</i></dt>
<dd> <p> Select which messages will be displayed to the terminal. If missing the level defaults to the verbosity level. </p>
 </dd>
<dt><code>--test-server</code></dt>
<dd> <p> Test for the presence of a compatible rdiff-backup server as specified in the following host::filename argument(s). The filename section will be ignored. </p>
 </dd>
<dt><code>--user-mapping-file </code><i>filename</i></dt>
<dd> <p> Map user names and ids according to the user mapping file <i>filename</i>. See the <code>USERS AND GROUPS</code> section for more information. </p>
 </dd>
<dt><code>-v</code><i>[0-9]</i><code>, --verbosity </code><i>[0-9]</i></dt>
<dd> <p> Specify verbosity level (0 is totally silent, 3 is the default, and 9 is noisiest). This determines how much is written to the log file. </p>
 </dd>
<dt><code>--verify</code></dt>
<dd> <p> This is short for <code>--verify-at-time</code><i> now</i> </p>
 </dd>
<dt><code>--verify-at-time</code><i> now</i></dt>
<dd> <p> Check all the data in the repository at the given time by computing the SHA1 hash of all the regular files and comparing them with the hashes stored in the metadata file. </p>
 </dd>
<dt><code>-V, --version</code></dt>
<dd> <p> Print the current version and exit </p>
 </dd></dl>
<h2>RESTORING</h2>
<p> There are two ways to tell rdiff-backup to restore a file or directory. Firstly, you can run rdiff-backup on a mirror file and use the <code>-r</code> or <code>--restore-as-of</code> options. Secondly, you can run it on an increment file. </p>
<p> For example, suppose in the past you have run: </p>
<dl>
<dd> <p> rdiff-backup /usr /usr.backup </p>
 </dd></dl>
<p> to back up the /usr directory into the /usr.backup directory, and now want a copy of the /usr/local directory the way it was 3 days ago placed at /usr/local.old. </p>
<p> One way to do this is to run: </p>
<dl>
<dd> <p> rdiff-backup -r 3D /usr.backup/local /usr/local.old </p>
 </dd></dl>
<p> where above the &quot;3D&quot; means 3 days (for other ways to specify the time, see the <code>TIME FORMATS</code> section). The /usr.backup/local directory was selected, because that is the directory containing the current version of /usr/local. </p>
<p> Note that the option to <code>--restore-as-of</code> always specifies an exact time. (So &quot;3D&quot; refers to the instant 72 hours before the present.) If there was no backup made at that time, rdiff-backup restores the state recorded for the previous backup. For instance, in the above case, if &quot;3D&quot; is used, and there are only backups from 2 days and 4 days ago, /usr/local as it was 4 days ago will be restored. </p>
<p> The second way to restore files involves finding the corresponding increment file. It would be in the /backup/rdiff-backup-data/increments/usr directory, and its name would be something like &quot;local.2002-11-09T12:43:53-04:00.dir&quot; where the time indicates it is from 3 days ago. Note that the increment files all end in &quot;.diff&quot;, &quot;.snapshot&quot;, &quot;.dir&quot;, or &quot;.missing&quot;, where &quot;.missing&quot; just means that the file didn&#8217;t exist at that time (finally, some of these may be gzip-compressed, and have an extra &quot;.gz&quot; to indicate this). Then running: </p>
<dl>
<dd> <p> rdiff-backup /backup/rdiff-backup-data/increments/usr/local.&lt;time&gt;.dir /usr/local.old </p>
 </dd></dl>
<p> would also restore the file as desired. </p>
<p> If you are not sure exactly which version of a file you need, it is probably easiest to either restore from the increments files as described immediately above, or to see which increments are available with -l/--list-increments, and then specify exact times into -r/--restore-as-of. </p>
<h2>TIME FORMATS</h2>
<p> rdiff-backup uses time strings in two places. Firstly, all of the increment files rdiff-backup creates will have the time in their filenames in the w3 datetime format as described in a w3 note at <a rel="nofollow" href="http://www.w3.org/TR/NOTE-datetime.">http://www.w3.org/TR/NOTE-datetime.</a> Basically they look like &quot;2001-07-15T04:09:38-07:00&quot;, which means what it looks like. The &quot;-07:00&quot; section means the time zone is 7 hours behind UTC. </p>
<p> Secondly, the <code>-r</code><i>,</i><code> --restore-as-of</code><i>, and </i><code>--remove-older-than</code> options take a time string, which can be given in any of several formats: </p>
<dl>
<dt>1.</dt>
<dd> <p> the string &quot;now&quot; (refers to the current time) </p>
 </dd>
<dt>2.</dt>
<dd> <p> a sequences of digits, like &quot;123456890&quot; (indicating the time in seconds after the epoch) </p>
 </dd>
<dt>3.</dt>
<dd> <p> A string like &quot;2002-01-25T07:00:00+02:00&quot; in datetime format </p>
 </dd>
<dt>4.</dt>
<dd> <p> An interval, which is a number followed by one of the characters s, m, h, D, W, M, or Y (indicating seconds, minutes, hours, days, weeks, months, or years respectively), or a series of such pairs. In this case the string refers to the time that preceded the current time by the length of the interval. For instance, &quot;1h78m&quot; indicates the time that was one hour and 78 minutes ago. The calendar here is unsophisticated: a month is always 30 days, a year is always 365 days, and a day is always 86400 seconds. </p>
 </dd>
<dt>5.</dt>
<dd> <p> A date format of the form YYYY/MM/DD, YYYY-MM-DD, MM/DD/YYYY, or MM-DD-YYYY, which indicates midnight on the day in question, relative to the current timezone settings. For instance, &quot;2002/3/5&quot;, &quot;03-05-2002&quot;, and &quot;2002-3-05&quot; all mean March 5th, 2002. </p>
 </dd>
<dt>6.</dt>
<dd> <p> A backup session specification which is a non-negative integer followed by &#8216;B&#8217;. For instance, &#8216;0B&#8217; specifies the time of the current mirror, and &#8216;3B&#8217; specifies the time of the 3rd newest increment. </p>
 </dd></dl>
<h2>REMOTE OPERATION</h2>
<p> In order to access remote files, rdiff-backup opens up a pipe to a copy of rdiff-backup running on the remote machine. Thus rdiff-backup must be installed on both ends. To open this pipe, rdiff-backup first splits the filename into host_info::pathname. It then substitutes host_info into the remote schema, and runs the resulting command, reading its input and output. </p>
<p> The default remote schema is &#8216;ssh -C %s rdiff-backup --server&#8217; where host_info is substituted for &#8216;%s&#8217;. So if the host_info is user [at] host.net, then rdiff-backup runs &#8216;ssh user [at] host.net rdiff-backup --server&#8217;. Using --remote-schema, rdiff-backup can invoke an arbitrary command in order to open up a remote pipe. For instance, </p>
<dl>
<dd> <p> rdiff-backup --remote-schema &#8216;cd /usr; %s&#8217; foo &#8216;rdiff-backup --server&#8217;::bar </p>
 </dd></dl>
<p> is basically equivalent to (but slower than) </p>
<dl>
<dd> <p> rdiff-backup foo /usr/bar </p>
 </dd></dl>
<p> Concerning quoting, if for some reason you need to put two consecutive colons in the host_info section of a host_info::pathname argument, or in the pathname of a local file, you can quote one of them by prepending a backslash. So in &#8216;a\::b::c&#8217;, host_info is &#8216;a::b&#8217; and the pathname is &#8216;c&#8217;. Similarly, if you want to refer to a local file whose filename contains two consecutive colons, like &#8216;strange::file&#8217;, you&#8217;ll have to quote one of the colons as in &#8216;strange\::file&#8217;. Because the backslash is a quote character in these circumstances, it too must be quoted to get a literal backslash, so &#8216;foo\::\\bar&#8217; evaluates to &#8216;foo::\bar&#8217;. To make things more complicated, because the backslash is also a common shell quoting character, you may need to type in &#8216;\\\\&#8216; at the shell prompt to get a literal backslash (if it makes you feel better, I had to type in 8 backslashes to get that in this man page...). And finally, to include a literal % in the string specified by --remote-schema, quote it with another %, as in %%. </p>
<p> Although ssh itself may be secure, using rdiff-backup in the default way presents some security risks. For instance if the server is run as root, then an attacker who compromised the client could then use rdiff-backup to overwrite arbitrary server files by &quot;backing up&quot; over them. Such a setup can be made more secure by using the sshd configuration option <code>command=rdiff-backup --server</code> possibly along with the <code>--restrict*</code> options to rdiff-backup. For more information, see the web page, the wiki, and the entries for the <code>--restrict*</code> options on this man page. </p>
<h2>FILE SELECTION</h2>
<p> <code>rdiff-backup</code> has a number of file selection options. When rdiff-backup is run, it searches through the given source directory and backs up all the files matching the specified options. This selection system may appear complicated, but it is supposed to be flexible and easy-to-use. If you just want to learn the basics, first look at the selection examples in the examples.html file included in the package, or on the web at <i><a rel="nofollow" href="http://rdiff-backup.nongnu.org/examples.html">http://rdiff-backup.nongnu.org/examples.html</a></i> </p>
<p> <code>rdiff-backup</code>&#8216;s selection system was originally inspired by <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1), but there are many differences. (For instance, trailing backslashes have no special significance.) </p>
<p> The file selection system comprises a number of file selection conditions, which are set using one of the following command line options: <code>--exclude</code>, <code>--exclude-filelist</code>, <code>--exclude-device-files</code>, <code>--exclude-fifos</code>, <code>--exclude-sockets</code>, <code>--exclude-symbolic-links</code>, <code>--exclude-globbing-filelist</code>, <code>--exclude-globbing-filelist-stdin</code>, <code>--exclude-filelist-stdin</code>, <code>--exclude-regexp</code>, <code>--exclude-special-files</code>, <code>--include</code>, <code>--include-filelist</code>, <code>--include-globbing-filelist</code>, <code>--include-globbing-filelist-stdin</code>, <code>--include-filelist-stdin</code>, and <code>--include-regexp</code>. Each file selection condition either matches or doesn&#8217;t match a given file. A given file is excluded by the file selection system exactly when the first matching file selection condition specifies that the file be excluded; otherwise the file is included. When backing up, if a file is excluded, rdiff-backup acts as if that file does not exist in the source directory. When restoring, an excluded file is considered not to exist in either the source or target directories. </p>
<p> For instance, </p>
<dl>
<dd> <p> rdiff-backup --include /usr --exclude /usr /usr /backup </p>
 </dd></dl>
<p> is exactly the same as </p>
<dl>
<dd> <p> rdiff-backup /usr /backup </p>
 </dd></dl>
<p> because the include and exclude directives match exactly the same files, and the <code>--include</code> comes first, giving it precedence. Similarly, </p>
<dl>
<dd> <p> rdiff-backup --include /usr/local/bin --exclude /usr/local /usr /backup </p>
 </dd></dl>
<p> would backup the /usr/local/bin directory (and its contents), but not /usr/local/doc. </p>
<p> The <code>include</code>, <code>exclude</code>, <code>include-globbing-filelist</code>, and <code>exclude-globbing-filelist</code> options accept <i>extended shell globbing patterns</i>. These patterns can contain the special patterns <code>*</code>, <code>**</code>, <code>?</code>, and <code>[...]</code>. As in a normal shell, <code>*</code> can be expanded to any string of characters not containing &quot;/&quot;, <code>?</code> expands to any character except &quot;/&quot;, and <code>[...]</code> expands to a single character of those characters specified (ranges are acceptable). The new special pattern, <code>**</code>, expands to any string of characters whether or not it contains &quot;/&quot;. Furthermore, if the pattern starts with &quot;ignorecase:&quot; (case insensitive), then this prefix will be removed and any character in the string can be replaced with an upper- or lowercase version of itself. </p>
<p> If you need to match filenames which contain the above globbing characters, they may be escaped using a backslash &quot;\&quot;. The backslash will only escape the character following it so for <code>**</code> you will need to use &quot;\*\*&quot; to avoid escaping it to the <code>* </code> globbing character. </p>
<p> Remember that you may need to quote these characters when typing them into a shell, so the shell does not interpret the globbing patterns before rdiff-backup sees them. </p>
<p> The <code>--exclude </code><i>pattern</i> option matches a file iff: </p>
<dl>
<dt><code>1.</code></dt>
<dd> <p> <i>pattern</i> can be expanded into the file&#8217;s filename, or </p>
 </dd>
<dt><code>2.</code></dt>
<dd> <p> the file is inside a directory matched by the option. </p>
 </dd></dl>
<p> Conversely, <code>--include </code><i>pattern</i> matches a file iff: </p>
<dl>
<dt><code>1.</code></dt>
<dd> <p> <i>pattern</i> can be expanded into the file&#8217;s filename, </p>
 </dd>
<dt><code>2.</code></dt>
<dd> <p> the file is inside a directory matched by the option, or </p>
 </dd>
<dt><code>3.</code></dt>
<dd> <p> the file is a directory which contains a file matched by the option. </p>
 </dd></dl>
<p> For example, </p>
<dl>
<dd> <p> <code>--exclude</code> /usr/local </p>
 </dd></dl>
<p> matches /usr/local, /usr/local/lib, and /usr/local/lib/netscape. It is the same as --exclude /usr/local --exclude &#8216;/usr/local/**&#8216;. </p>
<dl>
<dd> <p> <code>--include</code> /usr/local </p>
 </dd></dl>
<p> specifies that /usr, /usr/local, /usr/local/lib, and /usr/local/lib/netscape (but not /usr/doc) all be backed up. Thus you don&#8217;t have to worry about including parent directories to make sure that included subdirectories have somewhere to go. Finally, </p>
<dl>
<dd> <p> <code>--include</code> ignorecase:&#8216;/usr/[a-z0-9]foo/*/**.py&#8217; </p>
 </dd></dl>
<p> would match a file like /usR/5fOO/hello/there/world.py. If it did match anything, it would also match /usr. If there is no existing file that the given pattern can be expanded into, the option will not match /usr. </p>
<p> The <code>--include-filelist</code>, <code>--exclude-filelist</code>, <code>--include-filelist-stdin</code>, and <code>--exclude-filelist-stdin</code> options also introduce file selection conditions. They direct rdiff-backup to read in a file, each line of which is a file specification, and to include or exclude the matching files. Lines are separated by newlines or nulls, depending on whether the --null-separator switch was given. Each line in a filelist is interpreted similarly to the way <i>extended shell patterns</i> are, with a few exceptions: </p>
<dl>
<dt><code>1.</code></dt>
<dd> <p> Globbing patterns like <code>*</code>, <code>**</code>, <code>?</code>, and <code>[...]</code> are not expanded. </p>
 </dd>
<dt><code>2.</code></dt>
<dd> <p> Include patterns do not match files in a directory that is included. So /usr/local in an include file will not match /usr/local/doc. </p>
 </dd>
<dt><code>3.</code></dt>
<dd> <p> Lines starting with &quot;+ &quot; are interpreted as include directives, even if found in a filelist referenced by <code>--exclude-filelist</code>. Similarly, lines starting with &quot;- &quot; exclude files even if they are found within an include filelist. </p>
<p> For example, if the file &quot;list.txt&quot; contains the lines: </p>
 </dd>
<dl>
<dd> <p> /usr/local </p>
 </dd></dl>
<dl>
<dd> <p> - /usr/local/doc </p>
 </dd></dl>
<dl>
<dd> <p> /usr/local/bin </p>
 </dd></dl>
<dl>
<dd> <p> + /var </p>
 </dd></dl>
<dl>
<dd> <p> - /var </p>
 </dd></dl>
<p> then &quot;--include-filelist list.txt&quot; would include /usr, /usr/local, and /usr/local/bin. It would exclude /usr/local/doc, /usr/local/doc/python, etc. It neither excludes nor includes /usr/local/man, leaving the fate of this directory to the next specification condition. Finally, it is undefined what happens with /var. A single file list should not contain conflicting file specifications. </p>
<p> The <code>--include-globbing-filelist</code> and <code>--exclude-globbing-filelist</code> options also specify filelists, but each line in the filelist will be interpreted as a globbing pattern the way <code>--include</code> and <code>--exclude</code> options are interpreted (although &quot;+ &quot; and &quot;- &quot; prefixing is still allowed). For instance, if the file &quot;globbing-list.txt&quot; contains the lines: </p>
<dl>
<dd> <p> dir/foo </p>
 </dd></dl>
<dl>
<dd> <p> + dir/bar </p>
 </dd></dl>
<dl>
<dd> <p> - ** </p>
 </dd></dl>
<p> Then &quot;--include-globbing-filelist globbing-list.txt&quot; would be exactly the same as specifying &quot;--include dir/foo --include dir/bar --exclude **&quot; on the command line. </p>
<p> Finally, the <code>--include-regexp</code> and <code>--exclude-regexp</code> allow files to be included and excluded if their filenames match a python regular expression. Regular expression syntax is too complicated to explain here, but is covered in Python&#8217;s library reference. Unlike the <code>--include</code> and <code>--exclude</code> options, the regular expression options don&#8217;t match files containing or contained in matched files. So for instance </dl>
 </p>
<dl>
<dd> <p> --include &#8216;[0-9]{7}(?!foo)&#8216; </p>
 </dd></dl>
<p> matches any files whose full pathnames contain 7 consecutive digits which aren&#8217;t followed by &#8216;foo&#8217;. However, it wouldn&#8217;t match /home even if /home/ben/1234567 existed. </p>
<h2>USERS AND GROUPS</h2>
<p> There can be complications preserving ownership across systems. For instance the username that owns a file on the source system may not exist on the destination. Here is how rdiff-backup maps ownership on the source to the destination (or vice-versa, in the case of restoring): </p>
<dl>
<dt><code>1.</code></dt>
<dd> <p> If the --preserve-numerical-ids option is given, the remote files will always have the same uid and gid, both for ownership and ACL entries. This may cause unames and gnames to change. </p>
 </dd>
<dt><code>2.</code></dt>
<dd> <p> Otherwise, attempt to preserve the user and group names for ownership and in ACLs. This may result in files having different uids and gids across systems. </p>
 </dd>
<dt><code>3.</code></dt>
<dd> <p> If a name cannot be preserved (e.g. because the username does not exist), preserve the original id, but only in cases of user and group ownership. For ACLs, omit any entry that has a bad user or group name. </p>
 </dd>
<dt><code>4.</code></dt>
<dd> <p> The <code>--user-mapping-file</code> and <code>--group-mapping-file</code> options override this behavior. If either of these options is given, the policy described in 2 and 3 above will be followed, but with the mapped user and group instead of the original. If you specify both <code>--preserve-numerical-ids</code> and one of the mapping options, the behavior is undefined. </p>
<p> The user and group mapping files both have the same form: </p>
 </dd>
<dl>
<dd> <p> old_name_or_id1:new_name_or_id1 </p>
 </dd></dl>
<dl>
<dd> <p> old_name_or_id2:new_name_or_id2 </p>
 </dd></dl>
<dl>
<dd> <p> &lt;etc&gt; </p>
 </dd></dl>
<p> Each line should contain a name or id, followed by a colon &quot;:&quot;, followed by another name or id. If a name or id is not listed, they are treated in the default way described above. </p>
<p> When restoring, the above behavior is also followed, but note that the original source user/group information will be the input, not the already mapped user/group information present in the backup repository. For instance, suppose you have mapped all the files owned by <i>alice</i> in the source so that they are owned by <i>ben</i> in the repository, and now you want to restore, making sure the files owned originally by <i>alice</i> are still owned by <i>alice</i>. In this case there is no need to use any of the mapping options. However, if you wanted to restore the files so that the files originally owned by <i>alice</i> on the source are now owned by <i>ben</i>, you would have to use the mapping options, even though you just want the unames of the repository&#8217;s files preserved in the restored files. </p>
<h2>STATISTICS</h2>
<p> Every session rdiff-backup saves various statistics into two files, the session statistics file at rdiff-backup-data/session_statistics.&lt;time&gt;.data and the directory statistics file at rdiff-backup-data/directory_statistics.&lt;time&gt;.data. They are both text files and contain similar information: how many files changed, how many were deleted, the total size of increment files created, etc. However, the session statistics file is intended to be very readable and only describes the session as a whole. The directory statistics file is more compact (and slightly less readable) but describes every directory backed up. It also may be compressed to save space. </p>
<p> Statistics-related options include <code>--print-statistics</code> and <code>--null-separator</code>. </p>
<p> Also, rdiff-backup will save various messages to the log file, which is rdiff-backup-data/backup.log for backup sessions and rdiff-backup-data/restore.log for restore sessions. Generally what is written to this file will coincide with the messages displayed to stdout or stderr, although this can be changed with the <code>--terminal-verbosity</code> option. </p>
<p> The log file is not compressed and can become quite large if rdiff-backup is run with high verbosity. </p>
<h2>EXIT STATUS</h2>
<p> If rdiff-backup finishes successfully, the exit status will be 0. If there is an unrecoverable (critical) error, it will be non-zero (usually 1, but don&#8217;t depend on this specific value). When setting up rdiff-backup to run automatically (as from <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8) or similar) it is probably a good idea to check the exit code. </p>
<h2>BUGS</h2>
<p> The gzip library in versions 2.2 and earlier of python (but fixed in 2.3a1) has trouble producing files over 2GB in length. This bug will prevent rdiff-backup from producing large compressed increments (snapshots or diffs). A workaround is to disable compression for large uncompressable files. </p>
<h2>AUTHOR</h2>
<p> Ben Escoto &lt;ben [at] emerose.org&gt; </p>
<p> Feel free to ask me questions or send me bug reports, but you may want to see the web page, mentioned below, first. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-python/">python</a></code>(1), <code><a href="/docs/linux/man/1-rdiff/">rdiff</a></code>(1), <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1). The main rdiff-backup web page is at <i><a rel="nofollow" href="http://rdiff-backup.nongnu.org/">http://rdiff-backup.nongnu.org/</a></i>. It has more information, links to the mailing list and CVS, etc. </p>
