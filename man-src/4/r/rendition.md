---
title: "rendition(4)"
name: "rendition"
section: "4"
letter: "r"
url: "/docs/linux/man/4-rendition/"
description: "rendition – Rendition video driver"
---

<p>rendition &#8211; Rendition video driver</p>
<h2>Synopsis</h2>
<pre><code>Section N'34'DeviceN'34'</code>
<code> Identifier N'34'</code><i>devname</i><code>N'34'</code>
<code> Driver N'34'renditionN'34'</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>rendition </code> is an Xorg driver for Rendition/Micron based video cards. The driver supports following framebuffer depths: 8, 15 (Verite V1000 only), 16 and 24. Acceleration and multi-head configurations are not supported yet, but are work in progress.</p>
<h2>Supported Hardware</h2>
<p>The <code>rendition</code> driver supports PCI and AGP video cards based on the following Rendition/Micron chips:</p>
<dl>
<dt><code>V1000</code></p>
<dd>Verite V1000 based cards.</p>
<dt><code>V2100</code></p>
<dd>Verite V2100 based cards. Diamond Stealth II S220 is the only known such card.</p>
<dt><code>V2200</code></p>
<dd>Verite V2200 based cards.</dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The driver auto-detects the chipset type, but the following <code>ChipSet</code> names may optionally be specified in the config file <code>N&#8217;34&#8217;DeviceN&#8217;34&#8217;</code> section, and will override the auto-detection: </p>
<dl>
<dd>&quot;v1000&quot;, &quot;v2x00&quot;.</dl>
<p> The driver will auto-detect the amount of video memory present for all chips. If the amount of memory is detected incorrectly, the actual amount of video memory should be specified with a <code>VideoRam</code> entry in the config file <code>N&#8217;34&#8217;DeviceN&#8217;34&#8217;</code> section. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;SWCursorN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Disables use of the hardware cursor. Default: use HW-cursor.</p>
<dt><code>Option N&#8217;34&#8217;OverclockMemN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Increases the Mem/Sys clock to 125MHz/60MHz from standard 110MHz/50MHz. Default: Not overclocked.</p>
<dt><code>Option N&#8217;34&#8217;DacSpeedN&#8217;34&#8217; N&#8217;34&#8217;</code><i>MHz</i><code>N&#8217;34&#8217;</code></p>
<dd>Run the memory at a higher clock. Useful on some cards with display glitches at higher resolutions. But adds the risk to damage the hardware. Use with caution.</p>
<dt><code>Option N&#8217;34&#8217;FramebufferWCN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>If writecombine is disabled in BIOS, and you add this option in configuration file, then the driver will try to request writecombined access to the framebuffer. This can drastically increase the performance on unaccelerated server. Requires that &quot;MTRR&quot;-support is compiled into the OS-kernel. Default: Disabled for V1000, enabled for V2100/V2200.</p>
<dt><code>Option N&#8217;34&#8217;NoDDCN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Disable probing of DDC-information from your monitor. This information is not used yet and is only there for informational purposes. Safe to disable if you experience problems during startup of X-server. Default: Probe DDC.</p>
<dt><code>Option N&#8217;34&#8217;ShadowFBN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>If this option is enabled, the driver will cause the CPU to do each drawing operation first into a shadow frame buffer in system virtual memory and then copy the result into video memory. If this option is not active, the CPU will draw directly into video memory. Enabling this option is beneficial for those systems where reading from video memory is, on average, slower than the corresponding read/modify/write operation in system virtual memory. This is normally the case for PCI or AGP adapters, and, so, this option is enabled by default unless acceleration is enabled. Default: Enabled unless acceleration is used.</p>
<dt><code>Option N&#8217;34&#8217;RotateN&#8217;34&#8217; N&#8217;34&#8217;CWN&#8217;34&#8217;</code></p>
<dd>
<dt><code>Option N&#8217;34&#8217;RotateN&#8217;34&#8217; N&#8217;34&#8217;CCWN&#8217;34&#8217;</code></p>
<dd>Rotate the display clockwise or counterclockwise. This mode is unaccelerated. Default: no rotation.</p>
<dt></dl>
<h2>Notes</h2>
<dd>For the moment the driver defaults to not request write-combine for any chipset as there has been indications of problems with it. Use <code>Option N&#8217;34&#8217;MTRRN&#8217;34&#8217;</code> to let the driver request write-combining of memory access on the video board.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: Marc Langenbach, Dejan Ilic</p>
