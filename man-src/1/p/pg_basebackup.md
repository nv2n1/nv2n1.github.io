---
title: "pg_basebackup(1)"
name: "pg_basebackup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_basebackup/"
description: "pg_basebackup – take a base backup of a PostgreSQL cluster"
---

<h2 class="name">NAME</h2>
<p> pg_basebackup &#8211; take a base backup of a PostgreSQL cluster </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_basebackup</code> [<i>option</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>pg_basebackup is used to take base backups of a running PostgreSQL database cluster. These are taken without affecting other clients to the database, and can be used both for point-in-time recovery (see Section 24.3, &#8220;Continuous Archiving and Point-in-Time Recovery (PITR)&#8221;, in the documentation) and as the starting point for a log shipping or streaming replication standby servers (see Section 25.2, &#8220;Log-Shipping Standby Servers&#8221;, in the documentation). </p>
<p> pg_basebackup makes a binary copy of the database cluster files, while making sure the system is put in and out of backup mode automatically. Backups are always taken of the entire database cluster; it is not possible to back up individual databases or database objects. For individual database backups, a tool such as <code><a href="/docs/linux/man/1-pg_dump/">pg_dump</a></code>(1) must be used. </p>
<p> The backup is made over a regular PostgreSQL connection, and uses the replication protocol. The connection must be made with a superuser or a user having REPLICATION permissions (see Section 20.2, &#8220;Role Attributes&#8221;, in the documentation), and pg_hba.conf must explicitly permit the replication connection. The server must also be configured with max_wal_senders set high enough to leave at least one session available for the backup. </p>
<p> There can be multiple <code>pg_basebackup</code>s running at the same time, but it is better from a performance point of view to take only one backup, and copy the result. </p>
<p> pg_basebackup can make a base backup from not only the master but also the standby. To take a backup from the standby, set up the standby so that it can accept replication connections (that is, set <i>max_wal_senders</i> and hot_standby, and configure host-based authentication). You will also need to enable full_page_writes on the master. </p>
<p> Note that there are some limitations in an online backup from the standby: </p>
<dl>
<dt>
<dd> &bull; The backup history file is not created in the database cluster backed up.</dl>
<dl>
<dt>
<dd> &bull; There is no guarantee that all WAL files required for the backup are archived at the end of backup. If you are planning to use the backup for an archive recovery and want to ensure that all required files are available at that moment, you need to include them into the backup by using -x option.</dl>
<dl>
<dt>
<dd> &bull; If the standby is promoted to the master during online backup, the backup fails.</dl>
<dl>
<dt>
<dd> &bull; All WAL records required for the backup must contain sufficient full-page writes, which requires you to enable <i>full_page_writes</i> on the master and not to use a tool like pg_compresslog as <i>archive_command</i> to remove full-page writes from WAL files.</dl>
<h2>OPTIONS</h2>
<p> The following command-line options control the location and format of the output. </p>
<p> <code>-D </code><i>directory</i>, <code>&#8211;pgdata=</code><i>directory</i></p>
<dl>
<dt>
<dd> Directory to write the output to. pg_basebackup will create the directory and any parent directories if necessary. The directory may already exist, but it is an error if the directory already exists and is not empty. </p>
<p> When the backup is in tar mode, and the directory is specified as &#8211; (dash), the tar file will be written to stdout. </p>
<p> This option is required.</dl>
<p> <code>-F </code><i>format</i>, <code>&#8211;format=</code><i>format</i></p>
<dl>
<dt>
<dd> Selects the format for the output. <i>format</i> can be one of the following: </p>
<p> p, plain</p>
<dl>
<dt>
<dd> Write the output as plain files, with the same layout as the current data directory and tablespaces. When the cluster has no additional tablespaces, the whole database will be placed in the target directory. If the cluster contains additional tablespaces, the main data directory will be placed in the target directory, but all other tablespaces will be placed in the same absolute path as they have on the server. </p>
<p> This is the default format.</dl>
<p> t, tar</p>
<dl>
<dt>
<dd> Write the output as tar files in the target directory. The main data directory will be written to a file named base.tar, and all other tablespaces will be named after the tablespace OID. </p>
<p> If the value &#8211; (dash) is specified as target directory, the tar contents will be written to standard output, suitable for piping to for example gzip. This is only possible if the cluster has no additional tablespaces.</dl>
</dl>
<p> <code>-x</code>, <code>&#8211;xlog</code></p>
<dl>
<dt>
<dd> Using this option is equivalent of using -X with method fetch.</dl>
<p> <code>-X </code><i>method</i>, <code>&#8211;xlog-method=</code><i>method</i></p>
<dl>
<dt>
<dd> Includes the required transaction log files (WAL files) in the backup. This will include all transaction logs generated during the backup. If this option is specified, it is possible to start a postmaster directly in the extracted directory without the need to consult the log archive, thus making this a completely standalone backup. </p>
<p> The following methods for collecting the transaction logs are supported: </p>
<p> f, fetch</p>
<dl>
<dt>
<dd> The transaction log files are collected at the end of the backup. Therefore, it is necessary for the wal_keep_segments parameter to be set high enough that the log is not removed before the end of the backup. If the log has been rotated when it&#8217;s time to transfer it, the backup will fail and be unusable.</dl>
<p> s, stream</p>
<dl>
<dt>
<dd> Stream the transaction log while the backup is created. This will open a second connection to the server and start streaming the transaction log in parallel while running the backup. Therefore, it will use up two slots configured by the max_wal_senders parameter. As long as the client can keep up with transaction log received, using this mode requires no extra transaction logs to be saved on the master.</dl>
</dl>
<p> <code>-z</code>, <code>&#8211;gzip</code></p>
<dl>
<dt>
<dd> Enables gzip compression of tar file output, with the default compression level. Compression is only available when using the tar format.</dl>
<p> <code>-Z </code><i>level</i>, <code>&#8211;compress=</code><i>level</i></p>
<dl>
<dt>
<dd> Enables gzip compression of tar file output, and specifies the compression level (0 through 9, 0 being no compression and 9 being best compression). Compression is only available when using the tar format.</dl>
<p> The following command-line options control the generation of the backup and the running of the program. </p>
<p> <code>-c </code><i>fast|spread</i>, <code>&#8211;checkpoint=</code><i>fast|spread</i></p>
<dl>
<dt>
<dd> Sets checkpoint mode to fast or spread (default).</dl>
<p> <code>-l </code><i>label</i>, <code>&#8211;label=</code><i>label</i></p>
<dl>
<dt>
<dd> Sets the label for the backup. If none is specified, a default value of &#8220;pg_basebackup base backup&#8221; will be used.</dl>
<p> <code>-P</code>, <code>&#8211;progress</code></p>
<dl>
<dt>
<dd> Enables progress reporting. Turning this on will deliver an approximate progress report during the backup. Since the database may change during the backup, this is only an approximation and may not end at exactly 100%. In particular, when WAL log is included in the backup, the total amount of data cannot be estimated in advance, and in this case the estimated target size will increase once it passes the total estimate without WAL. </p>
<p> When this is enabled, the backup will start by enumerating the size of the entire database, and then go back and send the actual contents. This may make the backup take slightly longer, and in particular it will take longer before the first data is sent.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Enables verbose mode. Will output some extra steps during startup and shutdown, as well as show the exact file name that is currently being processed if progress reporting is also enabled.</dl>
<p> The following command-line options control the database connection parameters. </p>
<p> <code>-h </code><i>host</i>, <code>&#8211;host=</code><i>host</i></p>
<dl>
<dt>
<dd> Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket. The default is taken from the <code>PGHOST</code> environment variable, if set, else a Unix domain socket connection is attempted.</dl>
<p> <code>-p </code><i>port</i>, <code>&#8211;port=</code><i>port</i></p>
<dl>
<dt>
<dd> Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections. Defaults to the <code>PGPORT</code> environment variable, if set, or a compiled-in default.</dl>
<p> <code>-s </code><i>interval</i>, <code>&#8211;status-interval=</code><i>interval</i></p>
<dl>
<dt>
<dd> Specifies the number of seconds between status packets sent back to the server. This is required when streaming the transaction log (using &#8211;xlog=stream) if replication timeout is configured on the server, and allows for easier monitoring. A value of zero disables the status updates completely. The default value is 10 seconds.</dl>
<p> <code>-U </code><i>username</i>, <code>&#8211;username=</code><i>username</i></p>
<dl>
<dt>
<dd> User name to connect as.</dl>
<p> <code>-w</code>, <code>&#8211;no-password</code></p>
<dl>
<dt>
<dd> Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a .pgpass file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dl>
<p> <code>-W</code>, <code>&#8211;password</code></p>
<dl>
<dt>
<dd> Force pg_basebackup to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since pg_basebackup will automatically prompt for a password if the server demands password authentication. However, pg_basebackup will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<p> Other options are also available: </p>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the pg_basebackup version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_basebackup command line arguments, and exit.</dl>
<h2>ENVIRONMENT</h2>
<p> This utility, like most other PostgreSQL utilities, uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>NOTES</h2>
<p> The backup will include all files in the data directory and tablespaces, including the configuration files and any additional files placed in the directory by third parties. Only regular files and directories are allowed in the data directory, no symbolic links or special device files. </p>
<p> The way PostgreSQL manages tablespaces, the path for all additional tablespaces must be identical whenever a backup is restored. The main data directory, however, is relocatable to any location.</p>
<h2>EXAMPLES</h2>
<p> To create a base backup of the server at mydbserver and store it in the local directory /usr/local/pgsql/data: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_basebackup -h mydbserver -D /usr/local/pgsql/data</code>
</pre>
</dl>
<p> To create a backup of the local server with one compressed tar file for each tablespace, and store it in the directory backup, showing a progress report while running: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_basebackup -D backup -Ft -z -P</code>
</pre>
</dl>
<p> To create a backup of a single-tablespace local database and compress this with bzip2: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_basebackup -D - -Ft | bzip2 &gt; backup.tar.bz2</code>
</pre>
</dl>
<p> (This command will fail if there are multiple tablespaces in the database.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pg_dump/">pg_dump</a></code>(1) </p>
<h2>Index</h2>
