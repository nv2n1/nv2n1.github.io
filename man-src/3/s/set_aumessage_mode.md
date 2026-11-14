---
title: "set_aumessage_mode(3)"
name: "set_aumessage_mode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_aumessage_mode/"
description: "set_message_mode – Sets the message mode"
---

<p>set_message_mode &#8211; Sets the message mode</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;libaudit.h&gt;
void set_message_mode(message_t mode);
</code></pre>
<h2>Description</h2>
<p><code>set_message_mode</code> sets the location where informational messages are sent. If <i>mode</i>=0 (default), then informational messages are sent to stderr. If <i>mode</i>=1, then informational messages are sent to syslog. </p>
<h2>Example</h2>
<pre>/* Sample code */
set_message_mode(MSG_SYSLOG)</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8), <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3). </p>
<h2>Author</h2>
<p>Debora Velarde.</p>
