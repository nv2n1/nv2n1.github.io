---
title: "remove-ds-admin-pl(8)"
name: "remove-ds-admin-pl"
section: "8"
letter: "r"
url: "/docs/linux/man/8-remove-ds-admin-pl/"
description: "remove-ds-admin.pl – Remove all Directory Servers and Admin Server"
---

<p>remove-ds-admin.pl &#8211; Remove all Directory Servers and Admin Server</p>
<h2>Synopsis</h2>
<p><code>remove-ds-admin.pl</code> [-f] [-d -d &#8230; -d] [-y] [-a]</p>
<h2>Description</h2>
<p>Shuts down and removes all Directory Server instances and the Admin Server from the system. The directory server instance configuration directories will have a .removed extension appended to them, which will contain the retained certificate database files. <code>WARNING: This command is extremely destructive!</code> It will remove all of the data and configuration of all directory servers and admin servers, with no chance of recovery. Therefore, in order to actually do this, you must give the -y option. <code>Please use caution and backup your data if you want to keep it!</code> </p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-f</code></p>
<dd>Force removal &#8211; continue on error &#8211; otherwise, the command will abort at the first error encountered</p>
<dt><code>-d</code></p>
<dd>Enable debugging &#8211; adding more -d will make output more verbose</p>
<dt><code>-y</code></p>
<dd>Do the actual processing. Since the command is very destructive, you must provide the -y argument in order for the operation to proceed. <code>Use with extreme caution!</code> Note, the security/certificate files are preserved for future setups.</p>
<dt><code>-a</code></p>
<dd>Remove all the security/certificate files (used with the -y option). This ensures a complete clean up of the previous installation.
</dl>
<h2>Author</h2>
<p>remove-ds-admin.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Red Hat, Inc.<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution.</p>
