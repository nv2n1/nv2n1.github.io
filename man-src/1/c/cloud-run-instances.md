---
title: "cloud-run-instances(1)"
name: "cloud-run-instances"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cloud-run-instances/"
description: "cloud-run-instances – wrapper for euca-run-instances that supports an option for injecting public ssh keys retrievable from Launchpad.net"
---

<h2>NAME</h2>
<p> <code>cloud-run-instances</code> &#8211; wrapper for euca-run-instances that supports an option for injecting public ssh keys retrievable from <i>Launchpad.net</i> </p>
<h2>SYNOPSIS</h2>
<p> <code>cloud-run-instances [-l|&#8211;launchpad-id lp_id_1,lp_id_2,lp_id_3] [euca-run-instances options]</code> </p>
<h2>DESCRIPTION</h2>
<p> This program is a wrapper script for <code><a href="/docs/linux/man/1-euca-run-instances/">euca-run-instances</a></code>(1) that takes one additional option, <code>-l|&#8211;launchpad-id</code>. </p>
<p> With this option, a user can specify a comma-separated list of <i>Launchpad.net</i> usernames. </p>
<p> Once the instance is booted, the cloud-init boot script will retrieve the public ssh keys of the specified users from Launchpad.net using <code><a href="/docs/linux/man/1-ssh-import-lp-id/">ssh-import-lp-id</a></code>(1). </p>
<p> All other options besides <code>-l|&#8211;launchpad-id</code> are simply passed on to <code><a href="/docs/linux/man/1-euca-run-instances/">euca-run-instances</a></code>(1). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-euca-run-instances/">euca-run-instances</a></code>(1), <code><a href="/docs/linux/man/1-ssh-import-lp-id/">ssh-import-lp-id</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manpage and the utility was written by Dustin Kirkland &lt;kirkland [at] canonical.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
