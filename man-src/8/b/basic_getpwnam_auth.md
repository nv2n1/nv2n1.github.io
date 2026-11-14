---
title: "basic_getpwnam_auth(8)"
name: "basic_getpwnam_auth"
section: "8"
letter: "b"
url: "/docs/linux/man/8-basic_getpwnam_auth/"
description: "basic_getpwnam_auth – Local Users auth helper for Squid"
---

<p>basic_getpwnam_auth &#8211; Local Users auth helper for Squid</p>
<h2>Synopsis</h2>
<p><code>basic_getpwnam_auth</code></p>
<h2>Description</h2>
<p><code>basic_getpwnam_auth</code> allows Squid to authenticate any local user accounts to validate the user name and password of Basic HTTP authentication. </p>
<p> It uses <code>getpwnam()</code> and <code>getspnam()</code> routines for authentication. </p>
<p> This has the following advantages over the NCSA module:</p>
<dl>
<dt>&#8211; Allows authentication of all known local users</p>
<dd>
<dt>&#8211; Allows authentication through nsswitch.conf</p>
<dd>
<dt>&#8211; Can handle NIS(+) requests</p>
<dd>
<dt>&#8211; Can handle LDAP requests</p>
<dd>
<dt>&#8211; Can handle PAM requests</p>
<dd></dl>
<h2>Configuration</h2>
<dl>
<dd><code>auth_param basic program /path/to/basic_getpwnam_auth</code><br />
 <code>auth_param basic children concurrency=1</code></dl>
<p> When used for authenticating to local UNIX shadow password databases the program must be running as root or else it won&#8217;t have sufficient permissions to access the user password database. Such use of this program is not recommended, but if you absolutely need to then make the program <code>setuid</code> <code>root</code></p>
<dl>
<dd><code>chown root basic_getpwnam_auth</code><br />
 <code>chmod u+s basic_getpwnam_auth</code></dl>
<p> Please note that in such configurations it is also strongly recommended that the program is moved into a directory where normal users cannot access it, as this mode of operation will allow any local user to brute-force other users passwords. Also note the program has not been fully audited and the author cannot be held responsible for any security issues due to such installations.</p>
<h2>Author</h2>
<p>This program was written by <i>Erik Hofman &lt;erik.hofman [at] a1.nl&gt;</i> <i>Robin Elfrink &lt;robin [at] a1.nl&gt;</i> <i>Giancarlo Razzolini &lt;linux-fan [at] onda.com.br&gt;</i> </p>
<p> Based on original code by <i>Jon Thackray &lt;jrmt [at] uk.gdscorp.com&gt;.</i> </p>
<p> This manual was written by <i>Amos Jeffries &lt;amosjeffries [at] squid-cache.org&gt;</i></p>
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
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/8-basic_pam_auth/">basic_pam_auth</a></code>(8), <code><a href="/docs/linux/man/8-basic_ncsa_auth/">basic_ncsa_auth</a></code>(8), <code><a href="/docs/linux/man/8-basic_ldap_auth/">basic_ldap_auth</a></code>(8), <code><a href="/docs/linux/man/8-basic_nis_auth/">basic_nis_auth</a></code>(8), <code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5), <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), <code><a href="/docs/linux/man/3-getspnam/">getspnam</a></code>(3), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
