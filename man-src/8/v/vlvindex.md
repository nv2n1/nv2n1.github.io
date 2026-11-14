---
title: "vlvindex(8)"
name: "vlvindex"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vlvindex/"
description: "vlvindex – Directory Server script for VLV indexing"
---

<p>vlvindex &#8211; Directory Server script for VLV indexing</p>
<h2>Synopsis</h2>
<p>vlvindex [-Z serverID] -n backendname | {-s includesuffix}* -T vlvTag [-d debuglevel] [-h]</p>
<h2>Description</h2>
<p>Creates virtual list view (VLV) indexes, known in the Directory Server Console as browsing indexes. VLV indexes introduce flexibility in the way search results are viewed. VLV index configuration must already exist prior to running this script. The Directory Server must be stopped before running this script.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-n</code> <i>Backend Name</i></p>
<dd>The name of the LDBM database to reindex. Example: userRoot</p>
<dt><code>-s</code> <i>includeSuffix</i></p>
<dd>Specifies suffixes to be included or the subtrees to be included</p>
<dt><code>-T</code> <i>vlvTag</i></p>
<dd>This is the name of the vlv index entry under cn=config.</p>
<dt><code>-d</code> <i>Debug Level</i></p>
<dd>Settings the debugging level.</p>
<dt><code>-h</code></p>
<dd>Display the usage.</dl>
<h2>Example</h2>
<dl>
<dt>vlvindex -n userRoot -T myVLVIndex -Z instance2</p>
<dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>vlvindex was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
