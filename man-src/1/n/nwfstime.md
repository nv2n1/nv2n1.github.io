---
title: "nwfstime(1)"
name: "nwfstime"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwfstime/"
description: "nwfstime – Display / Set a NetWare server’s date and time"
---

<h2>NAME</h2>
<p> nwfstime &#8211; Display / Set a NetWare server&#8217;s date and time</p>
<h2>SYNOPSIS</h2>
<p> <code>nwfstime</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-s</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwfstime</code> displays a NetWare server&#8217;s date and time. You can also set a NetWare server&#8217;s date and time from the local time. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> With -h nwfstime prints a little help text.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dt>
<dd> is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>user</i></p>
<dl>
<dt>
<dd> <code>user</code> is the user name to use for login. To set the server&#8217;s time, you need supervisor privileges.</dl>
<p> <code>-P</code> <i>password</i></p>
<dl>
<dt>
<dd> <code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwfstime prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if no password is required for the login. As you need supervisor privileges for setting the date and time, this option is probably not used very often.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> With <code>-s,</code> nwfstime sets the file server&#8217;s date and time according to the local date and time.</dl>
<h2>Index</h2>
