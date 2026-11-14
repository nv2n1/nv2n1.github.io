---
title: "nwbpvalues(1)"
name: "nwbpvalues"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwbpvalues/"
description: "nwbpvalues – Print a NetWare Bindery Propery’s contents"
---

<h2>NAME</h2>
<p> nwbpvalues &#8211; Print a NetWare Bindery Propery&#8217;s contents</p>
<h2>SYNOPSIS</h2>
<p> <code>nwbpvalues</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-o</code> <i>object name</i> ] [ <code>-t</code> <i>type</i> ] [ <code>-p</code> <i>property</i> ] [ <code>-v</code> ] [ <code>-c</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwbpvalues</code> prints the contents of a SET property. </p>
<p> <code>nwbpvalues</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of $HOME/.nwclient MUST be 600 for security reasons. </p>
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
<dd> <code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwbpvalues prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if no password is required for the login.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-o</code> <i>object name</i></p>
<dl>
<dt>
<dd> The name of the object to be looked up.</dl>
<p> <code>-t</code> <i>object type</i></p>
<dl>
<dt>
<dd> The type of the object. <i>Object type</i> must be specified as a decimal value. Common values are 1 for user objects, 2 for group objects and 3 for print queues. Other values are allowed, but are usually used for specialized applications.</dl>
<p> <code>-p</code> <i>property</i></p>
<dl>
<dt>
<dd> The name of the property to be printed.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> For set values, this lists the object id and type of each set member in addition to the object&#8217;s name. Without this flag, only the name is listed.</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Use canonical output, to be used with nwbpset.</dl>
<h2>AUTHORS</h2>
<p> nwbpvalues was written by Volker Lendecke with the corresponding Caldera utility in mind. See the Changes file of ncpfs for other contributors. </p>
<h2>Index</h2>
