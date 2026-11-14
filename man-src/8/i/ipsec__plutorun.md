---
title: "ipsec__plutorun(8)"
name: "ipsec__plutorun"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec__plutorun/"
description: "ipsec__plutorun – internal script to (re)start pluto on old SYSV initscript systems"
---

<p>ipsec__plutorun &#8211; internal script to (re)start pluto on old SYSV initscript systems</p>
<h2>Description</h2>
<p><i>_plutorun</i> is called by <code>_realsetup</code> to configure and bring up <code><a href="/docs/linux/man/8-pluto/">pluto</a>(8).</code> It invokes pluto, and watches to makes sure that pluto is restarted if it fails, as the SYSV initscripts do not provide a restart facility. When other init systems are used, such as systemd or upstart, _plutorun is not used.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_setup/">ipsec_setup</a></code>(8), <code><a href="/docs/linux/man/8-ipsec__realsetup/">ipsec__realsetup</a></code>(8), <code><a href="/docs/linux/man/8-pluto/">pluto</a></code>(8).</p>
<h2>History</h2>
<p>Man page written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Michael Richardson. Original program written by Henry Spencer. Updated for the Libreswan project &lt;m[blue]<code><a href="http://www.libreswan.org/">http://www.libreswan.org/</a></code>m[]&gt; by Paul Wouters</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
