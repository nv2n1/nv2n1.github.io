---
title: "xrdp-sesman(8)"
name: "xrdp-sesman"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdp-sesman/"
description: "xrdp-sesman – xrdp(8) session manager"
---

<p>xrdp-sesman &#8211; <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) session manager </p>
<h2>Syntax</h2>
<p><code>xrdp-sesman</code> [<code>&#8211;nodaemon</code>|<code>&#8211;kill</code>|<code>&#8211;help</code>]</p>
<h2>Description</h2>
<p><code>xrdp-sesman</code> is <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) session manager.<br />
 It manages user sessions by authenticating the user and starting the appropriate Xserver. </p>
<h2>Options</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;nodaemon</code></p>
<dd>Starts <code>xrdp-sesman</code> in foreground instead of starting it as a daemon.</p>
<dt><code>-k</code>, <code>&#8211;kill</code></p>
<dd>Kills running <code>xrdp-sesman</code> daemon.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Output help information and exit. </p>
</dl>
<h2>Files</h2>
<p>${SESMAN_BIN_DIR}/sesman<br />
 ${SESMAN_BIN_DIR}/sesrun<br />
 ${SESMAN_CFG_DIR}/sesman.ini<br />
 ${SESMAN_LOG_DIR}/sesman.log<br />
 ${SESMAN_PID_DIR}/sesman.pid</p>
<h2>Authors</h2>
<p>Jay Sorg &lt;jsorg71 [at] users.sourceforge.net&gt;<br />
 Simone Fedele &lt;ilsimo [at] users.sourceforge.net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sesman-ini/">sesman.ini</a></code>(5), <code><a href="/docs/linux/man/8-xrdp-sesrun/">xrdp-sesrun</a></code>(8), <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8), <code><a href="/docs/linux/man/5-xrdp-ini/">xrdp.ini</a></code>(5) for more info on <code>xrdp</code> see <a rel="nofollow" href="http://www.xrdp.org/">http://www.xrdp.org/</a> </p>
