---
title: "cleanallruv-pl(8)"
name: "cleanallruv-pl"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cleanallruv-pl/"
description: "cleanallruv.pl – Directory Server perl script for issuing a cleanAllRUV task"
---

<p>cleanallruv.pl &#8211; Directory Server perl script for issuing a cleanAllRUV task</p>
<h2>Synopsis</h2>
<p>cleanallruv.pl [-v] [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } -b basedn -r rid [-A] [-P protocol] [-h]</p>
<h2>Description</h2>
<p>Creates and adds a cleanAllRUV task to the Directory Server</p>
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
<dt><code>-b</code> <i>basedn</i></p>
<dd>The replicated suffix that needs to be cleaned.</p>
<dt><code>-r</code> <i>rid</i></p>
<dd>The replica ID that needs to be removed.</p>
<dt><code>-P</code> <i>Protocol</i></p>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</p>
<dt><code>-A</code></p>
<dd>Abort a cleanAllRUV task that is currently running.</p>
<dt><code>-v</code></p>
<dd>Display verbose output</p>
<dt><code>-h</code></p>
<dd>Display usage</dl>
<h2>Example</h2>
<dl>
<dt>cleanallruv.pl -Z instance1 -D &#8216;cn=directory manager&#8217; -j /tmp/pw.txt -b &#8216;dc=example,dc=com&#8217; -r 87 -P STARTTLS</p>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</p>
<dt>cleanallruv.pl -j /export/rootdnpw.txt -b &#8216;dc=example,dc=com&#8217; -A -r 87</p>
<dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>cleanallruv.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
