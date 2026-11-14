---
title: "nsend(1)"
name: "nsend"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nsend/"
description: "nsend – Send messages to users or groups"
---

<h2>NAME</h2>
<p> nsend &#8211; Send messages to users or groups</p>
<h2>SYNOPSIS</h2>
<p> <code>nsend</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-a</code> ] <code>-i</code> <i>objectID</i> | <code>-c</code> <i>connNum</i>[,<i>&#8230;</i>] | { [ <code>-t</code> <i>recipient type</i> ] <code>-o</code> <i>recipient name</i> | <i>recipient name</i> } <i>message</i> </p>
<h2>DESCRIPTION</h2>
<p> With <code>nsend</code>, you can send messages to the user&#8217;s workstations. </p>
<p> <code>nsend</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of <i>.nwclient</i> MUST be 0600, for security reasons. </p>
<h2>OPTIONS</h2>
<p> <code>recipient name</code></p>
<dl>
<dt>
<dd> <code>recipient name</code> is either the NetWare name of the user to receive the message or the name of an existing user group on that server. You can use wildcards in this specification.</dl>
<p> <code>-o</code> <i>recipient name</i></p>
<dl>
<dt>
<dd> Specifies recipient&#8217;s name. This can specify user or group.</dl>
<p> <code>-t</code> <i>recipent type</i></p>
<dl>
<dt>
<dd> Specifies recipient&#8217;s type.</dl>
<p> <code>-c</code> <i>connNum</i>[,<i>&#8230;</i>]</p>
<dl>
<dt>
<dd> Specifies connection numbers of recipients. You can use this option as workaround to deliver messages to directory services users.</dl>
<p> <code>-i</code> <i>userID</i></p>
<dl>
<dt>
<dd> Specifies recipient&#8217;s object ID. You can use this option as workaround to deliver messages to directory services users.</dl>
<p> <code>message</code></p>
<dl>
<dt>
<dd> <code>message</code> is the message to be sent. Please note that this has to be a single command line argument. If you want to send a message that contains spaces, you have to quote them on the command line. For example, to annoy your system administrator, you should try </p>
<p>nsend supervisor&nbsp;<wbr>&#8216;I know how this works!&#8217;<br />
 Program first searches (wildcards allowed) bindery with <i>recipients name</i> and <i>type</i>. If <code>user</code> is found, message is sent to this user, if <code>group</code> is found, message is sent to this group. Other object types are ignored. If no suitable object was found in this phase, <code>connection list</code> for specified object is retrieved (no wildcards allowed) and message is sent to this object (including <code>print servers</code> and so on). No expansions on <code>group</code> is done this time.</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> By default, nsend prepends &#8216;From &#8230;.&#8217; text to message. You can suppress this by adding <code>-a</code> to command line.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dt>
<dd> <code>server</code> is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>user name</i></p>
<dl>
<dt>
<dd> If the user name your NetWare administrator gave to you differs from your unix user-id, you should use <code>-U</code> to tell the server about your NetWare user name.</dl>
<p> <code>-P</code> <i>password</i></p>
<dl>
<dt>
<dd> You may want to give the password required by the server on the command line. You should be careful about using passwords in scripts.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if specified user does not have password. </p>
<p> If neither <code>-n</code> nor <code>-P</code> are given, nsend prompts for a password.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C</code>.</dl>
<h2>BUGS</h2>
<p> Directory services connection are not supported yet.<br />
 Options <code>-c</code>, <code>-i</code> and <code>-o</code> cannot be used together.<br />
 If user is specified multiple times (using wildcards in group specification or by repeating same number in <code>-c</code>), message is delivered multiple times to him. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nwclient/">nwclient</a>(5), <a href="/docs/linux/man/1-nprint/">nprint</a>(1), <a href="/docs/linux/man/1-slist/">slist</a>(1), <a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8)</code> </p>
<h2>CREDITS</h2>
<p> nsend was written by looking at mars_nwe&#8217;s message handling. Thanks to Martin Stover &lt;mstover [at] freeway.de&gt;.<br />
 Support for Netware groups by Philippe Andersson &lt;philippe_andersson [at] ste.scitex.com&gt;.<br />
 Support for connections greater than 255 by Petr Vandrovec &lt;vandrove [at] vc.cvut.cz&gt;. </p>
<h2>Index</h2>
