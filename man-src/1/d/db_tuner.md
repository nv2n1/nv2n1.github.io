---
title: "db_tuner(1)"
name: "db_tuner"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_tuner/"
description: "db_tuner – analyze and tune btree database"
---

<h2>NAME</h2>
<p> db_tuner &#8211; analyze and tune btree database</p>
<h2>SYNOPSIS</h2>
<p> <code>db_tuner</code> [-c <i>cachesize</i>] -d <i>file</i> [-h <i>home</i>] [-s <i>database</i>] [-v]</p>
<h2>DESCRIPTION</h2>
<p> The <code>db_tuner</code> utility analyzes the data in a btree database, and suggests a page size that is likely to deliver optimal operation.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>cachesize</i></p>
<dd> Specify a value of the cachesize, otherwise, the default value will be set.</p>
<dt><code>-d</code> <i>file</i></p>
<dd> Display database statistics for the specified file. If the database contains multiple databases and the <code>-s</code> flag is not specified, the statistics are for the internal database that describes the other databases the file contains, and not for the file as a whole.</p>
<dt><code>-h</code> <i>home</i></p>
<dd> Specify a home directory for the database environment.</p>
<dt><code>-s</code> <i>database</i></p>
<dd> Display page size recommendation for the specified database contained in the file specified with the <code>-d</code> flag.</p>
<dt><code>-v</code></p>
<dd> Display verbose information.</dl>
<h2>NOTES</h2>
<p> The <code>db_tuner</code> utility assumes that databases are compacted when analysing the data. The analysis is based on a static view of the data and the data access and update patterns are not take into account.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-db_archive/">db_archive</a></code>(1) <code><a href="/docs/linux/man/1-db_checkpoint/">db_checkpoint</a></code>(1) <code><a href="/docs/linux/man/1-db_deadlock/">db_deadlock</a></code>(1) <code><a href="/docs/linux/man/1-db_dump/">db_dump</a></code>(1) <code><a href="/docs/linux/man/1-db_hotbackup/">db_hotbackup</a></code>(1) <code><a href="/docs/linux/man/1-db_log_verify/">db_log_verify</a></code>(1) <code><a href="/docs/linux/man/1-db_load/">db_load</a></code>(1) <code><a href="/docs/linux/man/1-db_printlog/">db_printlog</a></code>(1) <code><a href="/docs/linux/man/1-db_recover/">db_recover</a></code>(1) <code><a href="/docs/linux/man/1-db_replicate/">db_replicate</a></code>(1) <code><a href="/docs/linux/man/1-db_stat/">db_stat</a></code>(1) <code><a href="/docs/linux/man/1-db_upgrade/">db_upgrade</a></code>(1) <code><a href="/docs/linux/man/1-db_verify/">db_verify</a></code>(1) </p>
<h2>Index</h2>
