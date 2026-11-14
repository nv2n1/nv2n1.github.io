---
title: "restoreconfig(8)"
name: "restoreconfig"
section: "8"
letter: "r"
url: "/docs/linux/man/8-restoreconfig/"
description: "restoreconfig – Directory Server script for restoring the Admin Server configuration"
---

<p>restoreconfig &#8211; Directory Server script for restoring the Admin Server configuration</p>
<h2>Synopsis</h2>
<p>restoreconfig [ -Z serverID ] [-h]</p>
<h2>Description</h2>
<p>Restores the most recently saved Admin Server configuration information to the NetscapeRoot partition under the /etc/dirsrv/slapd-instance_name/ directory.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-h</code></p>
<dd>Display the usage.</dl>
<h2>Example</h2>
<dl>
<dt>restoreconfig</p>
<dd>
<dt>restoreconfig -Z instance2</p>
<dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>restoreconfig was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
