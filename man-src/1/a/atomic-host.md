---
title: "atomic-host(1)"
name: "atomic-host"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-host/"
description: "atomic-host – Manage Atomic Host Commands"
---

<h2 class="name">NAME</h2>
<p> atomic-host &#8211; Manage Atomic Host Commands </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic host [OPTIONS] COMMAND</code> </p>
<p> This command is a high-level wrapper for the underlying rpm-ostree tool which can perform upgrades, rollbacks, and system state inspection. It is used for implementations of the Project Atomic Host pattern. </p>
<p> #NOTE The host subcommand is only available on Atomic Host Systems. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code> <code>-help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-r</code> <code>&#8211;reboot</code> Initiate a reboot after rollback is prepared. </p>
<h2>COMMANDS</h2>
<p> <code>status</code> List information about all deployments </p>
<p> <code>rollback</code> Switch to alternate installed tree at next boot </p>
<p> <code>upgrade</code> Upgrade to the latest Atomic tree if one is available </p>
<p> <code>deploy</code> Download and deploy a specific Atomic tree </p>
<p> <code>unlock</code> Remove the read-only bind mount on /usr and replace it with a writable overlay filesystem. This default invocation of &quot;unlock&quot; is intended for development/testing purposes. All changes in the overlay are lost on reboot (or upgrade). Pass &#8211;hotfix to create changes that persist on reboot (but still not upgrades). </p>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd>
<pre>
man rpm-ostree 
man ostree 
</pre>
</dl>
<h2>HISTORY</h2>
<p> January 2015, Originally compiled by Daniel Walsh (dwalsh at redhat dot com) </p>
<h2>Index</h2>
