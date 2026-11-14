---
title: "fbdev(4)"
name: "fbdev"
section: "4"
letter: "f"
url: "/docs/linux/man/4-fbdev/"
description: "fbdev – video driver for framebuffer device"
---

<p>fbdev &#8211; video driver for framebuffer device</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;fbdev&#34;</code>
<code> BusID &#34;pci:</code><i>bus</i><code>:</code><i>dev</i><code>:</code><i>func</i><code>&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>fbdev</code> is an Xorg driver for framebuffer devices. This is a non-accelerated driver, the following framebuffer depths are supported: 8, 15, 16, 24. All visual types are supported for depth 8, and TrueColor visual is supported for the other depths. Multi-head configurations are supported.</p>
<h2>Supported Hardware</h2>
<p>The <code>fbdev</code> driver supports all hardware where a framebuffer driver is available. fbdev uses the os-specific submodule <a href="/docs/linux/man/4-fbdevhw/">fbdevhw</a>(4) to talk to the kernel device driver. Currently a fbdevhw module is available for linux.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> For this driver it is not required to specify modes in the screen section of the config file. The <code>fbdev</code> driver can pick up the currently used video mode from the framebuffer driver and will use it if there are no video modes configured. </p>
<p> For PCI boards you might have to add a BusID line to the Device section. See above for a sample line. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;fbdev&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>The framebuffer device to use. Default: /dev/fb0.</p>
<dt><code>Option &#34;ShadowFB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. Mandatory for 24bpp framebuffers on newer servers. Default: on.</p>
<dt><code>Option &#34;Rotate&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Enable rotation of the display. The supported values are &quot;CW&quot; (clockwise, 90 degrees), &quot;UD&quot; (upside down, 180 degrees) and &quot;CCW&quot; (counter clockwise, 270 degrees). Implies use of the shadow framebuffer layer. Disabled for 24bpp framebuffers. Default: off.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/4-fbdevhw/">fbdevhw</a>(4)</p>
<h2>Authors</h2>
<p>Authors include: Gerd Knorr, Michel D&auml;nzer, Geert Uytterhoeven</p>
