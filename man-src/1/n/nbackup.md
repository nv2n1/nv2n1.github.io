---
title: "nbackup(1)"
name: "nbackup"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nbackup/"
description: "nbackup – Physical backup manager for Firebird"
---

<h2 class="name">NAME</h2>
<p> nbackup &#8211; Physical backup manager for Firebird </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>nbackup</code> [<i>option</i>&#8230;] -l|-u|-f <i>database</i></p>
<dd>
<dt><code>nbackup</code> [<i>option</i>&#8230;] -b <i>level</i> <i>database</i> <i>file</i></p>
<dd>
<dt><code>nbackup</code> [<i>option</i>&#8230;] -r <i>database</i> <i>file0</i> [<i>file1</i>&#8230;]</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>nbackup</code> allows making incremental backups of firebird databases. It also allows database files to be locked for copying with <font SIZE="-1">OS</font> tools like <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1).</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-l</code> <i>database</i></p>
<dd>
<dt><code>-lock</code> <i>database</i></p>
<dd> Locks <i>database</i> for filesystem copy. </p>
<p> Options of the <code>-lock</code> command:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-s</code></p>
<dd>
<dt><code>-size</code></p>
<dd> Print database size (in database pages) after locking.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-un</code> <i>database</i></p>
<dd>
<dt><code>-unlock</code> <i>database</i></p>
<dd> Unlocks previously locked database.</p>
<dt><code>-f</code> <i>database</i></p>
<dd>
<dt><code>-fixup</code> <i>database</i></p>
<dd> Fixup <i>database</i> after filesystem copy. This needs to be done on the target database before usage.</p>
<dt><code>-b</code> <i>level</i> <i>database</i> <i>file</i></p>
<dd>
<dt><code>-backup</code> <i>level</i> <i>database</i> <i>file</i></p>
<dd> Create incremental backup of level <i>level</i>. Level 0 means full backup. Level <i>N</i> includes all the changes since the last backup of level <i>N</i>. <i>file</i> may be <tt>&quot;stdout&quot;</tt> meaning to write the backup data to the standard output. </p>
<p> Additional options to the <code>-backup</code> command:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-d</code> <i>on|off</i></p>
<dd>
<dt><code>-direct</code> <i>on|off</i></p>
<dd> Turns on or off direct I/O during database backup. </p>
<p> Direct I/O may be useful when database is much larger that <font SIZE="-1">RAM,</font> because in that case using buffered I/O may cause replacing useful cache contents with database file contents, which are generally read only once.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-r</code> <i>database</i> <i>file0</i> [<i>file1</i>&#8230;]</p>
<dd>
<dt><code>-restore</code> <i>database</i> <i>file0</i> [<i>file1</i>&#8230;]</p>
<dd> Restore incremental backup. <i>file0</i> is the level 0 backup, <i>file1</i> is the level 1 backup and so on. </p>
<p> Additional <code>-restore</code> options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-de</code> <i>command</i></p>
<dd>
<dt><code>-decompress</code> <i>command</i></p>
<dd> Decompress backup file contents using the given <i>command</i>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>Note:</code> <code>-restore</code> should be the last argument to <code>nbackup</code> followed only by database and file names. All other options must precede <code>-restore</code> or will be interpreted as backup file names.</dl>
</dl>
<h2>COMMON OPTIONS</h2>
<dl>
<dt><code>-u</code> <i>user</i></p>
<dd>
<dt><code>-user</code> <i>user</i></p>
<dd> User name for connecting to the firebird server.</p>
<dt><code>-p</code> <i>password</i></p>
<dd>
<dt><code>-password</code> <i>password</i></p>
<dd> Password for connecting to the firebird server.</p>
<dt><code>-fetch_password</code> <i>file</i></p>
<dd> Read password from specified <i>file</i>.</p>
<dt><code>-nod</code></p>
<dd>
<dt><code>-nodbtriggers</code></p>
<dd> Do not run database-level triggers.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gbak/">gbak</a></code>(1) </p>
<p> Additional documentation about <code>nbackup</code> and other Firebird utilities can be found on the Firebird Project website, &lt;<a rel="nofollow" href="http://www.firebirdsql.org">http://www.firebirdsql.org</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Original idea is of Sean Leyne sean [at] broadviewsoftware.com. Designed and implemented by Nickolay Samofatov skidder [at] bssys.com. This work was funded through a grant from BroadView Software, Inc. </p>
<p> This manual page was written by Damyan Ivanov dmn [at] debian.org for the Debian project. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
<h2>Index</h2>
