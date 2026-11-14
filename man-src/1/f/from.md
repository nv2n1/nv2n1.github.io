---
title: "from(1)"
name: "from"
section: "1"
letter: "f"
url: "/docs/linux/man/1-from/"
description: "from – print names of those who have sent mail"
---

<h2 class="name">NAME</h2>
<p> <code>from</code> &#8211; print names of those who have sent mail </p>
<h2>SYNOPSIS</h2>
<p> [-<code>c</code> ] [-<code>f </code><i>file</i> ] [-<code>s </code><i>sender</i> ] [<i>user</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The utility prints out the mail header lines from the invoker&#8217;s mailbox. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-c</code></p>
<dd> Just print a count of messages and exit.</p>
<dt><code>-f </code><i>file</i></p>
<dd> The supplied <i>file</i> is examined instead of the invoker&#8217;s mailbox. If the &#8211;<code>f</code> option is used, the <i>user</i> argument should not be used. Read from standard input if file name &#8220;- &#8221; is given.</p>
<dt><code>-s </code><i>sender</i></p>
<dd> Only mail from addresses containing the supplied string are printed.</dl>
<p> If <i>user</i> is given, the <i>user </i><code>&#8216;s</code> mailbox is examined instead of the invoker&#8217;s own mailbox. (Privileges are required.)</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MAIL</code></p>
<dd> If set, the location of the invoker&#8217;s mailbox. Otherwise, the default in /var/mail is used.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/var/mail/* </code></p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-biff/">biff</a>(1), <a href="/docs/linux/man/1-mail/">mail</a>(1)</p>
<h2>HISTORY</h2>
<p> The command appeared in BSD 3.0 </p>
<h2>Index</h2>
