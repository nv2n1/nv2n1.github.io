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
<dt><code>-Z</code> <i>Server Identifier</i></dt>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</dd>
<dt><code>-n</code> <i>Backend Name</i></dt>
<dd>The name of the LDBM database to reindex. Example: userRoot</dd>
<dt><code>-s</code> <i>includeSuffix</i></dt>
<dd>Specifies suffixes to be included in the LDIF file.</dd>
<dt><code>-x</code> <i>excludeSuffix</i></dt>
<dd>Specifies suffixes to be excluded from the LDIF file.</dd>
<dt><code>-a</code> <i>Output File</i></dt>
<dd>The name for the LDIF file.</dd>
<dt><code>-m</code></dt>
<dd>Minimize the base64 encodings in the exported LDIF file.</dd>
<dt><code>-M</code></dt>
<dd>Exported ldif is stored in multiple files. These files are named : &lt;instance&gt;_&lt;filename&gt;<br />
 By default, all instances are stored in the filename specified by the -a option.</dd>
<dt><code>-r</code></dt>
<dd>Export replication data(information required to initialize a replica when the LDIF is imported).</dd>
<dt><code>-u</code></dt>
<dd>Do not export the unique-id attribute.</dd>
<dt><code>-U</code></dt>
<dd>Requests that the output LDIF is not folded.</dd>
<dt><code>-C</code></dt>
<dd>Uses only the main database file.</dd>
<dt><code>-N</code></dt>
<dd>Suppress printing sequential number</dd>
<dt><code>-E</code></dt>
<dd>Decrypts any encrypted data during export.</dd>
<dt><code>-1</code></dt>
<dd>Deletes, for reasons of backward compatibility, the first line of the LDIF file that gives the version of the LDIF standard.</dd>
<dt><code>-q</code></dt>
<dd>Quiet mode. Suppresses output of the script.</dd>
<dt><code>-h</code></dt>
<dd>Display the usage.</dd></dl>
<h2>Example</h2>
<dl>
<dt>db2ldif -Z instance3 -n userRoot -a /LDAP/ldif/export.ldif</dt>
<dd>
</dd><dt>db2ldif -s &#8216;dc=example,dc=com&#8217; -a /LDAP/ldif/export.ldif -m -E -q</dt>
<dd></dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>db2ldif was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
