---
title: "db5-3_archive(1)"
name: "db5-3_archive"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db5-3_archive/"
description: "db5.3_archive – Find unused log files for archiving purposes"
---

<p>db5.3_archive &#8211; Find unused log files for archiving purposes </p>
<h2>Synopsis</h2>
<p><code>db5.3_archive</code> [-adlsVv] [-h home] [-P password]</p>
<h2>Description</h2>
<p>The db5.3_archive utility writes the pathnames of log files that are no longer in use (for example, no longer involved in active transactions), to the standard output, one pathname per line. These log files should be written to backup media to provide for recovery in the case of catastrophic failure (which also requires a snapshot of the database files), but they may then be deleted from the system to reclaim disk space.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Write all pathnames as absolute pathnames, instead of relative to the database home directories.</p>
<dt><code>-d</code></p>
<dd>Remove log files that are no longer needed; no filenames are written. Automatic log file removal is likely to make catastrophic recovery impossible.</p>
<dt><code>-h</code></p>
<dd>Specify a home directory for the database environment; by default, the current working directory is used.</p>
<dt><code>-l</code></p>
<dd>Write out the pathnames of all the database log files, whether or not they are involved in active transactions.</p>
<dt><code>-P</code></p>
<dd>Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-s</code></p>
<dd>Write the pathnames of all the database files that need to be archived in order to recover the database from catastrophic failure. If any of the database files have not been accessed during the lifetime of the current log files, db5.3_archive will not include them in this output. </p>
<p> It is possible that some of the files to which the log refers have since been deleted from the system. In this case, db5.3_archive will ignore them. When db5.3_recover is run, any files to which the log refers that are not present during recovery are assumed to have been deleted and will not be recovered.</p>
<dt><code>-V</code></p>
<dd>Write the library version number to the standard output, and exit.</p>
<dt><code>-v</code></p>
<dd>Run in verbose mode, listing the checkpoints in the log files as they are reviewed.</dl>
<p> Log cursor handles (returned by the DB_ENV-&gt;log_cursor method) may have open file descriptors for log files in the database environment. Also, the Berkeley DB interfaces to the database environment logging subsystem (for example, DB_ENV-&gt;log_put and DB_TXN-&gt;abort) may allocate log cursors and have open file descriptors for log files as well. On operating systems where filesystem related system calls (for example, rename and unlink on Windows/NT) can fail if a process has an open file descriptor for the affected file, attempting to move or remove the log files listed by db5.3_archive may fail. All Berkeley DB internal use of log cursors operates on active log files only and furthermore, is short-lived in nature. So, an application seeing such a failure should be restructured to close any open log cursors it may have, and otherwise to retry the operation until it succeeds. (Although the latter is not likely to be necessary; it is hard to imagine a reason to move or rename a log file in which transactions are being logged or aborted.) </p>
<p> The db5.3_archive utility uses a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_archive should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_archive to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The DB_ENV-&gt;log_archive method is the underlying method used by the db5.3_archive utility. See the db5.3_archive utility source code for an example of using DB_ENV-&gt;log_archive in a IEEE/ANSI Std 1003.1 (POSIX) environment. </p>
<p> The db5.3_archive utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>Environment</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd>If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>Authors</h2>
<p>Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_archive from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others).</p>
