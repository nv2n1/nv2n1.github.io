---
title: "tlp-stat(8)"
name: "tlp-stat"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tlp-stat/"
description: "tlp-stat – show power management settings"
---

<p>tlp-stat &#8211; show power management settings</p>
<h2>Synopsis</h2>
<p><code>tlp-stat </code><i>[option]</i> </p>
<h2>Description</h2>
<p>This command shows the configuration, affected power management settings and additional system info. </p>
<h2>Options</h2>
<dl>
<dt><code>-b, &#8211;battery</code></p>
<dd>Show battery data. </p>
<dt><code>-c, &#8211;config</code></p>
<dd>Show configuration. </p>
<dt><code>-d, &#8211;disk</code></p>
<dd>Show disk data. </p>
<dt><code>-e, &#8211;pcie</code></p>
<dd>Show PCI(e) device data. </p>
<dt><code>-p, &#8211;processor</code></p>
<dd>Show processor data. </p>
<dt><code>-r, &#8211;rfkill</code></p>
<dd>Show radio device data. </p>
<dt><code>-s, &#8211;system</code></p>
<dd>Show system information. </p>
<dt><code>-t, &#8211;temp</code></p>
<dd>Show temperatures and fan speed. </p>
<dt><code>-u, &#8211;usb</code></p>
<dd>Show USB device data. </p>
<dt><code>-w, &#8211;warn</code></p>
<dd>Show warnings. </p>
<dt><code>-P, &#8211;pev</code></p>
<dd>Monitor power supply udev events. </p>
<dt><code>-T, &#8211;trace</code></p>
<dd>Show trace output. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Be more verbose. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/default/tlp</i></p>
<dl>
<dd>System configuration file containing all power management settings. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tlp/">tlp</a></code>(8). </p>
<h2>Author</h2>
<p>Thomas Koch &lt;linrunner at gmx.net&gt;</p>
