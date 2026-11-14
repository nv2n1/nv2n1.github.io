---
title: "db_replicate(1)"
name: "db_replicate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_replicate/"
description: "db_replicate – Provide replication services"
---

<h2>NAME</h2>
<p> db_replicate &#8211; Provide replication services</p>
<h2>SYNOPSIS</h2>
<p> <code>db_replicate</code> [-MVv] [-h <i>home</i>] [-L <i>file</i>] [-P <i>password</i>] [-T <i>num-threads</i>] [-t <i>secs</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>db_replicate</code> utility is a daemon process that provides replication/HA services on a transactional environment. This utility enables you to upgrade an existing Transactional Data Store application to an HA application with minor modifications.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <i>home</i></p>
<dd> Specify a home directory for the database environment; by default, the current working directory is used.</p>
<dt><code>-L</code> <i>file</i></p>
<dd> Log the execution of the <code>db_replicate</code> utility to the specified file in the following format, where ### is the process ID, and the date is the time the utility was started. </p>
<p> db_replicate: ### Wed Jun 15 01:23:45 EDT 1995 </p>
<p> Additionally, events such as site role changes will be noted in the log file. This file will be removed if the <code>db_replicate</code> utility exits gracefully.</p>
<dt><code>-M</code></p>
<dd> Start the <code>db_replicate</code> utility to be the master site of the replication group. Otherwise, the site will be started as a client replica.</p>
<dt><code>-P</code> <i>password</i></p>
<dd> Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-T</code> <i>num-threads</i></p>
<dd> Specify the number of replication message processing threads.</p>
<dt><code>-t</code> <i>secs</i></p>
<dd> Specify how often (in seconds) the utility will check for program interruption and resend the last log record.</p>
<dt><code>-V</code></p>
<dd> Write the library version number to the standard output, and exit.</p>
<dt><code>-v</code></p>
<dd> Turn on replication verbose messages. These messages will be written to the standard output and will be quite voluminous.</dl>
<p> The <code>db_replicate</code> utility does not attempt to create the Berkeley DB shared memory regions if they do not already exist. The application that creates the region should be started first, and once the region is created, the <code>db_replicate</code> utility should be started. The application must use the <i>DB_INIT_REP</i> and <i>DB_THREAD</i> flags when creating the environment. </p>
<p> The <code>db_replicate</code> utility uses a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, <code>db_replicate</code> should always be given the chance to detach from the environment and exit gracefully. To cause <code>db_replicate</code> to release all environment resources and exit cleanly, send it an interrupt signal (<code>SIGINT</code>).</p>
<h2>EXIT STATUS</h2>
<p> The <code>db_replicate</code> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd> If the <code>-h</code> option is not specified and the environment variable <code>DB_HOME</code> is set, it is used as the path of the database home, as described in <i>DB_ENV-&gt;open</i>.</dl>
<h2>NOTES</h2>
<p> This utility is not supported for use with the DB SQL APIs.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-db_archive/">db_archive</a></code>(1) <code><a href="/docs/linux/man/1-db_checkpoint/">db_checkpoint</a></code>(1) <code><a href="/docs/linux/man/1-db_deadlock/">db_deadlock</a></code>(1) <code><a href="/docs/linux/man/1-db_dump/">db_dump</a></code>(1) <code><a href="/docs/linux/man/1-db_hotbackup/">db_hotbackup</a></code>(1) <code><a href="/docs/linux/man/1-db_log_verify/">db_log_verify</a></code>(1) <code><a href="/docs/linux/man/1-db_load/">db_load</a></code>(1) <code><a href="/docs/linux/man/1-db_printlog/">db_printlog</a></code>(1) <code><a href="/docs/linux/man/1-db_recover/">db_recover</a></code>(1) <code><a href="/docs/linux/man/1-db_stat/">db_stat</a></code>(1) <code><a href="/docs/linux/man/1-db_tuner/">db_tuner</a></code>(1) <code><a href="/docs/linux/man/1-db_upgrade/">db_upgrade</a></code>(1) <code><a href="/docs/linux/man/1-db_verify/">db_verify</a></code>(1) </p>
<h2>Index</h2>
