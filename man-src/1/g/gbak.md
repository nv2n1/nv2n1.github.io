---
title: "gbak(1)"
name: "gbak"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gbak/"
description: "gbak — backup /restore Firebird database"
---

<h2 class="name">NAME</h2>
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
<dt><code>-user</code> <i>string</i></p>
<dd> User name to use when connecting to the database.</p>
<dt><code>-ro</code> <i>string</i></p>
<dd>
<dt><code>-role</code> <i>string</i></p>
<dd> <font SIZE="-1">SQL</font> role to use when connecting to theh database.</p>
<dt><code>-pas</code> <i>string</i></p>
<dd>
<dt><code>-password</code> <i>string</i></p>
<dd> Password to use when connecting to the database.</p>
<dt><code>-se</code></p>
<dd>
<dt><code>-service</code></p>
<dd> Use services manager when talking to the database.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>-verify</code></p>
<dd> Report each action. </p>
<p> Displays verbose information about what metadata is being processed, what table is being backed up/restored and how many records are processed.</p>
<dt><code>-y</code> <i>string</i></p>
<dd> Redirects status/error messages to the given path.</p>
<dt><code>-z</code></p>
<dd> Prints full program version number before doing anything else. Prints server and database version information after connecting to the database.</dl>
<h2>BACKUP OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd>
<dt><code>-backup_database</code></p>
<dd> Turns on backup mode.</p>
<dt><code>-co</code></p>
<dd>
<dt><code>-convert</code></p>
<dd> Converts external tables into tables. </p>
<p> Normally external tables are ignored during backup and restore. With the <code>-convert</code> option external tables are included in the backup as any other regular table. When such a backup is restored, these previously external tables are created as regular tables.</p>
<dt><code>-fa</code> <i>number</i></p>
<dd>
<dt><code>-factor</code> <i>number</i></p>
<dd> Blocking factor. Output is written in block of <i>number</i> bytes. Useful when backing up to a tape.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>-garbage_collect</code></p>
<dd> Inhibits garbage collection. </p>
<p> Normally Firebird runs a garbage collector when reading through the tables. Since the backup process reads all the tables, this forces garbage collection of the whole database. Using this switch speeds up the backup process and also can help in some cases of backing up damaged databases.</p>
<dt><code>-ig</code></p>
<dd>
<dt><code>-ignore</code></p>
<dd> Ignores records with bad checksums. </p>
<p> This option should be used only when backing up damaged databases.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>-limbo</code></p>
<dd> Ignores transactions in limbo.</p>
<dt><code>-m</code></p>
<dd>
<dt><code>-metadata_only</code></p>
<dd> Backs up metadata only. No table content is included in the backup.</p>
<dt><code>-nt</code></p>
<dd> Uses non-transportable backup format. </p>
<p> Non-transportable backups can be restored only on machines using the same byte order.</p>
<dt><code>-o</code></p>
<dd>
<dt><code>-old_descriptions</code></p>
<dd> Saves old-style metadata descriptions.</dl>
<h2>RESTORE OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd>
<dt><code>-create</code></p>
<dd> Turns on restore mode. </p>
<p> <i>target</i> database will be created and must not exist.</p>
<dt><code>-r</code> [<code>o</code>]</p>
<dd>
<dt><code>-recreate_database</code> [<code>overwrite</code>]</p>
<dd> Like <code>-create_database</code>, but by adding <tt>&quot;overwrite&quot;</tt> any existing database is overwritten.</p>
<dt><code>-rep</code></p>
<dd>
<dt><code>-replace_database</code></p>
<dd> Turns on restore mode. Target database is overwritten if it exists.</p>
<dt><code>-bu</code> <i>number</i></p>
<dd>
<dt><code>-buffers</code> <i>number</i></p>
<dd> When creating target database, ignore information about database buffers stored in the backup and use specified number.</p>
<dt><code>-e</code></p>
<dd>
<dt><code>-expand</code></p>
<dd> Normally, Firebird uses <font SIZE="-1">RLE</font> compression for strings when storing them on disk. This option turns this compression off.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>-inactive</code></p>
<dd> Restore indexes in inactive state. This can be used to restore a backup, containing data inconsistent with foreign key/unique constraints. </p>
<p> Note that since version 3.0 gbak leaves any problematic indices in inactive state automatically.</p>
<dt><code>-k</code></p>
<dd>
<dt><code>-kill</code></p>
<dd> Does not restore database shadow files.</p>
<dt><code>-mo</code> <i>access</i></p>
<dd>
<dt><code>-mode</code> <i>access</i></p>
<dd> Restores the database with given <i>access</i>. </p>
<p> Valid values for <i>access</i> are <tt>&quot;read_only&quot;</tt> and <tt>&quot;read_write&quot;</tt>. The default is to restore the database with its original access mode.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>-no_validity</code></p>
<dd> Restores the database without its validity constraints. This includes foreign key, unique and check constraints. Useful for restoring a backup, containing inconsistent data.</p>
<dt><code>-o</code></p>
<dd>
<dt><code>-one_at_a_time</code></p>
<dd> Commits restoring transaction after each table.</p>
<dt><code>-p</code> <i>number</i></p>
<dd>
<dt><code>-page_size</code> <i>number</i></p>
<dd> Override page size stored in the backup. Valid values are 1024, 2048, 4096, 8192, 16384 and 32768.</p>
<dt><code>-use_</code></p>
<dd>
<dt><code>-use_all_space</code></p>
<dd> Normally, Fireburd reserves some space on each data page for further use. This reserved space is used for newly inserted data and for keeping older versions of the data. Having space reserved for this purpose &#8220;near&#8221; to the data speeds up modifications. If the database will be used mainly for read operations, specifying this option will save disk space.</p>
<dt><code>-fix_fss_metadata</code> <i>string</i></p>
<dd> When restoring metadata, in case it is not valid <font SIZE="-1">UTF8,</font> try to convert it from the specified character set. Useful when table descriptions are given in some national non-UTF8 encoding, which was possible with Firebird before version 2.5.</p>
<dt><code>-fix_fss_data</code> <i>string</i></p>
<dd> When restoring table data, in case a column defined with <font SIZE="-1">UNICODE_FSS</font> character set contains no valid <font SIZE="-1">UTF8</font> (which was possible with versions of Firebird prior to 2.5), try to convert the data from the specified character set.</dl>
<h3><font SIZE="-1">RESTORING TO</font> MULTIPLE-FILE <font SIZE="-1">DATABASE</font></h3>
<p> When the <i>target</i> argument is in the form <i>file_1</i> <i>pages_1</i> &#8230; <i>file_N</i>, the restored database is written in several files with <i>file_i</i> not bigger than <i>pages_i</i> pages. This may be useful if the file system that holds the database file can&#8217;t handle files above certain size. </p>
<p> <code>Note 1</code>: the file size limit is in <code>pages</code>. </p>
<p> <code>Note 1</code>: there is no limit on the size of the last file.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>ISC_USER</code></font></p>
<dd> Default value for the -user option.</p>
<dt><font SIZE="-1"><code>ISC_ROLE</code></font></p>
<dd> Default value for the -role option.</p>
<dt><font SIZE="-1"><code>ISC_PASSWORD</code></font></p>
<dd> Default value for the -password option.</dl>
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
<h2>Index</h2>
<dt><a href="#lbAI">ENVIRONMENT</a></p>
<dd>
<dt><a href="#lbAJ">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAM">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAN">AUTHOR</a></p>
<dd></dl>
