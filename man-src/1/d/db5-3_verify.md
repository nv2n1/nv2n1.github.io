---
title: "db5-3_verify(1)"
name: "db5-3_verify"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db5-3_verify/"
description: "db5.3_verify – Verifies the structure databases"
---

<p>db5.3_verify &#8211; Verifies the structure databases </p>
<h2>Synopsis</h2>
<p><code>db5.3_verify</code> [-NoqV] [-h home] [-P password] file &#8230;</p>
<h2>Description</h2>
<p>The db5.3_verify utility verifies the structure of one or more files and the databases they contain.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Specify a home directory for the database environment; by default, the current working directory is used.</p>
<dt><code>-o</code></p>
<dd>Skip the database checks for btree and duplicate sort order and for hashing. </p>
<p> If the file being verified contains databases with non-default comparison or hashing configurations, calling the db5.3_verify utility without the <code>-o</code> flag will usually return failure. The <code>-o</code> flag causes db5.3_verify to ignore database sort or hash ordering and allows db5.3_verify to be used on these files. To fully verify these files, verify them explicitly using the DB-&gt;verify method, after configuring the correct comparison or hashing functions.</p>
<dt><code>-N</code></p>
<dd>Do not acquire shared region mutexes while running. Other problems, such as potentially fatal errors in Berkeley DB, will be ignored as well. This option is intended only for debugging errors, and should not be used under any other circumstances.</p>
<dt><code>-P</code></p>
<dd>Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-q</code></p>
<dd>Suppress the printing of any error descriptions, simply exit success or failure.</p>
<dt><code>-V</code></p>
<dd>Write the library version number to the standard output, and exit.</dl>
<p> <code>The db5.3_verify utility does not perform any locking, even in Berkeley DB environments that are configured with a locking subsystem. As such, it should only be used on files that are not being modified by another thread of control.</code> </p>
<p> The db5.3_verify utility may be used with a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_verify should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_verify to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The db5.3_verify utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>Environment</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd>If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>Authors</h2>
<p>Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_verify from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others).</p>
