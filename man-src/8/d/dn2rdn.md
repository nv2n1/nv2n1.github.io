---
title: "dn2rdn(8)"
name: "dn2rdn"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dn2rdn/"
description: "dn2rdn – Directory Server script to check for outdated index versions"
---

<p>dn2rdn &#8211; Directory Server script to check for outdated index versions</p>
<h2>Synopsis</h2>
<p>dn2rdn [-Z serverID] [-h] [-f] [-v] [-d debuglevel]</p>
<h2>Description</h2>
<p>Checks the database index version, and if it&#8217;s in a old format, then it will rebuild the indexes. The server instance needs to be stopped prior to running this script.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-d</code> <i>Debug Level</i></p>
<dd>Sets the debugging level.</p>
<dt><code>-f</code></p>
<dd>Force the upgrade.</p>
<dt><code>-v</code></p>
<dd>Display the version of the Directory Server.</p>
<dt><code>-h</code></p>
<dd>Display the usage.</dl>
<h2>Example</h2>
<p>dn2rdn </p>
<p> dn2rdn -Z instance3 -f</p>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>dn2rdn was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
