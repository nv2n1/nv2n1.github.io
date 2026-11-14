---
title: "sendmail-opensmtpd(8)"
name: "sendmail-opensmtpd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sendmail-opensmtpd/"
description: "sendmail – a mail enqueuer for smtpd(8)"
---

<p><code>sendmail</code> &#8211; a mail enqueuer for <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8)</p>
<h2>Synopsis</h2>
<p><code>sendmail</code> [<code>-tv</code>] [<code>-F</code> <i>name</i>] [<code>-f</code> <i>from</i>] <i>to</i> &#8230;</p>
<h2>Description</h2>
<p>The <code>sendmail</code> utility is a local enqueuer for the <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) daemon, compatible with <code><a href="/docs/linux/man/8-mailwrapper/">mailwrapper</a></code>(8). The message is read on standard input (stdin) until <code>sendmail</code> encounters an end-of-file. The <code>sendmail</code> enqueuer is not intended to be used directly to send mail, but rather via a frontend known as a mail user agent. </p>
<p> Unless the optional <code>-t</code> flag is specified, one or more recipients must be specified on the command line. </p>
<p> The options are as follows:</p>
<dl>
<dd>
<dl>
<dt><code>-F</code> <i>name</i></p>
<dd>Set the sender&#8217;s full name.</p>
<dt><code>-f</code> <i>from</i></p>
<dd>Set the sender&#8217;s address.</p>
<dt><code>-t</code></p>
<dd>Read the message&#8217;s To:, Cc:, and Bcc: fields for recipients. The Bcc: field will be deleted before sending.</p>
<dt><code>-v</code></p>
<dd>Enable verbose output.</dl>
</dl>
<p> To maintain compatibility with Sendmail, Inc.&#8217;s implementation of <code>sendmail</code>, various other flags are accepted, but have no effect.</p>
<h2>Exit Status</h2>
<p>The <code>sendmail</code> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-smtpctl/">smtpctl</a></code>(8), <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8)</p>
<h2>Authors</h2>
<p><code>OpenSMTPD</code> is primarily developed by Gilles Chehade, Eric Faurot, and Charles Longeau, with contributions from various OpenBSD hackers. It is distributed under the ISC license. </p>
<p> This manpage was written by Ryan Kavanagh &lt;Mt rak [at] debian.org&gt; for the Debian project and is distributed under the ISC license.</p>
