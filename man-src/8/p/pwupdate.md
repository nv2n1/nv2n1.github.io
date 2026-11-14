---
title: "pwupdate(8)"
name: "pwupdate"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pwupdate/"
description: "pwupdate – updates passwd and shadow NIS map"
---

<p>pwupdate &#8211; updates passwd and shadow NIS map</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/lib/yp/pwupdate</code> [<i>shadow</i>]</dl>
<h2>Description</h2>
<p><code>pwupdate</code></p>
<dd>is invoked by <code><a href="/docs/linux/man/8-rpc-yppasswdd/">rpc.yppasswdd</a></code>(8) after changing the password and it should update the passwd and shadow NIS map. Never run it by hand.</p>
<h2>Options</h2>
<p><code>shadow</code></p>
<dl>
<dd>Normally, only the passwd map will be updated. With this option, <code>pwupdate</code> will update the shadow map, too.</dl>
<h2>Files</h2>
<p><i>/etc/passwd</i>, <i>/etc/shadow</i></p>
<dl>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rpc-yppasswdd/">rpc.yppasswdd</a></code>(8), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8)</p>
<h2>Author</h2>
<p>Olaf Kirch &lt;okir [at] monad.swb.de&gt;, Thorsten Kukuk &lt;kukuk [at] suse.de&gt;</p>
