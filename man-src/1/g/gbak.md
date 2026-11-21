---

title: "gbak(1)"
name: "gbak"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gbak/"
description: "gbak — backup /restore Firebird database"
---

<p> gbak &#8212; backup /restore Firebird database </p>
<h2>SYNOPSIS</h2>
<p> <code>gbak</code> -b [<i>backup option</i>&#8230;] [<i>common option</i>&#8230;] <i>source</i> <i>target</i> </p>
<p> <code>gbak</code> -c|-r [<i>restore option</i>&#8230;] [<i>common option</i>&#8230;] <i>source</i> <i>target</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gbak</code> is the tool for managing Firebird database logical backup and restore. </p>
<p> In backup mode <i>source</i> is the path to an existing database and <i>target</i> is the backup file name. If <i>target</i> is <tt>&quot;stdout&quot;</tt>, the backup is sent to the standard output. </p>
<p> In restore mode <i>source</i> is an existing backup file and <i>target</i> is the path to a firebird database. If <i>source</i> is <tt>&quot;stdin&quot;</tt>, the backup data is expected on the standard input.</p>
<h2>COMMON OPTIONS</h2>
<p> Most options can be abbreviated. Below are given the shortest abbreviations as well as the full versions.</p>
<dl>
<dt><code>-user</code> <i>string</i></dt>
<dd> User name to use when connecting to the database.</dd>
<dt><code>-ro</code> <i>string</i></dt>
<dd>
</dd><dt><code>-role</code> <i>string</i></dt>
<dd> <font SIZE="-1">SQL</font> role to use when connecting to theh database.</dd>
<dt><code>-pas</code> <i>string</i></dt>
<dd>
</dd><dt><code>-password</code> <i>string</i></dt>
<dd> Password to use when connecting to the database.</dd>
<dt><code>-se</code></dt>
<dd>
</dd><dt><code>-service</code></dt>
<dd> Use services manager when talking to the database.</dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>-verify</code></dt>
<dd> Report each action. </dd>
<p> Displays verbose information about what metadata is being processed, what table is being backed up/restored and how many records are processed.</p>
<dt><code>-y</code> <i>string</i></dt>
<dd> Redirects status/error messages to the given path.</dd>
<dt><code>-z</code></dt>
<dd> Prints full program version number before doing anything else. Prints server and database version information after connecting to the database.</dd></dl>
<h2>BACKUP OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd>
</dd><dt><code>-backup_database</code></dt>
<dd> Turns on backup mode.</dd>
<dt><code>-co</code></dt>
<dd>
</dd><dt><code>-convert</code></dt>
<dd> Converts external tables into tables. </dd>
<p> Normally external tables are ignored during backup and restore. With the <code>-convert</code> option external tables are included in the backup as any other regular table. When such a backup is restored, these previously external tables are created as regular tables.</p>
<dt><code>-fa</code> <i>number</i></dt>
<dd>
</dd><dt><code>-factor</code> <i>number</i></dt>
<dd> Blocking factor. Output is written in block of <i>number</i> bytes. Useful when backing up to a tape.</dd>
<dt><code>-g</code></dt>
<dd>
</dd><dt><code>-garbage_collect</code></dt>
<dd> Inhibits garbage collection. </dd>
<p> Normally Firebird runs a garbage collector when reading through the tables. Since the backup process reads all the tables, this forces garbage collection of the whole database. Using this switch speeds up the backup process and also can help in some cases of backing up damaged databases.</p>
<dt><code>-ig</code></dt>
<dd>
</dd><dt><code>-ignore</code></dt>
<dd> Ignores records with bad checksums. </dd>
<p> This option should be used only when backing up damaged databases.</p>
<dt><code>-l</code></dt>
<dd>
</dd><dt><code>-limbo</code></dt>
<dd> Ignores transactions in limbo.</dd>
<dt><code>-m</code></dt>
<dd>
</dd><dt><code>-metadata_only</code></dt>
<dd> Backs up metadata only. No table content is included in the backup.</dd>
<dt><code>-nt</code></dt>
<dd> Uses non-transportable backup format. </dd>
<p> Non-transportable backups can be restored only on machines using the same byte order.</p>
<dt><code>-o</code></dt>
<dd>
</dd><dt><code>-old_descriptions</code></dt>
<dd> Saves old-style metadata descriptions.</dd></dl>
<h2>RESTORE OPTIONS</h2>
<dl>
<dt><code>-c</code></dt>
<dd>
</dd><dt><code>-create</code></dt>
<dd> Turns on restore mode. </dd>
<p> <i>target</i> database will be created and must not exist.</p>
<dt><code>-r</code> [<code>o</code>]</dt>
<dd>
</dd><dt><code>-recreate_database</code> [<code>overwrite</code>]</dt>
<dd> Like <code>-create_database</code>, but by adding <tt>&quot;overwrite&quot;</tt> any existing database is overwritten.</dd>
<dt><code>-rep</code></dt>
<dd>
</dd><dt><code>-replace_database</code></dt>
<dd> Turns on restore mode. Target database is overwritten if it exists.</dd>
<dt><code>-bu</code> <i>number</i></dt>
<dd>
</dd><dt><code>-buffers</code> <i>number</i></dt>
<dd> When creating target database, ignore information about database buffers stored in the backup and use specified number.</dd>
<dt><code>-e</code></dt>
<dd>
</dd><dt><code>-expand</code></dt>
<dd> Normally, Firebird uses <font SIZE="-1">RLE</font> compression for strings when storing them on disk. This option turns this compression off.</dd>
<dt><code>-i</code></dt>
<dd>
</dd><dt><code>-inactive</code></dt>
<dd> Restore indexes in inactive state. This can be used to restore a backup, containing data inconsistent with foreign key/unique constraints. </dd>
<p> Note that since version 3.0 gbak leaves any problematic indices in inactive state automatically.</p>
<dt><code>-k</code></dt>
<dd>
</dd><dt><code>-kill</code></dt>
<dd> Does not restore database shadow files.</dd>
<dt><code>-mo</code> <i>access</i></dt>
<dd>
</dd><dt><code>-mode</code> <i>access</i></dt>
<dd> Restores the database with given <i>access</i>. </dd>
<p> Valid values for <i>access</i> are <tt>&quot;read_only&quot;</tt> and <tt>&quot;read_write&quot;</tt>. The default is to restore the database with its original access mode.</p>
<dt><code>-n</code></dt>
<dd>
</dd><dt><code>-no_validity</code></dt>
<dd> Restores the database without its validity constraints. This includes foreign key, unique and check constraints. Useful for restoring a backup, containing inconsistent data.</dd>
<dt><code>-o</code></dt>
<dd>
</dd><dt><code>-one_at_a_time</code></dt>
<dd> Commits restoring transaction after each table.</dd>
<dt><code>-p</code> <i>number</i></dt>
<dd>
</dd><dt><code>-page_size</code> <i>number</i></dt>
<dd> Override page size stored in the backup. Valid values are 1024, 2048, 4096, 8192, 16384 and 32768.</dd>
<dt><code>-use_</code></dt>
<dd>
</dd><dt><code>-use_all_space</code></dt>
<dd> Normally, Fireburd reserves some space on each data page for further use. This reserved space is used for newly inserted data and for keeping older versions of the data. Having space reserved for this purpose &#8220;near&#8221; to the data speeds up modifications. If the database will be used mainly for read operations, specifying this option will save disk space.</dd>
<dt><code>-fix_fss_metadata</code> <i>string</i></dt>
<dd> When restoring metadata, in case it is not valid <font SIZE="-1">UTF8,</font> try to convert it from the specified character set. Useful when table descriptions are given in some national non-UTF8 encoding, which was possible with Firebird before version 2.5.</dd>
<dt><code>-fix_fss_data</code> <i>string</i></dt>
<dd> When restoring table data, in case a column defined with <font SIZE="-1">UNICODE_FSS</font> character set contains no valid <font SIZE="-1">UTF8</font> (which was possible with versions of Firebird prior to 2.5), try to convert the data from the specified character set.</dd></dl>
<h3><font SIZE="-1">RESTORING TO</font> MULTIPLE-FILE <font SIZE="-1">DATABASE</font></h3>
<p> When the <i>target</i> argument is in the form <i>file_1</i> <i>pages_1</i> &#8230; <i>file_N</i>, the restored database is written in several files with <i>file_i</i> not bigger than <i>pages_i</i> pages. This may be useful if the file system that holds the database file can&#8217;t handle files above certain size. </p>
<p> <code>Note 1</code>: the file size limit is in <code>pages</code>. </p>
<p> <code>Note 1</code>: there is no limit on the size of the last file.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>ISC_USER</code></font></dt>
<dd> Default value for the -user option.</dd>
<dt><font SIZE="-1"><code>ISC_ROLE</code></font></dt>
<dd> Default value for the -role option.</dd>
<dt><font SIZE="-1"><code>ISC_PASSWORD</code></font></dt>
<dd> Default value for the -password option.</dd></dl>
<h2>EXAMPLES</h2>
<h3>Backup a database into a compressed format</h3>
<p> gbak -b srv:/database.fdb stdout | gzip &gt; database.fbk.gz</p>
<h3>Restore a database from a compressed backup</h3>
<p> zcat database.fbk.gz | gbak -c stdin srv:/new-database.fdb</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-isql-fb/">isql-fb</a></code>(1), <code><a href="/docs/linux/man/1-gfix/">gfix</a></code>(1), <code><a href="/docs/linux/man/1-fbstat/">fbstat</a></code>(1). </p>
<p> Additional documentation about Firebird can be found on the Firebird Project website, &lt;<a rel="nofollow" href="http://www.firebirdsql.org">http://www.firebirdsql.org</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Damyan Ivanov dmn [at] debian.org for the Debian project. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
