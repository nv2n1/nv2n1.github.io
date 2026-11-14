---
title: "vfs_scannedonly(8)"
name: "vfs_scannedonly"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_scannedonly/"
description: "vfs_scannedonly – Ensures that only files that have been scanned for viruses are visible and accessible to the end user."
---

<p>vfs_scannedonly &#8211; Ensures that only files that have been scanned for viruses are visible and accessible to the end user.</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = scannedonly</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/8-samba/">samba</a></code>(8) suite. </p>
<p> The vfs_scannedonly VFS module ensures that only files that have been scanned for viruses are visible and accessible to the end user. If non-scanned files are found an anti-virus scanning daemon is notified. The anti-virus scanning daemon is not part of the Samba suite. </p>
<p> Scannedonly comes in two parts: a samba vfs module and (one or more) daemons. The daemon scans files. If a certain file is clean, a second file is created with prefix .scanned:. The Samba module simply looks if such a .scanned: file exists, and is newer than the pertinent file. If this is the case, the file is shown to the user. If this is not the case, the file is not returned in a directory listing (configurable), and cannot be opened (configurable). The Samba vfs module will notify the daemon to scan this file. </p>
<p> So what happens for the user in the default configuration. The first time a directory is listed, it shows files as &#8216;file is being scanned for viruses, but after the first time all files are shown. There is a utility scannedonly_prescan that can help you to prescan all directories. When new files are written the daemon is notified immediately after the file is complete. </p>
<p> If a virus is found by the daemon, a file with a warning message is created in the directory of the user, a warning is sent to the logs, and the file is renamed to have prefix .virus:. Files with the .virus: prefix are never shown to the user and all access is denied. </p>
<p> This module is stackable.</p>
<h2>Configuration</h2>
<p>vfs_scannedonly relies on a anti-virus scanning daemon that listens on the scannedonly socket (unix domain socket or UDP socket).</p>
<h2>Options</h2>
<p>scannedonly:domain_socket = True</p>
<dl>
<dd>Whether to use a unix domain socket or not (false reverts to use udp)</dl>
<p> scannedonly:socketname = /var/lib/scannedonly/scan</p>
<dl>
<dd>The location of the unix domain socket to connect to</dl>
<p> scannedonly:portnum = 2020</p>
<dl>
<dd>The udp port number to connect to</dl>
<p> scannedonly:scanhost = localhost</p>
<dl>
<dd>When using UDP the host that runs the scanning daemon (this host needs access to the files!)</dl>
<p> scannedonly:show_special_files = True</p>
<dl>
<dd>Whether sockets, devices and fifo&#8217;s (all not scanned for viruses) should be visible to the user</dl>
<p> scannedonly:rm_hidden_files_on_rmdir = True</p>
<dl>
<dd>Whether files that are not visible (.scanned: files, .failed: files and .virus: files) should be deleted if the user tries to remove the directory. If false, the user will get the &quot;directory is not empty&quot; error.</dl>
<p> scannedonly:hide_nonscanned_files = True</p>
<dl>
<dd>If false, all non-scanned files are visible in directory listings. If such files are found in a directory listing the scanning daemon is notified that scanning is required. Access to non-scanned files is still denied (see scannedonly:allow_nonscanned_files).</dl>
<p> scannedonly:scanning_message = is being scanned for viruses</p>
<dl>
<dd>If non-scanned files are hidden (if scannedonly:hide_nonscanned_files = True), a fake 0 byte file is shown. The filename is the original filename with the message as suffix.</dl>
<p> scannedonly:recheck_time_open = 50</p>
<dl>
<dd>If a non-scanned file is opened, the vfs module will wait recheck_tries_open times for recheck_time_open milliseconds for the scanning daemon to create a .scanned: file. For small files that are scanned by the daemon within the time (tries * time) the behavior will be just like on-access scanning.</dl>
<p> scannedonly:recheck_tries_open = 100</p>
<dl>
<dd>See recheck_time_open.</dl>
<p> scannedonly:recheck_time_readdir = 50</p>
<dl>
<dd>If a non-scanned file is in a directory listing the vfs module notifies the daemon (once for all files that need scanning in that directory), and waits recheck_tries_readdir times for recheck_time_readdir milliseconds. Only used when hide_nonscanned_files is false.</dl>
<p> scannedonly:recheck_tries_readdir = 20</p>
<dl>
<dd>See recheck_time_readdir.</dl>
<p> scannedonly:allow_nonscanned_files = False</p>
<dl>
<dd>Allow access to non-scanned files. The daemon is notified, however, and special files such as .scanned: files. .virus: files and .failed: files are not listed.</dl>
<h2>Examples</h2>
<p>Enable anti-virus scanning: </p>
<dl>
<dd>
<pre> <i>[homes]</i>
 m[blue]<code>vfs objects = scannedonly</code>m[]
 m[blue]<code>scannedonly:hide_nonscanned_files = False</code>m[]</pre>
</dl>
<h2>Caveats</h2>
<p>This is not true on-access scanning. However, it is very fast for files that have been scanned already.</p>
<h2>Version</h2>
<p>This man page is correct for version 4.0.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Scannedonly was developed for Samba by Olivier Sessink. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
