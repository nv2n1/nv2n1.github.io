---
title: "xfsrestore(8)"
name: "xfsrestore"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfsrestore/"
description: "xfsrestore – XFS filesystem incremental restore utility"
---

<p>xfsrestore &#8211; XFS filesystem incremental restore utility</p>
<h2>Synopsis</h2>
<pre><code>xfsrestore</code> -h
<code>xfsrestore</code> [ options ] -f <i>source</i> [ -f <i>source</i> ... ] <i>dest</i>
<code>xfsrestore</code> [ options ] - <i>dest</i>
<code>xfsrestore</code> -I [ subopt=value ... ]</pre>
<h2>Description</h2>
<p><i>xfsrestore</i> restores filesystems from dumps produced by <i><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></i>(8). Two modes of operation are available: simple and cumulative. </p>
<p> The default is simple mode. <i>xfsrestore</i> populates the specified destination directory, <i>dest</i>, with the files contained in the dump media. </p>
<p> The <code>-r</code> option specifies the cumulative mode. Successive invocations of <i>xfsrestore</i> are used to apply a chronologically ordered sequence of delta dumps to a base (level 0) dump. The contents of the filesystem at the time each dump was produced is reproduced. This can involve adding, deleting, renaming, linking, and unlinking files and directories. </p>
<p> A delta dump is defined as either an incremental dump (<i>xfsdump</i> <code>-l</code> option with level &gt; 0) or a resumed dump (<i>xfsdump</i> <code>-R</code> option). The deltas must be applied in the order they were produced. Each delta applied must have been produced with the previously applied delta as its base. </p>
<p> <i>xfsrestore</i> keeps state information in the <i>xfsrestorehousekeepingdir</i>, to inform subsequent invocations when used in cumulative mode, or in the event a restore is interrupted. To ensure that the state information can be processed, a compatible version of <i>xfsrestore</i> must be used for each subsequent invocation. Additionally, each invocation must run on a system of the same endianness and page size. </p>
<p> The options to <i>xfsrestore</i> are:</p>
<dl>
<dt><code>-a</code> <i>housekeeping</i></p>
<dd>Each invocation of <i>xfsrestore</i> creates a directory called <i>xfsrestorehousekeepingdir</i>. This directory is normally created directly under the <i>dest</i> directory. The <code>-a</code> option allows the operator to specify an alternate directory, <i>housekeeping</i>, in which <i>xfsrestore</i> creates the <i>xfsrestorehousekeepingdir</i> directory. When performing a cumulative (<code>-r</code> option) restore or resuming (<code>-R</code> option) a restore, each successive invocation must specify the same alternate directory.</p>
<dt><code>-b</code> <i>blocksize</i></p>
<dd>Specifies the blocksize, in bytes, to be used for the restore. For other drives such as DAT or 8 mm , the same blocksize used for the xfsdump operation must be specified to restore the tape. The default block size is 1Mb.</p>
<dt><code>-c</code> <i>progname</i></p>
<dd>Use the specified program to alert the operator when a media change is required. The alert program is typically a script to send a mail or flash a window to draw the operator&#8217;s attention.</p>
<dt><code>-e</code></p>
<dd>Prevents <i>xfsrestore</i> from overwriting existing files in the <i>dest</i> directory.</p>
<dt><code>-f</code> <i>source</i> [ <code>-f</code> <i>source</i> &#8230; ]</p>
<dd>Specifies a source of the dump to be restored. This can be the pathname of a device (such as a tape drive), a regular file or a remote tape drive (see <i><a href="/docs/linux/man/8-rmt/">rmt</a></i>(8)). This option must be omitted if the standard input option (a lone <code>&#8211;</code> preceding the <i>dest</i> specification) is specified.</p>
<dt><code>-i</code></p>
<dd>Selects interactive operation. Once the on-media directory hierarchy has been read, an interactive dialogue is begun. The operator uses a small set of commands to peruse the directory hierarchy, selecting files and subtrees for extraction. The available commands are given below. Initially nothing is selected, except for those subtrees specified with <code>-s</code> command line options.</p>
<dl>
<dd>
<dl>
<dt><code>ls</code> [<i>arg</i>]</p>
<dd>List the entries in the current directory or the specified directory, or the specified non-directory file entry. Both the entry&#8217;s original inode number and name are displayed. Entries that are directories are appended with a `/&#8217;. Entries that have been selected for extraction are prepended with a `*&#8217;.</p>
<dt><code>cd</code> [<i>arg</i>]</p>
<dd>Change the current working directory to the specified argument, or to the filesystem root directory if no argument is specified.</p>
<dt><code>pwd</code></p>
<dd>Print the pathname of the current directory, relative to the filesystem root.</p>
<dt><code>add</code> [<i>arg</i>]</p>
<dd>The current directory or specified file or directory within the current directory is selected for extraction. If a directory is specified, then it and all its descendents are selected. Entries that are selected for extraction are prepended with a `*&#8217; when they are listed by <code>ls</code>.</p>
<dt><code>delete</code> [<i>arg</i>]</p>
<dd>The current directory or specified file or directory within the current directory is deselected for extraction. If a directory is specified, then it and all its descendents are deselected. The most expedient way to extract most of the files from a directory is to select the directory and then deselect those files that are not needed.</p>
<dt><code>extract</code></p>
<dd>Ends the interactive dialogue, and causes all selected subtrees to be restored.</p>
<dt><code>quit</code></p>
<dd><i>xfsrestore</i> ends the interactive dialogue and immediately exits, even if there are files or subtrees selected for extraction.</p>
<dt><code>help</code></p>
<dd>List a summary of the available commands.</dl>
</dl>
<dt><code>-m</code></p>
<dd>Use the minimal tape protocol. This option cannot be used without specifying a blocksize to be used (see <code>-b</code> option above).</p>
<dt><code>-n</code> <i>file</i></p>
<dd>Allows <i>xfsrestore</i> to restore only files newer than <i>file</i>. The modification time of <i>file</i> (i.e., as displayed with the <code>ls -l</code> command) is compared to the inode modification time of each file on the source media (i.e., as displayed with the <code>ls -lc</code> command). A file is restored from media only if its inode modification time is greater than or equal to the modification time of <i>file</i>.</p>
<dt><code>-o</code></p>
<dd>Restore file and directory owner/group even if not root. When run with an effective user id of root, <i>xfsrestore</i> restores owner and group of each file and directory. When run with any other effective user id it does not, unless this option is specified.</p>
<dt><code>-p</code> <i>interval</i></p>
<dd>Causes progress reports to be printed at intervals of <i>interval</i> seconds. The interval value is approximate, <i>xfsrestore</i> will delay progress reports to avoid undue processing overhead.</p>
<dt><code>-q</code></p>
<dd>Source tape drive is a QIC tape. QIC tapes only use a 512 byte blocksize, for which <i>xfsrestore</i> must make special allowances.</p>
<dt><code>-r</code></p>
<dd>Selects the cumulative mode of operation. The <code>-a</code> and <i>destination</i> options must be the same for each invocation.</p>
<dt><code>-s</code> <i>subtree</i></p>
<dd>Specifies a subtree to restore. Any number of <code>-s</code> options are allowed. The restore is constrained to the union of all subtrees specified. Each subtree is specified as a pathname relative to the restore <i>dest</i>. If a directory is specified, the directory and all files beneath that directory are restored.</p>
<dt><code>-t</code></p>
<dd>Displays the contents of the dump, but does not create or modify any files or directories. It may be desirable to set the verbosity level to <code>silent</code> when using this option.</p>
<dt><code>-v</code> <i>verbosity</i></p>
<dd>
<dt><code>-v</code> <i>subsys</i>=<i>verbosity</i>[,<i>subsys</i>=<i>verbosity</i>,&#8230;]</p>
<dd>Specifies the level of detail used for messages displayed during the course of the restore. The <i>verbosity</i> argument can be passed as either a string or an integer. If passed as a string the following values may be used: <code>silent</code>, <code>verbose</code>, <code>trace</code>, <code>debug</code>, or <code>nitty</code>. If passed as an integer, values from 0-5 may be used. The values 0-4 correspond to the strings already listed. The value 5 can be used to produce even more verbose debug output. </p>
<p> The first form of this option activates message logging across all restore subsystems. The second form allows the message logging level to be controlled on a per-subsystem basis. The two forms can be combined (see the example below). The argument <i>subsys</i> can take one of the following values: <code>general</code>, <code>proc</code>, <code>drive</code>, <code>media</code>, <code>inventory</code>, and <code>tree</code>. </p>
<p> For example, to restore the root filesystem with tracing activated for all subsystems: <code> </p>
<p> </code></p>
<pre># xfsrestore -v trace -f /dev/tape /</pre>
<p>To enable debug-level tracing for drive and media operations: <code> </p>
<p> </code></p>
<pre># xfsrestore -v drive=debug,media=debug -f /dev/tape /</pre>
<p>To enable tracing for all subsystems, and debug level tracing for drive operations only: <code> </p>
<p> </code></p>
<pre># xfsrestore -v trace,drive=debug -f /dev/tape /</pre>
<dt><code>-A</code></p>
<dd>Do not restore extended file attributes. When restoring a filesystem managed within a DMF environment this option should not be used. DMF stores file migration status within extended attributes associated with each file. If these attributes are not preserved when the filesystem is restored, files that had been in migrated state will not be recallable by DMF. Note that dumping of extended file attributes is also optional.</p>
<dt><code>-B</code></p>
<dd>Change the ownership and permissions of the destination directory to match those of the root directory of the dump.</p>
<dt><code>-D</code></p>
<dd>Restore DMAPI (Data Management Application Programming Interface) event settings. If the restored filesystem will be managed within the same DMF environment as the original dump it is essential that the -D option be used. Otherwise it is not usually desirable to restore these settings.</p>
<dt><code>-E</code></p>
<dd>Prevents <i>xfsrestore</i> from overwriting newer versions of files. The inode modification time of the on-media file is compared to the inode modification time of corresponding file in the <i>dest</i> directory. The file is restored only if the on-media version is newer than the version in the <i>dest</i> directory. The inode modification time of a file can be displayed with the <code>ls -lc</code> command.</p>
<dt><code>-F</code></p>
<dd>Inhibit interactive operator prompts. This option inhibits <i>xfsrestore</i> from prompting the operator for verification of the selected dump as the restore target and from prompting for any media change.</p>
<dt><code>-I</code></p>
<dd>Causes the <i>xfsdump</i> inventory to be displayed (no restore is performed). Each time <i>xfsdump</i> is used, an online inventory in <i>/var/lib/xfsdump/inventory</i> is updated. This is used to determine the base for incremental dumps. It is also useful for manually identifying a dump session to be restored (see the <code>-L</code> and <code>-S</code> options). Suboptions to filter the inventory display are described later.</p>
<dt><code>-J</code></p>
<dd>Inhibits inventory update when on-media session inventory encountered during restore. <i>xfsrestore</i> opportunistically updates the online inventory when it encounters an on-media session inventory, but only if run with an effective user id of root and only if this option is not given.</p>
<dt><code>-K</code></p>
<dd>Force <i>xfsrestore</i> to use dump format 2 generation numbers. Normally the need for this is determined automatically, but this option is required on the first <i>xfsrestore</i> invocation in the rare case that a cumulative restore begins with a format 3 (or newer) dump and will be followed by a format 2 dump.</p>
<dt><code>-L</code> <i>session_label</i></p>
<dd>Specifies the label of the dump session to be restored. The source media is searched for this label. It is any arbitrary string up to 255 characters long. The label of the desired dump session can be copied from the inventory display produced by the <code>-I</code> option.</p>
<dt><code>-O</code> <i>options_file</i></p>
<dd>Insert the options contained in <i>options_file</i> into the beginning of the command line. The options are specified just as they would appear if typed into the command line. In addition, newline characters (
) can be used as whitespace. The options are placed before all options actually given on the command line, just after the command name. Only one <code>-O</code> option can be used. Recursive use is ignored. The destination directory cannot be specified in <i>options_file</i>.</p>
<dt><code>-Q</code></p>
<dd>Force completion of an interrupted restore session. This option is required to work around one specific pathological scenario. When restoring a dump session which was interrupted due to an EOM condition and no online session inventory is available, <i>xfsrestore</i> cannot know when the restore of that dump session is complete. The operator is forced to interrupt the restore session. In that case, if the operator tries to subsequently apply a resumed dump (using the <code>-r</code> option), <i>xfsrestore</i> refuses to do so. The operator must tell <i>xfsrestore</i> to consider the base restore complete by using this option when applying the resumed dump.</p>
<dt><code>-R</code></p>
<dd>Resume a previously interrupted restore. <i>xfsrestore</i> can be interrupted at any time by pressing the terminal interrupt character (see <i><a href="/docs/linux/man/1-stty/">stty</a></i>(1)). Use this option to resume the restore. The <code>-a</code> and <i>destination</i> options must be the same.</p>
<dt><code>-S</code> <i>session_id</i></p>
<dd>Specifies the session UUID of the dump session to be restored. The source media is searched for this UUID. The UUID of the desired dump session can be copied from the inventory display produced by the <code>-I</code> option.</p>
<dt><code>-T</code></p>
<dd>Inhibits interactive dialogue timeouts. <i>xfsrestore</i> prompts the operator for media changes. This dialogue normally times out if no response is supplied. This option prevents the timeout.</p>
<dt><code>-X</code> <i>subtree</i></p>
<dd>Specifies a subtree to exclude. This is the converse of the <code>-s</code> option. Any number of <code>-X</code> options are allowed. Each subtree is specified as a pathname relative to the restore <i>dest</i>. If a directory is specified, the directory and all files beneath that directory are excluded.</p>
<dt><code>-Y</code> <i>io_ring_length</i></p>
<dd>Specify I/O buffer ring length. <i>xfsrestore</i> uses a ring of input buffers to achieve maximum throughput when restoring from tape drives. The default ring length is 3. However, this is not currently enabled on Linux yet, making this option benign.</p>
<dt><code>&#8211;</code></p>
<dd>A lone <code>&#8211;</code> causes the standard input to be read as the source of the dump to be restored. Standard input can be a pipe from another utility (such as <i><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></i>(8)) or a redirected file. This option cannot be used with the <code>-f</code> option. The <code>&#8211;</code> must follow all other options, and precede the <i>dest</i> specification.</dl>
<p> The dumped filesystem is restored into the <i>dest</i> directory. There is no default; the <i>dest</i> must be specified.</p>
<h2>Notes</h2>
<h3>Cumulative Restoration</h3>
<p>A base (level 0) dump and an ordered set of delta dumps can be sequentially restored, each on top of the previous, to reproduce the contents of the original filesystem at the time the last delta was produced. The operator invokes <i>xfsrestore</i> once for each dump. The <code>-r</code> option must be specified. The <i>dest</i> directory must be the same for all invocations. Each invocation leaves a directory named <i>xfsrestorehousekeeping</i> in the <i>dest</i> directory (however, see the <code>-a</code> option above). This directory contains the state information that must be communicated between invocations. The operator must remove this directory after the last delta has been applied. </p>
<p> <i>xfsrestore</i> also generates a directory named <i>orphanage</i> in the <i>dest</i> directory. <i>xfsrestore</i> removes this directory after completing a simple restore. However, if <i>orphanage</i> is not empty, it is not removed. This can happen if files present on the dump media are not referenced by any of the restored directories. The <i>orphanage</i> has an entry for each such file. The entry name is the file&#8217;s original inode number, a &quot;.&quot;, and the file&#8217;s generation count modulo 4096 (only the lower 12 bits of the generation count are used). </p>
<p> <i>xfsrestore</i> does not remove the <i>orphanage</i> after cumulative restores. Like the <i>xfsrestorehousekeeping</i> directory, the operator must remove it after applying all delta dumps.</p>
<h3>Media Management</h3>
<p>A dump consists of one or more media files contained on one or more media objects. A media file contains all or a portion of the filesystem dump. Large filesystems are broken up into multiple media files to minimize the impact of media dropouts, and to accommodate media object boundaries (end-of-media). </p>
<p> A media object is any storage medium: a tape cartridge, a remote tape device (see <i><a href="/docs/linux/man/8-rmt/">rmt</a></i>(8)), a regular file, or the standard input (currently other removable media drives are not supported). Tape cartridges can contain multiple media files, which are typically separated by (in tape parlance) file marks. If a dump spans multiple media objects, the restore must begin with the media object containing the first media file dumped. The operator is prompted when the next media object is needed. </p>
<p> Media objects can contain more than one dump. The operator can select the desired dump by specifying the dump label (<code>-L</code> option), or by specifying the dump UUID (<code>-S</code> option). If neither is specified, <i>xfsrestore</i> scans the entire media object, prompting the operator as each dump session is encountered. </p>
<p> The inventory display (<code>-I</code> option) is useful for identifying the media objects required. It is also useful for identifying a dump session. The session UUID can be copied from the inventory display to the <code>-S</code> option argument to unambiguously identify a dump session to be restored. </p>
<p> Dumps placed in regular files or the standard output do not span multiple media objects, nor do they contain multiple dumps.</p>
<h3>Inventory</h3>
<p>Each dump session updates an inventory database in <i>/var/lib/xfsdump/inventory</i>. This database can be displayed by invoking <i>xfsrestore</i> with the <code>-I</code> option. The display uses tabbed indentation to present the inventory hierarchically. The first level is filesystem. The second level is session. The third level is media stream (currently only one stream is supported). The fourth level lists the media files sequentially composing the stream. </p>
<p> The following suboptions are available to filter the display.</p>
<dl>
<dt><code>-I depth=</code><i>n</i></p>
<dd>(where <i>n</i> is 1, 2, or 3) limits the hierarchical depth of the display. When <i>n</i> is 1, only the filesystem information from the inventory is displayed. When <i>n</i> is 2, only filesystem and session information are displayed. When <i>n</i> is 3, only filesystem, session and stream information are displayed.</p>
<dt><code>-I level=</code><i>n</i></p>
<dd>(where <i>n</i> is the dump level) limits the display to dumps of that particular dump level.</dl>
<p> The display may be restricted to media files contained in a specific media object.</p>
<dl>
<dt><code>-I mobjid=</code><i>value</i></p>
<dd>(where <i>value</i> is a media ID) specifies the media object by its media ID.</p>
<dt><code>-I mobjlabel=</code><i>value</i></p>
<dd>(where <i>value</i> is a media label) specifies the media object by its media label.</dl>
<p> Similarly, the display can be restricted to a specific filesystem.</p>
<dl>
<dt><code>-I mnt=</code><i>mount_point</i></p>
<dd>(that is, [hostname:]pathname), identifies the filesystem by mountpoint. Specifying the hostname is optional, but may be useful in a clustered environment where more than one host can be responsible for dumping a filesystem.</p>
<dt><code>-I fsid=</code><i>filesystem_id</i></p>
<dd>identifies the filesystem by filesystem ID.</p>
<dt><code>-I dev=</code><i>device_pathname</i></p>
<dd>(that is, [hostname:]device_pathname) identifies the filesystem by device. As with the <code>mnt</code> filter, specifying the hostname is optional.</dl>
<p> More than one of these suboptions, separated by commas, may be specified at the same time to limit the display of the inventory to those dumps of interest. However, at most four suboptions can be specified at once: one to constrain the display hierarchy depth, one to constrain the dump level, one to constrain the media object, and one to constrain the filesystem. </p>
<p> For example, <code>-I depth=1,mobjlabel=tape 1,mnt=host1:/test_mnt</code> would display only the filesystem information (depth=1) for those filesystems that were mounted on <i>host1:/test_mnt</i> at the time of the dump, and only those filesystems dumped to the media object labeled &quot;tape 1&quot;. </p>
<p> Dump records may be removed (pruned) from the inventory using the <i>xfsinvutil</i> program. </p>
<p> An additional media file is placed at the end of each dump stream. This media file contains the inventory information for the current dump session. If the online inventory files in <i>/var/lib/xfsdump/inventory</i> are missing information for the current dump session, then the inventory information in the media file is automatically added to the files in <i>/var/lib/xfsdump/inventory.</i> If you wish to incorporate the inventory information from the media file without restoring any data, you may do so using the <code>-t</code> option: <code> </p>
<p> </code></p>
<pre># xfsrestore -t -f /dev/tape</pre>
<p>This is useful to rebuild the inventory database if it is ever lost or corrupted. The only caveat is that <i>xfsrestore</i> needs to read through the entire dump in order to reach the inventory media file. This could become time consuming for dump sessions with large media files.</p>
<h3>Media Errors</h3>
<p><i>xfsdump</i> is tolerant of media errors, but cannot do error correction. If a media error occurs in the body of a media file, the filesystem file represented at that point is lost. The bad portion of the media is skipped, and the restoration resumes at the next filesystem file after the bad portion of the media. </p>
<p> If a media error occurs in the beginning of the media file, the entire media file is lost. For this reason, large dumps are broken into a number of reasonably sized media files. The restore resumes with the next media file.</p>
<h3>Quotas</h3>
<p>When <i>xfsdump</i> dumps a filesystem with user quotas, it creates a file in the root of the dump called <i>xfsdump_quotas</i>. <i>xfsrestore</i> can restore this file like any other file included in the dump. This file can be processed by the restore command of <i><a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a></i>(8) to reactivate the quotas. However, the <i>xfsdump_quotas</i> file contains information which may first require modification; specifically the filesystem name and the user ids. If you are restoring the quotas for the same users on the same filesystem from which the dump was taken, then no modification will be necessary. However, if you are restoring the dump to a different filesystem, you will need to:</p>
<dl>
<dt> &#8211;</p>
<dd>ensure the new filesystem is mounted with the quota option</p>
<dt> &#8211;</p>
<dd>modify the <i>xfsdump_quotas</i> file to contain the new filesystem name</p>
<dt> &#8211;</p>
<dd>ensure the uids in the <i>xfsdump_quotas</i> file are correct</dl>
<p> Once the quota information has been verified, the restore command of <i>xfs_quota (8)</i> can be used to apply the quota limits to the filesystem. </p>
<p> Group and project quotas are handled in a similar fashion and will be restored in files called <i>xfsdump_quotas_group</i> and <i>xfsdump_quotas_proj</i>, respectively.</p>
<h2>Examples</h2>
<p>To restore the root filesystem from a locally mounted tape: <code> </code></p>
<pre># xfsrestore -f /dev/tape /</pre>
<p>To restore from a remote tape, specifying the dump session id: <code> </code></p>
<pre># xfsrestore -L session_1 -f otherhost:/dev/tape /new</pre>
<p>To restore the contents a of a dump to another subdirectory: <code> </code></p>
<pre># xfsrestore -f /dev/tape /newdir</pre>
<p>To copy the contents of a filesystem to another directory (see <i><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></i>(8)): <code> </code></p>
<pre># xfsdump -J - / | xfsrestore -J - /new</pre>
<h2>Files</h2>
<dl>
<dt>/var/lib/xfsdump/inventory</p>
<dd>dump inventory database</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-rmt/">rmt</a>(8), <a href="/docs/linux/man/8-xfsdump/">xfsdump</a>(8), <a href="/docs/linux/man/8-xfsinvutil/">xfsinvutil</a>(8), <a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a>(8), <a href="/docs/linux/man/2-attr_set/">attr_set</a>(2).</p>
<h2>Diagnostics</h2>
<p>The exit code is 0 on normal completion, and non-zero if an error occurred or the restore was terminated by the operator. </p>
<p> For all verbosity levels greater than 0 (<code>silent</code>) the final line of the output shows the exit status of the restore. It is of the form: <code> </p>
<p> </code></p>
<pre>xfsdump: Restore Status: <i>code</i></pre>
<p>Where <i>code</i> takes one of the following values: <code>SUCCESS</code> (normal completion), <code>INTERRUPT</code> (interrupted), <code>QUIT</code> (media no longer usable), <code>INCOMPLETE</code> (restore incomplete), <code>FAULT</code> (software error), and <code>ERROR</code> (resource error). Every attempt will be made to keep both the syntax and the semantics of this log message unchanged in future versions of xfsrestore. However, it may be necessary to refine or expand the set of exit codes, or their interpretation at some point in the future.</p>
<h2>Bugs</h2>
<p>Pathnames of restored non-directory files (relative to the <i>dest</i> directory) must be 1023 characters (MAXPATHLEN) or less. Longer pathnames are discarded and a warning message displayed. There is no verify option to <i>xfsrestore</i>. This would allow the operator to compare a filesystem dump to an existing filesystem, without actually doing a restore. The interactive commands (<code>-i</code> option) do not understand regular expressions. When the minimal rmt option is specified, <i>xfsrestore</i> applies it to all remote tape sources. The same blocksize (specified by the <code>-b</code> option) is used for all these remote drives. <i>xfsrestore</i> uses the alert program only when a media change is required. Cumulative mode (<code>-r</code> option) requires that the operator invoke <i>xfsrestore</i> for the base and for each delta to be applied in sequence to the base. It would be better to allow the operator to identify the last delta in the sequence of interest, and let <i>xfsrestore</i> work backwards from that delta to identify and apply the preceding deltas and base dump, all in one invocation. </p>
