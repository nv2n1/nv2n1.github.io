---
title: "nwauth(1)"
name: "nwauth"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwauth/"
description: "nwauth – Verify username/password"
---

<h2>NAME</h2>
<p> nwauth &#8211; Verify username/password</p>
<h2>SYNOPSIS</h2>
<p> <code>nwauth</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-D</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>nwauth</code> does nothing but logging into a NetWare server. If the login was successful, an error code of 0 is returned. If the login was not successful, an error code of 1 is returned. It was designed for use by other programs who want authenticate users via a NetWare server. </p>
<p> If there is no <code>-P</code> or <code>-n</code> option specified on command line, nwauth <code>always</code> expects a password on stdin. If the stdin is a tty, then the user is prompted for a password. Otherwise nwauth simply reads stdin for a password. </p>
<p> <code>nwauth</code> looks up the file <i>$HOME/.nwclient</i> to find a file server and a user name if they are not specified on command line. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of <i>.nwclient</i> MUST be 600, for security reasons. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> <code>-h</code> is used to print a short help text.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dt>
<dd> <code>server</code> is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>user name</i></p>
<dl>
<dt>
<dd> If the user name your NetWare administrator gave to you differs from your unix user-id, you should use <code>-U</code> to tell the server about your NetWare user name.</dl>
<p> <code>-D</code></p>
<dl>
<dt>
<dd> <code>nwauth</code> says that your password is correct if you have existing connection to <i>server</i> with name <i>user name</i>. This is handy for some shell scripts, but it is unacceptable for authorization modules, such as PAM, PHP or Apache. It was pointed to me that this behavior was not well known, and there exist at least one PAM module which does not know that (this module is not part of ncpfs; you should use PAM module which comes with ncpfs instead anyway).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nwclient/">nwclient</a>(5)</code> </p>
<h2>CREDITS</h2>
<p> nwauth was written by Volker Lendecke (lendecke [at] math.uni-goettingen.de) </p>
<h2>Index</h2>
