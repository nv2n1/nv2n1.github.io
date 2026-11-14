---
title: "trident(4)"
name: "trident"
section: "4"
letter: "t"
url: "/docs/linux/man/4-trident/"
description: "trident – Trident video driver"
---

<p>trident &#8211; Trident video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;trident&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>trident</code> is an Xorg driver for Trident video cards. The driver is accelerated, and provides support for the following framebuffer depths: 1, 4, 8, 15, 16, and 24. Multi-head configurations are supported. The XvImage extension is supported on TGUI96xx and greater cards.</p>
<h2>Supported Hardware</h2>
<p>The <code>trident</code> driver supports PCI,AGP and ISA video cards based on the following Trident chips:</p>
<dl>
<dt><code>Blade</code></p>
<dd>Blade3D, CyberBlade series i1, i7 (DSTN), i1, i1 (DSTN), Ai1, Ai1 (DSTN), CyberBlade/e4, CyberBladeXP, CyberBladeAi1/XP, BladeXP</p>
<dt><code>Image</code></p>
<dd>3DImage975, 3DImage985, Cyber9520, Cyber9525, Cyber9397, Cyber9397DVD</p>
<dt><code>ProVidia</code></p>
<dd>9682, 9685, Cyber9382, Cyber9385, Cyber9388</p>
<dt><code>TGUI</code></p>
<dd>9440AGi, 9660, 9680</p>
<dt><code>ISA/VLBus</code></p>
<dd>8900C, 8900D, 9000, 9200CXr, Cyber9320, 9400CXi, 9440AGi These cards have been ported but need further testing and may not work.</dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;SWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable the SW cursor. Default: off.</p>
<dt><code>Option &#34;NoAccel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option &#34;PciRetry&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable PCI retries. Default: off.</p>
<dt><code>Option &#34;CyberShadow&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>For Cyber chipsets only, turn off shadow registers. If you only see a partial display &#8211; this may be the option for you. Default: on.</p>
<dt><code>Option &#34;CyberStretch&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>For Cyber chipsets only, turn on stretching. When the resolution is lower than the LCD&#8217;s screen, this option will stretch the graphics mode to fill the entire LCD. Default: off.</p>
<dt><code>Option &#34;ShadowFB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. Default: off.</p>
<dt><code>Option &#34;VideoKey&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This sets the default pixel value for the YUV video overlay key. Default: undefined.</p>
<dt><code>Option &#34;TVChipset&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>This sets the TV chipset. Options are CH7005 or VT1621. Default: off.</p>
<dt><code>Option &#34;TVSignal&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This sets the TV signalling. Options are 0 for NTSC or 1 for PAL. Default: undefined.</p>
<dt><code>Option &#34;NoPciBurst&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Turn off PCI burst mode, PCI Bursting is on by default. Default: off.</p>
<dt><code>Option &#34;XvHsync&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Override the default Horizontal-sync value for the Xv extension. This is used to center the Xv image on the screen. By default the values are assigned based on the video card. Default: 0.</p>
<dt><code>Option &#34;XvVsync&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Override the default Vertical-sync value for the Xv extension. This is used to center the Xv image on the screen. By default the values are assigned based on the video card. Default: 0.</p>
<dt><code>Option &#34;XvBskew&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Override the default Bottom skew value for the Xv extension. This is used to extend the Xv image on the screen at the bottom. By default the values are assigned based on the video card. Default: 0.</p>
<dt><code>Option &#34;XvRskew&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Override the default Right skew value for the Xv extension. This is used to extend the Xv image on the screen at the right. By default the values are assigned based on the video card. Default: 0.</p>
<dt><code>Option &#34;Display&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Override the display. Possible values are &#34;CRT&#34;, &#34;LCD&#34; and &#34;Dual&#34;. Please note that this option is only experimentally. Default: Use display active when X started.</p>
<dt><code>Option &#34;Display1400&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Inform driver to expect 1400&#215;1050 display instead of a 1280&#215;1024. Default: off.</p>
<dt><code>Option &#34;GammaBrightness&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Set display gamma value and brightness. &#34;<i>string</i>&#34; is &#34;<i>gamma</i>, <i>brightness</i>&#34;, where <i>gamma</i> is a floating point value greater than 0 and less or equal to 10. <i>brightness</i> is an integer value greater or equal to 0 and less than 128. Default: gamma and brightness control is turned off. Note: This is not supported on all chipsets. <code>Option &#34;AccelMethod&#34; &#34;</code><i>string</i><code>&#34;</code> Choose acceleration architecture, either &quot;XAA&quot; or &quot;EXA&quot;. XAA is the old (but stable) XFree86 based acceleration architecture. EXA is a newer and simpler acceleration architecture designed to better accelerate the X Render extension. Default: &quot;XAA&quot;.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Author</h2>
<p>Author: Alan Hourihane, EXA for Blade chips by Jesse Barnes</p>
