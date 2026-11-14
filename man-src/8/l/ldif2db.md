---
title: "ldif2db(8)"
name: "ldif2db"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ldif2db/"
description: "ldif2db – Directory Server script for importing a LDIF file"
---

<p>ldif2db &#8211; Directory Server script for importing a LDIF file</p>
<h2>Synopsis</h2>
<p>ldif2db [-Z serverID] -n backendname {-s includesuffix}* [{-x excludesuffix}*] [-g [string] [-G namespace_id]] {-i ldiffile}* [-c chunksize] [-O] [-E] [-q] [-h]</p>
<h2>Description</h2>
<p>Imports a LDIF file. Either the option &#8216;-n&#8217; or &#8216;-s&#8217; must be used. The server instance must be stopped prior to running this command.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-n</code> <i>Backend Name</i></p>
<dd>The name of the LDBM database to restore. Example: userRoot</p>
<dt><code>-s</code> <i>includeSuffix</i></p>
<dd>Specifies the suffixes to be included or specifies the subtrees to be included.</p>
<dt><code>-x</code> <i>excludeSuffix</i></p>
<dd>Specifies the suffixes to be excluded or specifies the subtrees to be excluded.</p>
<dt><code>-i</code> <i>filename</i></p>
<dd>Name for the LDIF file to import.</p>
<dt><code>-c</code> <i>Chunk size</i></p>
<dd>The number of entries to process before starting a fresh pass during the import. By default this is handled internally by the server.</p>
<dt><code>-O</code></p>
<dd>Requests that only the core database is created without attribute indexes.</p>
<dt><code>-g</code> <i>[string]</i></p>
<dd>Generates a unique ID. Type none for no unique ID to be generated and deterministic for the generated unique ID to be name-based. By default, a time-based unique ID is generated. When using the deterministic generation to have a name-based unique ID, it is also possible to specify the namespace for the server to use, as follows: </p>
<p> -g deterministic namespaceId </p>
<p> namespaceId is a string of characters in the format 00-xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxxxxx.</p>
<dt><code>-G</code> <i>namespace_id</i></p>
<dd>Generates a namespace ID as a name-based unique ID. This is the same as specifying the -g deterministic option.</p>
<dt><code>-E</code></p>
<dd>Encrypts data during import. This option is used only if database encryption is enabled.</p>
<dt><code>-v</code></p>
<dd>Display verbose output</p>
<dt><code>-h</code></p>
<dd>Display usage</dl>
<h2>Example</h2>
<dl>
<dt>ldif2db -Z instance1 -n userRoot -i /LDAP/ldif/data.ldif</p>
<dd>
<dt>ldif2db -s &quot;dc=example,dc=com&quot; -i /LDAP/ldif/data.ldif</p>
<dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>ldif2db was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
