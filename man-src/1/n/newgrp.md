---
title: "newgrp(1)"
name: "newgrp"
section: "1"
letter: "n"
url: "/docs/linux/man/1-newgrp/"
description: "newgrp – log in to a new group"
---

<h2 class="name">NAME</h2>
<p> newgrp &#8211; log in to a new group </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>newgrp</code> [-] [<i>group</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>newgrp</code> command is used to change the current group ID during a login session. If the optional <code>&#8211;</code> flag is given, the user&#8217;s environment will be reinitialized as though the user had logged in, otherwise the current environment, including current working directory, remains unchanged. </p>
<p> <code>newgrp</code> changes the current real group ID to the named group, or to the default group listed in /etc/passwd if no group name is given. <code>newgrp</code> also tries to add the group to the user groupset. If not root, the user will be prompted for a password if she does not have a password (in /etc/shadow if this user has an entry in the shadowed password file, or in /etc/passwd otherwise) and the group does, or if the user is not listed as a member and the group has a password. The user will be denied access if the group password is empty and the user is not listed as a member. </p>
<p> If there is an entry for this group in /etc/gshadow, then the list of members and the password of this group will be taken from this file, otherwise, the entry in /etc/group is considered.</p>
<h2>CONFIGURATION</h2>
<p> The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>SYSLOG_SG_ENAB</code> (boolean)</p>
<dl>
<dt>
<dd> Enable &quot;syslog&quot; logging of <code>sg</code> activity.</dl>
<h2>FILES</h2>
<p> /etc/passwd</p>
<dl>
<dt>
<dd> User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dt>
<dd> Secure user account information.</dl>
<p> /etc/group</p>
<dl>
<dt>
<dd> Group account information.</dl>
<p> /etc/gshadow</p>
<dl>
<dt>
<dd> Secure group account information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-id/">id</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/1-sg/">sg</a></code>(1), <code><a href="/docs/linux/man/1-gpasswd/">gpasswd</a></code>(1), <code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/5-gshadow/">gshadow</a></code>(5). </p>
<h2>Index</h2>
