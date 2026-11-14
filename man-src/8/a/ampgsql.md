---
title: "ampgsql(8)"
name: "ampgsql"
section: "8"
letter: "a"
url: "/docs/linux/man/8-ampgsql/"
description: "ampgsql – Amanda Application to interface with PostgreSQL"
---

<p>ampgsql &#8211; Amanda Application to interface with PostgreSQL</p>
<h2>Description</h2>
<p>Ampgsql is an Amanda Application API script. It should not be run by users directly. It implements on-line backups of PostgreSQL databases in conjunction with WAL archiving.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Tablespaces are not currently supported. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 On versions of PostgreSQL earlier than 8.2, if the database is quiet during a full backup, then the backup may not complete until enough database activity takes place to trigger the archiving of the current WAL file. Consider adjusting the PG-MAX-WAL-WAIT property from its default (60s) to compensate. Note that you will need to increase <code>dtimeout</code> on the server accordingly. </p>
<h2>Operation</h2>
<p>This application implements the backup strategy described in <a rel="nofollow" href="http://www.postgresql.org/docs/current/static/continuous-archiving.html.">http://www.postgresql.org/docs/current/static/continuous-archiving.html.</a> For a level zero (full) backup, ampgsql: </p>
<dl>
<dd>&bull; execute PG_START_BACKUP()</dl>
<dl>
<dd>&bull; dump the data directory</dl>
<dl>
<dd>&bull; execute PG_STOP_BACKUP()</dl>
<dl>
<dd>&bull; wait for the final WAL file to be archived</dl>
<dl>
<dd>&bull; back up the required WAL files</dl>
<dl>
<dd>&bull; optionally delete WAL files that are no longer necessary</dl>
<p> The two dumps are made with GNU Tar, to data_dir.tar and archive_dir, respectively. They are then combined into a single tar file. </p>
<p> A level N backup creates a single tar file containing all WAL files since the previous level N-1 backup.</p>
<h2>Properties</h2>
<p>This section lists the <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) properties that control ampsql&#8217;s functionality. See <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) for information on application properties and how they are configured. </p>
<p> ARCHIVEDIR</p>
<dl>
<dd>Directory that WAL segment files are archived to, as specified by the archive_command in PosgreSQL&#8217;s postgresql.conf. The amanda user on the client must have at least read and execute permission on this directory, and preferably write. Without write permission, Amanda cannot clean up expired WAL and backup files.</dl>
<p> CLEANUPWAL</p>
<dl>
<dd>Whether or not to remove old WAL segment files during base backups. Defaults to yes.</dl>
<p> DB</p>
<dl>
<dd>Database to connect to. Defaults to &quot;template1&quot; (which exists by default).</dl>
<p> DIRECTORY</p>
<dl>
<dd>For restore command only, the data is recoved in that directory. Must be a unix path.</dl>
<p> GNUTAR-PATH</p>
<dl>
<dd>Path to the GNU tar executable. This option only has an effect during restore. The default is set when Amanda is built by the &#8211;with-gnutar configure option.</dl>
<p> HOST</p>
<dl>
<dd>Host to connect to. If it starts with &quot;/&quot; it will be interepreted as a directory that holds the socket file. PostgreSQL defaults to /tmp.</dl>
<p> MAX-WAL-WAIT</p>
<dl>
<dd>The maximum amount of time to wait for PG_STOP_BACKUP to archive a WAL file. In versions of PostgreSQL before 8.2, PG_STOP_BACKUP does not automatically archive the latest WAL file, so a quiet database may wait a very long time before archiving the WAL file. Default: 60 seconds. Set to 0 to wait forever.</dl>
<p> PASSFILE</p>
<dl>
<dd>Connect using the creditials in this file. Each line should have the format &quot;hostname:port:database:username:password&quot;. The permissions must permit it to be read only by the user, or the file will not be used. Only usable with Postgres 8.1 and up.</dl>
<p> PORT</p>
<dl>
<dd>The TCP port to connect to, or the suffix of the socket file. PostgreSQL defaults to 5432.</dl>
<p> PSQL-PATH</p>
<dl>
<dd>Path to the psql binary. If not specified, the PATH environment variable will be searched.</dl>
<p> STATEDIR</p>
<dl>
<dd>Directory for saving state about backups already made. The default is set when Amanda is built by the &#8211;with-gnutar-listdir configure option.</dl>
<p> TMPDIR</p>
<dl>
<dd>Directory to use for temporary files during the backup process. It should have enough space to store a complete copy of the database. The default is set when Amanda is built by the &#8211;with-tmpdir configure option.</dl>
<p> USER</p>
<dl>
<dd>User to connect as. It must be a superuser.</dl>
<h2>Client Properties</h2>
<p>Client properties are deprecated. All properties should be set in the dumptype. </p>
<p> This section lists the <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5) properties that control ampsql&#8217;s functionality. If a property is prefixed with the diskname and an underscore, then it will be used when that diskname is being backed up. For example, if the properties PG-DATADIR and foo-PG-DATADIR are set, the value of PG-DATADIR will be used when bar and baz are being backed up, but foo-PG-DATADIR will be used when foo is being backed up. Disknames are specified in the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5). </p>
<p> PG-ARCHIVEDIR</p>
<dl>
<dd>Directory that WAL segment files are archived to, as specified by the archive_command in PosgreSQL&#8217;s postgresql.conf. The amanda user on the client must have at least read and execute permission on this directory, and preferably write. Without write permission, Amanda cannot clean up expired WAL and backup files.</dl>
<p> PG-CLEANUPWAL</p>
<dl>
<dd>Whether or not to remove old WAL segment files during base backups. Defaults to yes.</dl>
<p> PG-DATADIR</p>
<dl>
<dd>Cluster data directory</dl>
<p> PG-DB</p>
<dl>
<dd>Database to connect to. Defaults to &quot;template1&quot; (which exists by default).</dl>
<p> PG-HOST</p>
<dl>
<dd>Host to connect to. If it starts with &quot;/&quot; it will be interepreted as a directory that holds the socket file. PostgreSQL defaults to /tmp.</dl>
<p> PG-MAX-WAL-WAIT</p>
<dl>
<dd>The maximum amount of time to wait for PG_STOP_BACKUP to archive a WAL file. In versions of PostgreSQL before 8.2, PG_STOP_BACKUP does not automatically archive the latest WAL file, so a quiet database may wait a very long time before archiving the WAL file. Default: 60 seconds. Set to 0 to wait forever.</dl>
<p> PG-PASSFILE</p>
<dl>
<dd>Connect using the creditials in this file. Each line should have the format &quot;hostname:port:database:username:password&quot;. The permissions must permit it to be read only by the user, or the file will not be used. Only usable with Postgres 8.1 and up.</dl>
<p> PG-PASSWORD</p>
<dl>
<dd>Password to use when connecting. Deprecated in favor of passfiles.</dl>
<p> PG-PORT</p>
<dl>
<dd>The TCP port to connect to, or the suffix of the socket file. PostgreSQL defaults to 5432.</dl>
<p> PG-USER</p>
<dl>
<dd>User to connect as. It must be a superuser.</dl>
<p> PSQL-PATH</p>
<dl>
<dd>Path to the psql binary. If not specified, the PATH environment variable will be searched.</dl>
<h2>Recovery</h2>
<p>Read the postgres documentation carefully before attempting a recovery. This section is only a rough guide to the process. </p>
<p> The data recovered from a postgres backup consists of a data tarball and one or more archive tarballs. The data contains the state of the database at the time the full backup was performed, and the archive tarballs contain postgres WAL files that must be re-run to generate a consistent state. </p>
<p> Ensure that the database server is shut down, and move the existing data directory aside. Untar the data tarball over this directory, and verify that ownership and permissions are correct. Untar all of the archive tarballs into a single directory &#8211; the archive directory. Create a recovery.conf in the data directory, owned by the proper user and with proper permissions. Add a <code>restore_command</code> to it, e.g., </p>
<pre>restore_command = 'cp /path/to/archive_dir/%f &quot;%p&quot;'</pre>
<p>Start the database server, and examine the logs to track the process of the recovery. When the recovery is complete, the server will transition into a running state, and will move the recovery.conf file aside so that it will not attempt a recovery on the next invocation.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Nikolas Coukouma</code> &lt;atrus [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
