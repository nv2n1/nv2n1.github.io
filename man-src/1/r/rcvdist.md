---
title: "rcvdist(1)"
name: "rcvdist"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcvdist/"
description: "rcvdist – asynchronously redistribute new mail"
---

<h2 class="name">NAME</h2>
<p> rcvdist &#8211; asynchronously redistribute new mail </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/usr/libexec/nmh/rcvdist</code> [<code>-form</code> <i>formfile</i>] [switches for <i>postproc</i>] <i>address1</i> &#8230; [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>rcvdist</code> program will accept a message on its standard input and resend a copy of this message to all of the addresses listed on its command line. </p>
<p> When a message is redistributed with the <code>rcvdist</code> command, the format of the Resent-xxx header fields is controlled by the forms files &#8220;<i>rcvdistcomps</i>&#8221;. If a file named &#8220;<i>rcvdistcomps</i>&#8221; exists in the user&#8217;s nmh directory, it will be used instead of the default one. You may specify an alternate forms file with the switch <code>-form</code> <i>formfile</i>. </p>
<p> The &#8220;<i>rcvdistcomps</i>&#8221; file uses the format string facility described in <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5). In addition to the standard format escapes, <code>rcvdist</code> also recognizes the following additional <i>component</i> escape: </p>
<dl>
<dt>
<dd>
<pre>
<i>Escape   Returns  Description</i>
addresses string   the addresses to distribute to
</pre>
</dl>
<p> By default, <code>rcvdist</code> uses the program <code>post</code> to do the actual delivery of the message, although this can be changed by defining the <i>postproc</i> profile component.</p>
<h2>FILES</h2>
<pre>
^/etc/nmh/rcvdistcomps~^Default message skeleton
^or &lt;mh-dir&gt;/rcvdistcomps~^Rather than standard message skeleton
^/etc/nmh/mts.conf~^nmh mts configuration file
^$HOME/.maildelivery~^The file controlling local delivery
^/etc/nmh/maildelivery~^Rather than the standard file
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rcvpack/">rcvpack</a></i>(1), <i><a href="/docs/linux/man/1-rcvstore/">rcvstore</a></i>(1), <i><a href="/docs/linux/man/1-rcvtty/">rcvtty</a></i>(1), <i><a href="/docs/linux/man/1-slocal/">slocal</a></i>(1), <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) </p>
<h2>Index</h2>
