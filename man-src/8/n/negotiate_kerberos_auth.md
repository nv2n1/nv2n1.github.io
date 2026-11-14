---
title: "negotiate_kerberos_auth(8)"
name: "negotiate_kerberos_auth"
section: "8"
letter: "n"
url: "/docs/linux/man/8-negotiate_kerberos_auth/"
description: "negotiate_kerberos_auth – Squid kerberos based authentication helper"
---

<p>negotiate_kerberos_auth &#8211; Squid kerberos based authentication helper </p>
<p> Version 3.0.4sq</p>
<h2>Synopsis</h2>
<p><code>negotiate_kerberos_auth</code> <code>[-h] [-d] [-i] [-r] [-s Service-Principal-Name] [-k Keytab-Name] [-c Replay-Cache-Directory] [-t Replay-Cache-Type] </code></p>
<h2>Description</h2>
<p><code>negotiate_kerberos_auth</code> is an installed binary and allows Squid to authenticate users via the Negotiate protocol and Kerberos. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Display the binary help and command line syntax info using stderr.</p>
<dt><code>-d</code></p>
<dd>Write debug messages to stderr.</p>
<dt><code>-i</code></p>
<dd>Write informational messages to stderr.</p>
<dt><code>-r </code></p>
<dd>Remove realm from username before returning the username to squid.</p>
<dt><code>-s Service-Principal-name</code></p>
<dd>Provide Service Principal Name.</p>
<dt><code>-k Keytab-Name</code></p>
<dd>Provide Kerberos Keytab Name (Default: /etc/krb5.keytab)</p>
<dt><code>-c Replay-Cache-Directory</code></p>
<dd>Provide Replay Cache Directory (Default: /var/tmp)</p>
<dt><code>-t Replay-Cache-Type</code></p>
<dd>Provide Replay Cache Type (Default: dfl)</dl>
<h2>Configuration</h2>
<p>This helper is intended to be used as an <code>authentication</code> helper in <code>squid.conf.</code> </p>
<pre>auth_param negotiate program /path/to/negotiate_kerberos_auth<br>
auth_param negotiate children 10<br>
auth_param negotiate keep_alive on</pre>
<p><code>NOTE:</code> The following squid startup file modification may be required: </p>
<p> Add the following lines to the squid startup script to point squid to a keytab file which contains the HTTP/fqdn service principal for the default Kerberos domain. The keytab name can also be provided by the -k &lt;keytab name&gt; option. The fqdn must be the proxy name set in IE<br />
&nbsp;<wbr>or firefox. You can not use an IP address. </p>
<p> KRB5_KTNAME=/etc/squid/HTTP.keytab export KRB5_KTNAME </p>
<p> If you use a different Kerberos domain than the machine itself is in you can point squid to the seperate Kerberos config file by setting the following environmnet variable in the startup script. </p>
<p> KRB5_CONFIG=/etc/krb5-squid.conf export KRB5_CONFIG </p>
<p> Kerberos can keep a replay cache to detect the reuse of Kerberos tickets (usually only possible in a 5 minute window) . If squid is under high load with Negotiate(Kerberos) proxy authentication requests the replay cache checks can create high CPU load. If the environment does not require high security the replay cache check can be disabled for MIT based Kerberos implementations by adding the below to the startup script or use the -t none option. </p>
<p> KRB5RCACHETYPE=none export KRB5RCACHETYPE </p>
<p> If negotiate_kerberos_auth doesn&#8217;t determine for some reason the right service principal you can provide it with -s HTTP/fqdn. </p>
<p> If you serve multiple Kerberos realms add a HTTP/fqdn [at] REALM service principal per realm to the HTTP.keytab file and use the -s GSS_C_NO_NAME option with negotiate_kerberos_auth.</p>
<h2>Author</h2>
<p>This program was written by <i>Markus Moeller &lt;markus_moeller [at] compuserve.com&gt;</i> </p>
<p> This manual was written by <i>Markus Moeller &lt;markus_moeller [at] compuserve.com&gt;</i></p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2014 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details. </p>
<p> This program and documentation is copyright to the authors named above. </p>
<p> Distributed under the GNU General Public License (GNU GPL) version 2 or later (GPLv2+).</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt;</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8) <code><a href="/docs/linux/man/8-ext_kerberos_ldap_group_acl/">ext_kerberos_ldap_group_acl</a></code>(8)<br />
 <code>RFC4559</code> &#8211; SPNEGO-based Kerberos and NTLM HTTP Authentication in Microsoft Windows,<br />
 <code>RFC2478</code> &#8211; The Simple and Protected GSS-API Negotiation Mechanism,<br />
 <code>RFC1964</code> &#8211; The Kerberos Version 5 GSS-API Mechanism,<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> <a rel="nofollow" href="http://wiki.squid-cache.org/ConfigExamples/Authenticate/Kerberos">http://wiki.squid-cache.org/ConfigExamples/Authenticate/Kerberos</a> </p>
