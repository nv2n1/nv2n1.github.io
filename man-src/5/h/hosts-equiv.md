---
title: "hosts-equiv(5)"
name: "hosts-equiv"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hosts-equiv/"
description: "hosts.equiv – list of hosts and users that are granted \"trusted\" r command access to your system"
---

<p>hosts.equiv &#8211; list of hosts and users that are granted &quot;trusted&quot; <code>r</code> command access to your system</p>
<h2>Description</h2>
<p>The file <i>/etc/hosts.equiv</i> allows or denies hosts and users to use the <code>r</code>-commands (e.g., <code>rlogin</code>, <code>rsh</code>, or <code>rcp</code>) without supplying a password. </p>
<p> The file uses the following format:</p>
<dl>
<dt><i>+|[-]hostname|+@netgroup|-@netgroup</i> <i>[+|[-]username|+@netgroup|-@netgroup]</i></p>
<dd></dl>
<p> The <i>hostname</i> is the name of a host which is logically equivalent to the local host. Users logged into that host are allowed to access like-named user accounts on the local host without supplying a password. The <i>hostname</i> may be (optionally) preceded by a plus (+) sign. If the plus sign is used alone, it allows any host to access your system. You can explicitly deny access to a host by preceding the <i>hostname</i> by a minus (-) sign. Users from that host must always supply additional credentials, including possibly a password. For security reasons you should always use the FQDN of the hostname and not the short hostname. </p>
<p> The <i>username</i> entry grants a specific user access to all user accounts (except root) without supplying a password. That means the user is NOT restricted to like-named accounts. The <i>username</i> may be (optionally) preceded by a plus (+) sign. You can also explicitly deny access to a specific user by preceding the <i>username</i> with a minus (-) sign. This says that the user is not trusted no matter what other entries for that host exist. </p>
<p> Netgroups can be specified by preceding the netgroup by an @ sign. </p>
<p> Be extremely careful when using the plus (+) sign. A simple typographical error could result in a standalone plus sign. A standalone plus sign is a wildcard character that means &quot;any host&quot;!</p>
<h2>Files</h2>
<p><i>/etc/hosts.equiv</i></p>
<h2>Notes</h2>
<p>Some systems will honor the contents of this file only when it has owner root and no write permission for anybody else. Some exceptionally paranoid systems even require that there be no other hard links to the file. </p>
<p> Modern systems use the Pluggable Authentication Modules library (PAM). With PAM a standalone plus sign is considered a wildcard character which means &quot;any host&quot; only when the word <i>promiscuous</i> is added to the auth component line in your PAM file for the particular service (e.g., <code>rlogin</code>).</p>
<h2>Examples</h2>
<p>Below are some example <i>/etc/host.equiv</i> or <i>~/.rhosts</i> files. </p>
<p> Allow any user to log in from any host: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+ </p>
<p> Allow any user from <i>host</i> with a matching local account to log in: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;host </p>
<p> Note: the use of <i>+host</i> is never a valid syntax, including attempting to specify that any user from the host is allowed. </p>
<p> Allow any user from <i>host</i> to log in: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;host&nbsp;+ </p>
<p> Note: this is distinct from the previous example since it does not require a matching local account. </p>
<p> Allow <i>user</i> from <i>host</i> to log in as any non-root user: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;host user </p>
<p> Allow all users with matching local accounts from <i>host</i> to log in except for <i>baduser</i>: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;host -baduser<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;host </p>
<p> Deny all users from <i>host</i>: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-host </p>
<p> Note: the use of <i>-host -user</i> is never a valid syntax, including attempting to specify that a particular user from the host is not trusted. </p>
<p> Allow all users with matching local accounts on all hosts in a <i>netgroup</i>: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+@netgroup </p>
<p> Disallow all users on all hosts in a <i>netgroup</i>: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-@netgroup </p>
<p> Allow all users in a <i>netgroup</i> to log in from <i>host</i> as any non-root user: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;host&nbsp;+@netgroup </p>
<p> Allow all users with matching local accounts on all hosts in a <i>netgroup</i> except <i>baduser</i>: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+@netgroup -baduser<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+@netgroup </p>
<p> Note: the deny statements must always precede the allow statements because the file is processed sequentially until the first matching rule is found.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-rhosts/">rhosts</a></code>(5), <code><a href="/docs/linux/man/8-rlogind/">rlogind</a></code>(8), <code><a href="/docs/linux/man/8-rshd/">rshd</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
