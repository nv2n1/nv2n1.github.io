---
title: "getmail(1)"
name: "getmail"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getmail/"
description: "getmail – retrieve messages from one or more POP3, IMAP4, or SDPS mailboxes and deliver to a maildir, mboxrd-format mbox file, or external MDA"
---

<h2 class="name">NAME</h2>
<p> getmail &#8211; retrieve messages from one or more POP3, IMAP4, or SDPS mailboxes and deliver to a maildir, mboxrd-format mbox file, or external MDA </p>
<h2>SYNOPSIS</h2>
<p> <code>getmail</code> [<i>OPTION</i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> getmail can retrieve messages from POP3, IMAP4, and SDPS mailboxes. SSL-wrapped POP3 and IMAP are also supported. Single-user and domain (multi-drop) mailboxes are supported. </p>
<p> getmail has built-in support for delivering to maildirs, mboxrd-format mbox files, and external MDAs.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show a short usage summary and exit</p>
<dt><code>-g</code><i>DIR</i>, <code>&#8211;getmaildir</code>=<i>DIR</i></p>
<dd> look in DIR for config/data files</p>
<dt><code>-r</code><i>FILE</i>, <code>&#8211;rcfile</code>=<i>FILE</i></p>
<dd> load configuration from FILE (may be given multiple times)</p>
<dt><code>&#8211;dump</code></p>
<dd> dump configuration and exit (debugging)</p>
<dt><code>&#8211;trace</code></p>
<dd> print extended trace information (extremely verbose)</p>
<dt><code>-i</code><i>FOLDER</i>, <code>&#8211;idle</code>=<i>FOLDER</i></p>
<dd> maintain connection and listen for new messages in <i>FOLDER</i>. This flag will only work if a single rc file is given, and will only work on IMAP connections where the server supports IMAP4 IDLE (RFC 2177).</dl>
<p> The following options override any in the configuration file(s).</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> operate more verbosely (can be given multiple times)</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> do not print informational messages</p>
<dt><code>-d</code>, <code>&#8211;delete</code></p>
<dd> delete messages from server after retrieving</p>
<dt><code>-l</code>, <code>&#8211;dont-delete</code></p>
<dd> do not delete messages from server after retrieving</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> retrieve all messages</p>
<dt><code>-n</code>, <code>&#8211;new</code></p>
<dd> retrieve only unread messages</dl>
<h2>AUTHOR</h2>
<p> Written by Charles Cazabon.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;charlesc-getmail-bugs [at] pyropus.ca&gt;. </p>
<p> <code>IMPORTANT:</code> include the output of <code>getmail [options] &#8211;dump</code> with any bug report.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998-2019 Charles Cazabon<br />
 This is free software; see the file COPYING for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>getmail</code> is maintained in HTML and plaintext formats. See the included files for details. </p>
<h2>Index</h2>
