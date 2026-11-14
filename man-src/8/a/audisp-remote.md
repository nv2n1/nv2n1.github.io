---
title: "audisp-remote(8)"
name: "audisp-remote"
section: "8"
letter: "a"
url: "/docs/linux/man/8-audisp-remote/"
description: "audisp-remote – plugin for remote logging"
---

<p>audisp-remote &#8211; plugin for remote logging</p>
<h2>Synopsis</h2>
<p><code>audisp-remote</code></p>
<h2>Description</h2>
<p><code>audisp-remote</code> is a plugin for the audit event dispatcher daemon, audispd, that preforms remote logging to an aggregate logging server. </p>
<h2>Tips</h2>
<p>If you are aggregating multiple machines, you should enable node information and enriched events in the audit event stream. You can do this in one of two places. If you want computer node names written to disk as well as sent in the realtime event stream, edit the name_format option in /etc/audit/auditd.conf. This is the best option for enriched events. If you only want the node names in the realtime event stream, then edit the name_format option in /etc/audisp/audispd.conf. Do not enable both as it will put 2 node fields in the event stream.</p>
<h2>Signals</h2>
<dl>
<dt>SIGUSR1</p>
<dd>Causes the audisp-remote program to write the value of some of its internal flags to syslog. The <i>suspend</i> flag tells whether or not logging has been suspended. The <i>remote_ended</i> flage tells if the connection was broken by the server saying it can&#8217;t log events. The <i>transport_ok</i> flag tells whether or not the connection to the remote server is healthy. The <i>queue_size</i> tells how many records are enqueued to be sent to the remote server.</p>
<dt>SIGUSR2</p>
<dd>Causes the audisp-remote program to resume logging if it were suspended due to an error. </p>
</dl>
<h2>Files</h2>
<p>/etc/audisp/plugins.d/au-remote.conf, /etc/audit/auditd.conf, /etc/audisp/audispd.conf, /etc/audisp/audisp-remote.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8), <code><a href="/docs/linux/man/8-auditd-conf/">auditd.conf</a>(8),</code> <code><a href="/docs/linux/man/8-audispd-conf/">audispd.conf</a>(8),</code> <code><a href="/docs/linux/man/5-audisp-remote-conf/">audisp-remote.conf</a>(5).</code></p>
<h2>Author</h2>
<p>Steve Grubb</p>
