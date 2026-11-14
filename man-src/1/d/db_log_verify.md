---
title: "db_log_verify(1)"
name: "db_log_verify"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_log_verify/"
description: "db_log_verify – Verify log files of a database environment"
---

<h2>NAME</h2>
<p> db_log_verify &#8211; Verify log files of a database environment</p>
<h2>SYNOPSIS</h2>
<p> <code>db_log_verify</code> [-cNvV] [-h <i>home-to-verify</i>] [-H <i>temporary-home</i>] [-P <i>password</i>] [-C <i>cache-size</i>] [-b <i>start-lsn</i>] [-e <i>end-lsn</i>] [-s <i>start-time</i>] [-z <i>end-time</i>] [-d <i>database-filename</i>] [-D <i>database-name</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>db_log_verify</code> utility verifies the log files of a specific database environment. This utility verifies a specific range of log records, or changed log records of a specific database.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code> <i>cache-size</i></p>
<dd> Specify the cache size (in megabytes) of the temporary database environment internally used during the log verification.</p>
<dt><code>-b</code> <i>start-lsn</i></p>
<dd> Specify the starting log record (by lsn) to verify.</p>
<dt><code>-c</code></p>
<dd> Specify whether to continue the verification after an error is detected. If not specified, the verification stops when the first error is detected.</p>
<dt><code>-D</code> <i>database-name</i></p>
<dd> Specify a database name. Only log records related to this database are verified.</p>
<dt><code>-d</code> <i>database-filename</i></p>
<dd> Specify a database file name. Only log records related this database file are verified.</p>
<dt><code>-e</code> <i>end-lsn</i></p>
<dd> Specify the ending log record by lsn.</p>
<dt><code>-h</code> <i>home-to-verify</i></p>
<dd> Specify a home directory of the database environment whose log is to be verified.</p>
<dt><code>-H</code> <i>temporary-home</i></p>
<dd> Specify a home directory for this utility to create a temporarily database environment to store runtime data during the verification. </p>
<p> It is an error to specify the same directory as the <code>-h</code> option. If this directory is not specified, all temporary databases created during the verification will be in-memory, which is not a problem if the log files to verify are not huge.</p>
<dt><code>-N</code></p>
<dd> Do not acquire shared region mutexes while running. Other problems, such as potentially fatal errors in Berkeley DB, are ignored as well. This option is intended only for debugging errors, and should not be used under any other circumstances.</p>
<dt><code>-P</code> <i>password</i></p>
<dd> Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-s</code> <i>start-time</i></p>
<dd> Specify the starting log record by time. The time range specified is not precise because the lsn of the most recent time point is used as the starting lsn.</p>
<dt><code>-V</code></p>
<dd> Write the library version number to the standard output and exit.</p>
<dt><code>-v</code></p>
<dd> Enable verbose mode to display verbose output during the verification process.</p>
<dt><code>-z</code> <i>end-time</i></p>
<dd> Specify the ending log record by time. The time range specified is not precise because the lsn of the most recent time point is used as the ending lsn.</dl>
<p> To specify a range of log records, you must provide either an lsn range or a time range. You can neither specify both nor specify an lsn and a time as a range. </p>
<p> If the log footprint is over several megabytes, specify a home directory and a big cache size for log verification internal use. Else, the process&#8217; private memory may be exhausted before the verification completes. </p>
<p> The <code>db_log_verify</code> utility does not perform the locking function, even in Berkeley DB environments that are configured with a locking subsystem. All errors are written to stderr, and all normal and verbose messages are written to stdout. </p>
<p> The <code>db_log_verify</code> utility uses a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, <code>db_log_verify</code> should always be given the chance to detach from the environment and exit gracefully. To cause <code>db_log_verify</code> to release all environment resources and exit cleanly, send it an interrupt signal (<code>SIGINT</code>).</p>
<h2>EXIT STATUS</h2>
<p> The <code>db_log_verify</code> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd> If the <code>-h</code> option is not specified and the environment variable <code>DB_HOME</code> is set, it is used as the path of the database home, as described in <i>DB_ENV-&gt;open</i>.</dl>
<h2>NOTES</h2>
<p> If the application(s) that use the environment make use of the <i>DB_ENV-&gt;set_lg_dir</i> method, then in order for this utility to run correctly, you need a <code>DB_CONFIG</code> file which sets the proper paths using the set_lg_dir configuration parameter.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-db_archive/">db_archive</a></code>(1) <code><a href="/docs/linux/man/1-db_checkpoint/">db_checkpoint</a></code>(1) <code><a href="/docs/linux/man/1-db_deadlock/">db_deadlock</a></code>(1) <code><a href="/docs/linux/man/1-db_dump/">db_dump</a></code>(1) <code><a href="/docs/linux/man/1-db_hotbackup/">db_hotbackup</a></code>(1) <code><a href="/docs/linux/man/1-db_load/">db_load</a></code>(1) <code><a href="/docs/linux/man/1-db_printlog/">db_printlog</a></code>(1) <code><a href="/docs/linux/man/1-db_recover/">db_recover</a></code>(1) <code><a href="/docs/linux/man/1-db_replicate/">db_replicate</a></code>(1) <code><a href="/docs/linux/man/1-db_stat/">db_stat</a></code>(1) <code><a href="/docs/linux/man/1-db_tuner/">db_tuner</a></code>(1) <code><a href="/docs/linux/man/1-db_upgrade/">db_upgrade</a></code>(1) <code><a href="/docs/linux/man/1-db_verify/">db_verify</a></code>(1) </p>
<h2>Index</h2>
