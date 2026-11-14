---
title: "vmmouse(4)"
name: "vmmouse"
section: "4"
letter: "v"
url: "/docs/linux/man/4-vmmouse/"
description: "vmmouse – VMware Mouse input driver"
---

<p>vmmouse &#8211; VMware Mouse input driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>idevname</i><code>&#34;</code>
<code> Driver &#34;vmmouse&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>vmmouse</code> is an XFree86 input driver for mice. The driver supports most available mouse types and interfaces. USB mice are only supported on some OSs, and the level of support for PS/2 mice depends on the OS. </p>
<p> The <code>vmmouse</code> driver functions as a pointer input device, and may be used as the X server&#8217;s core pointer. Multiple mice are supported by multiple instances of this driver.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> The driver will automatically detect if the vmmouse device is present and if it is not, it will load the regular <code>mouse</code> driver and attempt to fall back to it. There are no <code>vmmouse</code> specific options, but if you set <code><a href="/docs/linux/man/4-mouse/">mouse</a>(4)</code> options, they will be passed on. </p>
<p> See the <code><a href="/docs/linux/man/4-mouse/">mouse</a>(4)</code> man page for details on these options.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/4-mouse/">mouse</a>(4)</p>
<h2>Authors</h2>
<p>Copyright (c) 1999-2007 VMware, Inc.</p>
