---
title: "db5-3_deadlock(1)"
name: "db5-3_deadlock"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db5-3_deadlock/"
description: "db5.3_deadlock – Detect and abort deadlocks"
---

<p>db5.3_deadlock &#8211; Detect and abort deadlocks </p>
<h2>Synopsis</h2>
<p><code>db5.3_deadlock</code> [-Vv] [-a e | m | n | o | W | w | y] [-h home] [-L file] [-t sec.usec]</p>
<h2>Description</h2>
<p>The db5.3_deadlock utility traverses the database environment lock region, and aborts a lock request each time it detects a deadlock or a lock request that has timed out. By default, in the case of a deadlock, a random lock request is chosen to be aborted. </p>
<p> This utility should be run as a background daemon, or the underlying Berkeley DB deadlock detection interfaces should be called in some other way, whenever there are multiple threads or processes accessing a database and at least one of them is modifying it.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>When a deadlock is detected, abort the locker:</p>
<dl>
<dd>
<dl>
<dt>m</p>
<dd>with the most locks</p>
<dt>n</p>
<dd>with the fewest locks</p>
<dt>o</p>
<dd>with the oldest lock</p>
<dt>W</p>
<dd>with the most write locks</p>
<dt>w</p>
<dd>with the fewest write locks</p>
<dt>y</p>
<dd>with the youngest lock</dl>
</dl>
<dd>When lock or transaction timeouts have been specified:</p>
<dl>
<dd>
<dl>
<dt>e</p>
<dd>abort any lock request that has timed out</dl>
</dl>
<dt><code>-h</code></p>
<dd>Specify a home directory for the database environment; by default, the current working directory is used.</p>
<dt><code>-L</code></p>
<dd>Log the execution of the db5.3_deadlock utility to the specified file in the following format, where <i>###</i> is the process ID, and the date is the time the utility was started. </p>
<dt>db_deadlock: ### Wed Jun 15 01:23:45 EDT 1995</p>
<dd>This file will be removed if the db5.3_deadlock utility exits gracefully.</p>
<dt><code>-t</code></p>
<dd>Check the database environment every <code>sec</code> seconds plus <code>usec</code> microseconds to see if a process has been forced to wait for a lock; if one has, review the database environment lock structures.</p>
<dt><code>-V</code></p>
<dd>Write the library version number to the standard output, and exit.</p>
<dt><code>-v</code></p>
<dd>Run in verbose mode, generating messages each time the detector runs.</dl>
<p> If the <code>-t</code> option is not specified, db5.3_deadlock will run once and exit. </p>
<p> The db5.3_deadlock utility uses a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_deadlock should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_deadlock to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The db5.3_deadlock utility does not attempt to create the Berkeley DB shared memory regions if they do not already exist. The application which creates the region should be started first, and then, once the region is created, the db5.3_deadlock utility should be started. </p>
<p> The DB_ENV-&gt;lock_detect method is the underlying method used by the db_deadlock utility. See the db_deadlock utility source code for an example of using DB_ENV-&gt;lock_detect in a IEEE/ANSI Std 1003.1 (POSIX) environment. </p>
<p> The db5.3_deadlock utility exits 0 on success, and &gt;0 if an error occurs. </p>
<h2>Environment</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd>If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>Authors</h2>
<p>Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_deadlock from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others).</p>
