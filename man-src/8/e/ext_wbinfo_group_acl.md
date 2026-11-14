---
title: "ext_wbinfo_group_acl(8)"
name: "ext_wbinfo_group_acl"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ext_wbinfo_group_acl/"
---

<pre> ext_wbinfo_group_acl - external ACL helper for Squid to verify NT Domain group membership using wbinfo.</pre>
<h2>Synopsis</h2>
<pre> ext_wbinfo_group_acl [-dhK]</pre>
<h2>Description</h2>
<p><code>ext_wbinfo_group_acl</code> is an installed executable script. It uses <code>wbinfo</code> from Samba to lookup group membership of logged in users. </p>
<p> This helper must be used in with an authentication scheme (typically Basic or <font SIZE="-1">NTLM</font>) based on Windows <font SIZE="-1">NT/2000</font> domain users. </p>
<p> It reads from the standard input the domain username and a list of groups and tries to match each against the groups membership of the specified username.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Write debug info to stderr.</p>
<dt><code>-h</code></p>
<dd>Print the help.</p>
<dt><code>-K</code></p>
<dd>Downgrade Kerberos credentials to <font SIZE="-1">NTLM.</font></dl>
<h2>Configuration</h2>
<pre> external_acl_type wbinfo_check %LOGIN /path/to/ext_wbinfo_group_acl
 acl allowed_group external wbinfo_check Group1 Group2
 http_access allow allowed_group</pre>
<p>If the local perl interpreter is in a unusual location it may need to be added: </p>
<pre> external_acl_type wbinfo_check %LOGIN /path/to/perl /path/to/ext_wbinfo_group_acl</pre>
<h2>Author</h2>
<p>This program was written by Jerry Murdock &lt;jmurdock [at] itraktech.com&gt; </p>
<p> This manual was written by Amos Jeffries &lt;amosjeffries [at] squid-cache.org&gt;</p>
<h2>Copyright</h2>
<pre> * Copyright (C) 1996-2016 The Squid Software Foundation and contributors
 *
 * Squid software is distributed under GPLv2+ license and includes
 * contributions from numerous individuals and organizations.
 * Please see the COPYING and CONTRIBUTORS files for details.
 This program is put in the public domain by Jerry Murdock
 &lt;jmurdock [at] itraktech.com&gt;. It is distributed in the hope that it will
 be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
 of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</pre>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list &lt;squid-users [at] squid-cache.org</i>&gt;</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org</i>&gt; </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list &lt;squid-dev [at] squid-cache.org</i>&gt;</p>
<h2>See Also</h2>
<p>The Squid <font SIZE="-1">FAQ</font> wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a> The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
