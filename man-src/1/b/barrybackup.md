---
title: "barrybackup(1)"
name: "barrybackup"
section: "1"
letter: "b"
url: "/docs/linux/man/1-barrybackup/"
description: "barrybackup – Barry Project’s backup program for the BlackBerry handheld"
---

<h2 class="name">NAME</h2>
<p> <code>barrybackup</code> &#8211; Barry Project&#8217;s backup program for the BlackBerry handheld </p>
<h2>SYNOPSIS</h2>
<p> <code>barrybackup</code> [-?][-d]</p>
<h2>DESCRIPTION</h2>
<p> <code>barrybackup</code> is a GUI application for backing up and restoring Blackberry handheld databases. </p>
<p> The application allows for filtering of databases for both backup and restore, so not all databases need to be backed up at once, nor all restored. </p>
<p> Backups and configuration files are stored by default in the user&#8217;s home directory, under ~/.barry/backup/PIN. This destination can be changed in the config dialogs, per device. </p>
<p> The backup files are compressed tarballs containing specially named files for each record of the databases.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> <code>&#8211;debug-output</code> Enables low level protocol debug output written to stdout/stderr.</p>
<dt><code>&#8211;display=DISPLAY</code></p>
<dd> Specify which X display to use.</p>
<dt><code>-?</code></p>
<dd> <code>&#8211;help</code> Show summary of options.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options. </p>
</dl>
<h2>TAR FORMAT</h2>
<p> Backups are stored in tar format, compressed with gzip. Backup files are named with the following pattern: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PIN-YYYYMMDD-HHMMSS[-tag_name].tar.gz</p>
<p> The tag name is optional and is used to name a particular backup. </p>
<p> Each record is appended to the tar file using the following pattern for the filename: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>DBname/RecordID RecordTypeID</p>
<p> That is, the database name is used as the directory name, and the filename contains the record ID and record type ID separated by a space. </p>
<p> Database names can contain spaces. </p>
<p> Record IDs are generally unique, but not all Blackberry devices mandate this, so it is possible, but rare, to have two records in the tar file with the same filename. This is ok. The only problem you&#8217;d see is if you expanded such a tar file to a filesystem. The restore process just reads in the filename sequentially and writes them to the device, so duplicate record IDs are not a problem. </p>
<h2>AUTHOR</h2>
<p> <code>barrybackup</code> is part of the Barry project. This manual page was written by Chris Frey.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a> </p>
<h2>Index</h2>
