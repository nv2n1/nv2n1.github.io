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
<p>ns-accountstatus.pl [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } [-p port] [-h host] [-P protocol] {-I DN |<br/>
&nbsp;<wbr>-b basedn -f filter&nbsp;<wbr>[-s scope]}&nbsp;<wbr>[-i]&nbsp;<wbr>[-g seconds]</p>
<h2>Description</h2>
<p>Provides account status information to establish whether an entry or group of entries is inactivated.</p>
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
<dt><code>-I</code> <i>DN</i></dt>
<dd>Specifies the entry DN or role DN whose status is required.</dd>
<dt><code>-h</code> <i>host</i></dt>
<dd>Host name of the Directory Server.</dd>
<dt><code>-p</code> <i>port</i></dt>
<dd>Port number of the Directory Server.</dd>
<dt><code>-b</code> <i>basedn</i></dt>
<dd>The suffix DN from which to search from.</dd>
<dt><code>-f</code> <i>filter</i></dt>
<dd>The search filter used to find user entries.</dd>
<dt><code>-s</code> <i>scope</i></dt>
<dd>The search scope. &quot;base&quot;, &quot;one, &quot;sub&quot;. Default is &quot;sub&quot;</dd>
<dt><code>-i</code></dt>
<dd>Only list entries that are inactivated.</dd>
<dt><code>-g</code> <i>seconds</i></dt>
<dd>Only display entries that will become inactive within the timeframe. </dd>
</dl>
<h2>Example</h2>
<dl>
<dt>ns-accountstatus.pl -Z instance3 -D &#8216;cn=directory manager&#8217; -w password -I &#8216;uid=user,ou=people,dc=example,dc=com&#8217;</dt>
<dd>
</dd><dt>ns-accountstatus.pl -Z instance3 -D &#8216;cn=directory manager&#8217; -w password -b &#8216;dc=example,dc=com&#8217; -f &quot;(uid=*)&quot;</dt>
<dd>
</dd><dt>ns-accountstatus.pl -Z instance3 -D &#8216;cn=directory manager&#8217; -w password -b &#8216;dc=example,dc=com&#8217; -f &quot;(uid=*)&quot; -g 86400</dt>
<dd>
</dd><dt>ns-accountstatus.pl -w password -I &#8216;uid=user,ou=people,dc=example,dc=com&#8217; -P STARTTLS</dt>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>ns-accountstatus.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2016 Red Hat, Inc.</p>
