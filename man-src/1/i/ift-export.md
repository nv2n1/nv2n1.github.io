---
title: "ift-export(1)"
name: "ift-export"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ift-export/"
description: "ift-export.info – ift-export.info"
---

<h2>NAME</h2>
<p> ift-export.info &#8211; ift-export.info</p>
<h2>Built-in iSight firmware export</h2>
<p> ift-export export a Built-in iSight firmware produced by ift-extract and convert it to Intel <font SIZE="-1">HEX</font> file. Note that Apple Built-in iSight seems to have extende on-chip memory. This case is not handled by fxload and thus, not allowing to load the Intel <font SIZE="-1">HEX</font> file into the chip. Use ift-load to load directly the binary firmware on-chip. </p>
<p> * Menu: </p>
<p> Command line options: see &#8220;Options&#8221; </p>
<p> See also &#8220;Copying&#8221;</p>
<h2>1 Command line options</h2>
<p> `<code>-i</code>&#8216; `<code>&#8211;input-firmware</code>&#8216; Driver filename to export to Intel <font SIZE="-1">HEX</font> file. </p>
<p> `<code>-o</code>&#8216; `<code>&#8211;output</code>&#8216; The output Intel <font SIZE="-1">HEX</font> filename. </p>
<p> `<code>-?</code>&#8216; `<code>&#8211;help</code>&#8216; Shows option help and quit.</p>
<h2>2 Copying</h2>
<p> isight-firmware-tools is a project developped by Étienne Bersac based on the work of Ronald S. Bultje, Johannes Berg and Ivan N. Zlatev. </p>
<p> This manual has been written by Étienne Bersac. </p>
<p> Copyright (C) 2007 Étienne Bersac </p>
<h2>Index</h2>
