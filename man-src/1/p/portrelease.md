---
title: "portrelease(1)"
name: "portrelease"
section: "1"
letter: "p"
url: "/docs/linux/man/1-portrelease/"
description: "portrelease – release previously-reserved ports"
---

<h2 class="name">NAME</h2>
<p> portrelease &#8211; release previously-reserved ports </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>portrelease</code> [<i>SVC</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>portrelease</code> program instructs the <code>portreserve</code> daemon to release the port associated with the given service configuration file. </p>
<p> It is intended that <code>portrelease</code> is run by the initscript of the service wanting the port. For example, the cups initscript might run <code>portrelease cups</code>.</p>
<h2>EXIT CODE</h2>
<p> An exit code of zero means that a best effort attempt has been made to instruct the daemon to release the port. Non-zero exit codes mean that the daemon is running but couldn&#8217;t be contacted.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-portreserve/">portreserve</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
