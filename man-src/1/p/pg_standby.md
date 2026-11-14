---
title: "pg_standby(1)"
name: "pg_standby"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_standby/"
description: "pg_standby – supports the creation of a PostgreSQL warm standby server"
---

<h2 class="name">NAME</h2>
<p> pg_standby &#8211; supports the creation of a PostgreSQL warm standby server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_standby</code> [<i>option</i>&#8230;] <i>archivelocation</i> <i>nextwalfile</i> <i>xlogfilepath</i> [<i>restartwalfile</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>pg_standby supports creation of a &#8220;warm standby&#8221; database server. It is designed to be a production-ready program, as well as a customizable template should you require specific modifications. </p>
<p> pg_standby is designed to be a waiting <i>restore_command</i>, which is needed to turn a standard archive recovery into a warm standby operation. Other configuration is required as well, all of which is described in the main server manual (see Section 25.2, &#8220;Log-Shipping Standby Servers&#8221;, in the documentation). </p>
<p> To configure a standby server to use pg_standby, put this into its recovery.conf configuration file: </p>
<dl>
<dt>
<dd>
<pre>
restore_command = 'pg_standby <i>archiveDir</i> %f %p %r'
</pre>
</dl>
<p> where <i>archiveDir</i> is the directory from which WAL segment files should be restored. </p>
<p> If <i>restartwalfile</i> is specified, normally by using the %r macro, then all WAL files logically preceding this file will be removed from <i>archivelocation</i>. This minimizes the number of files that need to be retained, while preserving crash-restart capability. Use of this parameter is appropriate if the <i>archivelocation</i> is a transient staging area for this particular standby server, but <i>not</i> when the <i>archivelocation</i> is intended as a long-term WAL archive area. </p>
<p> pg_standby assumes that <i>archivelocation</i> is a directory readable by the server-owning user. If <i>restartwalfile</i> (or -k) is specified, the <i>archivelocation</i> directory must be writable too. </p>
<p> There are two ways to fail over to a &#8220;warm standby&#8221; database server when the master server fails: </p>
<p> Smart Failover</p>
<dl>
<dt>
<dd> In smart failover, the server is brought up after applying all WAL files available in the archive. This results in zero data loss, even if the standby server has fallen behind, but if there is a lot of unapplied WAL it can be a long time before the standby server becomes ready. To trigger a smart failover, create a trigger file containing the word smart, or just create it and leave it empty.</dl>
<p> Fast Failover</p>
<dl>
<dt>
<dd> In fast failover, the server is brought up immediately. Any WAL files in the archive that have not yet been applied will be ignored, and all transactions in those files are lost. To trigger a fast failover, create a trigger file and write the word fast into it. pg_standby can also be configured to execute a fast failover automatically if no new WAL file appears within a defined interval.</dl>
<h2>OPTIONS</h2>
<p> pg_standby accepts the following command-line arguments: </p>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Use cp or copy command to restore WAL files from archive. This is the only supported behavior so this option is useless.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Print lots of debug logging output on stderr.</dl>
<p> <code>-k</code></p>
<dl>
<dt>
<dd> Remove files from <i>archivelocation</i> so that no more than this many WAL files before the current one are kept in the archive. Zero (the default) means not to remove any files from <i>archivelocation</i>. This parameter will be silently ignored if <i>restartwalfile</i> is specified, since that specification method is more accurate in determining the correct archive cut-off point. Use of this parameter is <i>deprecated</i> as of PostgreSQL 8.3; it is safer and more efficient to specify a <i>restartwalfile</i> parameter. A too small setting could result in removal of files that are still needed for a restart of the standby server, while a too large setting wastes archive space.</dl>
<p> <code>-r</code> <i>maxretries</i></p>
<dl>
<dt>
<dd> Set the maximum number of times to retry the copy command if it fails (default 3). After each failure, we wait for <i>sleeptime</i> * <i>num_retries</i> so that the wait time increases progressively. So by default, we will wait 5 secs, 10 secs, then 15 secs before reporting the failure back to the standby server. This will be interpreted as end of recovery and the standby will come up fully as a result.</dl>
<p> <code>-s</code> <i>sleeptime</i></p>
<dl>
<dt>
<dd> Set the number of seconds (up to 60, default 5) to sleep between tests to see if the WAL file to be restored is available in the archive yet. The default setting is not necessarily recommended; consult Section 25.2, &#8220;Log-Shipping Standby Servers&#8221;, in the documentation for discussion.</dl>
<p> <code>-t</code> <i>triggerfile</i></p>
<dl>
<dt>
<dd> Specify a trigger file whose presence should cause failover. It is recommended that you use a structured file name to avoid confusion as to which server is being triggered when multiple servers exist on the same system; for example /tmp/pgsql.trigger.5432.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the pg_standby version and exit.</dl>
<p> <code>-w</code> <i>maxwaittime</i></p>
<dl>
<dt>
<dd> Set the maximum number of seconds to wait for the next WAL file, after which a fast failover will be performed. A setting of zero (the default) means wait forever. The default setting is not necessarily recommended; consult Section 25.2, &#8220;Log-Shipping Standby Servers&#8221;, in the documentation for discussion.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_standby command line arguments, and exit.</dl>
<h2>NOTES</h2>
<p> pg_standby is designed to work with PostgreSQL 8.2 and later. </p>
<p> PostgreSQL 8.3 provides the %r macro, which is designed to let pg_standby know the last file it needs to keep. With PostgreSQL 8.2, the -k option must be used if archive cleanup is required. This option remains available in 8.3, but its use is deprecated. </p>
<p> PostgreSQL 8.4 provides the <i>recovery_end_command</i> option. Without this option a leftover trigger file can be hazardous. </p>
<p> pg_standby is written in C and has an easy-to-modify source code, with specifically designated sections to modify for your own needs</p>
<h2>EXAMPLES</h2>
<p> On Linux or Unix systems, you might use: </p>
<dl>
<dt>
<dd>
<pre>
archive_command = 'cp %p .../archive/%f'
restore_command = 'pg_standby -d -s 2 -t /tmp/pgsql.trigger.5442 .../archive %f %p %r 2&gt;&gt;standby.log'
recovery_end_command = 'rm -f /tmp/pgsql.trigger.5442'
</pre>
</dl>
<p> where the archive directory is physically located on the standby server, so that the <i>archive_command</i> is accessing it across NFS, but the files are local to the standby (enabling use of ln). This will: </p>
<dl>
<dt>
<dd> &bull; produce debugging output in standby.log</dl>
<dl>
<dt>
<dd> &bull; sleep for 2 seconds between checks for next WAL file availability</dl>
<dl>
<dt>
<dd> &bull; stop waiting only when a trigger file called /tmp/pgsql.trigger.5442 appears, and perform failover according to its content</dl>
<dl>
<dt>
<dd> &bull; remove the trigger file when recovery ends</dl>
<dl>
<dt>
<dd> &bull; remove no-longer-needed files from the archive directory</dl>
<p> On Windows, you might use: </p>
<dl>
<dt>
<dd>
<pre>
archive_command = 'copy %p ...\archive\%f'
restore_command = 'pg_standby -d -s 5 -t C:\pgsql.trigger.5442 ...rchive %f %p %r 2&gt;&gt;standby.log'
recovery_end_command = 'del C:\pgsql.trigger.5442'
</pre>
</dl>
<p> Note that backslashes need to be doubled in the <i>archive_command</i>, but <i>not</i> in the <i>restore_command</i> or <i>recovery_end_command</i>. This will: </p>
<dl>
<dt>
<dd> &bull; use the copy command to restore WAL files from archive</dl>
<dl>
<dt>
<dd> &bull; produce debugging output in standby.log</dl>
<dl>
<dt>
<dd> &bull; sleep for 5 seconds between checks for next WAL file availability</dl>
<dl>
<dt>
<dd> &bull; stop waiting only when a trigger file called C:\pgsql.trigger.5442 appears, and perform failover according to its content</dl>
<dl>
<dt>
<dd> &bull; remove the trigger file when recovery ends</dl>
<dl>
<dt>
<dd> &bull; remove no-longer-needed files from the archive directory</dl>
<p> The copy command on Windows sets the final file size before the file is completely copied, which would ordinarily confuse pg_standby. Therefore pg_standby waits sleeptime seconds once it sees the proper file size. GNUWin32&#8217;s cp sets the file size only after the file copy is complete. </p>
<p> Since the Windows example uses copy at both ends, either or both servers might be accessing the archive directory across the network.</p>
<h2>AUTHOR</h2>
<p> Simon Riggs &lt;simon [at] 2ndquadrant.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pg_archivecleanup/">pg_archivecleanup</a></code>(1) </p>
<h2>Index</h2>
