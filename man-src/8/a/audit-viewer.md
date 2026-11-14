---
title: "audit-viewer(8)"
name: "audit-viewer"
section: "8"
letter: "a"
url: "/docs/linux/man/8-audit-viewer/"
description: "audit-viewer – A graphical utility for viewing and summarizing audit events"
---

<p>audit-viewer &#8211; A graphical utility for viewing and summarizing audit events</p>
<h2>Synopsis</h2>
<p><code>audit-viewer</code> [<code>&#8211;unprivileged</code>] <i>SAVED</i>&#8230; </p>
<h2>Description</h2>
<p><code>audit-viewer</code> is a GUI for viewing and summarizing audit events. Tabs displaying specific configuration can be specified on the command line using one or more <i>SAVED</i> file names, each file should contain either a previously saved window layout or a previously saved configuration of a single tab. If no <i>SAVED</i> files are specified, <code>audit-viewer</code> opens a simple unfiltered list of audit events. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;unprivileged</code></p>
<dd>Do not try to start the privileged <code>audit-viewer-server</code> back-end. </p>
<p> If this option is specified, only audit log files that are readable by the current user are available. This usually means that the system audit log files stored in <code>/var/log/audit</code> are not available. </p>
</dl>
<h2>Exit Status</h2>
<p><code>audit-viewer</code> usually exists with status 0. Non-zero exit status is returned if <code>audit-viewer</code> can not start the <code>audit-viewer-server</code> back-end or terminates unexpectedly.</p>
<h2>Files</h2>
<dl>
<dt><code>/var/log/audit</code></p>
<dd>The directory containing system log files. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ausearch-expression/">ausearch-expression</a></code>(5), <code><a href="/docs/linux/man/8-aureport/">aureport</a></code>(8), <code><a href="/docs/linux/man/8-ausearch/">ausearch</a></code>(8) </p>
