---
title: "deliverquota(8)"
name: "deliverquota"
section: "8"
letter: "d"
url: "/docs/linux/man/8-deliverquota/"
description: "deliverquota – deliver to a maildir with a quota"
---

<p>deliverquota &#8211; deliver to a maildir with a quota</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>deliverquota</code> [-c] [-w&nbsp;<wbr><i>percent</i>] [-W&nbsp;<wbr><i>filename</i>] {<i>maildir</i>} {<i>quota</i>}</dl>
<h2>Description</h2>
<p><code>deliverquota</code></p>
<dd>delivers mail to a <i>maildir</i> taking into account any software-imposed quota on the maildir. This manually-enforced quota mechanism is described in the m[blue]<code><a href="/docs/linux/man/7-maildirquota/">maildirquota</a></code>(7)m[]<font SIZE="-2">[1]</font> and m[blue]<code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)m[]<font SIZE="-2">[2]</font> manual pages. Instead of setting up your mail server to deliver the message directly to a maildir, configure the mail server to run the <code>deliverquota</code> program in order to deliver the message, and specify the location of the maildir as the argument to <code>deliverquota</code>. </p>
<p> The second argument to <code>deliverquota</code> is optional. If present, <i>quota</i> specifies a new quota setting for this maildir. Specifying <i>quota</i> is equivalent to running m[blue]<code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)m[]<font SIZE="-2">[2]</font> with the <code>-q</code> option. The second argument to <code>deliverquota</code> is considered obsolete, and may be removed in the future. </p>
<p> <code>deliverquota</code> reads the message from standard input and delivers it to <i>maildir</i>. <i>maildir</i> may specify a path directly to a maildir folder, not the main <i>maildir</i> (as long as the folder was created by the m[blue]<code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)m[]<font SIZE="-2">[2]</font> command. </p>
<p> The <code>-c</code> option automatically creates the maildir, and all missing parent subdirectories (as &#8216;<code>mkdir -p</code>&#8216;). This option should be used with caution. </p>
<p> The <code>-w N</code> option places a warning message into the maildir if the maildir has a quota setting, and after the message was successfully delivered the maildir was at least <i>N</i> percent full. The warning message is copied from the file specified by the <code>-W</code> option, or from /etc/quotawarnmsg if <code>-W</code> was not specified. The &quot;Date:&quot; and &quot;Message-Id:&quot; headers are added to the message. The warning is repeated every 24 hours (at least), until the maildir drops below <i>N</i> percent full.</p>
<h2>Return Code</h2>
<p><code>deliverquota</code> delivers the message to the maildir and terminates with exit code 0 if the message can be delivered without going over quota. </p>
<p> If the maildir is over its specified quota, <code>deliverquota</code> terminates with exit code 77 (EX_NOPERM).</p>
<h2>See Also</h2>
<p>m[blue]<code><a href="/docs/linux/man/7-maildirquota/">maildirquota</a></code>(7)m[]<font SIZE="-2">[1]</font>, m[blue]<code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)m[]<font SIZE="-2">[2]</font>, m[blue]<code><a rel="nofollow" href="http://www.qmail.org/man/man5/maildir.html">http://www.qmail.org/man/man5/maildir.html</a></code>m[].</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><code><a href="/docs/linux/man/7-maildirquota/">maildirquota</a></code>(7)</p>
<dl>
<dd>[set $man.base.url.for.relative.links]/maildirquota.html</dl>
<dt> 2.</p>
<dd><code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)</p>
<dl>
<dd>[set $man.base.url.for.relative.links]/maildirmake.html</dl>
