---
title: "nwtrustee(1)"
name: "nwtrustee"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwtrustee/"
description: "nwtrustee – List an object’s trustee directory assignments"
---

<h2>NAME</h2>
<p> nwtrustee &#8211; List an object&#8217;s trustee directory assignments</p>
<h2>SYNOPSIS</h2>
<p> <code>nwtrustee</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-l</code> <i>volume number</i> ] [ <code>-L</code> <i>volume name</i> ] [ <code>-O</code> <i>object id</i> ] [ <code>-o</code> <i>object name</i> ] [ <code>-t</code> <i>object type</i> ] [ <code>-v</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwtrustee</code> lists the trustee directory assignments a user has on a specific volume. </p>
<p> <code>nwtrustee</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of $HOME/.nwclient MUST be 600 for security reasons. </p>
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
<dd> <code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwtrustee prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if no password is required for the login.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-O</code> <i>object id</i></p>
<dl>
<dt>
<dd> The bindery object id of the user whose assignments should be listed. Alternatively, use -o object name.</dl>
<p> <code>-o</code> <i>object name</i></p>
<dl>
<dt>
<dd> The name of the user whose assignments should be listed.</dl>
<p> <code>-t</code> <i>object type</i></p>
<dl>
<dt>
<dd> The type of object whose assignments should be listed. This defaults to 1, which means user. Another sensible value is 2, which means group.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Verbose listing. Also list the specific rights that are assigned to the user.</dl>
<h2>AUTHORS</h2>
<p> nwtrustee was written by Jacek Stepniewski &lt;cunio [at] gazeta.pl&gt;. This manual page was written by Volker Lendecke. </p>
<h2>Index</h2>
