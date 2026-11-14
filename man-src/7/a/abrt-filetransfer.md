---
title: "abrt-filetransfer(7)"
name: "abrt-filetransfer"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-filetransfer/"
---

FileTransfer plugin for <a HREF="/docs/linux/man/8-abrt/">abrt</a>(8)

<h2>Description</h2>

<i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the crash data and takes action according to its configuration. This manual page describes the <i>FileTransfer</i> plugin for <i>abrt</i>. This plugin is used to transfer the crash report to another machine using a file transfer protocol. The protocols supported are FTP, FTPS, HTTP, HTTPS, SCP, SFTP, and TFTP.

<h2>Invocation</h2>

The plugin is invoked in the <i>abrt.conf</i> file, usually in the <i>ActionsAndReporters</i> option and/or the <i>[cron]</i> section. There are two modes of invocation: * Specify <i>FileTransfer(one)</i> in ActionsAndReporters directive. Immediately after crash is detected, the plugin transfers crash data to the server specified in the <i>FileTransfer.conf</i> configuration file. * Specify <i>FileTransfer(store)</i> in ActionsAndReporters directive and add <i>HH:MM = FileTransfer</i> line in [cron] section. At the time of the crash, the plugin stores a record of it in its internal list. When specified time is reached, the plugin iterates through its internal list and sends every recorded crash to the specified URL. After that, the internal list is cleared.

<h2>Configuration</h2>

The <i>FileTransfer.conf</i> configuration file contains several entries in the format &quot;Option = Value&quot;. The options are:

<h3>Url</h3>

The URL of the server, where the crash should be transfered, specifying the protocol, the path, the user name and the password, for example: 
 URL = <a HREF="ftp://user:passwd@server.com/path">ftp://user:passwd@server.com/path</a>

<h3>ArchiveType</h3>

The type of the archive in which to pack the crash data. Currently, <i>.tar</i>, <i>.tar.gz</i>, <i>.tar.bz2</i> and <i>.zip</i> are supported. The default is <i>.tar.gz</i>

<h3>RetryCount</h3>

This specifies how many times the plugin will try to resend the file if the transfer was not succesful. The plugin waits a while before it retries the transfer: see <i>RetryDelay</i>. The default is 3

<h3>RetryDelay</h3>

If the transfer was not succesful, the plugin will wait some time before sending the file again. This configuration option specifies the time in seconds. The default is 20.

<h2>Examples</h2>

Typical configuration in <i>abrt.conf</i>. The crash is stored each time it happens and at midnight, all the crash data is transferred to a central server. [common] 
 ActionsAndReporters = FileTransfer(store) 
 [cron] 
 00:00 = FileTransfer

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a HREF="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7)

<h2>Author</h2>

Written by Daniel Novotny &lt;dnovotny [at] redhat.com&gt;.
