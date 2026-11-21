---

title: "nbackup(1)"
name: "nbackup"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nbackup/"
description: "nbackup – Physical backup manager for Firebird"
---

<dl>
<dt><code>nbackup</code> [<i>option</i>&#8230;] -l|-u|-f <i>database</i></dt>
<dd>
</dd><dt><code>nbackup</code> [<i>option</i>&#8230;] -b <i>level</i> <i>database</i> <i>file</i></dt>
<dd>
</dd><dt><code>nbackup</code> [<i>option</i>&#8230;] -r <i>database</i> <i>file0</i> [<i>file1</i>&#8230;]</dt>
<dd></dd></dl>
<p> <code>nbackup</code> allows making incremental backups of firebird databases. It also allows database files to be locked for copying with <font SIZE="-1">OS</font> tools like <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1).</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-l</code> <i>database</i></dt>
<dd>
</dd><dt><code>-lock</code> <i>database</i></dt>
<dd> Locks <i>database</i> for filesystem copy. </dd>
<p> Options of the <code>-lock</code> command:</p>
<dl>
<dl>
<dt><code>-s</code></dt>
<dd>
</dd><dt><code>-size</code></dt>
<dd> Print database size (in database pages) after locking.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-un</code> <i>database</i></dt>
<dd>
</dd><dt><code>-unlock</code> <i>database</i></dt>
<dd> Unlocks previously locked database.</dd>
<dt><code>-f</code> <i>database</i></dt>
<dd>
</dd><dt><code>-fixup</code> <i>database</i></dt>
<dd> Fixup <i>database</i> after filesystem copy. This needs to be done on the target database before usage.</dd>
<dt><code>-b</code> <i>level</i> <i>database</i> <i>file</i></dt>
<dd>
</dd><dt><code>-backup</code> <i>level</i> <i>database</i> <i>file</i></dt>
<dd> Create incremental backup of level <i>level</i>. Level 0 means full backup. Level <i>N</i> includes all the changes since the last backup of level <i>N</i>. <i>file</i> may be <tt>&quot;stdout&quot;</tt> meaning to write the backup data to the standard output. </dd>
<p> Additional options to the <code>-backup</code> command:</p>
<dl>
<dl>
<dt><code>-d</code> <i>on|off</i></dt>
<dd>
</dd><dt><code>-direct</code> <i>on|off</i></dt>
<dd> Turns on or off direct I/O during database backup. </dd>
<p> Direct I/O may be useful when database is much larger that <font SIZE="-1">RAM,</font> because in that case using buffered I/O may cause replacing useful cache contents with database file contents, which are generally read only once.</dl>
</dl>
<dl>
</dl>
<dt><code>-r</code> <i>database</i> <i>file0</i> [<i>file1</i>&#8230;]</dt>
<dd>
</dd><dt><code>-restore</code> <i>database</i> <i>file0</i> [<i>file1</i>&#8230;]</dt>
<dd> Restore incremental backup. <i>file0</i> is the level 0 backup, <i>file1</i> is the level 1 backup and so on. </dd>
<p> Additional <code>-restore</code> options:</p>
<dl>
<dl>
<dt><code>-de</code> <i>command</i></dt>
<dd>
</dd><dt><code>-decompress</code> <i>command</i></dt>
<dd> Decompress backup file contents using the given <i>command</i>.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <code>Note:</code> <code>-restore</code> should be the last argument to <code>nbackup</code> followed only by database and file names. All other options must precede <code>-restore</code> or will be interpreted as backup file names.</dd></dl>
</dl>
<h2>COMMON OPTIONS</h2>
<dl>
<dt><code>-u</code> <i>user</i></dt>
<dd>
</dd><dt><code>-user</code> <i>user</i></dt>
<dd> User name for connecting to the firebird server.</dd>
<dt><code>-p</code> <i>password</i></dt>
<dd>
</dd><dt><code>-password</code> <i>password</i></dt>
<dd> Password for connecting to the firebird server.</dd>
<dt><code>-fetch_password</code> <i>file</i></dt>
<dd> Read password from specified <i>file</i>.</dd>
<dt><code>-nod</code></dt>
<dd>
</dd><dt><code>-nodbtriggers</code></dt>
<dd> Do not run database-level triggers.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gbak/">gbak</a></code>(1) </p>
<p> Additional documentation about <code>nbackup</code> and other Firebird utilities can be found on the Firebird Project website, &lt;<a rel="nofollow" href="http://www.firebirdsql.org">http://www.firebirdsql.org</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Original idea is of Sean Leyne sean [at] broadviewsoftware.com. Designed and implemented by Nickolay Samofatov skidder [at] bssys.com. This work was funded through a grant from BroadView Software, Inc. </p>
<p> This manual page was written by Damyan Ivanov dmn [at] debian.org for the Debian project. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
