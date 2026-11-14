---
title: "verify-db-pl(8)"
name: "verify-db-pl"
section: "8"
letter: "v"
url: "/docs/linux/man/8-verify-db-pl/"
description: "verify-db.pl – Directory Server perl script for verifying the database."
---

<p>verify-db.pl &#8211; Directory Server perl script for verifying the database.</p>
<h2>Synopsis</h2>
<p>verify-db.pl [-Z serverID] [ -a path ] [-h]</p>
<h2>Description</h2>
<p>Verifies the backend database files. If the server crashes because of a corrupted database, this script can be used to verify the integrity of the different database files to help isolate any problems.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-a</code> <i>path</i></p>
<dd>Gives the path to the database directory. If this option is not passed with the verify-db.pl command, then it uses the default database directory, /var/lib/dirsrv/slapd-instance_name/db.</p>
<dt><code>-h</code></p>
<dd>Display usage</dl>
<h2>Example</h2>
<dl>
<dt>verify-db.pl -Z instance2 -a /var/lib/dirsrv/slapd-instance2/db</p>
<dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>verify-db.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
