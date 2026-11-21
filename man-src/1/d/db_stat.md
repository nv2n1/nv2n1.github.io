---

title: "db_stat(1)"
name: "db_stat"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_stat/"
description: "db5.3_stat – Display statistics for Berkeley DB environments"
---

<p> db5.3_stat &#8211; Display statistics for Berkeley DB environments </p>
<h2>SYNOPSIS</h2>
<p> <code>db5.3_stat</code> -d file [-fN] [-h home] [-P password] [-s database] </p>
<p> <code>db5.3_stat</code> [-cEelmNrtVZ] [-C Aclop] [-h home] [-L A] [-M A] [-R A] [-P password]</p>
<h2>DESCRIPTION</h2>
<p> The db5.3_stat utility displays statistics for Berkeley DB environments.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code></dt>
<dd> Display internal information about the locking subsystem. (The output from this option is often both voluminous and meaningless, and is intended only for debugging.)</dd>
<dl>
<dl>
<dt>A</dt>
<dd> Display all information.</dd>
<dt>c</dt>
<dd> Display lock conflict matrix.</dd>
<dt>l</dt>
<dd> Display lockers within hash chains.</dd>
<dt>o</dt>
<dd> Display lock objects within hash chains.</dd>
<dt>p</dt>
<dd> Display locking subsystem parameters.</dd></dl>
</dl>
<dt><code>-c</code></dt>
<dd> Display locking subsystem statistics, as described in DB_ENV-&gt;lock_stat.</dd>
<dt><code>-d</code></dt>
<dd> Display database statistics for the specified file, as described in DB-&gt;stat. </dd>
<p> If the database contains multiple databases and the <code>-s</code> flag is not specified, the statistics are for the internal database that describes the other databases the file contains, and not for the file as a whole.</p>
<dt><code>-E</code></dt>
<dd> Display internal information about the database environment, including all configured subsystems of the database environment. (The output from this option is often both voluminous and meaningless, and is intended only for debugging.)</dd>
<dt><code>-e</code></dt>
<dd> Display information about the database environment, including all configured subsystems of the database environment.</dd>
<dt><code>-f</code></dt>
<dd> Display only those database statistics that can be acquired without traversing the database.</dd>
<dt><code>-h</code></dt>
<dd> Specify a home directory for the database environment; by default, the current working directory is used.</dd>
<dt><code>-l</code></dt>
<dd> Display logging subsystem statistics, as described in DB_ENV-&gt;log_stat.</dd>
<dt><code>-M</code></dt>
<dd> Display internal information about the cache. (The output from this option is often both voluminous and meaningless, and is intended only for debugging.)</dd>
<dl>
<dl>
<dt>A</dt>
<dd> Display all information.</dd>
<dt>h</dt>
<dd> Display buffers within hash chains.</dd></dl>
</dl>
<dt><code>-m</code></dt>
<dd> Display cache statistics, as described in DB_ENV-&gt;memp_stat.</dd>
<dt><code>-N</code></dt>
<dd> Do not acquire shared region mutexes while running. Other problems, such as potentially fatal errors in Berkeley DB, will be ignored as well. This option is intended only for debugging errors, and should not be used under any other circumstances.</dd>
<dt><code>-P</code></dt>
<dd> Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</dd>
<dt><code>-R</code></dt>
<dd> Display internal information about the replication subsystem. (The output from this option is often both voluminous and meaningless, and is intended only for debugging.)</dd>
<dl>
<dl>
<dt>A</dt>
<dd> Display all information.</dd></dl>
</dl>
<dt><code>-r</code></dt>
<dd> Display replication statistics, as described in DB_ENV-&gt;rep_stat.</dd>
<dt><code>-s</code></dt>
<dd> Display statistics for the specified database contained in the file specified with the <code>-d</code> flag.</dd>
<dt><code>-t</code></dt>
<dd> Display transaction subsystem statistics, as described in DB_ENV-&gt;txn_stat.</dd>
<dt><code>-V</code></dt>
<dd> Write the library version number to the standard output, and exit.</dd>
<dt><code>-Z</code></dt>
<dd> Reset the statistics after reporting them; valid only with the <code>-C</code>, <code>-c</code>, <code>-E</code>, <code>-e</code>, <code>-L</code>, <code>-l</code>, <code>-M</code>, <code>-m</code>, <code>-R</code>, <code>-r</code>, and <code>-t</code> options.</dd></dl>
<p> Values normally displayed in quantities of bytes are displayed as a combination of gigabytes (GB), megabytes (MB), kilobytes (KB), and bytes (B). Otherwise, values smaller than 10 million are displayed without any special notation, and values larger than 10 million are displayed as a number followed by &quot;M&quot;. </p>
<p> The db5.3_stat utility may be used with a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_stat should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_stat to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The db5.3_stat utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DB_HOME</code></dt>
<dd> If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dd></dl>
<h2>AUTHORS</h2>
<p> Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_stat from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others). </p>
