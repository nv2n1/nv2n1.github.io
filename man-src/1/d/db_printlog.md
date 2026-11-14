---
title: "db_printlog(1)"
name: "db_printlog"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_printlog/"
description: "db5.3_printlog – Dumps Berkeley DB log files in a human-readable format"
---

<h2 class="name">NAME</h2>
<p> db5.3_printlog &#8211; Dumps Berkeley DB log files in a human-readable format </p>
<h2>SYNOPSIS</h2>
<p> <code>db5.3_printlog</code> [-NrV] [-b start-LSN] [-e stop-LSN] [-h home] [-P password]</p>
<h2>DESCRIPTION</h2>
<p> The db5.3_printlog utility is a debugging utility that dumps Berkeley DB log files in a human-readable format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Display log records starting at log sequence number (LSN) <code>start-LSN</code>; <code>start-LSN</code> is specified as a file number, followed by a slash (/) character, followed by an offset number, with no intervening whitespace.</p>
<dt><code>-e</code></p>
<dd> Stop displaying log records at log sequence number (LSN) <code>stop-LSN</code>; <code>stop-LSN</code> is specified as a file number, followed by a slash (/) character, followed by an offset number, with no intervening whitespace.</p>
<dt><code>-h</code></p>
<dd> Specify a home directory for the database environment; by default, the current working directory is used.</p>
<dt><code>-N</code></p>
<dd> Do not acquire shared region mutexes while running. Other problems, such as potentially fatal errors in Berkeley DB, will be ignored as well. This option is intended only for debugging errors, and should not be used under any other circumstances.</p>
<dt><code>-P</code></p>
<dd> Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-r</code></p>
<dd> Read the log files in reverse order.</p>
<dt><code>-V</code></p>
<dd> Write the library version number to the standard output, and exit.</dl>
<p> The db5.3_printlog utility uses a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_printlog should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_printlog to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The db5.3_printlog utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd> If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>AUTHORS</h2>
<p> Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_printlog from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others). </p>
<h2>Index</h2>
