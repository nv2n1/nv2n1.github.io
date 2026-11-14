---
title: "safekeep-backup(5)"
name: "safekeep-backup"
section: "5"
letter: "s"
url: "/docs/linux/man/5-safekeep-backup/"
description: "safekeep.backup – Configuration file for a ‘"
---

<p>safekeep.backup &#8211; Configuration file for a &#8216;</p>
<p><a href="/docs/linux/man/1-safekeep/">safekeep</a>(1)&#8217; client</p>
<h2>Synopsis</h2>
<p>These files are usually placed in /etc/safekeep/backup.d/, or optionally in ~/.safekeep/backup.d/ for non-root users, to be picked up automatically by <i><a href="/docs/linux/man/1-safekeep/">safekeep</a>(1)</i>. They must have a .backup extension.</p>
<h2>Description</h2>
<p>Each configuration file controls the backup of a host. They are typically named after the hostname of the machine they control the backup for, and have a <i>.backup</i> extension (e.g. mailbox.backup). These files are written in XML. Virtually all elements and attributes are optional; if not present, <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) will provide reasonable, useful defaults. </p>
<p> The full set of supported elements and attributes looks as follows: </p>
<dl>
<dd>
<pre>&lt;backup id=&quot;my_workstation&quot; enabled=&quot;true&quot;&gt;
 &lt;!-- the client backup host, the user and keys for access --&gt;
 &lt;host name=&quot;myhost&quot; user=&quot;root&quot; nice=&quot;10&quot;
 key-ctrl=&quot;/home/jdoe/.ssh/backup_id_rsa&quot;
 key-data=&quot;/home/jdoe/.ssh/backup2_id_rsa&quot; /&gt;
 &lt;!-- rate limit bandwidth (kB/s) on a client basis --&gt;
 &lt;bandwidth overall=&quot;80&quot; download=&quot;50&quot; upload=&quot;50&quot; /&gt;
 &lt;!-- where to stored the data on the server, and for now long --&gt;
 &lt;repo path=&quot;./data&quot; retention=&quot;10D&quot; /&gt;
 &lt;!-- settings for database dump and for volume snapshot --&gt;
 &lt;setup&gt;
 &lt;!-- databases can be dumbed before the backup --&gt;
 &lt;dump type=&quot;postgres&quot; db=&quot;my_db&quot; dbuser=&quot;foobar&quot; options=&quot;--schema=public&quot;
 file=&quot;/var/backup/dumps/mydata&quot; cleanup=&quot;true&quot; /&gt;
 &lt;!-- what volume is to be snapshot, and the size of the snapshot --&gt;
 &lt;snapshot device=&quot;/path/to/volume&quot; size=&quot;500M&quot; /&gt;
 &lt;!-- location of a script to be executed at different stages of the run --&gt;
 &lt;script path=&quot;server:/path/to/script&quot; /&gt;
 &lt;/setup&gt;
 &lt;!-- data to be backup --&gt;
 &lt;data exclude-fifos=&quot;true&quot; exclude-sockets=&quot;true&quot;&gt;
 &lt;!-- each type of tag can be present more than one time --&gt;
 &lt;!-- if a database dump was created, it must be added in this section --&gt;
 &lt;include path=&quot;/home&quot;/&gt;
 &lt;exclude path=&quot;/home/guest&quot;/&gt;
 &lt;include glob=&quot;**/important/&quot;/&gt;
 &lt;exclude glob=&quot;/home/*/tmp&quot;/&gt;
 &lt;include regexp=&quot;.*\.ogg&quot;/&gt;
 &lt;exclude regexp=&quot;.*\.mp3&quot;/&gt;
 &lt;/data&gt;
&lt;/backup&gt;</pre>
</dl>
<h2>Parameters</h2>
<p>XML elements and attributes are referred to via XPath expressions: elements are separated by <i>/</i>, attributes are introduced by <i>@</i>: </p>
<p> /backup</p>
<dl>
<dd>The root element of the XML file. Mandatory.</dl>
<p> /backup/@id</p>
<dl>
<dd>This is the ID by which <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) will address this host. If specified it overrides the default value derived from the filename. Optional, defaults to the filename without the .backup extension. Use of the default value is <code>highly</code> recommended.</dl>
<p> /backup/@enabled</p>
<dl>
<dd>If specified and set to <i>false</i> or <i>0</i>, it disables this host. It is a nicer way to disable a host without renaming the file. Optional, defaults to <i>true</i>.</dl>
<p> /backup/host/@name</p>
<dl>
<dd>The name or IP address of the client. If you need to backup the box that the server is running from, you can set this to &quot;localhost&quot;. This is different from leaving it blank, as it will establish a SSH session and use the user specified by /backup/host/@user. Optional, defaults to local access.</dl>
<p> /backup/host/@port</p>
<dl>
<dd>The network port to use when connecting to the client. This must be a number and is passed to the network connection agent, usually SSH. Optional, default to not passing any port specification.</dl>
<p> /backup/host/@user</p>
<dl>
<dd>The user name to use when connecting to the client. This user must have read permissions for the files that will be backed up, so it most likely needs to be <i>root</i>. Optional, defaults to the value given by client.user in safekeep.conf.</dl>
<p> /backup/host/@nice</p>
<dl>
<dd>The nice adjustment for the client. This settings is normally not all that important, as most of the load rests on the server side. NB: if you change this value, you will have to re-deploy the auth keys. Optional, defaults to no nice level.</dl>
<p> /backup/host/@key-ctrl</p>
<dl>
<dd>This is the private key used to establish the SSH connection to the client for the control channel. Use of the default value is recommended. Optional, defaults to ~/.ssh/safekeep-server-ctrl-key.</dl>
<p> /backup/host/@key-data</p>
<dl>
<dd>This is the private key used to establish the SSH connection to the client for the data channel. Use of the default value is recommended. Optional, defaults to ~/.ssh/safekeep-server-data-key.</dl>
<p> /backup/bandwidth/@overall</p>
<dl>
<dd>This is the client bandwidth limit for both upload and download. It is an integer number of KB/s (see the NOTES section in <a href="/docs/linux/man/5-safekeep-conf/">safekeep.conf</a>(5) for more information). Optional, overrides bandwidth.overall in <a href="/docs/linux/man/5-safekeep-conf/">safekeep.conf</a>(5) if specified.</dl>
<p> /backup/bandwidth/@download</p>
<dl>
<dd>This is the client bandwidth limit for download (see /backup/bandwidth/@overall for more information). Optional, overrides /backup/bandwidth/@overall if specified.</dl>
<p> /backup/bandwidth/@upload</p>
<dl>
<dd>This is the client bandwidth limit for upload (see /backup/bandwidth/@overall for more information). Optional, overrides /backup/bandwidth/@overall if specified.</dl>
<p> /backup/repo/@path</p>
<dl>
<dd>The path under which the backups will be stored. Relative paths are based on the <i>base.dir</i> setting from the <i><a href="/docs/linux/man/5-safekeep-conf/">safekeep.conf</a>(5)</i>. Since the default value for <i>base.dir</i> is the user&#8217;s home directory, in a typical installation the data will be stored under /var/lib/safekeep/&lt;id&gt;/. If the directory does not exist, <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) will attempt to create it automatically. The backup will fail altogether if the directory can not be created. Optional, defaults to the client ID, see /backup/@id. Use of the default value is <code>highly</code> recommended. <code>NOTE</code>: if you must set this value explicitly, you must make sure that the path is not shared between different boxes; a shared repository path <i>will</i> result in data loss.</dl>
<p> /backup/repo/@retention</p>
<dl>
<dd>Specifies the duration for which the backup data will be retained. The incremental backup information in the destination directory that has been around longer than the retention time will be removed. The value specified by this attribute is an time interval: an integer followed by the character s, m, h, D, W, M, or Y, indicating seconds, minutes, hours, days, weeks, months, or years respectively, or a number of these concatenated. For example, 32m means 32 minutes, and 3W2D10h7s means 3 weeks, 2 days, 10 hours, and 7 seconds. In this context, a month means 30 days, a year is 365 days, and a day is always 86400 seconds. Note that backups of deleted files are covered by this operation. Thus if you deleted a file two weeks ago, backed up immediately afterward, and then ran <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) with a retention of <i>10D</i> today, no trace of that file would remain. Finally, file selection options don&#8217;t affect removal of incremental data. Optional, defaults to empty (unlimited retention).</dl>
<p> /backup/options/special-files/@include</p>
<dl>
<dd><code>NOTE: THIS OPTION HAS BEEN DEPRECATED.</code> See data attributes below. One of &quot;true&quot; or &quot;false&quot;. If &quot;true&quot;, the dump file will include all special files, including device files, fifo files and socket files. Optional, defaults to <i>false</i>. <code>NOTE</code>: Specification of no options is equivalent to false, but the inclusion of other options may cause the underlying backup defaults to be use.</dl>
<p> /backup/options/rdiff-backup/@append</p>
<dl>
<dd>Append the specified options to the current rdiff-backup run. This is planned to be specific to the current rdiff-backup, and different options will be made available for other backends.</dl>
<p> /backup/setup/@writable</p>
<dl>
<dd>A boolean (i.e. &quot;true&quot; or &quot;false&quot;) to set mount as writable or not, including snapshots and bind mounts. This is normally not required, and, if set, overrides the system default, but is overridden by a snapshot option. In general the system default is to create non-writable mount for both snapshots and bind mounts. Optional for a &lt;setup&gt; element.</dl>
<p> /backup/setup/dump/@type</p>
<dl>
<dd>One of &quot;postgres&quot; or &quot;mysql&quot;. Mandatory for a &lt;dump&gt; element.</dl>
<p> /backup/setup/dump/@db</p>
<dl>
<dd>Name of the database to dump. If not specified, it defaults to all databases maintained in the RDBMS specified by type. Optional, defaults to all databases.</dl>
<p> /backup/setup/dump/@save-db-name</p>
<dl>
<dd>Specify if CREATE DATABASE instructions are included in database dumps. If the option is not specified then the result defaults to what is natural for the default database dump function. If the option is &quot;true&quot; then CREATE DATABASE are added in all cases. If the option is &quot;false&quot; then no CREATE DATABASE statement is added. <code>NOTE</code>: For Postgres it is not possible to suppress the CREATE DATABASE statement when dumping all databases, i.e. no single database named, in which case this option is ignored. Optional, defaults to not set.</dl>
<p> /backup/setup/dump/@dbuser</p>
<dl>
<dd>Name of the database user to use while doing the dump. Optional, defaults to whatever the database determines based on the system user.</dl>
<p> /backup/setup/dump/@dbpasswd</p>
<dl>
<dd>Password of the database user to use while doing the dump. NB: this makes the DB password available in a plain text file. Make sure you use appropriate read permissions on the backup configuration file to prevent unauthorized access to the password. Optional, it has no default value.</dl>
<p> /backup/setup/dump/@options</p>
<dl>
<dd>Extra options to be passed along to the dump command. This is database specific, and it is passed along as-is. Please refer to your database documentation for possible values that you can pass along. Optional, it has no default value.</dl>
<p> /backup/setup/dump/@user</p>
<dl>
<dd>The system user under which the dump should take place. Please note that using this feature requires that <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) runs as root on the client. Optional, defaults to the user under which <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) runs on the client side.</dl>
<p> /backup/setup/dump/@file</p>
<dl>
<dd>The full path to the dump file on the client host. Mandatory for a &lt;dump&gt; element.</dl>
<p> /backup/setup/dump/@cleanup</p>
<dl>
<dd>One of &quot;true&quot; or &quot;false&quot;. If &quot;true&quot;, the dump file will be deleted from the client system once the backup is over. It is usually futile to delete it, since it will be created for each backup, and hence you will need to have the space available. Optional, defaults to <i>false</i>.</dl>
<p> /backup/setup/snapshot/@device</p>
<dl>
<dd>The path (device location) to the client LVM volume to snapshot before the backup commences. Note that the snapshot happens on the client machines, and it ensures that the data that is being backed-up is in a consistent state throughout the backup process. Multiple snapshots may be specified, in which case the order is important, the associated filesystems are mounted in the order given. Please note that using this feature requires that <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) runs as root on the client. Mandatory for a &lt;snapshot&gt; element.</dl>
<p> /backup/setup/snapshot/@size</p>
<dl>
<dd>The size of the snapshot. Unallocated space must exist on the volume group. It is recommended that it is about 15-20% of the original device&#8217;s size. This can be specified as a percentage, e.g. 20%, which is equivalent to 20% of the logical volume. Other values as listed for <a href="/docs/linux/man/8-lvcreate/">lvcreate</a>(8) can also be given. Optional, defaults to <i>snapshot.size</i> as specified in safekeep.conf.</dl>
<p> /backup/setup/snapshot/@tag</p>
<dl>
<dd>A list of tags to be added to the snapshot, with the &#8211;addtag argument to <a href="/docs/linux/man/8-lvcreate/">lvcreate</a>(8). The @tag entry consists of a , separated list of tags. An @ is automatically added to each generated tag. Optional for a &lt;snapshot&gt; element.</dl>
<p> /backup/setup/snapshot/@mountoptions</p>
<dl>
<dd>Mount options to be used with the snapshot device. This is normally not required, as the default options should suit routine usage. Optional for a &lt;snapshot&gt; element.</dl>
<p> /backup/setup/snapshot/@writable</p>
<dl>
<dd>A boolean (i.e. &quot;true&quot; or &quot;false&quot;) to set if snapshot mount is writable or not. This is normally not required, and, if set, overrides other settings from the setup option or the system default. Optional for a &lt;snapshot&gt; element.</dl>
<p> /backup/setup/script/@path</p>
<dl>
<dd>Execute the script specified path on the client or server at certain steps of the backup process. This script is executed with four arguments: </p>
<dl>
<dd>&bull; Backup id (/backup/@id)</dl>
<dl>
<dd>&bull; Backup step</dl>
<dl>
<dd>&bull; Backup root directory (valid after creation of a snapshot) for client or safekeep backup directory for server</dl>
<dl>
<dd>&bull; Run-on parameter, i.e. <i>client</i> or <i>server</i> For client-side scripts, the location optionally consists of an optional host and a mandatory path, separated by a &quot;:&quot;, where the host part is either &quot;client&quot; or &quot;server&quot;. If no host part is specified then it is first looked for on the client, and if not found, then is looked for on the server. If it not found on either, then a warning is raised. Only one &lt;script&gt; element may be specified. See the CLIENT AND SERVER SCRIPTS section for more information. Mandatory for a &lt;script&gt; element.</dl>
</dl>
<p> /backup/setup/script/@run-on</p>
<dl>
<dd>Execute the script on the &quot;server&quot; or the &quot;client&quot;. Optional, defaults to <i>client</i>.</dl>
<p> /backup/data/@exclude-devices</p>
<dl>
<dd>One of &quot;true&quot; or &quot;false&quot;. If &quot;true&quot;, the dump file will exclude all device files. Optional, defaults to <i>false</i>. <code>NOTE</code>: specification of no attributes is equivalent to false, but the inclusion of other options may cause the underlying backup defaults to be use.</dl>
<p> /backup/data/@exclude-fifos</p>
<dl>
<dd>One of &quot;true&quot; or &quot;false&quot;. If &quot;true&quot;, the dump file will exclude all fifos. Optional, defaults to <i>false</i>. <code>NOTE</code>: specification of no attributes is equivalent to false, but the inclusion of other options may cause the underlying backup defaults to be use.</dl>
<p> /backup/data/@exclude-sockets</p>
<dl>
<dd>One of &quot;true&quot; or &quot;false&quot;. If &quot;true&quot;, the dump file will exclude all sockets. Optional, defaults to <i>false</i>. <code>NOTE</code>: specification of no attribute is equivalent to false, but the inclusion of other options may cause the underlying backup defaults to be use.</dl>
<p> /backup/data/exclude/@path</p>
<dl>
<dd>Exclude the file or files matched by the path. If a directory is matched, then files under that directory will also be matched. See the FILE SELECTION section for more information.</dl>
<p> /backup/data/include/@path</p>
<dl>
<dd>Include the file or files matched by the path. If a directory is matched, then files under that directory will also be matched. See the FILE SELECTION section for more information.</dl>
<p> /backup/data/exclude/@glob</p>
<dl>
<dd>Exclude the file or files matched by the shell pattern. If a directory is matched, then files under that directory will also be matched. See the FILE SELECTION section for more information.</dl>
<p> /backup/data/include/@glob</p>
<dl>
<dd>Include the file or files matched by the shell pattern. If a directory is matched, then files under that directory will also be matched. See the FILE SELECTION section for more information.</dl>
<p> /backup/data/exclude/@regexp</p>
<dl>
<dd>Exclude the file or files matched by the regular expression. If a directory is matched, then files under that directory will also be matched. See the FILE SELECTION section for more information.</dl>
<p> /backup/data/include/@regexp</p>
<dl>
<dd>Include the file or files matched by the regular expression. If a directory is matched, then files under that directory will also be matched. See the FILE SELECTION section for more information.</dl>
<h2>File Selection</h2>
<p><a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) supports file selection options similar to <a href="/docs/linux/man/1-rdiff-backup/">rdiff-backup</a>(1). When rdiff-backup is run, it searches through the given source directory and backs up all the files specified by the file selection system. </p>
<p> The file selection system comprises a number of file selection conditions, which are set using one of the &lt;include&gt;/&lt;exclude&gt; elements. Each file selection condition either matches or doesn&#8217;t match a given file. A given file is included or excluded by the file selection system when the first matching file selection condition specifies that the file be included or excluded respectively; if the file matches no include or exclude statement, it is by default excluded. </p>
<p> When backing up, if a file is excluded, <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) acts as if that file does not exist in the source directory. </p>
<p> For more information on file selection semantics, please see <a href="/docs/linux/man/1-rdiff-backup/">rdiff-backup</a>(1).</p>
<h2>Client And Scripts</h2>
<p><a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) support the optional execution of a script or program on the client or server systems at different steps during execution of the backup. </p>
<p> Currently only a single script, either client-side or server-side can be specified for a client. </p>
<p> For client-side scripts the script may be located on either the server or the client. If it is located on the server, then the file is copied to the client into a temporary directory before execution. Note that this directory is located where ever the system normally creates temporary files, and it is possible that the execution of scripts are disallowed. In that case it is recommended that a client based script is used. In addition, the script is copied from the server on a line by line basis, and so it is not suitable to pass binary files. </p>
<p> For server-side scripts the script must be located on the server. </p>
<p> Note: specification of a script which does not exist is not considered an error, and is treated as the same as not specifying a script. However, if the specified path does match a file or directory, the security tests listed below will occur. </p>
<p> This script is executed with the following four arguments: </p>
<dl>
<dd>&bull; Safekeep step</dl>
<dl>
<dd>&bull; Backup id</dl>
<dl>
<dd>&bull; Backup root directory, which may be set during the creation of a snapshot for client or safekeep backup directory for server.</dl>
<dl>
<dd>&bull; Run-on parameter, i.e. <i>client</i> or <i>server</i></dl>
<p> For both client-side and server-side scripts, the steps currently defined and tokens passed, are: </p>
<dl>
<dd>&bull; STARTUP &#8211; prior to any execution, however, if it exits with a non-zero status this constitutes an error and the backup is aborted.</dl>
<dl>
<dd>&bull; PRE-SETUP &#8211; prior to running any setup steps being run. A non-zero status is considered a warning and execution continues.</dl>
<dl>
<dd>&bull; POST-SETUP &#8211; after setup, but prior to execution of backup. A non-zero status is considered a warning, and execution continues.</dl>
<dl>
<dd>&bull; POST-BACKUP &#8211; after execution of backup. A non-zero status is considered a warning, and execution continues.</dl>
<dl>
<dd>&bull; POST-SCRUB &#8211; after execution of a server cleanup step, normally only seen after a backup failure. A non-zero status is considered a warning, and execution continues.</dl>
<p> Due to security considerations, there are a number of checks made on this script prior to execution and failure of any of these steps will cause the backup for that client to be aborted. The following tests are applied prior to each execution of the script (i.e. multiple time per backup), in order: &#8211; script is a regular file, not a directory or special file, &#8211; script is executable by the user running on the client system, &#8211; script is owned by root or the user running on the client system, &#8211; script is NOT writable by any one except the script owner. </p>
<p> Note: no test is made on the ownership of the parent directory or any other directories.</p>
<h2>Files</h2>
<dl>
<dd>
<pre>/etc/safekeep/backup.d/
~/.safekeep/backup.d/</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-safekeep/">safekeep</a>(1), <a href="/docs/linux/man/5-safekeep-conf/">safekeep.conf</a>(5), <a href="/docs/linux/man/1-rdiff-backup/">rdiff-backup</a>(1), <a href="/docs/linux/man/8-lvcreate/">lvcreate</a>(8)</p>
<h2>Author</h2>
<p>This man page was originally written by Dimi Paun &lt;m[blue]<code>dimi [at] lattica.com</code>m[]<font SIZE="-2">[1]</font>&gt;.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>dimi [at] lattica.com</p>
<dl>
<dd>mailto:dimi [at] lattica.com</dl>
