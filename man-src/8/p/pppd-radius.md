---
title: "pppd-radius(8)"
name: "pppd-radius"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppd-radius/"
description: "radius.so – RADIUS authentication plugin for"
---

<p>radius.so &#8211; RADIUS authentication plugin for <code></p>
<p> <a href="/docs/linux/man/8-pppd/">pppd</a></code>(8)</p>
<h2>Synopsis</h2>
<p><code>pppd</code> [ <i>options</i> ] plugin radius.so</p>
<h2>Description</h2>
<p>The RADIUS plugin for pppd permits pppd to perform PAP, CHAP, MS-CHAP and MS-CHAPv2 authentication against a RADIUS server instead of the usual <i>/etc/ppp/pap-secrets</i> and <i>/etc/ppp/chap-secrets</i> files. The RADIUS plugin is built on a library called <code>radiusclient</code> which has its own configuration files (usually in <i>/etc/radiusclient</i>), consult those files for more information on configuring the RADIUS plugin </p>
<h2>Options</h2>
<p>The RADIUS plugin introduces one additional pppd option:</p>
<dl>
<dt><code>radius-config-file </code><i>filename</i></p>
<dd>The file <i>filename</i> is taken as the radiusclient configuration file. If this option is not used, then the plugin uses <i>/etc/radiusclient/radiusclient.conf</i> as the configuration file.</p>
<dt><code>avpair </code><i>attribute=value</i></p>
<dd>Adds an Attribute-Value pair to be passed on to the RADIUS server on each request.</p>
<dt><code>map-to-ifname</code></p>
<dd>Sets Radius NAS-Port attribute to number equal to interface name (Default)</p>
<dt><code>map-to-ttyname</code></p>
<dd>Sets Radius NAS-Port attribute value via libradiusclient library </p>
</dl>
<h2>Usage</h2>
<p>To use the plugin, simply supply the <code>plugin radius.so</code> option to pppd, and edit <i>/etc/radiusclient/radiusclient.conf</i> appropriately. If you use the RADIUS plugin, the normal pppd authentication schemes (login, checking the /etc/ppp/*-secrets files) are skipped. The RADIUS server should assign an IP address to the peer using the RADIUS Framed-IP-Address attribute.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8)<code> <a href="/docs/linux/man/8-pppd-radattr/">pppd-radattr</a></code>(8) </p>
<h2>Author</h2>
<p>David F. Skoll &lt;dfs [at] roaringpenguin.com&gt;</p>
