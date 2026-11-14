---
title: "restore(8)"
name: "restore"
section: "8"
letter: "r"
url: "/docs/linux/man/8-restore/"
description: "restore – restore files or file systems from backups made with dump"
---

<p>restore &#8211; restore files or file systems from backups made with dump</p>
<h2>Synopsis</h2>
<p><code>restore -C </code> [<code>-cdHklMvVy</code>] [<code>-b </code><i>blocksize</i>] [<code>-D </code><i>filesystem</i>] [<code>-f </code><i>file</i>] [<code>-F </code><i>script</i>] [<code>-L </code><i>limit</i>] [<code>-s </code><i>fileno</i>] [<code>-T </code><i>directory</i>] </p>
<p> <code>restore -i</code> [<code>-acdhHklmMNouvVy</code>] [<code>-A </code><i>file</i>] [<code>-b </code><i>blocksize</i>] [<code>-f </code><i>file</i>] [<code>-F </code><i>script</i>] [<code>-Q </code><i>file</i>] [<code>-s </code><i>fileno</i>] [<code>-T </code><i>directory</i>] </p>
<p> <code>restore -P </code> <i>file</i> [<code>-acdhHklmMNuvVy</code>] [<code>-b </code><i>blocksize</i>] [<code>-f </code><i>file</i>] [<code>-F </code><i>script</i>] [<code>-s </code><i>fileno</i>] [<code>-T </code><i>directory</i>] [<code>-X </code><i>filelist</i>] [ <i>file &#8230; </i>] </p>
<p> <code>restore -R</code> [<code>-cdHklMNuvVy</code>] [<code>-b </code><i>blocksize</i>] [<code>-f </code><i>file</i>] [<code>-F </code><i>script</i>] [<code>-s </code><i>fileno</i>] [<code>-T </code><i>directory</i>] </p>
<p> <code>restore -r </code> [<code>-cdHklMNuvVy</code>] [<code>-b </code><i>blocksize</i>] [<code>-f </code><i>file</i>] [<code>-F </code><i>script</i>] [<code>-s </code><i>fileno</i>] [<code>-T </code><i>directory</i>] </p>
<p> <code>restore -t</code> [<code>-cdhHklMNuvVy</code>] [<code>-A </code><i>file</i>] [<code>-b </code><i>blocksize</i>] [<code>-f </code><i>file</i>] [<code>-F </code><i>script</i>] [<code>-Q </code><i>file</i>] [<code>-s </code><i>fileno</i>] [<code>-T </code><i>directory</i>] [<code>-X </code><i>filelist</i>] [ <i>file &#8230; </i>] </p>
<p> <code>restore -x </code> [<code>-adchHklmMNouvVy</code>] [<code>-A </code><i>file</i>] [<code>-b </code><i>blocksize</i>] [<code>-f </code><i>file</i>] [<code>-F </code><i>script</i>] [<code>-Q </code><i>file</i>] [<code>-s </code><i>fileno</i>] [<code>-T </code><i>directory</i>] [<code>-X </code><i>filelist</i>] [ <i>file &#8230; </i>]</p>
<h2>Description</h2>
<p>The <code>restore</code> command performs the inverse function of <code><a href="/docs/linux/man/8-dump/">dump</a></code>(8). A full backup of a file system may be restored and subsequent incremental backups layered on top of it. Single files and directory subtrees may be restored from full or partial backups. <code>Restore</code> works across a network; to do this see the <code>-f</code> flag described below. Other arguments to the command are file or directory names specifying the files that are to be restored. Unless the <code>-h</code> flag is specified (see below), the appearance of a directory name refers to the files and (recursively) subdirectories of that directory. </p>
<p> Exactly one of the following flags is required:</p>
<dl>
<dt><code>-C</code></p>
<dd>This mode allows comparison of files from a dump. <code>Restore</code> reads the backup and compares its contents with files present on the disk. It first changes its working directory to the root of the filesystem that was dumped and compares the tape with the files in its new current directory. See also the <code>-L</code> flag described below.</p>
<dt><code>-i</code></p>
<dd>This mode allows interactive restoration of files from a dump. After reading in the directory information from the dump, <code>restore</code> provides a shell like interface that allows the user to move around the directory tree selecting files to be extracted. The available commands are given below; for those commands that require an argument, the default is the current directory.</p>
<dl>
<dd>
<dl>
<dt><code>add </code>[<i>arg</i>]</p>
<dd>The current directory or specified argument is added to the list of files to be extracted. If a directory is specified, then it and all its descendants are added to the extraction list (unless the <code>-h</code> flag is specified on the command line). Files that are on the extraction list are prepended with a &#8220;*&#8221; when they are listed by <code>ls</code>.</p>
<dt><code>cd</code><i> arg</i></p>
<dd>Change the current working directory to the specified argument.</p>
<dt><code>delete </code>[<i>arg</i>]</p>
<dd>The current directory or specified argument is deleted from the list of files to be extracted. If a directory is specified, then it and all its descendants are deleted from the extraction list (unless the <code>-h</code> flag is specified on the command line). The most expedient way to extract most of the files from a directory is to add the directory to the extraction list and then delete those files that are not needed.</p>
<dt><code>extract</code></p>
<dd>All files on the extraction list are extracted from the dump. <code>Restore</code> will ask which volume the user wishes to mount. The fastest way to extract a few files is to start with the last volume and work towards the first volume.</p>
<dt><code>help</code></p>
<dd>List a summary of the available commands.</p>
<dt><code>ls </code>[<i>arg</i>]</p>
<dd>List the current or specified directory. Entries that are directories are appended with a &#8220;/&#8221;. Entries that have been marked for extraction are prepended with a &#8220;*&#8221;. If the verbose flag is set, the inode number of each entry is also listed.</p>
<dt><code>pwd</code></p>
<dd>Print the full pathname of the current working directory.</p>
<dt><code>quit</code></p>
<dd><code>Restore</code> immediately exits, even if the extraction list is not empty.</p>
<dt><code>setmodes</code></p>
<dd>All directories that have been added to the extraction list have their owner, modes, and times set; nothing is extracted from the dump. This is useful for cleaning up after a <code>restore </code> has been prematurely aborted.</p>
<dt><code>verbose</code></p>
<dd>The sense of the <code>-v</code> flag is toggled. When set, the verbose flag causes the <code>ls</code> command to list the inode numbers of all entries. It also causes <code>restore</code> to print out information about each file as it is extracted.</dl>
</dl>
<dt><code>-P</code><i> file</i></p>
<dd><code>Restore</code> creates a new Quick File Access file <i>file</i> from an existing dump file without restoring its contents.</p>
<dt><code>-R</code></p>
<dd><code>Restore</code> requests a particular tape of a multi-volume set on which to restart a full restore (see the <code>-r</code> flag below). This is useful if the restore has been interrupted.</p>
<dt><code>-r</code></p>
<dd>Restore (rebuild) a file system. The target file system should be made pristine with <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), mounted, and the user <code>cd</code>&#8216;d into the pristine file system before starting the restoration of the initial level 0 backup. If the level 0 restores successfully, the <code>-r</code> flag may be used to restore any necessary incremental backups on top of the level 0. The <code>-r</code> flag precludes an interactive file extraction and can be detrimental to one&#8217;s health (not to mention the disk) if not used carefully. An example:</p>
<dd>
<dl>
<dd><code>mke2fs /dev/sda1</code></p>
<dl>
<dt><code>mount /dev/sda1 /mnt</code></p>
<dd>
<dt><code>cd /mnt</code></p>
<dd>
<dt><code>restore rf /dev/st0</code></p>
<dd></dl>
</dl>
<dd>Note that <code>restore</code> leaves a file <i>restoresymtable</i> in the root directory to pass information between incremental restore passes. This file should be removed when the last incremental has been restored.</p>
<dd><code>Restore</code>, in conjunction with <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) and <code><a href="/docs/linux/man/8-dump/">dump</a></code>(8), may be used to modify file system parameters such as size or block size.</p>
<dt><code>-t</code></p>
<dd>The names of the specified files are listed if they occur on the backup. If no file argument is given, the root directory is listed, which results in the entire content of the backup being listed, unless the <code>-h</code> flag has been specified. Note that the <code>-t</code> flag replaces the function of the old <code><a href="/docs/linux/man/8-dumpdir/">dumpdir</a></code>(8) program. See also the <code>-X</code> option below.</p>
<dt><code>-x</code></p>
<dd>The named files are read from the given media. If a named file matches a directory whose contents are on the backup and the <code>-h</code> flag is not specified, the directory is recursively extracted. The owner, modification time, and mode are restored (if possible). If no file argument is given, the root directory is extracted, which results in the entire content of the backup being extracted, unless the <code>-h</code> flag has been specified. See also the <code>-X</code> option below.</dl>
<h2>Options</h2>
<p>The following additional options may be specified:</p>
<dl>
<dt><code>-a</code></p>
<dd>In <code>-i</code> or <code>-x</code> mode, <code>restore </code> does ask the user for the volume number on which the files to be extracted are supposed to be (in order to minimise the time by reading only the interesting volumes). The <code>-a</code> option disables this behaviour and reads all the volumes starting with 1. This option is useful when the operator does not know on which volume the files to be extracted are and/or when he prefers the longer unattended mode rather than the shorter interactive mode.</p>
<dt><code>-A</code><i> archive_file</i></p>
<dd>Read the table of contents from <i>archive_file</i> instead of the media. This option can be used in combination with the <code>-t</code>, <code>-i</code>, or <code>-x </code> options, making it possible to check whether files are on the media without having to mount the media.</p>
<dt><code>-b</code><i> blocksize</i></p>
<dd>The number of kilobytes per dump record. If the <code>-b</code> option is not specified, <code>restore</code> tries to determine the media block size dynamically.</p>
<dt><code>-c</code></p>
<dd>Normally, <code>restore</code> will try to determine dynamically whether the dump was made from an old (pre-4.4) or new format file system. The <code>-c</code> flag disables this check, and only allows reading a dump in the old format.</p>
<dt><code>-d</code></p>
<dd>The <code>-d</code> (debug) flag causes <code>restore</code> to print debug information.</p>
<dt><code>-D</code><i> filesystem</i></p>
<dd>The <code>-D</code> flag allows the user to specify the filesystem name when using <code>restore</code> with the <code>-C</code> option to check the backup.</p>
<dt><code>-f</code><i> file</i></p>
<dd>Read the backup from <i>file</i>; <i>file</i> may be a special device file like <i>/dev/st0</i> (a tape drive), <i>/dev/sda1</i> (a disk drive), an ordinary file, or <i>&#8211;</i> (the standard input). If the name of the file is of the form <i>host:file </i> or <i>user [at] host:file</i>, <code>restore</code> reads from the named file on the remote host using <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8).</p>
<dt><code>-F</code><i> script</i></p>
<dd>Run script at the beginning of each tape. The device name and the current volume number are passed on the command line. The script must return 0 if <code>restore</code> should continue without asking the user to change the tape, 1 if <code>restore</code> should continue but ask the user to change the tape. Any other exit code will cause <code>restore</code> to abort. For security reasons, <code>restore</code> reverts back to the real user ID and the real group ID before running the script.</p>
<dt><code>-h</code></p>
<dd>Extract the actual directory, rather than the files that it references. This prevents hierarchical restoration of complete subtrees from the dump.</p>
<dt><code>-H</code><i> hash_size</i></p>
<dd>Use a hashtable having the specified number of entries for storing the directories entries instead of a linked list. This hashtable will considerably speed up inode lookups (visible especially in interactive mode when adding/removing files from the restore list), but at the price of much more memory usage. The default value is 1, meaning no hashtable is used.</p>
<dt><code>-k</code></p>
<dd>Use Kerberos authentication when contacting the remote tape server. (Only available if this options was enabled when <code>restore</code> was compiled.)</p>
<dt><code>-l</code></p>
<dd>When doing remote restores, assume the remote file is a regular file (instead of a tape device). If you&#8217;re restoring a remote compressed file, you will need to specify this option or <code>restore</code> will fail to access it correctly.</p>
<dt><code>-L</code><i> limit</i></p>
<dd>The <code>-L</code> flag allows the user to specify a maximal number of miscompares when using <code>restore</code> with the <code>-C</code> option to check the backup. If this limit is reached, <code>restore</code> will abort with an error message. A value of 0 (the default value) disables the check.</p>
<dt><code>-m</code></p>
<dd>Extract by inode numbers rather than by file name. This is useful if only a few files are being extracted, and one wants to avoid regenerating the complete pathname to the file.</p>
<dt><code>-M</code></p>
<dd>Enables the multi-volume feature (for reading dumps made using the <code>-M</code> option of dump). The name specified with <code>-f</code> is treated as a prefix and <code>restore</code> tries to read in sequence from <i>&lt;prefix&gt;001, &lt;prefix&gt;002 </i> etc.</p>
<dt><code>-N</code></p>
<dd>The <code>-N</code> flag causes <code>restore</code> to perform a full execution as requested by one of <code>-i</code>, <code>-R</code>, <code>-r</code>, <code>t</code> or <code>x</code> command without actually writing any file on disk.</p>
<dt><code>-o</code></p>
<dd>The <code>-o</code> flag causes <code>restore</code> to automatically restore the current directory permissions without asking the operator whether to do so in one of <code>-i</code> or <code>-x</code> modes.</p>
<dt><code>-Q</code><i> file</i></p>
<dd>Use the file <i>file</i> in order to read tape position as stored using the dump Quick File Access mode, in one of <code>-i</code>, <code>-x</code> or <code>-t</code> mode.</p>
<dd>It is recommended to set up the st driver to return logical tape positions rather than physical before calling <code>dump/restore</code> with parameter <code>-Q</code>. Since not all tape devices support physical tape positions those tape devices return an error during <code>dump/restore</code> when the st driver is set to the default physical setting. Please see the <code><a href="/docs/linux/man/4-st/">st</a></code>(4) man page, option <code>MTSETDRVBUFFER</code> , or the <code><a href="/docs/linux/man/1-mt/">mt</a>(1)</code> man page, on how to set the driver to return logical tape positions.</p>
<dd>Before calling <code>restore</code> with parameter <code>-Q</code>, always make sure the st driver is set to return the same type of tape position used during the call to <code>dump</code>. Otherwise <code>restore</code> may be confused.</p>
<dd>This option can be used when restoring from local or remote tapes (see above) or from local or remote files.</p>
<dt><code>-s</code><i> fileno</i></p>
<dd>Read from the specified <i>fileno</i> on a multi-file tape. File numbering starts at 1.</p>
<dt><code>-T</code><i> directory</i></p>
<dd>The <code>-T</code> flag allows the user to specify a directory to use for the storage of temporary files. The default value is <i>/tmp</i>. This flag is most useful when restoring files after having booted from a floppy. There might be little or no space on the floppy filesystem, but another source of space might exist.</p>
<dt><code>-u</code></p>
<dd>When creating certain types of files, <code>restore</code> may generate a warning diagnostic if they already exist in the target directory. To prevent this, the <code>-u</code> (unlink) flag causes <code>restore</code> to remove old entries before attempting to create new ones.</p>
<dt><code>-v</code></p>
<dd>Normally <code>restore</code> does its work silently. The <code>-v</code> (verbose) flag causes it to type the name of each file it treats preceded by its file type.</p>
<dt><code>-V</code></p>
<dd>Enables reading multi-volume non-tape mediums like CDROMs.</p>
<dt><code>-X</code><i> filelist</i></p>
<dd>Read list of files to be listed or extracted from the text file <i>filelist</i> in addition to those specified on the command line. This can be used in conjunction with the <code>-t</code> or <code>-x</code> commands. The file <i>filelist</i> should contain file names separated by newlines. <i>filelist</i> may be an ordinary file or <i>&#8211;</i> (the standard input).</p>
<dt><code>-y</code></p>
<dd>Do not ask the user whether to abort the restore in the event of an error. Always try to skip over the bad block(s) and continue.</dl>
<p> (The 4.3BSD option syntax is implemented for backward compatibility but is not documented here.)</p>
<h2>Diagnostics</h2>
<p>Complains if it gets a read error. If <code>y</code> has been specified, or the user responds <code>y</code>, <code>restore</code> will attempt to continue the restore. </p>
<p> If a backup was made using more than one tape volume, <code>restore</code> will notify the user when it is time to mount the next volume. If the <code>-x</code> or <code>-i</code> flag has been specified, <code>restore</code> will also ask which volume the user wishes to mount. The fastest way to extract a few files is to start with the last volume, and work towards the first volume. </p>
<p> There are numerous consistency checks that can be listed by <code>restore</code>. Most checks are self-explanatory or can &#8220;never happen&#8221;. Common errors are given below:</p>
<dl>
<dt><i>Converting to new file system format</i></p>
<dd>A dump tape created from the old file system has been loaded. It is automatically converted to the new file system format.</p>
<dt><i>&lt;filename&gt;: not found on tape</i></p>
<dd>The specified file name was listed in the tape directory, but was not found on the tape. This is caused by tape read errors while looking for the file, and from using a dump tape created on an active file system.</p>
<dt><i>expected next file &lt;inumber&gt;, got &lt;inumber&gt;</i></p>
<dd>A file that was not listed in the directory showed up. This can occur when using a dump created on an active file system.</p>
<dt><i>Incremental dump too low</i></p>
<dd>When doing an incremental restore, a dump that was written before the previous incremental dump, or that has too low an incremental level has been loaded.</p>
<dt><i>Incremental dump too high</i></p>
<dd>When doing an incremental restore, a dump that does not begin its coverage where the previous incremental dump left off, or that has too high an incremental level has been loaded.</p>
<dt><i>Tape read error while restoring &lt;filename&gt;</i></p>
<dd>
<dt><i>Tape read error while skipping over inode &lt;inumber&gt;</i></p>
<dd>
<dt><i>Tape read error while trying to resynchronize</i></p>
<dd>A tape (or other media) read error has occurred. If a file name is specified, its contents are probably partially wrong. If an inode is being skipped or the tape is trying to resynchronize, no extracted files have been corrupted, though files may not be found on the tape.</p>
<dt><i>resync restore, skipped &lt;num&gt; blocks</i></p>
<dd>After a dump read error, <code>restore</code> may have to resynchronize itself. This message lists the number of blocks that were skipped over.</dl>
<h2>Exit Status</h2>
<p><code>Restore</code> exits with zero status on success. Tape errors are indicated with an exit code of 1. </p>
<p> When doing a comparison of files from a dump, an exit code of 2 indicates that some files were modified or deleted since the dump was made.</p>
<h2>Environment</h2>
<p>If the following environment variable exists it will be utilized by <code>restore</code>:</p>
<dl>
<dt><code>TAPE</code></p>
<dd>If no <code>-f</code> option was specified, <code>restore</code> will use the device specified via <code>TAPE</code> as the dump device. <code>TAPE</code> may be of the form <i>tapename</i>, <i>host:tapename</i> or <i>user [at] host:tapename</i>.</p>
<dt><code>TMPDIR</code></p>
<dd>The directory given in <code>TMPDIR</code> will be used instead of <i>/tmp</i> to store temporary files.</p>
<dt><code>RMT</code></p>
<dd>The environment variable <code>RMT</code> will be used to determine the pathname of the remote <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8) program.</p>
<dt><code>RSH</code></p>
<dd><code>Restore</code> uses the contents of this variable to determine the name of the remote shell command to use when doing a network restore (rsh, ssh etc.). If this variable is not set, <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3) will be used, but only root will be able to do a network restore.</dl>
<h2>Files</h2>
<dl>
<dt><i>/dev/st0</i></p>
<dd>the default tape drive</p>
<dt><i>/tmp/rstdir*</i></p>
<dd>file containing directories on the tape</p>
<dt><i>/tmp/rstmode*</i></p>
<dd>owner, mode, and time stamps for directories</p>
<dt><i>./restoresymtable</i></p>
<dd>information passed between incremental restores</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dump/">dump</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8)</p>
<h2>Bugs</h2>
<p><code>Restore</code> can get confused when doing incremental restores from dumps that were made on active file systems. </p>
<p> A level 0 dump must be done after a full restore. Because <code>restore</code> runs in user code, it has no control over inode allocation; thus a full dump must be done to get a new set of directories reflecting the new inode numbering, even though the content of the files is unchanged. </p>
<p> The temporary files <i>/tmp/rstdir*</i> and <i>/tmp/rstmode*</i> are generated with a unique name based on the date of the dump and the process ID (see <code><a href="/docs/linux/man/3-mktemp/">mktemp</a></code>(3)<code>),</code> except when <code>-r</code> or <code>-R</code> is used. Because <code>-R</code> allows you to restart a <code>-r</code> operation that may have been interrupted, the temporary files should be the same across different processes. In all other cases, the files are unique because it is possible to have two different dumps started at the same time, and separate operations shouldn&#8217;t conflict with each other. </p>
<p> To do a network restore, you have to run <code>restore</code> as root or use a remote shell replacement (see <code>RSH</code> variable). This is due to the previous security history of <code>dump </code> and <code>restore</code>. ( <code>restore</code> is written to be setuid root, but we are not certain all bugs are gone from the code &#8211; run setuid at your own risk.) </p>
<p> At the end of restores in <code>-i</code> or <code>-x</code> modes (unless <code>-o</code> option is in use), <code>restore</code> will ask the operator whether to set the permissions on the current directory. If the operator confirms this action, the permissions on the directory from where <code>restore</code> was launched will be replaced by the permissions on the dumped root inode. Although this behaviour is not really a bug, it has proven itself to be confusing for many users, so it is recommended to answer &#8216;no&#8217;, unless you&#8217;re performing a full restore and you do want to restore the permissions on &#8216;/&#8217;. </p>
<p> It should be underlined that because it runs in user code, <code>restore</code> , when run with the <code>-C</code> option, sees the files as the kernel presents them, whereas <code>dump</code> sees all the files on a given filesystem. In particular, this can cause some confusion when comparing a dumped filesystem a part of which is hidden by a filesystem mounted on top of it.</p>
<h2>Author</h2>
<p>The <code>dump/restore</code> backup suite was ported to Linux&#8217;s Second Extended File System by Remy Card &lt;card [at] Linux.EU.Org&gt;. He maintained the initial versions of <code>dump</code> (up and including 0.4b4, released in January 1997). </p>
<p> Starting with 0.4b5, the new maintainer is Stelian Pop &lt;stelian [at] popies.net&gt;.</p>
<h2>Availability</h2>
<p>The <code>dump/restore</code> backup suite is available from &lt;<a rel="nofollow" href="http://dump.sourceforge.net">http://dump.sourceforge.net</a>&gt;</p>
<h2>History</h2>
<p>The <code>restore</code> command appeared in 4.2BSD.</p>
