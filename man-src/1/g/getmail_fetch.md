---
title: "getmail_fetch(1)"
name: "getmail_fetch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getmail_fetch/"
description: "getmail_fetch – retrieve messages from one or more POP3 or POP3-over-SSL mailboxes and deliver to a maildir, mboxrd-format mbox file, or external MDA"
---

<h2 class="name">NAME</h2>
<p> getmail_fetch &#8211; retrieve messages from one or more POP3 or POP3-over-SSL mailboxes and deliver to a maildir, mboxrd-format mbox file, or external MDA </p>
<h2>SYNOPSIS</h2>
<p> <code>getmail_fetch</code> [<i>OPTIONS</i>] <i>SERVER</i> <i>USERNAME</i> <i>PASSWORD</i> <i>DESTINATION</i></p>
<h2>DESCRIPTION</h2>
<p> getmail_fetch retrieves messages from POP3 or POP3-over-SSL mailboxes and delivers to a maildir, mboxrd, or external MDA. This command is intended primarily for scripting, and as such does not require a client-side configuration file, and does not record any state. </p>
<p> The <i>DESTINATION</i> argument is interpreted as follows: </p>
<p> If it begins with a dot or a slash and ends with a slash, it is assumed to be a path to a maildir. </p>
<p> If it begins with a dot or a slash and does not end with a slash, it is assumed to be a path to an mboxrd file. </p>
<p> If it begins with a pipe, it is assumed to be a path to an external MDA command. Note that arguments can be included in this string by separating them by whitespace; untrusted data <code>must not</code> be used in constructing this string.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show a short usage summary and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> output information messages while running</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> output only on error</p>
<dt><code>-m</code><i>FILE</i>, <code>&#8211;message</code>=<i>FILE</i></p>
<dd> read well-formatted RFC822 message from FILE and deliver prior to connecting to POP server</p>
<dt><code>-p</code><i>PORT</i>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> use port PORT instead of default (POP3: 110, POP3-over-SSL: 995)</p>
<dt><code>-d</code>, <code>&#8211;delete</code></p>
<dd> delete messages from server after delivery</p>
<dt><code>-t</code><i>TIMEOUT</i>, <code>&#8211;timeout</code>=<i>TIMEOUT</i></p>
<dd> use timeout of TIMEOUT seconds instead of default 180</p>
<dt><code>-a</code>, <code>&#8211;apop</code></p>
<dd> use APOP authentication</p>
<dt><code>-s</code>, <code>&#8211;ssl</code></p>
<dd> use POP3-over-SSL</dl>
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
