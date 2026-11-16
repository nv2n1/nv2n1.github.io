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
<dt><code>-b</code> <i>basedn</i></dt>
<dd>The replicated suffix that needs to be cleaned.</dd>
<dt><code>-r</code> <i>rid</i></dt>
<dd>The replica ID that needs to be removed.</dd>
<dt><code>-P</code> <i>Protocol</i></dt>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</dd>
<dt><code>-A</code></dt>
<dd>Abort a cleanAllRUV task that is currently running.</dd>
<dt><code>-v</code></dt>
<dd>Display verbose output</dd>
<dt><code>-h</code></dt>
<dd>Display usage</dd></dl>
<h2>Example</h2>
<dl>
<dt>cleanallruv.pl -Z instance1 -D &#8216;cn=directory manager&#8217; -j /tmp/pw.txt -b &#8216;dc=example,dc=com&#8217; -r 87 -P STARTTLS</dt>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dd>
<dt>cleanallruv.pl -j /export/rootdnpw.txt -b &#8216;dc=example,dc=com&#8217; -A -r 87</dt>
<dd></dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>cleanallruv.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
