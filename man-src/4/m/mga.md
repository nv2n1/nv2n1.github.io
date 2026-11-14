---
title: "mga(4)"
name: "mga"
section: "4"
letter: "m"
url: "/docs/linux/man/4-mga/"
description: "mga – Matrox video driver"
---

<p>mga &#8211; Matrox video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;mga&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>mga</code> is an Xorg driver for Matrox video cards. The driver is fully accelerated, and provides support for the following framebuffer depths: 8, 15, 16, 24, and an 8+24 overlay mode. All visual types are supported for depth 8, and both TrueColor and DirectColor visuals are supported for the other depths except 8+24 mode which supports PseudoColor, GrayScale and TrueColor. Multi-card configurations are supported. XVideo is supported on G200 and newer systems, with either <code>TexturedVideo</code> or video overlay. The second head of dual-head cards is supported for the G450 and G550. Support for the second head on G400 cards requires a binary-only &quot;mga_hal&quot; module that is available from Matrox &lt;<a rel="nofollow" href="http://www.matrox.com">http://www.matrox.com</a>&gt;, and may be on the CD supplied with the card. That module also provides various other enhancements, and may be necessary to use the DVI (digital) output on the G550 (and other cards).</p>
<h2>Supported Hardware</h2>
<p>The <code>mga</code> driver supports PCI and AGP video cards based on the following Matrox chips. They are listed in approximate chronological order of production (with the most recent chipsets listed last), so consult this list when you are unsure whether your card is meant when references are made to &#8216;G200 and later&#8217; chips, for example.</p>
<dl>
<dt><code>MGA2064W</code></p>
<dd>
<dt><code>MGA1064SG</code></p>
<dd>Mystique</p>
<dt><code>MGA2164W</code></p>
<dd>Millennium II</p>
<dt><code>G100</code></p>
<dd>Productiva G100</p>
<dt><code>G200</code></p>
<dd>Millennium G200 and Mystique G200</p>
<dt><code>G400</code></p>
<dd>Millennium G400, Millennium G400 MAX, Millennium G450, and Marvel G450 eTV</p>
<dt><code>G550</code></p>
<dd>Millennium G550 and Millennium G550 Dual DVI</dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The driver auto-detects the chipset type, but the following <code>ChipSet</code> names may optionally be specified in the config file <code>&#34;Device&#34;</code> section, and will override the auto-detection: </p>
<dl>
<dd>&quot;mga2064w&quot;, &quot;mga1064sg&quot;, &quot;mga2164w&quot;, &quot;mga2164w agp&quot;, &quot;mgag100&quot;, &quot;mgag200&quot;, &quot;mgag200 pci&quot;, &quot;mgag400&quot;, &quot;mgag550&quot;.</dl>
<p> The G450 is Chipset &quot;mgag400&quot; with ChipRev 0x80. </p>
<p> The driver will auto-detect the amount of video memory present for all chips except the Millennium II. In the Millennium II case it defaults to 4096 kBytes. When using a Millennium II, the actual amount of video memory should be specified with a <code>VideoRam</code> entry in the config file <code>&#34;Device&#34;</code> section. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;ColorKey&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Set the colormap index used for the transparency key for the depth 8 plane when operating in 8+24 overlay mode. The value must be in the range 2-255. Default: 255.</p>
<dt><code>Option &#34;HWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable the HW cursor. Default: on.</p>
<dt><code>Option &#34;MGASDRAM&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Specify whether G100, G200 or G400 cards have SDRAM. The driver attempts to auto-detect this based on the card&#8217;s PCI subsystem ID. This option may be used to override that auto-detection. The <code>mga</code> driver is not able to auto-detect the presence of of SDRAM on secondary heads in multihead configurations so this option will often need to be specified in multihead configurations. Default: auto-detected.</p>
<dt><code>Option &#34;NoAccel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option &#34;AccelMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Chooses between available acceleration architectures. Valid options are <code>XAA</code> and <code>EXA.</code> XAA is the traditional acceleration architecture and support for it is very stable. EXA is a newer acceleration architecture with better performance for the Render and Composite extensions, but the rendering code for it is newer and possibly unstable. The default is <code>XAA.</code></p>
<dt><code>Option &#34;NoHal&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable loading the &quot;mga_hal&quot; module. Default: the module is loaded when available and when using hardware that it supports.</p>
<dt><code>Option &#34;OverclockMem&#34;</code></p>
<dd>Set clocks to values used by some commercial X Servers (G100, G200 and G400 only). Default: off.</p>
<dt><code>Option &#34;PciRetry&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable PCI retries. Default: off.</p>
<dt><code>Option &#34;Rotate&#34; &#34;CW&#34;</code></p>
<dd>
<dt><code>Option &#34;Rotate&#34; &#34;CCW&#34;</code></p>
<dd>Rotate the display clockwise or counterclockwise. This mode is unaccelerated. Default: no rotation.</p>
<dt><code>Option &#34;ShadowFB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. Default: off.</p>
<dt><code>Option &#34;SyncOnGreen&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable combining the sync signals with the green signal. Default: off.</p>
<dt><code>Option &#34;UseFBDev&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of on OS-specific fb interface (and is not supported on all OSs). See <a href="/docs/linux/man/4-fbdevhw/">fbdevhw</a>(4) for further information. Default: off.</p>
<dt><code>Option &#34;VideoKey&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This sets the default pixel value for the YUV video overlay key. Default: undefined.</p>
<dt><code>Option &#34;TexturedVideo&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This has XvImage support use the texture engine rather than the video overlay. This option is only supported by G200 and later chips, and only at 16 and 32 bits per pixel. Default: off.</p>
<dt><code>Option &#34;OldDmaInit&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This forces the driver to use the old DMA initialization path for DRI. Use this option only to support a older version of the DRI driver with a newer DRM (version 3.2 or later). This option also disables the use of direct rendering on PCI cards. Default: off.</p>
<dt><code>Option &#34;ForcePciDma&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This forces the use of PCI DMA even if AGP DMA could be used. This option is primarily intended for testing purposes, but it could also be used on systems with a buggy or poorly function AGP implementation. Default: off.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: Radoslaw Kapitan, Mark Vojkovich, and also David Dawes, Guy Desbief, Dirk Hohndel, Doug Merritt, Andrew E. Mileski, Andrew van der Stock, Leonard N. Zubkoff, Andrew C. Aitchison.</p>
