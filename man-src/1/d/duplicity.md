---
title: "duplicity(1)"
name: "duplicity"
section: "1"
letter: "d"
url: "/docs/linux/man/1-duplicity/"
description: "duplicity – Encrypted incremental backup to local or remote storage."
---

<h2 class="name">NAME</h2>
<p> duplicity &#8211; Encrypted incremental backup to local or remote storage.</p>
<h2>SYNOPSIS</h2>
<p> For detailed descriptions for each command see chapter <code>ACTIONS</code>. </p>
<p> <code>duplicity [full|incremental]</code> <i>[options]</i> source_directory target_url </p>
<p> <code>duplicity verify</code> <i>[options] [&#8211;compare-data] [&#8211;file-to-restore &lt;relpath&gt;] [&#8211;time time]</i> source_url target_directory </p>
<p> <code>duplicity collection-status</code> <i>[options] [&#8211;file-changed &lt;relpath&gt;]</i> target_url </p>
<p> <code>duplicity list-current-files</code> <i>[options] [&#8211;time time]</i> target_url </p>
<p> <code>duplicity [restore]</code> <i>[options] [&#8211;file-to-restore &lt;relpath&gt;] [&#8211;time time]</i> source_url target_directory </p>
<p> <code>duplicity remove-older-than &lt;time&gt;</code> <i>[options] [&#8211;force]</i> target_url </p>
<p> <code>duplicity remove-all-but-n-full &lt;count&gt;</code> <i>[options] [&#8211;force]</i> target_url </p>
<p> <code>duplicity remove-all-inc-of-but-n-full &lt;count&gt;</code> <i>[options] [&#8211;force]</i> target_url </p>
<p> <code>duplicity cleanup</code> <i>[options] [&#8211;force]</i> target_url </p>
<p> <code>duplicity replicate</code> <i>[options] [&#8211;time time]</i> source_url target_url </p>
<h2>DESCRIPTION</h2>
<p> Duplicity incrementally backs up files and folders into tar-format volumes encrypted with GnuPG and places them to a remote (or local) storage backend. See chapter <code>URL FORMAT</code> for a list of all supported backends and how to address them. Because duplicity uses librsync, incremental backups are space efficient and only record the parts of files that have changed since the last backup. Currently duplicity supports deleted files, full Unix permissions, uid/gid, directories, symbolic links, fifos, etc., but not hard links. </p>
<p> If you are backing up the root directory /, remember to &#8211;exclude /proc, or else duplicity will probably crash on the weird stuff in there. </p>
<h2>EXAMPLES</h2>
<p> Here is an example of a backup, using sftp to back up /home/me to some_dir on the other.host machine: </p>
<dl>
<dt>
<dd> duplicity /home/me <a href="sftp://uid@other.host/some_dir">sftp://uid@other.host/some_dir</a> </p>
</dl>
<p> If the above is run repeatedly, the first will be a full backup, and subsequent ones will be incremental. To force a full backup, use the <i>full</i> action: </p>
<dl>
<dt>
<dd> duplicity full /home/me <a href="sftp://uid@other.host/some_dir">sftp://uid@other.host/some_dir</a> </p>
</dl>
<p> or enforcing a full every other time via <i>&#8211;full-if-older-than &lt;time&gt;</i> , e.g. a full every month: </p>
<dl>
<dt>
<dd> duplicity &#8211;full-if-older-than 1M /home/me <a href="sftp://uid@other.host/some_dir">sftp://uid@other.host/some_dir</a> </p>
</dl>
<p> Now suppose we accidentally delete /home/me and want to restore it the way it was at the time of last backup: </p>
<dl>
<dt>
<dd> duplicity <a href="sftp://uid@other.host/some_dir">sftp://uid@other.host/some_dir</a> /home/me </p>
</dl>
<p> Duplicity enters restore mode because the URL comes before the local directory. If we wanted to restore just the file &quot;Mail/article&quot; in /home/me as it was three days ago into /home/me/restored_file: </p>
<dl>
<dt>
<dd> duplicity -t 3D &#8211;file-to-restore Mail/article <a href="sftp://uid@other.host/some_dir">sftp://uid@other.host/some_dir</a> /home/me/restored_file </p>
</dl>
<p> The following command compares the latest backup with the current files: </p>
<dl>
<dt>
<dd> duplicity verify <a href="sftp://uid@other.host/some_dir">sftp://uid@other.host/some_dir</a> /home/me </p>
</dl>
<p> Finally, duplicity recognizes several include/exclude options. For instance, the following will backup the root directory, but exclude /mnt, /tmp, and /proc: </p>
<dl>
<dt>
<dd> duplicity &#8211;exclude /mnt &#8211;exclude /tmp &#8211;exclude /proc / file:///usr/local/backup </p>
</dl>
<p> Note that in this case the destination is the local directory /usr/local/backup. The following will backup only the /home and /etc directories under root: </p>
<dl>
<dt>
<dd> duplicity &#8211;include /home &#8211;include /etc &#8211;exclude &#8216;**&#8217; / file:///usr/local/backup </p>
</dl>
<p> Duplicity can also access a repository via ftp. If a user name is given, the environment variable FTP_PASSWORD is read to determine the password: </p>
<dl>
<dt>
<dd> FTP_PASSWORD=mypassword duplicity /local/dir <a href="ftp://user@other.host/some_dir">ftp://user@other.host/some_dir</a> </p>
</dl>
<h2>ACTIONS</h2>
<p> Duplicity knows action commands, which can be finetuned with options.<br />
 The actions for backup (full,incr) and restoration (restore) can as well be left out as duplicity detects in what mode it should switch to by the order of target URL and local folder. If the target URL comes before the local folder a restore is in order, is the local folder before target URL then this folder is about to be backed up to the target URL.<br />
 If a backup is in order and old signatures can be found duplicity automatically performs an incremental backup. </p>
<p> <code>Note:</code> The following explanations explain some but <code>not</code> all options that can be used in connection with that action command. Consult the OPTIONS section for more detailed informations. </p>
<dl>
<dt><code>full </code><i>&lt;folder&gt; &lt;url&gt;</i></p>
<dd> Perform a full backup. A new backup chain is started even if signatures are available for an incremental backup. </p>
<dt><code>incr </code><i>&lt;folder&gt; &lt;url&gt;</i></p>
<dd> If this is requested an incremental backup will be performed. Duplicity will abort if no old signatures can be found. </p>
<dt><code>verify </code><i>[&#8211;compare-data] [&#8211;time &lt;time&gt;] [&#8211;file-to-restore &lt;rel_path&gt;] &lt;url&gt; &lt;local_path&gt;</i></p>
<dd> Verify tests the integrity of the backup archives at the remote location by downloading each file and checking both that it can restore the archive and that the restored file matches the signature of that file stored in the backup, i.e. compares the archived file with its hash value from archival time. Verify does not actually restore and will not overwrite any local files. Duplicity will exit with a non-zero error level if any files do not match the signature stored in the archive for that file. On verbosity level 4 or higher, it will log a message for each file that differs from the stored signature. Files must be downloaded to the local machine in order to compare them. Verify does not compare the backed-up version of the file to the current local copy of the files unless the &#8211;compare-data option is used (see below).<br />
 The <i>&#8211;file-to-restore</i> option restricts verify to that file or folder. The <i>&#8211;time</i> option allows to select a backup to verify. The <i>&#8211;compare-data</i> option enables data comparison (see below). </p>
<dt><code>collection-status </code><i>[&#8211;file-changed &lt;relpath&gt;]</i><code>&lt;url&gt;</code></p>
<dd> Summarize the status of the backup repository by printing the chains and sets found, and the number of volumes in each. </p>
<dt><code>list-current-files </code><i>[&#8211;time &lt;time&gt;] &lt;url&gt;</i></p>
<dd> Lists the files contained in the most current backup or backup at time. The information will be extracted from the signature files, not the archive data itself. Thus the whole archive does not have to be downloaded, but on the other hand if the archive has been deleted or corrupted, this command will not detect it. </p>
<dt><code>restore </code><i>[&#8211;file-to-restore &lt;relpath&gt;] [&#8211;time &lt;time&gt;] &lt;url&gt; &lt;target_folder&gt;</i></p>
<dd> You can restore the full monty or selected folders/files from a specific time. Use the relative path as it is printed by <code>list-current-files</code>. Usually not needed as duplicity enters restore mode when it detects that the URL comes before the local folder. </p>
<dt><code>remove-older-than </code><i>&lt;time&gt; [&#8211;force] &lt;url&gt;</i></p>
<dd> Delete all backup sets older than the given time. Old backup sets will not be deleted if backup sets newer than <i>time</i> depend on them. See the <code>TIME FORMATS</code> section for more information. Note, this action cannot be combined with backup or other actions, such as cleanup. Note also that <i>&#8211;force</i> will be needed to delete the files instead of just listing them. </p>
<dt><code>remove-all-but-n-full </code><i>&lt;count&gt; [&#8211;force] &lt;url&gt;</i></p>
<dd> Delete all backups sets that are older than the count:th last full backup (in other words, keep the last <i>count</i> full backups and associated incremental sets). <i>count</i> must be larger than zero. A value of 1 means that only the single most recent backup chain will be kept. Note that <i>&#8211;force</i> will be needed to delete the files instead of just listing them. </p>
<dt><code>remove-all-inc-of-but-n-full </code><i>&lt;count&gt; [&#8211;force] &lt;url&gt;</i></p>
<dd> Delete incremental sets of all backups sets that are older than the count:th last full backup (in other words, keep only old full backups and not their increments). <i>count</i> must be larger than zero. A value of 1 means that only the single most recent backup chain will be kept intact. Note that <i>&#8211;force</i> will be needed to delete the files instead of just listing them. </p>
<dt><code>cleanup </code><i>[&#8211;force] &lt;url&gt;</i></p>
<dd> Delete the extraneous duplicity files on the given backend. Non-duplicity files, or files in complete data sets will not be deleted. This should only be necessary after a duplicity session fails or is aborted prematurely. Note that <i>&#8211;force</i> will be needed to delete the files instead of just listing them. </p>
<dt><code>replicate </code><i>[&#8211;time time] &lt;source_url&gt; &lt;target_url&gt;</i></p>
<dd> Replicate backup sets from source to target backend. Files will be (re)-encrypted and (re)-compressed depending on normal backend options. Signatures and volumes will not get recomputed, thus options like <code>&#8211;volsize</code> or <code>&#8211;max-blocksize</code> have no effect. When <i>&#8211;time time</i> is given, only backup sets older than time will be replicated. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;allow-source-mismatch</code></p>
<dd> Do not abort on attempts to use the same archive dir or remote backend to back up different directories. duplicity will tell you if you need this switch. </p>
<dt><code>&#8211;archive-dir </code><i>path</i></p>
<dd> The archive directory. <code>NOTE:</code> This option changed in 0.6.0. The archive directory is now necessary in order to manage persistence for current and future enhancements. As such, this option is now used only to change the location of the archive directory. The archive directory should <code>not</code> be deleted, or duplicity will have to recreate it from the remote repository (which may require decrypting the backup contents). </p>
<p> When backing up or restoring, this option specifies that the local archive directory is to be created in <i>path</i>. If the archive directory is not specified, the default will be to create the archive directory in <i>~/.cache/duplicity/</i>. </p>
<p> The archive directory can be shared between backups to multiple targets, because a subdirectory of the archive dir is used for individual backups (see <code>&#8211;name</code> ). </p>
<p> The combination of archive directory and backup name must be unique in order to separate the data of different backups. </p>
<p> The interaction between the <code>&#8211;archive-dir</code> and the <code>&#8211;name</code> options allows for four possible combinations for the location of the archive dir: </p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> neither specified (default)<br />
&nbsp;~/.cache/duplicity/<i>hash-of-url</i></p>
<dt>2.</p>
<dd> &#8211;archive-dir=/arch, no &#8211;name<br />
&nbsp;/arch/<i>hash-of-url</i></p>
<dt>3.</p>
<dd> no &#8211;archive-dir, &#8211;name=foo<br />
&nbsp;~/.cache/duplicity/foo</p>
<dt>4.</p>
<dd> &#8211;archive-dir=/arch, &#8211;name=foo<br />
&nbsp;/arch/foo</dl>
</dl>
<dt><code>&#8211;asynchronous-upload </code></p>
<dd> (EXPERIMENTAL) Perform file uploads asynchronously in the background, with respect to volume creation. This means that duplicity can upload a volume while, at the same time, preparing the next volume for upload. The intended end-result is a faster backup, because the local CPU and your bandwidth can be more consistently utilized. Use of this option implies additional need for disk space in the temporary storage location; rather than needing to store only one volume at a time, enough storage space is required to store two volumes. </p>
<dt><code>&#8211;backend-retry-delay </code><i>number</i></p>
<dd> Specifies the number of seconds that duplicity waits after an error has occured before attempting to repeat the operation. </p>
<dt><code>&#8211;cf-backend </code><i>backend</i></p>
<dd> Allows the explicit selection of a cloudfiles backend. Defaults to <code>pyrax</code>. Alternatively you might choose <code>cloudfiles</code>. </p>
<dt><code>&#8211;compare-data</code></p>
<dd> Enable data comparison of regular files on action verify. This conducts a verify as described above to verify the integrity of the backup archives, but additionally compares restored files to those in target_directory. Duplicity will not replace any files in target_directory. Duplicity will exit with a non-zero error level if the files do not correctly verify or if any files from the archive differ from those in target_directory. On verbosity level 4 or higher, it will log a message for each file that differs from its equivalent in target_directory. </p>
<dt><code>&#8211;copy-links</code></p>
<dd> Resolve symlinks during backup. Enabling this will resolve &amp; back up the symlink&#8217;s file/folder data instead of the symlink itself, potentially increasing the size of the backup. </p>
<dt><code>&#8211;dry-run </code></p>
<dd> Calculate what would be done, but do not perform any backend actions </p>
<dt><code>&#8211;encrypt-key </code><i>key-id</i></p>
<dd> When backing up, encrypt to the given public key, instead of using symmetric (traditional) encryption. Can be specified multiple times. The key-id can be given in any of the formats supported by GnuPG; see <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), section &quot;HOW TO SPECIFY A USER ID&quot; for details. </p>
<dt><code>&#8211;encrypt-secret-keyring </code><i>filename</i></p>
<dd> This option can only be used with <code>&#8211;encrypt-key</code>, and changes the path to the secret keyring for the encrypt key to <i>filename</i> This keyring is not used when creating a backup. If not specified, the default secret keyring is used which is usually located at .gnupg/secring.gpg </p>
<dt><code>&#8211;encrypt-sign-key </code><i>key-id</i></p>
<dd> Convenience parameter. Same as <code>&#8211;encrypt-key</code> <i>key-id</i> <code>&#8211;sign-key</code> <i>key-id</i>. </p>
<dt><code>&#8211;exclude </code><i>shell_pattern</i></p>
<dd> Exclude the file or files matched by <i>shell_pattern</i>. If a directory is matched, then files under that directory will also be matched. See the <code>FILE SELECTION</code> section for more information. </p>
<dt><code>&#8211;exclude-device-files</code></p>
<dd> Exclude all device files. This can be useful for security/permissions reasons or if duplicity is not handling device files correctly. </p>
<dt><code>&#8211;exclude-filelist </code><i>filename</i></p>
<dd> Excludes the files listed in <i>filename,</i> with each line of the filelist interpreted according to the same rules as <code>&#8211;include</code> and <code>&#8211;exclude.</code> See the <code>FILE SELECTION</code> section for more information. </p>
<dt><code>&#8211;exclude-if-present </code>filename</p>
<dd> Exclude directories if filename is present. Allows the user to specify folders that they do not wish to backup by adding a specified file (e.g. &quot;.nobackup&quot;) instead of maintaining a comprehensive exclude/include list. </p>
<dt><code>&#8211;exclude-older-than </code>time</p>
<dd> Exclude any files whose modification date is earlier than the specified <i>time</i>. This can be used to produce a partial backup that contains only recently changed files. See the <code>TIME FORMATS</code> section for more information. </p>
<dt><code>&#8211;exclude-other-filesystems</code></p>
<dd> Exclude files on file systems (identified by device number) other than the file system the root of the source directory is on. </p>
<dt><code>&#8211;exclude-regexp </code><i>regexp</i></p>
<dd> Exclude files matching the given regexp. Unlike the <code>&#8211;exclude</code> option, this option does not match files in a directory it matches. See the <code>FILE SELECTION</code> section for more information. </p>
<dt><code>&#8211;file-prefix, &#8211;file-prefix-manifest, &#8211;file-prefix-archive, &#8211;file-prefix-signature</code></p>
<dd> Adds a prefix to all files, manifest files, archive files, and/or signature files. </p>
<p> The same set of prefixes must be passed in on backup and restore. </p>
<p> If both global and type-specific prefixes are set, global prefix will go before type-specific prefixes. </p>
<p> See also <code>A NOTE ON FILENAME PREFIXES</code> </p>
<dt><code>&#8211;file-to-restore </code><i>path</i></p>
<dd> This option may be given in restore mode, causing only <i>path</i> to be restored instead of the entire contents of the backup archive. <i>path</i> should be given relative to the root of the directory backed up. </p>
<dt><code>&#8211;full-if-older-than </code><i>time</i></p>
<dd> Perform a full backup if an incremental backup is requested, but the latest full backup in the collection is older than the given <i>time</i>. See the <code>TIME FORMATS</code> section for more information. </p>
<dt><code>&#8211;force</code></p>
<dd> Proceed even if data loss might result. Duplicity will let the user know when this option is required. </p>
<dt><code>&#8211;ftp-passive</code></p>
<dd> Use passive (PASV) data connections. The default is to use passive, but to fallback to regular if the passive connection fails or times out. </p>
<dt><code>&#8211;ftp-regular</code></p>
<dd> Use regular (PORT) data connections. </p>
<dt><code>&#8211;gio</code></p>
<dd> Use the GIO backend and interpret any URLs as GIO would. </p>
<dt><code>&#8211;hidden-encrypt-key </code><i>key-id</i></p>
<dd> Same as <code>&#8211;encrypt-key</code>, but it hides user&#8217;s key id from encrypted file. It uses the gpg&#8217;s <code>&#8211;hidden-recipient</code> command to obfuscate the owner of the backup. On restore, gpg will automatically try all available secret keys in order to decrypt the backup. See <a href="/docs/linux/man/1-gpg/">gpg</a>(1) for more details. </p>
<dt><code>&#8211;ignore-errors</code></p>
<dd> Try to ignore certain errors if they happen. This option is only intended to allow the restoration of a backup in the face of certain problems that would otherwise cause the backup to fail. It is not ever recommended to use this option unless you have a situation where you are trying to restore from backup and it is failing because of an issue which you want duplicity to ignore. Even then, depending on the issue, this option may not have an effect. </p>
<p> Please note that while ignored errors will be logged, there will be no summary at the end of the operation to tell you what was ignored, if anything. If this is used for emergency restoration of data, it is recommended that you run the backup in such a way that you can revisit the backup log (look for lines containing the string IGNORED_ERROR). </p>
<p> If you ever have to use this option for reasons that are not understood or understood but not your own responsibility, please contact duplicity maintainers. The need to use this option under production circumstances would normally be considered a bug. </p>
<dt><code>&#8211;imap-full-address </code><i>email_address</i></p>
<dd> The full email address of the user name when logging into an imap server. If not supplied just the user name part of the email address is used. </p>
<dt><code>&#8211;imap-mailbox </code><i>option</i></p>
<dd> Allows you to specify a different mailbox. The default is &quot;INBOX&quot;. Other languages may require a different mailbox than the default. </p>
<dt><code>&#8211;gpg-binary </code><i>file_path</i></p>
<dd> Allows you to force duplicity to use <i>file_path</i> as gpg command line binary. Can be an absolute or relative file path or a file name. Default value is &#8216;gpg&#8217;. The binary will be localized via the PATH environment variable. </p>
<dt><code>&#8211;gpg-options </code><i>options</i></p>
<dd> Allows you to pass options to gpg encryption. The <i>options</i> list should be of the form &quot;&#8211;opt1 &#8211;opt2=parm&quot; where the string is quoted and the only spaces allowed are between options. </p>
<dt><code>&#8211;include </code><i>shell_pattern</i></p>
<dd> Similar to <code>&#8211;exclude</code> but include matched files instead. Unlike <code>&#8211;exclude</code>, this option will also match parent directories of matched files (although not necessarily their contents). See the <code>FILE SELECTION</code> section for more information. </p>
<dt><code>&#8211;include-filelist </code><i>filename</i></p>
<dd> Like <code>&#8211;exclude-filelist</code>, but include the listed files instead. See the <code>FILE SELECTION</code> section for more information. </p>
<dt><code>&#8211;include-regexp </code><i>regexp</i></p>
<dd> Include files matching the regular expression <i>regexp</i>. Only files explicitly matched by <i>regexp</i> will be included by this option. See the <code>FILE SELECTION</code> section for more information. </p>
<dt><code>&#8211;log-fd </code><i>number</i></p>
<dd> Write specially-formatted versions of output messages to the specified file descriptor. The format used is designed to be easily consumable by other programs. </p>
<dt><code>&#8211;log-file </code><i>filename</i></p>
<dd> Write specially-formatted versions of output messages to the specified file. The format used is designed to be easily consumable by other programs. </p>
<dt><code>&#8211;max-blocksize </code><i>number</i></p>
<dd> determines the number of the blocks examined for changes during the diff process. For files &lt; 1MB the blocksize is a constant of 512. For files over 1MB the size is given by: </p>
<p> file_blocksize = int((file_len / (2000 * 512)) * 512)<br />
 return min(file_blocksize, globals.max_blocksize) </p>
<p> where globals.max_blocksize defaults to 2048. If you specify a larger max_blocksize, your difftar files will be larger, but your sigtar files will be smaller. If you specify a smaller max_blocksize, the reverse occurs. The &#8211;max-blocksize option should be in multiples of 512. </p>
<dt><code>&#8211;name </code><i>symbolicname</i></p>
<dd> Set the symbolic name of the backup being operated on. The intent is to use a separate name for each logically distinct backup. For example, someone may use &quot;home_daily_s3&quot; for the daily backup of a home directory to Amazon S3. The structure of the name is up to the user, it is only important that the names be distinct. The symbolic name is currently only used to affect the expansion of <code>&#8211;archive-dir</code> , but may be used for additional features in the future. Users running more than one distinct backup are encouraged to use this option. </p>
<p> If not specified, the default value is a hash of the backend URL. </p>
<dt><code>&#8211;no-compression</code></p>
<dd> Do not use GZip to compress files on remote system. </p>
<dt><code>&#8211;no-encryption</code></p>
<dd> Do not use GnuPG to encrypt files on remote system. </p>
<dt><code>&#8211;no-print-statistics</code></p>
<dd> By default duplicity will print statistics about the current session after a successful backup. This switch disables that behavior. </p>
<dt><code>&#8211;null-separator</code></p>
<dd> Use nulls (
