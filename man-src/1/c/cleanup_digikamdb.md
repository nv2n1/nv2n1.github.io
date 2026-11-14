---
title: "cleanup_digikamdb(1)"
name: "cleanup_digikamdb"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cleanup_digikamdb/"
description: "cleanup_digikamdb – Cleanup the digiKam databases to reduce their sizes and increase access speed"
---

<h2>NAME</h2>
<p> cleanup_digikamdb &#8211; Cleanup the digiKam databases to reduce their sizes and increase access speed</p>
<h2>SYNOPSIS</h2>
<p> <code>cleanup_digikamdb</code> [-t] [-T] [-p] [-h]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code></p>
<dd> Include thumbnail databases.</p>
<dt><code>-T</code></p>
<dd> Only cleanup thumbnail databases.</p>
<dt><code>-p </code><i>path</i></p>
<dd> Specify a different database <i>path</i>. If this option is not set or the specified <i>path</i> is invalid, the entry from the configuration file will be used.</p>
<dt><code>-h</code></p>
<dd> Show command line options.</dl>
<h2>DESCRIPTION</h2>
<p> <code>cleanup_digikamdb</code> will cleanup and optimize the digiKam database file. This will, in most cases, lead to a smaller database file size and an increased access speed, because unneeded elements are removed from the database and data is optimized. </p>
<p> The program will make sure that no instance of digiKam is running, because it is more safe to have no database access during the optimization process. It then will read the digiKam configuration file and determine the database location. In a final step the database will be optimized by invoking the sqlite command &#8216;<i>VACUUM</i>;&#8217; on it. If more then one database is found in this location, <code>cleanup_digikamdb</code> will optimize every database found in this path and below. </p>
<p> For further explanation, see the following description of the <i>VACUUM</i> command from the sqlite3 website: </p>
<p> When an object (table, index, or trigger) is dropped from the database, it leaves behind empty space. This empty space will be reused the next time new information is added to the database. But in the meantime, the database file might be larger than strictly necessary. Also, frequent inserts, updates, and deletes can cause the information in the database to become fragmented &#8211; scrattered out all across the database file rather than clustered together in one place. </p>
<p> The <i>VACUUM</i> command cleans the main database by copying its contents to a temporary database file and reloading the original database file from the copy. This eliminates free pages, aligns table data to be contiguous, and otherwise cleans up the database file structure.</p>
<h2>AUTHOR</h2>
<p> <code>cleanup_digikamdb</code> was written by Andi Clemens &lt;andi dot clemens at gmail dot com&gt; </p>
<h2>Index</h2>
