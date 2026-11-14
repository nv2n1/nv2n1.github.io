---
title: "gshadow(5)"
name: "gshadow"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gshadow/"
description: "gshadow – shadowed group file"
---

<p>gshadow &#8211; shadowed group file</p>
<h2>Description</h2>
<p>/etc/gshadow contains the shadowed information for group accounts. </p>
<p> This file must not be readable by regular users if password security is to be maintained. </p>
<p> Each line of this file contains the following colon-separated fields: </p>
<p> <code>group name</code></p>
<dl>
<dd>It must be a valid group name, which exist on the system.</dl>
<p> <code>encrypted password</code></p>
<dl>
<dd>Refer to <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) for details on how this string is interpreted. </p>
<p> If the password field contains some string that is not a valid result of <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3), for instance ! or *, users will not be able to use a unix password to access the group (but group members do not need the password). </p>
<p> The password is used when a user who is not a member of the group wants to gain the permissions of this group (see <code><a href="/docs/linux/man/1-newgrp/">newgrp</a></code>(1)). </p>
<p> This field may be empty, in which case only the group members can gain the group permissions. </p>
<p> A password field which starts with an exclamation mark means that the password is locked. The remaining characters on the line represent the password field before the password was locked. </p>
<p> This password supersedes any password specified in /etc/group.</dl>
<p> <code>administrators</code></p>
<dl>
<dd>It must be a comma-separated list of user names. </p>
<p> Administrators can change the password or the members of the group. </p>
<p> Administrators also have the same permissions as the members (see below).</dl>
<p> <code>members</code></p>
<dl>
<dd>It must be a comma-separated list of user names. </p>
<p> Members can access the group without being prompted for a password. </p>
<p> You should use the same list of users as in /etc/group.</dl>
<h2>Files</h2>
<p>/etc/group</p>
<dl>
<dd>Group account information.</dl>
<p> /etc/gshadow</p>
<dl>
<dd>Secure group account information.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-gpasswd/">gpasswd</a></code>(5), <code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/8-grpck/">grpck</a></code>(8), <code><a href="/docs/linux/man/8-grpconv/">grpconv</a></code>(8), <code><a href="/docs/linux/man/1-newgrp/">newgrp</a></code>(1). </p>
