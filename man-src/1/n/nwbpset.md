---
title: "nwbpset(1)"
name: "nwbpset"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwbpset/"
description: "nwbpset – Create a bindery property or set its value"
---

<h2>NAME</h2>
<p> nwbpset &#8211; Create a bindery property or set its value</p>
<h2>SYNOPSIS</h2>
<p> <code>nwbpset</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwbpset</code> Reads a property specification from the standard input and creates and sets the corresponding property. The format is determined by the output of &#8216;nwbpvalues -c&#8217;. nwbpset will hopefully become an important part of the bindery management suite of ncpfs, together with </p>
<p> As another example, look at the following command line: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>nwbpvalues -t 1 -o supervisor -p user_defaults -c |\&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>sed&nbsp;<wbr>&#8216;2s/.*/ME/&#8217;|\<br />
&nbsp;<wbr>&nbsp;<wbr>sed&nbsp;<wbr>&#8216;3s/.*/LOGIN_CONTROL/&#8217;|\<br />
&nbsp;<wbr>&nbsp;<wbr>nwbpset </p>
<p> With this command, the property user_defaults of the user object &#8216;supervisor&#8217; is copied into the property login_control of the user object &#8216;me&#8217;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>nwbpvalues -t 1 -o me -p login_control -c |\<br />
&nbsp;<wbr>&nbsp;<wbr>sed&nbsp;<wbr>&#8216;9s/.*/ff/&#8217;|\<br />
&nbsp;<wbr>&nbsp;<wbr>nwbpset </p>
<p> This command disables the user object me. </p>
<p> Feel free to contribute other examples! </p>
<p> <code>nwbpset</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of $HOME/.nwclient MUST be 600 for security reasons. </p>
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
<dd> <code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwbpset prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if no password is required for the login.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<h2>AUTHORS</h2>
<p> nwbpset was written by Volker Lendecke. See the Changes file of ncpfs for other contributors. </p>
<h2>Index</h2>
