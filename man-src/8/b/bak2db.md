---
title: "bak2db(8)"
name: "bak2db"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bak2db/"
description: "bak2db – Directory Server script for restoring a backup"
---

<p>bak2db &#8211; Directory Server script for restoring a backup</p>
<h2>Synopsis</h2>
<p>bak2db archivedir [-Z serverID] [-n backendname] [-q] | [-h]</p>
<h2>Description</h2>
<p>Restores the database from a archived backup. The Directory Server must be stopped prior to running this script.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>archivedir</code></p>
<dd>The directory of the archived database.</p>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-n</code> <i>Backend Name</i></p>
<dd>The name of the LDBM database to restore. Example: userRoot</p>
<dt><code>-q</code></p>
<dd>Quiet mode. Reduces output of task.</p>
<dt><code>-h</code></p>
<dd>Display the usage.</dl>
<h2>Example</h2>
<p>bak2db /LDAP/backups/20130305/ -Z instance1 -n userRoot bak2db /LDAP/backups/20130305/ -n example </p>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>bak2db was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
