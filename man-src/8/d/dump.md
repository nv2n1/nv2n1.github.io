---

title: "dump(8)"
name: "dump"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dump/"
description: "dump – ext2/3/4 filesystem backup"
---

<p> dump - ext2/3/4 filesystem backup  </p>
<p> <code>dump </code> [<code>-</code><i>level#</i>] [<code>-ackMnqSuv] [-A </code><i>file</i>] [<code>-B </code><i>records</i>] [<code>-b </code><i>blocksize</i>] [<code>-d </code><i>density</i>] [<code>-D </code><i>file</i>] [<code>-e </code><i>inode numbers</i>] [<code>-E </code><i>file</i>] [<code>-f </code><i>file</i>] [<code>-F </code><i>script</i>] [<code>-h </code><i>level</i>] [<code>-I </code><i>nr errors</i>] [<code>-j</code><i>compression level</i>] [<code>-L </code><i>label</i>] [<code>-Q </code><i>file</i>] [<code>-s </code><i>feet</i>] [<code>-T </code><i>date</i>] [<code>-y</code>] [<code>-z</code><i>compression level</i>] <i>files-to-dump</i> </p>
<p> <code>dump </code> [<code>-W </code>| <code>-w</code>]  </p>
<p> <code>Dump</code> examines files on an ext2/3/4 filesystem and determines which files need to be backed up. These files are copied to the given disk, tape or other storage medium for safe keeping (see the <code>-f </code> option below for doing remote backups). A dump that is larger than the output medium is broken into multiple volumes. On most media the size is determined by writing until an end-of-media indication is returned. </p>
<p>On media that cannot reliably return an end-of-media indication (such as some cartridge tape drives), each volume is of a fixed size; the actual size is determined by specifying cartridge media, or via the tape size, density and/or block count options below. By default, the same output file name is used for each volume after prompting the operator to change media. </p>
<p> <i>files-to-dump</i> is either a mountpoint of a filesystem or a list of files and directories to be backed up as a subset of a filesystem. In the former case, either the path to a mounted filesystem or the device of an unmounted filesystem can be used. In the latter case, certain restrictions are placed on the backup: <code>-u</code> is not allowed, the only dump level that is supported is <code>0 </code> and all the files and directories must reside on the same filesystem.  </p>
<h2>OPTIONS</h2>
<p> The following options are supported by <code>dump:</code> </p>
<dl>
<dt><code>-level#</code></dt>
<dd> <p> The dump level (any integer). A level 0, full backup, specified by <code>-0</code> guarantees the entire file system is copied (but see also the <code>-h</code> option below). A level number above 0, incremental backup, tells <code>dump</code> to copy all files new or modified since the last dump of a lower level. The default level is 0. Historically only levels 0 to 9 were usable in dump, this version is able to understand any integer as a dump level. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> ``auto-size&#8217;&#8216;. Bypass all tape length calculations, and write until an end-of-media indication is returned. This works best for most modern tape drives, and is the default. Use of this option is particularly recommended when appending to an existing tape, or using a tape drive with hardware compression (where you can never be sure about the compression ratio). </p>
 </dd>
<dt><code>-A</code><i> archive_file</i></dt>
<dd> <p> Archive a dump table-of-contents in the specified <i>archive_file</i> to be used by <code><a href="/docs/linux/man/8-restore/">restore</a></code>(8) to determine whether a file is in the dump file that is being restored. </p>
 </dd>
<dt><code>-b</code><i> blocksize</i></dt>
<dd> <p> The number of kilobytes per dump record. The default blocksize is 10, unless the <code>-d</code> option has been used to specify a tape density of 6250BPI or more, in which case the default blocksize is 32. Th maximal value is 1024. Note however that, since the IO system slices all requests into chunks of <code>MAXBSIZE</code> (which can be as low as 64kB), you can experience problems with <code><a href="/docs/linux/man/8-dump/">dump</a></code>(8) and <code><a href="/docs/linux/man/8-restore/">restore</a></code>(8) when using a higher value, depending on your kernel and/or libC versions. </p>
 </dd>
<dt><code>-B</code><i> records</i></dt>
<dd> <p> The number of 1 kB blocks per volume. Not normally required, as <code>dump</code> can detect end-of-media. When the specified size is reached, <code>dump</code> waits for you to change the volume. This option overrides the calculation of tape size based on length and density. If compression is on this limits the size of the compressed output per volume. Multiple values may be given as a single argument separated by commas. Each value will be used for one dump volume in the order listed; if <code>dump</code> creates more volumes than the number of values given, the last value will be used for the remaining volumes. This is useful for filling up already partially filled media (and then continuing with full size volumes on empty media) or mixing media of different sizes. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Change the defaults for use with a cartridge tape drive, with a density of 8000 bpi, and a length of 1700 feet. Specifying a cartridge drive overrides the end-of-media detection. </p>
 </dd>
<dt><code>-d</code><i> density</i></dt>
<dd> <p> Set tape density to <i>density</i>. The default is 1600BPI. Specifying a tape density overrides the end-of-media detection. </p>
 </dd>
<dt><code>-D</code><i> file</i></dt>
<dd> <p> Set the path name of the file storing the information about the previous full and incremental dumps. The default location is <i>/etc/dumpdates</i>. </p>
 </dd>
<dt><code>-e</code><i> inodes</i></dt>
<dd> <p> Exclude <i>inodes</i> from the dump. The <i>inodes</i> parameter is a comma separated list of inode numbers (you can use <code><a href="/docs/linux/man/1-stat/">stat</a></code>(1) to find the inode number for a file or directory). </p>
 </dd>
<dt><code>-E</code><i> file</i></dt>
<dd> <p> Read list of inodes to be excluded from the dump from the text file <i>file</i>. The file <i>file</i> should be an ordinary file containing inode numbers separated by newlines. </p>
 </dd>
<dt><code>-f</code><i> file</i></dt>
<dd> <p> Write the backup to <i>file</i>; <i>file</i> may be a special device file like <i>/dev/st0</i> (a tape drive), <i>/dev/rsd1c</i> (a floppy disk drive), an ordinary file, or <i>-</i> (the standard output). Multiple file names may be given as a single argument separated by commas. Each file will be used for one dump volume in the order listed; if the dump requires more volumes than the number of names given, the last file name will used for all remaining volumes after prompting for media changes. If the name of the file is of the form <i>host:file</i> or <i>user [at] host:file</i> <code>dump</code> writes to the named file on the remote host (which should already exist, dump doesn&#8217;t create a new remote file) using <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8). The default path name of the remote <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8) program is <i>/etc/rmt</i>; this can be overridden by the environment variable <code>RMT</code>. </p>
 </dd>
<dt><code>-F</code><i> script</i></dt>
<dd> <p> Run script at the end of each tape (except for the last one). The device name and the current volume number are passed on the command line. The script must return 0 if <code>dump</code> should continue without asking the user to change the tape, 1 if <code>dump</code> should continue but ask the user to change the tape. Any other exit code will cause <code>dump</code> to abort. For security reasons, <code>dump</code> reverts back to the real user ID and the real group ID before running the script. </p>
 </dd>
<dt><code>-h</code><i> level</i></dt>
<dd> <p> Honor the user <code>nodump</code> flag <code>UF_NODUMP</code> only for dumps at or above the given <i>level</i>. The default honor level is 1, so that incremental backups omit such files but full backups retain them. </p>
 </dd>
<dt><code>-I</code><i> nr errors</i></dt>
<dd> <p> By default, <code>dump</code> will ignore the first 32 read errors on the file system before asking for operator intervention. You can change this using this flag to any value. This is useful when running <code>dump</code> on an active filesystem where read errors simply indicate an inconsistency between the mapping and dumping passes. </p>
 </dd>
<dd> <p> A value of 0 means that all read errors will be ignored. </p>
 </dd>
<dt><code>-j</code><i>compression level</i></dt>
<dd> <p> Compress every block to be written on the tape using bzlib library. This option will work only when dumping to a file or pipe or, when dumping to a tape drive, if the tape drive is capable of writing variable length blocks. You will need at least the 0.4b24 version of <code>restore</code> in order to extract compressed tapes. Tapes written using compression will not be compatible with the BSD tape format. The (optional) parameter specifies the compression level bzlib will use. The default compression level is 2. If the optional parameter is specified, there should be no white space between the option letter and the parameter. </p>
 </dd>
<dt><code>-k</code></dt>
<dd> <p> Use Kerberos authentication to talk to remote tape servers. (Only available if this option was enabled when <code>dump</code> was compiled.) </p>
 </dd>
<dt><code>-L</code><i> label</i></dt>
<dd> <p> The user-supplied text string <i>label</i> is placed into the dump header, where tools like <code><a href="/docs/linux/man/8-restore/">restore</a></code>(8) and <code>file</code>(8) can access it. Note that this label is limited to be at most <code>LBLSIZE</code> (currently 16) characters, which must include the terminating \0. </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> If this flag is specified, <code>dump</code> will optimise the output for inodes having been changed but not modified since the last dump (&#8216;changed&#8217; and &#8216;modified&#8217; have the meaning defined in <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) ). For those inodes, <code>dump</code> will save only the metadata, instead of saving the entire inode contents. Inodes which are either directories or have been modified since the last dump are saved in a regular way. Uses of this flag must be consistent, meaning that either every dump in an incremental dump set have the flag, or no one has it. </p>
 </dd>
<dd> <p> If you use this option, be aware that many programs that unpack files from archives (e.g. tar, rpm, unzip, dpkg) may set files&#8217; mtimes to dates in the past. Files installed in this way may not be dumped correctly using &quot;dump -m&quot; if the modified mtime is earlier than the previous level dump. </p>
 </dd>
<dd> <p> Tapes written using such &#8216;metadata only&#8217; inodes will not be compatible with the BSD tape format or older versions of <code>restore.</code> </p>
 </dd>
<dt><code>-M</code></dt>
<dd> <p> Enable the multi-volume feature. The name specified with <code>f </code> is treated as a prefix and <code>dump</code> writes in sequence to <i>&lt;prefix&gt;001, &lt;prefix&gt;002 </i> etc. This can be useful when dumping to files on an ext2/3/4 partition, in order to bypass the 2GB file size limitation. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Whenever <code>dump</code> requires operator attention, notify all operators in the group <code>operator</code> by means similar to a <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1). </p>
 </dd>
<dt><code>-q</code></dt>
<dd> <p> Make <code>dump</code> abort immediately whenever operator attention is required, without prompting in case of write errors, tape changes etc. </p>
 </dd>
<dt><code>-Q</code><i> file</i></dt>
<dd> <p> Enable the Quick File Access support. Tape positions for each inode are stored into the file <i>file</i> which is used by <code>restore</code> (if called with parameter <code>-Q</code> and the filename) to directly position the tape at the file <code>restore </code> is currently working on. This saves hours when restoring single files from large backups, saves the tapes and the drive&#8217;s head. </p>
 </dd>
<dd> <p> It is recommended to set up the st driver to return logical tape positions rather than physical before calling <code>dump/restore </code> with parameter <code>-Q</code>. Since not all tape devices support physical tape positions those tape devices return an error during <code>dump/restore</code> when the st driver is set to the default physical setting. Please see the <code><a href="/docs/linux/man/4-st/">st</a></code>(4) man page, option <code>MTSETDRVBUFFER</code> , or the <code><a href="/docs/linux/man/1-mt/">mt</a></code>(1) man page, on how to set the driver to return logical tape positions. </p>
 </dd>
<dd> <p> Before calling <code>restore</code> with parameter <code>-Q</code>, always make sure the st driver is set to return the same type of tape position used during the call to <code>dump</code>. Otherwise <code>restore</code> may be confused. </p>
 </dd>
<dd> <p> This option can be used when dumping to local tapes (see above) or to local files. </p>
 </dd>
<dt><code>-s</code><i> feet</i></dt>
<dd> <p> Attempt to calculate the amount of tape needed at a particular density. If this amount is exceeded, <code>dump</code> prompts for a new tape. It is recommended to be a bit conservative on this option. The default tape length is 2300 feet. Specifying the tape size overrides end-of-media detection. </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> Size estimate. Determine the amount of space that is needed to perform the dump without actually doing it, and display the estimated number of bytes it will take. This is useful with incremental dumps to determine how many volumes of media will be needed. </p>
 </dd>
<dt><code>-T</code><i> date</i></dt>
<dd> <p> Use the specified date as the starting time for the dump instead of the time determined from looking in <i>/etc/dumpdates .</i> The format of <i>date</i> is the same as that of <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) followed by an rfc822 timezone specification: either a plus or minus sign followed by two digits for the number of hours and two digits for the minutes. For example, -0800 for eight hours west of Greenwich or +0230 for two hours and a half east of Greenwich. This timezone offset takes into account daylight savings time (if applicable to the timezone): UTC offsets when daylight savings time is in effect will be different than offsets when daylight savings time is not in effect. For backward compatibility, if no timezone is specified, a local time is assumed. This option is useful for automated dump scripts that wish to dump over a specific period of time. The <code>-T</code> option is mutually exclusive from the <code>-u</code> option. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Update the file <i>/etc/dumpdates</i> after a successful dump. The format of <i>/etc/dumpdates</i> is readable by people, consisting of one free format record per line: filesystem name, increment level and <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) format dump date followed by a rfc822 timezone specification (see the <code>-u</code> option for details). If no timezone offset is specified, times are interpreted as local. Whenever the file is written, all dates in the file are converted to the local time zone, without changing the UTC times. There may be only one entry per filesystem at each level. The file <i>/etc/dumpdates</i> may be edited to change any of the fields, if necessary. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> The <code>-v</code> (verbose) makes <code>dump</code> to print extra information which could be helpful in debug sessions. </p>
 </dd>
<dt><code>-W</code></dt>
<dd> <p> <code>Dump</code> tells the operator what file systems need to be dumped. This information is gleaned from the files <i>/etc/dumpdates</i> and <i>/etc/fstab</i>. The <code>-W</code> option causes <code>dump</code> to print out, for all file systems in <i>/etc/dumpdates ,</i> and recognized file systems in <i>/etc/mtab</i> and <i>/etc/fstab</i>. the most recent dump date and level, and highlights those that should be dumped. If the <code>-W</code> option is set, all other options are ignored, and <code>dump</code> exits immediately. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Is like <code>-W</code>, but prints only recognized filesystems in <i>/etc/mtab</i> and <i>/etc/fstab</i> which need to be dumped. </p>
 </dd>
<dt><code>-y</code></dt>
<dd> <p> Compress every block to be written to the tape using the lzo library. This doesn&#8217;t compress as well as the zlib library but it&#8217;s much faster. This option will work only when dumping to a file or pipe or, when dumping to a tape drive, if the tape drive is capable of writing variable length blocks. You will need at least the 0.4b34 version of <code>restore</code> in order to extract compressed tapes. Tapes written using compression will not be compatible with the BSD tape format. </p>
 </dd>
<dt><code>-z</code><i>compression level</i></dt>
<dd> <p> Compress every block to be written on the tape using zlib library. This option will work only when dumping to a file or pipe or, when dumping to a tape drive, if the tape drive is capable of writing variable length blocks. You will need at least the 0.4b22 version of <code>restore</code> in order to extract compressed tapes. Tapes written using compression will not be compatible with the BSD tape format. The (optional) parameter specifies the compression level zlib will use. The default compression level is 2. If the optional parameter is specified, there should be no white space between the option letter and the parameter. </p>
 </dd></dl>
<p> <code>Dump</code> requires operator intervention on these conditions: end of tape, end of dump, tape write error, tape open error or disk read error (if there is more than a threshold of nr errors). In addition to alerting all operators implied by the <code>-n</code> key, <code>dump</code> interacts with the operator on dump&#8217;s control terminal at times when <code>dump</code> can no longer proceed, or if something is grossly wrong. All questions <code>dump</code> poses <i>must</i> be answered by typing ``yes&#8217;&#8216; or ``no&#8217;&#8216;, appropriately. </p>
<p>Since making a dump involves a lot of time and effort for full dumps, <code>dump</code> checkpoints itself at the start of each tape volume. If writing that volume fails for some reason, <code>dump</code> will, with operator permission, restart itself from the checkpoint after the old tape has been rewound and removed, and a new tape has been mounted. </p>
<p> <code>Dump</code> tells the operator what is going on at periodic intervals, including usually low estimates of the number of blocks to write, the number of tapes it will take, the time to completion, and the time to the tape change. The output is verbose, so that others know that the terminal controlling <code>dump</code> is busy, and will be for some time. </p>
<p>In the event of a catastrophic disk event, the time required to restore all the necessary backup tapes or files to disk can be kept to a minimum by staggering the incremental dumps. An efficient method of staggering incremental dumps to minimize the number of tapes follows: </p>
<dl>
<dt>---</dt>
<dd> <p> Always start with a level 0 backup, for example: </p>
 </dd>
<dl>
<dd> <p> <code>/sbin/dump -0u -f /dev/st0 /usr/src</code> </p>
 </dd></dl>
<dd> <p> This should be done at set intervals, say once a month or once every two months, and on a set of fresh tapes that is saved forever. </p>
 </dd>
<dt>---</dt>
<dd> <p> After a level 0, dumps of active file systems are taken on a daily basis, with this sequence of dump levels: </p>
 </dd>
<dl>
<dd> <p> <code>3 2 5 4 7 6 9 8 9 9 ...</code> </p>
 </dd></dl>
<dd> <p> For the daily dumps, it should be possible to use a fixed number of tapes for each day, used on a weekly basis. Each week, a level 1 dump is taken, and the daily Hanoi sequence repeats beginning with 3. For weekly dumps, another fixed set of tapes per dumped file system is used, also on a cyclical basis. </p>
 </dd></dl>
<p>After several months or so, the daily and weekly tapes should get rotated out of the dump cycle and fresh tapes brought in. </p>
<p>Another backup strategy is the Tower of Hanoi sequence, which reuses older tapes in a way that for newer dates the available restore points are more frequent, then for older dates (see <a rel="nofollow" href="http://en.wikipedia.org/wiki/Backup_rotation_scheme">http://en.wikipedia.org/wiki/Backup_rotation_scheme</a> for additional information). </p>
<p>(The 4.3BSD option syntax is implemented for backward compatibility but is not documented here.)  </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TAPE</code></dt>
<dd> <p> If no <code>-f </code> option was specified, <code>dump</code> will use the device specified via <code>TAPE</code> as the dump device. <code>TAPE</code> may be of the form <i>tapename</i>, <i>host:tapename</i>, or <i>user [at] host:tapename</i>. </p>
 </dd>
<dt><code>RMT</code></dt>
<dd> <p> The environment variable <code>RMT</code> will be used to determine the pathname of the remote <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8) program. </p>
 </dd>
<dt><code>RSH</code></dt>
<dd> <p> <code>Dump</code> uses the contents of this variable to determine the name of the remote shell command to use when doing remote backups (rsh, ssh etc.). If this variable is not set, <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3) will be used, but only root will be able to do remote backups. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/dev/st0</i></dt>
<dd> <p> default tape unit to dump to </p>
 </dd>
<dt><i>/etc/dumpdates</i></dt>
<dd> <p> dump date records </p>
 </dd>
<dt><i>/etc/fstab</i></dt>
<dd> <p> dump table: file systems and frequency </p>
 </dd>
<dt><i>/etc/mtab</i></dt>
<dd> <p> dump table: mounted file systems </p>
 </dd>
<dt><i>/etc/group</i></dt>
<dd> <p> to find group <i>operator</i> </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-restore/">restore</a></code>(8), <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8)  </p>
<h2>DIAGNOSTICS</h2>
<p> Many, and verbose.  </p>
<h2>COMPATIBILITY</h2>
<p> The format of the <i>/etc/dumpdates</i> file has changed in release 0.4b34, however, the file will be read correctly with either pre-0.4b34 or 0.4b34 and later versions of <code>dump</code> provided that the machine on which <code>dump</code> is run did not change timezones (which should be a fairly rare occurrence).  </p>
<h2>EXIT STATUS</h2>
<p> <code>Dump</code> exits with zero status on success. Startup errors are indicated with an exit code of 1; abnormal termination is indicated with an exit code of 3.  </p>
<h2>BUGS</h2>
<p> It might be considered a bug that this version of dump can only handle ext2/3/4 filesystems. Specifically, it does not work with FAT filesystems. </p>
<p>Fewer than 32 read errors (change this with <code>-I</code>) on the filesystem are ignored. If noticing read errors is important, the output from dump can be parsed to look for lines that contain the text &#8216;read error&#8217;. </p>
<p>When a read error occurs, <code>dump</code> prints out the corresponding physical disk block and sector number and the ext2/3/4 logical block number. It doesn&#8217;t print out the corresponding file name or even the inode number. The user has to use <code><a href="/docs/linux/man/8-debugfs/">debugfs</a></code>(8), commands <code>ncheck</code> and <code>icheck</code> to translate the <code>ext2blk</code> number printed out by <code>dump</code> into an inode number, then into a file name. </p>
<p>Each reel requires a new process, so parent processes for reels already written just hang around until the entire tape is written. </p>
<p>The estimated number of tapes is not correct if compression is on. </p>
<p>It would be nice if <code>dump</code> knew about the dump sequence, kept track of the tapes scribbled on, told the operator which tape to mount when, and provided more assistance for the operator running <code>restore</code>. </p>
<p> <code>Dump</code> cannot do remote backups without being run as root, due to its security history. Presently, it works if you set it setuid (like it used to be), but this might constitute a security risk. Note that you can set <code>RSH</code> to use a remote shell program instead.  </p>
<h2>AUTHOR</h2>
<p> The <code>dump/restore</code> backup suite was ported to Linux&#8217;s Second Extended File System by Remy Card &lt;card [at] Linux.EU.Org&gt;. He maintained the initial versions of <code>dump</code> (up and including 0.4b4, released in January 1997). </p>
<p>Starting with 0.4b5, the new maintainer is Stelian Pop &lt;stelian [at] popies.net&gt;.  </p>
<h2>AVAILABILITY</h2>
<p> The <code>dump/restore</code> backup suite is available from &lt;<a rel="nofollow" href="http://dump.sourceforge.net">http://dump.sourceforge.net</a>&gt;  </p>
<h2>HISTORY</h2>
<p> A <code>dump</code> command appeared in <code>Version 6 AT&amp;T UNIX.</code> </p>
