---
title: "smbtar(1)"
name: "smbtar"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smbtar/"
description: "smbtar – shell script for backing up SMB/CIFS shares directly to UNIX tape drives"
---

<h2 class="name">NAME</h2>
<p> smbtar &#8211; shell script for backing up SMB/CIFS shares directly to UNIX tape drives </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>smbtar [-r] [-i] [-a] [-v] {-s server} [-p password] [-x services] [-X] [-N filename] [-b blocksize] [-d directory] [-l loglevel] [-u user] [-t tape] {filenames}</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> smbtar is a very small shell script on top of <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1) which dumps SMB shares directly to tape.</p>
<h2>OPTIONS</h2>
<p> -s server</p>
<dl>
<dt>
<dd> The SMB/CIFS server that the share resides upon.</dl>
<p> -x service</p>
<dl>
<dt>
<dd> The share name on the server to connect to. The default is &quot;backup&quot;.</dl>
<p> -X</p>
<dl>
<dt>
<dd> Exclude mode. Exclude filenames&#8230; from tar create or restore.</dl>
<p> -d directory</p>
<dl>
<dt>
<dd> Change to initial <i>directory </i> before restoring / backing up files.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Verbose mode.</dl>
<p> -p password</p>
<dl>
<dt>
<dd> The password to use to access a share. Default: none</dl>
<p> -u user</p>
<dl>
<dt>
<dd> The user id to connect as. Default: UNIX login name.</dl>
<p> -a</p>
<dl>
<dt>
<dd> Reset DOS archive bit mode to indicate file has been archived.</dl>
<p> -t tape</p>
<dl>
<dt>
<dd> Tape device. May be regular file or tape device. Default: <i>$TAPE</i> environmental variable; if not set, a file called tar.out.</dl>
<p> -b blocksize</p>
<dl>
<dt>
<dd> Blocking factor. Defaults to 20. See <a href="/docs/linux/man/1-tar/">tar</a>(1) for a fuller explanation.</dl>
<p> -N filename</p>
<dl>
<dt>
<dd> Backup only files newer than filename. Could be used (for example) on a log file to implement incremental backups.</dl>
<p> -i</p>
<dl>
<dt>
<dd> Incremental mode; tar files are only backed up if they have the archive bit set. The archive bit is reset after each file is read.</dl>
<p> -r</p>
<dl>
<dt>
<dd> Restore. Files are restored to the share from the tar file.</dl>
<p> -l log level</p>
<dl>
<dt>
<dd> Log (debug) level. Corresponds to the <i>-d</i> flag of <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1).</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The <i>$TAPE</i> variable specifies the default tape device to write to. May be overridden with the -t option.</p>
<h2>BUGS</h2>
<p> The smbtar script has different options from ordinary tar and from smbclient&#8217;s tar command.</p>
<h2>CAVEATS</h2>
<p> Sites that are more careful about security may not like the way the script handles PC passwords. Backup and restore work on entire shares; should work on file lists. smbtar works best with GNU tar and may not work well with other versions.</p>
<h2>DIAGNOSTICS</h2>
<p> See the <i>DIAGNOSTICS</i> section for the <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1) command.</p>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8), <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1), <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5).</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> Ricky Poulten wrote the tar extension and this man page. The smbtar script was heavily rewritten and improved by Martin Kraemer. Many thanks to everyone who suggested extensions, improvements, bug fixes, etc. The man page sources were converted to YODL format (another excellent piece of Open Source software, available at <a href="ftp://ftp.icce.rug.nl/pub/unix/)">ftp://ftp.icce.rug.nl/pub/unix/)</a> and updated for the Samba 2.0 release by Jeremy Allison. The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy. </p>
<h2>Index</h2>
