---
title: "fud(8)"
name: "fud"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fud/"
description: "FUD – provide information about user mailboxes"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>FUD &#8211; provide information about user mailboxes</p>
<h2>Synopsis</h2>
<p><code>fud</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-U</code> <i>uses</i> ] [ <code>-T</code> <i>timeout</i> ] [ <code>-D</code> ]</p>
<h2>Description</h2>
<p><code>FUD</code> is a long lived datagram daemon started from master that provides information about when a user last read their mail, when mail last arrived in a user&#8217;s mailbox, and how many messages are recent for that user. </p>
<p> Note that for <code>FUD</code> to run properly you must set proto=udp in its cyrus.conf services entry. prefork=1 is also recommended. <code>FUD</code> will automatically proxy any and all FUD requests to the appropriate backend server if it is runing on a Cyrus Murder frontend machine. </p>
<p> <code>FUD</code> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
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
<dd>Cyrus Master process configuration file.</dl>
<h2>Bugs</h2>
<p>Though not really a bug, <code>FUD</code> will silently ignore any requests that it does not consider valid. Also not really a bug, <code>FUD</code> requires that the anonymous user has the 0 (zero) right on the mailbox in question. This is only a &quot;bug&quot; because 0 is not a standard IMAP ACL bit. <code>FUD</code> is an experimental interface meant to provide information to build a finger-like service around. Eventually it should be superceded by a more standards-based protocol. </p>
