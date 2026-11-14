---
title: "xrdp-sesrun(8)"
name: "xrdp-sesrun"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdp-sesrun/"
description: "xrdp-sesrun – sesman(8) session launcher"
---

<p>xrdp-sesrun &#8211; <code><a href="/docs/linux/man/8-sesman/">sesman</a></code>(8) session launcher </p>
<h2>Syntax</h2>
<p><code>xrdp-sesrun</code> <i>server username password width height bpp</i></p>
<h2>Description</h2>
<p><code>xrdp-sesrun</code> starts a session using <code><a href="/docs/linux/man/8-xrdp-sesman/">xrdp-sesman</a></code>(8).<br />
 This is a tool useful for testing, it simply behaves like xrdp when some user logs in a new session and authenticates, thus starting a new session. </p>
<h2>Options</h2>
<dl>
<dt><i>server</i></p>
<dd>Server on which sesman is running</p>
<dt><i>username</i></p>
<dd>user name of the session being started</p>
<dt><i>password</i></p>
<dd>user password</p>
<dt><i>width</i></p>
<dd>Screen width</p>
<dt><i>height</i></p>
<dd>Screen height</p>
<dt><i>bpp</i></p>
<dd>Session color depth </p>
</dl>
<h2>Files</h2>
<p>${SESMAN_BIN_DIR}/sesman<br />
 ${SESMAN_BIN_DIR}/sesrun</p>
<h2>Authors</h2>
<p>Jay Sorg &lt;jsorg71 [at] users.sourceforge.net&gt;<br />
 Simone Fedele &lt;ilsimo [at] users.sourceforge.net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xrdp-sesman/">xrdp-sesman</a></code>(8), <code><a href="/docs/linux/man/5-sesman-ini/">sesman.ini</a></code>(5), <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8), <code><a href="/docs/linux/man/5-xrdp-ini/">xrdp.ini</a></code>(5) for more info on <code>xrdp</code> see <a rel="nofollow" href="http://www.xrdp.org/">http://www.xrdp.org/</a> </p>
