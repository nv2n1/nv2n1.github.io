---
title: "sisusb(4)"
name: "sisusb"
section: "4"
letter: "s"
url: "/docs/linux/man/4-sisusb/"
description: "sisusb – SiS USB video driver"
---

<p>sisusb &#8211; SiS USB video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;sisusb&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>sisusb</code> is an Xorg driver for SiS (Silicon Integrated Systems) video chips that are connected via a Net2280-based USB dongle. The driver is not accelerated, but provides support for colordepths of 8, 16 and 24 bpp as well as Render and other extensions.</p>
<h2>Supported Hardware</h2>
<p>The <code>sisusb</code> driver supports USB video cards based on the following chipsets: </p>
<p> <code>SiS315E/PRO</code> </p>
<p> The SiS315E/PRO features two CRT controllers. However, in its USB version, only the first output, referred to as &quot;CRT1&quot;, is being used.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and to <a href="/docs/linux/man/4-sis/">sis</a>(4) for more information. This manpage only covers a subset of the supported options. </p>
<p> Detailed information on all supported options can be obtained at <a rel="nofollow" href="http://www.winischhofer.at/linuxsisusbvga.shtml">http://www.winischhofer.at/linuxsisusbvga.shtml</a> </p>
<p> Please note that this driver requires a Linux kernel driver as well which is included in Linux 2.6.12 and later, as well as available at the aforementioned website. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;HWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable the hardware cursor. It is not recommended to disable the hardware cursor as this will increase the amount of data transferred over the USB. Default: HWCursor is on.</p>
<dt><code>Option &#34;SWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>The opposite of HWCursor. This enables or disables the software cursor. This sort of cursor is slower because the pointer must be painted into the graphics display. This increases the amount of data transferred over the USB significantly. Default: SWCursor is off.</p>
<dt><code>Option &#34;CRT1Gamma&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable gamma correction. Default: Gamma correction is on.</p>
<dt><code>Option &#34;DisconnectTimeout&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This option determines how the driver will react to a disconnection of the USB device. If the integer supplied is -1, the driver will abort the X server immediately upon disconnection. If the value given is 0, the driver will probe for a re-connection every 2 seconds and in case the device is detected, re-establish the display. If the value is greater than 0, the driver will do this re-probing within the given number of seconds and abort the server if it does not detect the device within this time-out. Default: 0 (probe forever for device reconnection).</dl>
<h2>Known Bugs</h2>
<p>none.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/4-sis/">sis</a>(4) </p>
<p> <code><a rel="nofollow" href="http://www.winischhofer.at/linuxsisvga.shtml">http://www.winischhofer.at/linuxsisvga.shtml</a></code> for more information and updates</p>
<h2>Authors</h2>
<p>Author: Thomas Winischhofer</p>
