---
title: "htdigest(1)"
name: "htdigest"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htdigest/"
description: "htdigest – manage user files for digest authentication"
---

<h2 class="name">NAME</h2>
<p> htdigest &#8211; manage user files for digest authentication</p>
<h2>SYNOPSIS</h2>
<p>&nbsp; </p>
<p> <code>htdigest</code> [ &#8211;<code>c</code> ] <i>passwdfile</i> <i>realm</i> <i>username</i><br />
&nbsp; </p>
<h2>SUMMARY</h2>
<p>&nbsp; </p>
<p> <code>htdigest</code> is used to create and update the flat-files used to store usernames, realm and password for digest authentication of HTTP users. Resources available from the Apache HTTP server can be restricted to just the users listed in the files created by <code>htdigest</code>.<br />
&nbsp; </p>
<p> This manual page only lists the command line arguments. For details of the directives necessary to configure digest authentication in httpd see the Apache manual, which is part of the Apache distribution or can be found at <a rel="nofollow" href="http://httpd.apache.org/.">http://httpd.apache.org/.</a><br />
&nbsp; </p>
<h2>OPTIONS</h2>
<p>&nbsp;<br />
&nbsp;</p>
<dl>
<dt><code>-c</code></p>
<dd> Create the <i>passwdfile</i>. If <i>passwdfile</i> already exists, it is deleted first.</p>
<dt><i>passwdfile</i></p>
<dd> Name of the file to contain the username, realm and password. If <code>-c</code> is given, this file is created if it does not already exist, or deleted and recreated if it does exist.</p>
<dt><i>realm</i></p>
<dd> The realm name to which the user name belongs. See <a rel="nofollow" href="http://tools.ietf.org/html/rfc2617#section-3.2.1">http://tools.ietf.org/html/rfc2617#section-3.2.1</a> for more details.</p>
<dt><i>username</i></p>
<dd> The user name to create or update in <i>passwdfile</i>. If <i>username</i> does not exist is this file, an entry is added. If it does exist, the password is changed.<br />
&nbsp;</dl>
<h2>SECURITY CONSIDERATIONS</h2>
<p>&nbsp; </p>
<p> This program is not safe as a setuid executable. Do <i>not</i> make it setuid.<br />
&nbsp; </p>
<h2>Index</h2>
