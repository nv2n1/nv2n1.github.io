---
title: "glint(4)"
name: "glint"
section: "4"
letter: "g"
url: "/docs/linux/man/4-glint/"
description: "glint – GLINT/Permedia video driver"
---

<p>glint &#8211; GLINT/Permedia video driver</p>
<h2>Synopsis</h2>
<pre><code>Section N'34'DeviceN'34'</code>
<code> Identifier N'34'</code><i>devname</i><code>N'34'</code>
<code> Driver N'34'glintN'34'</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>glint </code> is an Xorg driver for 3Dlabs &amp; Texas Instruments GLINT/Permedia based video cards. The driver is rather fully accelerated, and provides support for the following framebuffer depths: 8, 15 (may give bad results with FBDev support), 16, 24 (32 bpp recommended, 24 bpp has problems), 30, and an 8+24 overlay mode.</p>
<h2>Supported Hardware</h2>
<p>The <code>glint</code> driver supports 3Dlabs (GLINT MX, GLINT 500TX, GLINT 300SX, GLINT GAMMA, GLINT DELTA, GLINT GAMMA2, Permedia, Permedia 2, Permedia 2v, Permedia 3, R3, R4) and Texas Instruments (Permedia, Permedia 2) chips.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The driver auto-detects the chipset type, but the following <code>ChipSet</code> names may optionally be specified in the config file <code>N&#8217;34&#8217;DeviceN&#8217;34&#8217;</code> section, and will override the auto-detection: </p>
<dl>
<dd>&quot;ti_pm2&quot;, &quot;ti_pm&quot;, &quot;r4&quot;, &quot;pm3&quot;, &quot;pm2v&quot;, &quot;pm2&quot;, &quot;pm&quot;, &quot;300sx&quot;, &quot;500tx&quot;, &quot;mx&quot;, &quot;gamma&quot;, &quot;gamma2&quot;, &quot;delta&quot;</dl>
<p> The driver will try to auto-detect the amount of video memory present for all chips. If it&#8217;s not detected correctly, the actual amount of video memory should be specified with a <code>VideoRam</code> entry in the config file <code>N&#8217;34&#8217;DeviceN&#8217;34&#8217;</code> section. </p>
<p> Additionally, you may need to specify the bus ID of your card with a <code>BusID</code> entry in the config file <code>N&#8217;34&#8217;DeviceN&#8217;34&#8217;</code> section, especially with FBDev support. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;UseFlatPanelN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable the FlatPanel feature on the Permedia3. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;SWCursorN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable the SW cursor. Default: off. This option disables the <code>HWCursor</code> option and vice versa.</p>
<dt><code>Option N&#8217;34&#8217;NoAccelN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option N&#8217;34&#8217;OverlayN&#8217;34&#8217;</code></p>
<dd>Enable 8+24 overlay mode. Only appropriate for depth 24, 32 bpp. (<code>Note:</code> This hasn&#8217;t been tested with FBDev support and probably won&#8217;t work.) Recognized values are: &quot;8,24&quot;, &quot;24,8&quot;. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;PciRetryN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable PCI retries. (<code>Note:</code> This doesn&#8217;t work with Permedia2 based cards for Amigas.) Default: off.</p>
<dt><code>Option N&#8217;34&#8217;ShadowFBN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. (<code>Note:</code> This disables hardware acceleration.) Default: off.</p>
<dt><code>Option N&#8217;34&#8217;UseFBDevN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable use of an OS-specific fb interface (which is not supported on all OSs). See <a href="/docs/linux/man/4-fbdevhw/">fbdevhw</a>(4) for further information. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;BlockWriteN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable block writes for the various Permedia 2 chips. This improves acceleration in general, but disables it for some special cases. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;FireGL3000N&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>If you have a card of the same name, turn this on. Default: off.</p>
<dt></dl>
<h2>See Also</h2>
<dd><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: Alan Hourihane, Dirk Hohndel, Stefan Dirsch, Michel Dänzer, Sven Luther</p>
