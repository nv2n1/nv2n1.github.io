---
title: "schema-reload-pl(8)"
name: "schema-reload-pl"
section: "8"
letter: "s"
url: "/docs/linux/man/8-schema-reload-pl/"
description: "schema-reload.pl – Directory Server perl script for updating the schema."
---

<p>schema-reload.pl &#8211; Directory Server perl script for updating the schema.</p>
<h2>Synopsis</h2>
<p>schema-reload.pl [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } [-P protocol] [-d schemadir] [-v] [-h]</p>
<h2>Description</h2>
<p>Manually reloads the schema files used by the Directory Server instance, either in the default location, or in user-specified locations.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></dt>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</dd>
<dt><code>-D</code> <i>Root DN</i></dt>
<dd>The Directory Manager DN, or root DN. If not specified, the script will search the server instance configuration for the value.</dd>
<dt><code>-w</code> <i>password</i></dt>
<dd>The rootdn password.</dd>
<dt><code>-w &#8211;</code></dt>
<dd>Prompt for the rootdn password.</dd>
<dt><code>-j</code> <i>password filename</i></dt>
<dd>The name of the file that contains the root DN password.</dd>
<dt><code>-d</code> <i>schemadir</i></dt>
<dd>Gives the full path to the directory where the schema file is located. If this is not specified, the script uses the default schema directory, /etc/dirsrv/schema.</dd>
<dt><code>-P</code> <i>protocol</i></dt>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</dd>
<dt><code>-v</code></dt>
<dd>Display verbose output</dd>
<dt><code>-h</code></dt>
<dd>Display usage</dd></dl>
<h2>Example</h2>
<dl>
<dt>schema-reload.pl -Z instance3 -D &#8216;cn=directory manager&#8217; -w password -P STARTTLS -d /LDAP/schema/</dt>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>schema-reload.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
