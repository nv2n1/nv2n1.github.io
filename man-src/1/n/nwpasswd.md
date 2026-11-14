---
title: "nwpasswd(1)"
name: "nwpasswd"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwpasswd/"
description: "nwpasswd – Change a user’s password"
---

<h2>NAME</h2>
<p> nwpasswd &#8211; Change a user&#8217;s password</p>
<h2>SYNOPSIS</h2>
<p> <code>nwpasswd</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-O</code> <i>object name</i> ] [ <code>-t</code> <i>object type</i> ] </p>
<h2>DESCRIPTION</h2>
<p> With <code>nwpasswd,</code> you can change your password on a NetWare server. <code>nwpasswd</code> asks for the old password and twice for the new password. Then it changes the password on the server. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> With -h nwpasswd prints a little help text.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dt>
<dd> is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>user name</i></p>
<dl>
<dt>
<dd> is the name of the bindery object whose password is to be changed.</dl>
<p> <code>-O</code> <i>object name</i></p>
<dl>
<dt>
<dd> If you have supervisor privileges, you can change other users&#8217; passwords. With <code>-O</code> you can tell nwpasswd the name of the user whose password should be changed.</dl>
<p> <code>-t</code> <i>object type</i></p>
<dl>
<dt>
<dd> is the bindery object type of the object whose password is to be changed.</dl>
<h2>CREDITS</h2>
<p> nwpasswd would not have been possible without the work of Guntram Blom. Look at nwcrypt.c for his work. </p>
<h2>Index</h2>
