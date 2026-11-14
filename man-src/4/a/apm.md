---
title: "apm(4)"
name: "apm"
section: "4"
letter: "a"
url: "/docs/linux/man/4-apm/"
description: "apm – Alliance ProMotion video driver"
---

<p>apm &#8211; Alliance ProMotion video driver</p>
<h2>Synopsis</h2>
<pre><code>Section N'34'DeviceN'34'</code>
<code> Identifier N'34'</code><i>devname</i><code>N'34'</code>
<code> Driver N'34'apmN'34'</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>apm </code> is an Xorg driver for Alliance ProMotion video cards. The driver is accelerated for supported hardware/depth combination. It supports framebuffer depths of 8, 15, 16, 24 and 32 bits. For 6420, 6422, AT24, AT3D and AT25, all depths are fully accelerated except 24 bpp for which only screen to screen copy and rectangle filling is accelerated.</p>
<h2>Supported Hardware</h2>
<p>The <code>apm</code> driver supports PCI and ISA video cards on the following Alliance ProMotion chipsets</p>
<dl>
<dt><code>ProMotion 6420</code></p>
<dd>
<dt><code>ProMotion 6422</code></p>
<dd>
<dt><code>AT24</code></p>
<dd>
<dt><code>AT3D</code></p>
<dd>
<dt><code>AT25</code></p>
<dd></dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The driver auto-detects the chipset type, but the following <code>ChipSet</code> names may optionally be specified in the config file <code>N&#8217;34&#8217;DeviceN&#8217;34&#8217;</code> section, and will override the auto-detection: </p>
<dl>
<dd>&quot;6422&quot;, &quot;at24&quot;, &quot;at3d&quot;. </p>
<p> The AT25 is Chipset &quot;at3d&quot; and the 6420 is 6422. </p>
<p> The driver will auto-detect the amount of video memory present for all chips. The actual amount of video memory can also be specified with a <code>VideoRam</code> entry in the config file <code>N&#8217;34&#8217;DeviceN&#8217;34&#8217;</code> section. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;HWCursorN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable the hardware cursor. Default: on.</p>
<dt><code>Option N&#8217;34&#8217;NoAccelN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option N&#8217;34&#8217;NoLinearN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Disable or enable use of linear frame buffer. Default: on. Note: it may or may not work. Tell me if you need it.</p>
<dt><code>Option N&#8217;34&#8217;PciRetryN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable PCI retries. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;Remap_DPMS_OnN&#8217;34&#8217; N&#8217;34&#8217;</code><i>string</i><code>N&#8217;34&#8217;</code></p>
<dd>
<dt><code>Option N&#8217;34&#8217;Remap_DPMS_StandbyN&#8217;34&#8217; N&#8217;34&#8217;</code><i>string</i><code>N&#8217;34&#8217;</code></p>
<dd>
<dt><code>Option N&#8217;34&#8217;Remap_DPMS_SuspendN&#8217;34&#8217; N&#8217;34&#8217;</code><i>string</i><code>N&#8217;34&#8217;</code></p>
<dd>
<dt><code>Option N&#8217;34&#8217;Remap_DPMS_OffN&#8217;34&#8217; N&#8217;34&#8217;</code><i>string</i><code>N&#8217;34&#8217;</code></p>
<dd>Remaps the corresponding DPMS events. I&#8217;ve found that my Hercules 128/3D swaps Off and Suspend events. You can correct that with </p>
<pre><dl><dt><dd><dl><dt><dd><code>Option N'34'Remap_DPMS_SuspendN'34' N'34'OffN'34'</code>
<code>Option N'34'Remap_DPMS_OffN'34' N'34'SuspendN'34'</code>
</dl></pre>
<p>in the <code>Device</code> section of the config file.</p>
<dl>
<dt><code>Option N&#8217;34&#8217;SWCursorN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Force the software cursor. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;ShadowFBN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. Default: off.</dl>
</dl>
</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: &#8230;</p>
