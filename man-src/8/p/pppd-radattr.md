---
title: "pppd-radattr(8)"
name: "pppd-radattr"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppd-radattr/"
description: "radattr.so – RADIUS utility plugin for"
---

<p>radattr.so &#8211; RADIUS utility plugin for <code></p>
<p> <a href="/docs/linux/man/8-pppd/">pppd</a></code>(8)</p>
<h2>Synopsis</h2>
<p><code>pppd</code> [ <i>options</i> ] plugin radius.so plugin radattr.so</p>
<h2>Description</h2>
<p>The radattr plugin for pppd causes all radius attributes returned by the RADIUS server at authentication time to be stored in the file <i>/var/run/radattr.pppN</i> where <i>pppN</i> is the name of the PPP interface. The RADIUS attributes are stored one per line in the format &quot;Attribute-Name Attribute-Value&quot;. This format is convenient for use in /etc/ppp/ip-up and /etc/ppp/ip-down scripts. Note that you <i>must</i> load the radius.so plugin before loading the radattr.so plugin; radattr.so depends on symbols defined in radius.so. </p>
<h2>Usage</h2>
<p>To use the plugin, simply supply the <code>plugin radius.so plugin radattr.so</code> options to pppd.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8)<code> <a href="/docs/linux/man/8-pppd-radius/">pppd-radius</a></code>(8) </p>
<h2>Author</h2>
<p>David F. Skoll &lt;dfs [at] roaringpenguin.com&gt;</p>
