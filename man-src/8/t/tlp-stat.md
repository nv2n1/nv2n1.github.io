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
<dt><code>-b, &#8211;battery</code></dt>
<dd>Show battery data. </dd>
<dt><code>-c, &#8211;config</code></dt>
<dd>Show configuration. </dd>
<dt><code>-d, &#8211;disk</code></dt>
<dd>Show disk data. </dd>
<dt><code>-e, &#8211;pcie</code></dt>
<dd>Show PCI(e) device data. </dd>
<dt><code>-p, &#8211;processor</code></dt>
<dd>Show processor data. </dd>
<dt><code>-r, &#8211;rfkill</code></dt>
<dd>Show radio device data. </dd>
<dt><code>-s, &#8211;system</code></dt>
<dd>Show system information. </dd>
<dt><code>-t, &#8211;temp</code></dt>
<dd>Show temperatures and fan speed. </dd>
<dt><code>-u, &#8211;usb</code></dt>
<dd>Show USB device data. </dd>
<dt><code>-w, &#8211;warn</code></dt>
<dd>Show warnings. </dd>
<dt><code>-P, &#8211;pev</code></dt>
<dd>Monitor power supply udev events. </dd>
<dt><code>-T, &#8211;trace</code></dt>
<dd>Show trace output. </dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Be more verbose. </dd>
</dl>
<h2>Files</h2>
<p><i>/etc/default/tlp</i></p>
<dl>
<dd>System configuration file containing all power management settings. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tlp/">tlp</a></code>(8). </p>
<h2>Author</h2>
<p>Thomas Koch &lt;linrunner at gmx.net&gt;</p>
