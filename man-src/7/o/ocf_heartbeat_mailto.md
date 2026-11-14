---
title: "ocf_heartbeat_mailto(7)"
name: "ocf_heartbeat_mailto"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_mailto/"
description: "ocf_heartbeat_MailTo – Notifies recipients by email in the event of resource takeover"
---

<p>ocf_heartbeat_MailTo &#8211; Notifies recipients by email in the event of resource takeover</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>MailTo</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This is a resource agent for MailTo. It sends email to a sysadmin whenever a takeover occurs.</p>
<h2>Supported Parameters</h2>
<p><code>email</code></p>
<dl>
<dd>The email address of sysadmin. </p>
<p> (required, string, no default)</dl>
<p> <code>subject</code></p>
<dl>
<dd>The subject of the email. </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 10.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 10.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a MailTo resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_MailTo ocf:heartbeat:MailTo \
 params \
 email=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;10&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a MailTo resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_MailTo ocf:heartbeat:MailTo \
 email=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;10&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/MailTo_(resource_agent)">http://www.linux-ha.org/wiki/MailTo_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
