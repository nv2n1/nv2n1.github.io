---
title: "subuid(5)"
name: "subuid"
section: "5"
letter: "s"
url: "/docs/linux/man/5-subuid/"
description: "subuid – the subordinate uid file"
---

<p>subuid &#8211; the subordinate uid file</p>
<h2>Description</h2>
<p>Each line in /etc/subuid contains a user name and a range of subordinate user ids that user is allowed to use. This is specified with three fields delimited by colons (&#8220;:&#8221;). These fields are: </p>
<dl>
<dd>&bull; login name or UID</dl>
<dl>
<dd>&bull; numerical subordinate user ID</dl>
<dl>
<dd>&bull; numerical subordinate user ID count</dl>
<p> This file specifies the user IDs that ordinary users can use, with the <code>newuidmap</code> command, to configure uid mapping in a user namespace. </p>
<p> Multiple ranges may be specified per user. </p>
<p> When large number of entries (10000-100000 or more) are defined in /etc/subuid, parsing performance penalty will become noticeable. In this case it is recommended to use UIDs instead of login names. Benchmarks have shown speed-ups up to 20x.</p>
<h2>Files</h2>
<p>/etc/subuid</p>
<dl>
<dd>Per user subordinate user IDs.</dl>
<p> /etc/subuid-</p>
<dl>
<dd>Backup file for /etc/subuid.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/1-newgidmap/">newgidmap</a></code>(1), <code><a href="/docs/linux/man/1-newuidmap/">newuidmap</a></code>(1), <code><a href="/docs/linux/man/1-newusers/">newusers</a></code>(1), <code><a href="/docs/linux/man/5-subgid/">subgid</a></code>(5), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7). </p>
