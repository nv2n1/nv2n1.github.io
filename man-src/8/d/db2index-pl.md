---
title: "db2index-pl(8)"
name: "db2index-pl"
section: "8"
letter: "d"
url: "/docs/linux/man/8-db2index-pl/"
description: "db2index.pl – Directory Server perl script for indexing a database"
---

<p>db2index.pl &#8211; Directory Server perl script for indexing a database</p>
<h2>Synopsis</h2>
<p>db2index.pl [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } [-n backendname] [-P protocol] [-t attributeName[:indextypes[:matchingrules]]] [-T vlvTag] [-v] [-h]</p>
<h2>Description</h2>
<p>Indexes attributes in the specified database. If no attributes are specified, then all the attribute indexes will be regenerated. The Directory Server must be started prior to running this script.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-D</code> <i>Root DN</i></p>
<dd>The Directory Manager DN, or root DN. If not specified, the script will search the server instance configuration for the value.</p>
<dt><code>-w</code> <i>password</i></p>
<dd>The rootdn password.</p>
<dt><code>-w &#8211;</code></p>
<dd>Prompt for the rootdn password.</p>
<dt><code>-j</code> <i>password filename</i></p>
<dd>The name of the file that contains the root DN password.</p>
<dt><code>-n</code> <i>Backend Name</i></p>
<dd>The name of the LDBM database to restore. Example: userRoot</p>
<dt><code>-t</code> <i>attributeName[:indextypes[:matchingrules]]</i></p>
<dd>The attribute to index. Optionally you can specify a comma separated list of index types: eq, sub, pres, and approx. An optional matching rule OID can also be set.</p>
<dt><code>-T</code> <i>vlvTag</i></p>
<dd>This is the name of the vlv index entry under cn=config.</p>
<dt><code>-P</code> <i>Protocol</i></p>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</p>
<dt><code>-v</code></p>
<dd>Display verbose output</p>
<dt><code>-h</code></p>
<dd>Display usage</dl>
<h2>Example</h2>
<dl>
<dt>db2index.pl -n userRoot -D &#8216;cn=directory manager&#8217; -w password -t uid:eq,pres,sub:1.3.6.1.4.1.42.2.27.9.4.76.1 -t cn:eq,pres</p>
<dd>
<dt>db2index.pl -Z instance3</p>
<dd>
<dt>db2index.pl -Z instance2 -w password -s &#8216;dc=example,dc=com&#8217; -t uid:eq:pres:sub -t sn -P STARTTLS</p>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>db2index.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
