---
title: "superhyway_add_device(9)"
name: "superhyway_add_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-superhyway_add_device/"
description: "superhyway_add_device – Add a SuperHyway module"
---

<p>superhyway_add_device &#8211; Add a SuperHyway module</p>
<h2>Synopsis</h2>
<pre><code>int superhyway_add_device(unsigned long base, struct superhyway_device *sdev, struct superhyway_bus *bus);</code></pre>
<h2>Arguments</h2>
<p><i>base</i></p>
<dl>
<dd>
<dd>Physical address where module is mapped.</dl>
<p> <i>sdev</i></p>
<dl>
<dd>SuperHyway device to add, or NULL to allocate a new one.</dl>
<p> <i>bus</i></p>
<dl>
<dd>Bus where SuperHyway module resides.</dl>
<h2>Description</h2>
<p>This is responsible for adding a new SuperHyway module. This sets up a new struct superhyway_device for the module being added if <i>sdev</i> == NULL. </p>
<p> Devices are initially added in the order that they are scanned (from the top-down of the memory map), and are assigned an ID based on the order that they are added. Any manual addition of a module will thus get the ID after the devices already discovered regardless of where it resides in memory. </p>
<p> Further work can and should be done in <code>superhyway_scan_bus</code>, to be sure that any new modules are properly discovered and subsequently registered.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
