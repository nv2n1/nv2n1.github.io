---
title: "rsnapshot(1)"
name: "rsnapshot"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rsnapshot/"
description: "rsnapshot – remote filesystem snapshot utility"
---

<h2 class="name">NAME</h2>
<p> rsnapshot &#8211; remote filesystem snapshot utility </p>
<h2>SYNOPSIS</h2>
<p> <code>rsnapshot</code> [<code>-vtxqVD</code>] [<code>-c</code> cfgfile] [command] [args]</p>
<h2>DESCRIPTION</h2>
<p> <code>rsnapshot</code> is a filesystem snapshot utility. It can take incremental snapshots of local and remote filesystems for any number of machines. </p>
<p> Local filesystem snapshots are handled with <a href="/docs/linux/man/1-rsync/">rsync</a><code>(1)</code>. Secure remote connections are handled with rsync over <a href="/docs/linux/man/1-ssh/">ssh</a><code>(1)</code>, while anonymous rsync connections simply use an rsync server. Both remote and local transfers depend on rsync. </p>
<p> <code>rsnapshot</code> saves much more disk space than you might imagine. The amount of space required is roughly the size of one full backup, plus a copy of each additional file that is changed. <code>rsnapshot</code> makes extensive use of hard links, so if the file doesn&#8217;t change, the next snapshot is simply a hard link to the exact same file. </p>
<p> <code>rsnapshot</code> will typically be invoked as root by a cron job, or series of cron jobs. It is possible, however, to run as any arbitrary user with an alternate configuration file. </p>
<p> All important options are specified in a configuration file, which is located by default at <code>/etc/rsnapshot.conf</code>. An alternate file can be specified on the command line. There are also additional options which can be passed on the command line. </p>
<p> The command line options are as follows: </p>
<dl>
<dt>
<dd> <code>-v</code> verbose, show shell commands being executed </p>
<p> <code>-t</code> test, show shell commands that would be executed </p>
<p> <code>-c</code> path to alternate config file </p>
<p> <code>-x</code> one filesystem, don&#8217;t cross partitions within each backup point </p>
<p> <code>-q</code> quiet, suppress non-fatal warnings </p>
<p> <code>-V</code> same as -v, but with more detail </p>
<p> <code>-D</code> a firehose of diagnostic information</dl>
<h2>CONFIGURATION</h2>
<p> <code>/etc/rsnapshot.conf</code> is the default configuration file. All parameters in this file must be separated by tabs. <code>/etc/rsnapshot.conf.default</code> can be used as a reference. </p>
<p> It is recommended that you copy <code>/etc/rsnapshot.conf.default</code> to <code>/etc/rsnapshot.conf</code>, and then modify <code>/etc/rsnapshot.conf</code> to suit your needs. </p>
<p> Long lines may be split over several lines. &#8220;Continuation&#8221; lines <code>must</code> begin with a space or a tab character. Continuation lines will have all leading and trailing whitespace stripped off, and then be appended with an intervening tab character to the previous line when the configuation file is parsed. </p>
<p> Here is a list of allowed parameters: </p>
<dl>
<dt>
<dd> <code>config_version</code> Config file version (required). Default is 1.2 </p>
<p> <code>snapshot_root</code> Local filesystem path to save all snapshots </p>
<p> <code>include_conf</code> Include another file in the configuration at this point. </p>
<dl>
<dt>
<dd> This is recursive, but you may need to be careful about paths when specifying which file to include. We check to see if the file you have specified is readable, and will yell an error if it isn&#8217;t. We recommend using a full path. As a special case, include_conf&#8217;s value may be enclosed in `backticks` in which case it will be executed and whatever it spits to <font SIZE="-1">STDOUT</font> will be included in the configuration. Note that shell meta-characters may be interpreted.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>no_create_root</code> If set to 1, rsnapshot won&#8217;t create snapshot_root directory </p>
<p> <code>cmd_rsync</code> Full path to rsync (required) </p>
<p> <code>cmd_ssh</code> Full path to ssh (optional) </p>
<p> <code>cmd_cp</code> Full path to cp (optional, but must be <font SIZE="-1">GNU</font> version) </p>
<dl>
<dt>
<dd> If you are using Linux, you should uncomment cmd_cp. If you are using a platform which does not have <font SIZE="-1">GNU</font> cp, you should leave cmd_cp commented out. </p>
<p> With <font SIZE="-1">GNU</font> cp, rsnapshot can take care of both normal files and special files (such as FIFOs, sockets, and block/character devices) in one pass. </p>
<p> If cmd_cp is disabled, rsnapshot will use its own built-in function, <i>native_cp_al()</i> to backup up regular files and directories. This will then be followed up by a separate call to rsync, to move the special files over (assuming there are any).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>cmd_rm</code> Full path to rm (optional) </p>
<p> <code>cmd_logger</code> Full path to logger (optional, for syslog support) </p>
<p> <code>cmd_du</code> Full path to du (optional, for disk usage reports) </p>
<p> <code>cmd_rsnapshot_diff</code> Full path to rsnapshot-diff (optional) </p>
<p> <code>cmd_preexec</code> </p>
<dl>
<dt>
<dd> Full path (plus any arguments) to preexec script (optional). This script will run immediately before each backup operation (but not any rotations). If the execution fails, rsnapshot will stop immediately.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>cmd_postexec</code> </p>
<dl>
<dt>
<dd> Full path (plus any arguments) to postexec script (optional). This script will run immediately after each backup operation (but not any rotations). If the execution fails, rsnapshot will stop immediately.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>linux_lvm_cmd_lvcreate</code> </p>
<p> <code>linux_lvm_cmd_lvremove</code> </p>
<p> <code>linux_lvm_cmd_mount</code> </p>
<p> <code>linux_lvm_cmd_umount</code> </p>
<dl>
<dt>
<dd> Paths to lvcreate, lvremove, mount and umount commands, for use with Linux LVMs. You may include options to the commands also. The lvcreate, lvremove, mount and umount commands are required for managing snapshots of <font SIZE="-1">LVM</font> volumes and are otherwise optional.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>retain</code> [name] [number] </p>
<dl>
<dt>
<dd> &#8220;name&#8221; refers to the name of this backup level (e.g., alpha, beta, so also called the &#8216;interval&#8217;). &#8220;number&#8221; is the number of snapshots for this type of interval that will be retained. The value of &#8220;name&#8221; will be the command passed to <code>rsnapshot</code> to perform this type of backup. </p>
<p> A deprecated alias for &#8216;retain&#8217; is &#8216;interval&#8217;. </p>
<p> Example: <code>retain alpha 6</code> </p>
<p> [root [at] localhost]# <code>rsnapshot alpha</code> </p>
<p> For this example, every time this is run, the following will happen: </p>
<p> &lt;snapshot_root&gt;/alpha.5/ will be deleted, if it exists. </p>
<p> &lt;snapshot_root&gt;/alpha.{1,2,3,4} will all be rotated +1, if they exist. </p>
<p> &lt;snapshot_root&gt;/alpha.0/ will be copied to &lt;snapshot_root&gt;/alpha.1/ using hard links. </p>
<p> Each backup point (explained below) will then be rsynced to the corresponding directories in &lt;snapshot_root&gt;/alpha.0/ </p>
<p> Backup levels must be specified in the config file in order, from most frequent to least frequent. The first entry is the one which will be synced with the backup points. The subsequent backup levels (e.g., beta, gamma, etc) simply rotate, with each higher backup level pulling from the one below it for its .0 directory. </p>
<p> Example: </p>
<dl>
<dt>
<dd> <code>retain alpha 6</code> </p>
<p> <code>retain beta 7</code> </p>
<p> <code>retain gamma 4</code></dl>
</dl>
<dl>
<dt>
<dd>
<p> beta.0/ will be moved from alpha.5/, and gamma.0/ will be moved from beta.6/ </p>
<p> alpha.0/ will be rsynced directly from the filesystem.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>link_dest 1</code> </p>
<dl>
<dt>
<dd> If your version of rsync supports &#8211;link-dest (2.5.7 or newer), you can enable this to let rsync handle some things that <font SIZE="-1">GNU</font> cp or the built-in subroutines would otherwise do. Enabling this makes rsnapshot take a slightly more complicated code branch, but it&#8217;s the best way to support special files on non-Linux systems.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>sync_first 1</code> </p>
<dl>
<dt>
<dd> sync_first changes the behaviour of rsnapshot. When this is enabled, all calls to rsnapshot with various backup levels simply rotate files. All backups are handled by calling rsnapshot with the &#8220;sync&#8221; argument. The synced files are stored in a &#8220;.sync&#8221; directory under the snapshot_root. </p>
<p> This allows better recovery in the event that rsnapshot is interrupted in the middle of a sync operation, since the sync step and rotation steps are separated. This also means that you can easily run &#8220;rsnapshot sync&#8221; on the command line without fear of forcing all the other directories to rotate up. This benefit comes at the cost of one more snapshot worth of disk space. The default is 0 (off).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>verbose 2</code> </p>
<dl>
<dt>
<dd> The amount of information to print out when the program is run. Allowed values are 1 through 5. The default is 2. </p>
<pre>
    1        Quiet            Show fatal errors only
    2        Default          Show warnings and errors
    3        Verbose          Show equivalent shell commands being executed
    4        Extra Verbose    Same as verbose, but with more detail
    5        Debug            All kinds of information
</pre>
</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>loglevel 3</code> </p>
<dl>
<dt>
<dd> This number means the same thing as <code>verbose</code> above, but it determines how much data is written to the logfile, if one is being written.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>logfile /var/log/rsnapshot</code> </p>
<dl>
<dt>
<dd> Full filesystem path to the rsnapshot log file. If this is defined, a log file will be written, with the amount of data being controlled by <code>loglevel</code>. If this is commented out, no log file will be written.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>include [file-name-pattern]</code> </p>
<dl>
<dt>
<dd> This gets passed directly to rsync using the &#8211;include directive. This parameter can be specified as many times as needed, with one pattern defined per line. See the <i><a href="/docs/linux/man/1-rsync/">rsync</a></i>(1) man page for the syntax.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>exclude [file-name-pattern]</code> </p>
<dl>
<dt>
<dd> This gets passed directly to rsync using the &#8211;exclude directive. This parameter can be specified as many times as needed, with one pattern defined per line. See the <i><a href="/docs/linux/man/1-rsync/">rsync</a></i>(1) man page for the syntax.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>include_file /path/to/include/file</code> </p>
<dl>
<dt>
<dd> This gets passed directly to rsync using the &#8211;include-from directive. See the <i><a href="/docs/linux/man/1-rsync/">rsync</a></i>(1) man page for the syntax.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>exclude_file /path/to/exclude/file</code> </p>
<dl>
<dt>
<dd> This gets passed directly to rsync using the &#8211;exclude-from directive. See the <i><a href="/docs/linux/man/1-rsync/">rsync</a></i>(1) man page for the syntax.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>rsync_short_args -a</code> </p>
<dl>
<dt>
<dd> List of short arguments to pass to rsync. If not specified, &#8220;-a&#8221; is the default. Please note that these must be all next to each other. For example, &#8220;-az&#8221; is valid, while &#8220;-a -z&#8221; is not. </p>
<p> &#8220;-a&#8221; is rsync&#8217;s &#8220;archive mode&#8221; which tells it to copy as much of the filesystem metadata as it can for each file. This specifically does *not* include information about hard links, as that would greatly increase rsync&#8217;s memory usage and slow it down. If you need to preserve hard links in your backups, then add &#8220;H&#8221; to this.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>rsync_long_args &#8211;delete &#8211;numeric-ids &#8211;relative &#8211;delete-excluded</code> </p>
<dl>
<dt>
<dd> List of long arguments to pass to rsync. The default values are<br />
&nbsp;<wbr>&#8211;delete &#8211;numeric-ids &#8211;relative &#8211;delete-excluded This means that the directory structure in each backup point destination will match that in the backup point source. </p>
<p> Quotes are permitted in rsync_long_args, eg &#8211;rsync-path=&#8220;sudo /usr/bin/rsync&#8221;. You may use either single (&#8216;) or double (&quot;) quotes, but nested quotes (including mixed nested quotes) are not permitted. Similar quoting is also allowed in per-backup-point rsync_long_args.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>ssh_args -p 22</code> </p>
<dl>
<dt>
<dd> Arguments to be passed to ssh. If not specified, the default is none.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>du_args -csh</code> </p>
<dl>
<dt>
<dd> Arguments to be passed to du. If not specified, the default is -csh. <font SIZE="-1">GNU</font> du supports -csh, <font SIZE="-1">BSD</font> du supports -csk, Solaris du doesn&#8217;t support -c at all. The <font SIZE="-1">GNU</font> version is recommended, since it offers the most features.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>lockfile /var/run/rsnapshot.pid</code> </p>
<p> <code>stop_on_stale_lockfile<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</code></p>
<dl>
<dt>
<dd> Lockfile to use when rsnapshot is run. This prevents a second invocation from clobbering the first one. If not specified, no lock file is used. Make sure to use a directory that is not world writeable for security reasons. Use of a lock file is strongly recommended. </p>
<p> If a lockfile exists when rsnapshot starts, it will try to read the file and stop with an error if it can&#8217;t. If it *can* read the file, it sees if a process exists with the <font SIZE="-1">PID</font> noted in the file. If it does, rsnapshot stops with an error message. If there is no process with that <font SIZE="-1">PID,</font> then we assume that the lockfile is stale and ignore it *unless* stop_on_stale_lockfile is set to 1 in which case we stop. </p>
<p> stop_on_stale_lockfile defaults to 0.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>one_fs 1</code> </p>
<dl>
<dt>
<dd> Prevents rsync from crossing filesystem partitions. Setting this to a value of 1 enables this feature. 0 turns it off. This parameter is optional. The default is 0 (off).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>use_lazy_deletes 1</code> </p>
<dl>
<dt>
<dd> Changes default behavior of rsnapshot and does not initially remove the oldest snapshot. Instead it moves that directory to _delete.[processid] and continues as normal. Once the backup has been completed, the lockfile will be removed before rsnapshot starts deleting the directory. </p>
<p> Enabling this means that snapshots get taken sooner (since the delete doesn&#8217;t come first), and any other rsnapshot processes are allowed to start while the final delete is happening. This benefit comes at the cost of using more disk space. The default is 0 (off). </p>
<p> The details of how this works have changed in rsnapshot version 1.3.1. Originally you could only ever have one .delete directory per backup level. Now you can have many, so if your next (eg) alpha backup kicks off while the previous one is still doing a lazy delete you may temporarily have extra _delete directories hanging around.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>linux_lvm_snapshotsize 2G</code> </p>
<dl>
<dt>
<dd> <font SIZE="-1">LVM</font> snapshot(s) size (lvcreate &#8211;size option).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>linux_lvm_snapshotname rsnapshot</code> </p>
<dl>
<dt>
<dd> Name to be used when creating the <font SIZE="-1">LVM</font> logical volume snapshot(s) (lvcreate &#8211;name option).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>linux_lvm_vgpath<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev</code></p>
<dl>
<dt>
<dd> Path to the <font SIZE="-1">LVM</font> Volume Groups.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>linux_lvm_mountpath<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/mnt/lvm-snapshot</code></p>
<dl>
<dt>
<dd> Mount point to use to temporarily mount the snapshot(s).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup</code> /etc/ localhost/ </p>
<p> <code>backup</code> root [at] example.com:/etc/ example.com/ </p>
<p> <code>backup</code> <a href="rsync://example.com/path2/">rsync://example.com/path2/</a> example.com/ </p>
<p> <code>backup</code> /var/ localhost/ one_fs=1 </p>
<p> <code>backup</code> <a href="lvm://vg0/home/path2/">lvm://vg0/home/path2/</a> lvm-vg0/ </p>
<p> <code>backup_script</code> /usr/local/bin/backup_pgsql.sh pgsql_backup/ </p>
<dl>
<dt>
<dd> Examples: </p>
<p> <code>backup /etc/ localhost/</code> </p>
<dl>
<dt>
<dd> Backs up /etc/ to &lt;snapshot_root&gt;/&lt;retain&gt;.0/localhost/etc/ using rsync on the local filesystem</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup /usr/local/ localhost/</code> </p>
<dl>
<dt>
<dd> Backs up /usr/local/ to &lt;snapshot_root&gt;/&lt;retain&gt;.0/localhost/usr/local/ using rsync on the local filesystem</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup root [at] example.com:/etc/ example.com/</code> </p>
<dl>
<dt>
<dd> Backs up root [at] example.com:/etc/ to &lt;snapshot_root&gt;/&lt;retain&gt;.0/example.com/etc/ using rsync over ssh</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup example.com:/etc/ example.com/</code> </p>
<dl>
<dt>
<dd> Same thing but let ssh choose the remote username (as specified in ~/.ssh/config, otherwise the same as the local username)</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup root [at] example.com:/usr/local/ example.com/</code> </p>
<dl>
<dt>
<dd> Backs up root [at] example.com:/usr/local/ to &lt;snapshot_root&gt;/&lt;retain&gt;.0/example.com/usr/local/ using rsync over ssh</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup <a href="rsync://example.com/pub/">rsync://example.com/pub/</a> example.com/pub/</code> </p>
<dl>
<dt>
<dd> Backs up <a href="rsync://example.com/pub/">rsync://example.com/pub/</a> to &lt;snapshot_root&gt;/&lt;retain&gt;.0/example.com/pub/ using an anonymous rsync server. Please note that unlike backing up local paths and using rsync over ssh, rsync servers have &#8220;modules&#8221;, which are top level directories that are exported. Therefore, the module should also be specified in the destination path, as shown in the example above (the pub/ directory at the end).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup /var/ localhost/ one_fs=1</code> </p>
<dl>
<dt>
<dd> This is the same as the other examples, but notice the fourth column. This is how you specify per-backup-point options to over-ride global settings. This extra parameter can take several options, separated by <code>commas</code>. </p>
<p> It is most useful when specifying per-backup rsync excludes thus: </p>
<p> <code>backup root [at] somehost:/ somehost +rsync_long_args=&#8211;exclude=/var/spool/</code> </p>
<p> Note the + sign. That tells rsnapshot to <i>add</i> to the list of arguments to pass to rsync instead of replacing the list.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup <a href="lvm://vg0/home/path2/">lvm://vg0/home/path2/</a> lvm-vg0/</code> </p>
<dl>
<dt>
<dd> Backs up the <font SIZE="-1">LVM</font> logical volume called home, of volume group vg0, to &lt;snapshot_root&gt;/&lt;interval&gt;.0/lvm-vg0/. Will create, mount, backup, unmount and remove an <font SIZE="-1">LVM</font> snapshot for each lvm:// entry.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup_script /usr/local/bin/backup_database.sh db_backup/</code> </p>
<dl>
<dt>
<dd> In this example, we specify a script or program to run. This script should simply create files and/or directories in its current working directory. rsnapshot will then take that output and move it into the directory specified in the third column. </p>
<p> Please note that whatever is in the destination directory will be completely deleted and recreated. For this reason, rsnapshot prevents you from specifying a destination directory for a backup_script that will clobber other backups. </p>
<p> So in this example, say the backup_database.sh script simply runs a command like: </p>
<dl>
<dt>
<dd> #!/bin/sh </p>
<p> mysqldump -uusername mydatabase &gt; mydatabase.sql </p>
<p> chmod u=r,go= mydatabase.sql<tt>&nbsp;<wbr></tt># r&#8212;&#8212;&#8211; (0400)
</dl>
</dl>
<dl>
<dt>
<dd>
<p> rsnapshot will take the generated &#8220;mydatabase.sql&#8221; file and move it into the &lt;snapshot_root&gt;/&lt;retain&gt;.0/db_backup/ directory. On subsequent runs, rsnapshot checks the differences between the files created against the previous files. If the backup script generates the same output on the next run, the files will be hard linked against the previous ones, and no additional disk space will be taken up.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>backup_exec ssh root [at] 1.2.3.4 &#8220;du -sh /.offsite_backup&#8221; optional/</code> <code>backup_exec rsync -az /.snapshots/daily.0 root [at] 1.2.3.4:/.offsite_backup/ required/</code> <code>backup_exec /bin/true/</code> </p>
<dl>
<dt>
<dd> backup_exec simply runs the command listed. The second argument is not required and defaults to a value of &#8216;optional&#8217;. It specifies the importance that the command return 0. Valid values are &#8216;optional&#8217; and &#8216;required&#8217;. If the command is specified as optional, a non-zero exit status from the command will result in a warning message being output. If the command is specified as &#8216;required&#8217;, a non-zero exit status from the command will result in an error message being output and rsnapshot itself will exit with a non-zero exit status.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Remember that tabs must separate all elements, and that there must be a trailing slash on the end of every directory. </p>
<p> A hash mark (#) on the beginning of a line is treated as a comment. </p>
<p> Putting it all together (an example file): </p>
<pre><code>
#THIS IS A COMMENT, REMEMBER TABS MUST SEPARATE ALL ELEMENTS
config_version 1.2 snapshot_root /.snapshots /
        cmd_rsync / usr / bin / rsync cmd_ssh / usr / bin / ssh
#cmd_cp / bin / cp
                                                                cmd_rm /
        bin / rm cmd_logger / usr / bin / logger cmd_du / usr / bin / du linux_lvm_cmd_lvcreate / sbin / lvcreate linux_lvm_cmd_lvremove / sbin / lvremove linux_lvm_cmd_mount / bin / mount linux_lvm_cmd_umount / bin / umount linux_lvm_snapshotsize 2G linux_lvm_snapshotname rsnapshot linux_lvm_vgpath / dev linux_lvm_mountpath / mnt / lvm -
    snapshot
            retain alpha 6 retain beta 7 retain gamma 7 retain delta 3 backup /
        etc / localhost /
        backup / home / localhost /
        backup_script / usr / local / bin / backup_mysql.sh mysql_backup /
        backup root[at] foo.com : / etc / foo.com /
                                  backup root[at] foo.com : / home / foo.com /
                                                            backup root[at] mail.foo.com : / home / mail.foo.com /
                                                                                           backup rsync :              // example.com/pub/  example.com/pub/
                                                                                                          backup lvm : // vg0/xen-home/       lvm-vg0/xen-home/
                                                                                                                       backup_exec echo "backup finished!"
</code></pre>
</dl>
<dl>
<dt>
<dd></dl>
<h2>USAGE</h2>
<p> <code>rsnapshot</code> can be used by any user, but for system-wide backups you will probably want to run it as root. </p>
<p> Since backups usually get neglected if human intervention is required, the preferred way is to run it from cron. </p>
<p> When you are first setting up your backups, you will probably also want to run it from the command line once or twice to get a feel for what it&#8217;s doing. </p>
<p> Here is an example crontab entry, assuming that backup levels <code>alpha</code>, <code>beta</code>, <code>gamma</code> and <code>delta</code> have been defined in <code>/etc/rsnapshot.conf</code> </p>
<dl>
<dt>
<dd> <code>0 */4 * * * /usr/local/bin/rsnapshot alpha</code> </p>
<p> <code>50 23 * * * /usr/local/bin/rsnapshot beta</code> </p>
<p> <code>40 23 * * 6 /usr/local/bin/rsnapshot gamma</code> </p>
<p> <code>30 23 1 * * /usr/local/bin/rsnapshot delta</code></dl>
<p> This example will do the following: </p>
<dl>
<dt>
<dd> 6 alpha backups a day (once every 4 hours, at 0,4,8,12,16,20) </p>
<p> 1 beta backup every day, at 11:50PM </p>
<p> 1 gamma backup every week, at 11:40PM, on Saturdays (6th day of week) </p>
<p> 1 delta backup every month, at 11:30PM on the 1st day of the month</dl>
<p> It is usually a good idea to schedule the larger backup levels to run a bit before the lower ones. For example, in the crontab above, notice that &#8220;beta&#8221; runs 10 minutes before &#8220;alpha&#8221;. The main reason for this is that the beta rotate will pull out the oldest alpha and make that the youngest beta (which means that the next alpha rotate will not need to delete the oldest alpha), which is more efficient. A secondary reason is that it is harder to predict how long the lowest backup level will take, since it needs to actually do an rsync of the source as well as the rotate that all backups do. </p>
<p> If rsnapshot takes longer than 10 minutes to do the &#8220;beta&#8221; rotate (which usually includes deleting the oldest beta snapshot), then you should increase the time between the backup levels. Otherwise (assuming you have set the <code>lockfile</code> parameter, as is recommended) your alpha snapshot will fail sometimes because the beta still has the lock. </p>
<p> Remember that these are just the times that the program runs. To set the number of backups stored, set the <code>retain</code> numbers in <code>/etc/rsnapshot.conf</code> </p>
<p> To check the disk space used by rsnapshot, you can call it with the &#8220;du&#8221; argument. </p>
<p> For example: </p>
<dl>
<dt>
<dd> <code>rsnapshot du</code></dl>
<p> This will show you exactly how much disk space is taken up in the snapshot root. This feature requires the <font SIZE="-1">UNIX </font><code>du</code> command to be installed on your system, for it to support the &#8220;-csh&#8221; command line arguments, and to be in your path. You can also override your path settings and the flags passed to du using the cmd_du and du_args parameters. </p>
<p> It is also possible to pass a relative file path as a second argument, to get a report on a particular file or subdirectory. </p>
<dl>
<dt>
<dd> <code>rsnapshot du localhost/home/</code></dl>
<p> The <font SIZE="-1">GNU</font> version of &#8220;du&#8221; is preferred. The <font SIZE="-1">BSD</font> version works well also, but does not support the -h flag (use -k instead, to see the totals in kilobytes). Other versions of &#8220;du&#8221;, such as Solaris, may not work at all. </p>
<p> To check the differences between two directories, call rsnapshot with the &#8220;diff&#8221; argument, followed by two backup levels or directory paths. </p>
<p> For example: </p>
<dl>
<dt>
<dd> <code>rsnapshot diff beta.0 beta.1</code> </p>
<p> <code>rsnapshot diff beta.0/localhost/etc beta.1/localhost/etc</code> </p>
<p> <code>rsnapshot diff /.snapshots/beta.0 /.snapshots/beta.1</code></dl>
<p> This will call the rsnapshot-diff program, which will scan both directories looking for differences (based on hard links). </p>
<p> <code>rsnapshot sync</code> </p>
<dl>
<dt>
<dd> When <code>sync_first</code> is enabled, rsnapshot must first be called with the <code>sync</code> argument, followed by the other usual cron entries. The sync should happen as the lowest, most frequent backup level, and right before. For example: </p>
<dl>
<dt>
<dd> <code>0 */4 * * * /usr/local/bin/rsnapshot sync &amp;&amp; /usr/local/bin/rsnapshot alpha</code> </p>
<p> <code>50 23 * * * /usr/local/bin/rsnapshot beta</code> </p>
<p> <code>40 23 1,8,15,22 * * /usr/local/bin/rsnapshot gamma</code> </p>
<p> <code>30 23 1 * * /usr/local/bin/rsnapshot delta</code></dl>
</dl>
<dl>
<dt>
<dd>
<p> The sync operation simply runs rsync and all backup scripts. In this scenario, all calls simply rotate directories, even the lowest backup level.</dl>
<p> <code>rsnapshot sync [dest]</code> </p>
<dl>
<dt>
<dd> When <code>sync_first</code> is enabled, all sync behaviour happens during an additional sync step (see above). When using the sync argument, it is also possible to specify a backup point destination as an optional parameter. If this is done, only backup points sharing that destination path will be synced. </p>
<p> For example, let&#8217;s say that example.com is a destination path shared by one or more of your backup points. </p>
<dl>
<dt>
<dd> rsnapshot sync example.com</dl>
</dl>
<dl>
<dt>
<dd>
<p> This command will only sync the files that normally get backed up into example.com. It will <font SIZE="-1">NOT</font> get any other backup points with slightly different values (like example.com/etc/, for example). In order to sync example.com/etc, you would need to run rsnapshot again, using example.com/etc as the optional parameter.</dl>
<p> <code>rsnapshot configtest</code> </p>
<dl>
<dt>
<dd> Do a quick sanity check to make sure everything is ready to go.</dl>
<h2>EXIT VALUES</h2>
<dl>
<dt>
<dd> <code>0</code> All operations completed successfully </p>
<p> <code>1</code> A fatal error occurred </p>
<p> <code>2</code> Some warnings occurred, but the backup still finished</dl>
<h2>FILES</h2>
<p> /etc/rsnapshot.conf</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rsync/">rsync</a></i>(1), <i><a href="/docs/linux/man/1-ssh/">ssh</a></i>(1), <i><a href="/docs/linux/man/1-logger/">logger</a></i>(1), <i><a href="/docs/linux/man/1-sshd/">sshd</a></i>(1), <i><a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a></i>(1), <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i><a href="/docs/linux/man/1-cp/">cp</a></i>(1), <i><a href="/docs/linux/man/1-du/">du</a></i>(1), <i><a href="/docs/linux/man/1-crontab/">crontab</a></i>(1)</p>
<h2>DIAGNOSTICS</h2>
<p> Use the <code>-t</code> flag to see what commands would have been executed. This will show you the commands rsnapshot would try to run. There are a few minor differences (for example, not showing an attempt to remove the lockfile because it wasn&#8217;t really created in the test), but should give you a very good idea what will happen. </p>
<p> Using the <code>-v</code>, <code>-V</code>, and <code>-D</code> flags will print increasingly more information to <font SIZE="-1">STDOUT.</font> </p>
<p> Make sure you don&#8217;t have spaces in the config file that you think are actually tabs. </p>
<p> Much other weird behavior can probably be attributed to plain old file system permissions and ssh authentication issues.</p>
<h2>BUGS</h2>
<p> Please report bugs (and other comments) to the rsnapshot-discuss mailing list: </p>
<p> <code><a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/rsnapshot-discuss">http://lists.sourceforge.net/lists/listinfo/rsnapshot-discuss</a></code></p>
<h2>NOTES</h2>
<p> Make sure your /etc/rsnapshot.conf file has all elements separated by tabs. See /etc/rsnapshot.conf.default for a working example file. </p>
<p> Make sure you put a trailing slash on the end of all directory references. If you don&#8217;t, you may have extra directories created in your snapshots. For more information on how the trailing slash is handled, see the <a href="/docs/linux/man/1-rsync/">rsync</a><code>(1)</code> manpage. </p>
<p> Make sure to make the snapshot directory chmod 700 and owned by root (assuming backups are made by the root user). If the snapshot directory is readable by other users, they will be able to modify the snapshots containing their files, thus destroying the integrity of the snapshots. </p>
<p> If you would like regular users to be able to restore their own backups, there are a number of ways this can be accomplished. One such scenario would be: </p>
<p> Set <code>snapshot_root</code> to <code>/.private/.snapshots</code> in <code>/etc/rsnapshot.conf</code> </p>
<p> Set the file permissions on these directories as follows: </p>
<dl>
<dt>
<dd> drwx&#8212;&#8212; /.private </p>
<p> drwxr-xr-x /.private/.snapshots</dl>
<p> Export the /.private/.snapshots directory over read-only <font SIZE="-1">NFS,</font> a read-only Samba share, etc. </p>
<p> See the rsnapshot <font SIZE="-1">HOWTO</font> for more information on making backups accessible to non-privileged users. </p>
<p> For ssh to work unattended through cron, you will probably want to use public key logins. Create an ssh key with no passphrase for root, and install the public key on each machine you want to backup. If you are backing up system files from remote machines, this probably means unattended root logins. Another possibility is to create a second user on the machine just for backups. Give the user a different name such as &#8220;rsnapshot&#8221;, but keep the <font SIZE="-1">UID</font> and <font SIZE="-1">GID</font> set to 0, to give root privileges. However, make logins more restrictive, either through ssh configuration, or using an alternate shell. </p>
<p> <font SIZE="-1">BE CAREFUL</font>! If the private key is obtained by an attacker, they will have free run of all the systems involved. If you are unclear on how to do this, see <a href="/docs/linux/man/1-ssh/">ssh</a><code>(1)</code>, <a href="/docs/linux/man/1-sshd/">sshd</a><code>(1)</code>, and <a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a><code>(1)</code>. </p>
<p> Backup scripts are run as the same user that rsnapshot is running as. Typically this is root. Make sure that all of your backup scripts are only writable by root, and that they don&#8217;t call any other programs that aren&#8217;t owned by root. If you fail to do this, anyone who can write to the backup script or any program it calls can fully take over the machine. Of course, this is not a situation unique to rsnapshot. </p>
<p> By default, rsync transfers are done using the &#8211;numeric-ids option. This means that user names and group names are ignored during transfers, but the <font SIZE="-1">UID/GID</font> information is kept intact. The assumption is that the backups will be restored in the same environment they came from. Without this option, restoring backups for multiple heterogeneous servers would be unmanageable. If you are archiving snapshots with <font SIZE="-1">GNU</font> tar, you may want to use the &#8211;numeric-owner parameter. Also, keep a copy of the archived system&#8217;s /etc/passwd and /etc/group files handy for the <font SIZE="-1">UID/GID</font> to name mapping. </p>
<p> If you remove backup points in the config file, the previously archived files under those points will permanently stay in the snapshots directory unless you remove the files yourself. If you want to conserve disk space, you will need to go into the &lt;snapshot_root&gt; directory and manually remove the files from the smallest backup level&#8217;s &#8220;.0&#8221; directory. </p>
<p> For example, if you were previously backing up /home/ with a destination of localhost/, and alpha is your smallest backup level, you would need to do the following to reclaim that disk space: </p>
<dl>
<dt>
<dd> rm -rf &lt;snapshot_root&gt;/alpha.0/localhost/home/</dl>
<p> Please note that the other snapshots previously made of /home/ will still be using that disk space, but since the files are flushed out of alpha.0/, they will no longer be copied to the subsequent directories, and will thus be removed in due time as the rotations happen.</p>
<h2>AUTHORS</h2>
<p> Mike Rubel &#8211; <code><a rel="nofollow" href="http://www.mikerubel.org/computers/rsync_snapshots/">http://www.mikerubel.org/computers/rsync_snapshots/</a></code></p>
<dl>
<dt>&#8211; Created the original shell scripts on which this project is based</p>
<dd></dl>
<p> Nathan Rosenquist (<code>nathan [at] rsnapshot.org</code>)</p>
<dl>
<dt>&#8211; Primary author and original maintainer of rsnapshot.</p>
<dd></dl>
<p> David Cantrell (<code>david [at] cantrell.org.uk</code>)</p>
<dl>
<dt>&#8211; Previous maintainer of rsnapshot</p>
<dd>
<dt>&#8211; Wrote the rsnapshot-diff utility</p>
<dd>
<dt>&#8211; Improved how use_lazy_deletes work so slow deletes don&#8217;t screw up the next backup at that backup level.</p>
<dd></dl>
<p> David Keegel &lt;djk [at] cybersource.com.au&gt;</p>
<dl>
<dt>&#8211; Previous rsnapshot maintainer</p>
<dd>
<dt>&#8211; Fixed race condition in lock file creation, improved error reporting</p>
<dd>
<dt>&#8211; Allowed remote ssh directory paths starting with &quot;~/&quot; as well as &quot;/&quot;</p>
<dd>
<dt>&#8211; Fixed a number of other bugs and buglets</p>
<dd></dl>
<p> Benedikt Heine &lt;benedikt [at] heine.rocks&gt;</p>
<dl>
<dt>&#8211; Current rsnapshot maintainer</p>
<dd></dl>
<p> Carl Wilhelm Soderstrom <code>(chrome [at] real-time.com)</code></p>
<dl>
<dt>&#8211; Created the <font SIZE="-1">RPM </font>.spec file which allowed the <font SIZE="-1">RPM</font> package to be built, among other things.</p>
<dd></dl>
<p> Ted Zlatanov (<code>tzz [at] lifelogs.com</code>)</p>
<dl>
<dt>&#8211; Added the one_fs feature, autoconf support, good advice, and much more.</p>
<dd></dl>
<p> Ralf van Dooren (<code>r.vdooren [at] snow.nl</code>)</p>
<dl>
<dt>&#8211; Added and maintains the rsnapshot entry in the FreeBSD ports tree.</p>
<dd></dl>
<p> SlapAyoda</p>
<dl>
<dt>&#8211; Provided access to his computer museum for software testing.</p>
<dd></dl>
<p> Carl Boe (<code>boe [at] demog.berkeley.edu</code>)</p>
<dl>
<dt>&#8211; Found several subtle bugs and provided fixes for them.</p>
<dd></dl>
<p> Shane Leibling (<code>shane [at] cryptio.net</code>)</p>
<dl>
<dt>&#8211; Fixed a compatibility bug in utils/backup_smb_share.sh</p>
<dd></dl>
<p> Christoph Wegscheider (<code>christoph.wegscheider [at] wegi.net</code>)</p>
<dl>
<dt>&#8211; Added (and previously maintained) the Debian rsnapshot package.</p>
<dd></dl>
<p> Bharat Mediratta (<code>bharat [at] menalto.com</code>)</p>
<dl>
<dt>&#8211; Improved the exclusion rules to avoid backing up the snapshot root (among other things).</p>
<dd></dl>
<p> Peter Palfrader (<code>weasel [at] debian.org</code>)</p>
<dl>
<dt>&#8211; Enhanced error reporting to include command line options.</p>
<dd></dl>
<p> Nicolas Kaiser (<code>nikai [at] nikai.net</code>)</p>
<dl>
<dt>&#8211; Fixed typos in program and man page</p>
<dd></dl>
<p> Chris Petersen &#8211; (<code><a rel="nofollow" href="http://www.forevermore.net/">http://www.forevermore.net/</a></code>) </p>
<dl>
<dt>
<dd> Added cwrsync permanent-share support</dl>
<p> Robert Jackson (<code>RobertJ [at] promedicalinc.com</code>) </p>
<dl>
<dt>
<dd> Added use_lazy_deletes feature</dl>
<p> Justin Grote (<code>justin [at] grote.name</code>) </p>
<dl>
<dt>
<dd> Improved rsync error reporting code</dl>
<p> Anthony Ettinger (<code>apwebdesign [at] yahoo.com</code>) </p>
<dl>
<dt>
<dd> Wrote the utils/mysqlbackup.pl script</dl>
<p> Sherman Boyd </p>
<dl>
<dt>
<dd> Wrote utils/random_file_verify.sh script</dl>
<p> William Bear (<code>bear [at] umn.edu</code>) </p>
<dl>
<dt>
<dd> Wrote the utils/rsnapreport.pl script (pretty summary of rsync stats)</dl>
<p> Eric Anderson (<code>anderson [at] centtech.com</code>) </p>
<dl>
<dt>
<dd> Improvements to utils/rsnapreport.pl.</dl>
<p> Alan Batie (<code>alan [at] batie.org</code>) </p>
<dl>
<dt>
<dd> Bug fixes for include_conf</dl>
<p> Dieter Bloms (<code>dieter [at] bloms.de</code>) </p>
<dl>
<dt>
<dd> Multi-line configuration options</dl>
<p> Henning Moll (<code>newsScott [at] gmx.de</code>) </p>
<dl>
<dt>
<dd> stop_on_stale_lockfile</dl>
<p> Ben Low (<code>ben [at] bdlow.net</code>) </p>
<dl>
<dt>
<dd> Linux <font SIZE="-1">LVM</font> snapshot support</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003-2005 Nathan Rosenquist </p>
<p> Portions Copyright (C) 2002-2007 Mike Rubel, Carl Wilhelm Soderstrom, Ted Zlatanov, Carl Boe, Shane Liebling, Bharat Mediratta, Peter Palfrader, Nicolas Kaiser, David Cantrell, Chris Petersen, Robert Jackson, Justin Grote, David Keegel, Alan Batie, Dieter Bloms, Henning Moll, Ben Low, Anthony Ettinger </p>
<p> This man page is distributed under the same license as rsnapshot: the <font SIZE="-1">GPL </font>(see below). </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA</font> </p>
<h2>Index</h2>
