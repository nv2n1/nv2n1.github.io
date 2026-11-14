---
title: "xrdp(8)"
name: "xrdp"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdp/"
description: "xrdp – a Remote Desktop Protocol (RDP) server"
---

<p><code>xrdp</code> &#8211; a Remote Desktop Protocol (RDP) server </p>
<h2>Syntax</h2>
<p>xrdp [ &#8211;nodaemon | &#8211;kill | &#8211;help ]</p>
<h2>Description</h2>
<p><code>xrdp</code> is a Remote Desktop Protocol (RDP) Server.<br />
 Unlike Windows NT/2000/2003 server, <code>xrdp</code> will not display a Windows desktop but an X window desktop to the user. It can also be used as a VNC-&gt;RDP bridge. </p>
<h2>Options</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;nodaemon</code></p>
<dd>Starts <code>xrdp</code> in foreground instead of starting it as a daemon.</p>
<dt><code>-k</code>, <code>&#8211;kill</code></p>
<dd>Kills running <code>xrdp</code> daemon.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Output help information and exit. </p>
</dl>
<h2>Files</h2>
<p>${XRDP_BIN_DIR}/xrdp<br />
 ${XRDP_CFG_DIR}/xrdp.ini<br />
 ${XRDP_LOG_DIR}/xrdp.log<br />
 ${XRDP_PID_DIR}/xrdp.pid</p>
<h2>Authors</h2>
<p>Jay Sorg &lt;jsorg71 [at] users.sourceforge.net&gt;<br />
 Simone Fedele &lt;ilsimo [at] users.sourceforge.net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-xrdp-ini/">xrdp.ini</a></code>(5), <code><a href="/docs/linux/man/8-sesman/">sesman</a></code>(8), <code><a href="/docs/linux/man/5-sesman-ini/">sesman.ini</a></code>(5), <code><a href="/docs/linux/man/8-sesrun/">sesrun</a></code>(8) for more info on <code>xrdp</code> see <a rel="nofollow" href="http://www.xrdp.org/">http://www.xrdp.org/</a> </p>
