---
title: "ns-accountstatus-pl(8)"
name: "ns-accountstatus-pl"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ns-accountstatus-pl/"
description: "ns-accountstatus.pl – Directory Server perl script for checking the status of entries."
---

<p>ns-accountstatus.pl &#8211; Directory Server perl script for checking the status of entries.</p>
<h2>Synopsis</h2>
<p>ns-accountstatus.pl [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } [-p port] [-h host] [-P protocol] {-I DN |<br />
&nbsp;<wbr>-b basedn -f filter&nbsp;<wbr>[-s scope]}&nbsp;<wbr>[-i]&nbsp;<wbr>[-g seconds]</p>
<h2>Description</h2>
<p>Provides account status information to establish whether an entry or group of entries is inactivated.</p>
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
<dt><code>-P</code> <i>Protocol</i></p>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</p>
<dt><code>-I</code> <i>DN</i></p>
<dd>Specifies the entry DN or role DN whose status is required.</p>
<dt><code>-h</code> <i>host</i></p>
<dd>Host name of the Directory Server.</p>
<dt><code>-p</code> <i>port</i></p>
<dd>Port number of the Directory Server.</p>
<dt><code>-b</code> <i>basedn</i></p>
<dd>The suffix DN from which to search from.</p>
<dt><code>-f</code> <i>filter</i></p>
<dd>The search filter used to find user entries.</p>
<dt><code>-s</code> <i>scope</i></p>
<dd>The search scope. &quot;base&quot;, &quot;one, &quot;sub&quot;. Default is &quot;sub&quot;</p>
<dt><code>-i</code></p>
<dd>Only list entries that are inactivated.</p>
<dt><code>-g</code> <i>seconds</i></p>
<dd>Only display entries that will become inactive within the timeframe. </p>
</dl>
<h2>Example</h2>
<dl>
<dt>ns-accountstatus.pl -Z instance3 -D &#8216;cn=directory manager&#8217; -w password -I &#8216;uid=user,ou=people,dc=example,dc=com&#8217;</p>
<dd>
<dt>ns-accountstatus.pl -Z instance3 -D &#8216;cn=directory manager&#8217; -w password -b &#8216;dc=example,dc=com&#8217; -f &quot;(uid=*)&quot;</p>
<dd>
<dt>ns-accountstatus.pl -Z instance3 -D &#8216;cn=directory manager&#8217; -w password -b &#8216;dc=example,dc=com&#8217; -f &quot;(uid=*)&quot; -g 86400</p>
<dd>
<dt>ns-accountstatus.pl -w password -I &#8216;uid=user,ou=people,dc=example,dc=com&#8217; -P STARTTLS</p>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>ns-accountstatus.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2016 Red Hat, Inc.</p>
