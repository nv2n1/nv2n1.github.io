---
title: "berkeley_db_svc(1)"
name: "berkeley_db_svc"
section: "1"
letter: "b"
url: "/docs/linux/man/1-berkeley_db_svc/"
description: "berkeley_db5.3_svc – Berkeley DB RPC server"
---

<h2 class="name">NAME</h2>
<p> berkeley_db5.3_svc &#8211; Berkeley DB RPC server </p>
<h2>SYNOPSIS</h2>
<p> <code>berkeley_db5.3_svc</code> [-Vv] [-h home] [-I seconds] [-L file] [-t seconds] [-T seconds]</p>
<h2>DESCRIPTION</h2>
<p> The berkeley_db5.3_svc utility is the Berkeley DB RPC server.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Add the specified home directory to the list of allowed home directories that can be specified by the client. The home directory should be an absolute pathname. The last component of each home directory specified must be unique because that is how clients specify which database environment they want to join. </p>
<p> Recovery will be run on each specified environment before the server begins accepting requests from clients. For this reason, only one copy of the server program should ever be run at any time because recovery must always be single-threaded.</p>
<dt><code>-I</code></p>
<dd> Set the default idle timeout for client environments to the specified number of seconds. The default timeout is 24 hours.</p>
<dt><code>-L</code></p>
<dd> Log the execution of the berkeley_db5.3_svc utility to the specified file in the following format, where <i>###</i> is the process ID, and the date is the time the utility was started. </p>
<p> berkeley_db5.3_svc: ### Wed Jun 15 01:23:45 EDT 1995 </p>
<p> This file will be removed if the berkeley_db5.3_svc utility exits gracefully.</p>
<dt><code>-t</code></p>
<dd> Set the default timeout for client resources (idle transactions and cursors) to the specified number of seconds. When the timeout expires, if the resource is a transaction, it is aborted; if the resource is a cursor, it is closed. The default timeout is 5 minutes.</p>
<dt><code>-T</code></p>
<dd> Set the maximum timeout allowed for client resources. The default timeout is 20 minutes. If a client application requests a server timeout greater than the maximum timeout set for this server, the client&#8217;s timeout will be capped at the maximum timeout value.</p>
<dt><code>-V</code></p>
<dd> Write the library version number to the standard output, and exit.</p>
<dt><code>-v</code></p>
<dd> Run in verbose mode.</dl>
<p> The berkeley_db5.3_svc utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DB_HOME</code></p>
<dd> If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open.</dl>
<h2>AUTHORS</h2>
<p> Sleepycat Software, Inc. This manual page was created based on the HTML documentation for berkeley_db_svc from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others). </p>
<h2>Index</h2>
