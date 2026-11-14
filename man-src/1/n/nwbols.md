---
title: "nwbols(1)"
name: "nwbols"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwbols/"
description: "nwbols – List NetWare Bindery Objects"
---

<h2>NAME</h2>
<p> nwbols &#8211; List NetWare Bindery Objects</p>
<h2>SYNOPSIS</h2>
<p> <code>nwbols</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-t</code> <i>type</i> ] [ <code>-o</code> <i>pattern</i> ] [ <code>-v</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwbols</code> lists the specified NetWare Bindery Objects visible for the user. </p>
<p> <code>nwbols</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of $HOME/.nwclient MUST be 600 for security reasons. </p>
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
<dd> <code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwbols prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if no password is required for the login.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-t</code> <i>type</i></p>
<dl>
<dt>
<dd> You can restrict the objects listed by specifying the type of the objects to be listed. <i>type</i> must be given as a decimal number.</dl>
<p> <code>-o</code> <i>pattern</i></p>
<dl>
<dt>
<dd> Specifying a pattern is another way to restrict the objects listed. Please note that this pattern is evaluated by the NetWare server. grep would be a better candidate for complex patterns.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> By default, the object&#8217;s name, its ID and its type are listed by <code>nwbols.</code> In the verbose mode, activated by <code>-v,</code> the object flags, its security byte and the properties flag is also listed.</dl>
<h2>AUTHORS</h2>
<p> nwbols was written by Volker Lendecke. See the Changes file of ncpfs for other contributors. </p>
<h2>Index</h2>
