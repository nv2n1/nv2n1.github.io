---
title: "ns-newpwpolicy-pl(8)"
name: "ns-newpwpolicy-pl"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ns-newpwpolicy-pl/"
description: "ns-newpwpolicy.pl – Directory Server perl script for preparing new password policies."
---

<p>ns-newpwpolicy.pl &#8211; Directory Server perl script for preparing new password policies.</p>
<h2>Synopsis</h2>
<p>ns-newpwpolicy.pl [-Z serverID] [-v] [-D rootdn] { -w password | -j filename } [-P protocol] [-p port] [-h host] -U UserDN -S SuffixDN</p>
<h2>Description</h2>
<p>Adds entries required for implementing the user- and subtree-level password policy.</p>
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
<dt><code>-P</code> <i>Protocol</i></dt>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</dd>
<dt><code>-h</code> <i>host</i></dt>
<dd>Host name of the Directory Server.</dd>
<dt><code>-p</code> <i>port</i></dt>
<dd>Port number of the Directory Server.</dd>
<dt><code>-U</code> <i>userDN</i></dt>
<dd>Specifies the DN of the user entry that needs to be updated with user-level password policy attributes.</dd>
<dt><code>-S</code> <i>suffixDN</i></dt>
<dd>Specifies the DN of the suffix entry that needs to be updated with subtree-level password policy attributes.</dd>
<dt><code>-v</code></dt>
<dd>Display verbose output</dd></dl>
<h2>Example</h2>
<dl>
<dt>ns-newpwpolicy.pl -Z instance3 -D &#8216;cn=directory manager&#8217; -w password -P STARTTLS -U &#8216;uid=user,ou=people,dc=example,dc=com&#8217;</dt>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>ns-newpwpolicy.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
