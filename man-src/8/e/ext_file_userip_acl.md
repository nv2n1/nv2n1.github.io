---
title: "ext_file_userip_acl(8)"
name: "ext_file_userip_acl"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ext_file_userip_acl/"
description: "ext_file_userip_acl – Restrict users to certain IP addresses, using a text file backend."
---

<p>ext_file_userip_acl &#8211; Restrict users to certain IP addresses, using a text file backend. </p>
<p> Version 1.0</p>
<h2>Synopsis</h2>
<p><code>ext_file_userip_acl</code> <code>[-dh] [-f </code> file name <code>]</code></p>
<h2>Description</h2>
<p><code>ext_file_userip_acl</code> is an installed binary. An external helper for the Squid external acl scheme. </p>
<p> It works by reading a pair composed by an IP address and an username on STDIN and matching it against a configuration file.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Write debug info to stderr.</p>
<dt><code>-f file</code></p>
<dd>Configuration <code>file </code> to load.</p>
<dt><code>-h</code></p>
<dd>Display the binary help and command line syntax info using stderr.</dl>
<h2>Configuration</h2>
<p>The <code>squid.conf </code> configuration for the external ACL should be:</p>
<dl>
<dd><code>external_acl_type type-name %SRC %LOGIN /path/to/ext_file_userip_acl -f /path/to/config.file</code></dl>
<p> If the helper program finds a matching username/ip in the configuration file, it returns <code>OK</code> , otherwise it returns <code>ERR .</code> </p>
<p> The configuration file format is as follows:</p>
<dl>
<dd>ip_addr[/netmask]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>username|@group|ALL|NONE</dl>
<p> Where<br />
 <code>ip_addr </code> is a dotted quad format IP address, the <code>netmask</code> must be in dotted quad format too. </p>
<p> When the second parameter is prefixed with an <code>@</code> , the program will lookup the <code>/etc/group</code> file entry for the specified username. </p>
<p> There are other two directives, <code>ALL </code> and <code>NONE </code> , which mean</p>
<h2>Author</h2>
<p>This program was written by <i>Rodrigo Campos &lt;rodrigo [at] geekbunker.org&gt;</i> </p>
<p> This manual was written by <i>Rodrigo Campos &lt;rodrigo [at] geekbunker.org&gt;</i> <i>Amos Jeffries &lt;amosjeffries [at] squid-cache.org&gt;</i></p>
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
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
