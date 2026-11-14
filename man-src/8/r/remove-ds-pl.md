---
title: "remove-ds-pl(8)"
name: "remove-ds-pl"
section: "8"
letter: "r"
url: "/docs/linux/man/8-remove-ds-pl/"
description: "remove-ds.pl – Remove an instance of Directory Server"
---

<p>remove-ds.pl &#8211; Remove an instance of Directory Server</p>
<h2>Synopsis</h2>
<p><code>remove-ds.pl</code> [-a] [-f] [-d -d &#8230; -d] -i <i>instance</i></p>
<h2>Description</h2>
<p>Removes a Directory Server instance from the system. The instance will be shutdown and the files will be removed. The certificate database files will not be removed. The instance configuration directory will have a .removed extension appended to it, which will contain the retained certificate database files. </p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-a</code></p>
<dd>Removes all files and directories belonging to the instance</p>
<dt><code>-f</code></p>
<dd>Force removal</p>
<dt><code>-d</code></p>
<dd>Enable debugging: adding more -d will make output more verbose</p>
<dt><code>-i</code> <i>instance</i></p>
<dd>The full name of the instance to remove (e.g. slapd-example)
</dl>
<h2>Author</h2>
<p>remove-ds.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Red Hat, Inc.<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution.</p>
