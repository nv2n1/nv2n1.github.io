---
title: "mlmmj-receive(1)"
name: "mlmmj-receive"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlmmj-receive/"
description: "mlmmj-receive – receive mails for an mlmmj managed mailinglist"
---

<h2>NAME</h2>
<p> mlmmj-receive &#8211; receive mails for an mlmmj managed mailinglist</p>
<h2>SYNOPSIS</h2>
<p> <code>mlmmj-receive</code> <i>-L /path/to/listdir </i>[<i>-h</i>] [<i>-V</i>] [<i>-P</i>] [<i>-F</i>]</p>
<dl>
<dt> <code>-h</code>: This help</p>
<dt> <code>-F</code>: Don&#8217;t fork in the background (debugging only)</p>
<dt> <code>-L</code>: Full path to list directory</p>
<dt> <code>-P</code>: Don&#8217;t execute mlmmj-process (debugging only)</p>
<dt> <code>-V</code>: Print version</dl>
<h2>DESCRIPTION</h2>
<dd>The mlmmj-receive binary is the one specified in the mailserver configuration file (aliases file), which writes the mail to the &lt;listdir&gt;/incoming directory and invokes mlmmj-process unless the <code>-P</code> option is specified. On systems using mailservers supporting the <code>/etc/aliases</code> file, a line to activate an mlmmj managed mailinglist would look like this: </p>
<p> list: &quot;|/usr/bin/mlmmj-receive -L /var/spool/mlmmj/list/&quot; </p>
<p> It&#8217;s very important to specify the full path to the binary, or the mailinglist will not function. </p>
<p> When the <code>-F</code> option is used, it will not fork in the background. The reason it forks is that if delivery of a mail takes longer time than the mail server will allow a command to be idle before presumed dead, the mail server would kill it. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mlmmj-process/">mlmmj-process</a>(1)</p>
<h2>AUTHORS</h2>
<p> This manual page was written by the following persons:</p>
<dl>
<dt>
<dd>S&oslash;ren Boll Overgaard &lt;boll [at] debian.org&gt; (based on html2man output)</p>
<dt>
<dd>Mads Martin J&oslash;rgensen &lt;mmj [at] mmj.dk&gt; </p>
</dl>
<h2>Index</h2>
