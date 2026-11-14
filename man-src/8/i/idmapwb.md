---
title: "idmapwb(8)"
name: "idmapwb"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idmapwb/"
description: "idmapwb.so – winbind ID mapping plugin for cifs-utils"
---

<p>idmapwb.so &#8211; winbind ID mapping plugin for cifs-utils</p>
<h2>Description</h2>
<p>This plugin allows the utilities in cifs-utils to work in conjuction with the winbind facility of Samba suite. It handles several functions including mapping <font SIZE="-1">UID</font> and <font SIZE="-1">GID</font> to SIDs and vice versa. </p>
<p> Utilities are usually configured to use the correct plugin by creating a symlink at <tt>@pluginpath</tt>@ that points to the correct plugin that you wish to use. </p>
<p> This plugin requires that <a href="/docs/linux/man/8-winbindd/">winbindd</a><code>(8)</code> be properly configured and running.</p>
<h2>SEE ALSO <i><a href="/docs/linux/man/1-getcifsacl/">getcifsacl</a></i>(1), <i><a href="/docs/linux/man/1-setcifsacl/">setcifsacl</a></i>(1), <i><a href="/docs/linux/man/8-cifs-idmap/">cifs.idmap</a></i>(8), <i><a href="/docs/linux/man/7-samba/">samba</a></i>(7), <i><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></i>(5), <i><a href="/docs/linux/man/8-winbindd/">winbindd</a></i>(8)</h2>
<h2>AUTHOR idmapwb.so was written by Jeff Layton &lt;jlayton [at] samba.org&gt;</h2>
