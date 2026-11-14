---
title: "db5-3_checkpoint(1)"
name: "db5-3_checkpoint"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db5-3_checkpoint/"
description: "db5.3_checkpoint – Periodically checkpoint transactions"
---

<p>db5.3_checkpoint &#8211; Periodically checkpoint transactions </p>
<h2>Synopsis</h2>
<p><code>db5.3_checkpoint</code> [-1Vv] [-h home] [-k kbytes] [-L file] [-P password] [-p min]</p>
<h2>Description</h2>
<p>The db5.3_checkpoint utility is a daemon process that monitors the database log, and periodically calls DB_ENV-&gt;txn_checkpoint to checkpoint it.</p>
<h2>Options</h2>
<dl>
<dt><code>-1</code></p>
<dd>Checkpoint the log once, regardless of whether or not there has been activity since the last checkpoint and then exit.</p>
<dt><code>-h</code></p>
<dd>Specify a home directory for the database environment; by default, the current working directory is used.</p>
<dt><code>-k</code></p>
<dd>Checkpoint the database at least as often as every <code>kbytes</code> of log file are written.</p>
<dt><code>-L</code></p>
<dd>Log the execution of the db5.3_checkpoint utility to the specified file in the following format, where <i>###</i> is the process ID, and the date is the time the utility was started. </p>
<dt>db_checkpoint: ### Wed Jun 15 01:23:45 EDT 1995</p>
<dd>This file will be removed if the db5.3_checkpoint utility exits gracefully.</p>
<dt><code>-P</code></p>
<dd>Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-p</code></p>
<dd>Checkpoint the database at least every <code>min</code> minutes if there has been any activity since the last checkpoint.</p>
<dt><code>-V</code></p>
<dd>Write the library version number to the standard output, and exit.</p>
<dt><code>-v</code></p>
<dd>Write the time of each checkpoint attempt to the standard output.</dl>
<p> At least one of the <code>-1</code>, <code>-k</code>, and <code>-p</code> options must be specified. </p>
<p> The db5.3_checkpoint utility uses a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_checkpoint should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_checkpoint to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The db5.3_checkpoint utility does not attempt to create the Berkeley DB shared memory regions if they do not already exist. The application that creates the region should be started first, and once the region is created, the db5.3_checkpoint utility should be started. </p>
<p> The DB_ENV-&gt;txn_checkpoint method is the underlying method used by the db5.3_checkpoint utility. See the db_checkpoint utility source code for an example of using DB_ENV-&gt;txn_checkpoint in a IEEE/ANSI Std 1003.1 (POSIX) environment. </p>
<p> The db5.3_checkpoint utility exits 0 on success, and &gt;0 if an error occurs. </p>
<h2>Environment</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd>If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>Authors</h2>
<p>Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_checkpoint from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others).</p>
