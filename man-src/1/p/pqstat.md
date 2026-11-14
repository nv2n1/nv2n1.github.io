---
title: "pqstat(1)"
name: "pqstat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pqstat/"
description: "pqstat – List jobs in NetWare print queue"
---

<h2>NAME</h2>
<p> pqstat &#8211; List jobs in NetWare print queue</p>
<h2>SYNOPSIS</h2>
<p> <code>pqstat</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i><br />
&nbsp;<wbr>| <code>-n</code> ] [ <code>-C</code> ] [ <code>-B</code> ] <i>queue name</i> [ <i>job count</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>pqstat</code> lists specified number of jobs from the specified NetWare print queue available to you on some server. If you are already connected to some server, this one is used. </p>
<p> If pqstat does not print to a tty, the decorative header line is not printed, so that you can count the jobs in print queue by doing </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pqstat -S server queue | wc -l </p>
<p> <code>pqstat</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of .nwclient MUST be 600, for security reasons. </p>
<h2>OPTIONS</h2>
<p> <code>queue name</code></p>
<dl>
<dt>
<dd> <code>queue name</code> is used to specify queue. You can not use wildcards in the name.</dl>
<p> <code>job count</code></p>
<dl>
<dt>
<dd> <code>job count</code> is used to specify how much entries will be shown. Default is to show all entries.</dl>
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
<p> If neither <code>-n</code> nor <code>-P</code> are given, pqstat prompts for a password.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-B</code></p>
<dl>
<dt>
<dd> By default, pqstat lists the Netware name of the print job owner. <code>-B</code> causes it to list the banner name instead.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nwclient/">nwclient</a>(5), <a href="/docs/linux/man/1-nprint/">nprint</a>(1), <a href="/docs/linux/man/1-slist/">slist</a>(1), <a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8), <a href="/docs/linux/man/1-pqlist/">pqlist</a>(1), <a href="/docs/linux/man/1-pqrm/">pqrm</a>(1)</code> </p>
<h2>CREDITS</h2>
<p> pqstat was written by David Woodhouse (dave [at] imladris.demon.co.uk) </p>
<h2>Index</h2>
