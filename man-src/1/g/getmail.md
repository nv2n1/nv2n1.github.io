---

title: "getmail(1)"
name: "getmail"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getmail/"
description: "getmail – retrieve messages from one or more POP3, IMAP4, or SDPS mailboxes and deliver to a maildir, mboxrd-format mbox file, or external MDA"
---

<p> getmail &#8211; retrieve messages from one or more POP3, IMAP4, or SDPS mailboxes and deliver to a maildir, mboxrd-format mbox file, or external MDA </p>
<h2>SYNOPSIS</h2>
<p> <code>getmail</code> [<i>OPTION</i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> getmail can retrieve messages from POP3, IMAP4, and SDPS mailboxes. SSL-wrapped POP3 and IMAP are also supported. Single-user and domain (multi-drop) mailboxes are supported. </p>
<p> getmail has built-in support for delivering to maildirs, mboxrd-format mbox files, and external MDAs.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show a short usage summary and exit</dd>
<dt><code>-g</code><i>DIR</i>, <code>&#8211;getmaildir</code>=<i>DIR</i></dt>
<dd> look in DIR for config/data files</dd>
<dt><code>-r</code><i>FILE</i>, <code>&#8211;rcfile</code>=<i>FILE</i></dt>
<dd> load configuration from FILE (may be given multiple times)</dd>
<dt><code>&#8211;dump</code></dt>
<dd> dump configuration and exit (debugging)</dd>
<dt><code>&#8211;trace</code></dt>
<dd> print extended trace information (extremely verbose)</dd>
<dt><code>-i</code><i>FOLDER</i>, <code>&#8211;idle</code>=<i>FOLDER</i></dt>
<dd> maintain connection and listen for new messages in <i>FOLDER</i>. This flag will only work if a single rc file is given, and will only work on IMAP connections where the server supports IMAP4 IDLE (RFC 2177).</dd></dl>
<p> The following options override any in the configuration file(s).</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> operate more verbosely (can be given multiple times)</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> do not print informational messages</dd>
<dt><code>-d</code>, <code>&#8211;delete</code></dt>
<dd> delete messages from server after retrieving</dd>
<dt><code>-l</code>, <code>&#8211;dont-delete</code></dt>
<dd> do not delete messages from server after retrieving</dd>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> retrieve all messages</dd>
<dt><code>-n</code>, <code>&#8211;new</code></dt>
<dd> retrieve only unread messages</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Charles Cazabon.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;charlesc-getmail-bugs [at] pyropus.ca&gt;. </p>
<p> <code>IMPORTANT:</code> include the output of <code>getmail [options] &#8211;dump</code> with any bug report.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998-2019 Charles Cazabon<br/>
 This is free software; see the file COPYING for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>getmail</code> is maintained in HTML and plaintext formats. See the included files for details. </p>
