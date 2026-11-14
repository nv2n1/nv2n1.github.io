---
title: "db5-3_hotbackup(1)"
name: "db5-3_hotbackup"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db5-3_hotbackup/"
description: "db5.3_hotbackup – Create \"hot backup\" or \"hot failover\" snapshots"
---

<p>db5.3_hotbackup &#8211; Create &quot;hot backup&quot; or &quot;hot failover&quot; snapshots </p>
<h2>Synopsis</h2>
<p><code>db5.3_hotbackup</code> [-cDuVv] [-d data_dir &#8230;] [-h home] [-l log_dir] [-P password] -b backup_dir</p>
<h2>Description</h2>
<p>The db5.3_hotbackup utility creates &quot;hot backup&quot; or &quot;hot failover&quot; snapshots of Berkeley DB database environments. </p>
<p> The db5.3_hotbackup utility performs the following steps:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>If the -c option is specified, checkpoint the source home database environment, and remove any unnecessary log files.</p>
<dt>2.</p>
<dd>If the target directory for the backup does not exist, it is created with mode read-write-execute for the owner. </p>
<p> If the target directory for the backup does exist and the -u option was specified, all log files in the target directory are removed; if the -u option was not specified, all files in the target directory are removed.</p>
<dt>3.</p>
<dd>If the -u option was not specified, copy application-specific files found in the database environment home directory, or any directory specified using the -d option, into the target directory for the backup.</p>
<dt>4.</p>
<dd>Copy all log files found in the directory specified by the -l option (or in the database environment home directory, if no -l option was specified), into the target directory for the backup.</p>
<dt>5.</p>
<dd>Perform catastrophic recovery on the hot backup.</p>
<dt>6.</p>
<dd>Remove any unnecessary log files from the hot backup.</dl>
</dl>
<p> The db5.3_hotbackup utility does not resolve pending transactions that are in the prepared state. Applications that use DB_TXN-&gt;prepare should specify DB_RECOVER_FATAL when opening the environment, and run DB_ENV-&gt;txn_recover to resolve any pending transactions, when failing over to the hot backup.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd>Specify the target directory for the backup.</p>
<dt><code>-c</code></p>
<dd>Before performing the snapshot, checkpoint the source database environment and remove any log files that are no longer required in that environment. <code>To avoid making catastrophic failure impossible, log file removal must be integrated with log file archival.</code></p>
<dt><code>-d</code></p>
<dd>Specify one or more source directories that contain databases; if none is specified, the database environment home directory will be searched for database files. As database files are copied into a single backup directory, files named the same, stored in different source directories, could overwrite each other when copied into the backup directory.</p>
<dt><code>-h</code></p>
<dd>Specify the source directory for the backup, that is, the database environment home directory.</p>
<dt><code>-l</code></p>
<dd>Specify a source directory that contains log files; if none is specified, the database environment home directory will be searched for log files.</p>
<dt><code>-P</code></p>
<dd>Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-u</code></p>
<dd>Update a pre-existing hot backup snapshot by copying in new log files. If the <code>-u</code> option is specified, no databases will be copied into the target directory.</p>
<dt><code>-V</code></p>
<dd>Write the library version number to the standard output, and exit.</p>
<dt><code>-v</code></p>
<dd>Run in verbose mode, listing operations as they are done.</p>
<dt><code>-D</code></p>
<dd>Use the data directories listed in the DB_CONFIG configuration file in the source directory. This option has three effects: First, if they do not already exist, the specified data directories will be created relative to the target directory (with mode read-write-execute owner). Second, all files in the source data directories will be copied to the target data directories. If the DB_CONFIG file specifies one or more absolute pathnames, files in those source directories will be copied to the top-level target directory. Third, the DB_CONFIG configuration file will be copied from the +source directory to the target directory, and subsequently used for configuration if recovery is run in the target directory.</dl>
<p> Care should be taken with the <code>-D</code> option and data directories which are named relative to the source directory but are not subdirectories (that is, the name includes the element &quot;..&quot;) Specifically, the constructed target directory names must be meaningful and distinct from the source directory names, otherwise running recovery in the target directory might corrupt the source data files. </p>
<p> <code>It is an error to use absolute pathnames for data directories or the log directory in this mode, as the DB_CONFIG configuration file copied into the target directory would then point at the source directories and running recovery would corrupt the source data files.</code> </p>
<p> The db5.3_hotbackup utility uses a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_hotbackup should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_hotbackup to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The db5.3_hotbackup utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>Environment</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd>If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>Authors</h2>
<p>Oracle Corporation. This manual page was created based on the HTML documentation for db_hotbackup from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others).</p>
