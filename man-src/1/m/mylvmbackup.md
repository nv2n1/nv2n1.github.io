---
title: "mylvmbackup(1)"
name: "mylvmbackup"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mylvmbackup/"
description: "mylvmbackup – a utility for creating MySQL backups using LVM snapshots"
---

<h2 class="name">NAME</h2>
<p> mylvmbackup &#8211; a utility for creating MySQL backups using LVM snapshots </p>
<h2>SYNOPSIS</h2>
<p> mylvmbackup [<font SIZE="-1">OPTIONS</font>]</p>
<h2>DESCRIPTION</h2>
<p> <i>mylvmbackup</i> is a tool for quickly creating full physical backups of a MySQL server&#8217;s data files. To perform a backup, <i>mylvmbackup</i> obtains a read lock on all tables and flushes all server caches to disk, makes an <font SIZE="-1">LVM</font> snapshot of the volume containing the MySQL data directory, and unlocks the tables again. The snapshot process takes only a small amount of time. When it is done, the server can continue normal operations, while the actual file backup proceeds. </p>
<p> The <font SIZE="-1">LVM</font> snapshot is mounted to a temporary directory and all data is backed up using the <i>tar</i> program by default. The archive files are created using names in the form of <i>backup-YYYYMMDD_hhmmss_mysql.tar.gz</i>, where <i></i><font SIZE="-1"><i>YYYY</i></font><i></i>, <i></i><font SIZE="-1"><i>MM</i></font><i></i>, <i></i><font SIZE="-1"><i>DD</i></font><i></i>, <i>hh</i>, <i>mm</i> and <i>ss</i> represent the year, month, day, hour, minute, and second of the time at which the backup occurred. The default prefix <i>backup</i>, date format and file suffix may be modified. The use of timestamped archive names allows you to run <i>mylvmbackup</i> many times without risking to overwrite old archives. It is possible to preserve only a defined number of last backups, to avoid running out of disk space. </p>
<p> Alternatively, instead of <i>tar</i>, you can use <i>rsync</i>, <i>rsnap</i> or <i>zbackup</i> to perform the archiving. </p>
<p> The <i>rsync</i> backup can perform both local backups as well as backing up to a remote server using rsyncd or rsync via <font SIZE="-1">SSH.</font> </p>
<p> <i>rsnap</i> is a wrapper around <i>rsync</i> to automatically maintain and rotate a given number of last backups (7 by default). It utilizes hard links to link to unchanged files for saving disk space. </p>
<p> <i>zbackup</i> is a globally-deduplicating backup tool. Feed a large .tar into it, and it will store duplicate regions of it only once, then compress and optionally encrypt the result. Feed another .tar file, and it will also re-use any data found in any previous backups. This way only new changes are stored, and as long as the files are not very different, the amount of storage required is very low. Any of the backup files stored previously can be read back in full at any time. </p>
<p> Moreover, a backup type <i>none</i> is provided for cases where the user wants to use <i>mylvmbackup</i> only for creating the snapshots and intends to perform the actual backup by using the appropriate hooks. (Or for cases where the snapshot itself is considered to be the backup). </p>
<p> <i>mylvmbackup</i> also provides several methods for logging and reporting the progress and success of a backup run. The log messages can either be printed to the console (<font SIZE="-1">STDOUT</font>) or logged via <i>syslog</i>. </p>
<p> Additionally, a report can be sent to you via email, and you can receive notifications about failures or successes via <font SIZE="-1">SNMP.</font></p>
<h2>GENERAL HINTS</h2>
<p> It is required to run <i>mylvmbackup</i> on the same host where the MySQL server runs. If your MySQL daemon is not listening on localhost or using the default socket location, you must specify <i>&#8211;host</i> or <i>&#8211;socket</i>. Even though <i>mylvmbackup</i> communicates with the server through a normal client connection to obtain the read lock and flush data, it performs the actual backup by accessing the file system directly. It is also a requirement that the MySQL server&#8217;s data directory resides on an <font SIZE="-1">LVM</font> volume. (It is, however, a good idea to do the <font SIZE="-1">LVM</font> backup to a different partition than the one where the data directory resides. Otherwise, there is a good chance that <font SIZE="-1">LVM</font> will run out of undo space for <font SIZE="-1">LVM</font> snapshot maintenance and the backup will fail.) </p>
<p> The user who invokes <i>mylvmbackup</i> must have sufficient filesystem permissions to create the <font SIZE="-1">LVM</font> snapshot and mount it. This includes read/write access to the backup directory. </p>
<p> If you plan to back up InnoDB tables using <font SIZE="-1">LVM</font> snapshots, be advised that it is not sufficient to lock the tables and issue the <i></i><font SIZE="-1"><i>FLUSH TABLES</i></font><i></i> command to get the table files into a consistent state. When starting the MySQL server from these restored files, InnoDB will detect these tables as being in an inconsistent state and will perform a log recovery run before the tables can be accessed again. As this can potentially take some time (which you may not want to spend after restoring a server and trying to get it back on its feet as fast as possible), consider using the option <i>&#8211;innodb_recover</i>, which will perform the recovery operation on the backup snapshot prior to archiving it. </p>
<p> The recovery operation is performed by spawning a second mysqld instance that uses the snapshot volume as the data directory. Note that this functionality currently assumes a default InnoDB configuration in which all InnoDB table spaces and log files are stored inside of the data directory &#8211; it does not work properly if you use options like <i>&#8211;innodb-data-home-dir</i>, <i>&#8211;innodb-data-file-path</i> or <i>&#8211;innodb-log-group-home-dir</i> that modify the default file layout for InnoDB tables. </p>
<p> If you use InnoDB tables exclusively, you may also want to consider to include the option <i>&#8211;skip_flush_tables</i>, to avoid the probably time-consuming and in this case unnecessary flushing of buffers. But don&#8217;t enable this option when MyISAM tables are involved!</p>
<h2>HOOKS</h2>
<p> It is possible to run arbitrary external programs or scripts (hooks) at various stages of the backup process, to perform additional actions as part of the backup process. </p>
<p> These scripts or symbolic links to executables should be placed in the directory that the <i>hooksdir</i> configuration option points to (<i>/usr/share/mylvmbackup</i> by default). They should return zero upon successful completion, any non-zero return value will be considered a failure which will be logged. </p>
<p> Hook scripts can also be implemented as Perl modules. The module must be named <i>hookname.pm</i> and must be a package of type <i>hookname</i>. The module must implement <i>execute()</i> which is called by <i>mylvmbackup</i> to initiate the hook. It must return boolean true/false (1 or 0) on success/failure. <i>execute()</i> will be passed 2 parameters. The first parameter is a <i>clone()</i> of the global database handle <tt>$dbh</tt>. This will allow hook scripts to interact with the database using the established connection. The second parameter is a string containing any messages passed to the <i>run_hook()</i> function. The module must also implement <i>errmsg()</i> which will return a string error message to be sent to <i>log_msg()</i>. This will be called by <i>mylvmbackup</i> when <i>execute()</i> returns false/0. </p>
<p> The names of the scripts or symbolic links reflect the stage in which the hook will be called. Currently, the following stages exist:</p>
<dl>
<dt><code>preconnect</code></p>
<dd> before a connection to the database server is established</p>
<dt><code>preflush</code></p>
<dd> before calling <font SIZE="-1">FLUSH TABLES</font></p>
<dt><code>presnapshot</code></p>
<dd> before the file system snapshot is created</p>
<dt><code>preunlock</code></p>
<dd> before the database tables are unlocked again</p>
<dt><code>predisconnect</code></p>
<dd> before the connection to the database server is released</p>
<dt><code>premount</code></p>
<dd> before the snapshot volume is mounted</p>
<dt><code>prebackup</code></p>
<dd> before the snapshot backup will be performed</p>
<dt><code>backupsuccess</code></p>
<dd> after a successful backup</p>
<dt><code>backupfailure</code></p>
<dd> after a failed backup</p>
<dt><code>logerr</code></p>
<dd> when an error is logged</p>
<dt><code>precleanup</code></p>
<dd> before the snapshot is unmounted and discarded</dl>
<p> These hooks are optional and will only be called if a file for the particular stage exists and is executable. Note that hooks implemented as Perl modules (<i>hookname.pm</i>) have priority over &#8220;plain&#8221; hook scripts (<i>hookname</i>), if both exist, only the first one will be used. The execution of all hooks can be suppressed by passing the <i>&#8211;skip_hooks</i> option or by setting the <i>skip_hooks</i> configuration option to <i>1</i>;</p>
<h2>OPTIONS</h2>
<p> <i>mylvmbackup</i> supports the following command line options. The same options can also be defined in the <i>/etc/mylvmbackup.conf</i> configuration file (omitting the leading dashes, of course). A sample configuration file is included in the distribution.</p>
<dl>
<dt><code>&#8211;action=string</code></p>
<dd> Selects the mode of action. Possible values are <i>backup</i> and <i>purge</i>. </p>
<p> When this option is omitted, the <i>backup</i> action is assumed by default, which performs the actual backup creation. Older backup files are preserved. </p>
<p> The <i>purge</i> action can be used to remove older tar or local rsync backups from the backup directory, except for the a configurable number of most recent backups, defined by the <i>backupretention</i> option. The backup creation process is skipped in this case. </p>
<p> Note that this option erases <code>all</code> files contained in this directory that match the criterion of being older than the last n backup files (with the exception of hidden (dot) files!</p>
<dt><code>&#8211;user=string</code></p>
<dd> Specifies the username to use for connecting to the MySQL server. The default is <i>root</i>.</p>
<dt><code>&#8211;password=string</code></p>
<dd> Specifies the password to use for connecting to the MySQL server. The default is the empty string (no password). Alternatively, you can set the password by defining the environment variable <i></i><font SIZE="-1"><i>MYSQL_PWD</i></font><i></i> prior to starting the script. Note however that this method is considered to be highly insecure, as it&#8217;s possible for other users to obtain the password by examining the environment variables of the running process. See the MySQL Reference manual for more details on password security.</p>
<dt><code>&#8211;host=string</code></p>
<dd> Specifies the host name to use for connecting to the MySQL server. Note that <i>mylvmbackup</i> needs to be run on the same system that the MySQL server to be backed up runs on &#8211; do not enter a remote host&#8217;s host name or <font SIZE="-1">IP</font> address here! A non-empty value for <i>host</i> other than <i>localhost</i> overrides any given <i>socket</i> path value. The default is the empty string.</p>
<dt><code>&#8211;port=number</code></p>
<dd> Specifies the <font SIZE="-1">TCP</font> port number to use for connecting to the MySQL server. This value is only honoured, if <i>host</i> is provided as well and is not equal to <i>localhost</i>. The default is the empty string.</p>
<dt><code>&#8211;socket=string</code></p>
<dd> Specifies the path to the local socket file, if it is not located at the default location. The default is the empty string.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Suppresses logging of informal messages. Warnings and errors will still be printed or logged (depending on the selected logging mechanism). The default is verbose logging.</p>
<dt><code>&#8211;innodb_recover</code></p>
<dd> Run InnoDB recovery on the writable snapshot prior to performing the backup.</p>
<dt><code>&#8211;recoveryopts</code></p>
<dd> Additional values to pass to the startup options of the separate MySQL instance that gets spawned to perform the InnoDB log recovery option. Depending on your MySQL Server version, you may have to modify these startup parameters. </p>
<p> The default is <i>&#8211;skip-networking &#8211;skip-grant &#8211;bootstrap &#8211;skip-syslog &#8211;skip-slave-start</i>.</p>
<dt><code>&#8211;skip_flush_tables</code></p>
<dd> Don&#8217;t issue a <i></i><font SIZE="-1"><i>FLUSH TABLES WITH READ LOCK</i></font><i></i> command before creating the snapshot. Only use this option when backing up InnoDB tables (as they don&#8217;t support this function anyway and will require recovery in any case). This option skips the (probably time consuming) flushing of buffers.</p>
<dt><code>&#8211;extra_flush_tables</code></p>
<dd> If your database performs a lot of writes, it may help to perform an extra initial <i></i><font SIZE="-1"><i>FLUSH TABLES</i></font><i></i> so that the <i>lvcreate</i> can finish within the interactivity timeout during the read-locked flush.</p>
<dt><code>&#8211;pidfile=string</code></p>
<dd> Specifies the full path and file name to the <font SIZE="-1">PID</font> file of the server instance that is spawned to perform the InnoDB recovery (see option <i>&#8211;innodb_recover</i>). Must be different from the <font SIZE="-1">PID</font> file that the actual running server uses. The default is <i>/var/tmp/mylvmbackup_recoverserver.pid</i></p>
<dt><code>&#8211;lvcreate=string</code></p>
<dd> Specifies the pathname for the <i>lvcreate</i> program. The default is <i>lvcreate</i>.</p>
<dt><code>&#8211;lvremove=string</code></p>
<dd> Specifies the pathname for the <i>lvremove</i> program. The default is <i>lvremove</i>.</p>
<dt><code>&#8211;lvs=string</code></p>
<dd> Specifies the pathname for the <i>lvs</i> program. The default is <i>lvs</i>.</p>
<dt><code>&#8211;mysqld_safe=string</code></p>
<dd> Specifies the pathname for the <i>mysqld_safe</i> program. The default is <i>mysqld_safe</i>. Only used to perform InnoDB recovery.</p>
<dt><code>&#8211;mycnf=string</code></p>
<dd> Specifies the name of a MySQL config file (e.g. <i>/etc/my.cnf</i>) or an entire config directory (e.g. <i>/etc/mysql</i>) to include in the backup. The default is <i>/etc/my.cnf</i>.</p>
<dt><code>&#8211;skip_mycnf</code></p>
<dd> Skip backing up the MySQL configuration. The default is to include a copy of the MySQL configuration in the backup.</p>
<dt><code>&#8211;hooksdir=string</code></p>
<dd> The location of external scripts or executable to be called during various stages of the backup. See the <font SIZE="-1">HOOKS</font> section in this manual page for more info. The default is <i>/usr/share/mylvmbackup</i>.</p>
<dt><code>&#8211;skip_hooks</code></p>
<dd> Skip invoking any external hooks during the backup.</p>
<dt><code>&#8211;vgname=string</code></p>
<dd> Specifies the volume group of the logical volume where the MySQL data directory is located. The default is <i>mysql</i>.</p>
<dt><code>&#8211;lvname=string</code></p>
<dd> Specifies the name of the logical volume where the MySQL data directory is located. The default is <i>data</i>.</p>
<dt><code>&#8211;backuplv=string</code></p>
<dd> Specifies the name used for the snapshot volume. If left empty, <code>_snapshot</code> will simply be appended to the original volume name (e.g. <i>data_snapshot</i>). </p>
<p> It is possible to use selected <i>timestr()</i> formatting sequences to create snapshot volume names which contain a dynamic date value. This can be useful if you use thin provisioned snapshots as the actual backup, by enabling the <i>keep_snapshot</i> option. </p>
<p> Currently, the following format strings are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>%Y</i></p>
<dd> 4-digit year (e.g. 2009)</p>
<dt><i>%m</i></p>
<dd> Month (01..12)</p>
<dt><i>%d</i></p>
<dd> Day of month, leading zero</p>
<dt><i>%h</i></p>
<dd> Month abbreviation,</p>
<dt><i>%H</i></p>
<dd> Hour, 24 hour clock, leading zero</p>
<dt><i>%M</i></p>
<dd> Minute, leading zero</p>
<dt><i>%S</i></p>
<dd> Seconds, leading zero</dl>
</dl>
<dl>
<dt>
<dd>
<p> Example: <i></i>$backuplv<i>=backup-%Y-%m-%d-%H-%M-%S</i> will expand to <i>backup-2013-06-07-14-08-45</i>.</dl>
<dt><code>&#8211;keep_snapshot</code></p>
<dd> If this option is given, <i>mylvmbackup</i> will not remove the snapshot before terminating. Note that keeping multiple <font SIZE="-1">LVM</font> snapshots open at the same time can reduce I/O performance and you will need to manually discard the snapshot before invoking <i>mylvmbackup</i> again.</p>
<dt><code>&#8211;keep_mount</code></p>
<dd> If this option is given, <i>mylvmbackup</i> will not remove the mounted partition before terminating. This option also implies <i>keep_snapshot=1</i>, as it would not be useful if the snapshot is removed. You need to manually unmount this directory before invoking <i>mylvmbackup</i> again.</p>
<dt><code>&#8211;thin</code></p>
<dd> If this option is given, <i>mylvmbackup</i> will expect that the <font SIZE="-1">LVM</font> volume is using thin provisioning and that the snapshot will use physical space from the existing thin pool. Any size specified with <i>lvsize</i> is ignored.</p>
<dt><code>&#8211;relpath=string</code></p>
<dd> Relative path on the logical volume to the MySQL data directory (no leading or trailing slash). Example: the logical volume is mounted on <i>/var/lib</i>, but the MySQL data directory is /var/lib/mysql. In this case, <i>relpath</i> should be set to <i>mysql</i>. The default is the empty string.</p>
<dt><code>&#8211;lvsize=string</code></p>
<dd> Specifies the size for the snapshot volume. The default is <i>5G</i> (5 gigabytes).</p>
<dt><code>&#8211;backuptype=string</code></p>
<dd> Specifies what type of backup to perform. The available options are <i>tar</i>, <i>rsync</i>, <i>rsnap</i>, <i>zbackup</i> and <i>none</i>. Note that using <i>zbackup</i> still requires a <i>tar</i> executable to prepare the backup archives.</p>
<dt><code>&#8211;backupretention=string</code></p>
<dd> Specifies how many previous backups (tar archives or rsync directories only) to keep in the backup directory when performing the <i>purge</i> action. The default is <i>0</i> (keep all backups). </p>
<p> Note that this feature only works on a local backup directory with a static directory name! If you use <i>timestr()</i> formatting sequences for the backup directory, the retention mode will not work. </p>
<p> The script looks at the last modification time (mtime) of each file and directory to determine which files will be removed. </p>
<p> Be advised that this operation deletes <code>all</code> files and directories in the backup directory that are older than the last n files (with the exception of hidden (dot) files!</p>
<dt><code>&#8211;prefix=string</code></p>
<dd> Prefix added to the backup file names. It is also appended to the name of the directory used to mount the snapshot volume. The default value is <i>backup</i>.</p>
<dt><code>&#8211;suffix=string</code></p>
<dd> Suffix added to the backup file names (after the time stamp). The default value is <i>_mysql</i>.</p>
<dt><code>&#8211;datefmt=string</code></p>
<dd> Format of the time stamp included in the backup file name. See the <i>Date::Format</i> perldoc page for a description of the format. The default value is <i></i>%Y<i>%m%d_%H%M%S</i>, which creates a time stamp like <i></i><font SIZE="-1"><i>YYYYMMDD_HHMMSS</i></font><i></i>, e.g. <i>20070531_112549</i> Can be empty as well, to suppress adding a time stamp (e.g. when using rsync to always sync into the same backup directory).</p>
<dt><code>&#8211;mountdir=string</code></p>
<dd> Path for mounting the snapshot volume to. The default value is <i>/var/tmp/mylvmbackup/mnt/</i>. If the directory does not exist, it will be created. </p>
<p> It is possible to use selected <i>timestr()</i> formatting sequences to create directory names which contain a dynamic date value. Currently, the following format strings are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>%Y</i></p>
<dd> 4-digit year (e.g. 2009)</p>
<dt><i>%m</i></p>
<dd> Month (01..12)</p>
<dt><i>%d</i></p>
<dd> Day of month, leading zero</p>
<dt><i>%h</i></p>
<dd> Month abbreviation,</p>
<dt><i>%H</i></p>
<dd> Hour, 24 hour clock, leading zero</p>
<dt><i>%M</i></p>
<dd> Minute, leading zero</p>
<dt><i>%S</i></p>
<dd> Seconds, leading zero</dl>
</dl>
<dl>
<dt>
<dd>
<p> Example: <i></i>$mountdir<i>=/path/to/%Y-%m-%d</i> will expand to <i>/path/to/2009-06-13</i></dl>
<dt><code>&#8211;backupdir=string</code></p>
<dd> Specifies the pathname of the directory where the archive files will be written to. The backup directory must not be on the same volume as the MySQL data directory. If the directory does not exist, it will be created. </p>
<p> It is possible to use selected <i>timestr()</i> formatting sequences to create directory names which contain a dynamic date value. Currently, the following format strings are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>%Y</i></p>
<dd> 4-digit year (e.g. 2009)</p>
<dt><i>%m</i></p>
<dd> Month (01..12)</p>
<dt><i>%d</i></p>
<dd> Day of month, leading zero</p>
<dt><i>%h</i></p>
<dd> Month abbreviation,</p>
<dt><i>%H</i></p>
<dd> Hour, 24 hour clock, leading zero</p>
<dt><i>%M</i></p>
<dd> Minute, leading zero</p>
<dt><i>%S</i></p>
<dd> Seconds, leading zero</dl>
</dl>
<dl>
<dt>
<dd>
<p> Example: <i></i>$mountdir<i>=/path/to/%Y-%m-%d</i> will expand to <i>/path/to/2009-06-13</i> </p>
<p> Instead of a local directory, you can also provide a valid rsync <font SIZE="-1">URL</font> here, e.g. <i>username [at] hostname:/path</i>, <i>hostname:path</i> or <i>hostname::rsync-module/path</i>. This requires a properly configured remote rsync setup (e.g. pre-setup <font SIZE="-1">SSH</font> keys or a working rsyncd configuration). </p>
<p> Note that the <i>backupretention</i> option does not work for rsync URLs or directory names that use format strings. You need to define a static local directory name in <i>backupdir</i> if you want to use the <i>purge</i> action to automatically remove older backups from the backup directory. </p>
<p> The default is <i>/var/tmp/mylvmbackup/backup/</i></dl>
<dt><code>&#8211;mount=string</code></p>
<dd> Specifies the pathname for the <i>mount</i> program. The default is <i>mount</i>.</p>
<dt><code>&#8211;umount=string</code></p>
<dd> Specifies the pathname for the <i>umount</i> program. The default is <i>umount</i>.</p>
<dt><code>&#8211;tar=string</code></p>
<dd> Specifies the pathname for the <i>tar</i> program. The default is <i>tar</i>.</p>
<dt><code>&#8211;tararg=string</code></p>
<dd> Specifies the initial arguments for the <i>tar</i> program. The default is <i>cvf</i>.</p>
<dt><code>&#8211;tarsuffixarg=string</code></p>
<dd> Specifies the suffix arguments for the <i>tar</i> program. The default is the empty string. To exclude a database, you would pass <i>&#8211;exclude dbname</i> here.</p>
<dt><code>&#8211;tarfilesuffix=string</code></p>
<dd> Specifies the suffix for the tarball. This value should be set according to the selected compression method (e.g. <i>.tar.bz2</i> for bzip2 compression). The default is <i>.tar.gz</i>.</p>
<dt><code>&#8211;compress=string</code></p>
<dd> Specifies the name of the compression program. Only used if <i>backuptype</i> is set to <i>tar</i>. Some possibilities are <i>gzip</i>, <i>bzip2</i> or <i>lzma</i>. The program must support reading the to be compressed data from <i>stdin</i> and writing to <i>stdout</i>, without requiring intermediate temporary files (for this reason, 7zip cannot be used). It&#8217;s also possible to use <i>cat</i>. In this case, no compression will be done. Make sure to update the <i>compressarg</i> option and the <i>tarfilesuffix</i> accordingly. The default is <i>gzip</i>. Can be left empty.</p>
<dt><code>&#8211;compressarg=string</code></p>
<dd> Specifies the command line options given to the <i>compress</i> program. For <i>gzip</i>, that would be <i>&#8211;stdout &#8211;verbose &#8211;best</i>, for <i>lzma</i> or <i>bzip2</i> <i>&#8211;stdout &#8211;verbose -7</i> and for <i>cat</i>, it would be empty. The default is <i>&#8211;stdout &#8211;verbose &#8211;best</i>.</p>
<dt><code>&#8211;rsnap=string</code></p>
<dd> Specifies the pathname for the <i>rsnap</i> program. The default is <i>rsnap</i>.</p>
<dt><code>&#8211;rsnaparg=string</code></p>
<dd> Specifies the arguments for the <i>rsnap</i> program. The default is <i>7</i>, which causes it to keep the last 7 snapshot (useful when running <i>mylvmbackup</i> once per day).</p>
<dt><code>&#8211;rsnaprsyncarg=string</code></p>
<dd> Specifies the arguments for the <i>rsync</i> process that is spawned by <i>rsnap</i>, e.g. <i>&#8211;exclude \*.o &#8211;bwlimit=8</i>. You don&#8217;t need to provide the double dashes usually required by <i>rsnap</i> to separate these arguments. Default value is the empty string.</p>
<dt><code>&#8211;rsync=string</code></p>
<dd> Specifies the pathname for the <i>rsync</i> program. The default is <i>rsync</i>.</p>
<dt><code>&#8211;rsyncarg=string</code></p>
<dd> Specifies the arguments for the <i>rsync</i> program. The default is <i>-avWP</i>. You must ensure that the recursive option is included either implicitly by <i>-a</i>, or explicitly by using <i>-r</i>.</p>
<dt><code>&#8211;zbackup=string</code></p>
<dd> Specifies the pathname for the <i>zbackup</i> program. The default is <i>zbackup</i>.</p>
<dt><code>&#8211;zbackuparg=string</code></p>
<dd> Specifies the arguments for the <i>zbackup</i> program. The default is <i>&#8211;non-encrypted</i>. </p>
<p> You may use <i>&#8211;password-file /path/to/pass</i> to create an encrypted zbackup repository. The backup repository located in <i>backupdir</i> will be initialized automatically by running <i>zbackup init</i> before the first invocation.</p>
<dt><code>&#8211;xfs</code></p>
<dd> Use the <i>nouuid</i> mount option to safely mount snapshot partitions that use the <font SIZE="-1">XFS</font> file system.</p>
<dt><code>&#8211;log_method=string</code></p>
<dd> How to log output from this script. Valid options are <i>console</i>, <i>syslog</i> or <i>both</i>. The default value is <i>console</i>. Enabling the <i>syslog</i> option requires an installed <i>Sys::Syslog</i> Perl module.</p>
<dt><code>&#8211;syslog_socktype=string</code></p>
<dd> What type of socket to use for connecting to the syslog service. Valid options are <i>native</i>, <i>tcp</i> and <i>udp</i>. The default value is <i>native</i>.</p>
<dt><code>&#8211;syslog_facility=string</code></p>
<dd> Define a particular syslog facility Default value is the empty string.</p>
<dt><code>&#8211;syslog_remotehost=string</code></p>
<dd> Host name of a remote syslog server.</p>
<dt><code>&#8211;mail_report_on=string</code></p>
<dd> Enable sending the logging output via email to a specified email address. </p>
<p> This option requires an installed <i>MIME::Lite</i> Perl module as well as a functional local sendmail (or alternative) facility. </p>
<p> You should also review and adjust the <i>mail_from</i>, <i>mail_to</i> and <i>mail_subject</i> configuration options to match you requirements. </p>
<p> Supported values are <i>never</i>, this disables the mail reporting completely. A value of <i>always</i> sends an email report for each invocation of <i>mylvmbackup</i>, <i>errors</i> only sends a report in case of an error condition. </p>
<p> The default value is <i>never</i>.</p>
<dt><code>&#8211;mail_from=string</code></p>
<dd> The email address to be used in the <i>From:</i> header for email reports (requires the <i>mail_report</i> option to be set). The default value is <i>root [at] localhost</i>.</p>
<dt><code>&#8211;mail_to=string</code></p>
<dd> The email address to be used to send email reports to (requires the <i>mail_report</i> option to be set). The default value is <i>root [at] localhost</i>.</p>
<dt><code>&#8211;mail_subject=string</code></p>
<dd> The text to be used in the <i>Subject:</i> header for email reports (requires the <i>mail_report</i> option to be set). The default value is &#8220;mylvmbackup report for localhost&#8221;.</p>
<dt><code>&#8211;snmp_report_on=string</code></p>
<dd> Enable sending <font SIZE="-1">SNMP</font> traps to specified <font SIZE="-1">SNMP</font> target hosts. </p>
<p> This option requires an installed <i>Net::SNMP</i> Perl module. </p>
<p> You should also review and adjust the <i>snmp_base_oid</i>, <i>snmp_targets</i>, <i>snmp_community</i> <i>snmp_port</i> configuration options to match you requirements. </p>
<p> Supported values are <i>never</i>, this disables sending <font SIZE="-1">SNMP</font> traps completely. A value of <i>always</i> sends an <font SIZE="-1">SNMP</font> trap for each invocation of <i>mylvmbackup</i>, <i>errors</i> only sends an <font SIZE="-1">SNMP</font> trap in case of an error condition. </p>
<p> The default value is <i>never</i>.</p>
<dt><code>&#8211;snmp_base_oid=string</code></p>
<dd> The <font SIZE="-1">SNMP</font> object identifier (<font SIZE="-1">OID</font>) in dotted notation. The default is <i>1.3.6.1.4.1.0.0</i>.</p>
<dt><code>&#8211;snmp_targets=string</code></p>
<dd> A comma-separated list of host names or <font SIZE="-1">IP</font> addresses to send <font SIZE="-1">SNMP</font> traps to. The default is <i>localhost</i>.</p>
<dt><code>&#8211;snmp_community=string</code></p>
<dd> The <font SIZE="-1">SNMP</font> community name. The default is <i>public</i>.</p>
<dt><code>&#8211;snmp_port=number</code></p>
<dd> The <font SIZE="-1">TCP</font> port on the target host to send <font SIZE="-1">SNMP</font> traps to. The default is <i>162</i>.</p>
<dt><code>&#8211;configfile=string</code></p>
<dd> Specify an alternative configuration file. The default is <i>/etc/mylvmbackup.conf</i>.</p>
<dt><code>&#8211;help</code></p>
<dd> Displays a help message showing the available options.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/mylvbackup.conf</code></p>
<dd> The <i>mylvmbackup</i> configuration file</p>
<dt><code>mylvmbackup</code></p>
<dd> The executable Perl script that performs the work.</dl>
<h2>REQUIREMENTS</h2>
<p> For proper operation <i>mylvmbackup</i> requires Perl 5 with the <i></i><font SIZE="-1"><i>DBI</i></font><i></i> and <i>DBD::mysql</i> modules. It also needs the <i>Config::IniFiles</i> to read the global configuration file of the program. <i>Date::Format</i> is required to create the time stamp used in the backup file names. In addition, it utilizes <i>Getopt::Long</i>, <i>File::Basename</i> and <i>File::Temp</i>, which usually are part of the default Perl distribution. <i>File::Copy::Recursive</i> is used to copy the MySQL configuration file(s). <i>Sys::Syslog</i> is only required in case you want to enable the syslog log facility. The <i>MIME::Lite</i> module is required when you enable the mail reporting functionality. It also requires a functional local sendmail (or alternative) facility. </p>
<p> It also requires several other external programs: <font SIZE="-1">GNU </font><i>tar</i> and <i>gzip</i> to back up the data, <font SIZE="-1">LVM</font> utilities (<i>lvcreate</i>, <i>lvremove</i> and <i>lvs</i>) to create and remove the <font SIZE="-1">LVM</font> snapshot, and the system utilities <i>mount</i> and <i>umount</i>. Please note that <i>mylvmbackup</i> requires Linux <font SIZE="-1">LVM</font> Version 2 or higher. It does not work on LVMv1, as this version does not support writable snapshots. </p>
<p> Optionally, <i>rsync</i> or <i>rsnap</i> may be required instead of <i>tar</i> and <i>gzip</i>, depending on which backup type you choose.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-mount/">mount</a></i>(8), <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1), <i><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></i>(8), <i><a href="/docs/linux/man/8-lvremove/">lvremove</a></i>(8), <i><a href="/docs/linux/man/8-lvs/">lvs</a></i>(8), <i><a href="/docs/linux/man/8-umount/">umount</a></i>(8), <i><a href="/docs/linux/man/1-rsync/">rsync</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> This program was initially written by Aleksey &#8220;Walrus&#8221; Kishkin from MySQL <font SIZE="-1">AB,</font> with suggestions from Peter Zaitsev and Lenz Grimmer. </p>
<p> It is currently maintained by Lenz Grimmer &lt;lenz [at] grimmer.com&gt;</p>
<h2>RESOURCES</h2>
<p> Main web site: &lt;<a rel="nofollow" href="http://www.lenzg.net/mylvmbackup">http://www.lenzg.net/mylvmbackup</a>&gt; </p>
<p> Mailing list: &lt;<a rel="nofollow" href="https://launchpad.net/~mylvmbackup-discuss">https://launchpad.net/~mylvmbackup-discuss</a>&gt; </p>
<p> Source code, bug tracker: &lt;<a rel="nofollow" href="https://launchpad.net/mylvmbackup">https://launchpad.net/mylvmbackup</a>&gt;</p>
<h2>CREDITS</h2>
<p> See the file <font SIZE="-1">CREDITS</font> included in the distribution for a list of individual contributors.</p>
<h2>COPYING</h2>
<p> <i>mylvmbackup</i> is distributed under the <font SIZE="-1">GNU</font> public license. See the file <font SIZE="-1">COPYING</font> for details. </p>
<h2>Index</h2>
