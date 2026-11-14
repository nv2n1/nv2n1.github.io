---
title: "pppoeconf(8)"
name: "pppoeconf"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppoeconf/"
description: "pppoeconf — configures a PPPoE (ADSL) connection"
---

<p>pppoeconf &#8212; configures a PPPoE (ADSL) connection</p>
<h2>Synopsis</h2>
<p><code>pppoeconf</code> [<i>-nox</i>] [<i>iface</i>]</p>
<h2>Description</h2>
<p>The <code>pppoeconf</code> program is user-friendly dialog based setup tool for <code>pppd</code> (and <code>pppoe</code> if needed). It will look for existing ethernet cards and look for ADSL hardware connected to one of them. You can add an interface name <code>iface</code> to force pppoeconf to use it. Then it will get some login info and do some minor modifications to make working settings. Note that you can use ESC key to exit program when you wan.</p>
<h2>Options</h2>
<dl>
<dt><code>-nox</code></p>
<dd>Force ncurses use.</dl>
<h2>Files</h2>
<p><code>/etc/ppp/peers/dsl-provider</code> is pppd options file for your dsl provider. </p>
<p> <code>/etc/ppp/pap-secrets</code> and <code>/etc/ppp/chap-secrets</code> are described in pppd documentation. pppoeconf may add lines to theses files. </p>
<p> <code>/etc/ppp/ip-up.d/0clampmss</code> and <code>/etc/ppp/ip-down.d/0clampmss</code> are used to clamp MSS if needed. </p>
<p> <code>/etc/network/interfaces</code> is network interface file for your system.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/5-interfaces/">interfaces</a>(5), <a href="/docs/linux/man/1-pon/">pon</a>(1) and <a href="/docs/linux/man/8-pppoe/">pppoe</a>(8).</p>
<h2>Author</h2>
<p>This manual page was originally written by Eduard Bloch (blade [at] debian.org) and now maintained by Gregory Colpart (reg [at] evolix.fr) for the <code>Debian GNU/Linux</code> system (but may be used by others). This document is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
