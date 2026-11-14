---
title: "zarafa-passwd(1)"
name: "zarafa-passwd"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-passwd/"
description: "zarafa-passwd – Change Zarafa user password."
---

<h2 class="name">NAME</h2>
<p> zarafa-passwd &#8211; Change Zarafa user password. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-passwd</code> <i>ACTION</i> [<i>OPTION</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>This tool can be used to change a user password. The Zarafa server must be running for <code>zarafa-passwd</code> to work. </p>
<p> If no action is given, an error message is printed. When invalid actions or not enough options for an action are given, an error message is printed. </p>
<p> The Zarafa passwd works only with the dbplugin. Please see the <code>EXTERNAL USERS</code>() section for more information.</p>
<h2>ACTIONS</h2>
<p> zarafa-passwd needs an action command with the appropriate options. Valid actions are: </p>
<p> <code>-u</code> <i>username</i></p>
<dl>
<dt>
<dd> Update the password. Valid parameters are: <i>[-p]</i> and <i>-o</i> </p>
<p> Default the password can be entered on the password prompt. The password will not be shown.</dl>
<h2>OPTIONS</h2>
<p> The options used by actions are as follows: </p>
<p> <code>-p</code> <i>&#8216;new password&#8217;</i></p>
<dl>
<dt>
<dd> Set new password for a user. This option is only valid with the <i>-o</i>.</dl>
<p> <code>-o</code> <i>oldpassword</i></p>
<dl>
<dt>
<dd> old password of a user. This option is only valid with the <i>-p</i>.</dl>
<p> <code>&#8211;host</code>, <code>-h</code> <i>path</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server through <i>path</i>, e.g. file:///path/to/socket. Default: file:///var/run/zarafa. This option can always be specified.</dl>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) </p>
<h2>Index</h2>
