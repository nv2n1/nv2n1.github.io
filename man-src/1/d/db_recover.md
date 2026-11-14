---
title: "db_recover(1)"
name: "db_recover"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_recover/"
description: "db5.3_recover – Restore the database to a consistent state"
---

<h2 class="name">NAME</h2>
<p> db5.3_recover &#8211; Restore the database to a consistent state </p>
<h2>SYNOPSIS</h2>
<p> <code>db5.3_recover</code> [-ceVv] [-h home] [-P password] [-t [[CC]YY]MMDDhhmm[.SS]]]</p>
<h2>DESCRIPTION</h2>
<p> The db5.3_recover utility must be run after an unexpected application, Berkeley DB, or system failure to restore the database to a consistent state. All committed transactions are guaranteed to appear after db5.3_recover has run, and all uncommitted transactions will be completely undone.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Perform catastrophic recovery instead of normal recovery.</p>
<dt><code>-e</code></p>
<dd> Retain the environment after running recovery. This option will rarely be used unless a DB_CONFIG file is present in the home directory. If a DB_CONFIG file is not present, then the regions will be created with default parameter values.</p>
<dt><code>-h</code></p>
<dd> Specify a home directory for the database environment; by default, the current working directory is used.</p>
<dt><code>-P</code></p>
<dd> Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-t</code></p>
<dd> Recover to the time specified rather than to the most current possible date. The timestamp argument should be in the form [[CC]YY]MMDDhhmm[.SS] where each pair of letters represents the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>CC</p>
<dd> The first two digits of the year (the century).</p>
<dt>YY</p>
<dd> The second two digits of the year. If &quot;YY&quot; is specified, but &quot;CC&quot; is not, a value for &quot;YY&quot; between 69 and 99 results in a &quot;CC&quot; value of 19. Otherwise, a &quot;YY&quot; value of 20 is used.</p>
<dt>MM</p>
<dd> The month of the year, from 1 to 12.</p>
<dt>DD</p>
<dd> The day of the month, from 1 to 31.</p>
<dt>hh</p>
<dd> The hour of the day, from 0 to 23.</p>
<dt>mm</p>
<dd> The minute of the hour, from 0 to 59.</p>
<dt>SS</p>
<dd> The second of the minute, from 0 to 61.</dl>
</dl>
<dt>
<dd> If the &quot;CC&quot; and &quot;YY&quot; letter pairs are not specified, the values default to the current year. If the &quot;SS&quot; letter pair is not specified, the value defaults to 0.</p>
<dt><code>-V</code></p>
<dd> Write the library version number to the standard output, and exit.</p>
<dt><code>-v</code></p>
<dd> Run in verbose mode.</dl>
<p> In the case of catastrophic recovery, an archival copy &#8211; or <i>snapshot</i> &#8211; of all database files must be restored along with all of the log files written since the database file snapshot was made. (If disk space is a problem, log files may be referenced by symbolic links). </p>
<p> If the failure was not catastrophic, the files present on the system at the time of failure are sufficient to perform recovery. </p>
<p> If log files are missing, db5.3_recover will identify the missing log file(s) and fail, in which case the missing log files need to be restored and recovery performed again. </p>
<p> The db5.3_recover utility uses a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_recover should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_recover to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The db5.3_recover utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd> If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>AUTHORS</h2>
<p> Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_recover from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others). </p>
<h2>Index</h2>
