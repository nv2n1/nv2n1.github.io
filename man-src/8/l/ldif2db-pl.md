---
title: "ldif2db-pl(8)"
name: "ldif2db-pl"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ldif2db-pl/"
description: "ldif2db.pl – Directory Server perl script for importing a LDIF file"
---

<p>ldif2db.pl &#8211; Directory Server perl script for importing a LDIF file</p>
<h2>Synopsis</h2>
<p>ldif2db.pl -n backend [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } [-P protocol] {-s includeSuffix}* [{-x excludeSuffix}*] [-O] [-c chunksize] [-v] [-h] [-g [string]] [-G namespace_id] {-i filename}*</p>
<h2>Description</h2>
<p>Imports LDIF file(s) into the server. Either the option &#8216;-n&#8217; or &#8216;-s&#8217; must be used. This script creates an entry in the directory that launches this dynamic task.</p>
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
<dd>Specifies the suffixes to be included or specifies the subtrees to be included.</p>
<dt><code>-x</code> <i>excludeSuffix</i></p>
<dd>Specifies the suffixes to be excluded or specifies the subtrees to be excluded.</p>
<dt><code>-i</code> <i>filename</i></p>
<dd>Name for the LDIF file to import.</p>
<dt><code>-g</code> <i>[string]</i></p>
<dd>Generates a unique ID. Type none for no unique ID to be generated and deterministic for the generated unique ID to be name-based. By default, a time-based unique ID is generated. When using the deterministic generation to have a name-based unique ID, it is also possible to specify the namespace for the server to use, as follows: </p>
<p> -g deterministic namespaceId </p>
<p> namespaceId is a string of characters in the format 00-xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxxxxx.</p>
<dt><code>-G</code> <i>namespace_id</i></p>
<dd>Generates a namespace ID as a name-based unique ID. This is the same as specifying the -g deterministic option.</p>
<dt><code>-P</code> <i>Protocol</i></p>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</p>
<dt><code>-O</code></p>
<dd>Requests that only the core database is created without attribute indexes.</p>
<dt><code>-c</code> <i>Chunk size</i></p>
<dd>The number of entries to process before starting a fresh pass during the import. By default this is handled internally by the server.</p>
<dt><code>-v</code></p>
<dd>Display verbose output</p>
<dt><code>-h</code></p>
<dd>Display usage</dl>
<h2>Example</h2>
<dl>
<dt>ldif2db.pl -Z instance1 -n userRoot -i /LDAP/ldif/data.ldif</p>
<dd>
<dt>ldif2db.pl -s &quot;dc=example,dc=com&quot; -i /LDAP/ldif/data.ldif -D &#8216;cn=directory manager&#8217; -w password -P STARTTLS</p>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>ldif2db.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
