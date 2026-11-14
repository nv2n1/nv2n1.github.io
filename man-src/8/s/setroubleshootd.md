---
title: "setroubleshootd(8)"
name: "setroubleshootd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setroubleshootd/"
description: "setroubleshootd – setroubleshoot daemon"
---

<p>setroubleshootd &#8211; setroubleshoot daemon </p>
<h2>Synopsis</h2>
<p><code>setroubleshootd</code> <i>[-d] [-f] [-h] [-c config]</i> </p>
<h2>Description</h2>
<p>This manual page describes the <code>setroubleshootd</code> program. setroubleshootd is the dbus service in the setroubleshoot system. setroubleshoot is used to diagnose SELinux denials and attempts to provide user friendly explanations for a SELinux denial (e.g. AVC) and recommendations for how one might adjust the system to prevent the denial in the future. In a standard configuration setroubleshoot is composed of two components, sealert and setroubleshootd. setroubleshootd is a system daemon which runs under setroubleshoot user and listens for audit events emitted from the kernel related to SELinux. When the setroubleshootd daemon sees an SELinux AVC denial it runs a series of analysis plugins which examines the audit data related to the AVC. It records the results of the analysis and signals any clients which have attached to the setroubleshootd daemon that a new alert has been seen. </p>
<h2>Options</h2>
<dl>
<dt><code>-f &#8211;nofork</code></p>
<dd>Do not fork the daemon</p>
<dt><code>-d &#8211;debug</code></p>
<dd>Do not exit after 10 seconds</p>
<dt><code>-h &#8211;help </code></p>
<dd>Show this message</p>
<dt><code>-c &#8211;config</code></p>
<dd>section.option=value<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>set a configuration value</p>
</dl>
<h2>Author</h2>
<p>This man page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sealert/">sealert</a>(8),</code><a href="/docs/linux/man/8-selinux/">selinux</a><code>(8)</code> </p>
