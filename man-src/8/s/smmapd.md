---
title: "smmapd(8)"
name: "smmapd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smmapd/"
description: "SMMAPD – Sendmail socket map daemon"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>SMMAPD &#8211; Sendmail socket map daemon</p>
<h2>Synopsis</h2>
<p><code>smmapd</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-U</code> <i>uses</i> ] [ <code>-T</code> <i>timeout</i> ] </p>
<p>&nbsp;<wbr>[ <code>-D</code> ]</p>
<h2>Description</h2>
<p><code>SMMAPD</code> is a Sendmail socket map daemon which is used to verify that a Cyrus mailbox exists, that it is postable and it is under quota. It accepts commands on its standard input and responds on its standard output. It MUST be invoked by <i><a href="/docs/linux/man/8-master/">master</a></i>(8) with those descriptors attached to a remote client connection. </p>
<p> <code>SMMAPD</code> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-U</code><i> uses</i></p>
<dd>The maximum number of times that the process should be used for new connections before shutting down. The default is 250.</p>
<dt><code>-T</code><i> timeout</i></p>
<dd>The number of seconds that the process will wait for a new connection before shutting down. Note that a value of 0 (zero) will disable the timeout. The default is 60.</p>
<dt><code>-D</code></p>
<dd>Run external debugger specified in debug_command.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd>Default configuration file.</p>
<dt><code>/etc/cyrus.conf</code></p>
<dd>Cyrus Master process configuration file. </p>
</dl>
