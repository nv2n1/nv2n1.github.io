---
title: "db2index(8)"
name: "db2index"
section: "8"
letter: "d"
url: "/docs/linux/man/8-db2index/"
description: "db2index – Directory Server script for indexing attributes"
---

<p>db2index &#8211; Directory Server script for indexing attributes</p>
<h2>Synopsis</h2>
<p>db2index [-Z serverID] [-n backend | {-s includeSuffix}* -t attribute[:indextypes[:matchingrules]] -T vlvTag] [-h]</p>
<h2>Description</h2>
<p>Reindexes the database index files. The Directory Server must be stopped prior to running this script.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-n</code> <i>Backend Name</i></p>
<dd>The name of the LDBM database to reindex. Example: userRoot</p>
<dt><code>-s</code> <i>includeSuffix</i></p>
<dd>Specifies suffixes to be included or the subtrees to be included</p>
<dt><code>-t</code> <i>attributeName[:indextypes[:matchingrules]]</i></p>
<dd>The attribute to index. Optionally you can specify a comma separated list of index types: eq, sub, pres, and approx. An optional matching rule OID can also be set.</p>
<dt><code>-T</code> <i>vlvTag</i></p>
<dd>This is the name of the vlv index entry under cn=config.</p>
<dt><code>-h</code></p>
<dd>Display the usage.</dl>
<h2>Example</h2>
<dl>
<dt>db2index -n userRoot -t uid:eq,sub:1.3.6.1.4.1.42.2.27.9.4.76.1 -t cn:eq,pres</p>
<dd>
<dt>db2index -Z instance2 -s &#8216;dc=example,dc=com&#8217; -t uid:eq:pres:sub -t sn</p>
<dd>
<dt>db2index -Z instance3</p>
<dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>db2index was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
