---
title: "saveconfig(8)"
name: "saveconfig"
section: "8"
letter: "s"
url: "/docs/linux/man/8-saveconfig/"
description: "saveconfig – Directory Server script for saving the Admin Server configuration"
---

<p>saveconfig &#8211; Directory Server script for saving the Admin Server configuration</p>
<h2>Synopsis</h2>
<p>saveconfig [ -Z serverID ] [-h]</p>
<h2>Description</h2>
<p>Makes a backup of the Admin Server configuration information and stores it in /var/lib/dirsrv/slapd-instance_name/bak.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></dt>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</dd>
<dt><code>-h</code></dt>
<dd>Display the usage.</dd></dl>
<h2>Example</h2>
<dl>
<dt>saveconfig</dt>
<dd>
</dd><dt>saveconfig -Z instance3</dt>
<dd></dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>saveconfig was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
