---
title: "vesa(4)"
name: "vesa"
section: "4"
letter: "v"
url: "/docs/linux/man/4-vesa/"
description: "vesa – Generic VESA video driver"
---

<p>vesa &#8211; Generic VESA video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;vesa&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>vesa</code> is an Xorg driver for generic VESA video cards. It can drive most VESA-compatible video cards, but only makes use of the basic standard VESA core that is common to these cards. The driver supports depths 8, 15 16 and 24.</p>
<h2>Supported Hardware</h2>
<p>The <code>vesa</code> driver supports most VESA-compatible video cards. There are some known exceptions, and those should be listed here.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The driver auto-detects the presence of VESA-compatible hardware. The <code>ChipSet</code> name may optionally be specified in the config file <code>&#34;Device&#34;</code> section, and will override the auto-detection: </p>
<dl>
<dd>&quot;vesa&quot;</dl>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;ShadowFB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. Default: on. </p>
<p> This option is recommended for performance reasons.</p>
<dt><code>Option &#34;ModeSetClearScreen&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Clear the screen on mode set. Some BIOSes seem to be broken in the sense that the newly set video mode is bogus if they are asked to clear the screen during mode setting. If you experience problems try to turn this option off. Default: on. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: Paulo Ce&#8217;sar Pereira de Andrade.</p>
