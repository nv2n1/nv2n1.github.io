---
title: "zarafa(1)"
name: "zarafa"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa/"
description: "zarafa – Zarafa server overview."
---

<h2 class="name">NAME</h2>
<p> zarafa &#8211; Zarafa server overview. </p>
<h2>DESCRIPTION</h2>
<p> Zarafa is a full-featured e-mail and groupware solution, focused towards clients using the MAPI standard. The Zarafa suite consists of the following parts: </p>
<p> zarafa-server</p>
<dl>
<dt>
<dd> The main server process, accepting client connections, and managing storage and retrieval of data from the database.</dl>
<p> zarafa-spooler</p>
<dl>
<dt>
<dd> The outgoing e-mail spooler. This service makes sure that e-mails sent by clients are converted to internet e-mail and forwarded to an SMTP server.</dl>
<p> zarafa-dagent</p>
<dl>
<dt>
<dd> The Zarafa delivery agent is called by your MTA to deliver an incoming e-mail message into a user&#8217;s inbox.</dl>
<p> zarafa-admin</p>
<dl>
<dt>
<dd> The admin program can be started from the command line to perform various administrational tasks such add creating users, and managing groups.</dl>
<p> zarafa-monitor</p>
<dl>
<dt>
<dd> The monitor server process monitors user stores for quota limits. When a user goes over the warning quota level, zarafa-monitor will issue a warning e-mail.</dl>
<p> zarafa-gateway</p>
<dl>
<dt>
<dd> The gateway server process enables POP3 and/or IMAP connectivity to the Zarafa server. Users with other non-Outlook or webaccess clients can still retreive their e-mail from the server.</dl>
<p> zarafa-passwd</p>
<dl>
<dt>
<dd> The passwd program can be started from the command line to update the user password when the server is running with dbplugin.</dl>
<p> zarafa-fsck</p>
<dl>
<dt>
<dd> The fsck program can be started from the command line to check and possibly fix broken items in your calendar or tasks folder.</dl>
<p> zarafa-backup</p>
<dl>
<dt>
<dd> The backup tool creates an incremental dump of a store. The data can be restored by the <code>zarafa-restore</code> tool. This tool can be used as a brick-level-backup. It can not be used as a disaster-recovery tool.</dl>
<p> zarafa-restore</p>
<dl>
<dt>
<dd> The restore tool reads data from a backup create by <code>zarafa-backup</code>. You can restore single items or folders. To restore a complete store, you can use the example script found in /usr/share/zarafa/zarafa-backup-helpers.</dl>
<p> zarafa-ical</p>
<dl>
<dt>
<dd> The iCal/CalDAV gateway enables users to retrieve their own Zarafa calendar using the iCalendar standard.</dl>
<p> zarafa-licensed</p>
<dl>
<dt>
<dd> The zarafa-licensed daemon is used for licensing query information from non-free parts of the zarafa product. You must run this daemon if you wish to use non-free components of the zarafa product, like access from Windows environments.</dl>
<p> zarafa-report</p>
<dl>
<dt>
<dd> A reporting program used by zarafa-licensed to send license reports to the zarafa-server using a secured connection.</dl>
<p> zarafa-stats</p>
<dl>
<dt>
<dd> A simple program that dumps some statistics the zarafa-server program collects.</dl>
<p> zarafa-cfgchecker</p>
<dl>
<dt>
<dd> This program tests for common configuration errors for a given config file.`</dl>
<p> zarafa-search</p>
<dl>
<dt>
<dd> The zarafa-search daemon is used to index all messages for all users in the zarafa-server. Indexing messages greatly enhances the search performance of the zarafa-server.</dl>
<p> zarafa-ws</p>
<dl>
<dt>
<dd> The Zarafa Web Services server process enables EWS connectivity to the Zarafa server. Users with other non-Windows Outlook or WebApp clients can still retreive their e-mail and calendars from the server.</dl>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-spooler/">zarafa-spooler</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-dagent/">zarafa-dagent</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-admin/">zarafa-admin</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-monitor/">zarafa-monitor</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-gateway/">zarafa-gateway</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-passwd/">zarafa-passwd</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-fsck/">zarafa-fsck</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-backup/">zarafa-backup</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-restore/">zarafa-restore</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-ical/">zarafa-ical</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-licensed/">zarafa-licensed</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-report/">zarafa-report</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-stats/">zarafa-stats</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-cfgchecker/">zarafa-cfgchecker</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-search/">zarafa-search</a></code>(1)<code><a href="/docs/linux/man/1-zarafa-ws/">zarafa-ws</a></code>(1) </p>
<h2>Index</h2>
