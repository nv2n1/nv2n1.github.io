---
title: "db5-3_stat(1)"
name: "db5-3_stat"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db5-3_stat/"
description: "db5.3_stat – Display statistics for Berkeley DB environments"
---

<p>db5.3_stat &#8211; Display statistics for Berkeley DB environments </p>
<h2>Synopsis</h2>
<p><code>db5.3_stat</code> -d file [-fN] [-h home] [-P password] [-s database] </p>
<p> <code>db5.3_stat</code> [-cEelmNrtVZ] [-C Aclop] [-h home] [-L A] [-M A] [-R A] [-P password]</p>
<h2>Description</h2>
<p>The db5.3_stat utility displays statistics for Berkeley DB environments.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code></p>
<dd>Display internal information about the locking subsystem. (The output from this option is often both voluminous and meaningless, and is intended only for debugging.)</p>
<dl>
<dd>
<dl>
<dt>A</p>
<dd>Display all information.</p>
<dt>c</p>
<dd>Display lock conflict matrix.</p>
<dt>l</p>
<dd>Display lockers within hash chains.</p>
<dt>o</p>
<dd>Display lock objects within hash chains.</p>
<dt>p</p>
<dd>Display locking subsystem parameters.</dl>
</dl>
<dt><code>-c</code></p>
<dd>Display locking subsystem statistics, as described in DB_ENV-&gt;lock_stat.</p>
<dt><code>-d</code></p>
<dd>Display database statistics for the specified file, as described in DB-&gt;stat. </p>
<p> If the database contains multiple databases and the <code>-s</code> flag is not specified, the statistics are for the internal database that describes the other databases the file contains, and not for the file as a whole.</p>
<dt><code>-E</code></p>
<dd>Display internal information about the database environment, including all configured subsystems of the database environment. (The output from this option is often both voluminous and meaningless, and is intended only for debugging.)</p>
<dt><code>-e</code></p>
<dd>Display information about the database environment, including all configured subsystems of the database environment.</p>
<dt><code>-f</code></p>
<dd>Display only those database statistics that can be acquired without traversing the database.</p>
<dt><code>-h</code></p>
<dd>Specify a home directory for the database environment; by default, the current working directory is used.</p>
<dt><code>-l</code></p>
<dd>Display logging subsystem statistics, as described in DB_ENV-&gt;log_stat.</p>
<dt><code>-M</code></p>
<dd>Display internal information about the cache. (The output from this option is often both voluminous and meaningless, and is intended only for debugging.)</p>
<dl>
<dd>
<dl>
<dt>A</p>
<dd>Display all information.</p>
<dt>h</p>
<dd>Display buffers within hash chains.</dl>
</dl>
<dt><code>-m</code></p>
<dd>Display cache statistics, as described in DB_ENV-&gt;memp_stat.</p>
<dt><code>-N</code></p>
<dd>Do not acquire shared region mutexes while running. Other problems, such as potentially fatal errors in Berkeley DB, will be ignored as well. This option is intended only for debugging errors, and should not be used under any other circumstances.</p>
<dt><code>-P</code></p>
<dd>Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-R</code></p>
<dd>Display internal information about the replication subsystem. (The output from this option is often both voluminous and meaningless, and is intended only for debugging.)</p>
<dl>
<dd>
<dl>
<dt>A</p>
<dd>Display all information.</dl>
</dl>
<dt><code>-r</code></p>
<dd>Display replication statistics, as described in DB_ENV-&gt;rep_stat.</p>
<dt><code>-s</code></p>
<dd>Display statistics for the specified database contained in the file specified with the <code>-d</code> flag.</p>
<dt><code>-t</code></p>
<dd>Display transaction subsystem statistics, as described in DB_ENV-&gt;txn_stat.</p>
<dt><code>-V</code></p>
<dd>Write the library version number to the standard output, and exit.</p>
<dt><code>-Z</code></p>
<dd>Reset the statistics after reporting them; valid only with the <code>-C</code>, <code>-c</code>, <code>-E</code>, <code>-e</code>, <code>-L</code>, <code>-l</code>, <code>-M</code>, <code>-m</code>, <code>-R</code>, <code>-r</code>, and <code>-t</code> options.</dl>
<p> Values normally displayed in quantities of bytes are displayed as a combination of gigabytes (GB), megabytes (MB), kilobytes (KB), and bytes (B). Otherwise, values smaller than 10 million are displayed without any special notation, and values larger than 10 million are displayed as a number followed by &quot;M&quot;. </p>
<p> The db5.3_stat utility may be used with a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_stat should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_stat to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The db5.3_stat utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>Environment</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd>If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>Authors</h2>
<p>Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_stat from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others).</p>
