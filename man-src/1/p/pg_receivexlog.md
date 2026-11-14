---
title: "pg_receivexlog(1)"
name: "pg_receivexlog"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_receivexlog/"
description: "pg_receivexlog – streams transaction logs from a PostgreSQL cluster"
---

<h2 class="name">NAME</h2>
<p> pg_receivexlog &#8211; streams transaction logs from a PostgreSQL cluster </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_receivexlog</code> [<i>option</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>pg_receivexlog is used to stream transaction log from a running PostgreSQL cluster. The transaction log is streamed using the streaming replication protocol, and is written to a local directory of files. This directory can be used as the archive location for doing a restore using point-in-time recovery (see Section 24.3, &#8220;Continuous Archiving and Point-in-Time Recovery (PITR)&#8221;, in the documentation). </p>
<p> pg_receivexlog streams the transaction log in real time as it&#8217;s being generated on the server, and does not wait for segments to complete like archive_command does. For this reason, it is not necessary to set archive_timeout when using pg_receivexlog. </p>
<p> The transaction log is streamed over a regular PostgreSQL connection, and uses the replication protocol. The connection must be made with a superuser or a user having REPLICATION permissions (see Section 20.2, &#8220;Role Attributes&#8221;, in the documentation), and pg_hba.conf must explicitly permit the replication connection. The server must also be configured with max_wal_senders set high enough to leave at least one session available for the stream. </p>
<p> If the connection is lost, or if it cannot be initially established, with a non-fatal error, pg_receivexlog will retry the connection indefinitely, and reestablish streaming as soon as possible. To avoid this behavior, use the -n parameter.</p>
<h2>OPTIONS</h2>
<p> The following command-line options control the location and format of the output. </p>
<p> <code>-D </code><i>directory</i>, <code>&#8211;directory=</code><i>directory</i></p>
<dl>
<dt>
<dd> Directory to write the output to. </p>
<p> This parameter is required.</dl>
<p> The following command-line options control the running of the program. </p>
<p> <code>-n</code>, <code>&#8211;no-loop</code></p>
<dl>
<dt>
<dd> Don&#8217;t loop on connection errors. Instead, exit right away with an error.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Enables verbose mode.</dl>
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
<dd> Specifies the number of seconds between status packets sent back to the server. This is required if replication timeout is configured on the server, and allows for easier monitoring. A value of zero disables the status updates completely. The default value is 10 seconds.</dl>
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
<dd> Force pg_receivexlog to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since pg_receivexlog will automatically prompt for a password if the server demands password authentication. However, pg_receivexlog will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<p> Other options are also available: </p>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the pg_receivexlog version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_receivexlog command line arguments, and exit.</dl>
<h2>ENVIRONMENT</h2>
<p> This utility, like most other PostgreSQL utilities, uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>NOTES</h2>
<p> When using pg_receivexlog instead of archive_command, the server will continue to recycle transaction log files even if the backups are not properly archived, since there is no command that fails. This can be worked around by having an archive_command that fails when the file has not been properly archived yet, for example: </p>
<dl>
<dt>
<dd>
<pre>
archive_command = 'sleep 5 &amp;&amp; test -f /mnt/server/archivedir/%f'
</pre>
</dl>
<p> The initial timeout is necessary because pg_receivexlog works using asynchronous replication and can therefore be slightly behind the master.</p>
<h2>EXAMPLES</h2>
<p> To stream the transaction log from the server at mydbserver and store it in the local directory /usr/local/pgsql/archive: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_receivexlog -h mydbserver -D /usr/local/pgsql/archive</code>
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pg_basebackup/">pg_basebackup</a></code>(1) </p>
<h2>Index</h2>
