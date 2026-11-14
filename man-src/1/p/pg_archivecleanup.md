---
title: "pg_archivecleanup(1)"
name: "pg_archivecleanup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_archivecleanup/"
description: "pg_archivecleanup – clean up PostgreSQL WAL archive files"
---

<h2 class="name">NAME</h2>
<p> pg_archivecleanup &#8211; clean up PostgreSQL WAL archive files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_archivecleanup</code> [<i>option</i>&#8230;] <i>archivelocation</i> <i>oldestkeptwalfile</i></dl>
<h2>DESCRIPTION</h2>
<dd>pg_archivecleanup is designed to be used as an archive_cleanup_command to clean up WAL file archives when running as a standby server (see Section 25.2, &#8220;Log-Shipping Standby Servers&#8221;, in the documentation). pg_archivecleanup can also be used as a standalone program to clean WAL file archives. </p>
<p> To configure a standby server to use pg_archivecleanup, put this into its recovery.conf configuration file: </p>
<dl>
<dt>
<dd>
<pre>
archive_cleanup_command = 'pg_archivecleanup <i>archivelocation</i> %r'
</pre>
</dl>
<p> where <i>archivelocation</i> is the directory from which WAL segment files should be removed. </p>
<p> When used within archive_cleanup_command, all WAL files logically preceding the value of the %r argument will be removed from <i>archivelocation</i>. This minimizes the number of files that need to be retained, while preserving crash-restart capability. Use of this parameter is appropriate if the <i>archivelocation</i> is a transient staging area for this particular standby server, but <i>not</i> when the <i>archivelocation</i> is intended as a long-term WAL archive area, or when multiple standby servers are recovering from the same archive location. </p>
<p> When used as a standalone program all WAL files logically preceding the <i>oldestkeptwalfile</i> will be removed from <i>archivelocation</i>. In this mode, if you specify a .backup file name, then only the file prefix will be used as the <i>oldestkeptwalfile</i>. This allows you to remove all WAL files archived prior to a specific base backup without error. For example, the following example will remove all files older than WAL file name 000000010000003700000010: </p>
<dl>
<dt>
<dd>
<pre>
pg_archivecleanup -d archive 000000010000003700000010.00000020.backup
pg_archivecleanup:  keep WAL file &quot;archive/000000010000003700000010&quot; and later
pg_archivecleanup:  removing file &quot;archive/00000001000000370000000F&quot;
pg_archivecleanup:  removing file &quot;archive/00000001000000370000000E&quot;
</pre>
</dl>
<p> pg_archivecleanup assumes that <i>archivelocation</i> is a directory readable and writable by the server-owning user.</p>
<h2>OPTIONS</h2>
<p> pg_archivecleanup accepts the following command-line arguments: </p>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Print lots of debug logging output on stderr.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Print the names of the files that would have been removed on stdout (performs a dry run).</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the pg_archivecleanup version and exit.</dl>
<p> <code>-x</code> <i>extension</i></p>
<dl>
<dt>
<dd> When using the program as a standalone utility, provide an extension that will be stripped from all file names before deciding if they should be deleted. This is typically useful for cleaning up archives that have been compressed during storage, and therefore have had an extension added by the compression program. For example: -x .gz.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_archivecleanup command line arguments, and exit.</dl>
<h2>NOTES</h2>
<p> pg_archivecleanup is designed to work with PostgreSQL 8.0 and later when used as a standalone utility, or with PostgreSQL 9.0 and later when used as an archive cleanup command. </p>
<p> pg_archivecleanup is written in C and has an easy-to-modify source code, with specifically designated sections to modify for your own needs</p>
<h2>EXAMPLES</h2>
<p> On Linux or Unix systems, you might use: </p>
<dl>
<dt>
<dd>
<pre>
archive_cleanup_command = 'pg_archivecleanup -d /mnt/standby/archive %r 2&gt;&gt;cleanup.log'
</pre>
</dl>
<p> where the archive directory is physically located on the standby server, so that the <i>archive_command</i> is accessing it across NFS, but the files are local to the standby. This will: </p>
<dl>
<dt>
<dd> &bull; produce debugging output in cleanup.log</dl>
<dl>
<dt>
<dd> &bull; remove no-longer-needed files from the archive directory</dl>
<h2>AUTHOR</h2>
<p> Simon Riggs &lt;simon [at] 2ndquadrant.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pg_standby/">pg_standby</a></code>(1) </p>
<h2>Index</h2>
