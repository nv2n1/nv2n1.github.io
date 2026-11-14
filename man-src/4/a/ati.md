---
title: "ati(4)"
name: "ati"
section: "4"
letter: "a"
url: "/docs/linux/man/4-ati/"
description: "ati – ATI video driver"
---

<p>ati &#8211; ATI video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;ati&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>ati</code> is an Xorg wrapper driver for ATI video cards. It autodetects whether your hardware has a Radeon, Rage 128, or Mach64 or earlier class of chipset, and loads the <a href="/docs/linux/man/4-radeon/">radeon</a>(4), <a href="/docs/linux/man/4-r128/">r128</a>(4), or mach64 driver as appropriate.</p>
<h2>Supported Hardware</h2>
<p>The <code>ati</code> driver supports Radeon, Rage 128, and Mach64 and earlier chipsets by loading those drivers. See those manpages for specific cards supported.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details, and the specific card driver for driver configuration details.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/4-r128/">r128</a>(4), <a href="/docs/linux/man/4-radeon/">radeon</a>(4)</p>
<h2>Authors</h2>
<p>See the individual driver pages for authors.</p>
