---
title: "ldif2ldap(8)"
name: "ldif2ldap"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ldif2ldap/"
description: "ldif2ldap – Directory Server script for adding entries"
---

<p>ldif2ldap &#8211; Directory Server script for adding entries</p>
<h2>Synopsis</h2>
<p>ldif2ldap [-Z serverID] [-D &lt;rootdn&gt;] -w &lt;password&gt; -f &lt;ldifFile&gt; [-P protocol] [-h]</p>
<h2>Description</h2>
<p>Performs an import operation over LDAP to the Directory Server. To run this script, the server must be running.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-D</code> <i>Root DN</i></p>
<dd>The Directory Manager DN, or root DN. If not specified, the script will search the server instance configuration for the value.</p>
<dt><code>-w</code> <i>password</i></p>
<dd>The rootdn password.</p>
<dt><code>-f</code> <i>LDIF file</i></p>
<dd>The LDIF file with the entries to add.</p>
<dt><code>-P</code> <i>Protocol</i></p>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</p>
<dt><code>-h</code></p>
<dd>Display the usage.</dl>
<h2>Example</h2>
<p>ldif2ldap -Z instance3 -D &#8216;cn=directory manager&#8217; -w password -f /LDAP/ldif/entries.ldif -P STARTTLS </p>
<p> Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</p>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>ldif2ldap was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
