---
title: "fbdevhw(4)"
name: "fbdevhw"
section: "4"
letter: "f"
url: "/docs/linux/man/4-fbdevhw/"
description: "fbdevhw – os-specific submodule for framebuffer device access"
---

<p>fbdevhw &#8211; os-specific submodule for framebuffer device access</p>
<h2>Description</h2>
<p><code>fbdevhw</code> provides functions for talking to a framebuffer device. It is os-specific. It is a submodule used by other video drivers. A <code>fbdevhw</code> module is currently available for linux framebuffer devices. </p>
<p> <a href="/docs/linux/man/4-fbdev/">fbdev</a>(4) is a non-accelerated driver which runs on top of the fbdevhw module. fbdevhw can be used by other drivers too, this is usually activated with `Option &quot;UseFBDev&quot;&#8217; in the device section.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xorgconfig/">xorgconfig</a>(1), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/4-fbdev/">fbdev</a>(4)</p>
<h2>Authors</h2>
<p>Authors include: Gerd Knorr, based on the XF68_FBDev Server code (Martin Schaller, Geert Uytterhoeven).</p>
