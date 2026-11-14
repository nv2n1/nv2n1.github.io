---
title: "dump(8)"
name: "dump"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dump/"
description: "dump – ext2/3/4 filesystem backup"
---

<p>dump &#8211; ext2/3/4 filesystem backup</p>
<h2>Synopsis</h2>
<p><code>dump </code> [<code>&#8211;</code><i>level#</i>] [<code>-ackMnqSuv] [-A </code><i>file</i>] [<code>-B </code><i>records</i>] [<code>-b </code><i>blocksize</i>] [<code>-d </code><i>density</i>] [<code>-D </code><i>file</i>] [<code>-e </code><i>inode numbers</i>] [<code>-E </code><i>file</i>] [<code>-f </code><i>file</i>] [<code>-F </code><i>script</i>] [<code>-h </code><i>level</i>] [<code>-I </code><i>nr errors</i>] [<code>-j</code><i>compression level</i>] [<code>-L </code><i>label</i>] [<code>-Q </code><i>file</i>] [<code>-s </code><i>feet</i>] [<code>-T </code><i>date</i>] [<code>-y</code>] [<code>-z</code><i>compression level</i>] <i>files-to-dump</i> </p>
<p> <code>dump </code> [<code>-W </code>| <code>-w</code>]</p>
<h2>Description</h2>
<p><code>Dump</code> examines files on an ext2/3/4 filesystem and determines which files need to be backed up. These files are copied to the given disk, tape or other storage medium for safe keeping (see the <code>-f </code> option below for doing remote backups). A dump that is larger than the output medium is broken into multiple volumes. On most media the size is determined by writing until an end-of-media indication is returned. </p>
<p> On media that cannot reliably return an end-of-media indication (such as some cartridge tape drives), each volume is of a fixed size; the actual size is determined by specifying cartridge media, or via the tape size, density and/or block count options below. By default, the same output file name is used for each volume after prompting the operator to change media. </p>
<p> <i>files-to-dump</i> is either a mountpoint of a filesystem or a list of files and directories to be backed up as a subset of a filesystem. In the former case, either the path to a mounted filesystem or the device of an unmounted filesystem can be used. In the latter case, certain restrictions are placed on the backup: <code>-u</code> is not allowed, the only dump level that is supported is <code>0 </code> and all the files and directories must reside on the same filesystem.</p>
<h2>Options</h2>
<p>The following options are supported by <code>dump:</code></p>
<dl>
<dt><code>-level#</code></p>
<dd>The dump level (any integer). A level 0, full backup, specified by <code>-0</code> guarantees the entire file system is copied (but see also the <code>-h</code> option below). A level number above 0, incremental backup, tells <code>dump</code> to copy all files new or modified since the last dump of a lower level. The default level is 0. Historically only levels 0 to 9 were usable in dump, this version is able to understand any integer as a dump level.</p>
<dt><code>-a</code></p>
<dd>&#8220;auto-size&#8221;. Bypass all tape length calculations, and write until an end-of-media indication is returned. This works best for most modern tape drives, and is the default. Use of this option is particularly recommended when appending to an existing tape, or using a tape drive with hardware compression (where you can never be sure about the compression ratio).</p>
<dt><code>-A</code><i> archive_file</i></p>
<dd>Archive a dump table-of-contents in the specified <i>archive_file</i> to be used by <code><a href="/docs/linux/man/8-restore/">restore</a></code>(8) to determine whether a file is in the dump file that is being restored.</p>
<dt><code>-b</code><i> blocksize</i></p>
<dd>The number of kilobytes per dump record. The default blocksize is 10, unless the <code>-d</code> option has been used to specify a tape density of 6250BPI or more, in which case the default blocksize is 32. Th maximal value is 1024. Note however that, since the IO system slices all requests into chunks of <code>MAXBSIZE</code> (which can be as low as 64kB), you can experience problems with <code><a href="/docs/linux/man/8-dump/">dump</a></code>(8) and <code><a href="/docs/linux/man/8-restore/">restore</a></code>(8) when using a higher value, depending on your kernel and/or libC versions.</p>
<dt><code>-B</code><i> records</i></p>
<dd>The number of 1 kB blocks per volume. Not normally required, as <code>dump</code> can detect end-of-media. When the specified size is reached, <code>dump</code> waits for you to change the volume. This option overrides the calculation of tape size based on length and density. If compression is on this limits the size of the compressed output per volume. Multiple values may be given as a single argument separated by commas. Each value will be used for one dump volume in the order listed; if <code>dump</code> creates more volumes than the number of values given, the last value will be used for the remaining volumes. This is useful for filling up already partially filled media (and then continuing with full size volumes on empty media) or mixing media of different sizes.</p>
<dt><code>-c</code></p>
<dd>Change the defaults for use with a cartridge tape drive, with a density of 8000 bpi, and a length of 1700 feet. Specifying a cartridge drive overrides the end-of-media detection.</p>
<dt><code>-d</code><i> density</i></p>
<dd>Set tape density to <i>density</i>. The default is 1600BPI. Specifying a tape density overrides the end-of-media detection.</p>
<dt><code>-D</code><i> file</i></p>
<dd>Set the path name of the file storing the information about the previous full and incremental dumps. The default location is <i>/etc/dumpdates</i>.</p>
<dt><code>-e</code><i> inodes</i></p>
<dd>Exclude <i>inodes</i> from the dump. The <i>inodes</i> parameter is a comma separated list of inode numbers (you can use <code><a href="/docs/linux/man/1-stat/">stat</a></code>(1) to find the inode number for a file or directory).</p>
<dt><code>-E</code><i> file</i></p>
<dd>Read list of inodes to be excluded from the dump from the text file <i>file</i>. The file <i>file</i> should be an ordinary file containing inode numbers separated by newlines.</p>
<dt><code>-f</code><i> file</i></p>
<dd>Write the backup to <i>file</i>; <i>file</i> may be a special device file like <i>/dev/st0</i> (a tape drive), <i>/dev/rsd1c</i> (a floppy disk drive), an ordinary file, or <i>&#8211;</i> (the standard output). Multiple file names may be given as a single argument separated by commas. Each file will be used for one dump volume in the order listed; if the dump requires more volumes than the number of names given, the last file name will used for all remaining volumes after prompting for media changes. If the name of the file is of the form <i>host:file</i> or <i>user [at] host:file</i> <code>dump</code> writes to the named file on the remote host (which should already exist, dump doesn&#8217;t create a new remote file) using <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8). The default path name of the remote <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8) program is <i>/etc/rmt</i>; this can be overridden by the environment variable <code>RMT</code>.</p>
<dt><code>-F</code><i> script</i></p>
<dd>Run script at the end of each tape (except for the last one). The device name and the current volume number are passed on the command line. The script must return 0 if <code>dump</code> should continue without asking the user to change the tape, 1 if <code>dump</code> should continue but ask the user to change the tape. Any other exit code will cause <code>dump</code> to abort. For security reasons, <code>dump</code> reverts back to the real user ID and the real group ID before running the script.</p>
<dt><code>-h</code><i> level</i></p>
<dd>Honor the user <code>nodump</code> flag <code>UF_NODUMP</code> only for dumps at or above the given <i>level</i>. The default honor level is 1, so that incremental backups omit such files but full backups retain them.</p>
<dt><code>-I</code><i> nr errors</i></p>
<dd>By default, <code>dump</code> will ignore the first 32 read errors on the file system before asking for operator intervention. You can change this using this flag to any value. This is useful when running <code>dump</code> on an active filesystem where read errors simply indicate an inconsistency between the mapping and dumping passes.</p>
<dd>A value of 0 means that all read errors will be ignored.</p>
<dt><code>-j</code><i>compression level</i></p>
<dd>Compress every block to be written on the tape using bzlib library. This option will work only when dumping to a file or pipe or, when dumping to a tape drive, if the tape drive is capable of writing variable length blocks. You will need at least the 0.4b24 version of <code>restore</code> in order to extract compressed tapes. Tapes written using compression will not be compatible with the BSD tape format. The (optional) parameter specifies the compression level bzlib will use. The default compression level is 2. If the optional parameter is specified, there should be no white space between the option letter and the parameter.</p>
<dt><code>-k</code></p>
<dd>Use Kerberos authentication to talk to remote tape servers. (Only available if this option was enabled when <code>dump</code> was compiled.)</p>
<dt><code>-L</code><i> label</i></p>
<dd>The user-supplied text string <i>label</i> is placed into the dump header, where tools like <code><a href="/docs/linux/man/8-restore/">restore</a></code>(8) and <code><a href="/docs/linux/man/8-file/">file</a></code>(8) can access it. Note that this label is limited to be at most <code>LBLSIZE</code> (currently 16) characters, which must include the terminating 
