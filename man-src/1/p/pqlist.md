---
title: "pqlist(1)"
name: "pqlist"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pqlist/"
description: "pqlist – List available NetWare print queues"
---

<h2>NAME</h2>
<p> pqlist &#8211; List available NetWare print queues</p>
<h2>SYNOPSIS</h2>
<p> <code>pqlist</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i><br />
&nbsp;<wbr>| <code>-n</code> ] [ <code>-C</code> ] [ <i>pattern</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>pqlist</code> lists all the NetWare print queues available to you on some server. If you are already connected to some server, this one is used. </p>
<p> If pqlist does not print to a tty, the decorative header line is not printed, so that you can count the printing queue available on your server by doing </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pqlist -S server | wc -l </p>
<p> <code>pqlist</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of .nwclient MUST be 600, for security reasons. </p>
<h2>OPTIONS</h2>
<p> <code>pattern</code></p>
<dl>
<dt>
<dd> <code>pattern</code> is used to list only selected queues. You can use wildcards in the pattern, but you have to be careful to prevent shell interpretation of wildcards like &#8216;*&#8217;.</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> <code>-h</code> is used to print out a short help text.</dl>
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
<dd> <code>-n</code> should be given to mount shares which do not require a password to log in. </p>
<p> If neither <code>-n</code> nor <code>-P</code> are given, pqlist prompts for a password.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nwclient/">nwclient</a>(5), <a href="/docs/linux/man/1-nprint/">nprint</a>(1), <a href="/docs/linux/man/1-slist/">slist</a>(1), <a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8)</code> </p>
<h2>CREDITS</h2>
<p> pqlist was written by Volker Lendecke (lendecke [at] math.uni-goettingen.de) </p>
<h2>Index</h2>
