---
title: "basic_pam_auth(8)"
name: "basic_pam_auth"
section: "8"
letter: "b"
url: "/docs/linux/man/8-basic_pam_auth/"
description: "basic_pam_auth – PAM Basic authentication helper for Squid"
---

<p>basic_pam_auth &#8211; PAM Basic authentication helper for Squid</p>
<h2>Synopsis</h2>
<p><code>basic_pam_auth [-n service name</code> <code>TTL</code> <code>] [-o] [-1]</code></p>
<h2>Description</h2>
<p><code>basic_pam_auth</code> allows Squid to connect to a mostly any available PAM database to validate the user name and password of Basic HTTP authentication.</p>
<h2>Options</h2>
<dl>
<dt><code>-s service-name</code></p>
<dd>Specifies the PAM service name Squid uses, defaults to <code>squid</code></p>
<dt><code>-t TTL</code></p>
<dd>Enables persistent PAM connections where the connection to the PAM database is kept open and reused for new logins. The TTL specifies how long the connection will be kept open (in seconds). Default is to not keep PAM connections open. Please note that the use of persistent PAM connections is slightly outside the PAM specification and may not work with all PAM configurations.</p>
<dt><code>-o</code></p>
<dd>Do not perform the PAM account management group (account expiration etc)</dl>
<h2>Configuration</h2>
<p>The program needs a PAM service to be configured in <code>/etc/pam.conf</code> or <code>/etc/pam.d/squid</code> </p>
<p> The default service name is <code>squid</code> , and the program makes use of the <code>auth</code> and <code>account</code> management groups to verify the password and the accounts validity. </p>
<p> For details on how to configure PAM services, see the PAM documentation for your system. This manual does not cover PAM configuration details.</p>
<h2>Notes</h2>
<p>When used for authenticating to local UNIX shadow password databases the program must be running as root or else it won&#8217;t have sufficient permissions to access the user password database. Such use of this program is not recommended, but if you absolutely need to then make the program setuid root</p>
<dl>
<dd><code>chown root basic_pam_auth</code><br />
 <code>chmod u+s basic_pam_auth</code></dl>
<p> Please note that in such configurations it is also strongly recommended that the program is moved into a directory where normal users cannot access it, as this mode of operation will allow any local user to brute-force other users passwords. Also note the program has not been fully audited and the author cannot be held responsible for any security issues due to such installations.</p>
<h2>Author</h2>
<p>This program and documentation was written by <i>Henrik Nordstrom &lt;hno [at] squid-cache.org&gt;</i></p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details. </p>
<p> Squid <code>basic_pam_auth</code> and this manual is Copyright 1999,2002,2003 <i>Henrik Nordstrom &lt;hno [at] squid-cache.org&gt;</i> Distributed under the GNU General Public License (GNU GPL) version 2 or later (GPLv2+).</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt;</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/3-pam/">pam</a></code>(3), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 PAM Systems Administrator Guide<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
