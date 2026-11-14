---
title: "tls_prune(8)"
name: "tls_prune"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tls_prune/"
description: "tls_prune – prune expired sessions from the TLS sessions database"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>tls_prune &#8211; prune expired sessions from the TLS sessions database</p>
<h2>Synopsis</h2>
<p><code>tls_prune</code> [ <code>-C</code> <i>config-file</i> ]</p>
<h2>Description</h2>
<p><i>Tls_prune</i> is used to prune expired sessions from the TLS sessions database. The lifetime of a TLS session is determined by the <code>tls_session_timeout</code> configuration option. </p>
<p> <i>Tls_prune</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
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
