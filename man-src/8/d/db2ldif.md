---
title: "db2ldif(8)"
name: "db2ldif"
section: "8"
letter: "d"
url: "/docs/linux/man/8-db2ldif/"
description: "db2ldif – Directory Server script for exporting the database"
---

<p>db2ldif &#8211; Directory Server script for exporting the database</p>
<h2>Synopsis</h2>
<p>db2ldif [-Z serverID] {-n backend_instance}* | {-s includeSuffix}* [{-x excludeSuffix}*] [-a outputFile] [-m] [-M] [-r] [-u] [-U] [-C] [-N] [-E] [-1] [-q] [-h]</p>
<h2>Description</h2>
<p>Exports the contents of the database to a LDIF file. This script can be executed while the server is still running, except when using the -r option.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-n</code> <i>Backend Name</i></p>
<dd>The name of the LDBM database to reindex. Example: userRoot</p>
<dt><code>-s</code> <i>includeSuffix</i></p>
<dd>Specifies suffixes to be included in the LDIF file.</p>
<dt><code>-x</code> <i>excludeSuffix</i></p>
<dd>Specifies suffixes to be excluded from the LDIF file.</p>
<dt><code>-a</code> <i>Output File</i></p>
<dd>The name for the LDIF file.</p>
<dt><code>-m</code></p>
<dd>Minimize the base64 encodings in the exported LDIF file.</p>
<dt><code>-M</code></p>
<dd>Exported ldif is stored in multiple files. These files are named : &lt;instance&gt;_&lt;filename&gt;<br />
 By default, all instances are stored in the filename specified by the -a option.</p>
<dt><code>-r</code></p>
<dd>Export replication data(information required to initialize a replica when the LDIF is imported).</p>
<dt><code>-u</code></p>
<dd>Do not export the unique-id attribute.</p>
<dt><code>-U</code></p>
<dd>Requests that the output LDIF is not folded.</p>
<dt><code>-C</code></p>
<dd>Uses only the main database file.</p>
<dt><code>-N</code></p>
<dd>Suppress printing sequential number</p>
<dt><code>-E</code></p>
<dd>Decrypts any encrypted data during export.</p>
<dt><code>-1</code></p>
<dd>Deletes, for reasons of backward compatibility, the first line of the LDIF file that gives the version of the LDIF standard.</p>
<dt><code>-q</code></p>
<dd>Quiet mode. Suppresses output of the script.</p>
<dt><code>-h</code></p>
<dd>Display the usage.</dl>
<h2>Example</h2>
<dl>
<dt>db2ldif -Z instance3 -n userRoot -a /LDAP/ldif/export.ldif</p>
<dd>
<dt>db2ldif -s &#8216;dc=example,dc=com&#8217; -a /LDAP/ldif/export.ldif -m -E -q</p>
<dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>db2ldif was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
