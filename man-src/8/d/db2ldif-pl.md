---
title: "db2ldif-pl(8)"
name: "db2ldif-pl"
section: "8"
letter: "d"
url: "/docs/linux/man/8-db2ldif-pl/"
description: "db2ldif.pl – Directory Server perl script for exporting a database to a LDIF file"
---

<p>db2ldif.pl &#8211; Directory Server perl script for exporting a database to a LDIF file</p>
<h2>Synopsis</h2>
<p>db2ldif.pl [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j pwfilename } [-P protocol] {-n backendname}* | {-s includeSuffix}* [{-x excludeSuffix}*] [-m] [-M] [-r] [-u] [-C] [-N] [-E] [-1] [-U] [-a filename] [-v] [-h]</p>
<h2>Description</h2>
<p>Exports the contents of the database to LDIF. This script creates an entry in the directory that launches this dynamic task.</p>
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
<dt><code>-s</code> <i>includeSuffix</i></p>
<dd>The suffix DN to be included in the exported LDIF file.</p>
<dt><code>-x</code> <i>excludeSuffix</i></p>
<dd>The suffix DN to be excluded from the exported LDIF file.</p>
<dt><code>-a</code> <i>filename</i></p>
<dd>Name for the exported LDIF file.</p>
<dt><code>-P</code> <i>Protocol</i></p>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</p>
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
<dt><code>-v</code></p>
<dd>Display verbose output</p>
<dt><code>-h</code></p>
<dd>Display usage</dl>
<h2>Example</h2>
<dl>
<dt>db2ldif.pl -Z instance3 -n userRoot -a /LDAP/ldif/export.ldif -P STARTTLS</p>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</p>
<dt>db2ldif.pl -s &#8216;dc=example,dc=com&#8217; -a /LDAP/ldif/export.ldif -m -E -q</p>
<dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>db2ldif.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
