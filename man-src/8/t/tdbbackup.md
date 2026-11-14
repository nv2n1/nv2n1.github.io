---
title: "tdbbackup(8)"
name: "tdbbackup"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tdbbackup/"
description: "tdbbackup – tool for backing up and for validating the integrity of samba .tdb files"
---

<p>tdbbackup &#8211; tool for backing up and for validating the integrity of samba .tdb files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>tdbbackup</code> [-s suffix] [-v] [-h] [-l]</dl>
<h2>Description</h2>
<dd>This tool is part of the <code><a href="/docs/linux/man/1-samba/">samba</a></code>(1) suite. </p>
<p> <code>tdbbackup</code> is a tool that may be used to backup samba .tdb files. This tool may also be used to verify the integrity of the .tdb files prior to samba startup or during normal operation. If it finds file damage and it finds a prior backup the backup file will be restored.</p>
<h2>Options</h2>
<p>-h</p>
<dl>
<dd>Get help information.</dl>
<p> -s suffix</p>
<dl>
<dd>The <code>-s</code> option allows the administrator to specify a file backup extension. This way it is possible to keep a history of tdb backup files by using a new suffix for each backup.</dl>
<p> -v</p>
<dl>
<dd>The <code>-v</code> will check the database for damages (corrupt data) which if detected causes the backup to be restored.</dl>
<p> -l</p>
<dl>
<dd>This options disables any locking, by passing TDB_NOLOCK to tdb_open_ex(). Only use this for database files which are not used by any other process! And also only if it is otherwise not possible to open the database, e.g. databases which were created with mutex locking.</dl>
<h2>Commands</h2>
<p><i>GENERAL INFORMATION</i> </p>
<p> The <code>tdbbackup</code> utility can safely be run at any time. It was designed so that it can be used at any time to validate the integrity of tdb files, even during Samba operation. Typical usage for the command will be: </p>
<p> tdbbackup [-s suffix] *.tdb </p>
<p> Before restarting samba the following command may be run to validate .tdb files: </p>
<p> tdbbackup -v [-s suffix] *.tdb </p>
<p> Samba .tdb files are stored in various locations, be sure to run backup all .tdb file on the system. Important files includes: </p>
<dl>
<dd>&bull; <code>secrets.tdb</code> &#8211; usual location is in the /usr/local/samba/private directory, or on some systems in /etc/samba.</dl>
<dl>
<dd>&bull; <code>passdb.tdb</code> &#8211; usual location is in the /usr/local/samba/private directory, or on some systems in /etc/samba.</dl>
<dl>
<dd>&bull; <code>*.tdb</code> located in the /usr/local/samba/var directory or on some systems in the /var/cache or /var/lib/samba directories.</dl>
<h2>Version</h2>
<p>This man page is correct for version 3 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The tdbbackup man page was written by John H Terpstra.</p>
