---
title: "basic_sasl_auth(8)"
name: "basic_sasl_auth"
section: "8"
letter: "b"
url: "/docs/linux/man/8-basic_sasl_auth/"
description: "basic_sasl_auth – Basic Authentication using SASL (specifically the cyrus-sasl authentication method)"
---

<p>basic_sasl_auth &#8211; Basic Authentication using SASL (specifically the cyrus-sasl authentication method) </p>
<p> Version 1.0</p>
<h2>Synopsis</h2>
<p><code>basic_sasl_auth</code></p>
<h2>Description</h2>
<p><code>basic_sasl_auth</code> is an installed binary helper for Squid. SASL is configurable (somewhat like PAM). Each service authenticating against SASL identifies itself with an application name. Each application can be configured independently by the SASL administrator.</p>
<h2>Configuration</h2>
<p>To configure the authentication method used the file <code>basic_sasl_auth.conf</code> can be placed in the appropriate location, usually <code>/usr/lib/sasl.</code> </p>
<p> The authentication database is defined by the <code>pwcheck_method </code> parameter. Only the <code>PLAIN </code> authentication mechanism is used. </p>
<p> Examples: <code>pwcheck_method:sasldb</code> use sasldb &#8211; the default if no conf file is installed. <code>pwcheck_method:pam</code><br />
&nbsp;<wbr>&#8211; use PAM authentication database <code>pwcheck_method:passwd</code><br />
&nbsp;<wbr>&#8211; use traditional&nbsp;<wbr> <code>/etc/passwd</code> <code>pwcheck_method:shadow</code><br />
&nbsp;<wbr>&#8211; use slightly less traditional&nbsp;<wbr>/etc/shadow </p>
<p> Others methods may be supported by your cyrus-sasl implementation &#8211; consult your cyrus-sasl documentation for information. </p>
<p> Typically the authentication database ( <code>/etc/sasldb</code> , <code>/etc/shadow</code> , <code>PAM</code> ) can not be accessed by a normal user. You should use setuid/setgid and an appropriate user/group on the executable to allow the authenticator to access the appropriate password database. If the access to the database is not permitted then the authenticator will typically fail with &quot;-1, generic error&quot;. </p>
<dl>
<dd><code>chown root.mail basic_sasl_auth</code><br />
 <code>chmod ug+s basic_sasl_auth</code></dl>
<p> If the application name <code>basic_sasl_auth</code> will also be used for the PAM service name if <code>pwcheck_method:pam</code> is chosen. And example PAM configuration file <code>basic_sasl_auth.pam</code> is also included.</p>
<h2>Author</h2>
<p>This program was written by <i>Ian Castle &lt;ian.castle [at] coldcomfortfarm.net&gt;</i> </p>
<p> This manual was written by <i>Ian Castle &lt;ian.castle [at] coldcomfortfarm.net&gt;</i> <i>Amos Jeffries &lt;amosjeffries [at] squid-cache.org&gt;</i></p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
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
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/3-sasl/">SASL</a></code>(3), <code><a href="/docs/linux/man/7-pam/">PAM</a></code>(7), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
