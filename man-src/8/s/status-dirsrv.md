---
title: "status-dirsrv(8)"
name: "status-dirsrv"
section: "8"
letter: "s"
url: "/docs/linux/man/8-status-dirsrv/"
description: "status-dirsrv – script for showing the status of Directory Server"
---

<p>status-dirsrv &#8211; script for showing the status of Directory Server</p>
<h2>Synopsis</h2>
<p><code>status-dirsrv</code> [<i>&lt;instance&gt;</i>]</p>
<h2>Description</h2>
<p>status-dirsrv shows all the status of Directory Server instances on a system, or of a single instance if specified </p>
<h2>Options</h2>
<dl>
<dt><code>&lt;instance&gt;</code></p>
<dd>Specifies a single Directory Server instance to show the status
</dl>
<h2>Usage</h2>
<p>Sample usage:</p>
<dl>
<dt><code>status-dirsrv example</code></p>
<dd></dl>
<h2>Exit Status</h2>
<p>status-dirsrv returns 0 if all Directory Server instances are running. Otherwise, it returns a positive value which represents the number of server instances which are not running. </p>
<p> If a single Directory Server instance is specified, 0 is returned if the instance is running; 1 is returned if the instance is not running; 255 is returned if the instance does not exist.</p>
<h2>Author</h2>
<p>status-dirsrv was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2016 Red Hat, Inc.<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution.</p>
