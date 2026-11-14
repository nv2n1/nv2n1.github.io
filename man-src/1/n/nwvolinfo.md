---
title: "nwvolinfo(1)"
name: "nwvolinfo"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwvolinfo/"
description: "nwvolinfo – Diplay info on NetWare Volumes"
---

<h2>NAME</h2>
<p> nwvolinfo &#8211; Diplay info on NetWare Volumes</p>
<h2>SYNOPSIS</h2>
<p> <code>nwvolinfo</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-v</code> <i>volume</i> ] [ <code>-N</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwvolinfo</code> displays information on a NetWare Server Volume. </p>
<p> <code>nwvolinfo</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of $HOME/.nwclient MUST be 600 for security reasons. </p>
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
<dd> <code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwvolinfo prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if no password is required for the login.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-v</code> <i>volume</i></p>
<dl>
<dt>
<dd> The volume name to be used. Defaults to &#8216;SYS&#8217;.</dl>
<p> <code>-N</code></p>
<dl>
<dt>
<dd> Display the information in numeric-only format for use in a pipe.</dl>
<h2>AUTHORS</h2>
<p> nwvolinfo was written by Jacek Stepniewski &lt;cunio [at] gazeta.pl&gt; based on utilities by Volker Lendecke.</p>
<h2>Index</h2>
