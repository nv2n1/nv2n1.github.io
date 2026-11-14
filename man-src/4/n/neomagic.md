---
title: "neomagic(4)"
name: "neomagic"
section: "4"
letter: "n"
url: "/docs/linux/man/4-neomagic/"
description: "neomagic – Neomagic video driver"
---

<p>neomagic &#8211; Neomagic video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;neomagic&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>neomagic </code> is an Xorg driver for the Neomagic graphics chipsets found in many laptop computers.</p>
<h2>Supported Hardware</h2>
<p><code>neomagic</code> supports the following chipsets: </p>
<dl>
<dt>MagicGraph 128 (NM2070)</p>
<dd>
<dt>MagicGraph 128V (NM2090)</p>
<dd>
<dt>MagicGraph 128ZV (NM2093)</p>
<dd>
<dt>MagicGraph 128ZV+ (NM2097)</p>
<dd>
<dt>MagicGraph 128XD (NM2160)</p>
<dd>
<dt>MagicGraph 256AV (NM2200)</p>
<dd>
<dt>MagicGraph 256AV+ (NM2230)</p>
<dd>
<dt>MagicGraph 256ZX (NM2360)</p>
<dd>
<dt>MagicGraph 256XL+ (NM2380)</p>
<dd></dl>
<p> The driver supports depths 8, 15, 16 and 24 for all chipsets except the NM2070 which does not support depth 24. All depths are accelerated except for depth 24 which is only accelerated on NM2200 and newer models. All visuals are supported in depth 8. TrueColor and DirectColor visuals are supported in the other depths.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported</p>
<dl>
<dt><code>Option &#34;NoAccel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option &#34;SWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable software cursor. Default: software cursor is disable and a hardware cursor is used.</p>
<dt><code>Option &#34;PCIBurst&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable PCI burst modes. Default: enabled.</p>
<dt><code>Option &#34;Rotate&#34; &#34;CW&#34;</code></p>
<dd>
<dt><code>Option &#34;Rotate&#34; &#34;CCW&#34;</code></p>
<dd>Rotate the display clockwise or counterclockwise. This mode is unaccelerated. Default: no rotation.</p>
<dt><code>Option &#34;ShadowFB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. Default: off.</p>
<dt><code>Option &#34;OverlayMem&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Reserve the given amount of memory (in bytes) for the XVideo overlay. On boards with limited memory, display of large XVideo buffers might fail due to insufficient available memory. Using this option solves the problem at the expense of reducing the memory available for other operations. For full-resolution DVDs, 829440 bytes (720x576x2) are necessary.</dl>
<p> <code>Note</code><br />
 On some laptops using the 2160 chipset (MagicGraph 128XD) the following options are needed to avoid a lock-up of the graphic engine: </p>
<pre> Option &quot;XaaNoScanlineImageWriteRect&quot;
 Option &quot;XaaNoScanlineCPUToScreenColorExpandFill&quot;</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: Jens Owen, Kevin E. Martin, and also Egbert Eich, Mark Vojkovich, Alan Hourihane.</p>
