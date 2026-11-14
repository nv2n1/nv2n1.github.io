---
title: "nwuserlist(1)"
name: "nwuserlist"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwuserlist/"
description: "nwuserlist – List Users logged in at a NetWare server"
---

<h2>NAME</h2>
<p> nwuserlist &#8211; List Users logged in at a NetWare server</p>
<h2>SYNOPSIS</h2>
<p> <code>nwuserlist</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-a</code> ] [ <code>-q</code> ] [ <code>-f</code> [ <code>-d</code> ] [ <code>-D</code> ] [ <code>-t</code> ]] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwuserlist</code> lists the users logged in at a NetWare server, together with their connection number and their login time. </p>
<p> <code>nwuserlist</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <code><a href="/docs/linux/man/5-nwclient/">nwclient</a></code>(5) for more information. Please note that the access permissions of <i>$HOME/.nwclient</i> MUST be 600 for security reasons. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> <code>-h</code> is used to print out a short help text.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dt>
<dd> <code>server</code> is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>user</i></p>
<dl>
<dt>
<dd> <code>user</code> is the user name to use for login.</dl>
<p> <code>-P</code> <i>password</i></p>
<dl>
<dt>
<dd> <code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwuserlist prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if no password is required for the login.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> With option <code>-a</code> the IPX address of the station the user is logged in from is printed as well.</dl>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> With option <code>-q</code> object ID is printed in addition to user name.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> List also files opened by each connection.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> List detailed informations about each file.</dl>
<p> <code>-D</code></p>
<dl>
<dt>
<dd> List DOS filename instead of filename which was used for opening.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Show raw hexadecimal values in addition to human readable conversions.</dl>
<h2>AUTHORS</h2>
<p> nwuserlist was written by Volker Lendecke. See the Changes file of ncpfs for other contributors. </p>
<h2>Index</h2>
