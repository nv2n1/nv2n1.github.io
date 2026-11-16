---
title: "upgradedb(8)"
name: "upgradedb"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upgradedb/"
description: "upgradedb – Directory Server script for upgrading the database"
---

<p>upgradedb &#8211; Directory Server script for upgrading the database</p>
<h2>Synopsis</h2>
<p>upgradedb [-a archivedir] [-Z serverID] [-f] [-v] [-d debuglevel] [-h]</p>
<h2>Description</h2>
<p>Checks the DB version and if it has the old index formatting then it will rebuild the indexes. This is usually needed after migrating from older versions of Directory Server. This script must be run while the server is stopped.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-n</code> <i>Backend Name</i></dt>
<dd>The name of the LDBM database to reindex. Example: userRoot</dd>
<dt><code>-a</code> <i>Database directory</i></dt>
<dd>The full path to the database directory.</dd>
<dt><code>-Z</code> <i>Server Identifier</i></dt>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</dd>
<dt><code>-N</code></dt>
<dd>Only checks whether any DNs in the database need to be updated.</dd>
<dt><code>-h</code></dt>
<dd>Display the usage.</dd></dl>
<h2>Example</h2>
<dl>
<dt>upgradedb -Z instance2</dt>
<dd></dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>upgradedb was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
