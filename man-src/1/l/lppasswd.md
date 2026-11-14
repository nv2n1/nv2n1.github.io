---
title: "lppasswd(1)"
name: "lppasswd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lppasswd/"
description: "lppasswd – add, change, or delete digest passwords."
---

<h2>NAME</h2>
<p> lppasswd &#8211; add, change, or delete digest passwords.</p>
<h2>SYNOPSIS</h2>
<p> <code>lppasswd</code> [ <i>username</i> ]<br />
 <code>lppasswd</code> -a [ -g <i>groupname</i> ] <i>username</i><br />
 <code>lppasswd</code> -x <i>username</i></p>
<h2>DESCRIPTION</h2>
<p> <i>lppasswd</i> adds, changes, or deletes passwords in the CUPS digest password file, <i>passwd.md5</i>. When run by a normal user, <i>lppasswd</i> will prompt for the old and new passwords. When run by the super-user, <i>lppasswd</i> can add new accounts (<i>-a username</i>), change existing accounts (<i>username</i>), or delete accounts (<i>-x username</i>) in the digest password file. Digest usernames do not have to match local UNIX usernames.</p>
<h2>OPTIONS</h2>
<p> <i>lppasswd</i> supports the following options:</p>
<dl>
<dt>-g groupname</p>
<dd>
 Specifies a group other than the default system group.</dl>
<h2>SECURITY ISSUES</h2>
<p> By default, the <i>lppasswd</i> program is not installed to allow ordinary users to change their passwords. To enable this, the <i>lppasswd</i> command must be made setuid to root with the command: </p>
<pre>
chmod u+s lppasswd
</pre>
<p> While every attempt has been made to make <i>lppasswd</i> secure against exploits that could grant super-user privileges to unprivileged users, paranoid system administrators may wish to use Basic authentication with accounts managed by PAM instead.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-lp/">lp</a>(1)</i>, <i><a href="/docs/linux/man/1-lpr/">lpr</a>(1)</i>,<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2013 by Apple Inc. </p>
<h2>Index</h2>
