---
title: "xfsdump(8)"
name: "xfsdump"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfsdump/"
description: "xfsdump – XFS filesystem incremental dump utility"
---

<p>xfsdump &#8211; XFS filesystem incremental dump utility</p>
<h2>Synopsis</h2>
<pre><code>xfsdump</code> -h
<code>xfsdump</code> [ options ] -f <i>dest</i> [ -f <i>dest</i> ... ] <i>filesystem</i>
<code>xfsdump</code> [ options ] - <i>filesystem</i>
<code>xfsdump</code> -I [ subopt=value ... ]</pre>
<h2>Description</h2>
<p><i>xfsdump</i> backs up files and their attributes in a filesystem. The files are dumped to storage media, a regular file, or standard output. Options allow the operator to have all files dumped, just files that have changed since a previous dump, or just files contained in a list of pathnames. </p>
<p> The <i><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></i>(8) utility re-populates a filesystem with the contents of the dump. </p>
<p> Each invocation of <i>xfsdump</i> dumps just one filesystem. That invocation is termed a dump session. The dump session splits the filesystem into one or more dump streams, one per destination. The split is done in filesystem inode number (ino) order, at boundaries selected to equalize the size of each stream. Furthermore, the breakpoints between streams may be in the middle of very large files (at extent boundaries) if necessary to achieve reasonable stream size equalization. Each dump stream can span several media objects, and a single media object can contain several dump streams. The typical media object is a tape cartridge. The media object records the dump stream as one or more media files. A media file is a self-contained partial dump, intended to minimize the impact of media dropouts on the entire dump stream at the expense of increasing the time required to complete the dump. By default only one media file is written unless a media file size is specified using the <code>-d</code> option. Other techniques, such as making a second copy of the dump image, provide more protection against media failures than multiple media files will. </p>
<p> <i>xfsdump</i> maintains an online dump inventory in <i>/var/lib/xfsdump/inventory</i>. The <code>-I</code> option displays the inventory contents hierarchically. The levels of the hierarchy are: filesystem, dump session, stream, and media file. </p>
<p> The options to <i>xfsdump</i> are:</p>
<dl>
<dt><code>-a</code></p>
<dd>Specifies that files for which the Data Migration Facility (DMF) has complete offline copies (dual-state files) be treated as if they were offline (OFL). This means that the file data will not be dumped by xfsdump, resulting in a smaller dump file. If the file is later restored the file data is still accessible through DMF. If both &#8216;-a option&#8217; and &#8216;-z option&#8217; are specified, the &#8216;-a option&#8217; takes precedence (see &#8216;-z option&#8217; below).</p>
<dt><code>-b</code> <i>blocksize</i></p>
<dd>Specifies the blocksize, in bytes, to be used for the dump. The same blocksize must be specified to restore the tape. If the <code>-m</code> option is not used, then <code>-b</code> does not need to be specified. Instead, a default blocksize of 1Mb will be used.</p>
<dt><code>-c</code> <i>progname</i></p>
<dd>Use the specified program to alert the operator when a media change is required. The alert program is typically a script to send a mail or flash a window to draw the operator&#8217;s attention.</p>
<dt><code>-d</code> <i>filesize</i></p>
<dd>Specifies the size, in megabytes, of dump media files. If not specified, xfsdump will dump data to tape using a single media file per media object. The specified media file size may need to be adjusted if, for example, xfsdump cannot fit a media file onto a single tape.</p>
<dt><code>-e</code></p>
<dd>Allow files to be excluded from the dump. This will cause xfsdump to skip files which have the &quot;no dump&quot; file attribute set. See the &quot;Excluding individual files&quot; section below for details on setting this file attribute.</p>
<dt><code>-f</code> <i>dest</i> [ <code>-f</code> <i>dest</i> &#8230; ]</p>
<dd>Specifies a dump destination. A dump destination can be the pathname of a device (such as a tape drive), a regular file or a remote tape drive (see <i><a href="/docs/linux/man/8-rmt/">rmt</a></i>(8)). This option must be omitted if the standard output option (a lone <code>&#8211;</code> preceding the source filesystem specification) is specified.</p>
<dt><code>-l</code> <i>level</i></p>
<dd>Specifies a dump level of 0 to 9. The dump level determines the base dump to which this dump is relative. The base dump is the most recent dump at a lesser level. A level 0 dump is absolute &#8211; all files are dumped. A dump level where 1 &lt;= <i>level</i> &lt;= 9 is referred to as an incremental dump. Only files that have been changed since the base dump are dumped. Subtree dumps (see the <code>-s</code> option below) cannot be used as the base for incremental dumps.</p>
<dt><code>-m</code></p>
<dd>Use the minimal tape protocol for non-scsi tape destinations or remote tape destinations which are not scsi Linux tape drives nor IRIX tape drives. This option cannot be used without specifying a blocksize to be used (see <code>-b</code> option above).</p>
<dt><code>-o</code></p>
<dd>Overwrite the tape. With this option, <i>xfsdump </i> does not read the tape first to check the contents. This option may be used if <i>xfsdump </i> is unable to determine the block size of a tape .</p>
<dt><code>-p</code> <i>interval</i></p>
<dd>Causes progress reports to be printed at the specified interval. <i>interval</i> is given in seconds. The progress report indicates how many files have been dumped, the total number of files to dump, the percentage of data dumped, and the elapsed time.</p>
<dt><code>-q</code></p>
<dd>Destination tape drive is a QIC tape. QIC tapes only use a 512 byte blocksize, for which <i>xfsdump</i> must make special allowances.</p>
<dt><code>-s</code> <i>pathname</i> [ <code>-s</code> <i>pathname</i> &#8230; ]</p>
<dd>Restricts the dump to files contained in the specified pathnames (subtrees). A <i>pathname</i> must be relative to the mount point of the filesystem. For example, if a filesystem is mounted at <i>/d2</i>, the <i>pathname</i> argument for the directory <i>/d2/users</i> is &#8220;users&#8221;. A <i>pathname</i> can be a file or a directory; if it is a directory, the entire hierarchy of files and subdirectories rooted at that directory is dumped. Subtree dumps cannot be used as the base for incremental dumps (see the <code>-l</code> option above).</p>
<dt><code>-t</code> <i>file</i></p>
<dd>Sets the dump time to the modification time of <i>file</i> rather than using the current time. <i>xfsdump</i> uses the dump time to determine what files need to be backed up during an incremental dump. This option should be used when dumping snapshots so that the dump time matches the time the snapshot was taken. Otherwise files modified after a snapshot is taken may be skipped in the next incremental dump.</p>
<dt><code>-v</code> <i>verbosity</i></p>
<dd>
<dt><code>-v</code> <i>subsys</i>=<i>verbosity</i>[,<i>subsys</i>=<i>verbosity</i>,&#8230;]</p>
<dd>Specifies the level of detail used for messages displayed during the course of the dump. The <i>verbosity</i> argument can be passed as either a string or an integer. If passed as a string the following values may be used: <code>silent</code>, <code>verbose</code>, <code>trace</code>, <code>debug</code>, or <code>nitty</code>. If passed as an integer, values from 0-5 may be used. The values 0-4 correspond to the strings already listed. The value 5 can be used to produce even more verbose debug output. </p>
<p> The first form of this option activates message logging across all dump subsystems. The second form allows the message logging level to be controlled on a per-subsystem basis. The two forms can be combined (see the example below). The argument <i>subsys</i> can take one of the following values: <code>general</code>, <code>proc</code>, <code>drive</code>, <code>media</code>, <code>inventory</code>, <code>inomap</code> and <code>excluded_files</code>. </p>
<p> For example, to dump the root filesystem with tracing activated for all subsystems: <code> </p>
<p> </code></p>
<pre># xfsdump -v trace -f /dev/tape /</pre>
<p>To enable debug-level tracing for drive and media operations: <code> </p>
<p> </code></p>
<pre># xfsdump -v drive=debug,media=debug -f /dev/tape /</pre>
<p>To enable tracing for all subsystems, and debug level tracing for drive operations only: <code> </p>
<p> </code></p>
<pre># xfsdump -v trace,drive=debug -f /dev/tape /</pre>
<p>To list files that will be excluded from the dump: <code> </p>
<p> </code></p>
<pre># xfsdump -e -v excluded_files=debug -f /dev/tape /</pre>
<dt><code>-z</code> <i>size</i></p>
<dd>Specifies the maximum size, in kilobytes, of files to be included in the dump. Files over this size, will be excluded from the dump, except for DMF dual-state files when &#8216;-a option&#8217; is specified (see &#8216;-a option&#8217; above). When specified, &#8216;-a option&#8217; takes precedence over &#8216;-z option&#8217;. The size is an estimate based on the number of disk blocks actually used by the file, and so does not include holes. In other words, size refers to the amount of space the file would take in the resulting dump. On an interactive restore, the skipped file is visible with xfsrestore&#8217;s &#8216;ls&#8217; and while you can use the &#8216;add&#8217; and &#8216;extract&#8217; commands, nothing will be restored.</p>
<dt><code>-A</code></p>
<dd>Do not dump extended file attributes. When dumping a filesystem managed within a DMF environment this option should not be used. DMF stores file migration status within extended attributes associated with each file. If these attributes are not preserved when the filesystem is restored, files that had been in migrated state will not be recallable by DMF. Note that dumps containing extended file attributes cannot be restored with older versions of <i><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></i>(8).</p>
<dt><code>-B</code> <i>session_id</i></p>
<dd>Specifies the ID of the dump session upon which this dump session is to be based. If this option is specified, the <code>-l</code> (level) and <code>-R</code> (resume) options are not allowed. Instead, <code>xfsdump</code> determines if the current dump session should be incremental and/or resumed, by looking at the base session&#8217;s level and interrupted attributes. If the base session was interrupted, the current dump session is a resumption of that base at the same level. Otherwise, the current dump session is an incremental dump with a level one greater than that of the base session. This option allows incremental and resumed dumps to be based on any previous dump, rather than just the most recent.</p>
<dt><code>-D</code></p>
<dd>Controls which directories are backed up during an incremental dump. By default unchanged directories are dumped if files or directories beneath them have changed. This results in a self-contained dump &#8212; if a base dump is lost, or you know the file(s) you wish to restore is in an incremental dump, you can restore just that dump without loading the base dump(s) first. However, this method requires a potentially expensive traversal through the filesystem. </p>
<p> When <code>-D</code> is specified, unchanged directories are not dumped. This results in a faster dump, but files will end up in the <i><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></i>(8) <i>orphanage</i> directory unless the base dump(s) is loaded first.</p>
<dt><code>-E</code></p>
<dd>Pre-erase media. If this option is specified, media is erased prior to use. The operator is prompted for confirmation, unless the <code>-F</code> option is also specified.</p>
<dt><code>-F</code></p>
<dd>Don&#8217;t prompt the operator. When <i>xfsdump</i> encounters a media object containing non-xfsdump data, <i>xfsdump</i> normally asks the operator for permission to overwrite. With this option the overwrite is performed, no questions asked. When <i>xfsdump</i> encounters end-of-media during a dump, <i>xfsdump</i> normally asks the operator if another media object will be provided. With this option the dump is instead interrupted.</p>
<dt><code>-I</code></p>
<dd>Displays the <i>xfsdump</i> inventory (no dump is performed). <i>xfsdump</i> records each dump session in an online inventory in <i>/var/lib/xfsdump/inventory</i>. <i>xfsdump</i> uses this inventory to determine the base for incremental dumps. It is also useful for manually identifying a dump session to be restored. Suboptions to filter the inventory display are described later.</p>
<dt><code>-J</code></p>
<dd>Inhibits the normal update of the inventory. This is useful when the media being dumped to will be discarded or overwritten.</p>
<dt><code>-K</code></p>
<dd>Generate a format 2 dump instead of the current format. This is useful if the dump will be restored on a system with an older <i>xfsrestore</i> which does not understand the current dump format. Use of this option is otherwise not recommended.</p>
<dt><code>-L</code> <i>session_label</i></p>
<dd>Specifies a label for the dump session. It can be any arbitrary string up to 255 characters long.</p>
<dt><code>-M</code> <i>label</i> [ <code>-M</code> <i>label</i> &#8230; ]</p>
<dd>Specifies a label for the first media object (for example, tape cartridge) written on the corresponding destination during the session. It can be any arbitrary string up to 255 characters long. Multiple media object labels can be specified, one for each destination.</p>
<dt><code>-O</code> <i>options_file</i></p>
<dd>Insert the options contained in <i>options_file</i> into the beginning of the command line. The options are specified just as they would appear if typed into the command line. In addition, newline characters (
) can be used as whitespace. The options are placed before all options actually given on the command line, just after the command name. Only one <code>-O</code> option can be used. Recursive use is ignored. The source filesystem cannot be specified in <i>options_file</i>.</p>
<dt><code>-R</code></p>
<dd>Resumes a previously interrupted dump session. If the most recent dump at this dump&#8217;s level (<code>-l</code> option) was interrupted, this dump contains only files not in the interrupted dump and consistent with the incremental level. However, files contained in the interrupted dump that have been subsequently modified are re-dumped.</p>
<dt><code>-T</code></p>
<dd>Inhibits interactive dialogue timeouts. When the <code>-F</code> option is not specified, <i>xfsdump</i> prompts the operator for labels and media changes. Each dialogue normally times out if no response is supplied. This option prevents the timeout.</p>
<dt><code>-Y</code> <i>length</i></p>
<dd>Specify I/O buffer ring length. <i>xfsdump</i> uses a ring of output buffers to achieve maximum throughput when dumping to tape drives. The default ring length is 3. However, this is not currently enabled on Linux yet, making this option benign.</p>
<dt><code>&#8211;</code></p>
<dd>A lone <code>&#8211;</code> causes the dump stream to be sent to the standard output, where it can be piped to another utility such as <i><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></i>(8) or redirected to a file. This option cannot be used with the <code>-f</code> option. The <code>&#8211;</code> must follow all other options and precede the filesystem specification.</dl>
<p> The filesystem, <i>filesystem</i>, can be specified either as a mount point or as a special device file (for example, <i>/dev/dsk/dks0d1s0</i>). The filesystem must be mounted to be dumped.</p>
<h2>Notes</h2>
<h3>Dump Interruption</h3>
<p>A dump can be interrupted at any time and later resumed. To interrupt, type control-C (or the current terminal interrupt character). The operator is prompted to select one of several operations, including dump interruption. After the operator selects dump interruption, the dump continues until a convenient break point is encountered (typically the end of the current file). Very large files are broken into smaller subfiles, so the wait for the end of the current file is brief.</p>
<h3>Dump Resumption</h3>
<p>A previously interrupted dump can be resumed by specifying the <code>-R</code> option. If the most recent dump at the specified level was interrupted, the new dump does not include files already dumped, unless they have changed since the interrupted dump.</p>
<h3>Media Management</h3>
<p>A single media object can contain many dump streams. Conversely, a single dump stream can span multiple media objects. If a dump stream is sent to a media object already containing one or more dumps, <i>xfsdump</i> appends the new dump stream after the last dump stream. Media files are never overwritten. If end-of-media is encountered during the course of a dump, the operator is prompted to insert a new media object into the drive. The dump stream continuation is appended after the last media file on the new media object.</p>
<h3>Inventory</h3>
<p>Each dump session updates an inventory database in <i>/var/lib/xfsdump/inventory</i>. <i>xfsdump</i> uses the inventory to determine the base of incremental and resumed dumps. </p>
<p> This database can be displayed by invoking <i>xfsdump</i> with the <code>-I</code> option. The display uses tabbed indentation to present the inventory hierarchically. The first level is filesystem. The second level is session. The third level is media stream (currently only one stream is supported). The fourth level lists the media files sequentially composing the stream. </p>
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
<p> An additional media file is placed at the end of each dump stream. This media file contains the inventory information for the current dump session. Its contents may be merged back into the online inventory database at a later time using <i><a href="//www.systutorials.com/docs/linux/man/1M-xfsrestore/">xfsrestore</a></i>(1M). </p>
<p> The inventory files stored in <i>/var/lib/xfsdump</i> are not included in the dump, even if that directory is contained within the filesystem being dumped. Including the inventory in the dump may lead to loss or corruption of data, should an older version be restored overwriting the current version. To backup the <i>xfsdump</i> inventory, the contents of <i>/var/lib/xfsdump</i> should be copied to another location which may then be safely dumped. Upon restoration, those files may be copied back into <i>/var/lib/xfsdump</i>, overwriting whatever files may be there, or <i><a href="//www.systutorials.com/docs/linux/man/1M-xfsinvutil/">xfsinvutil</a></i>(1M) may be used to selectively merge parts of the restored inventory back into the current inventory. Prior to version 1.1.8, <i>xfsdump</i> would include the <i>/var/lib/xfsdump</i> directory in the dump. Care should be taken not to overwrite the <i>/var/lib/xfsdump</i> directory when restoring an old dump, by either restoring the filesystem to another location or by copying the current contents of <i>/var/lib/xfsdump</i> to a safe place prior to running <i><a href="//www.systutorials.com/docs/linux/man/1M-xfsrestore/">xfsrestore</a></i>(1M).</p>
<h3>Labels</h3>
<p>The operator can specify a label to identify the dump session and a label to identify a media object. The session label is placed in every media file produced in the course of the dump, and is recorded in the inventory. </p>
<p> The media label is used to identify media objects, and is independent of the session label. Each media file on the media object contains a copy of the media label. An error is returned if the operator specifies a media label that does not match the media label on a media object containing valid media files. Media labels are recorded in the inventory.</p>
<h3>UUIDs</h3>
<p>UUIDs (Universally Unique Identifiers) are used in three places: to identify the filesystem being dumped (using the filesystem UUID, see <i><a href="/docs/linux/man/5-xfs/">xfs</a></i>(5) for more details), to identify the dump session, and to identify each media object. The inventory display (<code>-I</code>) includes all of these.</p>
<h3>Dump Level Usage</h3>
<p>The dump level mechanism provides a structured form of incremental dumps. A dump of level <i>level</i> includes only files that have changed since the most recent dump at a level less than <i>level</i>. For example, the operator can establish a dump schedule that involves a full dump every Friday and a daily incremental dump containing only files that have changed since the previous dump. In this case Friday&#8217;s dump would be at level 0, Saturday&#8217;s at level 1, Sunday&#8217;s at level 2, and so on, up to the Thursday dump at level 6. </p>
<p> The above schedule results in a very tedious restore procedure to fully reconstruct the Thursday version of the filesystem; <i>xfsrestore</i> would need to be fed all 7 dumps in sequence. A compromise schedule is to use level 1 on Saturday, Monday, and Wednesday, and level 2 on Sunday, Tuesday, and Thursday. The Monday and Wednesday dumps would take longer, but the worst case restore requires the accumulation of just three dumps, one each at level 0, level 1, and level 2.</p>
<h3>Quotas</h3>
<p>If the filesystem being dumped contains user quotas, <i>xfsdump</i> will use <i><a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a></i>(8) to store the quotas in a file called <i>xfsdump_quotas </i> in the root of the filesystem to be dumped. This file will then be included in the dump. Upon restoration, <i>xfs_quota (8)</i> can be used to reactivate the quotas for the filesystem. Note, however, that the <i>xfsdump_quotas</i> file will probably require modification to change the filesystem or UIDs if the filesystem has been restored to a different partition or system. Group and project quotas will be handled in a similar fashion and saved in files called <i>xfsdump_quotas_group</i> and <i>xfsdump_quotas_proj ,</i> respectively.</p>
<h3>Excluding individual files</h3>
<p>It may be desirable to exclude particular files or directories from the dump. The <code>-s</code> option can be used to limit the dump to a specified directory, and the <code>-z</code> option can be used to exclude files over a particular size. Additionally, when <i>xfsdump</i> is run with the <code>-e</code> option, files that are tagged with the &quot;no dump&quot; file attribute will not be included in the dump. The <i><a href="/docs/linux/man/1-chattr/">chattr</a></i>(1) command can be used to set this attribute on individual files or entire subtrees. </p>
<p> To tag an individual file for exclusion from the dump: <code> </p>
<p> </code></p>
<pre>$ chattr +d file</pre>
<p>To tag all files in a subtree for exclusion from the dump: <code> </p>
<p> </code></p>
<pre>$ chattr -R +d directory</pre>
<p>Note that any new files or directories created in a directory which has the &quot;no dump&quot; attribute set will automatically inherit this attribute. Also note that <i>xfsdump</i> does not check directories for the &quot;no dump&quot; attribute. </p>
<p> Care should be taken to note which files have been tagged. Under normal operation, <i>xfsdump</i> will only report the number of files it will skip. The <code>-v excluded_files=debug</code> option, however, will cause <i>xfsdump</i> to list the inode numbers of the individual files affected.</p>
<h2>Examples</h2>
<p>To perform a level 0, single stream dump of the root filesystem to a locally mounted tape drive, prompting for session and media labels when required: <code> </code></p>
<pre># xfsdump -f /dev/tape /</pre>
<p>To specify session and media labels explicitly: <code> </code></p>
<pre># xfsdump -L session_1 -M tape_0 -f /dev/tape /</pre>
<p>To perform a dump to a remote tape using the minimal rmt protocol and a set blocksize of 64k: <code> </code></p>
<pre># xfsdump -m -b 65536 -f otherhost:/dev/tape /</pre>
<p>To perform a level 0, multi-stream dump to two locally mounted tape drives: <code> </code></p>
<pre># xfsdump -L session_2 -f /dev/rmt/tps4d6v -M tape_1 \
 -f /dev/rmt/tps5d6v -M tape_2 /</pre>
<p>To perform a level 1 dump relative to the last level 0 dump recorded in the inventory: <code> </code></p>
<pre># xfsdump -l 1 -f /dev/tape /</pre>
<p>To copy the contents of a filesystem to another directory (see <i><a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a></i>(8)): <code> </code></p>
<pre># xfsdump -J - / | xfsrestore -J - /new</pre>
<h2>Files</h2>
<dl>
<dt>/var/lib/xfsdump/inventory</p>
<dd>dump inventory database</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-attr/">attr</a>(1), <a href="/docs/linux/man/8-rmt/">rmt</a>(8), <a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a>(8), <a href="/docs/linux/man/8-xfsinvutil/">xfsinvutil</a>(8), <a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a>(8), <a href="/docs/linux/man/2-attr_get/">attr_get</a>(2).</p>
<h2>Diagnostics</h2>
<p>The exit code is 0 on normal completion, non-zero if an error occurs or the dump is terminated by the operator. </p>
<p> For all verbosity levels greater than 0 (<code>silent</code>) the final line of the output shows the exit status of the dump. It is of the form: <code> </p>
<p> </code></p>
<pre>xfsdump: Dump Status: <i>code</i></pre>
<p>Where <i>code</i> takes one of the following values: <code>SUCCESS</code> (normal completion), <code>INTERRUPT</code> (interrupted), <code>QUIT</code> (media no longer usable), <code>INCOMPLETE</code> (dump incomplete), <code>FAULT</code> (software error), and <code>ERROR</code> (resource error). Every attempt will be made to keep both the syntax and the semantics of this log message unchanged in future versions of xfsdump. However, it may be necessary to refine or expand the set of exit codes, or their interpretation at some point in the future. </p>
<p> The message &#8220;xfsdump: WARNING: unable to open directory: ino N: Invalid argument&#8221; can occur with filesystems which are actively being modified while <i>xfsdump</i> is running. This can happen to either directory or regular file inodes &#8211; affected files will not end up in the dump, files below affected directories will be placed in the <i>orphanage</i> directory by <i>xfsrestore</i>.</p>
<h2>Bugs</h2>
<p><i>xfsdump</i> does not dump unmounted filesystems. The dump frequency field of <i>/etc/fstab</i> is not supported. <i>xfsdump</i> uses the alert program only when a media change is required. <i>xfsdump</i> requires root privilege (except for inventory display). <i>xfsdump</i> can only dump XFS filesystems. The media format used by <i>xfsdump</i> can only be understood by <i>xfsrestore</i>. <i>xfsdump</i> does not know how to manage CD-ROM or other removable disk drives. <i>xfsdump</i> can become confused when doing incremental or resumed dumps if on the same machine you dump two XFS filesystems and both filesystems have the same filesystem identifier (UUID). Since <i>xfsdump</i> uses the filesystem identifier to identify filesystems, <i>xfsdump</i> maintains one combined set of dump inventories for both filesystems instead of two sets of dump inventories. This scenario can happen only if <i>dd</i> or some other block-by-block copy program was used to make a copy of an XFS filesystem. See <i><a href="/docs/linux/man/8-xfs_copy/">xfs_copy</a></i>(8) and <i><a href="/docs/linux/man/5-xfs/">xfs</a></i>(5) for more details. </p>
