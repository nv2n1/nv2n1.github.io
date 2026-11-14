---
title: "yppoll(8)"
name: "yppoll"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yppoll/"
description: "yppoll – return version and master server of a NIS map"
---

<p>yppoll &#8211; return version and master server of a NIS map</p>
<h2>Synopsis</h2>
<p><code>yppoll</code> [ <code>-h</code><i> host</i> ] [ <code>-d</code><i> domain</i> ] <i>mapname</i> </p>
<h2>Description</h2>
<p><code>yppoll</code> </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code><i> host</i></p>
<dd>Ask the NIS server process running on <i>host</i> for information about <i>mapname.</i> If <i>host</i> is not specified, the server polled is the default server returned by <code><a href="/docs/linux/man/1-ypwhich/">ypwhich</a></code>(1).</p>
<dt><code>-d</code><i> domain</i></p>
<dd>Specify a domain other than the default domain as returned by <code><a href="/docs/linux/man/8-domainname/">domainname</a></code>(8).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-domainname/">domainname</a></code>(8), <code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8), <code><a href="/docs/linux/man/8-ypcat/">ypcat</a></code>(8), <code><a href="/docs/linux/man/1-ypmatch/">ypmatch</a></code>(1), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-ypset/">ypset</a></code>(8), <code><a href="/docs/linux/man/1-ypwhich/">ypwhich</a></code>(1) </p>
<h2>Author</h2>
<p><code>yppoll</code> is part of the <code>yp-tools</code> package, which was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;.</p>
