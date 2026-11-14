---
title: "idled(8)"
name: "idled"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idled/"
description: "idled – provide near real-time updates for IMAP IDLE"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>idled &#8211; provide near real-time updates for IMAP IDLE</p>
<h2>Synopsis</h2>
<p><code>idled</code> [ <code>-C</code> <i>config-file</i> ]</p>
<h2>Description</h2>
<p><i>Idled</i> is a long lived datagram daemon which receives notifications of mailbox changes and signals the appropriate <i>imapd</i> to report the changes to the client. <i>Idled</i> is usually started from <i>master.</i> </p>
<p> <i>Idled</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. The <i>idlesocket</i> option is used to specify the Unix domain socket to listen on for notifications.</p>
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
