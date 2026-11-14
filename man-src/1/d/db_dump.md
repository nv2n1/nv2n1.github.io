---
title: "db_dump(1)"
name: "db_dump"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_dump/"
description: "db5.3_dump – Write database to flat-text format"
---

<h2 class="name">NAME</h2>
<p> db5.3_dump &#8211; Write database to flat-text format </p>
<h2>SYNOPSIS</h2>
<p> <code>db5.3_dump</code> [-klNpRrV] [-d ahr] [-f output] [-h home] [-P password] [-s database] file</p>
<h2>DESCRIPTION</h2>
<p> The db5.3_dump utility reads the database file file and writes it to the standard output using a portable flat-text format understood by the db5.3_load utility. The file argument must be a file produced using the Berkeley DB library functions.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Dump the specified database in a format helpful for debugging the Berkeley DB library routines.</p>
<dl>
<dt>
<dd>
<dl>
<dt>a</p>
<dd> Display all information.</p>
<dt>h</p>
<dd> Display only page headers.</p>
<dt>r</p>
<dd> Do not display the free-list or pages on the free list. This mode is used by the recovery tests.</dl>
</dl>
<dt>
<dd> <code>The output format of the -d option is not standard and may change, without notice, between releases of the Berkeley DB library.</code></p>
<dt><code>-f</code></p>
<dd> Write to the specified <code>file</code> instead of to the standard output.</p>
<dt><code>-h</code></p>
<dd> Specify a home directory for the database environment; by default, the current working directory is used.</p>
<dt><code>-k</code></p>
<dd> Dump record numbers from Queue and Recno databases as keys.</p>
<dt><code>-l</code></p>
<dd> List the databases stored in the file.</p>
<dt><code>-N</code></p>
<dd> Do not acquire shared region mutexes while running. Other problems, such as potentially fatal errors in Berkeley DB, will be ignored as well. This option is intended only for debugging errors, and should not be used under any other circumstances.</p>
<dt><code>-P</code></p>
<dd> Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-p</code></p>
<dd> If characters in either the key or data items are printing characters (as defined by <code><a href="/docs/linux/man/3-isprint/">isprint</a></code>(3)), use printing characters in <code>file</code> to represent them. This option permits users to use standard text editors and tools to modify the contents of databases. </p>
<p> Note: different systems may have different notions about what characters are considered <i>printing characters</i>, and databases dumped in this manner may be less portable to external systems.</p>
<dt><code>-R</code></p>
<dd> Aggressively salvage data from a possibly corrupt file. The <code>-R</code> flag differs from the <code>-r</code> option in that it will return all possible data from the file at the risk of also returning already deleted or otherwise nonsensical items. Data dumped in this fashion will almost certainly have to be edited by hand or other means before the data is ready for reload into another database</p>
<dt><code>-r</code></p>
<dd> Salvage data from a possibly corrupt file. When used on a uncorrupted database, this option should return equivalent data to a normal dump, but most likely in a different order.</p>
<dt><code>-s</code></p>
<dd> Specify a single database to dump. If no database is specified, all databases in the database file are dumped.</p>
<dt><code>-V</code></p>
<dd> Write the library version number to the standard output, and exit.</dl>
<p> Dumping and reloading Hash databases that use user-defined hash functions will result in new databases that use the default hash function. Although using the default hash function may not be optimal for the new database, it will continue to work correctly. </p>
<p> Dumping and reloading Btree databases that use user-defined prefix or comparison functions will result in new databases that use the default prefix and comparison functions. <code>In this case, it is quite likely that the database will be damaged beyond repair permitting neither record storage or retrieval.</code> </p>
<p> The only available workaround for either case is to modify the sources for the db5.3_load utility to load the database using the correct hash, prefix, and comparison functions. </p>
<p> The db5.3_dump utility output format is documented in the Dump Output Formats section of the Berkeley DB Reference Guide. </p>
<p> The db5.3_dump utility may be used with a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_dump should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_dump to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> Even when using a Berkeley DB database environment, the db5.3_dump utility does not use any kind of database locking if it is invoked with the <code>-d</code>, <code>-R</code>, or <code>-r</code> arguments. If used with one of these arguments, the db5.3_dump utility may only be safely run on databases that are not being modified by any other process; otherwise, the output may be corrupt. </p>
<p> The db5.3_dump utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd> If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>AUTHORS</h2>
<p> Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_dump from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others). </p>
<h2>Index</h2>
