---
title: "getmail_maildir(1)"
name: "getmail_maildir"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getmail_maildir/"
description: "getmail_maildir – read a message from stdin and deliver to a named maildir"
---

<h2 class="name">NAME</h2>
<p> getmail_maildir &#8211; read a message from stdin and deliver to a named maildir </p>
<h2>SYNOPSIS</h2>
<p> <code>getmail_maildir</code> [<i>OPTION</i>] <i>PATH</i></p>
<h2>DESCRIPTION</h2>
<p> Deliver a mail message from standard input, to the maildir named PATH. PATH must start with a dot or a slash and end with a slash. </p>
<p> <code>getmail_maildir</code> uses the SENDER environment variable to construct a <code>Return-Path:</code> header field and the contents of the RECIPIENT environment variable to construct a <code>Delivered-To:</code> header field at the top of the message.</p>
<dl>
<dt><code>&#8211;verbose, -v</code></p>
<dd> print a status message on success</dl>
<h2>AUTHOR</h2>
<p> Written by Charles Cazabon.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;charlesc-getmail-bugs [at] pyropus.ca&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998-2019 Charles Cazabon<br />
 This is free software; see the file COPYING for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>getmail_maildir</code> is maintained in HTML and plaintext formats. See the included files for details. </p>
<h2>Index</h2>
