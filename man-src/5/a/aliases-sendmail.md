---
title: "aliases-sendmail(5)"
name: "aliases-sendmail"
section: "5"
letter: "a"
url: "/docs/linux/man/5-aliases-sendmail/"
description: "aliases – aliases file for sendmail"
---

<p>aliases &#8211; aliases file for sendmail</p>
<h2>Synopsis</h2>
<p><code>aliases</code></p>
<h2>Description</h2>
<p>This file describes user ID aliases used by sendmail. The file resides in /etc and is formatted as a series of lines of the form</p>
<dl>
<dd>name: addr_1, addr_2, addr_3, . . .</dl>
<p> The <i>name</i> is the name to alias, and the <i>addr_n</i> are the aliases for that name. <i>addr_n</i> can be another alias, a local username, a local filename, a command, an include file, or an external address.</p>
<dl>
<dt><code>Local Username</code></p>
<dd>username</p>
<dd>The username must be available via <a href="/docs/linux/man/3-getpwnam/">getpwnam</a>(3).</p>
<dt><code>Local Filename</code></p>
<dd>/path/name</p>
<dd>Messages are appended to the file specified by the full pathname (starting with a slash (/))</p>
<dt><code>Command</code></p>
<dd>|command</p>
<dd>A command starts with a pipe symbol (|), it receives messages via standard input.</p>
<dt><code>Include File</code></p>
<dd>:include: /path/name</p>
<dd>The aliases in pathname are added to the aliases for <i>name.</i></p>
<dt><code>E-Mail Address</code></p>
<dd>user [at] domain</p>
<dd>An e-mail address in RFC 822 format.</dl>
<p> Lines beginning with white space are continuation lines. Another way to continue lines is by placing a backslash directly before a newline. Lines beginning with # are comments. </p>
<p> Aliasing occurs only on local names. Loops can not occur, since no message will be sent to any person more than once. </p>
<p> If an alias is found for <i>name</i>, sendmail then checks for an alias for <i>owner-name</i>. If it is found and the result of the lookup expands to a single address, the envelope sender address of the message is rewritten to that address. If it is found and the result expands to more than one address, the envelope sender address is changed to <i>owner-name</i>. </p>
<p> After aliasing has been done, local and valid recipients who have a &#8220;.forward&#8221; file in their home directory have messages forwarded to the list of users defined in that file. </p>
<p> This is only the raw data file; the actual aliasing information is placed into a binary format in the file /etc/aliases.db using the program <a href="/docs/linux/man/1-newaliases/">newaliases</a>(1). A newaliases command should be executed each time the aliases file is changed for the change to take effect.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-newaliases/">newaliases</a>(1), <a href="/docs/linux/man/3-dbm/">dbm</a>(3), <a href="/docs/linux/man/3-dbopen/">dbopen</a>(3), <a href="/docs/linux/man/3-db_open/">db_open</a>(3), <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8) </p>
<p> <i>SENDMAIL Installation and Operation Guide.</i> </p>
<p> <i>SENDMAIL An Internetwork Mail Router.</i></p>
<h2>Bugs</h2>
<p>If you have compiled sendmail with DBM support instead of NEWDB, you may have encountered problems in <a href="/docs/linux/man/3-dbm/">dbm</a>(3) restricting a single alias to about 1000 bytes of information. You can get longer aliases by &#8220;chaining&#8221;; that is, make the last name in the alias be a dummy name which is a continuation alias.</p>
<h2>History</h2>
<p>The <code>aliases</code> file format appeared in 4.0BSD.</p>
