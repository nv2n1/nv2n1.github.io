---
title: "rcvtty(1)"
name: "rcvtty"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcvtty/"
description: "rcvtty – report new mail"
---

<h2 class="name">NAME</h2>
<p> rcvtty &#8211; report new mail </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/usr/libexec/nmh/rcvtty</code> [<i>command</i>] [<code>-form</code> <i>formatfile</i>] [<code>-format</code> <i>string</i>] [<code>-width</code> <i>columns</i>] [<code>-bell</code> | <code>-nobell</code>] [<code>-newline</code> | <code>-nonewline</code>] [<code>-biff</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>rcvtty</code> can be used to report new mail. It is used primarily in conjunction with mail filtering agents such as <code>slocal</code> or <code>procmail</code>. </p>
<p> The <code>rcvtty</code> program executes the named command with the message as its standard input, and writes the resulting output on your terminal. </p>
<p> Alternately, if no command is specified (or is bogus), then <code>rcvtty</code> will instead write a one-line scan listing. The default output format of this scan listing may be overridden by using either the <code>-form</code> <i>formatfile</i> or <code>-format</code> <i>string</i> option, similar to the equivalent options for <code>scan</code> and <code>inc</code>. See <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) for details. </p>
<p> A newline is output before the message output, and the terminal bell is rung after the output. The <code>-nonewline</code> and <code>-nobell</code> options will inhibit these functions. </p>
<p> The switch <code>-width</code> <i>columns</i> may be given to specify the width of the scan line. The default is to use the width of the terminal. </p>
<p> In addition to the standard format escapes described in <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5), <code>rcvtty</code> also recognizes the following additional <i>component</i> escapes: </p>
<dl>
<dt>
<dd>
<pre>
Escape    Returns  Description
body      string   the (compressed) first part of the body
dtimenow  date     the current date
folder    string   the name of the current folder
</pre>
</dl>
<p> By default, <code>rcvtty</code> will send its output to every terminal on the local machine that is owned by current user, and that has given write permission as granted by the command <i><a href="/docs/linux/man/1-mesg/">mesg</a></i>(1). If the option <code>-biff</code> is given, then <code>rcvtty</code> will obey the notification status set by the command <i><a href="/docs/linux/man/1-biff/">biff</a></i>(1) instead.</p>
<h2>FILES</h2>
<pre>
^/etc/nmh/mts.conf~^nmh mts configuration file
^$HOME/.maildelivery~^The file controlling local delivery
^/etc/nmh/maildelivery~^Rather than the standard file
</pre>
<h2>CONTEXT</h2>
<p> None</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-width</code>' defaults to the width of the terminal
`<code>-newline</code>'
`<code>-bell</code>'
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rcvdist/">rcvdist</a></i>(1), <i><a href="/docs/linux/man/1-rcvpack/">rcvpack</a></i>(1), <i><a href="/docs/linux/man/1-rcvstore/">rcvstore</a></i>(1), <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5), <i><a href="/docs/linux/man/1-slocal/">slocal</a></i>(1)</p>
<h2>BUGS</h2>
<p> Only two return codes are meaningful, others should be. </p>
<h2>Index</h2>
