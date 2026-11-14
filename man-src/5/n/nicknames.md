---
title: "nicknames(5)"
name: "nicknames"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nicknames/"
description: "/var/yp/nicknames – nickname translation table for NIS maps"
---

<p>/var/yp/nicknames &#8211; nickname translation table for NIS maps</p>
<h2>Description</h2>
<p><code>nicknames</code> contains a list of aliases and the corresponding NIS maps. There is one entry per line. The default <code>nicknames</code> table looks like:</p>
<dl>
<dd>
<dl>
<dd>
<dt><code>passwd</p>
<dd>passwd.byname</p>
<dt>group</p>
<dd>group.byname</p>
<dt>networks</p>
<dd>networks.byaddr</p>
<dt>hosts</p>
<dd>hosts.byname</p>
<dt>protocols</p>
<dd>protocols.bynumber</p>
<dt>services</p>
<dd>services.byname</p>
<dt>aliases</p>
<dd>mail.aliases</p>
<dt>ethers</p>
<dd>ethers.byname</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ypcat/">ypcat</a></code>(1), <code><a href="/docs/linux/man/1-ypmatch/">ypmatch</a></code>(1), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/1-ypwhich/">ypwhich</a></code>(1) </p>
<h2>Author</h2>
<p>The <code>yp-tools</code> package was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;.</p>
