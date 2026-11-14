---
title: "voodoo(4)"
name: "voodoo"
section: "4"
letter: "v"
url: "/docs/linux/man/4-voodoo/"
description: "voodoo – Voodoo video driver"
---

<p>voodoo &#8211; Voodoo video driver</p>
<h2>Synopsis</h2>
<pre><code>Section N'34'DeviceN'34'</code>
<code> Identifier N'34'</code><i>devname</i><code>N'34'</code>
<code> Driver N'34'voodooN'34'</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>voodoo </code> is an Xorg driver for Voodoo 1 and Voodoo 2 series video adapters. On the Voodoo 1 the driver uses a shadow buffer in system memory as the video adapter has only 3D acceleration. Selected portions of the shadow framebuffer are copied out to the Voodoo board at the right time. Because of this, the speed of the driver is very dependent on the CPU. Processors nowadays are actually rather fast at moving data so we get very good speed anyway as the shadow framebuffer is in cached RAM. </p>
<p> The Voodoo2 has 16bpp acceleration and the driver provides accelerated versions of most operations except angled lines and stipples. Accelerated alpha blending with the Render extension is also supported as is DGA. </p>
<p> This driver supports 16bpp modes currently. The video hardware supports image conversion from 24bpp to 16bpp but the hardware is 16bpp only. </p>
<p> The Voodoo 1 series cards can go up to 800&#215;600 resolution while the Voodoo 2 can reach 1024&#215;768 providing it has at least 2Mb of frame buffer memory. 1024&#215;768 2D mode does not require two cards configured in scan-line interleave mode (SLI). </p>
<p> Multihead and Xinerama configurations are supported. SLI configurations will be treated as multiple video cards. </p>
<p> Limited support for DPMS screen saving is available. The &quot;standby&quot; and &quot;suspend&quot; modes are just painting the screen black. The &quot;off&quot; mode turns the Voodoo board off and thus works correctly. </p>
<p> This driver does not support a virtual screen size different from the display size. This is a hardware limitation. 3D rendering is also not supported.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;ShadowFBN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enables a shadow buffer in main memory. This turns off acceleration but for otherwise unaccelerated operations can improve performance materially. Default: off for voodoo2, on for voodoo1.</p>
<dt><code>Option N&#8217;34&#8217;NoAccelN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Disables acceleration if set. Unless debugging this option should only be set if ShadowFB is enabled. Default: off for voodoo2, on for voodoo1.</dl>
<h2>Bugs</h2>
<p>The driver interacts badly with the sstfb frame buffer driver as there is insufficient information to restore the chip to its previous state.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors: Alan Cox, Ghozlane Toumi, Henrik Harmsen.</p>
