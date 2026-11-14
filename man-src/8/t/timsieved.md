---
title: "timsieved(8)"
name: "timsieved"
section: "8"
letter: "t"
url: "/docs/linux/man/8-timsieved/"
description: "timsieved – CMU hack for getting sieve scripts onto the server"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>timsieved &#8211; CMU hack for getting sieve scripts onto the server</p>
<h2>Synopsis</h2>
<p><code>timsieved</code> [ <code>-C</code> <i>config-file</i> ]</p>
<h2>Description</h2>
<p><i>timsieved</i> is a server that allows users to remotely manage their sieve scripts kept on the server. It accepts commands on its standard input and responds on its standard output. It MUST be invoked by <i><a href="/docs/linux/man/8-master/">master</a></i>(8) with those descriptors attached to a remote client connection. Cyrus admins that authenticate and authorize as themselves (e.g. don&#8217;t proxy) manage global scripts. <i>Timsieved</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code> </p>
