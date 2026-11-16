---
title: "xrdp-chansrv(8)"
name: "xrdp-chansrv"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdp-chansrv/"
description: "xrdp-chansrv – xrdp channel server"
---

<p><code>xrdp-chansrv</code> &#8211; <code>xrdp</code> channel server </p>
<h2>Syntax</h2>
<p><code>xrdp-chansrv</code></p>
<h2>Description</h2>
<p><code>xrdp-chansrv</code> is the <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) channel server, which manages the Remote Desktop Protocol (RDP) sub-channels. This program is only forked internally by <code><a href="/docs/linux/man/8-xrdp-sesman/">xrdp-sesman</a></code>(8).<br />
 Currently <code>xrdp-chansrv</code> knows about the following channels:</p>
<dl>
<dt><code>cliprdr</code></dt>
<dd>Clipboard Redirection</dd>
<dt><code>rdpsnd</code></dt>
<dd>Remote Desktop Protocol Sound</dd>
<dt><code>rdpdr</code></dt>
<dd>Remote Desktop Protocol Device Redirection</dd>
<dt><code>rail</code></dt>
<dd>Remote Applications Integrated Locally</dd>
<dt><code>drdynvc</code></dt>
<dd>Dynamic Virtual Channel</dd>
<dl>
<dd>
<h2>Files</h2>
</dd><dl>
<dt><i>/tmp/.xrdp/xrdp_chansrv_socket_*</i></dt>
<dd>UNIX socket used by external programs to implement channels.</dd>
<dt><i>/tmp/.xrdp/xrdp_api_*</i></dt>
<dd>UNIX socket used by <code>xrdp-chansrv</code> to communicate with <code>xrdp-sesman</code>.</dd>
<dt><i>$XDG_DATA_HOME/xrdp/xrdp-chansrv.log</i></dt>
<dd>Log file used by <code><a href="/docs/linux/man/8-xrdp-chansrv/">xrdp-chansrv</a></code>(8). </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xrdp-sesman/">xrdp-sesman</a></code>(8), <code><a href="/docs/linux/man/5-sesman-ini/">sesman.ini</a></code>(5). for more info on <code>xrdp</code> see <a rel="nofollow" href="http://www.xrdp.org/">http://www.xrdp.org/</a> </p>
</dl></dl>