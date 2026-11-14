---
title: "vacuumlo(1)"
name: "vacuumlo"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vacuumlo/"
description: "vacuumlo – remove orphaned large objects from a PostgreSQL database"
---

<h2 class="name">NAME</h2>
<p> vacuumlo &#8211; remove orphaned large objects from a PostgreSQL database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>vacuumlo</code> [<i>option</i>&#8230;] <i>dbname</i>&#8230;</dl>
<h2>DESCRIPTION</h2>
<dd>vacuumlo is a simple utility program that will remove any &#8220;orphaned&#8221; large objects from a PostgreSQL database. An orphaned large object (LO) is considered to be any LO whose OID does not appear in any oid or lo data column of the database. </p>
<p> If you use this, you may also be interested in the <code>lo_manage</code> trigger in the lo module. <code>lo_manage</code> is useful to try to avoid creating orphaned LOs in the first place. </p>
<p> All databases named on the command line are processed.</p>
<h2>OPTIONS</h2>
<p> vacuumlo accepts the following command-line arguments: </p>
<p> <code>-l</code> <i>limit</i></p>
<dl>
<dt>
<dd> Remove no more than <i>limit</i> large objects per transaction (default 1000). Since the server acquires a lock per LO removed, removing too many LOs in one transaction risks exceeding max_locks_per_transaction. Set the limit to zero if you want all removals done in a single transaction.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Don&#8217;t remove anything, just show what would be done.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Write a lot of progress messages.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the vacuumlo version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about vacuumlo command line arguments, and exit.</dl>
<p> vacuumlo also accepts the following command-line arguments for connection parameters: </p>
<p> <code>-h</code> <i>hostname</i></p>
<dl>
<dt>
<dd> Database server&#8217;s host.</dl>
<p> <code>-p</code> <i>port</i></p>
<dl>
<dt>
<dd> Database server&#8217;s port.</dl>
<p> <code>-U</code> <i>username</i></p>
<dl>
<dt>
<dd> User name to connect as.</dl>
<p> <code>-w</code>, <code>&#8211;no-password</code></p>
<dl>
<dt>
<dd> Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a .pgpass file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dl>
<p> <code>-W</code></p>
<dl>
<dt>
<dd> Force vacuumlo to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since vacuumlo will automatically prompt for a password if the server demands password authentication. However, vacuumlo will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<h2>NOTES</h2>
<p> vacuumlo works by the following method: First, vacuumlo builds a temporary table which contains all of the OIDs of the large objects in the selected database. It then scans through all columns in the database that are of type oid or lo, and removes matching entries from the temporary table. (Note: Only types with these names are considered; in particular, domains over them are not considered.) The remaining entries in the temporary table identify orphaned LOs. These are removed.</p>
<h2>AUTHOR</h2>
<p> Peter Mount &lt;peter [at] retep.org.uk&gt; </p>
<h2>Index</h2>
