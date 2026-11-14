---
title: "ext_unix_group_acl(8)"
name: "ext_unix_group_acl"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ext_unix_group_acl/"
description: "ext_unix_group_acl – Squid UNIX Group ACL helper"
---

<p>ext_unix_group_acl &#8211; Squid UNIX Group ACL helper</p>
<h2>Synopsis</h2>
<p><code>ext_unix_group_acl [-d] [-g </code> group <code>] [-g </code> group <code> &#8230;] [-p] [-s]</code></p>
<h2>Description</h2>
<p><code>ext_unix_group_acl</code> allows Squid to base access controls on users memberships in UNIX groups.</p>
<h2>Options</h2>
<dl>
<dt><code>-d </code></p>
<dd>Write debug info to stderr. <code>-g </code><i>group </i> Specifies a group name to match.</p>
<dt><code>-p</code></p>
<dd>Also match the users primary group from <code>/etc/passwd</code></p>
<dt><code>-s</code></p>
<dd>Strip NT domain name component from user names (/ or \ separated)</dl>
<h2>Configuration</h2>
<p>This <code>squid.conf</code> example defines two Squid acls. <i>usergroup1</i> matches users in <i>group1</i> , and <i>usergroup2</i> matches users in <i>group2</i> or <i>group3</i></p>
<dl>
<dd><code>external_acl_type unix_group %LOGIN /usr/local/squid/libexec/ext_unix_group_acl -p</code><br />
 <code>acl usergroup1 external unix_group group1</code><br />
 <code>acl usergroup2 external unix_group group2 group3</code></dl>
<p> By default up to 11 groups can be matched in one acl (including commandline specified groups). This limit is defined by <code>MAX_GROUPS</code> in the source code.</p>
<h2>Known Issues</h2>
<p>Does not understand GID aliased groups sometimes used to work around groups size limitations. If you are using GID aliased groups then you must specify each alias by name.</p>
<h2>Author</h2>
<p>This program was written by <i>Rodrigo Campos &lt;rodrigo [at] geekbunker.org&gt;</i> </p>
<p> This manual was written by <i>Henrik Nordstrom &lt;hno [at] squid-cache.org&gt;</i></p>
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
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt; </p>
<p> Additionally bugs or bug-fixes can be reported to <i>Rodrigo Campos &lt;rodrigo [at] geekbunker.org&gt;</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
