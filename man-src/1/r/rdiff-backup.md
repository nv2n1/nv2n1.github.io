---
title: "rdiff-backup(1)"
name: "rdiff-backup"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdiff-backup/"
description: "rdiff-backup – local/remote mirror and incremental backup"
---

<h2>NAME</h2>
<p> rdiff-backup &#8211; local/remote mirror and incremental backup</p>
<h2>SYNOPSIS</h2>
<p> <code>rdiff-backup</code> <code>[</code><i>options</i><code>]</code> <code>[[[</code><i>user@</i><code>]</code><i>host1.foo</i><code>]::</code><i>source_directory</i><code>]</code> <code>[[[</code><i>user@</i><code>]</code><i>host2.foo</i><code>]::</code><i>destination_directory</i><code>]</code> </p>
<p> <code>rdiff-backup</code> <code>&#123;&#123; -l | &#8211;list-increments }</code> <code>| &#8211;remove-older-than </code><i>time_interval</i> <code>| &#8211;list-at-time </code><i>time</i> <code>| &#8211;list-changed-since </code><i>time</i> <code>| &#8211;list-increment-sizes </code> <code>| &#8211;verify</code> <code>| &#8211;verify-at-time </code><i>time</i><code>}</code> <code>[[[</code><i>user@</i><code>]</code><i>host2.foo</i><code>]::</code><i>destination_directory</i><code>]</code> </p>
<p> <code>rdiff-backup &#8211;calculate-average</code> <i>statfile1 statfile2 &#8230;</i> </p>
<p> <code>rdiff-backup &#8211;test-server</code> <code>[</code><i>user1</i><code>]</code><i>@host1.net1</i><code>::</code><i>path</i> <code>[[</code><i>user2</i><code>]</code><i>@host2.net2</i><code>::</code><i>path</i><code>]</code> <i>&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>rdiff-backup</code> is a script, written in <code><a href="/docs/linux/man/1-python/">python</a></code>(1) that backs up one directory to another. The target directory ends up a copy (mirror) of the source directory, but extra reverse diffs are stored in a special subdirectory of that target directory, so you can still recover files lost some time ago. The idea is to combine the best features of a mirror and an incremental backup. rdiff-backup also preserves symlinks, special files, hardlinks, permissions, uid/gid ownership, and modification times. </p>
<p> <code>rdiff-backup</code> can also operate in a bandwidth efficient manner over a pipe, like <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1). Thus you can use ssh and rdiff-backup to securely back a hard drive up to a remote location, and only the differences will be transmitted. Using the default settings, rdiff-backup requires that the remote system accept ssh connections, and that <code>rdiff-backup</code> is installed in the user&#8217;s PATH on the remote system. For information on other options, see the section on <code>REMOTE OPERATION.</code> </p>
<p> Note that you <code>should not write to the mirror directory</code> except with rdiff-backup. Many of the increments are stored as reverse diffs, so if you delete or modify a file, you may lose the ability to restore previous versions of that file. </p>
<p> Finally, this man page is intended more as a precise description of the behavior and syntax of rdiff-backup. New users may want to check out the examples.html file included in the rdiff-backup distribution. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b, &#8211;backup-mode</code></p>
<dd> Force backup mode even if first argument appears to be an increment or mirror file.</p>
<dt><code>&#8211;calculate-average</code></p>
<dd> Enter calculate average mode. The arguments should be a number of statistics files. rdiff-backup will print the average of the listed statistics files and exit.</p>
<dt><code>&#8211;carbonfile </code></p>
<dd> Enable backup of MacOS X carbonfile information.</p>
<dt><code>&#8211;check-destination-dir</code></p>
<dd> If an rdiff-backup session fails, running rdiff-backup with this option on the destination dir will undo the failed directory. This happens automatically if you attempt to back up to a directory and the last backup failed.</p>
<dt><code>&#8211;compare</code></p>
<dd> This is equivalent to <code>&#8216;&#8211;compare-at-time</code><i> now</i><code>&#8216;</code></p>
<dt><code>&#8211;compare-at-time </code><i>time</i></p>
<dd> Compare a directory with the backup set at the given time. This can be useful to see how archived data differs from current data, or to check that a backup is current. This only compares metadata, in the same way rdiff-backup decides whether a file has changed.</p>
<dt><code>&#8211;compare-full</code></p>
<dd> This is equivalent to <code>&#8216;&#8211;compare-full-at-time</code><i> now</i><code>&#8216;</code></p>
<dt><code>&#8211;compare-full-at-time </code><i>time</i></p>
<dd> Compare a directory with the backup set at the given time. To compare regular files, the repository data will be copied in its entirety to the source side and compared byte by byte. This is the slowest but most complete compare option.</p>
<dt><code>&#8211;compare-hash</code></p>
<dd> This is equivalent to <code>&#8216;&#8211;compare-hash-at-time</code><i> now</i><code>&#8216;</code></p>
<dt><code>&#8211;compare-hash-at-time </code><i>time</i></p>
<dd> Compare a directory with the backup set at the given time. Regular files will be compared by computing their SHA1 digest on the source side and comparing it to the digest recorded in the metadata.</p>
<dt><code>&#8211;create-full-path</code></p>
<dd> Normally only the final directory of the destination path will be created if it does not exist. With this option, all missing directories on the destination path will be created. Use this option with care: if there is a typo in the remote path, the remote filesystem could fill up very quickly (by creating a duplicate backup tree). For this reason this option is primarily aimed at scripts which automate backups.</p>
<dt><code>&#8211;current-time </code><i>seconds</i></p>
<dd> This option is useful mainly for testing. If set, rdiff-backup will use it for the current time instead of consulting the clock. The argument is the number of seconds since the epoch.</p>
<dt><code>&#8211;exclude </code><i>shell_pattern</i></p>
<dd> Exclude the file or files matched by <i>shell_pattern</i>. If a directory is matched, then files under that directory will also be matched. See the <code>FILE SELECTION</code> section for more information.</p>
<dt><code>&#8211;exclude-device-files</code></p>
<dd> Exclude all device files. This can be useful for security/permissions reasons or if rdiff-backup is not handling device files correctly.</p>
<dt><code>&#8211;exclude-fifos</code></p>
<dd> Exclude all fifo files.</p>
<dt><code>&#8211;exclude-filelist </code><i>filename</i></p>
<dd> Excludes the files listed in <i>filename</i>. If <i>filename</i> is handwritten you probably want <code>&#8211;exclude-globbing-filelist</code> instead. See the <code>FILE SELECTION</code> section for more information.</p>
<dt><code>&#8211;exclude-filelist-stdin</code></p>
<dd> Like <code>&#8211;exclude-filelist,</code> but the list of files will be read from standard input. See the <code>FILE SELECTION</code> section for more information.</p>
<dt><code>&#8211;exclude-globbing-filelist </code>filename</p>
<dd> Like <code>&#8211;exclude-filelist</code> but each line of the filelist will be interpreted according to the same rules as <code>&#8211;include</code> and <code>&#8211;exclude.</code></p>
<dt><code>&#8211;exclude-globbing-filelist-stdin</code></p>
<dd> Like <code>&#8211;exclude-globbing-filelist</code>, but the list of files will be read from standard input.</p>
<dt><code>&#8211;exclude-other-filesystems</code></p>
<dd> Exclude files on file systems (identified by device number) other than the file system the root of the source directory is on.</p>
<dt><code>&#8211;exclude-regexp </code><i>regexp</i></p>
<dd> Exclude files matching the given regexp. Unlike the <code>&#8211;exclude</code> option, this option does not match files in a directory it matches. See the <code>FILE SELECTION</code> section for more information.</p>
<dt><code>&#8211;exclude-special-files</code></p>
<dd> Exclude all device files, fifo files, socket files, and symbolic links.</p>
<dt><code>&#8211;exclude-sockets</code></p>
<dd> Exclude all socket files.</p>
<dt><code>&#8211;exclude-symbolic-links</code></p>
<dd> Exclude all symbolic links. This option is automatically enabled if the backup source is running on native Windows to avoid backing-up NTFS reparse points.</p>
<dt><code>&#8211;exclude-if-present </code><i>filename</i></p>
<dd> Exclude directories if <i>filename</i> is present. This option needs to come before any other include or exclude options.</p>
<dt><code>&#8211;force</code></p>
<dd> Authorize a more drastic modification of a directory than usual (for instance, when overwriting of a destination path, or when removing multiple sessions with <code>&#8211;remove-older-than</code>). rdiff-backup will generally tell you if it needs this. <code>WARNING:</code> You can cause data loss if you mis-use this option. Furthermore, do NOT use this option when doing a restore, as it will DELETE FILES, unless you absolutely know what you are doing.</p>
<dt><code>&#8211;group-mapping-file </code><i>filename</i></p>
<dd> Map group names and ids according the the group mapping file <i>filename</i>. See the <code>USERS AND GROUPS</code> section for more information.</p>
<dt><code>&#8211;include </code><i>shell_pattern</i></p>
<dd> Similar to <code>&#8211;exclude</code> but include matched files instead. Unlike <code>&#8211;exclude</code>, this option will also match parent directories of matched files (although not necessarily their contents). See the <code>FILE SELECTION</code> section for more information.</p>
<dt><code>&#8211;include-filelist </code><i>filename</i></p>
<dd> Like <code>&#8211;exclude-filelist</code>, but include the listed files instead. If <i>filename</i> is handwritten you probably want <code>&#8211;include-globbing-filelist</code> instead. See the <code>FILE SELECTION</code> section for more information.</p>
<dt><code>&#8211;include-filelist-stdin</code></p>
<dd> Like <code>&#8211;include-filelist</code>, but read the list of included files from standard input.</p>
<dt><code>&#8211;include-globbing-filelist </code><i>filename</i></p>
<dd> Like <code>&#8211;include-filelist</code> but each line of the filelist will be interpreted according to the same rules as <code>&#8211;include</code> and <code>&#8211;exclude.</code></p>
<dt><code>&#8211;include-globbing-filelist-stdin</code></p>
<dd> Like <code>&#8211;include-globbing-filelist</code>, but the list of files will be read from standard input.</p>
<dt><code>&#8211;include-regexp </code><i>regexp</i></p>
<dd> Include files matching the regular expression <i>regexp</i>. Only files explicitly matched by <i>regexp</i> will be included by this option. See the <code>FILE SELECTION</code> section for more information.</p>
<dt><code>&#8211;include-special-files</code></p>
<dd> Include all device files, fifo files, socket files, and symbolic links.</p>
<dt><code>&#8211;include-symbolic-links</code></p>
<dd> Include all symbolic links.</p>
<dt><code>&#8211;list-at-time </code><i>time</i></p>
<dd> List the files in the archive that were present at the given time. If a directory in the archive is specified, list only the files under that directory.</p>
<dt><code>&#8211;list-changed-since </code><i>time</i></p>
<dd> List the files that have changed in the destination directory since the given time. See <code>TIME FORMATS</code> for the format of <i>time</i>. If a directory in the archive is specified, list only the files under that directory. This option does not read the source directory; it is used to compare the contents of two different rdiff-backup sessions.</p>
<dt><code>-l, &#8211;list-increments</code></p>
<dd> List the number and date of partial incremental backups contained in the specified destination directory. No backup or restore will take place if this option is given.</p>
<dt><code>&#8211;list-increment-sizes</code></p>
<dd> List the total size of all the increment and mirror files by time. This may be helpful in deciding how many increments to keep, and when to &#8211;remove-older-than. Specifying a subdirectory is allowable; then only the sizes of the mirror and increments pertaining to that subdirectory will be listed.</p>
<dt><code>&#8211;max-file-size </code><i>size</i></p>
<dd> Exclude files that are larger than the given size in bytes</p>
<dt><code>&#8211;min-file-size </code><i>size</i></p>
<dd> Exclude files that are smaller than the given size in bytes</p>
<dt><code>&#8211;never-drop-acls</code></p>
<dd> Exit with error instead of dropping acls or acl entries. Normally this may happen (with a warning) because the destination does not support them or because the relevant user/group names do not exist on the destination side.</p>
<dt><code>&#8211;no-acls</code></p>
<dd> No Access Control Lists &#8211; disable backup of ACLs</p>
<dt><code>&#8211;no-carbonfile</code></p>
<dd> Disable backup of MacOS X carbonfile information</p>
<dt><code>&#8211;no-compare-inode</code></p>
<dd> This option prevents rdiff-backup from flagging a hardlinked file as changed when its device number and/or inode changes. This option is useful in situations where the source filesystem lacks persistent device and/or inode numbering. For example, network filesystems may have mount-to-mount differences in their device number (but possibly stable inode numbers); USB/1394 devices may come up at different device numbers each remount (but would generally have same inode number); and there are filesystems which don&#8217;t even have the same inode numbers from use to use. Without the option rdiff-backup may generate unnecessary numbers of tiny diff files.</p>
<dt><code>&#8211;no-compression</code></p>
<dd> Disable the default gzip compression of most of the .snapshot and .diff increment files stored in the rdiff-backup-data directory. A backup volume can contain compressed and uncompressed increments, so using this option inconsistently is fine.</p>
<dt><code>&#8211;no-compression-regexp regexp</code></p>
<dd> Do not compress increments based on files whose filenames match regexp. The default includes many common audiovisual and archive files, and may be found in Globals.py.</p>
<dt><code>&#8211;no-eas</code></p>
<dd> No Extended Attributes support &#8211; disable backup of EAs.</p>
<dt><code>&#8211;no-file-statistics</code></p>
<dd> This will disable writing to the file_statistics file in the rdiff-backup-data directory. rdiff-backup will run slightly quicker and take up a bit less space.</p>
<dt><code>&#8211;no-hard-links</code></p>
<dd> Don&#8217;t replicate hard links on destination side. If many hard-linked files are present, this option can drastically decrease memory usage. This option is enabled by default if the backup source or restore destination is running on native Windows.</p>
<dt><code>&#8211;null-separator</code></p>
<dd> Use nulls (
