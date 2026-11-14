---
title: "ntdbbackup(8)"
name: "ntdbbackup"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntdbbackup/"
description: "ntdbbackup – tool for backing up and for validating the integrity of samba .ntdb files"
---

<p>ntdbbackup &#8211; tool for backing up and for validating the integrity of samba .ntdb files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ntdbbackup</code> [-s suffix] [-v] [-h]</dl>
<h2>Description</h2>
<dd>This tool is part of the <code><a href="/docs/linux/man/1-samba/">samba</a></code>(1) suite. </p>
<p> <code>ntdbbackup</code> is a tool that may be used to backup samba .ntdb files. This tool may also be used to verify the integrity of the .ntdb files prior to samba startup or during normal operation. If it finds file damage and it finds a prior backup the backup file will be restored.</p>
<h2>Options</h2>
<p>-h</p>
<dl>
<dd>Get help information.</dl>
<p> -s suffix</p>
<dl>
<dd>The <code>-s</code> option allows the administrator to specify a file backup extension. This way it is possible to keep a history of ntdb backup files by using a new suffix for each backup.</dl>
<p> -v</p>
<dl>
<dd>The <code>-v</code> will check the database for damages (corrupt data) which if detected causes the backup to be restored.</dl>
<h2>Commands</h2>
<p><i>GENERAL INFORMATION</i> </p>
<p> The <code>ntdbbackup</code> utility can safely be run at any time. It was designed so that it can be used at any time to validate the integrity of ntdb files, even during Samba operation. Typical usage for the command will be: </p>
<p> ntdbbackup [-s suffix] *.ntdb </p>
<p> Before restarting samba the following command may be run to validate .ntdb files: </p>
<p> ntdbbackup -v [-s suffix] *.ntdb </p>
<p> Note that Samba 4 can use .tdb files instead, so you should use <code>tdbbackup</code> on those files. </p>
<p> Samba .tdb and .ntdb files are stored in various locations, be sure to run backup all .(n)tdb files on the system. Important files includes: </p>
<dl>
<dd>&bull; <code>secrets.(n)tdb</code> &#8211; usual location is in the /usr/local/samba/private directory, or on some systems in /etc/samba.</dl>
<dl>
<dd>&bull; <code>passdb.(n)tdb</code> &#8211; usual location is in the /usr/local/samba/private directory, or on some systems in /etc/samba.</dl>
<dl>
<dd>&bull; <code>*.tdb</code> and <code>*.ntdb</code> located in the /usr/local/samba/var directory or on some systems in the /var/cache or /var/lib/samba directories.</dl>
<h2>Version</h2>
<p>This man page is correct for version 4 of the Samba suite.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tdbbackup/">tdbbackup</a>(8), <a href="/docs/linux/man/8-ntdbrestore/">ntdbrestore</a>(8)</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The ntdbbackup man page was written by Rusty Russell, based on the tdbbackup man page by John H Terpstra.</p>
