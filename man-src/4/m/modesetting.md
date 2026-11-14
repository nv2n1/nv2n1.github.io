---
title: "modesetting(4)"
name: "modesetting"
section: "4"
letter: "m"
url: "/docs/linux/man/4-modesetting/"
description: "modesetting – video driver for framebuffer device"
---

<p>modesetting &#8211; video driver for framebuffer device</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;modesetting&#34;</code>
<code> BusID &#34;pci:</code><i>bus</i><code>:</code><i>dev</i><code>:</code><i>func</i><code>&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>modesetting</code> is an Xorg driver for KMS devices. This driver supports TrueColor visuals at framebuffer depths of 15, 16, 24, and 30. RandR 1.2 is supported for multi-head configurations. Acceleration is available through glamor for devices supporting at least OpenGL ES 2.0 or OpenGL 2.1. If glamor is not enabled, a shadow framebuffer is configured based on the KMS drivers&#8217; preference (unless the framebuffer is 24 bits per pixel, in which case the shadow framebuffer is always used).</p>
<h2>Supported Hardware</h2>
<p>The <code>modesetting</code> driver supports all hardware where a KMS driver is available. modesetting uses the Linux DRM KMS ioctls and dumb object create/map.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> For this driver it is not required to specify modes in the screen section of the config file. The <code>modesetting</code> driver can pick up the currently used video mode from the kernel driver and will use it if there are no video modes configured. </p>
<p> For PCI boards you might have to add a BusID line to the Device section. See above for a sample line. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;SWcursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Selects software cursor. The default is <code>off.</code></p>
<dt><code>Option &#34;kmsdev&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>The framebuffer device to use. Default: /dev/dri/card0.</p>
<dt><code>Option &#34;ShadowFB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. Default: on.</p>
<dt><code>Option &#34;DoubleShadow&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Double-buffer shadow updates. When enabled, the driver will keep two copies of the shadow framebuffer. When the shadow framebuffer is flushed, the old and new versions of the shadow are compared, and only tiles that have actually changed are uploaded to the device. This is an optimization for server-class GPUs with a remote display function (typically VNC), where remote updates are triggered by any framebuffer write, so minimizing the amount of data uploaded is crucial. This defaults to enabled for ASPEED and Matrox G200 devices, and disabled otherwise.</p>
<dt><code>Option &#34;AccelMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>One of &#34;glamor&#34; or &#34;none&#34;. Default: glamor.</p>
<dt><code>Option &#34;PageFlip&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable DRI3 page flipping. The default is <code>on.</code></p>
<dt><code>Option &#34;VariableRefresh&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enables support for enabling variable refresh on the Screen&#8217;s CRTCs when an suitable application is flipping via the Present extension.<br />
 The default is <code>off.</code></p>
<dt><code>Option &#34;AsyncFlipSecondaries&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Use async flips for secondary video outputs on multi-display setups. If a screen has multiple displays attached and DRI3 page flipping is used, then only one of the displays will have its page flip synchronized to vblank for tear-free presentation. This is the display that is used for presentation timing and timestamping, usually the one covering the biggest pixel area of the screen. All other displays (&quot;Secondaries&quot;) will not synchronize their flips. This may cause some tearing on these displays, but it prevents a permanent or periodic slowdown or irritating judder of animations if not all video outputs are running synchronized with each other and with the same refresh rate. There is no perfect solution apart from perfectly synchronized outputs, but this option may give preferrable results if the displays in a multi-display setup mirror or clone each other. The default is <code>off.</code></p>
<dt><code>Option &#34;ZaphodHeads&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specify the RandR output(s) to use with zaphod mode for a particular driver instance. If you use this option you must use this option for all instances of the driver.<br />
 For example: <code>Option &#34;ZaphodHeads&#34; &#34;LVDS,VGA-0&#34;</code> will assign xrandr outputs LVDS and VGA-0 to this instance of the driver.</p>
<dt><code>Option &#34;UseGammaLUT&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the GAMMA_LUT property, when available. When enabled, this option allows the driver to use gamma ramps with more entries, if supported by the kernel. By default, GAMMA_LUT will be used for kms drivers which are known to be safe for use of GAMMA_LUT.</p>
<dt></dl>
<h2>See Also</h2>
<dd><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: Dave Airlie</p>
