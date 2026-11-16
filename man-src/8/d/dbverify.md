---
title: "dbverify(8)"
name: "dbverify"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dbverify/"
description: "dbverify – Directory Server script for indexing attributes"
---

<p>dbverify &#8211; Directory Server script for indexing attributes</p>
<h2>Synopsis</h2>
<p>dbverify [-Z serverID] [-n backend] [-V] [-v] [-d debuglevel] [-h]</p>
<h2>Description</h2>
<p>Verifies the backend database files. If the server crashes because of a corrupted database, this command can be used to verify the integrity of the different database files to help isolate any problems. This script should be run while the server instacne is stopped.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></dt>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</dd>
<dt><code>-n</code> <i>Backend Name</i></dt>
<dd>The name of the LDBM database to reindex. Example: userRoot</dd>
<dt><code>-a</code> <i>Database Directory</i></dt>
<dd>Location of database if it is different than what is in the server configuration(e.g. backup directories)</dd>
<dt><code>-d</code> <i>Debug Level</i></dt>
<dd>Sets the debugging level.</dd>
<dt><code>-V</code></dt>
<dd>Verbose output.</dd>
<dt><code>-v</code></dt>
<dd>Display the version of the Directory Server.</dd>
<dt><code>-h</code></dt>
<dd>Display the usage.</dd></dl>
<h2>Example</h2>
<p>dbverify -Z instance3 -n userRoot -V </p>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>dbverify was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
