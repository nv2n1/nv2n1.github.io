---
title: "db2bak(8)"
name: "db2bak"
section: "8"
letter: "d"
url: "/docs/linux/man/8-db2bak/"
description: "db2bak – Directory Server script for making a backup of the database"
---

<p>db2bak &#8211; Directory Server script for making a backup of the database</p>
<h2>Synopsis</h2>
<p>db2bak [archivedir] [-Z serverID] [-q] [-h]</p>
<h2>Description</h2>
<p>Creates a backup of the database. This script can be executed while the server is running or stopped.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>archivedir</code></p>
<dd>The full path to the directory to store the backup.</p>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-q</code></p>
<dd>Quiet mode. Reduces output of task.</p>
<dt><code>-h</code></p>
<dd>Display the usage.</dl>
<h2>Example</h2>
<dl>
<dt>db2bak -Z instance2</p>
<dd>Makes a backup of the entire database for &#8216;instance2&#8217;, and stores it in the default server instance backup directory.</p>
<dt>db2bak /LDAP/backups/20130305</p>
<dd>Creates a backup of the database and stores it in specified location.</dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>db2bak was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
