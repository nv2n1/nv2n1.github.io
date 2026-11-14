---
title: "ipsec_tncfg(8)"
name: "ipsec_tncfg"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_tncfg/"
description: "ipsec_tncfg – manipulate KLIPS virtual interfaces"
---

<p>ipsec_tncfg &#8211; manipulate KLIPS virtual interfaces</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> tncfg</p>
<dd>
<dd>ipsec tncfg &#8211;create <i>virtual</i><br />
 ipsec tncfg &#8211;delete <i>virtual</i><br />
 ipsec tncfg &#8211;attach &#8211;virtual <i>virtual</i> &#8211;physical <i>physical</i><br />
 ipsec tncfg &#8211;detach &#8211;virtual <i>virtual</i><br />
 ipsec tncfg &#8211;clear<br />
 ipsec tncfg &#8211;version<br />
 ipsec tncfg &#8211;help</dl>
<h2>Klips</h2>
<p>Note that tncfg is only supported on the KLIPS stack which uses ipsecX interfaces bound to physical interfaces</p>
<h2>Description</h2>
<p>The purpose of <i>tncfg</i> is to attach/detach IPsec virtual interfaces (e.g. ipsec0) to/from physical interfaces (e.g. eth0) through which packets will be forwarded once processed by KLIPS. </p>
<p> When using the MAST stack, tncfg is used to create and delete virtual interfaces known as mastXXX. mast stands for Mooring and XXX. </p>
<p> The form with no additional arguments lists the contents of /proc/net/ipsec_tncfg. The format of /proc/net/ipsec_tncfg is discussed in <a href="/docs/linux/man/5-ipsec_tncfg/">ipsec_tncfg</a>(5). </p>
<p> The <code>&#8211;attach</code> form attaches the <i>virtual</i> interface to the <i>physical</i> one. </p>
<p> The <code>&#8211;detach</code> form detaches the <i>virtual</i> interface from whichever physical interface it is attached to. </p>
<p> The <code>&#8211;clear</code> form clears all the <i>virtual</i> interfaces from whichever physical interfaces they were attached to. </p>
<p> Virtual interfaces typically have names like <code>ipsec0</code> or <code>mast0</code> while physical interfaces typically have names like <code>eth0</code> or <code>ppp0</code>.</p>
<h2>Examples</h2>
<p><code>ipsec tncfg &#8211;create mast12</code></p>
<dl>
<dd>creates the mast12 device.</dl>
<p> <code>ipsec tncfg &#8211;create ipsec4</code></p>
<dl>
<dd>creates an ipsec4 device, but does not attach it.</dl>
<p> <code>ipsec tncfg &#8211;attach &#8211;virtual ipsec0 &#8211;physical eth0</code></p>
<dl>
<dd>attaches the <code>ipsec0</code> virtual device to the <code>eth0</code> physical device.</dl>
<h2>Files</h2>
<p>/proc/net/ipsec_tncfg, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/8-ipsec_eroute/">ipsec_eroute</a>(8), <a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a>(8), <a href="/docs/linux/man/8-ipsec_spigrp/">ipsec_spigrp</a>(8), <a href="/docs/linux/man/8-ipsec_klipsdebug/">ipsec_klipsdebug</a>(8), <a href="/docs/linux/man/5-ipsec_tncfg/">ipsec_tncfg</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
